"""Niagara/VFX tools — spawn, list, and configure particle systems."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register VFX/Niagara tools on the MCP server."""

    @mcp.tool()
    def niagara_spawn_system(
        system_path: Annotated[str, Field(description="Content path to the Niagara system asset.")],
        location: Annotated[Optional[list], Field(description="World location [x, y, z].")] = None,
        rotation: Annotated[Optional[list], Field(description="Rotation [pitch, yaw, roll].")] = None,
        label: Annotated[str, Field(description="Optional label for the spawned actor.")] = "",
    ) -> str:
        """Place a Niagara particle system in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "niagara_spawn_system",
            "kwargs": {
                "system_path": system_path,
                "location": location,
                "rotation": rotation,
                "label": label,
            },
        }))

    @mcp.tool()
    def niagara_list_systems(
        directory: Annotated[str, Field(description="Content path to search.")] = "/Game",
    ) -> str:
        """List all Niagara system assets in the project."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "niagara_list_systems",
            "kwargs": {"directory": directory},
        }))

    @mcp.tool()
    def niagara_set_parameter(
        actor_label: Annotated[str, Field(description="Label of the Niagara actor.")],
        parameter_name: Annotated[str, Field(description="Name of the Niagara parameter to set.")],
        value: Annotated[float, Field(description="Parameter value.")],
    ) -> str:
        """Set a parameter value on a Niagara system actor."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "niagara_bulk_set_parameter",
            "kwargs": {
                "actor_label": actor_label,
                "parameter_name": parameter_name,
                "value": value,
            },
        }))
