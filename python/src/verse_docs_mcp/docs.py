"""Query the packaged SQLite FTS5 documentation index.

Port of ``grounding_engine/src/docs.rs``.
"""

from __future__ import annotations

import importlib.resources
import os
import re
import shutil
import sqlite3
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx

# ---------------------------------------------------------------------------
# Constants (match Rust defaults)
# ---------------------------------------------------------------------------

DEFAULT_LIMIT = 5
MAX_LIMIT = 10
DEFAULT_OFFSET = 0
DEFAULT_MAX_FETCHES = 3
MAX_FETCHES = 5
MAX_CONTENT_CHARS = 16_000
MAX_FETCHED_TEXT_CHARS = 12_000

STOP_WORDS = frozenset(
    "a an and are find for from how in is latest me of on or show the to what with".split()
)

DOCS_DIR_NAME = ".vm"
DOCS_DB_FILE_NAME = "verse-docs.db"

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class DocsQueryOptions:
    limit: int | None = None
    offset: int | None = None
    fetch_source_urls: bool = False
    max_fetches: int | None = None


@dataclass
class DocsQueryResult:
    title: str = ""
    path: str = ""
    source_url: str = ""
    doc_type: str = ""
    snippet: str = ""
    content: str = ""
    content_truncated: bool = False
    score: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "path": self.path,
            "source_url": self.source_url,
            "doc_type": self.doc_type,
            "snippet": self.snippet,
            "content": self.content,
            "content_truncated": self.content_truncated,
            "score": self.score,
        }


@dataclass
class DocsQueryPagination:
    limit: int = DEFAULT_LIMIT
    offset: int = DEFAULT_OFFSET
    returned: int = 0
    has_more: bool = False
    next_offset: int | None = None

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "limit": self.limit,
            "offset": self.offset,
            "returned": self.returned,
            "has_more": self.has_more,
        }
        if self.next_offset is not None:
            d["next_offset"] = self.next_offset
        return d


@dataclass
class FetchedSource:
    url: str = ""
    status: str = ""
    content_type: str = ""
    title: str | None = None
    text: str = ""
    truncated: bool = False
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "url": self.url,
            "status": self.status,
            "content_type": self.content_type,
            "title": self.title,
            "text": self.text,
            "truncated": self.truncated,
        }
        if self.error is not None:
            d["error"] = self.error
        return d


@dataclass
class DocsQueryResponse:
    query: str = ""
    normalized_query: str = ""
    pagination: DocsQueryPagination = field(default_factory=DocsQueryPagination)
    results: list[DocsQueryResult] = field(default_factory=list)
    fetched_sources: list[FetchedSource] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "normalized_query": self.normalized_query,
            "pagination": self.pagination.to_dict(),
            "results": [r.to_dict() for r in self.results],
            "fetched_sources": [f.to_dict() for f in self.fetched_sources],
            "warnings": self.warnings,
        }


# ---------------------------------------------------------------------------
# DB path resolution
# ---------------------------------------------------------------------------

_materialized_db_path: Path | None = None


def _home_dir() -> Path:
    home = os.environ.get("HOME") or os.environ.get("USERPROFILE") or ""
    if not home:
        raise RuntimeError("could not determine home directory for docs cache")
    return Path(home)


def _docs_cache_dir() -> Path:
    return _home_dir() / DOCS_DIR_NAME


def _materialize_embedded_db() -> Path:
    """Extract the packaged DB to ``~/.vm/verse-docs.db`` (skip if size matches)."""
    cache_dir = _docs_cache_dir()
    cache_dir.mkdir(parents=True, exist_ok=True)
    final_path = cache_dir / DOCS_DB_FILE_NAME

    pkg_data = importlib.resources.files("verse_docs_mcp") / "data" / DOCS_DB_FILE_NAME
    with importlib.resources.as_file(pkg_data) as pkg_file:
        pkg_size = pkg_file.stat().st_size
        if final_path.exists() and final_path.stat().st_size == pkg_size:
            return final_path
        tmp_path = final_path.with_suffix(f".{os.getpid()}.{time.time_ns()}.tmp")
        shutil.copy2(pkg_file, tmp_path)

    if final_path.exists():
        final_path.unlink(missing_ok=True)
    tmp_path.rename(final_path)
    return final_path


def _docs_db_path(db_override: Path | None = None) -> Path:
    if db_override is not None:
        return db_override
    global _materialized_db_path  # noqa: PLW0603
    if _materialized_db_path is not None:
        return _materialized_db_path
    _materialized_db_path = _materialize_embedded_db()
    return _materialized_db_path


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------


def _open_db(path: Path) -> sqlite3.Connection:
    if not path.exists():
        raise FileNotFoundError(f"docs database not found at {path}")
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    _ensure_schema(conn)
    return conn


