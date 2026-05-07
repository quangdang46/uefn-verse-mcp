"""Optimization and audit tools — memory, Nanite, publish requirements."""
from typing import Annotated

from pydantic import Field

from server import bridge


def register(mcp):
    """Register optimization tools on the MCP server."""

    @mcp.tool()
    def memory_scan() -> str:
        """Scan the level for memory-heavy assets and report usage."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "memory_scan",
            "kwargs": {},
        }))

    @mcp.tool()
    def memory_top_offenders(
        limit: Annotated[int, Field(description="Number of top memory consumers to return.")] = 20,
    ) -> str:
        """List the top memory-consuming assets in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "memory_top_offenders",
            "kwargs": {"limit": limit},
        }))

    @mcp.tool()
    def nanite_audit() -> str:
        """Audit Nanite mesh status for all static meshes in the level."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "nanite_audit",
            "kwargs": {},
        }))

    @mcp.tool()
    def publish_audit() -> str:
        """Check the level against Fortnite Creative publishing requirements."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "publish_audit",
            "kwargs": {},
        }))

    @mcp.tool()
    def level_health_check() -> str:
        """Run a comprehensive health check on the level (overlaps, errors, warnings)."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "level_health_check",
            "kwargs": {},
        }))

    @mcp.tool()
    def reference_audit(
        asset_path: Annotated[str, Field(description="Content path to audit references for.")] = "",
    ) -> str:
        """Audit asset references — find unused assets or circular dependencies."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "reference_audit",
            "kwargs": {"asset_path": asset_path},
        }))
