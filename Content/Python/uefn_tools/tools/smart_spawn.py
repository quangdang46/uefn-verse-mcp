"""
uefn_tools — Smart Spawn
========================================
Intelligent device/actor spawning with natural name resolution.

Instead of requiring exact Content Browser paths, accepts natural names
like 'button', 'timer', 'teleporter' and resolves them automatically
through a multi-step pipeline:

  1. Built-in device alias map (30+ common Creative devices)
  2. Exact asset/class path passthrough
  3. Class prefix search (/Script/FortniteGame, /Script/Engine)
  4. Fuzzy Content Browser search
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import unreal

# ─── Well-known Creative device aliases ──────────────────────────────────────
# Maps natural names → (primary_class_path, [fallback_paths...])
DEVICE_ALIASES: Dict[str, tuple] = {
    # Fortnite Creative devices
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
    "spawnpad":        ("/Script/FortniteGame.FortPlayerStartCreative",
                        ["/Script/FortniteGame.FortPlayerStart"]),
    "player spawn":    ("/Script/FortniteGame.FortPlayerStartCreative",
                        ["/Script/FortniteGame.FortPlayerStart"]),
    "item spawner":    ("/Script/FortniteGame.FortItemSpawnerCreative",
                        ["/Game/Creative/Devices/ItemSpawner/BP_Creative_Device_ItemSpawner.BP_Creative_Device_ItemSpawner_C"]),
    "vending machine": ("/Script/FortniteGame.FortVendingMachineCreative", []),
    "capture area":    ("/Script/FortniteGame.FortCaptureAreaCreative", []),
    "billboard":       ("/Game/Creative/Devices/Billboard/BP_Creative_Billboard.BP_Creative_Billboard_C",
                        ["/Script/FortniteGame.FortCreativeBillboard"]),
    "hud message":     ("/Game/Creative/Devices/HUDMessage/BP_Creative_HudMessageDevice.BP_Creative_HudMessageDevice_C", []),
    "scoreboard":      ("/Game/Creative/Devices/Scoreboard/BP_Creative_Scoreboard.BP_Creative_Scoreboard_C", []),
    "damage volume":   ("/Game/Creative/Devices/DamageVolume/BP_Creative_DamageVolume.BP_Creative_DamageVolume_C", []),
    "explosive":       ("/Game/Creative/Devices/Explosive/BP_Creative_Explosive_Device.BP_Creative_Explosive_Device_C", []),
    "guard spawner":   ("/Game/Creative/Devices/GuardSpawner/BP_Creative_GuardSpawner.BP_Creative_GuardSpawner_C", []),
    "vehicle spawner": ("/Game/Creative/Devices/VehicleSpawner/BP_Creative_VehicleSpawner.BP_Creative_VehicleSpawner_C",
                        ["/Script/FortniteGame.FortVehicleSpawnerCreative"]),
    "music player":    ("/Game/Creative/Devices/MusicPlayer/BP_Creative_MusicPlayer.BP_Creative_MusicPlayer_C", []),
    # Engine primitives
    "point light":       ("/Script/Engine.PointLight", []),
    "spot light":        ("/Script/Engine.SpotLight", []),
    "directional light": ("/Script/Engine.DirectionalLight", []),
    "rect light":        ("/Script/Engine.RectLight", []),
    "cube":              ("/Script/Engine.StaticMeshActor", []),
    "static mesh":       ("/Script/Engine.StaticMeshActor", []),
    "camera":            ("/Script/Engine.CameraActor", []),
    "note":              ("/Script/Engine.Note", []),
}

# Class prefixes used in Step 3 resolution
_CLASS_PREFIXES = [
    "/Script/FortniteGame.Fort",
    "/Script/FortniteGame.FortCreative",
    "/Script/Engine.",
]

# Content Browser directories searched in Step 4
_SEARCH_DIRS = ["/Game/Creative/Devices", "/Fortnite", "/Game"]


# ─── Low-level helpers ───────────────────────────────────────────────────────

def try_load_class(path: str):
    """Try to load a class from a path, return None on failure."""
    try:
        return unreal.load_class(None, path)
    except Exception:
        return None


def try_load_asset(path: str):
    """Try to load an asset from a path, return None on failure."""
    try:
        return unreal.EditorAssetLibrary.load_asset(path)
    except Exception:
        return None


# ─── Content Browser search ─────────────────────────────────────────────────

def fuzzy_search_assets(query: str, limit: int = 10) -> List[Dict[str, str]]:
    """Search the Asset Registry for assets whose name contains the query."""
    query_lower = query.lower().replace(" ", "").replace("_", "")
    results: List[Dict[str, str]] = []

    for search_dir in _SEARCH_DIRS:
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


# ─── Resolution pipeline ────────────────────────────────────────────────────

def _resolve_alias(name_lower: str) -> tuple:
    """Step 1: Check built-in device alias map. Returns (path, via, loadable)."""
    if name_lower not in DEVICE_ALIASES:
        return ("", "", None)

    primary, fallbacks = DEVICE_ALIASES[name_lower]
    for path in [primary] + fallbacks:
        cls = try_load_class(path)
        if cls:
            return (path, "device_alias (class)", cls)
        asset = try_load_asset(path)
        if asset:
            return (path, "device_alias (asset)", asset)
    return ("", "", None)


def _resolve_exact(name: str) -> tuple:
    """Step 2: Try as exact asset/class path. Returns (path, via, loadable)."""
    if "/" not in name and "." not in name:
        return ("", "", None)

    asset = try_load_asset(name)
    if asset:
        return (name, "exact_asset_path", asset)
    cls = try_load_class(name)
    if cls:
        return (name, "exact_class_path", cls)
    return ("", "", None)


def _resolve_prefix(name: str) -> tuple:
    """Step 3: Try common class prefixes. Returns (path, via, cls)."""
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
    """Step 4: Fuzzy search in Content Browser. Returns (path, via, asset) or candidates."""
    candidates = fuzzy_search_assets(name)
    if not candidates:
        return ("", "", None)

    best = candidates[0]
    asset = try_load_asset(best["path"])
    if asset:
        return (best["path"], "content_browser_search", asset)
    # Return candidates as a special marker
    return ("", "candidates_only", candidates)


def resolve(name: str) -> Dict[str, Any]:
    """
    Resolve a natural name to a Content Browser path.

    Returns dict with keys: resolved_path, resolved_via, loadable, candidates.
    """
    name_lower = name.strip().lower()

    # Step 1: alias map
    path, via, loadable = _resolve_alias(name_lower)
    if path:
        return {"resolved_path": path, "resolved_via": via, "loadable": loadable}

    # Step 2: exact path
    path, via, loadable = _resolve_exact(name)
    if path:
        return {"resolved_path": path, "resolved_via": via, "loadable": loadable}

    # Step 3: class prefix search
    path, via, loadable = _resolve_prefix(name)
    if path:
        return {"resolved_path": path, "resolved_via": via, "loadable": loadable}

    # Step 4: fuzzy Content Browser search
    path, via, loadable = _resolve_fuzzy(name)
    if path:
        return {"resolved_path": path, "resolved_via": via, "loadable": loadable}
    if via == "candidates_only":
        return {"resolved_path": "", "resolved_via": "", "loadable": None, "candidates": loadable}

    return {"resolved_path": "", "resolved_via": "", "loadable": None}


def spawn(
    name: str,
    location: Optional[List[float]] = None,
    rotation: Optional[List[float]] = None,
    label: str = "",
    dry_run: bool = False,
    serializer: Any = None,
) -> dict:
    """
    Spawn an actor by natural name with intelligent path resolution.

    Args:
        name:       Natural name or exact path.
        location:   World location [x, y, z].
        rotation:   Rotation [pitch, yaw, roll] degrees.
        label:      Optional outliner label.
        dry_run:    If True, resolve only — don't spawn.
        serializer: Callable to serialize the spawned actor (optional).
    """
    if not name:
        raise ValueError("name is required — e.g. 'button', 'timer', 'spawn pad', or an asset path")

    loc = unreal.Vector(*location) if location else unreal.Vector(0, 0, 0)
    rot = unreal.Rotator(*rotation) if rotation else unreal.Rotator(0, 0, 0)
    sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    result = resolve(name)
    resolved_path = result["resolved_path"]
    resolved_via = result["resolved_via"]
    loadable = result.get("loadable")
    candidates = result.get("candidates")

    # No match at all
    if not resolved_path and not candidates:
        return {
            "status": "error",
            "error": f"Could not resolve '{name}' to any asset or class.",
            "suggestions": [
                "Try a more specific name (e.g. 'button', 'timer', 'teleporter')",
                "Use spawn_actor with an exact asset_path from Content Browser",
                "Use search_assets to find available assets first",
                "Run device_catalog_scan to build a full device catalog",
            ],
            "known_aliases": sorted(DEVICE_ALIASES.keys()),
        }

    # Found candidates but couldn't load
    if candidates and not resolved_path:
        return {
            "status": "not_spawned",
            "reason": "Found candidates but could not load them. Pick one and use spawn_actor with exact asset_path.",
            "query": name,
            "candidates": candidates,
        }

    # Dry run — resolve only
    if dry_run:
        return {
            "status": "dry_run",
            "resolved_path": resolved_path,
            "resolved_via": resolved_via,
            "query": name,
        }

    # Spawn
    actor = None
    if resolved_via.endswith("(class)") or resolved_via == "class_prefix_search" or resolved_via == "exact_class_path":
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
        raise ValueError("query is required — e.g. 'button', 'timer', 'tree'")
    results = fuzzy_search_assets(query, limit=limit)
    return {
        "query": query,
        "results": results,
        "count": len(results),
        "tip": "Use the 'path' from results with spawn_actor(asset_path=...) or smart_spawn(name=...)",
    }


def list_aliases() -> dict:
    """List all known device aliases for smart_spawn."""
    aliases = {}
    for alias, (primary, fallbacks) in sorted(DEVICE_ALIASES.items()):
        aliases[alias] = {"primary_path": primary, "fallbacks": fallbacks}
    return {"aliases": aliases, "count": len(aliases)}
