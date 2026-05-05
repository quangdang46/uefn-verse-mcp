"""
uefn_listener.py — MCP HTTP Listener for UEFN Editor
=========================================
Runs an HTTP server on a background thread inside the UEFN editor.
All unreal.* API calls are dispatched to the main thread via tick callback.

Architecture:
    Claude Code  <-- stdio -->  mcp_server.py (external)
                                      |
                                   HTTP POST 127.0.0.1:8765
                                      |
                          UEFN editor process (this file)
                          ├── HTTP daemon thread (receives commands)
                          ├── queue.Queue (cross-thread handoff)
                          └── register_slate_post_tick_callback
                              (drains queue on main thread, calls unreal.*)

Usage:
    # From UEFN console:
    import uefn_tools as ut; ut.run("mcp_start")

    # Or auto-start via init_unreal.py

Port range:
    Auto-detects a free port in 8765-8770.
"""

from __future__ import annotations

import io
import json
import queue
import socket
import sys
import threading
import time
import traceback
from collections import deque
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Callable, Dict, List, Optional

import unreal

# ─── Configuration ────────────────────────────────────────────────────────────

PROTOCOL_VERSION = "1.0.0"
DEFAULT_PORT     = 8765
MAX_PORT         = 8770
TICK_BATCH_LIMIT = 5
HTTP_TIMEOUT_SEC = 30.0
POLL_INTERVAL_SEC = 0.02
LOG_RING_SIZE    = 200
HISTORY_CAP      = 500

# ─── State ────────────────────────────────────────────────────────────────────

_server:         Optional[HTTPServer]       = None
_server_thread:  Optional[threading.Thread] = None
_tick_handle:    Optional[object]           = None
_bound_port:     int                        = 0
_start_time:     float                      = 0.0

_command_queue   = queue.Queue()
_responses:      Dict[str, dict]            = {}
_responses_lock  = threading.Lock()
_history:        deque                      = deque(maxlen=HISTORY_CAP)
_request_counter = 0
_log_ring:       deque                      = deque(maxlen=LOG_RING_SIZE)

# ─── Logging ──────────────────────────────────────────────────────────────────

def _log(msg: str, level: str = "info") -> None:
    entry = f"[MCP] {msg}"
    _log_ring.append(entry)
    if len(_log_ring) > LOG_RING_SIZE:
        _log_ring.pop(0)
    if level == "error":
        unreal.log_error(entry)
    elif level == "warning":
        unreal.log_warning(entry)
    else:
        unreal.log(entry)

# ─── Serialization ────────────────────────────────────────────────────────────

def _serialize(obj: Any) -> Any:
    """Convert unreal objects to JSON-serializable types."""
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return obj
    if isinstance(obj, (list, tuple)):
        return [_serialize(v) for v in obj]
    if isinstance(obj, dict):
        return {str(k): _serialize(v) for k, v in obj.items()}
    if isinstance(obj, unreal.Vector):
        return {"x": obj.x, "y": obj.y, "z": obj.z}
    if isinstance(obj, unreal.Rotator):
        return {"pitch": obj.pitch, "yaw": obj.yaw, "roll": obj.roll}
    if isinstance(obj, unreal.Vector2D):
        return {"x": obj.x, "y": obj.y}
    if isinstance(obj, unreal.LinearColor):
        return {"r": obj.r, "g": obj.g, "b": obj.b, "a": obj.a}
    if isinstance(obj, unreal.Color):
        return {"r": obj.r, "g": obj.g, "b": obj.b, "a": obj.a}
    if isinstance(obj, unreal.Transform):
        return {
            "location": _serialize(obj.translation),
            "rotation": _serialize(obj.rotation.rotator()),
            "scale": _serialize(obj.scale3d),
        }
    if isinstance(obj, unreal.AssetData):
        return {
            "package_name": obj.package_name,
            "asset_path": str(obj.package_name),
        }
    if isinstance(obj, unreal.Actor):
        return {
            "label": obj.get_actor_label(),
            "class": obj.get_class().get_name(),
            "location": _serialize(obj.get_actor_location()),
        }
    if isinstance(obj, unreal.Object):
        try:
            return obj.get_name()
        except Exception:
            return str(obj)
    return str(obj)

# ─── Command Registry ────────────────────────────────────────────────────────

_HANDLERS: Dict[str, Callable] = {}

def _register(cmd_name: str) -> Callable:
    """Decorator to register a command handler."""
    def decorator(fn: Callable) -> Callable:
        _HANDLERS[cmd_name] = fn
        return fn
    return decorator

# ─── System Commands ──────────────────────────────────────────────────────────

