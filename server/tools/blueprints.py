"""Blueprint inspection tools — list, inspect, compile (read-only in UEFN)."""
from typing import Annotated

from pydantic import Field

from server import bridge


def register(mcp):
    """Register blueprint tools on the MCP server."""

    @mcp.tool()
    def blueprint_list(
        directory: Annotated[str, Field(description="Content path to search (e.g. '/Game').")] = "/Game",
    ) -> str:
        """List all Blueprint assets in the project."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "blueprint_list",
            "kwargs": {"directory": directory},
        }))

    @mcp.tool()
    def blueprint_inspect(
        asset_path: Annotated[str, Field(description="Content path to the Blueprint asset.")],
    ) -> str:
        """Get Blueprint details (parent class, components, variables)."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "blueprint_inspect",
            "kwargs": {"asset_path": asset_path},
        }))

    @mcp.tool()
    def blueprint_compile(
        asset_path: Annotated[str, Field(description="Content path to the Blueprint to compile.")],
    ) -> str:
        """Compile a Blueprint asset and return compilation status."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "blueprint_compile_folder",
            "kwargs": {"asset_path": asset_path},
        }))
