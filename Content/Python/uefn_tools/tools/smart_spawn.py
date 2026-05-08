"""
uefn_tools -- Smart Spawn
========================================
Intelligent device/actor spawning with **dynamic** name resolution.

Instead of relying on a hardcoded alias map, this module scans the Content
Browser and Asset Registry at runtime to discover every available device,
blueprint, and actor class.  A small static fallback table is kept only for
the case where the editor hasn't finished loading yet.

Resolution pipeline (in order):
  1. Dynamic device catalog  (runtime scan of Content Browser)
  2. Static fallback aliases (minimal, for offline / early-boot)
  3. Exact asset / class path passthrough
  4. Class prefix search     (/Script/FortniteGame, /Script/Engine)
  5. Fuzzy Content Browser search
"""

from __future__ import annotations

import re
import time
from typing import Any, Dict, List, Optional, Tuple

import unreal

# ---------------------------------------------------------------------------
# Runtime device catalog -- populated by scan_device_catalog()
# ---------------------------------------------------------------------------
# Maps normalised name -> {"path": str, "name": str, "class": str, "source": str}
_device_catalog: Dict[str, dict] = {}
_catalog_scanned: bool = False
_catalog_scan_time: float = 0.0

# Directories the scanner walks (most-specific first for speed)
_SCAN_DIRS: List[str] = [
    "/Game/Creative/Devices",
    "/Fortnite",
    "/Game",
]

# Legacy/misconfigured roots that appear in some UEFN APIs or older configs.
# Canonicalize them before calling EditorAssetLibrary.list_assets().
_SCAN_DIR_ALIASES = {
    "/FortniteGame": "/Fortnite",
}

# Patterns that identify a "device" blueprint asset
_DEVICE_PATTERNS: List[re.Pattern] = [
    re.compile(r"BP_Creative", re.IGNORECASE),
    re.compile(r"Device", re.IGNORECASE),
    re.compile(r"Spawner", re.IGNORECASE),
    re.compile(r"Trigger", re.IGNORECASE),
    re.compile(r"Teleporter", re.IGNORECASE),
    re.compile(r"Scoreboard", re.IGNORECASE),
    re.compile(r"Billboard", re.IGNORECASE),
    re.compile(r"Timer", re.IGNORECASE),
    re.compile(r"Button", re.IGNORECASE),
    re.compile(r"Volume", re.IGNORECASE),
    re.compile(r"Checkpoint", re.IGNORECASE),
    re.compile(r"HUD", re.IGNORECASE),
    re.compile(r"Music", re.IGNORECASE),
    re.compile(r"Capture", re.IGNORECASE),
    re.compile(r"Vending", re.IGNORECASE),
    re.compile(r"PlayerStart", re.IGNORECASE),
]


def _normalise(name: str) -> str:
    """Lower-case, strip whitespace, collapse underscores/hyphens to spaces."""
    return re.sub(r"[\s_\-]+", " ", name.strip().lower())


def _derive_friendly_names(asset_name: str) -> List[str]:
    """Generate multiple friendly lookup keys from a raw asset name.

    e.g. "BP_Creative_Button" -> ["button", "creative button", "bp creative button"]
    """
    clean = asset_name
    for prefix in ("BP_Creative_Device_", "BP_Creative_", "BP_", "Fort", "FortCreative"):
        if clean.startswith(prefix):
            clean = clean[len(prefix):]
            break

    for suffix in ("_C", "Device", "Creative"):
        if clean.endswith(suffix):
            clean = clean[: -len(suffix)]

    parts = re.sub(r"([a-z])([A-Z])", r"\1 \2", clean).replace("_", " ").strip()
    normalised = _normalise(parts)

    names = [normalised]
    full_normalised = _normalise(clean)
    if full_normalised != normalised:
        names.append(full_normalised)
    orig = _normalise(asset_name)
    if orig not in names:
        names.append(orig)

    return [n for n in names if n]


def _iter_scan_dirs() -> List[str]:
    """Return deduplicated, canonical Content Browser roots for scanning."""
    dirs: List[str] = []
    seen = set()
    for raw_dir in _SCAN_DIRS:
        scan_dir = _SCAN_DIR_ALIASES.get(raw_dir, raw_dir)
        if scan_dir in seen:
            continue
        seen.add(scan_dir)
        dirs.append(scan_dir)
    return dirs


def _to_rotator(values: Optional[List[float]]) -> unreal.Rotator:
    """Build Rotator from [pitch, yaw, roll] reliably."""
    if values is None:
        return unreal.Rotator(0.0, 0.0, 0.0)
    if len(values) != 3:
        raise ValueError("rotation must be [pitch, yaw, roll]")
    pitch, yaw, roll = float(values[0]), float(values[1]), float(values[2])
    return unreal.Rotator(pitch=pitch, yaw=yaw, roll=roll)


