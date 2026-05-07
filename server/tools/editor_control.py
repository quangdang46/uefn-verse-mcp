"""Editor control tools — undo, redo, batch execution, history."""
from typing import Annotated

from pydantic import Field

from server import bridge


def register(mcp):
    """Register editor control tools on the MCP server."""

    @mcp.tool()
    def undo() -> str:
        """Undo the last editor action via the transaction system."""
        return str(bridge.send_command("undo"))

    @mcp.tool()
    def redo() -> str:
        """Redo the last undone editor action."""
        return str(bridge.send_command("redo"))

    @mcp.tool()
    def batch_exec(
        commands: Annotated[
            list,
            Field(
                description=(
                    'List of command dicts to execute in sequence within one editor tick. '
                    'Each dict: {"command": "name", "params": {...}}. '
                    'Example: [{"command": "spawn_actor", "params": {"class_path": "..."}}, '
                    '{"command": "save_current_level", "params": {}}]'
                )
            ),
        ],
    ) -> str:
        """Execute multiple bridge commands in a single editor tick — faster than sending one-by-one."""
        return str(bridge.send_command("batch_exec", {"commands": commands}))

    @mcp.tool()
    def command_history(
        tail: Annotated[int, Field(description="Number of recent commands to return.")] = 30,
    ) -> str:
        """Return recent MCP command history with per-command timing."""
        return str(bridge.send_command("history", {"tail": tail}))