def _ensure_schema(conn: sqlite3.Connection) -> None:
    cols = _table_columns(conn, "docs")
    if not cols:
        raise RuntimeError("docs database is missing required table: docs")
    for required in ("id", "title", "path"):
        if required not in cols:
            raise RuntimeError(f"docs database is missing required docs column: {required}")
    fts_cols = _table_columns(conn, "docs_fts")
    if not fts_cols:
        raise RuntimeError("docs database is missing required table: docs_fts")


def _table_columns(conn: sqlite3.Connection, table: str) -> list[str]:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return [row[1] for row in rows]


# ---------------------------------------------------------------------------
# Search plan (adapts to schema variations)
# ---------------------------------------------------------------------------


class _SearchPlan:
    def __init__(self, conn: sqlite3.Connection) -> None:
        docs_cols = _table_columns(conn, "docs")
        fts_cols = _table_columns(conn, "docs_fts")

        if "source_url" in docs_cols:
            self.source_url_expr = "COALESCE(d.source_url, '')"
        else:
            self.source_url_expr = "''"

        path_doc_type = (
            "CASE "
            "WHEN d.path LIKE 'verse-api-pages-canonical/%' THEN 'api' "
            "WHEN d.path LIKE 'fortnite-docs-pages-canonical/%' THEN 'guide' "
            "WHEN d.path LIKE 'assets/%.digest.verse' THEN 'digest' "
            "ELSE 'doc' END"
        )
        if "doc_type" in docs_cols:
            self.doc_type_expr = f"COALESCE(NULLIF(d.doc_type, ''), {path_doc_type})"
        else:
            self.doc_type_expr = path_doc_type

        self.snippet_col_idx = fts_cols.index("content") if "content" in fts_cols else 0

    def search_sql(self) -> str:
        return (
            "SELECT d.title, d.path, "
            f"{self.source_url_expr} AS source_url, "
            f"{self.doc_type_expr} AS doc_type, "
            f"snippet(docs_fts, {self.snippet_col_idx}, '[', ']', '...', 24) AS snippet, "
            "d.content, bm25(docs_fts) AS score "
            "FROM docs_fts "
            "JOIN docs d ON d.id = docs_fts.rowid "
            "WHERE docs_fts MATCH ?1 "
            "ORDER BY score ASC "
            "LIMIT ?2 OFFSET ?3"
        )

    def count_sql(self) -> str:
        return (
            "SELECT COUNT(*) FROM docs_fts "
            "JOIN docs d ON d.id = docs_fts.rowid "
            "WHERE docs_fts MATCH ?1"
        )


# ---------------------------------------------------------------------------
# Query logic
# ---------------------------------------------------------------------------

_FTS_EXPLICIT_RE = re.compile(r'["\s](OR|AND|NOT|NEAR)\s|"')


def _normalize_query(query: str) -> str:
    normalized = " ".join(query.split())
    if not normalized:
        raise ValueError("query must be a non-empty string")
    return normalized


def _looks_like_fts(query: str) -> bool:
    return bool(_FTS_EXPLICIT_RE.search(query))


def _build_fts_query(query: str) -> str:
    if _looks_like_fts(query):
        return query

    seen: set[str] = set()
    terms: list[str] = []
    for raw in re.split(r"[^\w]", query):
        if not raw:
            continue
        term = raw.lower()
        if len(term) < 2 or term in STOP_WORDS:
            continue
        if term not in seen:
            seen.add(term)
            terms.append(term)

    if not terms:
        raise ValueError("query did not contain searchable terms")

    joiner = " " if len(terms) <= 3 else " OR "
    return joiner.join(terms)


def _clamp_limit(limit: int | None) -> int:
    return max(1, min(limit or DEFAULT_LIMIT, MAX_LIMIT))


def _clamp_offset(offset: int | None) -> int:
    return offset or DEFAULT_OFFSET


def _clamp_fetches(max_fetches: int | None) -> int:
    return max(0, min(max_fetches if max_fetches is not None else DEFAULT_MAX_FETCHES, MAX_FETCHES))


def _truncate_text(text: str, max_chars: int) -> tuple[str, bool]:
    if len(text) <= max_chars:
        return text, False
    return text[:max_chars].rstrip() + "…", True


def _normalize_snippet(snippet: str) -> str:
    return " ".join(snippet.split())


def _normalize_content(content: str) -> str:
    return content.replace("\r\n", "\n").replace("\r", "\n").strip()


# ---------------------------------------------------------------------------
# Public query API
# ---------------------------------------------------------------------------


