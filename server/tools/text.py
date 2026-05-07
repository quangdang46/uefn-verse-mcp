"""Text and sign tools."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register text and sign tools on the MCP server."""

    @mcp.tool()
    def sign_list() -> str:
        """List all text/sign actors in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "sign_list",
            "kwargs": {},
        }))

    @mcp.tool()
    def sign_set_text(
        actor_label: Annotated[str, Field(description="Label of the sign/text actor.")],
        text: Annotated[str, Field(description="Text content to display.")],
    ) -> str:
        """Set text content on a sign or text actor."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "sign_set_text",
            "kwargs": {"actor_label": actor_label, "text": text},
        }))

    @mcp.tool()
    def sign_spawn_bulk(
        texts: Annotated[list, Field(description="List of text strings to create signs for.")],
        start_location: Annotated[Optional[list], Field(description="Starting location [x, y, z].")] = None,
        spacing: Annotated[float, Field(description="Spacing between signs in cm.")] = 300.0,
    ) -> str:
        """Spawn multiple sign actors with specified texts."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "sign_spawn_bulk",
            "kwargs": {
                "texts": texts,
                "start_location": start_location,
                "spacing": spacing,
            },
        }))
