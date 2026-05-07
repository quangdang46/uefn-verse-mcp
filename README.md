# uefn-mcp

Python 3.10+
UEFN
MCP

> A two-process MCP bridge for Unreal Editor for Fortnite that lets Claude Code, Cursor, and other MCP clients drive a live UEFN editor safely.

```text
MCP client (Claude Code / Cursor / custom host)
    │
    │ stdio
    ▼
server/main.py  ── FastMCP host process
    │
    │ HTTP 127.0.0.1:8765-8770
    ▼
Content/Python/uefn_tools/tools/mcp_bridge.py
    │
    │ queue + Slate tick callback
    ▼
UEFN editor main thread -> unreal.* -> 354 registered uefn_tools actions
```

**Quick setup**

```bash
git clone https://github.com/quangdang46/uefn-verse-mcp.git
cd uefn-verse-mcp
python -m pip install -r requirements.txt
python deploy.py --project "MyIsland"
```

There is no packaged one-line installer yet. The supported path today is source checkout plus local deploy into a UEFN project.

## TL;DR

### The Problem

UEFN's Python layer is powerful, but it is a bad place to host a modern MCP server directly:

- `unreal.*` calls must run on the editor main thread.
- Blocking Python code can freeze the editor.
- The MCP SDK belongs in a normal host Python runtime, not inside the editor sandbox.

### The Solution

`uefn-mcp` splits the system in two:

- `server/main.py` runs externally as a FastMCP stdio server.
- `Content/Python/uefn_tools/tools/mcp_bridge.py` runs inside UEFN as a local HTTP listener.
- Commands are queued and drained on Slate ticks so editor API calls stay on the main thread.

### Why Use `uefn-mcp`?


| Capability                | What it gives you                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| 31 direct MCP tools       | A curated surface for actors, assets, project info, viewport, logs, and status                          |
| 354 `run_tool` entries    | An escape hatch into the full `uefn_tools` registry without re-wrapping every action as first-class MCP |
| Main-thread-safe dispatch | `unreal.*` work is queued and executed on editor ticks instead of from the HTTP thread                  |
| Auto port discovery       | The host scans ports `8765-8770` and reconnects automatically if the listener moved                     |
| Generic UEFN loader       | `init_unreal.py` auto-loads any package under `Content/Python/` that exposes `register()`               |
| Deployment helper         | `deploy.py` copies the package and keeps `.urcignore` aligned for editor-only Python files              |


The live inventory is tracked in [FEATURES.md](FEATURES.md), and deeper engine constraints are documented in [docs/UEFN_QUIRKS.md](docs/UEFN_QUIRKS.md).

## Origins and Credits

This repo sits on top of two upstream lines:

