"""
uefn_mcp — FastMCP Server
=========================================
External MCP server that connects Claude Code to the UEFN editor.

Usage:
    python server/main.py          # MCP stdio (repo root on sys.path via __file__)
    python -m server.main         # same, from repo root

Requirements:
    pip install mcp

Configuration (.mcp.json):
    {
      "mcpServers": {
        "uefn": {
          "command": "python",
          "args": ["/path/to/server/main.py"]
        }
      }
    }

Then in UEFN console:
    import uefn_tools as ut; ut.run("mcp_start")
"""
import json
import os
import sys
from typing import Annotated

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP
from pydantic import Field

# Absolute imports so `python server/main.py` works (MCP stdio); relative imports
# require `python -m server.main` from repo root only.
from server import bridge
from server.tools import (
    actors,
    assets,
    audio,
    blueprints,
    bulk_ops,
    capture,
    devices,
    editor_control,
    escape_hatch,
    landscape,
    lighting,
    materials,
    optimization,
    organization,
    postprocess,
    procedural,
    sequencer,
    text,
    utility,
    verse,
    vfx,
    world,
)

# Initialize FastMCP
mcp = FastMCP("uefn-mcp")

# Register all expanded tool modules
_tool_modules = [
    actors, assets, audio, blueprints, bulk_ops, capture, devices,
    editor_control, escape_hatch, landscape, lighting, materials,
    optimization, organization, postprocess, procedural, sequencer,
    text, utility, verse, vfx, world,
]
for _mod in _tool_modules:
    if hasattr(_mod, "register"):
        _mod.register(mcp)

# ─── System Commands ──────────────────────────────────────────────────────────

@mcp.tool()
def ping() -> str:
    """Health check — verify connection to UEFN."""
    return str(bridge.ping())

@mcp.tool()
def get_status() -> str:
    """Get MCP listener status."""
    return str(bridge.get_status())

@mcp.tool()
def execute_python(
    code: Annotated[str, Field(description="Python source executed in the UEFN editor Python environment.")],
) -> str:
    """Execute arbitrary Python code in UEFN editor."""
    return str(bridge.send_command("execute_python", {"code": code}))

@mcp.tool()
def get_log(
    lines: Annotated[int, Field(description="Maximum number of recent log lines to return.")] = 50,
) -> str:
    """Get MCP listener log entries."""
    return str(bridge.send_command("get_log", {"lines": lines}))

@mcp.tool()
def shutdown() -> str:
    """Stop the MCP listener."""
    return str(bridge.send_command("shutdown"))

# ─── Actor Commands ───────────────────────────────────────────────────────────

@mcp.tool()
def get_all_actors() -> str:
    """Get all actors in the current level."""
    return str(bridge.send_command("get_all_actors"))

@mcp.tool()
def get_selected_actors() -> str:
    """Get currently selected actors."""
    return str(bridge.send_command("get_selected_actors"))

@mcp.tool()
def smart_spawn(
    name: Annotated[str, Field(description="Natural device name (e.g. 'button', 'timer', 'spawn pad') OR an exact Content Browser path.")],
    location: Annotated[list | None, Field(description="World location [x, y, z]. Defaults to origin.")] = None,
    rotation: Annotated[list | None, Field(description="Rotation [pitch, yaw, roll] in degrees.")] = None,
    label: Annotated[str, Field(description="Optional outliner label for the spawned actor.")] = "",
    dry_run: Annotated[bool, Field(description="If True, only resolve the path without spawning.")] = False,
) -> str:
    """Spawn a device/actor by natural name — no hardcoded paths needed.

    Accepts names like 'button', 'timer', 'teleporter', 'spawn pad' and resolves
    them automatically. Also accepts exact Content Browser paths.

    Resolution: device aliases → exact path → class prefix search → Content Browser fuzzy search.
    """
    params = {"name": name}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    if label:
        params["label"] = label
    if dry_run:
        params["dry_run"] = dry_run
    return str(bridge.send_command("smart_spawn", params))

