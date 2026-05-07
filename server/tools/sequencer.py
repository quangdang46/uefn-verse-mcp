"""Sequencer tools — keyframes, spline tracks, animation."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register sequencer tools on the MCP server."""

    @mcp.tool()
    def seq_batch_keyframe(
        actor_label: Annotated[str, Field(description="Actor label to keyframe.")],
        keyframes: Annotated[list, Field(description="List of keyframe dicts: [{'time': float, 'location': [x,y,z], 'rotation': [p,y,r]}].")],
    ) -> str:
        """Batch-add keyframes to a sequencer track for an actor."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "seq_batch_keyframe",
            "kwargs": {"actor_label": actor_label, "keyframes": keyframes},
        }))

    @mcp.tool()
    def seq_actor_to_spline(
        actor_label: Annotated[str, Field(description="Actor whose path to convert to a spline track.")],
    ) -> str:
        """Convert an actor's movement path to a spline-based sequencer track."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "seq_actor_to_spline",
            "kwargs": {"actor_label": actor_label},
        }))
