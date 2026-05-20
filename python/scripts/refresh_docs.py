#!/usr/bin/env python3
"""Refetch bundled Epic documentation pages and rewrite as markdown.

This is the source-of-truth script for the weekly GitHub Actions cron at
``.github/workflows/refresh-docs.yml``. It walks every ``*.md`` file under
``python/docs/``, reads the ``## <source-url>`` header, fetches the page,
converts the ``<main>`` element to Markdown with ``markdownify``, and writes
the file back atomically.

Run locally with::

    python -m pip install httpx beautifulsoup4 markdownify
    python python/scripts/refresh_docs.py --dry-run --limit 50

Notes
-----
* ``dev.epicgames.com`` is fronted by Cloudflare. Hammering it from a single
  IP gets the IP rate-limited (HTTP 403) for hours. The defaults
  (``--concurrency 4 --delay-ms 250``) are intentionally polite. The CI cron
  uses GitHub-hosted runners which get a fresh IP each run.
* Pages that are JS-rendered (Angular shell with empty SSR) cannot be
  scraped via static HTML and are skipped — the existing on-disk content is
  preserved. ~5% of bundled pages fall in this bucket.
* The output format mirrors the original snapshot: ``## <url>`` on line 1,
  blank line, then the rendered Markdown body.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

BASE = "https://dev.epicgames.com"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}
SOURCE_RE = re.compile(r"^## (https?://\S+)\s*$", re.MULTILINE)
HOMEPAGE_TITLES = (
    "Fortnite Documentation",
    "Unreal Editor for Fortnite Documentation",
    "Epic Developer Community",
)


class _EpicConverter(MarkdownConverter):
    """Markdownify converter that resolves relative Epic URLs to absolute."""

    def convert_a(self, el, text, parent_tags=None):
        href = el.get("href", "")
        if href.startswith("/"):
            el["href"] = BASE + href
        return super().convert_a(el, text, parent_tags)


def html_to_md(html: str) -> tuple[str | None, str]:
    """Convert an Epic doc HTML page to Markdown.

    Returns ``(markdown, "ok")`` on success or ``(None, reason)`` when the
    page should be skipped (JS-rendered shell, 404 redirect, etc.).
    """
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    main = soup.find("main")
    if not h1 or not h1.get_text(strip=True):
        return None, "no_h1"
    h1_text = h1.get_text(strip=True)
    if any(h1_text.startswith(t) for t in HOMEPAGE_TITLES):
        return None, "homepage_redirect"
    if not main or len(str(main)) < 800:
        return None, "short_main"

    clone = BeautifulSoup(str(main), "html.parser")
    for sel in (
        "nav", "aside", "footer", "script", "style", "form", "button", "summary",
        ".on-this-page", ".doc-feedback", ".table-of-contents", ".breadcrumb",
        ".section-page-header__breadcrumb", ".page-meta", "[class*=breadcrumb]",
    ):
        for el in clone.select(sel):
            el.decompose()
    # Strip leading breadcrumb ordered list.
    for ol in clone.find_all("ol"):
        items = ol.find_all("li")
        if 1 <= len(items) <= 6:
            ol.decompose()

    md = _EpicConverter(
        heading_style="ATX",
        bullets="-",
        escape_underscores=False,
        escape_asterisks=False,
    ).convert_soup(clone)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    lines = md.split("\n")
    cutoff = len(lines)
    for i, line in enumerate(lines):
        if re.match(r"^- \[\S.*?\]\(https?://\S+\?query=", line):
            cutoff = min(cutoff, i)
        if "Ask questions and help your peers" in line:
            cutoff = min(cutoff, i)
        if line.strip() == "On this page" and i > 5:
            cutoff = min(cutoff, i)
    return "\n".join(lines[:cutoff]).rstrip() + "\n", "ok"


def read_source_url(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    m = SOURCE_RE.search(text)
    return m.group(1).strip() if m else None


async def _fetch_one(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    path: Path,
    url: str,
    *,
    dry_run: bool,
    delay_ms: int,
    min_size_bytes: int,
) -> dict[str, object]:
    rec: dict[str, object] = {
        "path": str(path),
        "url": url,
        "status": "?",
        "old_size": path.stat().st_size,
        "new_size": 0,
        "ms": 0,
    }
    t0 = time.time()
    try:
        async with sem:
            if delay_ms:
                await asyncio.sleep(delay_ms / 1000)
            r = await client.get(
                url, headers=HEADERS, timeout=30, follow_redirects=True
            )
        rec["http"] = r.status_code
        if r.status_code != 200:
            rec["status"] = "http_error"
            return rec
        md, reason = html_to_md(r.text)
        if md is None:
            rec["status"] = reason
            return rec
        out = f"## {url}\n\n{md}"
        rec["new_size"] = len(out.encode("utf-8"))
        if rec["new_size"] < min_size_bytes:
            rec["status"] = "too_small"
            return rec
        if not dry_run:
            tmp = path.with_suffix(path.suffix + ".tmp")
            tmp.write_text(out, encoding="utf-8")
            tmp.replace(path)
        rec["status"] = "ok"
    except Exception as e:  # noqa: BLE001 - log everything
        rec["status"] = "error"
        rec["error"] = str(e)[:200]
    finally:
        rec["ms"] = int((time.time() - t0) * 1000)
    return rec


def _collect_files(docs_root: Path) -> list[Path]:
    files: list[Path] = []
    for sub in ("verse-api-pages-canonical", "fortnite-docs-pages-canonical"):
        files.extend(sorted((docs_root / sub).rglob("*.md")))
    return files


async def run(args: argparse.Namespace) -> int:
    files = _collect_files(args.docs)
    if args.limit:
        files = files[: args.limit]
    print(f"[refresh-docs] {len(files)} markdown files to refresh", file=sys.stderr)

    sem = asyncio.Semaphore(args.concurrency)
    log_f = args.log.open("w", encoding="utf-8") if args.log else None
    counts: dict[str, int] = {}

    async with httpx.AsyncClient(http2=False) as client:
        async def task(path: Path) -> dict[str, object]:
            url = read_source_url(path)
            if not url:
                return {"path": str(path), "status": "no_source_url"}
            return await _fetch_one(
                client,
                sem,
                path,
                url,
                dry_run=args.dry_run,
                delay_ms=args.delay_ms,
                min_size_bytes=args.min_size_bytes,
            )

        coros = [task(p) for p in files]
        for i, fut in enumerate(asyncio.as_completed(coros), 1):
            rec = await fut
            if log_f:
                log_f.write(json.dumps(rec) + "\n")
            counts[rec["status"]] = counts.get(rec["status"], 0) + 1
            if i % 100 == 0 or i == len(files):
                summary = " ".join(
                    f"{k}={v}" for k, v in sorted(counts.items(), key=lambda x: -x[1])
                )
                print(f"[refresh-docs] [{i}/{len(files)}] {summary}", file=sys.stderr)

    if log_f:
        log_f.close()

    print("\n[refresh-docs] final counts:", file=sys.stderr)
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {k:20s}  {v}", file=sys.stderr)

    # Exit non-zero only when *every* fetch failed (likely WAF block).
    ok = counts.get("ok", 0)
    return 0 if ok > 0 else 2


def _build_parser() -> argparse.ArgumentParser:
    here = Path(__file__).resolve().parent
    default_docs = here.parent / "docs"
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--docs",
        type=Path,
        default=default_docs,
        help=f"bundled docs root (default: {default_docs})",
    )
    p.add_argument("--limit", type=int, default=0, help="max files (0 = all)")
    p.add_argument(
        "--concurrency",
        type=int,
        default=4,
        help="max parallel HTTP requests (Cloudflare bans high values)",
    )
    p.add_argument(
        "--delay-ms",
        type=int,
        default=250,
        help="per-request delay inside the semaphore",
    )
    p.add_argument(
        "--min-size-bytes",
        type=int,
        default=200,
        help="reject responses smaller than this many bytes",
    )
    p.add_argument(
        "--log",
        type=Path,
        default=Path("refresh-docs.log.jsonl"),
        help="write a JSONL record per file (set empty to disable)",
    )
    p.add_argument("--dry-run", action="store_true")
    return p


def main() -> int:
    args = _build_parser().parse_args()
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
