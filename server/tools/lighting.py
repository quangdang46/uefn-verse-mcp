"""Lighting tools — place, configure, and list lights."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register lighting tools on the MCP server."""

    @mcp.tool()
    def light_place(
        light_type: Annotated[str, Field(description="Light type: 'point', 'spot', 'directional', or 'rect'.")],
        location: Annotated[Optional[list], Field(description="World location [x, y, z].")] = None,
        rotation: Annotated[Optional[list], Field(description="Rotation [pitch, yaw, roll] in degrees.")] = None,
        label: Annotated[str, Field(description="Optional label for the light actor.")] = "",
    ) -> str:
        """Place a light actor (Point, Spot, Directional, or Rect) at the specified location."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "lighting_place",
            "kwargs": {
                "light_type": light_type,
                "location": location,
                "rotation": rotation,
                "label": label,
            },
        }))

    @mcp.tool()
    def light_set(
        actor_label: Annotated[str, Field(description="Label of the light actor to modify.")],
        intensity: Annotated[Optional[float], Field(description="Light intensity value.")] = None,
        color: Annotated[Optional[list], Field(description="Light color [r, g, b] (0.0-1.0).")] = None,
        radius: Annotated[Optional[float], Field(description="Attenuation radius.")] = None,
        temperature: Annotated[Optional[float], Field(description="Color temperature in Kelvin.")] = None,
    ) -> str:
        """Set properties on a light actor (intensity, color, radius, temperature)."""
        kwargs = {"actor_label": actor_label}
        if intensity is not None:
            kwargs["intensity"] = intensity
        if color is not None:
            kwargs["color"] = color
        if radius is not None:
            kwargs["radius"] = radius
        if temperature is not None:
            kwargs["temperature"] = temperature
        return str(bridge.send_command("run_tool", {
            "tool_name": "lighting_set",
            "kwargs": kwargs,
        }))

    @mcp.tool()
    def light_list() -> str:
        """List all light actors in the level with their types and properties."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "lighting_list",
            "kwargs": {},
        }))

    @mcp.tool()
    def light_bulk_adjust(
        property_name: Annotated[str, Field(description="Property to adjust: 'intensity', 'color', 'temperature'.")],
        value: Annotated[float, Field(description="New value to set.")],
        light_type: Annotated[str, Field(description="Filter by light type (e.g. 'point', 'spot'). Empty for all.")] = "",
    ) -> str:
        """Adjust a property on all lights (or filtered by type) at once."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "lighting_bulk_adjust",
            "kwargs": {
                "property_name": property_name,
                "value": value,
                "light_type": light_type,
            },
        }))
