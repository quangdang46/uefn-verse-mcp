# uefn-mcp — MCP Server for UEFN

> Connect Claude Code to Unreal Editor for Fortnite via MCP.

```
Claude Code ←── stdio ──→ server/main.py (FastMCP)
                               │
                          HTTP 127.0.0.1:8765
                               │
                          uefn_listener.py (in UEFN)
                               │
                          uefn_tools/ (358 tools)
```

## Setup

### 1. Deploy to UEFN

```bash
# Clone / download this repo
cd uefn-mcp

# Deploy to your UEFN project
python deploy.py
```

### 2. Start Listener

Open UEFN → Python Console → type:

```python
import uefn_tools as ut; ut.run("mcp_start")
```

Output Log shows: `Listener started on http://127.0.0.1:8765`

### 3. Connect Claude Code

Add to `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "uefn": {
      "command": "python",
      "args": ["/path/to/uefn-mcp/server/main.py"]
    }
  }
}
```

Restart Claude Code. Full MCP access to UEFN!

## Tools

### Direct Commands (~40)

| Category | Tools |
|---|---|
| **System** | `ping`, `execute_python`, `get_log`, `shutdown` |
| **Actors** | `get_all_actors`, `spawn_actor`, `delete_actors`, `select_actors`... |
| **Assets** | `list_assets`, `get_asset_info`, `rename_asset`, `delete_asset`... |
| **Level** | `get_project_info`, `save_current_level`, `get_level_info` |
| **Viewport** | `get_viewport_camera`, `set_viewport_camera` |

### Escape Hatch (358 tools)

```python
run_tool("arena_generate", size="medium", teams=True)
list_tools("Materials")
describe_tool("material_master")
```

### Example Usage

```python
# Spawn 100 cubes
spawn_actor("/Game/Cube", location=[0, 0, 0])

# Generate arena
run_tool("arena_generate", size="large")

# Write Verse code
run_tool("verse_write_file", filename="MyGame.verse", content="...")
```

## Requirements

- Python 3.10+ on host machine
- `pip install mcp`
- UEFN with Python Editor Script Plugin enabled

## Structure

```
uefn-mcp/
├── server/           # External MCP server (run on host)
│   ├── main.py       # FastMCP entry point
│   ├── bridge.py     # HTTP client
│   └── tools/        # Tool definitions
├── uefn_listener.py  # HTTP listener (runs in UEFN)
├── uefn_tools/       # Tool package (deployed into UEFN)
├── init_unreal.py    # UEFN startup hook
├── deploy.py         # Deploy script
└── docs/             # Documentation
```

## License

MIT
