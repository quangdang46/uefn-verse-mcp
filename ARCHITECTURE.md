# Architecture

## Overview

```
Claude Code ←── stdio ──→ server/main.py (FastMCP)
                               │
                          HTTP POST 127.0.0.1:8765
                               │
                          uefn_tools mcp_bridge (inside UEFN)
                               │
                          uefn_tools/ (358 tools → unreal.* API)
```

## Components

### 1. server/main.py — External MCP Server

- FastMCP server running on host machine
- Exposes ~40 direct @mcp.tool() commands
- Exposes `run_tool()` escape hatch for 358 tools
- Uses `bridge.py` to send HTTP commands to UEFN

### 2. uefn_tools/tools/mcp_bridge.py — In-UEFN HTTP listener

- HTTPServer on a daemon thread; JSON POST API
- Queue + `register_slate_post_tick_callback` for main-thread `unreal.*` calls
- System / actors / assets / level / viewport commands + `run_tool` escape hatch

### 3. uefn_tools/ — Tool package

- 358 `@register_tool` functions (categories: Actors, Materials, Verse, …)
- Invoked from MCP via `run_tool` on the bridge

### 4. init_unreal.py — UEFN auto-loader

- Generic loader: discovers all packages in Content/Python/
- Calls `register()` on each package
- No toolbelt-specific code

## Threading Model

```
HTTP Thread          Main Editor Thread
     │                      │
     │ queue.put()          │
     │ ──────────────────► │
     │                      │ register_slate_post_tick_callback
     │                      │   ├── drain queue
     │                      │   ├── unreal.* calls
     │                      │   └── _responses[id] = result
     │                      │
     │ _responses[id]        │
     │ ◄─────────────────── │
     │                      │
     │ HTTP Response        │
```

## Port discovery

Host `server/port_discovery.py` scans 8765–8770 and picks a port whose GET response identifies the uefn_tools MCP bridge (`app` contains `UEFN uefn_tools MCP Bridge`).

## Deployment

```bash
python deploy.py
# Copies:
#   - uefn_tools/ → {project}/Content/Python/uefn_tools/
#   - init_unreal.py → {project}/Content/Python/
```