@_register("ping")
def _ping(**kwargs) -> dict:
    return {
        "status": "ok",
        "protocol": PROTOCOL_VERSION,
        "uptime": time.time() - _start_time if _start_time else 0,
    }

@_register("execute_python")
def _execute_python(code: str = "", **kwargs) -> dict:
    """Execute arbitrary Python code inside the UEFN editor."""
    if not code:
        return {"status": "error", "message": "No code provided."}

    import uefn_tools as tb

    local_vars: Dict[str, Any] = {
        "unreal": unreal,
        "tb": tb,
        "result": None,
    }

    output = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = output

    try:
        exec(code, {"__builtins__": __builtins__}, local_vars)
        result = local_vars.get("result")
        stdout = output.getvalue()
        return {
            "status": "ok",
            "result": _serialize(result),
            "stdout": stdout,
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "traceback": traceback.format_exc(),
            "stdout": output.getvalue(),
        }
    finally:
        sys.stdout = old_stdout

@_register("get_log")
def _get_log(lines: int = 50, **kwargs) -> dict:
    entries = list(_log_ring)[-lines:]
    return {"status": "ok", "entries": entries, "total": len(_log_ring)}

@_register("get_editor_log")
def _get_editor_log(lines: int = 50, **kwargs) -> dict:
    try:
        output_log = unreal.SystemLibrary.get_console_log()
        all_lines = output_log.split("\n") if output_log else []
        recent = all_lines[-lines:] if len(all_lines) > lines else all_lines
        return {"status": "ok", "entries": recent, "total": len(all_lines)}
    except Exception as e:
        return {"status": "ok", "entries": list(_log_ring)[-lines:], "total": len(_log_ring)}

@_register("shutdown")
def _shutdown(**kwargs) -> dict:
    stop_listener()
    return {"status": "ok", "message": "Listener stopped."}

# ─── Actor Commands ───────────────────────────────────────────────────────────

@_register("get_all_actors")
def _get_all_actors(**kwargs) -> dict:
    actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = actor_sub.get_all_level_actors()
    return {
        "status": "ok",
        "actors": _serialize(actors),
        "count": len(actors),
    }

@_register("get_selected_actors")
def _get_selected_actors(**kwargs) -> dict:
    actors = unreal.EditorLevelLibrary.get_selected_level_actors()
    return {
        "status": "ok",
        "actors": _serialize(actors),
        "count": len(actors),
    }

@_register("spawn_actor")
def _spawn_actor(class_path: str = "", location: list = None, rotation: list = None, **kwargs) -> dict:
    if not class_path:
        return {"status": "error", "message": "class_path is required."}

    loc = unreal.Vector(*(location or [0, 0, 0]))
    rot = unreal.Rotator(*(rotation or [0, 0, 0]))

    try:
        asset = unreal.load_asset(class_path)
        if asset:
            actor = unreal.EditorLevelLibrary.spawn_actor_from_object(asset, loc, rot)
        else:
            cls = unreal.load_class(None, class_path)
            if cls:
                actor = unreal.EditorLevelLibrary.spawn_actor_from_class(cls, loc, rot)
            else:
                return {"status": "error", "message": f"Could not load: {class_path}"}
        return {"status": "ok", "actor": _serialize(actor)}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@_register("delete_actors")
def _delete_actors(actor_labels: list = None, **kwargs) -> dict:
    if not actor_labels:
        return {"status": "error", "message": "actor_labels is required."}

    actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = actor_sub.get_all_level_actors()
    label_set = set(actor_labels)
    to_delete = [a for a in actors if a.get_actor_label() in label_set]
    for a in to_delete:
        actor_sub.destroy_actor(a)
    return {"status": "ok", "deleted": len(to_delete)}

@_register("set_actor_transform")
def _set_actor_transform(actor_label: str = "", location: list = None,
                         rotation: list = None, scale: list = None, **kwargs) -> dict:
    if not actor_label:
        return {"status": "error", "message": "actor_label is required."}

    actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = actor_sub.get_all_level_actors()
    target = next((a for a in actors if a.get_actor_label() == actor_label), None)
    if not target:
        return {"status": "error", "message": f"Actor '{actor_label}' not found."}

    if location:
        target.set_actor_location(unreal.Vector(*location), False, False)
    if rotation:
        target.set_actor_rotation(unreal.Rotator(*rotation), False)
    if scale:
        target.set_actor_scale3d(unreal.Vector(*scale))
    return {"status": "ok", "actor": _serialize(target)}

