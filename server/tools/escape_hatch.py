"""Escape hatch for all 358 uefn_tools."""
from server import bridge

def run_tool(tool_name: str, **kwargs) -> str:
    """Execute any registered uefn_tools tool by name."""
    params = {"tool_name": tool_name}
    params.update(kwargs)
    return str(bridge.send_command("run_tool", params))

def list_tools(category: str = "") -> str:
    """List all registered uefn_tools tools."""
    params = {}
    if category:
        params["category"] = category
    return str(bridge.send_command("list_tools", params))

def describe_tool(tool_name: str) -> str:
    """Get details about a specific tool."""
    return str(bridge.send_command("describe_tool", {"tool_name": tool_name}))