@mcp.tool()
def spawn_actor(
    class_path: Annotated[str, Field(description="Unreal class or object path to spawn (e.g. blueprint or actor class).")],
    location: Annotated[list | None, Field(description="Optional world location [x, y, z]; omit to use default spawn point.")] = None,
    rotation: Annotated[list | None, Field(description="Optional rotation [pitch, yaw, roll] in degrees.")] = None,
) -> str:
    """Spawn an actor from an exact class or object path. Prefer smart_spawn for natural name resolution."""
    params = {"class_path": class_path}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    return str(bridge.send_command("spawn_actor", params))

@mcp.tool()
def delete_actors(
    actor_labels: Annotated[list, Field(description="Actor labels (identifiers) to remove from the level.")],
) -> str:
    """Delete actors by their labels."""
    return str(bridge.send_command("delete_actors", {"actor_labels": actor_labels}))

@mcp.tool()
def set_actor_transform(
    actor_label: Annotated[str, Field(description="Label of the actor to modify.")],
    location: Annotated[list | None, Field(description="Optional new world location [x, y, z].")] = None,
    rotation: Annotated[list | None, Field(description="Optional new rotation [pitch, yaw, roll] in degrees.")] = None,
    scale: Annotated[list | None, Field(description="Optional new scale [x, y, z].")] = None,
) -> str:
    """Set actor transform (location, rotation, scale)."""
    params = {"actor_label": actor_label}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    if scale:
        params["scale"] = scale
    return str(bridge.send_command("set_actor_transform", params))

@mcp.tool()
def get_actor_properties(
    actor_label: Annotated[str, Field(description="Label of the actor to inspect.")],
) -> str:
    """Get properties of an actor."""
    return str(bridge.send_command("get_actor_properties", {"actor_label": actor_label}))

@mcp.tool()
def set_actor_properties(
    actor_label: Annotated[str, Field(description="Label of the actor to update.")],
    properties: Annotated[dict, Field(description="Property names and values to set on the actor (engine-specific keys).")],
) -> str:
    """Set properties of an actor."""
    return str(bridge.send_command("set_actor_properties", {"actor_label": actor_label, "properties": properties}))

@mcp.tool()
def select_actors(
    actor_labels: Annotated[list, Field(description="Actor labels to select in the editor viewport.")],
) -> str:
    """Select actors in the viewport."""
    return str(bridge.send_command("select_actors", {"actor_labels": actor_labels}))

@mcp.tool()
def focus_selected() -> str:
    """Focus the viewport on selected actors."""
    return str(bridge.send_command("focus_selected"))

# ─── Asset Commands ───────────────────────────────────────────────────────────

@mcp.tool()
def list_assets(
    directory: Annotated[str, Field(description="Content path root (e.g. '/Game' or '/').")] = "/",
    recursive: Annotated[bool, Field(description="If true, list assets under subfolders.")] = True,
    class_filter: Annotated[str, Field(description="Optional Unreal class name filter; empty returns all classes.")] = "",
) -> str:
    """List assets in a directory."""
    params = {"directory": directory, "recursive": recursive}
    if class_filter:
        params["class_filter"] = class_filter
    return str(bridge.send_command("list_assets", params))

@mcp.tool()
def get_asset_info(
    asset_path: Annotated[str, Field(description="Full content path of the asset (e.g. '/Game/MyFolder/MyAsset').")],
) -> str:
    """Get detailed info about an asset."""
    return str(bridge.send_command("get_asset_info", {"asset_path": asset_path}))

@mcp.tool()
def get_selected_assets() -> str:
    """Get assets currently selected in the Content Browser."""
    return str(bridge.send_command("get_selected_assets"))

@mcp.tool()
def rename_asset(
    old_path: Annotated[str, Field(description="Current asset content path.")],
    new_path: Annotated[str, Field(description="Destination content path (rename or move).")],
) -> str:
    """Rename or move an asset."""
    return str(bridge.send_command("rename_asset", {"old_path": old_path, "new_path": new_path}))

@mcp.tool()
def delete_asset(
    asset_path: Annotated[str, Field(description="Content path of the asset to delete.")],
) -> str:
    """Delete an asset."""
    return str(bridge.send_command("delete_asset", {"asset_path": asset_path}))

