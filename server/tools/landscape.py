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
            # uefn_tools tool expects `label`
            kwargs["label"] = landscape_label
        return str(bridge.send_command("run_tool", {
            "tool_name": "landscape_set_material",
            "kwargs": kwargs,
        }))

    @mcp.tool()
    def landscape_create(
        label: Annotated[str, Field(description="Outliner label for the landscape actor.")] = "mountain",
        location: Annotated[list | None, Field(description="Spawn location [x, y, z].")] = None,
        rotation: Annotated[list | None, Field(description="Spawn rotation [pitch, yaw, roll].")] = None,
        material_path: Annotated[str, Field(description="Optional landscape material path to apply after creation.")] = "",
        keep_placeholder: Annotated[bool, Field(description="If true, keep LandscapePlaceholder actor when creation is blocked.")] = False,
    ) -> str:
        """Attempt to create a real Landscape actor (UEFN may return LandscapePlaceholder)."""
        kwargs = {"label": label, "keep_placeholder": keep_placeholder}
        if location is not None:
            kwargs["location"] = location
        if rotation is not None:
            kwargs["rotation"] = rotation
        if material_path:
            kwargs["material_path"] = material_path
        return str(bridge.send_command("run_tool", {
            "tool_name": "landscape_create",
            "kwargs": kwargs,
        }))
