# verse-docs-mcp

> Python MCP server for querying Verse/Fortnite UEFN documentation via a packaged SQLite FTS5 index.

This is the Python port of the `query-docs` and `fetch-doc-source` tools from the Rust [verse-mcp](https://github.com/quangdang46/uefn-verse-mcp) project. It ships a pre-built SQLite full-text-search database with ~2 000 indexed Verse API and Fortnite docs pages, including Verse digest files.

## Install (one-liner)

```bash
curl -fsSL https://raw.githubusercontent.com/quangdang46/uefn-verse-mcp/main/python/install.sh | bash
```

Or install directly with **uv** / **pipx** / **pip**:

```bash
# uv (recommended)
uv tool install verse-docs-mcp --from "git+https://github.com/quangdang46/uefn-verse-mcp.git@main#subdirectory=python"

# pipx
pipx install "git+https://github.com/quangdang46/uefn-verse-mcp.git@main#subdirectory=python"

# pip
pip install "git+https://github.com/quangdang46/uefn-verse-mcp.git@main#subdirectory=python"
```

## MCP Tools

| Tool | Input | Output |
|---|---|---|
| `query-docs` | `query`, `limit?`, `offset?`, `fetch_source_urls?`, `max_fetches?` | Ranked Verse docs with full indexed content, optional fetched source page content |
| `fetch-doc-source` | `url` | Fetched and normalized documentation URL as plain text |

### Configure your MCP host

**Claude Code** (`~/.claude.json`):
```json
{
  "mcpServers": {
    "verse-docs-mcp": {
      "command": "verse-docs-mcp",
      "args": []
    }
  }
}
```

**Cursor** (`~/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "verse-docs-mcp": {
      "command": "verse-docs-mcp",
      "args": []
    }
  }
}
```

Auto-register during install:
```bash
REGISTER=1 curl -fsSL .../install.sh | bash
```

## CLI Usage

```bash
# Start MCP server (stdio, the default)
verse-docs-mcp
verse-docs-mcp serve
verse-docs-mcp serve --transport stdio

# Start MCP server (HTTP)
verse-docs-mcp serve --transport http --port 2003

# Run a docs query from the terminal
verse-docs-mcp query "editable properties"
verse-docs-mcp query "@editable usage" --limit 3

# Rebuild the docs database from source
verse-docs-mcp index --output /path/to/verse-docs.db --docs-root /path/to/repo
```

## How It Works

1. **At build time** (when you install the package), a hatch build hook compiles the documentation corpus into a SQLite FTS5 database and packages it inside the wheel.

2. **At runtime**, the server extracts the DB to `~/.vm/verse-docs.db` (same location as the Rust binary) and queries it using FTS5 full-text search with BM25 ranking.

3. **Source URLs** for each doc can optionally be fetched and normalized into plain text for enrichment.

## Development

```bash
cd python/
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
verse-docs-mcp query "creative_device events"
```

## Refreshing the bundled docs

The Markdown corpus under `python/docs/` is periodically refetched from
`dev.epicgames.com` so the bundled SQLite index stays current. The script
lives at `python/scripts/refresh_docs.py`.

Run it locally with:

```bash
pip install httpx beautifulsoup4 markdownify
# Dry run against 50 files
python python/scripts/refresh_docs.py --dry-run --limit 50

# Real refresh, conservative concurrency to avoid Cloudflare WAF
python python/scripts/refresh_docs.py --concurrency 4 --delay-ms 250
```

`dev.epicgames.com` is fronted by Cloudflare and will rate-limit a single
IP aggressively (HTTP 403) once it sees bursty traffic. The defaults are
intentionally polite. Pages that are pure JS shells or have been removed
are skipped and the existing on-disk content is kept.

### Automate via GitHub Actions

A drop-in workflow is provided at
`python/scripts/github-workflow-refresh-docs.yml.example`. Copy it into
`.github/workflows/refresh-docs.yml` to enable a weekly cron + manual
`workflow_dispatch` trigger that runs the refresh on GitHub-hosted
runners (different egress IP per run, so the WAF does not accumulate
per-IP bans). When the workflow finds diffs it opens a PR against your
default branch.

```bash
mkdir -p .github/workflows
cp python/scripts/github-workflow-refresh-docs.yml.example \
   .github/workflows/refresh-docs.yml
git add .github/workflows/refresh-docs.yml
git commit -m "chore: enable weekly docs refresh cron"
```

## License

MIT
