# VerseUEFN MCP Server — Master Plan

> **Mục tiêu:** Xóa UI tập trung vào MCP
> Kirch's listener + Toolbelt's 358 tool logic = Pure MCP

---

## 0. Executive Summary

**Architecture:**
```
Claude Code ←── stdio ──→ mcp_server.py (external, host machine)
                               │
                          HTTP POST 127.0.0.1:8765
                               │
                          uefn_listener.py (inside UEFN)
                               │
                          uefn_tools/ (358 @register_tool functions)
```

**Setup:**
```bash
# Step 1: Deploy
python deploy.py

# Step 2: Start listener
import uefn_tools; uefn_tools.run("mcp_start")
```

---

## 1. What Gets Deleted

### UI Files (DELETE)
```
uefn_tools/
├── dashboard_pyside6.py        # PySide6 GUI → DELETE
├── menu.py                      # Editor menu bar → DELETE
├── verse_device_graph.py         # PySide6 visualizer → DELETE
├── list_untested.py              # UI helper → DELETE
└── core/
    ├── base_window.py            # PySide6 base class → DELETE
    └── theme.py                  # PySide6 dark theme → DELETE
```

### UI Code in Tool Files (STRIP)
```
prefab_migrator.py    → Strip ToolbeltWindow classes (keep @register_tool functions)
cooker_optimizer.py   → Strip ToolbeltWindow classes (keep @register_tool functions)
smart_organizer.py    → Strip ToolbeltWindow + PALETTE (keep @register_tool functions)
ui_icon_import.py     → Strip ToolbeltWindow classes (keep @register_tool functions)
config_tools.py       → Strip theme_list/theme_set/theme_get tools (not needed for MCP)
actor_org_tools.py    → Check + strip if any window code
```

### __init__.py Updates (STUB)
```
uefn_tools/__init__.py
├── Remove launch_qt()           → stub: "Use MCP instead"
├── Remove launch()              → stub: "Use MCP instead"
├── Remove _schedule_menu()      → delete
├── Remove dashboard_pyside6 import → delete
└── Keep register_all_tools()    ✅
```

### core/__init__.py Updates (STRIP)
```
uefn_tools/core/__init__.py
├── Remove: from .theme import PALETTE, QSS, color
├── Remove: from .base_window import ToolbeltWindow
└── Keep: all helpers (path utils, logging, progress)
```

---

## 2. What Gets Kept

### Tool Logic (358 @register_tool functions) ✅
```
uefn_tools/tools/
├── actor_org_tools.py           # ✅ keep logic
├── arena_generator.py            # ✅ keep logic
├── asset_importer.py            # ✅ keep logic
├── bulk_operations.py           # ✅ keep logic
├── cooker_optimizer.py          # ✅ keep logic (strip windows)
├── material_master.py           # ✅ keep logic
├── prefab_migrator.py           # ✅ keep logic (strip windows)
├── smart_organizer.py          # ✅ keep logic (strip windows)
├── verse_snippet_generator.py   # ✅ keep logic
├── zone_tools.py                # ✅ keep logic
└── ... (all other tool files)
```

### Core Utilities ✅
```
uefn_tools/
├── __init__.py                  # ✅ stubbed
├── registry.py                   # ✅ @register_tool decorator
├── schema_utils.py              # ✅ Verse schema
├── smoke_test.py                # ✅ health check
├── diagnostics.py               # ✅ debug tools
└── core/
    ├── activity_log.py          # ✅ logging
    ├── config.py                 # ✅ user settings
    └── safety_gate.py           # ✅ security
```

---

## 3. New Files

### uefn_listener.py (MERGE)
```
Source: Kirch's uefn_listener.py + Toolbelt's mcp_bridge.py
├── HTTP server (127.0.0.1:8765)
├── queue.Queue (thread-safe)
├── register_slate_post_tick_callback (main thread dispatch)
├── 32 command handlers (Kirch's 28 + run_tool, describe_tool, mcp_start/stop/status)
└── Remove Tkinter status window
```

### server/ (NEW - External MCP)
```
server/
├── __init__.py
├── main.py                       # FastMCP entry point
├── bridge.py                     # HTTP client → UEFN listener
├── port_discovery.py             # Auto-detect 8765-8770
└── tools/
    ├── __init__.py
    ├── system.py                 # ping, execute_python, get_log
    ├── actors.py                 # get_all_actors, spawn_actor, etc.
    ├── assets.py                 # list_assets, search_assets, etc.
    ├── level.py                  # save_level, get_level_info
    ├── viewport.py               # get/set_viewport_camera
    └── escape_hatch.py           # run_tool, list_tools, describe_tool
```

### deploy.py (NEW)
```
Cross-platform deploy script:
1. Scan Fortnite Projects folder
2. User selects project
3. Copy:
   - uefn_tools/ → {project}/Content/Python/uefn_tools/
   - uefn_listener.py → {project}/Content/Python/
   - init_unreal.py → {project}/Content/Python/
4. Done
```

### init_unreal.py (UPDATE)
```
Auto-discovers packages (no change needed)
uefn_tools/ will auto-load via existing loader
```

---

## 4. MCP Tool Surface

### Direct Commands (~40) — @mcp.tool()

