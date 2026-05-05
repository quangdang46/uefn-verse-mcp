# uefn-mcp — AI Agent Context

## Architecture

Two-process MCP server for UEFN:

1. **server/main.py** — External FastMCP server (runs on host, connects to Claude Code via stdio)
2. **uefn_listener.py** — HTTP listener (runs inside UEFN, dispatches `unreal.*` calls on main thread)

Communication: HTTP POST `127.0.0.1:8765` (auto-detect 8765-8770)

## Key Files

| File | Purpose |
|---|---|
| `server/main.py` | FastMCP entry — ~40 @mcp.tool() + escape hatch |
| `server/bridge.py` | HTTP client → uefn_listener |
| `server/port_discovery.py` | Auto-detect listener port |
| `uefn_listener.py` | In-UEFN HTTP server (queue + Slate tick) |
| `Content/Python/uefn_tools/` | 358 registered tools |
| `deploy.py` | Deploy to UEFN project |
| `init_unreal.py` | UEFN auto-loader |

## Tool Surface

- **Direct:** ~40 curated @mcp.tool() commands (actors, assets, level, viewport)
- **Escape hatch:** `run_tool(name, **kwargs)` → any of 358 tools

## Rules

1. All `unreal.*` calls MUST run on UEFN main thread (queue + tick callback)
2. UEFN's embedded Python cannot `pip install` — MCP SDK runs externally
3. Deploy to UEFN via `python deploy.py` before testing
4. Start listener in UEFN: `import uefn_tools as ut; ut.run("mcp_start")`
