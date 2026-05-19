"""CLI entry-point for ``verse-docs-mcp``."""

from __future__ import annotations

import argparse
import json
import sys


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="verse-docs-mcp",
        description="Verse Docs MCP Server — query Verse/Fortnite UEFN documentation.",
    )
    parser.add_argument("--version", action="store_true", help="Print version and exit.")
    sub = parser.add_subparsers(dest="command")

    # serve -------------------------------------------------------------------
    serve_parser = sub.add_parser("serve", help="Start the MCP server.")
    serve_parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="Transport type (default: stdio).",
    )
    serve_parser.add_argument("--host", default="127.0.0.1", help="HTTP host (default: 127.0.0.1).")
    serve_parser.add_argument("--port", type=int, default=2003, help="HTTP port (default: 2003).")

    # index -------------------------------------------------------------------
    index_parser = sub.add_parser("index", help="Build the SQLite FTS5 docs database.")
    index_parser.add_argument("--docs-root", help="Repository root containing docs directories.")
    index_parser.add_argument("--output", required=True, help="Output SQLite database path.")

    # query -------------------------------------------------------------------
    query_parser = sub.add_parser("query", help="Run a docs query from the CLI.")
    query_parser.add_argument("query_text", help="Search query string.")
    query_parser.add_argument("--limit", type=int, default=5)
    query_parser.add_argument("--offset", type=int, default=0)
    query_parser.add_argument("--db", help="Path to a docs database file (overrides packaged DB).")

    args = parser.parse_args(argv)

    if args.version:
        from verse_docs_mcp import __version__

        print(f"verse-docs-mcp {__version__}")
        return

    if args.command is None:
        # Default: run as MCP stdio server
        _run_serve(transport="stdio", host="127.0.0.1", port=2003)
        return

    if args.command == "serve":
        _run_serve(transport=args.transport, host=args.host, port=args.port)
    elif args.command == "index":
        _run_index(docs_root=args.docs_root, output=args.output)
    elif args.command == "query":
        _run_query(query_text=args.query_text, limit=args.limit, offset=args.offset, db_path=args.db)
    else:
        parser.print_help()


def _run_serve(*, transport: str, host: str, port: int) -> None:
    from verse_docs_mcp.server import create_server

    server = create_server()
    if transport == "http":
        server.settings.host = host
        server.settings.port = port
        server.run(transport="streamable-http")
    else:
        server.run(transport="stdio")


def _run_index(*, docs_root: str | None, output: str) -> None:
    from pathlib import Path

    from verse_docs_mcp.index import build_database, find_repo_root

    root = Path(docs_root) if docs_root else find_repo_root()
    if root is None:
        print("ERROR: could not locate docs root. Pass --docs-root explicitly.", file=sys.stderr)
        sys.exit(1)
    build_database(root, Path(output))
    print(f"Built docs database at {output}")


def _run_query(*, query_text: str, limit: int, offset: int, db_path: str | None) -> None:
    from pathlib import Path

    from verse_docs_mcp.docs import DocsQueryOptions, format_query_response, query_docs

    db = Path(db_path) if db_path else None
    options = DocsQueryOptions(limit=limit, offset=offset)
    response = query_docs(query_text, options, db_override=db)
    print(format_query_response(response))
    print(f"\n--- JSON ---\n{json.dumps(response.to_dict(), indent=2, ensure_ascii=False)}")
