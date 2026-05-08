# uefn-mcp — AI Agent Context

## Architecture

Two-process MCP server for UEFN:

1. **server/main.py** — External FastMCP server (host, stdio to the IDE)
2. **uefn_tools/tools/mcp_bridge.py** — HTTP listener inside UEFN (queue + Slate tick → `unreal.*`)

Communication: HTTP POST `127.0.0.1:8765` (auto-detect 8765-8770)

## Key Files

| File | Purpose |
|---|---|
| `server/main.py` | FastMCP entry — ~40 @mcp.tool() + escape hatch |
| `server/bridge.py` | HTTP client → UEFN mcp_bridge |
| `server/port_discovery.py` | Find mcp_bridge port (8765–8770) |
| `Content/Python/uefn_tools/tools/mcp_bridge.py` | In-UEFN HTTP server |
| `Content/Python/uefn_tools/` | Registered tools (`uefn_tools.__tool_count__`) |
| `deploy.py` | Deploy to UEFN project |
| `init_unreal.py` | UEFN auto-loader |

## Tool Surface

- **Direct:** ~40 curated @mcp.tool() commands (actors, assets, level, viewport)
- **Escape hatch:** `run_tool(name, **kwargs)` → any registered tool

## Rules

1. All `unreal.*` calls MUST run on UEFN main thread (queue + tick callback)
2. UEFN's embedded Python cannot `pip install` — MCP SDK runs externally
3. Deploy to UEFN via `python deploy.py` before testing
4. Start listener in UEFN: `import uefn_tools as ut; ut.run("mcp_start")`