| Category | Tools |
|---|---|
| **System** | ping, execute_python, get_log, get_editor_log, shutdown |
| **Actors** | get_all_actors, get_selected_actors, spawn_actor, delete_actors, set_actor_transform, select_actors, focus_selected |
| **Assets** | list_assets, get_asset_info, get_selected_assets, rename_asset, delete_asset, duplicate_asset, search_assets |
| **Level** | get_project_info, save_current_level, get_level_info |
| **Viewport** | get_viewport_camera, set_viewport_camera |
| **Bridge** | mcp_start, mcp_stop, mcp_status |
| **High-Value** | arena_generate, snapshot_save, verse_write_file |

### Escape Hatch

```python
run_tool(tool_name: str, **kwargs)   # Execute any of 358 tools
list_tools(category?: str)            # List all tools
describe_tool(tool_name: str)         # Get tool schema
```

---

## 5. Directory Structure

```
verse-uefn-mcp/
│
├── uefn_tools/                    # Deployed into UEFN
│   ├── __init__.py               # stubbed (no UI)
│   ├── registry.py               # @register_tool
│   ├── schema_utils.py
│   ├── smoke_test.py
│   ├── diagnostics.py
│   ├── core/                     # helpers only
│   │   ├── activity_log.py
│   │   ├── config.py
│   │   └── safety_gate.py
│   └── tools/                    # 358 tool logic (no windows)
│       ├── actor_org_tools.py    # stripped
│       ├── arena_generator.py
│       ├── material_master.py
│       └── ... (all tool files)
│
├── uefn_listener.py              # In-UEFN HTTP listener
│
├── server/                        # External MCP (host machine)
│   ├── main.py
│   ├── bridge.py
│   ├── port_discovery.py
│   └── tools/
│
├── init_unreal.py                # UEFN startup hook
├── deploy.py                     # Deploy script
├── .mcp.json                    # Claude Code config
│
├── docs/
│   ├── UEFN_QUIRKS.md
│   ├── PIPELINE.md
│   ├── DEVICE_API_MAP.md
│   └── FORTNITE_DEVICES.md
│
├── legacy/                       # Archived
│   ├── uefn-mcp-server-master/
│   └── verse-mcp-main/
│
├── README.md
├── CLAUDE.md
├── ARCHITECTURE.md
└── LICENSE
```

---

## 6. Rollout Phases

### Phase 1: Delete UI Files
- [ ] Delete dashboard_pyside6.py, menu.py, verse_device_graph.py, list_untested.py
- [ ] Delete core/base_window.py, core/theme.py

### Phase 2: Strip Tool Files
- [ ] prefab_migrator.py — strip ToolbeltWindow classes
- [ ] cooker_optimizer.py — strip ToolbeltWindow classes
- [ ] smart_organizer.py — strip ToolbeltWindow + PALETTE
- [ ] ui_icon_import.py — strip ToolbeltWindow classes
- [ ] config_tools.py — strip theme tools
- [ ] actor_org_tools.py — check + strip if needed

### Phase 3: Update __init__.py & core/__init__.py
- [ ] Stub launch_qt(), launch()
- [ ] Remove _schedule_menu()
- [ ] Remove theme exports from core/__init__.py

### Phase 4: Create uefn_listener.py
- [ ] Merge Kirch's listener + toolbelt's bridge commands
- [ ] Add run_tool, describe_tool, mcp_start/stop/status
- [ ] Remove Tkinter status window

### Phase 5: Create server/ (External MCP)
- [ ] server/main.py — FastMCP entry
- [ ] server/bridge.py — HTTP client
- [ ] server/port_discovery.py
- [ ] ~40 direct @mcp.tool() implementations
- [ ] escape_hatch.py (run_tool, list_tools, describe_tool)

### Phase 6: Deploy Script
- [ ] deploy.py — cross-platform

### Phase 7: Rebrand Docs
- [ ] README.md, CLAUDE.md, ARCHITECTURE.md
- [ ] Clean all references (toolbelt, Ocean Bennett, undergroundrap)

### Phase 8: Validation
- [ ] Syntax check all files
- [ ] Test in UEFN

---

## 7. Quick Reference

```
╔══════════════════════════════════════════════════════════════╗
║              VerseUEFN MCP — Quick Start                   ║
╠══════════════════════════════════════════════════════════════╣
║  SETUP (one-time):                                          ║
║    pip install mcp                                         ║
║    python deploy.py                                         ║
║                                                               ║
║  START LISTENER (in UEFN console):                          ║
║    import uefn_tools; uefn_tools.run("mcp_start")           ║
║                                                               ║
║  USE IN CLAUDE CODE:                                         ║
║    "Spawn 100 cubes in a grid"                              ║
║    "Generate a large arena"                                 ║
║    "Write Verse game manager for my level"                  ║
║                                                               ║
║  DIRECT COMMANDS (~40):                                      ║
║    get_all_actors()                                         ║
║    spawn_actor("/Game/Cube", [0,0,0])                       ║
║    execute_python("print('hello')")                          ║
║                                                               ║
║  ESCAPE HATCH:                                               ║
║    run_tool("any_tool", param=value)     # 358 tools     ║
╚══════════════════════════════════════════════════════════════╝
```

---

*Plan: Delete UI, focus on MCP — Kirch's listener + Toolbelt's 358 tool logic*
