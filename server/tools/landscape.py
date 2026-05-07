"""Landscape tools — info, listing, material assignment."""
from typing import Annotated

from pydantic import Field

from server import bridge


def register(mcp):
    """Register landscape tools on the MCP server."""

    @mcp.tool()
    def landscape_info() -> str:
        """Get landscape details (size, layers, material) for the current level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "landscape_info",
            "kwargs": {},
        }))

    @mcp.tool()
    def landscape_list() -> str:
        """List all landscape actors in the current level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "landscape_list",
            "kwargs": {},
        }))

    @mcp.tool()
    def landscape_set_material(
        material_path: Annotated[str, Field(description="Content path to the landscape material.")],
        landscape_label: Annotated[str, Field(description="Label of the landscape actor. Empty for first found.")] = "",
    ) -> str:
        """Set the material on a landscape actor."""
        kwargs = {"material_path": material_path}
        if landscape_label:
            kwargs["landscape_label"] = landscape_label
        return str(bridge.send_command("run_tool", {
            "tool_name": "landscape_set_material",
            "kwargs": kwargs,
        }))
