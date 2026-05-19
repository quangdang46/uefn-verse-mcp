"""Build the SQLite FTS5 documentation index from markdown sources.

Port of ``grounding_engine/build.rs`` and ``scripts/build_docs_db.py``.
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

DOCS_DIRS = (
    "verse-api-pages-canonical",
    "fortnite-docs-pages-canonical",
)
DIGEST_FILES = (
    "assets/Fortnite.digest.verse",
    "assets/UnrealEngine.digest.verse",
    "assets/Verse.digest.verse",
)
SKIP_TITLES = {"table of contents"}
JUNK_MARKERS = (
    "# 404",
    "Page not found",
    "**No document**",
    "The document you're looking for does not exist in this version.",
    "```\nNot Found\n```",
)

SOURCE_URL_RE = re.compile(r"^##\s+(https?://\S+)\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK_RE = re.compile(r"\[(.*?)\]\([^)]*\)")
COPY_SNIPPET_RE = re.compile(r"^Copy full snippet\s*$", re.MULTILINE)
BLANK_LINES_RE = re.compile(r"\n{3,}")


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

SCHEMA_SQL = """\
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
DROP TABLE IF EXISTS docs;
DROP TABLE IF EXISTS docs_fts;

CREATE TABLE docs (
    id         INTEGER PRIMARY KEY,
    path       TEXT NOT NULL UNIQUE,
    title      TEXT NOT NULL,
    content    TEXT NOT NULL,
    raw_md     TEXT NOT NULL,
    tags       TEXT NOT NULL DEFAULT '[]',
    source_url TEXT NOT NULL DEFAULT '',
    doc_type   TEXT NOT NULL DEFAULT 'doc',
    mtime      INTEGER NOT NULL DEFAULT 0
);

CREATE VIRTUAL TABLE docs_fts USING fts5(
    title,
    content,
    tags,
    content='docs',
    content_rowid='id',
    tokenize='unicode61 remove_diacritics 1'
);
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def find_repo_root() -> Path | None:
    """Walk up from this file to find the repo root (has ``verse-api-pages-canonical/``)."""
    current = Path(__file__).resolve().parent
    for _ in range(10):
        if (current / "verse-api-pages-canonical").is_dir():
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent
    return None


def _iter_indexable_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for docs_dir in DOCS_DIRS:
        docs_path = root / docs_dir
        if docs_path.is_dir():
            files.extend(sorted(docs_path.rglob("*.md")))
    for digest in DIGEST_FILES:
        digest_path = root / digest
        if digest_path.is_file():
            files.append(digest_path)
    return files


def _extract_source_url(lines: list[str]) -> str:
    for line in lines[:20]:
        m = SOURCE_URL_RE.match(line.strip())
        if m:
            return m.group(1)
    return ""


def _extract_title(path: Path, lines: list[str]) -> str:
    for line in lines:
        m = HEADING_RE.match(line.strip())
        if not m:
            continue
        heading = m.group(2).strip()
        if heading.startswith("http://") or heading.startswith("https://"):
            continue
        if heading.lower() in SKIP_TITLES:
            continue
        return heading
    return _fallback_title(path)


def _extract_digest_title(path: Path, lines: list[str]) -> str:
    for line in lines:
        stripped = line.strip()
        if "<public> := module:" in stripped:
            module_name = stripped.split("<public> := module:", 1)[0].strip()
            if module_name:
                return module_name
    return _fallback_title(path)


def _fallback_title(path: Path) -> str:
    stem = path.stem.replace("-", " ").replace("_", " ").strip()
    return stem if stem else path.name


def _derive_doc_type(relative_path: str) -> str:
    if relative_path.startswith("verse-api-pages-canonical/"):
        return "api"
    if relative_path.startswith("fortnite-docs-pages-canonical/"):
        return "guide"
    if relative_path.startswith("assets/") and relative_path.endswith(".digest.verse"):
        return "digest"
    return "doc"


def _normalize_content(raw_md: str) -> str:
    content = raw_md.replace("\r\n", "\n")
    content = SOURCE_URL_RE.sub("", content)
    content = COPY_SNIPPET_RE.sub("", content)
    content = IMAGE_RE.sub(" ", content)
    content = LINK_RE.sub(r"\1", content)
    content = BLANK_LINES_RE.sub("\n\n", content.strip())
    return content.strip()


def _normalize_digest_content(raw_md: str) -> str:
    content = raw_md.replace("\r\n", "\n")
    return BLANK_LINES_RE.sub("\n\n", content.strip()).strip()


def _is_junk_doc(raw_md: str) -> bool:
    return any(marker in raw_md for marker in JUNK_MARKERS)


def _read_doc(root: Path, path: Path) -> tuple[str, str, str, str, str, str, int] | None:
    raw_md = path.read_text(encoding="utf-8", errors="replace")
    lines = raw_md.splitlines()
    relative_path = path.relative_to(root).as_posix()
    doc_type = _derive_doc_type(relative_path)
    is_digest = path.suffix == ".verse"

    if is_digest:
        title = _extract_digest_title(path, lines)
        source_url = ""
        content = _normalize_digest_content(raw_md)
    else:
        title = _extract_title(path, lines)
        source_url = _extract_source_url(lines)
        content = _normalize_content(raw_md)

    if not is_digest and (not content or _is_junk_doc(raw_md)):
        return None

    mtime = int(path.stat().st_mtime)
    return relative_path, title, content, raw_md, source_url, doc_type, mtime


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def build_database(root: Path, output_path: Path) -> None:
    """Build the SQLite FTS5 docs database from markdown sources under *root*."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        output_path.unlink()

    conn = sqlite3.connect(str(output_path))
    try:
        conn.executescript(SCHEMA_SQL)
        files = _iter_indexable_files(root)
        rows = [row for f in files if (row := _read_doc(root, f)) is not None]
        conn.executemany(
            "INSERT INTO docs (path, title, content, raw_md, tags, source_url, doc_type, mtime) "
            "VALUES (?, ?, ?, ?, '[]', ?, ?, ?)",
            rows,
        )
        conn.execute("INSERT INTO docs_fts(docs_fts) VALUES ('rebuild')")
        conn.commit()
        conn.execute("VACUUM")
    finally:
        conn.close()
