"""Escape hatch for all 358 uefn_tools."""
import json
import os
from typing import Any

from server import bridge

# Full integration suite often exceeds the default HTTP timeout; override via env if needed.
_LONG_RUN_TOOL_SEC = float(os.environ.get("UEFN_MCP_LONG_TOOL_TIMEOUT", "900"))
_LONG_RUN_TOOLS = frozenset({"toolbelt_integration_test"})


def run_tool(tool_name: str, kwargs: dict | str | None = None, **extra: Any) -> str:
    """Execute any registered uefn_tools tool by name."""
    if kwargs is None:
        kw = dict(extra) if extra else {}
    elif isinstance(kwargs, dict):
        kw = dict(kwargs)
        kw.update(extra)
    elif isinstance(kwargs, str):
        kw = json.loads(kwargs) if kwargs.strip() else {}
        kw.update(extra)
    else:
        kw = dict(extra)
    req_timeout = _LONG_RUN_TOOL_SEC if tool_name in _LONG_RUN_TOOLS else None
    return str(
        bridge.send_command(
            "run_tool",
            {"tool_name": tool_name, "kwargs": kw},
            timeout=req_timeout,
        )
    )

def list_tools(category: str = "") -> str:
    """List all registered uefn_tools tools."""
    params = {}
    if category:
        params["category"] = category
    return str(bridge.send_command("list_tools", params))

def describe_tool(tool_name: str) -> str:
    """Get details about a specific tool."""
    return str(bridge.send_command("describe_tool", {"tool_name": tool_name}))
