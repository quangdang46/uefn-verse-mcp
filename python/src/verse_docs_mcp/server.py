"""FastMCP server exposing ``query-docs`` and ``fetch-doc-source`` tools.

Tool names and parameter schemas match the Rust ``mcp_server`` exactly so
existing MCP host configurations remain compatible.
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from verse_docs_mcp.docs import (
    DocsQueryOptions,
    fetch_doc_source,
    format_query_response,
    query_docs,
)


def create_server() -> FastMCP:
    """Build and return the configured FastMCP server instance."""
    mcp = FastMCP(
        "verse-mcp",
        instructions=(
            "Verse MCP Server for UEFN/Verse development. "
            "Use query-docs to search the built-in documentation index "
            "and fetch-doc-source to fetch a documentation URL."
        ),
    )

    @mcp.tool(
        name="query-docs",
        description=(
            "Search the built-in SQLite Verse/Fortnite documentation index "
            "and return ranked results with full indexed content by default, "
            "plus optional fetched source_url page content."
        ),
    )
    def tool_query_docs(
        query: str,
        limit: int | None = None,
        offset: int | None = None,
        fetch_source_urls: bool = False,
        max_fetches: int | None = None,
    ) -> str:
        """Execute a docs query and return a human-readable summary."""
        options = DocsQueryOptions(
            limit=limit,
            offset=offset,
            fetch_source_urls=fetch_source_urls,
            max_fetches=max_fetches,
        )
        try:
            response = query_docs(query, options)
            return format_query_response(response)
        except Exception as exc:
            return (
                f"query-docs failed: {exc}. Fix the query input and try again. "
                "Example queries: `editable properties`, `npc behavior`, "
                "or `creative_device AND event`."
            )

    @mcp.tool(
        name="fetch-doc-source",
        description=(
            "Fetch and normalize one documentation source URL into "
            "agent-friendly text and JSON metadata."
        ),
    )
    def tool_fetch_doc_source(url: str) -> str:
        """Fetch a single documentation URL."""
        try:
            result = fetch_doc_source(url)
            return f"Fetched source {result.url} with status {result.status}."
        except Exception as exc:
            return (
                f"fetch-doc-source failed: {exc}. "
                "Pass a valid documentation URL and try again."
            )

    return mcp
