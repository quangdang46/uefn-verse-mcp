# uefn-mcp — MCP Server for UEFN

> Connect Claude Code to Unreal Editor for Fortnite via MCP.

```
Claude Code ←── stdio ──→ server/main.py (FastMCP)
                               │
                          HTTP 127.0.0.1:8765
                               │
                          uefn_tools/tools/mcp_bridge.py (in UEFN)
                               │
                          uefn_tools/ (358 tools)
```

## Origins and credits
This repo is a **fork and continuation** of **[UEFN-TOOLBELT](https://github.com/undergroundrap/UEFN-TOOLBELT)** — the large `uefn_tools` Python package for UEFN (hundreds of editor helpers, Verse workflows, arena tools, and related utilities). The in-editor side of this project is still that toolkit, deployed into your island project via `deploy.py`.
The **host MCP server ↔ in-editor HTTP listener** split (stdio MCP outside UEFN, JSON over HTTP on `127.0.0.1`, commands drained on the editor main thread) follows the same idea as **[uefn-mcp-server](https://github.com/KirChuvakov/uefn-mcp-server)** by Kir Chuvakov: external `mcp` SDK process plus a listener inside UEFN. This fork uses **FastMCP** (`server/main.py`), extends the bridge for the full toolbelt (including the escape-hatch `run_tool` surface), and documents the lineage in `Content/Python/uefn_tools/tools/mcp_bridge.py`. If you want a minimal reference implementation or Kir’s original tool set, start from that upstream repo.

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
import uefn_tools as ut; ut.register(); ut.run('mcp_start')
```

Output Log shows: `Listener started on http://127.0.0.1:8765`

### 3. Install MCP server dependencies

The stdio server imports `mcp` (FastMCP). Install it into the **same** Python that runs `server/main.py` (the one in your MCP `command`, often `python` on PATH):

```bash
cd uefn-mcp
python -m pip install -r requirements.txt
```

If Cursor still reports `No module named 'mcp'`, your IDE may be using a different Python than the terminal. Point MCP at that interpreter explicitly, e.g. `"command": "C:\\Path\\To\\python.exe"`.

### 4. Connect Cursor / Claude Code

Add to `.mcp.json` (project or user config):

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

- Python 3.10+ on host machine (same interpreter as MCP `command`)
- `python -m pip install -r requirements.txt` (installs `mcp` for `server/main.py`)
- UEFN with Python Editor Script Plugin enabled

## Structure

```
uefn-mcp/
├── server/           # External MCP server (run on host)
│   ├── main.py       # FastMCP entry point
│   ├── bridge.py     # HTTP client
│   └── tools/        # Tool definitions
├── Content/Python/uefn_tools/  # Tool package + MCP HTTP bridge (deployed)
├── init_unreal.py    # UEFN startup hook
├── deploy.py         # Deploy script
├── requirements.txt  # Host MCP server (pip install -r)
└── docs/             # Documentation
```

## License

MIT