@mcp.tool()
def duplicate_asset(
    source_path: Annotated[str, Field(description="Content path of the asset to copy.")],
    dest_path: Annotated[str, Field(description="Content path for the duplicated asset.")],
) -> str:
    """Duplicate an asset to a new path."""
    return str(bridge.send_command("duplicate_asset", {"source_path": source_path, "dest_path": dest_path}))

@mcp.tool()
def does_asset_exist(
    asset_path: Annotated[str, Field(description="Content path to test for existence.")],
) -> str:
    """Check if an asset exists."""
    return str(bridge.send_command("does_asset_exist", {"asset_path": asset_path}))

@mcp.tool()
def save_asset(
    asset_path: Annotated[str, Field(description="Content path of the dirty asset to save.")],
) -> str:
    """Save a modified asset."""
    return str(bridge.send_command("save_asset", {"asset_path": asset_path}))

@mcp.tool()
def search_assets(
    class_name: Annotated[str, Field(description="Filter by asset class name; empty string searches all classes.")] = "",
    directory: Annotated[str, Field(description="Content Browser root path to search under (e.g. '/Game').")] = "/",
    recursive: Annotated[bool, Field(description="If true, include assets in subfolders.")] = True,
) -> str:
    """Search assets using the Asset Registry."""
    return str(bridge.send_command("search_assets", {"class_name": class_name, "directory": directory, "recursive": recursive}))

# ─── Project / Level Commands ─────────────────────────────────────────────────

@mcp.tool()
def get_project_info() -> str:
    """Get project info."""
    return str(bridge.send_command("get_project_info"))

@mcp.tool()
def save_current_level() -> str:
    """Save the current level."""
    return str(bridge.send_command("save_current_level"))

@mcp.tool()
def get_level_info() -> str:
    """Get level info (actor count, etc)."""
    return str(bridge.send_command("get_level_info"))

# ─── Viewport Commands ────────────────────────────────────────────────────────

@mcp.tool()
def get_viewport_camera() -> str:
    """Get viewport camera position and rotation."""
    return str(bridge.send_command("get_viewport_camera"))

@mcp.tool()
def set_viewport_camera(
    location: Annotated[list | None, Field(description="Optional camera world location [x, y, z].")] = None,
    rotation: Annotated[list | None, Field(description="Optional camera rotation [pitch, yaw, roll] in degrees.")] = None,
) -> str:
    """Set viewport camera position and rotation."""
    params = {}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    return str(bridge.send_command("set_viewport_camera", params))

# ─── Tool Escape Hatch ────────────────────────────────────────────────────────

@mcp.tool()
def run_tool(
    tool_name: Annotated[str, Field(description="Registered uefn_tools name (e.g. from list_tools).")],
    kwargs: Annotated[
        str | dict | None,
        Field(description="Tool arguments as a dict or JSON string; forwarded to the bridge as the tool's kwargs object."),
    ] = None,
) -> str:
    """Execute any registered uefn_tools tool by name. Use this to access the full 358 tools.

    Pass tool arguments as JSON in `kwargs` (string or dict); they are forwarded to the bridge
    as the single `kwargs` object expected by `_c_run_tool`.
    """
    if kwargs is None:
        kw: dict = {}
    elif isinstance(kwargs, dict):
        kw = dict(kwargs)
    elif isinstance(kwargs, str):
        kw = json.loads(kwargs) if kwargs.strip() else {}
    else:
        kw = {}
    return str(bridge.send_command("run_tool", {"tool_name": tool_name, "kwargs": kw}))

@mcp.tool()
def list_tools(
    category: Annotated[str, Field(description="If non-empty, only list tools in this category name.")] = "",
) -> str:
    """List all registered uefn_tools tools."""
    params = {}
    if category:
        params["category"] = category
    return str(bridge.send_command("list_tools", params))

@mcp.tool()
def describe_tool(
    tool_name: Annotated[str, Field(description="Registered tool name to look up in the manifest.")],
) -> str:
    """Get details about a specific tool (parameters, description, category)."""
    return str(bridge.send_command("describe_tool", {"tool_name": tool_name}))


if __name__ == "__main__":
    mcp.run()
