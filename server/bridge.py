"""HTTP client for the uefn_tools MCP bridge (mcp_start in UEFN)."""
import json
import os
import threading
import time
import urllib.error
import urllib.request
from typing import Any, Optional

from server.port_discovery import discover_port

REQUEST_TIMEOUT = float(os.environ.get("UEFN_MCP_REQUEST_TIMEOUT", "30"))

# Serialize outbound MCP HTTP calls so parallel Cursor/tool threads cannot stampede UEFN.
_SEND_LOCK = threading.RLock()

def _client_cooldown_sec() -> float:
    try:
        return max(0.0, float(os.environ.get("UEFN_MCP_CLIENT_COOLDOWN_SEC", "0") or "0"))
    except (TypeError, ValueError):
        return 0.0


def send_command(
    command: str,
    params: Optional[dict] = None,
    *,
    timeout: Optional[float] = None,
) -> dict:
    """Send a command to the UEFN listener and return the result."""
    with _SEND_LOCK:
        deadline = REQUEST_TIMEOUT if timeout is None else timeout
        port = discover_port()
        url = f"http://127.0.0.1:{port}"

        payload = json.dumps({"command": command, "params": params or {}}).encode()
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=deadline) as resp:
                body = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            try:
                raw_txt = e.read().decode()
                err_body = json.loads(raw_txt)
            except Exception:
                raise RuntimeError(
                    f"UEFN HTTP {e.code} for '{command}' ({e.reason}). "
                    "Queue may be saturated — retry shortly."
                ) from e
            msg = err_body.get("error", raw_txt)
            raise RuntimeError(f"UEFN command '{command}' failed: {msg}") from None
        except urllib.error.URLError as e:
            # Port may have changed — retry once
            from server.port_discovery import _discovered_port as _dp
            if _dp is not None:
                from server.port_discovery import discover_port as _disc
                _disc()
                return send_command(command, params, timeout=timeout)
            raise ConnectionError(
                "UEFN listener is not running. "
                "Start it in the UEFN console: import uefn_tools as ut; ut.register(); ut.run('mcp_start')"
            ) from e
        except Exception as e:
            if "timed out" in str(e).lower():
                raise TimeoutError(f"Command '{command}' timed out after {deadline}s") from e
            raise

        if not body.get("success", False):
            error_msg = body.get("error", "Unknown error")
            raise RuntimeError(f"UEFN command '{command}' failed: {error_msg}")

        cd = _client_cooldown_sec()
        if cd > 0:
            time.sleep(cd)

        return body.get("result", {})


def ping() -> dict:
    """Quick health check."""
    return send_command("ping")


def get_status() -> dict:
    """Get listener status."""
    return send_command("mcp_status")
