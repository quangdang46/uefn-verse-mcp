"""Utility tools — tags, config, measurement, spline helpers."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register utility tools on the MCP server."""

    @mcp.tool()
    def tag_add(
        actor_label: Annotated[str, Field(description="Actor label to tag.")],
        tag: Annotated[str, Field(description="Gameplay tag to add.")],
    ) -> str:
        """Add a gameplay tag to an actor."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "tag_add",
            "kwargs": {"actor_label": actor_label, "tag": tag},
        }))

    @mcp.tool()
    def tag_remove(
        actor_label: Annotated[str, Field(description="Actor label to remove tag from.")],
        tag: Annotated[str, Field(description="Gameplay tag to remove.")],
    ) -> str:
        """Remove a gameplay tag from an actor."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "tag_remove",
            "kwargs": {"actor_label": actor_label, "tag": tag},
        }))

    @mcp.tool()
    def tag_search(
        tag: Annotated[str, Field(description="Gameplay tag to search for.")],
    ) -> str:
        """Find all actors with a specific gameplay tag."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "tag_search",
            "kwargs": {"tag": tag},
        }))

    @mcp.tool()
    def measure_distance(
        actor_a: Annotated[str, Field(description="Label of the first actor.")],
        actor_b: Annotated[str, Field(description="Label of the second actor.")],
    ) -> str:
        """Measure the distance between two actors."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "measure_distance",
            "kwargs": {"actor_a": actor_a, "actor_b": actor_b},
        }))

    @mcp.tool()
    def spline_place_props(
        spline_label: Annotated[str, Field(description="Label of the spline actor.")],
        asset_path: Annotated[str, Field(description="Content path of the asset to place along spline.")],
        count: Annotated[int, Field(description="Number of instances to place.")] = 10,
        randomize_rotation: Annotated[bool, Field(description="Randomize yaw rotation.")] = True,
    ) -> str:
        """Place props evenly along a spline actor."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "spline_place_props",
            "kwargs": {
                "spline_label": spline_label,
                "asset_path": asset_path,
                "count": count,
                "randomize_rotation": randomize_rotation,
            },
        }))

    @mcp.tool()
    def spline_export_json(
        spline_label: Annotated[str, Field(description="Label of the spline actor to export.")],
    ) -> str:
        """Export spline point data as JSON."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "spline_export_json",
            "kwargs": {"spline_label": spline_label},
        }))

    @mcp.tool()
    def spline_to_verse_patrol(
        spline_label: Annotated[str, Field(description="Label of the spline to convert.")],
        filename: Annotated[str, Field(description="Output .verse filename.")] = "patrol_path.verse",
    ) -> str:
        """Convert a spline actor to a Verse patrol path device with waypoints."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "spline_to_verse_patrol",
            "kwargs": {"spline_label": spline_label, "filename": filename},
        }))

    @mcp.tool()
    def config_get(
        key: Annotated[str, Field(description="Config key to read (e.g. 'verse.project_path').")] = "",
    ) -> str:
        """Get toolbelt configuration value(s)."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "config_get",
            "kwargs": {"key": key},
        }))

    @mcp.tool()
    def config_set(
        key: Annotated[str, Field(description="Config key to set.")],
        value: Annotated[str, Field(description="Value to assign.")],
    ) -> str:
        """Set a toolbelt configuration value."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "config_set",
            "kwargs": {"key": key, "value": value},
        }))

    @mcp.tool()
    def viewport_orbit(
        actor_label: Annotated[str, Field(description="Actor to orbit around.")],
        distance: Annotated[float, Field(description="Distance from the actor in cm.")] = 500.0,
        angle: Annotated[float, Field(description="Orbit angle in degrees.")] = 0.0,
    ) -> str:
        """Move the viewport camera to orbit around a specific actor."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "viewport_orbit",
            "kwargs": {
                "actor_label": actor_label,
                "distance": distance,
                "angle": angle,
            },
        }))
