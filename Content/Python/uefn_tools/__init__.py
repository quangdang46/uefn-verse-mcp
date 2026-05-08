"""
uefn_tools — Package Root
========================================
Public API:
    import uefn_tools as ut
    ut.register_all_tools()    # called automatically by init_unreal.py
    ut.run("tool_name")        # execute any tool by name
    ut.run("smoke_test")       # run the 6-layer health check
    ut.registry               # access the ToolRegistry directly

Generic loader contract:
    init_unreal.py calls ut.register() on every package that exposes it.
    register() handles tool loading and custom plugins.
"""

from typing import Any

from .registry import ToolRegistry, get_registry, register_tool
from . import core
from .core.config import get_config

# ut.config — persistent user settings, survives install.py updates
# Lives at Saved/uefn_tools/config.json
config = get_config()

# ── Version ───────────────────────────────────────────────────────────────────
__version__ = "2.2.1"
__tool_count__ = 363
__category_count__ = 54
TOOLBELT_API_VERSION = __version__  # backwards compat alias

# Singleton registry shared across all imports
registry: ToolRegistry = get_registry()

def register() -> None:
    """
    Generic loader entry point — called by init_unreal.py on editor startup.
    Registers all tools and loads custom plugins.
    """
    import unreal
    register_all_tools()
    load_custom_plugins()
    unreal.log("[uefn_tools] ✓ All tools registered.")

def register_all_tools() -> None:
    """Import every tool module so their @register_tool decorators fire."""
    from . import tools as _tools  # noqa: F401 — triggers all sub-imports
    from . import diagnostics as _diag  # noqa: F401 — registers debug tools
    import unreal
    unreal.log(f"[uefn_tools] {len(registry)} tools registered across {len(registry.categories())} categories.")

def load_custom_plugins() -> None:
    """Load user-provided tools from Saved/uefn_tools/Custom_Plugins."""
    import os, sys, glob, importlib, ast, hashlib, json, unreal
    from datetime import datetime
    custom_plugins_dir = os.path.join(unreal.Paths.project_saved_dir(), "uefn_tools", "Custom_Plugins")
    if not os.path.exists(custom_plugins_dir):
        return
        
    if custom_plugins_dir not in sys.path:
        sys.path.insert(0, custom_plugins_dir)

    MAX_PLUGIN_SIZE_KB = 50
    _BLOCKED_IMPORTS = frozenset({
        "subprocess", "shutil", "ctypes", "socket", "http",
        "urllib", "requests", "webbrowser", "smtplib", "ftplib",
        "xmlrpc", "multiprocessing", "signal", "_thread",
    })

    def _scan_plugin(filepath: str) -> list:
        errors = []
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            source = f.read()
        try:
            tree = ast.parse(source)
        except SyntaxError as e:
            return [{"error": f"Syntax error: {e}"}]
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.name.split(".")[0]
                    if name in _BLOCKED_IMPORTS:
                        errors.append(f"Blocked import: {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.module.split(".")[0] in _BLOCKED_IMPORTS:
                    errors.append(f"Blocked import: {node.module}")
        return errors

    audit_path = os.path.join(custom_plugins_dir, "plugin_audit.json")
    audit_log = []
    valid_count = 0

    for plugin_path in glob.glob(os.path.join(custom_plugins_dir, "*.py")):
        if os.path.basename(plugin_path) == "__init__.py":
            continue
        module_name = os.path.splitext(os.path.basename(plugin_path))[0]
        file_size_kb = os.path.getsize(plugin_path) / 1024

        errors = _scan_plugin(plugin_path)
        if errors:
            unreal.log_warning(f"[uefn_tools] Plugin {module_name} rejected: {errors}")
            audit_log.append({"plugin": module_name, "status": "REJECTED", "errors": errors})
            continue

        if file_size_kb > MAX_PLUGIN_SIZE_KB:
            unreal.log_warning(f"[uefn_tools] Plugin {module_name} rejected: exceeds {MAX_PLUGIN_SIZE_KB}KB limit ({file_size_kb:.1f}KB)")
            audit_log.append({"plugin": module_name, "status": "REJECTED", "reason": f"exceeds size limit ({file_size_kb:.1f}KB)"})
            continue

        try:
            import hashlib
            with open(plugin_path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()[:16]
            mod = importlib.import_module(module_name)
            if hasattr(mod, "register"):
                mod.register()
                valid_count += 1
                unreal.log(f"[uefn_tools] Loaded plugin: {module_name}")
                audit_log.append({
                    "plugin": module_name,
                    "status": "LOADED",
                    "sha256": file_hash,
                    "size_kb": round(file_size_kb, 1),
                    "loaded_at": datetime.now().isoformat(),
                })
        except Exception as e:
            unreal.log_error(f"[uefn_tools] Failed to load plugin {module_name}.py: {e}")
            audit_log.append({"plugin": module_name, "status": "LOAD_ERROR", "error": str(e)})

    with open(audit_path, "w", encoding="utf-8") as f:
        json.dump({
            "toolbelt_version": __version__,
            "scan_time": datetime.now().isoformat(),
            "plugins": audit_log,
        }, f, indent=2)

    if valid_count > 0:
        unreal.log(f"[uefn_tools] Loaded {valid_count} custom plugins. Audit log: {audit_path}")

def run(tool_id: str, **kwargs) -> Any:
    """Execute a registered tool by name. Returns the tool's return value."""
    return registry.execute(tool_id, **kwargs)

@register_tool(
    name="smoke_test",
    category="Utilities",
    description="Run the full 6-layer smoke test and print results to the Output Log.",
    tags=["smoke", "test", "health", "debug"],
)
def smoke_test(**kwargs) -> bool:
    """
    Run the full uefn_tools smoke test (6 layers: Python env, UEFN API,
    uefn_tools core, MCP bridge, etc.).
    Results printed to Output Log and saved to Saved/uefn_tools/smoke_test_results.txt.
    Returns True if all checks pass.
    """
    import sys, os
    test_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "smoke_test.py")
    if test_path not in sys.path:
        sys.path.insert(0, os.path.dirname(test_path))
    import importlib.util
    spec = importlib.util.spec_from_file_location("smoke_test", test_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.run_smoke_test()

def reload() -> None:
    """Reload all uefn_tools modules and the registry."""
    import importlib
    import unreal
    from . import registry
    from . import core
    from . import tools
    import os
    
    importlib.reload(core)
    importlib.reload(registry)
    
    reg = registry.get_registry()
    reg._tools.clear()
    
    tools_pkg_path = os.path.dirname(tools.__file__)
    for f in os.listdir(tools_pkg_path):
        if f.endswith(".py") and f != "__init__.py":
            mod_name = f[:-3]
            try:
                submod = getattr(tools, mod_name, None)
                if submod:
                    importlib.reload(submod)
            except Exception as e:
                unreal.log_warning(f"[uefn_tools] Reload failed for {mod_name}: {e}")
                
    importlib.reload(tools)
    unreal.log(f"[uefn_tools] ↻ All modules reloaded and registry rebuilt. (v{__version__})")
