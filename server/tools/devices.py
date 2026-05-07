"""Fortnite Creative device tools — list, configure, call methods, smart spawn (UEFN-specific)."""
from typing import Annotated, Optional

from pydantic import Field

from server import bridge


def register(mcp):
    """Register Fortnite device tools on the MCP server."""

    # smart_spawn, search_content_browser, list_device_aliases are registered
    # as top-level tools in server/main.py — no duplication needed here.

    @mcp.tool()
    def device_list(
        name_filter: Annotated[str, Field(description="Optional substring to filter device labels.")] = "",
    ) -> str:
        """List all Verse/Creative device actors in the current level with their types and locations."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_list_devices",
            "kwargs": {"name_filter": name_filter},
        }))

    @mcp.tool()
    def device_call_method(
        method: Annotated[str, Field(description="Method name to call (e.g. 'timer_start', 'Enable', 'Disable').")],
        class_filter: Annotated[str, Field(description="Case-insensitive class name substring to match.")] = "",
        label_filter: Annotated[str, Field(description="Case-insensitive label substring to match.")] = "",
        actor_path: Annotated[str, Field(description="Exact actor path or label for single-actor targeting.")] = "",
    ) -> str:
        """Call an exposed Python method on devices matching a filter (V2 runtime control)."""
        kwargs = {"method": method}
        if class_filter:
            kwargs["class_filter"] = class_filter
        if label_filter:
            kwargs["label_filter"] = label_filter
        if actor_path:
            kwargs["actor_path"] = actor_path
        return str(bridge.send_command("run_tool", {
            "tool_name": "device_call_method",
            "kwargs": kwargs,
        }))

    @mcp.tool()
    def device_set_property(
        property_name: Annotated[str, Field(description="UPROPERTY name to set (e.g. 'bIsEnabled', 'TeamIndex').")],
        value: Annotated[str, Field(description="Value to assign (will be type-coerced).")],
        class_filter: Annotated[str, Field(description="Case-insensitive class name substring.")] = "",
        label_filter: Annotated[str, Field(description="Case-insensitive label substring.")] = "",
        actor_path: Annotated[str, Field(description="Exact actor path or label.")] = "",
    ) -> str:
        """Set a property on devices matching a filter. For V1 device properties accessible via Python."""
        kwargs = {"property_name": property_name, "value": value}
        if class_filter:
            kwargs["class_filter"] = class_filter
        if label_filter:
            kwargs["label_filter"] = label_filter
        if actor_path:
            kwargs["actor_path"] = actor_path
        return str(bridge.send_command("run_tool", {
            "tool_name": "device_set_property",
            "kwargs": kwargs,
        }))

    @mcp.tool()
    def device_bulk_set_property(
        property_name: Annotated[str, Field(description="UPROPERTY name to set on all devices.")] = "bIsEnabled",
        value: Annotated[bool, Field(description="Value to assign.")] = True,
        use_all_devices: Annotated[bool, Field(description="If True, apply to ALL devices, not just selection.")] = False,
    ) -> str:
        """Set a property on all selected (or all) Verse device actors at once."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_bulk_set_property",
            "kwargs": {
                "property_name": property_name,
                "value": value,
                "use_all_devices": use_all_devices,
            },
        }))

    @mcp.tool()
    def device_select_by_name(
        name_filter: Annotated[str, Field(description="Case-insensitive substring to match device labels.")],
    ) -> str:
        """Select all Verse device actors whose label contains the filter string."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_select_by_name",
            "kwargs": {"name_filter": name_filter},
        }))

    @mcp.tool()
    def device_select_by_class(
        class_filter: Annotated[str, Field(description="Case-insensitive class name substring (e.g. 'SpawnPad', 'Timer').")],
    ) -> str:
        """Select all Verse device actors of a given class name substring."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_select_by_class",
            "kwargs": {"class_filter": class_filter},
        }))

    @mcp.tool()
    def device_export_report() -> str:
        """Export a JSON report of all Verse device properties to the Saved folder."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "verse_export_report",
            "kwargs": {},
        }))

    @mcp.tool()
    def device_crawl_api() -> str:
        """Discover available methods and properties on selected actors via API crawl."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "api_crawl_selection",
            "kwargs": {},
        }))

    @mcp.tool()
    def device_sim_generate_proxy() -> str:
        """Generate a Python simulation proxy class for the selected Verse device."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "sim_generate_proxy",
            "kwargs": {},
        }))

    @mcp.tool()
    def device_sim_trigger_method(
        method_name: Annotated[str, Field(description="Method name to trigger on the selected device.")],
    ) -> str:
        """Trigger a discoverable method on the selected Verse device via Python API."""
        return str(bridge.send_command("run_tool", {
            "tool_name": "sim_trigger_method",
            "kwargs": {"method_name": method_name},
        }))
