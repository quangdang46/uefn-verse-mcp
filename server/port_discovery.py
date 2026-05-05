"""
Port discovery for the in-editor HTTP MCP listener (8765–8770).

Scans in order and returns the first port whose GET `/` returns JSON with
``status == "ok"``. That matches both ``uefn_tools`` ``mcp_bridge`` and any
other listener that copied the same ping shape — if multiple are running,
the lowest port wins.
"""
from typing import Optional

DEFAULT_PORT = 8765
MAX_PORT = 8770
_discovered_port: Optional[int] = None


def discover_port() -> int:
    """Find the listener by scanning the port range. Caches result."""
    global _discovered_port

    if _discovered_port is not None:
        if _ping_port(_discovered_port):
            return _discovered_port
        _discovered_port = None

    for port in range(DEFAULT_PORT, MAX_PORT + 1):
        if _ping_port(port):
            _discovered_port = port
            return port

    raise ConnectionError(
        f"UEFN listener not found on ports {DEFAULT_PORT}-{MAX_PORT}. "
        "Start it in the UEFN console: import uefn_tools as ut; ut.register(); ut.run('mcp_start')"
    )


def _ping_port(port: int) -> bool:
    """Check if a listener responds on the given port."""
    try:
        import urllib.request
        req = urllib.request.Request(f"http://127.0.0.1:{port}")
        with urllib.request.urlopen(req, timeout=1.0) as resp:
            import json
            body = json.loads(resp.read().decode())
            return body.get("status") == "ok"
    except Exception:
        return False
