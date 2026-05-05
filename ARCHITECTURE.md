# Architecture

## Overview

```
Claude Code ←── stdio ──→ server/main.py (FastMCP)
                               │
                          HTTP POST 127.0.0.1:8765
                               │
                          uefn_listener.py (inside UEFN)
                               │
                          uefn_tools/ (358 tools → unreal.* API)
```

## Components

### 1. server/main.py — External MCP Server

- FastMCP server running on host machine
- Exposes ~40 direct @mcp.tool() commands
- Exposes `run_tool()` escape hatch for 358 tools
- Uses `bridge.py` to send HTTP commands to UEFN

### 2. uefn_listener.py — In-UEFN HTTP Listener

- HTTPServer running on daemon thread inside UEFN
- Receives JSON commands via HTTP POST
- Queues commands for main thread execution
- Dispatches via `register_slate_post_tick_callback`
- 28+ command handlers (actors, assets, level, viewport)

### 3. uefn_tools/ — Tool Package

- 358 @register_tool decorated functions
- Organized into categories (Actors, Materials, Verse, etc.)
- Accessed via `run_tool()` escape hatch in uefn_listener

### 4. init_unreal.py — UEFN Auto-Loader

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

## Port Discovery

Auto-detects free port in range 8765-8770:
1. Try cached port
2. Scan range sequentially
3. Cache successful discovery
4. Retry on connection failure

## Deployment

```bash
python deploy.py
# Copies:
#   - uefn_tools/ → {project}/Content/Python/uefn_tools/
#   - uefn_listener.py → {project}/Content/Python/
#   - init_unreal.py → {project}/Content/Python/
```
