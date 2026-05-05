"""System commands."""
from server import bridge

def ping() -> str:
    """Health check."""
    return str(bridge.ping())

def get_log(lines: int = 50) -> str:
    """Get listener log entries."""
    result = bridge.send_command("get_log", {"lines": lines})
    return str(result)

def execute_python(code: str) -> str:
    """Execute arbitrary Python code in UEFN."""
    result = bridge.send_command("execute_python", {"code": code})
    return str(result)

def shutdown() -> str:
    """Stop the MCP listener."""
    return str(bridge.send_command("shutdown"))

def get_status() -> str:
    """Get listener status."""
    return str(bridge.get_status())