def query_docs(
    query: str,
    options: DocsQueryOptions | None = None,
    *,
    db_override: Path | None = None,
) -> DocsQueryResponse:
    """Search the docs index and return ranked results."""
    if options is None:
        options = DocsQueryOptions()

    normalized_query = _normalize_query(query)
    fts_query = _build_fts_query(normalized_query)
    db_path = _docs_db_path(db_override)
    conn = _open_db(db_path)

    limit = _clamp_limit(options.limit)
    offset = _clamp_offset(options.offset)
    max_fetches = _clamp_fetches(options.max_fetches)

    plan = _SearchPlan(conn)

    total: int = conn.execute(plan.count_sql(), (fts_query,)).fetchone()[0]

    rows = conn.execute(plan.search_sql(), (fts_query, limit, offset)).fetchall()
    results: list[DocsQueryResult] = []
    for row in rows:
        raw_content = _normalize_content(row[5] or "")
        content_text, content_truncated = _truncate_text(raw_content, MAX_CONTENT_CHARS)
        results.append(
            DocsQueryResult(
                title=row[0],
                path=row[1],
                source_url=row[2],
                doc_type=row[3],
                snippet=_normalize_snippet(row[4] or ""),
                content=content_text,
                content_truncated=content_truncated,
                score=row[6],
            )
        )

    conn.close()

    warnings: list[str] = []
    fetched_sources: list[FetchedSource] = []
    if options.fetch_source_urls:
        fetched_sources = _fetch_sources(results, max_fetches, warnings)
        warnings.append(f"Fetched up to {max_fetches} source URLs for this query.")

    returned = len(results)
    has_more = offset + returned < total
    next_offset = (offset + returned) if has_more else None

    return DocsQueryResponse(
        query=query,
        normalized_query=normalized_query,
        pagination=DocsQueryPagination(
            limit=limit,
            offset=offset,
            returned=returned,
            has_more=has_more,
            next_offset=next_offset,
        ),
        results=results,
        fetched_sources=fetched_sources,
        warnings=warnings,
    )


# ---------------------------------------------------------------------------
# Format
# ---------------------------------------------------------------------------


def format_query_response(response: DocsQueryResponse) -> str:
    if not response.results:
        return f'No documentation matches found for "{response.normalized_query}".'

    parts: list[str] = []
    parts.append(
        f'Found {response.pagination.returned} documentation match(es) '
        f'for "{response.normalized_query}" '
        f'(offset {response.pagination.offset}, limit {response.pagination.limit}).'
    )
    if response.pagination.has_more and response.pagination.next_offset is not None:
        parts.append(
            f"More results available. Use offset={response.pagination.next_offset} to continue."
        )
    if response.fetched_sources:
        parts.append(
            f"Fetched {len(response.fetched_sources)} linked source page(s) for enrichment."
        )
    for warning in response.warnings:
        parts.append(f"Warning: {warning}")

    for i, result in enumerate(response.results):
        if i > 0:
            parts.append("\n\n--------------------------------\n")
        parts.append(f"### {result.title}")
        parts.append(f"Path: {result.path}")
        if result.source_url:
            parts.append(f"Source: {result.source_url}")
        if result.doc_type:
            parts.append(f"Type: {result.doc_type}")
        parts.append(f"Score: {result.score:.4f}")
        parts.append("")
        parts.append(f"Snippet: {result.snippet}")
        parts.append("")
        parts.append(result.content)
        if result.content_truncated:
            parts.append("\n[content truncated]")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Source fetching
# ---------------------------------------------------------------------------


def fetch_doc_source(url: str) -> FetchedSource:
    """Fetch and normalize one documentation source URL."""
    url = url.strip()
    if not url:
        raise ValueError("url must be a non-empty string")
    return _fetch_one(url)


def _fetch_sources(
    results: list[DocsQueryResult],
    max_fetches: int,
    warnings: list[str],
) -> list[FetchedSource]:
    if max_fetches == 0:
        warnings.append(
            "Source URL fetching was requested with max_fetches=0, so no links were fetched."
        )
        return []

    fetched: list[FetchedSource] = []
    for result in results:
        if not result.source_url:
            continue
        fetched.append(_fetch_one(result.source_url))
        if len(fetched) >= max_fetches:
            break
    return fetched


def _fetch_one(url: str) -> FetchedSource:
    try:
        resp = httpx.get(url, timeout=10.0, follow_redirects=True)
        content_type = resp.headers.get("content-type", "")
        title = _extract_html_title(resp.text)
        normalized = " ".join(resp.text.split())
        text, truncated = _truncate_text(normalized, MAX_FETCHED_TEXT_CHARS)
        return FetchedSource(
            url=url,
            status=str(resp.status_code),
            content_type=content_type,
            title=title,
            text=text,
            truncated=truncated,
        )
    except Exception as exc:
        return FetchedSource(
            url=url,
            status="request_failed",
            content_type="",
            text="",
            error=str(exc),
        )


def _extract_html_title(body: str) -> str | None:
    lower = body.lower()
    start = lower.find("<title>")
    if start == -1:
        return None
    end = lower.find("</title>", start + 7)
    if end == -1:
        return None
    title = body[start + 7 : end].strip()
    return title if title else None
