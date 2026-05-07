"""Audio tools — place, configure, and list audio sources."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register audio tools on the MCP server."""

    @mcp.tool()
    def audio_place(
        sound_asset: Annotated[str, Field(description="Content path to the sound asset (e.g. '/Game/Audio/MySFX').")],
        location: Annotated[Optional[list], Field(description="World location [x, y, z].")] = None,
        label: Annotated[str, Field(description="Optional label for the ambient sound actor.")] = "",
    ) -> str:
        """Place an ambient sound actor at the specified location."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "audio_place",
            "kwargs": {
                "sound_asset": sound_asset,
                "location": location,
                "label": label,
            },
        }))

    @mcp.tool()
    def audio_set(
        actor_label: Annotated[str, Field(description="Label of the audio actor to modify.")],
        volume: Annotated[Optional[float], Field(description="Volume multiplier (0.0-1.0).")] = None,
        pitch: Annotated[Optional[float], Field(description="Pitch multiplier.")] = None,
    ) -> str:
        """Set audio properties on an ambient sound actor."""
        kwargs = {"actor_label": actor_label}
        if volume is not None:
            kwargs["volume"] = volume
        if pitch is not None:
            kwargs["pitch"] = pitch
        return str(bridge.send_command("run_tool", {
            "tool_name": "audio_set",
            "kwargs": kwargs,
        }))

    @mcp.tool()
    def audio_list() -> str:
        """List all audio/ambient sound actors in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "audio_list",
            "kwargs": {},
        }))
