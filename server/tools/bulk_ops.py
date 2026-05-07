"""Bulk operations — align, distribute, randomize, snap, mirror."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register bulk operation tools on the MCP server."""

    @mcp.tool()
    def bulk_align(
        axis: Annotated[str, Field(description="Axis to align on: 'X', 'Y', or 'Z'.")] = "Z",
        mode: Annotated[str, Field(description="Alignment mode: 'min', 'max', 'center', 'average'.")] = "average",
    ) -> str:
        """Align selected actors along an axis."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "bulk_align",
            "kwargs": {"axis": axis, "mode": mode},
        }))

    @mcp.tool()
    def bulk_distribute(
        axis: Annotated[str, Field(description="Axis to distribute along: 'X', 'Y', or 'Z'.")] = "X",
    ) -> str:
        """Distribute selected actors evenly along an axis."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "bulk_distribute",
            "kwargs": {"axis": axis},
        }))

    @mcp.tool()
    def bulk_randomize(
        location_range: Annotated[Optional[list], Field(description="Max random offset [x, y, z] in cm.")] = None,
        rotation_range: Annotated[Optional[list], Field(description="Max random rotation [pitch, yaw, roll] in degrees.")] = None,
        scale_range: Annotated[Optional[list], Field(description="Scale range [min, max] as multipliers.")] = None,
    ) -> str:
        """Randomize transforms of selected actors for natural variation."""
        kwargs = {}
        if location_range:
            kwargs["location_range"] = location_range
        if rotation_range:
            kwargs["rotation_range"] = rotation_range
        if scale_range:
            kwargs["scale_range"] = scale_range
        return str(bridge.send_command("run_tool", {
            "tool_name": "bulk_randomize",
            "kwargs": kwargs,
        }))

    @mcp.tool()
    def bulk_snap_to_grid(
        grid_size: Annotated[float, Field(description="Grid size in cm.")] = 100.0,
    ) -> str:
        """Snap all selected actors to the nearest grid point."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "bulk_snap_to_grid",
            "kwargs": {"grid_size": grid_size},
        }))

    @mcp.tool()
    def bulk_mirror(
        axis: Annotated[str, Field(description="Mirror axis: 'X', 'Y', or 'Z'.")] = "X",
        pivot: Annotated[Optional[list], Field(description="Mirror pivot point [x, y, z]. Default: selection center.")] = None,
    ) -> str:
        """Mirror selected actors across an axis."""
        kwargs = {"axis": axis}
        if pivot:
            kwargs["pivot"] = pivot
        return str(bridge.send_command("run_tool", {
            "tool_name": "bulk_mirror",
            "kwargs": kwargs,
        }))