# ---------------------------------------------------------------------------
# Catalog scanner
# ---------------------------------------------------------------------------

def scan_device_catalog(force: bool = False) -> Dict[str, dict]:
    """Scan Content Browser to build a dynamic device catalog.

    Walks ``_SCAN_DIRS``, discovers blueprints/classes that look like
    devices, and indexes them by multiple friendly names.

    The result is cached; pass ``force=True`` to rescan.
    """
    global _device_catalog, _catalog_scanned, _catalog_scan_time

    if _catalog_scanned and not force:
        return _device_catalog

    catalog: Dict[str, dict] = {}
    seen_paths: set = set()

    for scan_dir in _iter_scan_dirs():
        try:
            paths = unreal.EditorAssetLibrary.list_assets(scan_dir, recursive=True)
        except Exception:
            continue

        for path in paths:
            path_str = str(path)
            if path_str in seen_paths:
                continue
            seen_paths.add(path_str)

            raw_name = path_str.rsplit("/", 1)[-1].rsplit(".", 1)[0]

            is_device = any(p.search(raw_name) for p in _DEVICE_PATTERNS)
            if not is_device and path_str.startswith("/Game/Creative/Devices"):
                is_device = True
            if not is_device:
                continue

            asset_class = ""
            display_name = raw_name
            try:
                data = unreal.EditorAssetLibrary.find_asset_data(path_str)
                if data:
                    display_name = str(data.asset_name)
                    asset_class = str(getattr(data, "asset_class_path", ""))
            except Exception:
                pass

            entry = {
                "path": path_str,
                "name": display_name,
                "class": asset_class,
                "source": "content_browser_scan",
            }

            for friendly in _derive_friendly_names(raw_name):
                if friendly and friendly not in catalog:
                    catalog[friendly] = entry

    _index_engine_classes(catalog)

    _device_catalog = catalog
    _catalog_scanned = True
    _catalog_scan_time = time.time()

    return _device_catalog


def _index_engine_classes(catalog: Dict[str, dict]) -> None:
    """Add common engine actor classes to the catalog."""
    engine_classes = {
        "point light":       "/Script/Engine.PointLight",
        "spot light":        "/Script/Engine.SpotLight",
        "directional light": "/Script/Engine.DirectionalLight",
        "rect light":        "/Script/Engine.RectLight",
        "static mesh":       "/Script/Engine.StaticMeshActor",
        "cube":              "/Script/Engine.StaticMeshActor",
        "camera":            "/Script/Engine.CameraActor",
        "note":              "/Script/Engine.Note",
    }
    for friendly, path in engine_classes.items():
        if friendly not in catalog:
            catalog[friendly] = {
                "path": path,
                "name": friendly,
                "class": path,
                "source": "engine_class",
            }


# ---------------------------------------------------------------------------
# Static fallback aliases -- used ONLY when catalog scan hasn't run yet
# ---------------------------------------------------------------------------
_STATIC_FALLBACKS: Dict[str, Tuple[str, List[str]]] = {
    "button":          ("/Game/Creative/Devices/Button/BP_Creative_Button.BP_Creative_Button_C",
                        ["/Script/FortniteGame.FortCreativeButtonDevice"]),
    "timer":           ("/Script/FortniteGame.FortCreativeTimerDevice",
                        ["/Game/Creative/Devices/Timer/BP_Creative_Device_Timer.BP_Creative_Device_Timer_C"]),
    "trigger":         ("/Game/Creative/Devices/Trigger/BP_Creative_Device_Trigger.BP_Creative_Device_Trigger_C",
                        ["/Script/FortniteGame.FortCreativeTriggerDevice"]),
    "teleporter":      ("/Game/Creative/Devices/Teleporter/BP_Creative_Device_Teleporter.BP_Creative_Device_Teleporter_C",
                        ["/Script/FortniteGame.FortCreativeTeleporter"]),
    "spawn pad":       ("/Script/FortniteGame.FortPlayerStartCreative",
                        ["/Script/FortniteGame.FortPlayerStart"]),
    "item spawner":    ("/Script/FortniteGame.FortItemSpawnerCreative", []),
}

# Class prefixes used in prefix search step
_CLASS_PREFIXES = [
    "/Script/FortniteGame.Fort",
    "/Script/FortniteGame.FortCreative",
    "/Script/Engine.",
]


# ---------------------------------------------------------------------------
# Low-level helpers
# ---------------------------------------------------------------------------