@_register("get_actor_properties")
def _get_actor_properties(actor_label: str = "", **kwargs) -> dict:
    if not actor_label:
        return {"status": "error", "message": "actor_label is required."}

    actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = actor_sub.get_all_level_actors()
    target = next((a for a in actors if a.get_actor_label() == actor_label), None)
    if not target:
        return {"status": "error", "message": f"Actor '{actor_label}' not found."}

    props = {
        "label": target.get_actor_label(),
        "class": target.get_class().get_name(),
        "location": _serialize(target.get_actor_location()),
        "rotation": _serialize(target.get_actor_rotation()),
        "scale": _serialize(target.get_actor_scale3d()),
        "hidden": target.is_hidden_ed(),
        "folder": target.get_folder_path(),
    }
    return {"status": "ok", "properties": props}

@_register("set_actor_properties")
def _set_actor_properties(actor_label: str = "", properties: dict = None, **kwargs) -> dict:
    if not actor_label or not properties:
        return {"status": "error", "message": "actor_label and properties are required."}

    actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = actor_sub.get_all_level_actors()
    target = next((a for a in actors if a.get_actor_label() == actor_label), None)
    if not target:
        return {"status": "error", "message": f"Actor '{actor_label}' not found."}

    if "hidden" in properties:
        target.set_actor_hidden_ed(properties["hidden"])
    if "folder" in properties:
        target.set_folder_path(properties["folder"])

    return {"status": "ok", "actor": _serialize(target)}

@_register("select_actors")
def _select_actors(actor_labels: list = None, **kwargs) -> dict:
    if not actor_labels:
        return {"status": "error", "message": "actor_labels is required."}

    actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = actor_sub.get_all_level_actors()
    label_set = set(actor_labels)
    to_select = [a for a in actors if a.get_actor_label() in label_set]
    unreal.EditorLevelLibrary.set_selected_level_actors(to_select)
    return {"status": "ok", "selected": len(to_select)}

@_register("focus_selected")
def _focus_selected(**kwargs) -> dict:
    actors = unreal.EditorLevelLibrary.get_selected_level_actors()
    if not actors:
        return {"status": "error", "message": "No actors selected."}
    return {"status": "ok", "message": f"Focused on {len(actors)} actor(s)."}

# ─── Asset Commands ───────────────────────────────────────────────────────────

@_register("list_assets")
def _list_assets(directory: str = "/", recursive: bool = True, class_filter: str = "", **kwargs) -> dict:
    ar = unreal.AssetRegistryHelpers.get_asset_registry()
    opts = unreal.ARFilter()
    if directory:
        opts.package_paths = [directory]
    opts.recursive_paths = recursive
    if class_filter:
        opts.class_names = [class_filter]
    assets = ar.get_assets(opts)
    return {
        "status": "ok",
        "assets": [_serialize(a) for a in assets],
        "count": len(assets),
    }

@_register("get_asset_info")
def _get_asset_info(asset_path: str = "", **kwargs) -> dict:
    if not asset_path:
        return {"status": "error", "message": "asset_path is required."}
    ar = unreal.AssetRegistryHelpers.get_asset_registry()
    data = ar.get_asset_by_object_path(asset_path)
    if not data:
        return {"status": "error", "message": f"Asset not found: {asset_path}"}
    return {"status": "ok", "asset": _serialize(data)}

@_register("get_selected_assets")
def _get_selected_assets(**kwargs) -> dict:
    tools = unreal.AssetToolsHelpers.get_asset_tools()
    assets = tools.get_selected_assets()
    return {"status": "ok", "assets": _serialize(assets), "count": len(assets)}

@_register("rename_asset")
def _rename_asset(old_path: str = "", new_path: str = "", **kwargs) -> dict:
    if not old_path or not new_path:
        return {"status": "error", "message": "old_path and new_path are required."}
    result = unreal.EditorAssetLibrary.rename_asset(old_path, new_path)
    return {"status": "ok" if result else "error", "old": old_path, "new": new_path}

@_register("delete_asset")
def _delete_asset(asset_path: str = "", **kwargs) -> dict:
    if not asset_path:
        return {"status": "error", "message": "asset_path is required."}
    result = unreal.EditorAssetLibrary.delete_asset(asset_path)
    return {"status": "ok" if result else "error", "path": asset_path}

@_register("duplicate_asset")
def _duplicate_asset(source_path: str = "", dest_path: str = "", **kwargs) -> dict:
    if not source_path or not dest_path:
        return {"status": "error", "message": "source_path and dest_path are required."}
    result = unreal.EditorAssetLibrary.duplicate_asset(source_path, dest_path)
    return {"status": "ok" if result else "error", "source": source_path, "dest": dest_path}

