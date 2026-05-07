"""Procedural placement tools — patterns, scatter, PCG."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register procedural placement tools on the MCP server."""

    @mcp.tool()
    def pattern_grid(
        asset_path: Annotated[str, Field(description="Content path of the asset to place.")],
        rows: Annotated[int, Field(description="Number of rows.")] = 5,
        columns: Annotated[int, Field(description="Number of columns.")] = 5,
        spacing: Annotated[float, Field(description="Distance between instances in cm.")] = 200.0,
        origin: Annotated[Optional[list], Field(description="Grid origin [x, y, z].")] = None,
    ) -> str:
        """Place actors in a grid pattern."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "pattern_grid",
            "kwargs": {
                "asset_path": asset_path,
                "rows": rows,
                "columns": columns,
                "spacing": spacing,
                "origin": origin,
            },
        }))

    @mcp.tool()
    def pattern_circle(
        asset_path: Annotated[str, Field(description="Content path of the asset to place.")],
        count: Annotated[int, Field(description="Number of instances around the circle.")] = 8,
        radius: Annotated[float, Field(description="Circle radius in cm.")] = 500.0,
        center: Annotated[Optional[list], Field(description="Circle center [x, y, z].")] = None,
    ) -> str:
        """Place actors in a circular pattern."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "pattern_circle",
            "kwargs": {
                "asset_path": asset_path,
                "count": count,
                "radius": radius,
                "center": center,
            },
        }))

    @mcp.tool()
    def pattern_line(
        asset_path: Annotated[str, Field(description="Content path of the asset to place.")],
        count: Annotated[int, Field(description="Number of instances along the line.")] = 10,
        start: Annotated[Optional[list], Field(description="Line start [x, y, z].")] = None,
        end: Annotated[Optional[list], Field(description="Line end [x, y, z].")] = None,
    ) -> str:
        """Place actors evenly along a line."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "pattern_line",
            "kwargs": {
                "asset_path": asset_path,
                "count": count,
                "start": start,
                "end": end,
            },
        }))

    @mcp.tool()
    def scatter_props(
        asset_path: Annotated[str, Field(description="Content path of the asset to scatter.")],
        count: Annotated[int, Field(description="Number of instances to scatter.")] = 50,
        radius: Annotated[float, Field(description="Scatter radius in cm.")] = 2000.0,
        center: Annotated[Optional[list], Field(description="Scatter center [x, y, z].")] = None,
        randomize_rotation: Annotated[bool, Field(description="Randomize yaw rotation.")] = True,
        randomize_scale: Annotated[bool, Field(description="Randomize scale within range.")] = False,
        scale_min: Annotated[float, Field(description="Minimum scale factor.")] = 0.8,
        scale_max: Annotated[float, Field(description="Maximum scale factor.")] = 1.2,
    ) -> str:
        """Scatter props randomly within a radius."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "scatter_props",
            "kwargs": {
                "asset_path": asset_path,
                "count": count,
                "radius": radius,
                "center": center,
                "randomize_rotation": randomize_rotation,
                "randomize_scale": randomize_scale,
                "scale_min": scale_min,
                "scale_max": scale_max,
            },
        }))

    @mcp.tool()
    def scatter_along_spline(
        asset_path: Annotated[str, Field(description="Content path of the asset to scatter.")],
        spline_actor_label: Annotated[str, Field(description="Label of the spline actor to scatter along.")],
        count: Annotated[int, Field(description="Number of instances.")] = 20,
    ) -> str:
        """Scatter props along a spline path."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "spline_place_props",
            "kwargs": {
                "asset_path": asset_path,
                "spline_actor_label": spline_actor_label,
                "count": count,
            },
        }))
