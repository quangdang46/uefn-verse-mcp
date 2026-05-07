"""Verse integration tools — write, compile, debug, and generate Verse code (UEFN-specific)."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register Verse integration tools on the MCP server."""

    @mcp.tool()
    def verse_build() -> str:
        """Trigger Verse compilation and return build status with any errors."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "system_build_verse",
            "kwargs": {},
        }))

    @mcp.tool()
    def verse_get_build_log() -> str:
        """Get the most recent UEFN build log for error analysis."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "system_get_last_build_log",
            "kwargs": {},
        }))

    @mcp.tool()
    def verse_build_status(
        stale_threshold_sec: Annotated[float, Field(description="Seconds after which the log is considered stale.")] = 300.0,
    ) -> str:
        """Quick Verse build status check — SUCCESS/FAILED/UNKNOWN with staleness info."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_build_status",
            "kwargs": {"stale_threshold_sec": stale_threshold_sec},
        }))

    @mcp.tool()
    def verse_write_file(
        filename: Annotated[str, Field(description="The .verse filename (e.g. 'game_manager.verse').")],
        content: Annotated[str, Field(description="Full Verse source code to write.")],
        subdir: Annotated[str, Field(description="Optional subdirectory inside the Verse project root.")] = "",
        overwrite: Annotated[bool, Field(description="If True, overwrite existing file. If False, error on existing.")] = False,
    ) -> str:
        """Write or update a .verse file in the project's Verse source directory."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_write_file",
            "kwargs": {
                "filename": filename,
                "content": content,
                "subdir": subdir,
                "overwrite": overwrite,
            },
        }))

    @mcp.tool()
    def verse_find_project_path() -> str:
        """Auto-detect and return the Verse source directory for the current UEFN project."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_find_project_path",
            "kwargs": {},
        }))

    @mcp.tool()
    def verse_patch_errors(
        verse_file: Annotated[str, Field(description="Optional filename to always include content for, even without errors.")] = "",
    ) -> str:
        """AI error-loop tool: parse Verse build errors + read erroring file contents for one-shot fix."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_patch_errors",
            "kwargs": {"verse_file": verse_file},
        }))

    @mcp.tool()
    def verse_template_list() -> str:
        """List all available Verse game templates with descriptions and required devices."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_template_list",
            "kwargs": {},
        }))

    @mcp.tool()
    def verse_template_get(
        name: Annotated[str, Field(description="Template name from verse_template_list (e.g. 'elimination_scoring').")],
    ) -> str:
        """Get full Verse source for a named template, ready to customize and deploy."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_template_get",
            "kwargs": {"name": name},
        }))

    @mcp.tool()
    def verse_template_deploy(
        name: Annotated[str, Field(description="Template name to deploy.")],
        filename: Annotated[str, Field(description="Output .verse filename (e.g. 'zone_game.verse').")],
        custom_source: Annotated[str, Field(description="Optional custom Verse source to override template content.")] = "",
        overwrite: Annotated[bool, Field(description="If True, overwrite existing file.")] = False,
    ) -> str:
        """Deploy a Verse template directly into the project's Verse source directory."""
        kwargs = {"name": name, "filename": filename, "overwrite": overwrite}
        if custom_source:
            kwargs["custom_source"] = custom_source
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_template_deploy",
            "kwargs": kwargs,
        }))

    @mcp.tool()
    def verse_gen_game_skeleton(
        device_name: Annotated[str, Field(description="Name for the game manager device class.")] = "MyGameManager",
    ) -> str:
        """Generate a full game device skeleton with round logic, timer, scoreboard, spawn pads."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_gen_game_skeleton",
            "kwargs": {"device_name": device_name},
        }))

    @mcp.tool()
    def verse_gen_elimination_handler() -> str:
        """Generate an elimination event handler that tracks kills and updates score."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_gen_elimination_handler",
            "kwargs": {},
        }))

    @mcp.tool()
    def verse_gen_scoring_tracker(
        max_score: Annotated[int, Field(description="Maximum score to win.")] = 10,
    ) -> str:
        """Generate a scoring tracker that grants points when players enter a zone."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_gen_scoring_tracker",
            "kwargs": {"max_score": max_score},
        }))

    @mcp.tool()
    def verse_gen_custom(
        filename: Annotated[str, Field(description="Output .verse filename.")],
        content: Annotated[str, Field(description="Custom Verse code to write.")],
        overwrite: Annotated[bool, Field(description="Overwrite existing file.")] = False,
    ) -> str:
        """Write a custom Verse snippet to disk in the snippets directory."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_gen_custom",
            "kwargs": {"filename": filename, "content": content, "overwrite": overwrite},
        }))

    @mcp.tool()
    def verse_list_snippets() -> str:
        """List all generated Verse snippet files organized by subcategory."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_list_snippets",
            "kwargs": {},
        }))

    @mcp.tool()
    def verse_gen_device_declarations() -> str:
        """Generate typed Verse device declarations from currently selected actors."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_gen_device_declarations",
            "kwargs": {},
        }))

    @mcp.tool()
    def verse_get_schema(
        class_name: Annotated[str, Field(description="Verse class name to look up (e.g. 'timer_device').")],
    ) -> str:
        """Get Verse schema (properties, events, functions) for a device class from .digest files."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "api_verse_get_schema",
            "kwargs": {"class_name": class_name},
        }))

    @mcp.tool()
    def verse_refresh_schemas() -> str:
        """Force re-scan of all Verse digest files for updated schema intelligence."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "api_verse_refresh_schemas",
            "kwargs": {},
        }))
