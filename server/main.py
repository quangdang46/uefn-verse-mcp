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
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server.fastmcp import FastMCP

# Absolute imports so `python server/main.py` works (MCP stdio); relative imports
# require `python -m server.main` from repo root only.
from server import bridge
from server.tools import actors, assets, escape_hatch, system

# Initialize FastMCP
mcp = FastMCP("uefn-mcp")

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
def execute_python(code: str) -> str:
    """Execute arbitrary Python code in UEFN editor."""
    return str(bridge.send_command("execute_python", {"code": code}))

@mcp.tool()
def get_log(lines: int = 50) -> str:
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
def spawn_actor(class_path: str, location: list = None, rotation: list = None) -> str:
    """Spawn an actor from a class or object path."""
    params = {"class_path": class_path}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    return str(bridge.send_command("spawn_actor", params))

@mcp.tool()
def delete_actors(actor_labels: list) -> str:
    """Delete actors by their labels."""
    return str(bridge.send_command("delete_actors", {"actor_labels": actor_labels}))

@mcp.tool()
def set_actor_transform(actor_label: str, location: list = None, rotation: list = None, scale: list = None) -> str:
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
def get_actor_properties(actor_label: str) -> str:
    """Get properties of an actor."""
    return str(bridge.send_command("get_actor_properties", {"actor_label": actor_label}))

@mcp.tool()
def set_actor_properties(actor_label: str, properties: dict) -> str:
    """Set properties of an actor."""
    return str(bridge.send_command("set_actor_properties", {"actor_label": actor_label, "properties": properties}))

@mcp.tool()
def select_actors(actor_labels: list) -> str:
    """Select actors in the viewport."""
    return str(bridge.send_command("select_actors", {"actor_labels": actor_labels}))

@mcp.tool()
def focus_selected() -> str:
    """Focus the viewport on selected actors."""
    return str(bridge.send_command("focus_selected"))

# ─── Asset Commands ───────────────────────────────────────────────────────────

@mcp.tool()
def list_assets(directory: str = "/", recursive: bool = True, class_filter: str = "") -> str:
    """List assets in a directory."""
    params = {"directory": directory, "recursive": recursive}
    if class_filter:
        params["class_filter"] = class_filter
    return str(bridge.send_command("list_assets", params))

@mcp.tool()
def get_asset_info(asset_path: str) -> str:
    """Get detailed info about an asset."""
    return str(bridge.send_command("get_asset_info", {"asset_path": asset_path}))

@mcp.tool()
def get_selected_assets() -> str:
    """Get assets currently selected in the Content Browser."""
    return str(bridge.send_command("get_selected_assets"))

@mcp.tool()
def rename_asset(old_path: str, new_path: str) -> str:
    """Rename or move an asset."""
    return str(bridge.send_command("rename_asset", {"old_path": old_path, "new_path": new_path}))

@mcp.tool()
def delete_asset(asset_path: str) -> str:
    """Delete an asset."""
    return str(bridge.send_command("delete_asset", {"asset_path": asset_path}))

@mcp.tool()
def duplicate_asset(source_path: str, dest_path: str) -> str:
    """Duplicate an asset to a new path."""
    return str(bridge.send_command("duplicate_asset", {"source_path": source_path, "dest_path": dest_path}))

@mcp.tool()
def does_asset_exist(asset_path: str) -> str:
    """Check if an asset exists."""
    return str(bridge.send_command("does_asset_exist", {"asset_path": asset_path}))

@mcp.tool()
def save_asset(asset_path: str) -> str:
    """Save a modified asset."""
    return str(bridge.send_command("save_asset", {"asset_path": asset_path}))

@mcp.tool()
def search_assets(class_name: str = "", directory: str = "/", recursive: bool = True) -> str:
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
def set_viewport_camera(location: list = None, rotation: list = None) -> str:
    """Set viewport camera position and rotation."""
    params = {}
    if location:
        params["location"] = location
    if rotation:
        params["rotation"] = rotation
    return str(bridge.send_command("set_viewport_camera", params))

# ─── Tool Escape Hatch ────────────────────────────────────────────────────────

@mcp.tool()
def run_tool(tool_name: str, **kwargs) -> str:
    """Execute any registered uefn_tools tool by name. Use this to access the full 358 tools."""
    params = {"tool_name": tool_name}
    params.update(kwargs)
    return str(bridge.send_command("run_tool", params))

@mcp.tool()
def list_tools(category: str = "") -> str:
    """List all registered uefn_tools tools."""
    params = {}
    if category:
        params["category"] = category
    return str(bridge.send_command("list_tools", params))

@mcp.tool()
def describe_tool(tool_name: str) -> str:
    """Get details about a specific tool (parameters, description, category)."""
    return str(bridge.send_command("describe_tool", {"tool_name": tool_name}))


if __name__ == "__main__":
    mcp.run()
