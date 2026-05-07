"""Screenshot and level snapshot tools."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register capture tools on the MCP server."""

    @mcp.tool()
    def screenshot_take(
        filename: Annotated[str, Field(description="Output filename (without extension).")] = "screenshot",
        resolution_x: Annotated[int, Field(description="Capture width in pixels.")] = 1920,
        resolution_y: Annotated[int, Field(description="Capture height in pixels.")] = 1080,
    ) -> str:
        """Capture a viewport screenshot and save to the project's Saved folder."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "screenshot_take",
            "kwargs": {
                "filename": filename,
                "resolution_x": resolution_x,
                "resolution_y": resolution_y,
            },
        }))

    @mcp.tool()
    def screenshot_focus_selection(
        filename: Annotated[str, Field(description="Output filename.")] = "focused_screenshot",
    ) -> str:
        """Focus viewport on selected actors and take a screenshot."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "screenshot_focus_selection",
            "kwargs": {"filename": filename},
        }))

    @mcp.tool()
    def snapshot_save(
        name: Annotated[str, Field(description="Name for the snapshot.")],
    ) -> str:
        """Save the current level state as a named snapshot (JSON serialization)."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "snapshot_save",
            "kwargs": {"name": name},
        }))

    @mcp.tool()
    def snapshot_restore(
        name: Annotated[str, Field(description="Name of the snapshot to restore.")],
    ) -> str:
        """Restore the level to a previously saved snapshot state."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "snapshot_restore",
            "kwargs": {"name": name},
        }))

    @mcp.tool()
    def snapshot_list() -> str:
        """List all available level snapshots."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "snapshot_list",
            "kwargs": {},
        }))

    @mcp.tool()
    def snapshot_diff(
        name: Annotated[str, Field(description="Snapshot name to compare against current state.")],
    ) -> str:
        """Compare the current level state against a saved snapshot."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "snapshot_diff",
            "kwargs": {"name": name},
        }))
