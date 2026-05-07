"""Post-processing volume tools."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register post-process tools on the MCP server."""

    @mcp.tool()
    def postprocess_spawn(
        location: Annotated[Optional[list], Field(description="Volume location [x, y, z].")] = None,
        infinite_extent: Annotated[bool, Field(description="If True, affects the entire level.")] = True,
        label: Annotated[str, Field(description="Optional label for the volume.")] = "",
    ) -> str:
        """Place a post-process volume in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "postprocess_spawn",
            "kwargs": {
                "location": location,
                "infinite_extent": infinite_extent,
                "label": label,
            },
        }))

    @mcp.tool()
    def postprocess_set(
        actor_label: Annotated[str, Field(description="Label of the post-process volume.")],
        bloom_intensity: Annotated[Optional[float], Field(description="Bloom intensity.")] = None,
        exposure_compensation: Annotated[Optional[float], Field(description="Exposure compensation (EV).")] = None,
        saturation: Annotated[Optional[float], Field(description="Color saturation.")] = None,
        contrast: Annotated[Optional[float], Field(description="Color contrast.")] = None,
        vignette_intensity: Annotated[Optional[float], Field(description="Vignette effect intensity.")] = None,
    ) -> str:
        """Configure post-process volume settings."""
        kwargs = {"actor_label": actor_label}
        if bloom_intensity is not None:
            kwargs["bloom_intensity"] = bloom_intensity
        if exposure_compensation is not None:
            kwargs["exposure_compensation"] = exposure_compensation
        if saturation is not None:
            kwargs["saturation"] = saturation
        if contrast is not None:
            kwargs["contrast"] = contrast
        if vignette_intensity is not None:
            kwargs["vignette_intensity"] = vignette_intensity
        return str(bridge.send_command("run_tool", {
            "tool_name": "postprocess_set",
            "kwargs": kwargs,
        }))
