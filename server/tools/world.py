"""World state and zone tools."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register world and zone tools on the MCP server."""

    @mcp.tool()
    def world_state_export() -> str:
        """Export full world state (all actors with properties) as JSON for AI analysis."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "world_state_export",
            "kwargs": {},
        }))

    @mcp.tool()
    def zone_spawn(
        zone_type: Annotated[str, Field(description="Zone type: 'box', 'sphere', or 'cylinder'.")] = "box",
        location: Annotated[Optional[list], Field(description="Zone center [x, y, z].")] = None,
        extent: Annotated[Optional[list], Field(description="Zone extent [x, y, z] in cm.")] = None,
        label: Annotated[str, Field(description="Optional zone label.")] = "",
    ) -> str:
        """Create a zone volume in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "zone_spawn",
            "kwargs": {
                "zone_type": zone_type,
                "location": location,
                "extent": extent,
                "label": label,
            },
        }))

    @mcp.tool()
    def zone_list() -> str:
        """List all zone/volume actors in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "zone_list",
            "kwargs": {},
        }))

    @mcp.tool()
    def zone_select_contents(
        zone_label: Annotated[str, Field(description="Label of the zone to select contents of.")],
    ) -> str:
        """Select all actors inside a zone volume."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "zone_select_contents",
            "kwargs": {"zone_label": zone_label},
        }))

    @mcp.tool()
    def proximity_find(
        actor_label: Annotated[str, Field(description="Reference actor label.")],
        radius: Annotated[float, Field(description="Search radius in cm.")] = 1000.0,
        class_filter: Annotated[str, Field(description="Optional class name filter.")] = "",
    ) -> str:
        """Find all actors within a radius of a reference actor."""
        kwargs = {"actor_label": actor_label, "radius": radius}
        if class_filter:
            kwargs["class_filter"] = class_filter
        return str(bridge.send_command("run_tool", {
            "tool_name": "proximity_find",
            "kwargs": kwargs,
        }))
