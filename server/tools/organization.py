"""Actor organization & selection tools — folders, visibility, locking, filtering."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register organization and selection tools on the MCP server."""

    @mcp.tool()
    def actor_move_to_folder(
        actor_labels: Annotated[list, Field(description="List of actor labels to move.")],
        folder_path: Annotated[str, Field(description="Outliner folder path (e.g. 'Props/Trees').")],
    ) -> str:
        """Move actors to an outliner folder for organization."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "actor_move_to_folder",
            "kwargs": {"actor_labels": actor_labels, "folder_path": folder_path},
        }))

    @mcp.tool()
    def actor_hide(
        actor_labels: Annotated[list, Field(description="Actor labels to hide in the editor.")],
    ) -> str:
        """Hide actors in the editor viewport (not in-game)."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "actor_hide",
            "kwargs": {"actor_labels": actor_labels},
        }))

    @mcp.tool()
    def actor_show(
        actor_labels: Annotated[list, Field(description="Actor labels to show.")],
    ) -> str:
        """Show previously hidden actors in the editor viewport."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "actor_show",
            "kwargs": {"actor_labels": actor_labels},
        }))

    @mcp.tool()
    def actor_lock(
        actor_labels: Annotated[list, Field(description="Actor labels to lock.")],
    ) -> str:
        """Lock actor transforms to prevent accidental movement."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "actor_lock",
            "kwargs": {"actor_labels": actor_labels},
        }))

    @mcp.tool()
    def actor_unlock(
        actor_labels: Annotated[list, Field(description="Actor labels to unlock.")],
    ) -> str:
        """Unlock actor transforms to allow movement again."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "actor_unlock",
            "kwargs": {"actor_labels": actor_labels},
        }))

    @mcp.tool()
    def select_by_class(
        class_name: Annotated[str, Field(description="Exact or partial class name to select (e.g. 'StaticMeshActor').")],
    ) -> str:
        """Select all actors of a given class in the current level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "select_by_class",
            "kwargs": {"class_name": class_name},
        }))

    @mcp.tool()
    def select_by_property(
        property_name: Annotated[str, Field(description="Property name to check.")],
        value: Annotated[str, Field(description="Expected property value (string-compared).")],
    ) -> str:
        """Select actors that have a property matching a given value."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "select_by_property",
            "kwargs": {"property_name": property_name, "value": value},
        }))

    @mcp.tool()
    def actor_set_label(
        actor_label: Annotated[str, Field(description="Current actor label (identifier).")],
        new_label: Annotated[str, Field(description="New label to assign.")],
    ) -> str:
        """Rename an actor's label in the outliner."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "actor_set_label",
            "kwargs": {"actor_label": actor_label, "new_label": new_label},
        }))

    @mcp.tool()
    def smart_organize() -> str:
        """Auto-organize level actors into outliner folders by class type."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "smart_organize",
            "kwargs": {},
        }))