def try_load_class(path: str):
    """Try to load a class from a path, return None on failure."""
    try:
        return unreal.load_class(None, path)
    except Exception:
        return None


def try_load_asset(path: str):
    """Try to load an asset from a path, return None on failure."""
    # `/Script/...` is a class namespace, not a Content Browser asset path.
    # Avoid calling EditorAssetLibrary.load_asset on it to prevent noisy errors.
    if not path or str(path).startswith("/Script/"):
        return None
    try:
        return unreal.EditorAssetLibrary.load_asset(path)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Content Browser fuzzy search (fallback for unresolved names)
# ---------------------------------------------------------------------------

def fuzzy_search_assets(query: str, limit: int = 10) -> List[Dict[str, str]]:
    """Search the Asset Registry for assets whose name contains *query*."""
    query_lower = query.lower().replace(" ", "").replace("_", "")
    results: List[Dict[str, str]] = []

    for search_dir in _iter_scan_dirs():
        try:
            paths = unreal.EditorAssetLibrary.list_assets(search_dir, recursive=True)
        except Exception:
            continue

        for path in paths:
            asset_name = path.rsplit("/", 1)[-1].rsplit(".", 1)[0].lower().replace("_", "")
            if query_lower in asset_name or asset_name in query_lower:
                try:
                    data = unreal.EditorAssetLibrary.find_asset_data(path)
                    if data:
                        results.append({
                            "path": str(path),
                            "name": str(data.asset_name),
                            "class": str(getattr(data, "asset_class_path", "")),
                        })
                except Exception:
                    results.append({
                        "path": str(path),
                        "name": path.rsplit("/", 1)[-1],
                        "class": "",
                    })
            if len(results) >= limit:
                break
        if len(results) >= limit:
            break

    return results


# ---------------------------------------------------------------------------
# Resolution pipeline
# ---------------------------------------------------------------------------

def _resolve_catalog(name_lower: str) -> tuple:
    """Step 1: Look up in runtime device catalog."""
    catalog = scan_device_catalog()

    entry = catalog.get(name_lower)
    if not entry:
        return ("", "", None)

    path = entry["path"]
    cls = try_load_class(path)
    if cls:
        return (path, "device_catalog (class)", cls)
    asset = try_load_asset(path)
    if asset:
        return (path, "device_catalog (asset)", asset)
    return ("", "", None)


def _resolve_static_fallback(name_lower: str) -> tuple:
    """Step 2: Check static fallback aliases (boot-time safety net)."""
    if name_lower not in _STATIC_FALLBACKS:
        return ("", "", None)

    primary, fallbacks = _STATIC_FALLBACKS[name_lower]
    for path in [primary] + fallbacks:
        cls = try_load_class(path)
        if cls:
            return (path, "static_fallback (class)", cls)
        asset = try_load_asset(path)
        if asset:
            return (path, "static_fallback (asset)", asset)
    return ("", "", None)


def _resolve_exact(name: str) -> tuple:
    """Step 3: Try as exact asset/class path."""
    if "/" not in name and "." not in name:
        return ("", "", None)

    # Class paths should resolve via load_class first.
    if name.startswith("/Script/"):
        cls = try_load_class(name)
        if cls:
            return (name, "exact_class_path", cls)
        return ("", "", None)

    asset = try_load_asset(name)
    if asset:
        return (name, "exact_asset_path", asset)
    cls = try_load_class(name)
    if cls:
        return (name, "exact_class_path", cls)
    return ("", "", None)


def _resolve_prefix(name: str) -> tuple:
    """Step 4: Try common class prefixes."""
    pascal = "".join(w.capitalize() for w in name.split())
    suffixes = [
        pascal,
        f"{pascal}Device",
        f"{pascal}Creative",
        f"Creative{pascal}",
        f"Creative{pascal}Device",
    ]

    for prefix in _CLASS_PREFIXES:
        for suffix in suffixes:
            path = f"{prefix}{suffix}"
            cls = try_load_class(path)
            if cls:
                return (path, "class_prefix_search", cls)
    return ("", "", None)


def _resolve_fuzzy(name: str) -> tuple:
    """Step 5: Fuzzy search in Content Browser."""
    candidates = fuzzy_search_assets(name)
    if not candidates:
        return ("", "", None)

    best = candidates[0]
    asset = try_load_asset(best["path"])
    if asset:
        return (best["path"], "content_browser_search", asset)
    return ("", "candidates_only", candidates)