@_register("does_asset_exist")
def _does_asset_exist(asset_path: str = "", **kwargs) -> dict:
    if not asset_path:
        return {"status": "error", "message": "asset_path is required."}
    exists = unreal.EditorAssetLibrary.does_asset_exist(asset_path)
    return {"status": "ok", "exists": exists, "path": asset_path}

@_register("save_asset")
def _save_asset(asset_path: str = "", **kwargs) -> dict:
    if not asset_path:
        return {"status": "error", "message": "asset_path is required."}
    result = unreal.EditorAssetLibrary.save_asset(asset_path)
    return {"status": "ok" if result else "error", "path": asset_path}

@_register("search_assets")
def _search_assets(class_name: str = "", directory: str = "/", recursive: bool = True, **kwargs) -> dict:
    ar = unreal.AssetRegistryHelpers.get_asset_registry()
    opts = unreal.ARFilter()
    if directory:
        opts.package_paths = [directory]
    opts.recursive_paths = recursive
    if class_name:
        opts.class_names = [class_name]
    assets = ar.get_assets(opts)
    return {"status": "ok", "assets": [_serialize(a) for a in assets], "count": len(assets)}

# ─── Project / Level Commands ─────────────────────────────────────────────────

@_register("get_project_info")
def _get_project_info(**kwargs) -> dict:
    return {
        "status": "ok",
        "project_name": unreal.Paths.get_project_file_path(),
        "content_root": unreal.Paths.project_content_dir(),
    }

@_register("save_current_level")
def _save_current_level(**kwargs) -> dict:
    unreal.EditorLevelLibrary.save_current_level()
    return {"status": "ok", "message": "Level saved."}

@_register("get_level_info")
def _get_level_info(**kwargs) -> dict:
    actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = actor_sub.get_all_level_actors()
    return {
        "status": "ok",
        "actor_count": len(actors),
    }

# ─── Viewport Commands ────────────────────────────────────────────────────────

@_register("get_viewport_camera")
def _get_viewport_camera(**kwargs) -> dict:
    loc, rot = unreal.EditorLevelLibrary.get_level_viewport_camera_info()
    return {
        "status": "ok",
        "location": _serialize(loc),
        "rotation": _serialize(rot),
    }

@_register("set_viewport_camera")
def _set_viewport_camera(location: list = None, rotation: list = None, **kwargs) -> dict:
    loc = unreal.Vector(*(location or [0, 0, 0])) if location else None
    rot = unreal.Rotator(*(rotation or [0, 0, 0])) if rotation else None
    unreal.EditorLevelLibrary.set_level_viewport_camera_info(loc, rot)
    return {"status": "ok"}

# ─── Tool Escape Hatch ────────────────────────────────────────────────────────

@_register("run_tool")
def _run_tool(tool_name: str = "", **kwargs) -> dict:
    """Execute any registered uefn_tools tool by name."""
    if not tool_name:
        return {"status": "error", "message": "tool_name is required."}

    try:
        import uefn_tools as tb
        result = tb.run(tool_name, **kwargs)
        if result is None:
            return {"status": "ok", "result": None}
        return _serialize(result) if isinstance(result, dict) else {"status": "ok", "result": _serialize(result)}
    except Exception as e:
        return {"status": "error", "message": str(e), "traceback": traceback.format_exc()}

@_register("list_tools")
def _list_tools(category: str = "", **kwargs) -> dict:
    """List all registered uefn_tools tools."""
    try:
        import uefn_tools as tb
        tools = tb.registry.list_tools()
        if category:
            tools = [t for t in tools if t.get("category") == category]
        return {"status": "ok", "tools": tools, "count": len(tools)}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@_register("describe_tool")
def _describe_tool(tool_name: str = "", **kwargs) -> dict:
    """Get details about a specific tool."""
    if not tool_name:
        return {"status": "error", "message": "tool_name is required."}
    try:
        import uefn_tools as tb
        info = tb.registry.get_tool_info(tool_name)
        if info is None:
            return {"status": "error", "message": f"Tool '{tool_name}' not found."}
        return {"status": "ok", "tool": info}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ─── Tick Handler (Main Thread Dispatch) ──────────────────────────────────────

def _tick(delta_time: float) -> None:
    """Called on editor tick — drain command queue and execute on main thread."""
    for _ in range(TICK_BATCH_LIMIT):
        try:
            request_id, cmd_name, params, result_event = _command_queue.get_nowait()
        except queue.Empty:
            break

        handler = _HANDLERS.get(cmd_name)
        if handler is None:
            with _responses_lock:
                _responses[request_id] = {
                    "success": False,
                    "error": f"Unknown command: {cmd_name}",
                }
            result_event.set()
            continue

        try:
            result = handler(**params)
            with _responses_lock:
                _responses[request_id] = {"success": True, "result": result}
        except Exception as e:
            with _responses_lock:
                _responses[request_id] = {
                    "success": False,
                    "error": str(e),
                    "traceback": traceback.format_exc(),
                }
        finally:
            result_event.set()