- **UEFN Toolbelt** — broad in-editor `uefn_tools` registry and tooling: [UEFN-TOOLBELT](https://github.com/undergroundrap/UEFN-TOOLBELT) (Ocean Bennett).
- **External MCP + in-editor listener** — architecture and code lineage from KirChuvakov’s MIT-licensed projects (commonly referenced as [uefn-mcp-server](https://github.com/KirChuvakov/uefn-mcp-server) or **uefn-verse-server**).

This fork keeps both ideas, but reshapes them into an MCP-first repo:

- external FastMCP host process in `server/`
- in-editor HTTP bridge in `Content/Python/uefn_tools/tools/mcp_bridge.py`
- curated direct MCP surface plus a registry escape hatch

### License

Licensing is documented in [LICENSE](LICENSE). In short:

- **Combined distribution:** This repository is offered under **GNU AGPL v3.0** with UEFN Toolbelt’s **additional visible-attribution term** (copyleft; network use triggers source-sharing obligations — see the license file and the [AGPL-3.0 text](https://www.gnu.org/licenses/agpl-3.0.en.html)).
- **Upstream MIT components:** Portions derived from KirChuvakov’s work were originally under the **MIT License**; their copyright and permission notice must stay intact in copies of this project (also reproduced in `LICENSE`).
- **Forks and derivatives:** If you ship something built on this codebase or its architecture, include the **visible Toolbelt credit** required in `LICENSE` (for example in README, docs, store page, or an in-editor credits panel):

  ```text
  Built on UEFN Toolbelt by Ocean Bennett
  (https://github.com/undergroundrap/UEFN-TOOLBELT)
  ```

  …or an equivalent that names Ocean Bennett and links to that repository.

This is not legal advice; read `LICENSE` for full terms.

## Quick Example

The fastest end-to-end workflow is:

```bash
git clone https://github.com/quangdang46/uefn-verse-mcp.git
cd uefn-verse-mcp
python -m pip install -r requirements.txt
python deploy.py --project "MyIsland"
```

```python
# In the UEFN Python console
import uefn_tools as ut; ut.register(); ut.run("mcp_start")
```

```jsonc
// In your MCP client config (.mcp.json)
{
  "mcpServers": {
    "uefn": {
      "command": "python",
      "args": ["C:\\path\\to\\uefn-verse-mcp\\server\\main.py"]
    }
  }
}
```

Once the client reconnects, the typical first calls look like this:

```python
ping()
get_project_info()
get_all_actors()
spawn_actor(class_path="/Game/Blueprints/BP_Cube.BP_Cube_C", location=[0, 0, 200])
set_viewport_camera(location=[-800, 0, 400], rotation=[-15, 0, 0])
list_tools(category="Materials")
describe_tool("material_gradient_painter")
run_tool("arena_generate", kwargs={"size": "large", "teams": True})
run_tool("smoke_test")
```

Examples above use conceptual MCP call syntax. The tool names and parameters match the real FastMCP surface exported by `server/main.py`.

## Design Philosophy

### 1. Keep the MCP SDK outside UEFN

The host process uses ordinary Python and `mcp>=1.2.0`. UEFN only needs the local listener and the tool registry.

### 2. Never call `unreal.*` from the wrong thread

The HTTP server runs on a daemon thread, but every editor action is queued and drained on the Slate post-tick callback. That is the safety boundary that keeps automation from fighting the editor event loop.

### 3. Curate the common path, keep the full escape hatch

The direct MCP surface covers the most common actor, asset, level, and viewport workflows. `run_tool`, `list_tools`, and `describe_tool` expose the deeper registry when you need specialized behavior.

### 4. Make deploys boring

The intended setup is:

1. Copy `uefn_tools/` and `init_unreal.py` into the target project.
2. Start the bridge in the editor.
3. Point the MCP client at `server/main.py`.

No editor-side package installation and no IDE-specific glue should be required beyond that.

## Comparison


| Approach                   | MCP-native | Full registry access | Main-thread safety model        | Best for                                         |
| -------------------------- | ---------- | -------------------- | ------------------------------- | ------------------------------------------------ |
| Ad hoc UEFN Python scripts | No         | No                   | You own every threading mistake | One-off local editor tasks                       |
| Minimal custom HTTP bridge | Partial    | Usually narrow       | Depends on your implementation  | Small, fixed editor automations                  |
| `uefn-mcp`                 | Yes        | Yes, via `run_tool`  | Queue + Slate tick dispatch     | AI-agent-driven UEFN editing and experimentation |


## Prerequisites

- UEFN on Windows, with the Python Editor Script Plugin enabled
- Host Python 3.10 or newer for `server/main.py`, `deploy.py`, and the MCP dependency
- A local UEFN project you can copy `Content/Python/` files into

## Installation

### Option 1: `deploy.py` (recommended)

`deploy.py` is the clean MCP-first path.

```bash
python -m pip install -r requirements.txt
python deploy.py --project "MyIsland"
```

You can also deploy by full path:

```bash
python deploy.py --path "D:\\Projects\\MyIsland"
```

If you omit both flags, `deploy.py` will prompt you interactively.

What it installs:

- `Content/Python/uefn_tools/`
- `Content/Python/init_unreal.py`
- `.urcignore` entry for `Content/Python/*`

### Option 2: `deploy.bat` (Windows interactive helper)

If you prefer a Windows batch workflow:

```bat
deploy.bat
```

This is still present as a helper, but the repo's documented MCP-first path is `deploy.py`.

### Option 3: Manual install

If you need full control:

1. Copy `Content/Python/uefn_tools/` into your project at `Content/Python/uefn_tools/`.
2. Copy `init_unreal.py` into your project at `Content/Python/init_unreal.py`.
3. Install host dependencies:

```bash
python -m pip install -r requirements.txt
```

1. Ensure the project root `.urcignore` includes:

```text
Content/Python/*
```

### Not Recommended: `install.py`

`install.py` still contains older Toolbelt/UI-era behavior. Use `deploy.py` for the current MCP-first workflow.

## Quick Start

1. Clone the repo.

```bash
git clone https://github.com/quangdang46/uefn-verse-mcp.git
cd uefn-verse-mcp
```

1. Install the host dependency into the same Python interpreter your MCP client will use.

```bash
python -m pip install -r requirements.txt
```

1. Deploy the UEFN-side package.

```bash
python deploy.py --project "MyIsland"
```

1. Start the listener inside UEFN.

```python
import uefn_tools as ut
ut.register()
ut.run("mcp_start")
```

1. Add the server to your MCP client config.

```jsonc
{
  "mcpServers": {
    "uefn": {
      "command": "python",
      "args": ["C:\\path\\to\\uefn-verse-mcp\\server\\main.py"]
    }
  }
}
```

1. Verify the connection.

```python
ping()
get_status()
run_tool("smoke_test")
```

1. Start editing the level from your MCP client.

```python
get_all_actors()
search_assets(class_name="StaticMesh", directory="/Game", recursive=True)
spawn_actor(class_path="/Game/Blueprints/BP_Cube.BP_Cube_C", location=[0, 0, 100])
```

## Command Reference

### System


| Tool             | What it does                                             | Example                                            |
| ---------------- | -------------------------------------------------------- | -------------------------------------------------- |
| `ping`           | Confirms the host can reach the in-editor bridge         | `ping()`                                           |
| `get_status`     | Returns listener status and bridge metadata              | `get_status()`                                     |
| `execute_python` | Executes arbitrary Python inside the UEFN editor runtime | `execute_python(code="result = {'status': 'ok'}")` |
| `get_log`        | Returns recent bridge log lines                          | `get_log(lines=100)`                               |
| `shutdown`       | Stops the in-editor listener                             | `shutdown()`                                       |


### Actors


| Tool                   | What it does                                   | Example                                                                              |
| ---------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| `get_all_actors`       | Lists actors in the current level              | `get_all_actors()`                                                                   |
| `get_selected_actors`  | Reads the current editor selection             | `get_selected_actors()`                                                              |
| `spawn_actor`          | Spawns an actor from a class or object path    | `spawn_actor(class_path="/Game/Blueprints/BP_Cube.BP_Cube_C", location=[0, 0, 100])` |
| `delete_actors`        | Deletes actors by label                        | `delete_actors(actor_labels=["Cube_1", "Cube_2"])`                                   |
| `set_actor_transform`  | Updates actor location, rotation, and/or scale | `set_actor_transform(actor_label="Cube_1", location=[200, 0, 100])`                  |
| `get_actor_properties` | Reads properties for a named actor             | `get_actor_properties(actor_label="Cube_1")`                                         |
| `set_actor_properties` | Writes multiple actor properties               | `set_actor_properties(actor_label="Cube_1", properties={"mobility": "Static"})`      |
| `select_actors`        | Selects actors in the editor                   | `select_actors(actor_labels=["Cube_1"])`                                             |
| `focus_selected`       | Moves the viewport to the active selection     | `focus_selected()`                                                                   |


### Assets


| Tool                  | What it does                                                 | Example                                                                   |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| `list_assets`         | Lists assets in a directory                                  | `list_assets(directory="/Game", recursive=True)`                          |
| `get_asset_info`      | Reads details for a specific asset path                      | `get_asset_info(asset_path="/Game/MyFolder/MyAsset")`                     |
| `get_selected_assets` | Returns selected Content Browser assets                      | `get_selected_assets()`                                                   |
| `rename_asset`        | Renames or moves an asset                                    | `rename_asset(old_path="/Game/Old", new_path="/Game/New")`                |
| `delete_asset`        | Deletes an asset                                             | `delete_asset(asset_path="/Game/Trash/TempAsset")`                        |
| `duplicate_asset`     | Copies an asset to a new path                                | `duplicate_asset(source_path="/Game/A", dest_path="/Game/B")`             |
| `does_asset_exist`    | Checks if an asset exists                                    | `does_asset_exist(asset_path="/Game/Props/SM_Crate")`                     |
| `save_asset`          | Saves a dirty asset                                          | `save_asset(asset_path="/Game/Props/SM_Crate")`                           |
| `search_assets`       | Searches the Asset Registry with directory and class filters | `search_assets(class_name="Material", directory="/Game", recursive=True)` |


### Project / Level


| Tool                 | What it does                                | Example                |
| -------------------- | ------------------------------------------- | ---------------------- |
| `get_project_info`   | Returns project metadata                    | `get_project_info()`   |
| `save_current_level` | Saves the current level                     | `save_current_level()` |
| `get_level_info`     | Returns summary info about the active level | `get_level_info()`     |


### Viewport


| Tool                  | What it does                                  | Example                                                              |
| --------------------- | --------------------------------------------- | -------------------------------------------------------------------- |
| `get_viewport_camera` | Reads the editor camera position and rotation | `get_viewport_camera()`                                              |
| `set_viewport_camera` | Moves the editor camera                       | `set_viewport_camera(location=[-800, 0, 400], rotation=[-15, 0, 0])` |


### Escape Hatch


| Tool            | What it does                                        | Example                                                |
| --------------- | --------------------------------------------------- | ------------------------------------------------------ |
| `run_tool`      | Executes any registered `uefn_tools` action by name | `run_tool("arena_generate", kwargs={"size": "large"})` |
| `list_tools`    | Lists all registered tools, optionally by category  | `list_tools(category="Materials")`                     |
| `describe_tool` | Returns description and parameters for one tool     | `describe_tool("material_gradient_painter")`           |


### Working With the Full Registry

The direct MCP surface is intentionally small. The deeper workflows are meant to be discovered dynamically:

```python
list_tools()
list_tools(category="Verse Helpers")
describe_tool("device_call_method")
run_tool("device_call_method", kwargs={"class_filter": "TimerObjective", "method": "blueprint_pause"})
```

The full generated inventory lives in [FEATURES.md](FEATURES.md).

## Configuration

### `.mcp.json`

Use the same Python interpreter here that you used for `python -m pip install -r requirements.txt`.

```jsonc
{
  "mcpServers": {
    "uefn": {
      "command": "python",
      "args": ["C:\\dev\\uefn-verse-mcp\\server\\main.py"]
    }
  }
}
```

### Environment Variables


| Variable                     | Default | Purpose                                                                     |
| ---------------------------- | ------- | --------------------------------------------------------------------------- |
| `UEFN_MCP_REQUEST_TIMEOUT`   | `30`    | Default timeout in seconds for bridge requests                              |
| `UEFN_MCP_LONG_TOOL_TIMEOUT` | `900`   | Timeout for long-running `run_tool` calls that opt into the extended budget |


### Port Behavior

- The in-editor listener binds to the first available port in `8765-8770`.
- The host discovers the active port by probing `http://127.0.0.1:<port>/`.
- If the cached port stops responding, the host rescans automatically.

### UEFN Loader Contract

`init_unreal.py` is intentionally generic:

- it adds `Content/Python/` to `sys.path`
- it discovers packages with `__init__.py`
- it calls `register()` when available

That means `uefn_tools` is only one possible package. The loader is reusable for other editor-side Python packages in the same project.

## Architecture

```text
┌──────────────────────────────────────────────────────────────────────┐
│ MCP client                                                          │
│ Claude Code / Cursor / custom FastMCP host                          │
└──────────────────────────────────────────────────────────────────────┘
                                │
                                │ stdio
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ server/main.py                                                      │
│ - FastMCP server                                                    │
│ - 31 direct tools                                                   │
│ - run_tool / list_tools / describe_tool                             │
└──────────────────────────────────────────────────────────────────────┘
                                │
                                │ HTTP JSON POST
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Content/Python/uefn_tools/tools/mcp_bridge.py                       │
│ - Local HTTP listener inside the UEFN process                       │
│ - Queue-based handoff from HTTP thread to editor main thread        │
│ - Bridge commands: system, actors, assets, viewport, escape hatch   │
└──────────────────────────────────────────────────────────────────────┘
                                │
                                │ Slate post-tick callback
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│ UEFN editor main thread                                             │
│ - Executes unreal.* calls safely                                    │
│ - Reads and writes level / assets / viewport                        │
│ - Invokes 354 registered uefn_tools actions                         │
└──────────────────────────────────────────────────────────────────────┘
```

Important files:


| File                                            | Responsibility                                   |
| ----------------------------------------------- | ------------------------------------------------ |
| `server/main.py`                                | External FastMCP entrypoint                      |
| `server/bridge.py`                              | Host-side HTTP client for the in-editor listener |
| `server/port_discovery.py`                      | Port probing across `8765-8770`                  |
| `Content/Python/uefn_tools/tools/mcp_bridge.py` | In-editor HTTP server and queue dispatcher       |
| `Content/Python/uefn_tools/__init__.py`         | Package root, registry setup, plugin loading     |
| `deploy.py`                                     | Project deployment and `.urcignore` maintenance  |
| `init_unreal.py`                                | Generic UEFN Python package loader               |


For a shorter architecture note, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Troubleshooting


| Symptom                                                          | Likely cause                                                                                       | Fix                                                                                                   |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `No module named 'mcp'`                                          | Your MCP client is running a different Python than the one you installed into                      | Install `requirements.txt` into the exact interpreter used by the MCP `command`                       |
| `UEFN listener not found on ports 8765-8770`                     | The in-editor bridge is not running                                                                | In the UEFN console, run `import uefn_tools as ut; ut.register(); ut.run("mcp_start")`                |
| Commands fail right after deploy                                 | The package was copied into the project, but the editor has not loaded it yet                      | Re-run `ut.register()` manually, or restart UEFN if you changed `init_unreal.py`                      |
| The editor freezes during custom automation                      | Blocking code is running on the main thread                                                        | Avoid `time.sleep()` and long synchronous loops in editor-side code; keep work queued and tick-driven |
| Asset or project paths resolve strangely in `init_unreal.py`     | UEFN path helpers do not always point where you expect during startup                              | Use the file-system path of `init_unreal.py` itself rather than `unreal.Paths.project_content_dir()`  |
| `run_tool` works locally but returns unusable data to the client | A tool is returning `None`, a primitive, or a live Unreal object instead of a JSON-friendly result | Make the tool return a structured `dict`, preferably with a `"status"` field                          |


## Limitations

- This repo does not make UEFN headless. You still need a live local editor session.
- The direct MCP surface is curated; deeper workflows rely on `run_tool`.
- The 354-tool registry is broad, but not every entry has been verified in every environment yet. See the status column in [FEATURES.md](FEATURES.md).
- UEFN Python has engine-specific quirks and unsafe APIs. Some operations that are fine in full Unreal Engine are limited or crash-prone in UEFN.
- The documented install path is source-based. There is no PyPI, Homebrew, `winget`, or standalone installer release flow documented here today.

## FAQ

### Do I need to install anything inside UEFN's embedded Python?

No for the MCP server itself. The `mcp` dependency belongs in the external host Python that runs `server/main.py`.

### Why not run the MCP SDK directly inside the editor?

Because the editor runtime is the wrong place for a long-lived stdio server and blocking automation. The two-process split is the safety boundary.

### What should I call first after connecting?

`ping()`, then `get_status()`, then either `get_project_info()` or `run_tool("smoke_test")`.

### How do I access the specialized tools?

Use `list_tools()` to discover categories, `describe_tool()` to inspect parameters, and `run_tool()` to execute the chosen action.

### Can I use this without Claude Code?

Yes. Any MCP client that can launch a stdio server can point at `server/main.py`.

### Do I have to restart UEFN after every change?

No. Most package changes can be reloaded with `ut.register()`. Changes to startup loader behavior in `init_unreal.py` are the ones most likely to require a restart.

### Where should I look if UEFN behavior seems weird?

Start with [docs/UEFN_QUIRKS.md](docs/UEFN_QUIRKS.md). That file captures the non-obvious engine behavior this repo is already compensating for.