def resolve(name: str) -> Dict[str, Any]:
    """Resolve a natural name to a Content Browser path.

    Returns dict with keys: resolved_path, resolved_via, loadable, candidates.
    """
    name_lower = _normalise(name)

    steps = [
        lambda: _resolve_catalog(name_lower),
        lambda: _resolve_static_fallback(name_lower),
        lambda: _resolve_exact(name),
        lambda: _resolve_prefix(name),
        lambda: _resolve_fuzzy(name),
    ]

    for step in steps:
        path, via, loadable = step()
        if path:
            return {"resolved_path": path, "resolved_via": via, "loadable": loadable}
        if via == "candidates_only":
            return {"resolved_path": "", "resolved_via": "", "loadable": None, "candidates": loadable}

    return {"resolved_path": "", "resolved_via": "", "loadable": None}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def spawn(
    name: str,
    location: Optional[List[float]] = None,
    rotation: Optional[List[float]] = None,
    label: str = "",
    dry_run: bool = False,
    serializer: Any = None,
) -> dict:
    """Spawn an actor by natural name with intelligent path resolution.

    Args:
        name:       Natural name or exact path.
        location:   World location [x, y, z].
        rotation:   Rotation [pitch, yaw, roll] degrees.
        label:      Optional outliner label.
        dry_run:    If True, resolve only -- don't spawn.
        serializer: Callable to serialize the spawned actor (optional).
    """
    if not name:
        raise ValueError("name is required -- e.g. 'button', 'timer', 'spawn pad', or an asset path")

    loc = unreal.Vector(*location) if location else unreal.Vector(0, 0, 0)
    rot = _to_rotator(rotation)
    sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    result = resolve(name)
    resolved_path = result["resolved_path"]
    resolved_via = result["resolved_via"]
    loadable = result.get("loadable")
    candidates = result.get("candidates")

    if not resolved_path and not candidates:
        return {
            "status": "error",
            "error": f"Could not resolve '{name}' to any asset or class.",
            "suggestions": [
                "Try a more specific name (e.g. 'button', 'timer', 'teleporter')",
                "Use search_content_browser to find available assets first",
                "Run refresh_device_catalog to rescan the Content Browser",
            ],
            "catalog_size": len(_device_catalog),
            "catalog_scanned": _catalog_scanned,
        }

    if candidates and not resolved_path:
        return {
            "status": "not_spawned",
            "reason": "Found candidates but could not load them. Pick one and use smart_spawn with exact path.",
            "query": name,
            "candidates": candidates,
        }

    if dry_run:
        return {
            "status": "dry_run",
            "resolved_path": resolved_path,
            "resolved_via": resolved_via,
            "query": name,
        }

    actor = None
    is_class = resolved_via.endswith("(class)") or resolved_via in ("class_prefix_search", "exact_class_path")
    if is_class:
        actor = sub.spawn_actor_from_class(loadable, loc, rot)
    else:
        actor = sub.spawn_actor_from_object(loadable, loc, rot)

    if actor is None:
        return {
            "status": "error",
            "error": f"Resolved path '{resolved_path}' but failed to spawn.",
            "resolved_path": resolved_path,
            "resolved_via": resolved_via,
        }

    if label:
        actor.set_actor_label(label)

    actor_data = serializer(actor) if serializer else str(actor.get_actor_label())
    return {
        "status": "ok",
        "actor": actor_data,
        "resolved_path": resolved_path,
        "resolved_via": resolved_via,
        "query": name,
    }


def search_content_browser(query: str, limit: int = 20) -> dict:
    """Fuzzy search the Content Browser for assets matching a query."""
    if not query:
        raise ValueError("query is required -- e.g. 'button', 'timer', 'tree'")
    results = fuzzy_search_assets(query, limit=limit)
    return {
        "query": query,
        "results": results,
        "count": len(results),
        "tip": "Use the 'path' from results with smart_spawn(name=...)",
    }


def list_aliases() -> dict:
    """List all device names the system knows about.

    Merges the runtime catalog (dynamic) with static fallbacks.
    """
    catalog = scan_device_catalog()

    aliases: Dict[str, dict] = {}
    for alias, (primary, fallbacks) in sorted(_STATIC_FALLBACKS.items()):
        aliases[alias] = {"primary_path": primary, "fallbacks": fallbacks, "source": "static_fallback"}
    for alias, entry in sorted(catalog.items()):
        aliases[alias] = {"primary_path": entry["path"], "fallbacks": [], "source": entry["source"]}

    return {
        "aliases": aliases,
        "count": len(aliases),
        "catalog_scanned": _catalog_scanned,
        "catalog_scan_time": _catalog_scan_time,
    }


def refresh_catalog() -> dict:
    """Force rescan the Content Browser and rebuild the device catalog."""
    catalog = scan_device_catalog(force=True)
    return {
        "status": "ok",
        "catalog_size": len(catalog),
        "scan_time": _catalog_scan_time,
    }