# ─── HTTP Handler ─────────────────────────────────────────────────────────────

class _Handler(BaseHTTPRequestHandler):
    """Handle incoming HTTP requests."""

    def do_GET(self) -> None:
        if self.path == "/":
            self._json_response({
                "status": "ok",
                "protocol": PROTOCOL_VERSION,
                "commands": list(_HANDLERS.keys()),
            })
        else:
            self._json_response({"status": "error", "message": "Not found."}, 404)

    def do_POST(self) -> None:
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
        except Exception:
            self._json_response({"status": "error", "message": "Invalid JSON."}, 400)
            return

        command = body.get("command", "")
        params = body.get("params", {})

        if not command:
            self._json_response({"status": "error", "message": "Missing 'command'."}, 400)
            return

        handler = _HANDLERS.get(command)
        if handler is None:
            self._json_response({"status": "error", "message": f"Unknown command: {command}."}, 404)
            return

        # Queue for main thread
        global _request_counter
        _request_counter += 1
        request_id = f"req_{_request_counter}"
        result_event = threading.Event()

        _command_queue.put((request_id, command, params, result_event))

        # Wait for result
        if result_event.wait(timeout=HTTP_TIMEOUT_SEC):
            with _responses_lock:
                response = _responses.pop(request_id, {"success": False, "error": "No response."})
            self._json_response(response)
        else:
            with _responses_lock:
                _responses.pop(request_id, None)
            self._json_response({"success": False, "error": f"Command '{command}' timed out."}, 504)

    def _json_response(self, data: dict, code: int = 200) -> None:
        payload = json.dumps(data, default=str).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args) -> None:
        pass  # suppress HTTP access logs

# ─── Port Discovery ──────────────────────────────────────────────────────────

def _find_free_port() -> int:
    for port in range(DEFAULT_PORT, MAX_PORT + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("127.0.0.1", port))
            s.close()
            return port
        except OSError:
            continue
    raise RuntimeError(f"No free port in range {DEFAULT_PORT}-{MAX_PORT}")

# ─── Start / Stop / Status ────────────────────────────────────────────────────

def start_listener(port: int = 0) -> int:
    global _server, _server_thread, _tick_handle, _bound_port, _start_time

    if _server is not None:
        _log(f"Listener already running on port {_bound_port}", "warning")
        return _bound_port

    if port == 0:
        port = _find_free_port()

    _server = HTTPServer(("127.0.0.1", port), _Handler)
    _bound_port = port
    _start_time = time.time()

    _server_thread = threading.Thread(target=_server.serve_forever, daemon=True)
    _server_thread.start()

    try:
        _tick_handle = unreal.register_slate_post_tick_callback(_tick)
    except Exception as e:
        _log(f"Tick callback failed: {e} — commands will run on HTTP thread", "warning")

    _log(f"Listener started on http://127.0.0.1:{port}")
    _log(f"{len(_HANDLERS)} commands registered")
    return port


def stop_listener() -> None:
    global _server, _server_thread, _tick_handle, _bound_port

    if _server is None:
        _log("Listener is not running", "warning")
        return

    if _tick_handle is not None:
        unreal.unregister_slate_post_tick_callback(_tick_handle)
        _tick_handle = None

    _server.shutdown()
    if _server_thread:
        _server_thread.join(timeout=3.0)

    old_port = _bound_port
    _server = None
    _server_thread = None
    _bound_port = 0
    _log(f"Listener stopped (was on port {old_port})")


def get_status() -> dict:
    return {
        "running": _server is not None,
        "port": _bound_port,
        "url": f"http://127.0.0.1:{_bound_port}" if _bound_port else None,
        "commands": len(_HANDLERS),
    }


# ─── Auto-start when executed directly ────────────────────────────────────────

if __name__ == "__main__":
    start_listener()
elif "unreal" in sys.modules:
    # Running inside UEFN — auto-start
    try:
        if _server is not None:
            _log("Previous listener detected — replacing")
            try:
                _server.server_close()
            except Exception:
                pass
            _server = None
            _server_thread = None
            _bound_port = 0

        start_listener()
    except Exception as e:
        unreal.log_error(f"[MCP] Failed to start listener: {e}")
        traceback.print_exc()
