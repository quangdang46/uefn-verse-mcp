# AGENTS.md

## For AI Agents

This is uefn-mcp, an MCP server for UEFN. Key info:

- **Architecture:** Two-process MCP (external server + in-UEFN listener)
- **Tools:** ~40 direct commands + `run_tool()` escape hatch for the full uefn_tools registry (see `uefn_tools.__tool_count__`)
- **Setup:** `python deploy.py` → `import uefn_tools as ut; ut.run("mcp_start")`
- **Rules:** All `unreal.*` calls must run on UEFN main thread (queue + tick callback)
