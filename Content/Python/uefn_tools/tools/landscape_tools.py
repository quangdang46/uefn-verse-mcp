"""
uefn_tools — Landscape Tools
==================================
Tools for inspecting and auditing Landscape actors in the level.

What Python CAN do:
  • List all Landscape actors in the current level
  • Inspect material, component count, section size, and render properties
  • Audit landscapes for missing materials or high component counts
  • Assign a material to a Landscape actor

What Python CANNOT do:
  • Edit heightmap data (height/weight painting is editor UI only)
  • Add or remove landscape layers programmatically
  • Import heightmaps from external files via Python
  • Create new Landscape actors (no factory exposed in UEFN Python)

API: EditorActorSubsystem, Landscape, LandscapeProxy, LandscapeComponent
"""

from __future__ import annotations

import math
import random
import unreal
from ..registry import register_tool
from ..core import (
    log_info,
    log_error,
    log_warning,
    undo_transaction,
    spawn_static_mesh_actor,
    get_selected_actors,
)


def _actor_sub():
    return unreal.get_editor_subsystem(unreal.EditorActorSubsystem)


def _get_landscapes():
    """Return all Landscape and LandscapeProxy actors in the current level."""
    all_actors = _actor_sub().get_all_level_actors()
    result = []
    for a in (all_actors or []):
        try:
            if isinstance(a, (unreal.Landscape, unreal.LandscapeProxy)):
                result.append(a)
        except Exception:
            pass
    return result


# ── Tools ──────────────────────────────────────────────────────────────────────

@register_tool(
    name="landscape_list",
    category="Landscape",
    description=(
        "List all Landscape actors in the current level. "
        "Returns label, location, assigned material, and component count for each. "
        "Use before landscape_audit to see how many landscapes are in the map."
    ),
    tags=["landscape", "list", "level", "terrain", "scan"],
    example='tb.run("landscape_list")',
)
def run_landscape_list(**kwargs) -> dict:
    try:
        landscapes = _get_landscapes()
        results = []
        for a in landscapes:
            entry = {
                "label": str(a.get_actor_label()),
                "class": type(a).__name__,
            }
            try:
                loc = a.get_actor_location()
                entry["location"] = [round(loc.x), round(loc.y), round(loc.z)]
            except Exception:
                pass
            try:
                mat = a.get_editor_property("landscape_material")
                entry["material"] = str(mat.get_path_name()) if mat else "none"
            except Exception:
                entry["material"] = "unknown"
            try:
                comps = a.get_components_by_class(unreal.LandscapeComponent)
                entry["component_count"] = len(comps) if comps else 0
            except Exception:
                entry["component_count"] = 0
            results.append(entry)

        log_info(f"[landscape_list] {len(results)} landscape actor(s) in level")
        return {"status": "ok", "count": len(results), "landscapes": results}
    except Exception as e:
        log_error(f"[landscape_list] {e}")
        return {"status": "error", "message": str(e)}


@register_tool(
    name="landscape_audit",
    category="Landscape",
    description=(
        "Audit all Landscape actors in the level for common issues: "
        "missing material or very high component count (performance risk). "
        "Returns a health report with per-landscape status and issue descriptions."
    ),
    tags=["landscape", "audit", "material", "performance", "health"],
    example='tb.run("landscape_audit", warn_components=256)',
)
def run_landscape_audit(warn_components: int = 256, **kwargs) -> dict:
    try:
        landscapes = _get_landscapes()
        issues = []
        clean = []

        for a in landscapes:
            label = str(a.get_actor_label())
            ls_issues = []

            try:
                mat = a.get_editor_property("landscape_material")
                if not mat:
                    ls_issues.append("No landscape material assigned")
            except Exception:
                pass

            try:
                comps = a.get_components_by_class(unreal.LandscapeComponent)
                count = len(comps) if comps else 0
                if count > warn_components:
                    ls_issues.append(f"High component count: {count} (warn={warn_components})")
            except Exception:
                pass

            if ls_issues:
                issues.append({"label": label, "issues": ls_issues})
            else:
                clean.append(label)

        log_info(f"[landscape_audit] {len(clean)} clean, {len(issues)} with issues")
        return {
            "status": "ok",
            "total": len(landscapes),
            "clean": len(clean),
            "issues": len(issues),
            "issue_list": issues,
        }
    except Exception as e:
        log_error(f"[landscape_audit] {e}")
        return {"status": "error", "message": str(e)}


@register_tool(
    name="landscape_info",
    category="Landscape",
    description=(
        "Get detailed info on a Landscape actor: material, component count, "
        "section size, quads per section, and render properties. "
        "Specify label to target a specific landscape, or leave blank for first found."
    ),
    tags=["landscape", "info", "inspect", "components", "sections"],
    example='tb.run("landscape_info", label="Landscape")',
)
def run_landscape_info(label: str = "", **kwargs) -> dict:
    try:
        landscapes = _get_landscapes()
        target = None
        for a in landscapes:
            if not label or label.lower() in str(a.get_actor_label()).lower():
                target = a
                break

        if target is None:
            return {"status": "error", "message": f"No Landscape actor found{' matching ' + repr(label) if label else ''}."}

        info = {
            "label": str(target.get_actor_label()),
            "class": type(target).__name__,
        }

        try:
            loc = target.get_actor_location()
            info["location"] = [round(loc.x), round(loc.y), round(loc.z)]
        except Exception:
            pass

        for prop in ("landscape_material", "component_size_quads", "num_subcomponents",
                     "subsection_size_quads", "static_lighting_resolution"):
            try:
                val = target.get_editor_property(prop)
                info[prop] = str(val) if val is not None else "unknown"
            except Exception:
                pass

        try:
            comps = target.get_components_by_class(unreal.LandscapeComponent)
            info["component_count"] = len(comps) if comps else 0
        except Exception:
            pass

        log_info(f"[landscape_info] {info['label']}: {info.get('component_count', '?')} components")
        return {"status": "ok", **info}
    except Exception as e:
        log_error(f"[landscape_info] {e}")
        return {"status": "error", "message": str(e)}


@register_tool(
    name="landscape_set_material",
    category="Landscape",
    description=(
        "Assign a material to a Landscape actor. "
        "Use label to target a specific landscape (leave blank for first found). "
        "Always dry_run=True first — this modifies the landscape material slot."
    ),
    tags=["landscape", "material", "assign", "set"],
    example='tb.run("landscape_set_material", material_path="/Game/Materials/M_Terrain", dry_run=False)',
)
def run_landscape_set_material(
    material_path: str = "",
    label: str = "",
    dry_run: bool = True,
    **kwargs,
) -> dict:
    if not material_path:
        return {"status": "error", "message": "material_path is required."}
    try:
        landscapes = _get_landscapes()
        target = None
        for a in landscapes:
            if not label or label.lower() in str(a.get_actor_label()).lower():
                target = a
                break

        if target is None:
            return {"status": "error", "message": f"No Landscape actor found{' matching ' + repr(label) if label else ''}."}

        mat = unreal.EditorAssetLibrary.load_asset(material_path)
        if mat is None:
            return {"status": "error", "message": f"Could not load material at '{material_path}'."}

        ls_label = str(target.get_actor_label())
        if not dry_run:
            target.set_editor_property("landscape_material", mat)

        action = "Would assign" if dry_run else "Assigned"
        log_info(f"[landscape_set_material] {action} {material_path} → {ls_label}")
        return {
            "status": "ok",
            "dry_run": dry_run,
            "landscape": ls_label,
            "material": material_path,
        }
    except Exception as e:
        log_error(f"[landscape_set_material] {e}")
        return {"status": "error", "message": str(e)}


# ── Material Instance (Landscape-ready parent chain) ───────────────────────────
#
# How to run (UEFN editor, Python enabled):
#   1. Copy/sync `Content/Python/uefn_tools/` into your island project (e.g. `python deploy.py`
#      from this repo). Restart UEFN if the editor was already open so Python picks up changes.
#   2. Optional MCP listener refresh: `import uefn_tools as ut; ut.run("mcp_start")`
#   3. Via registry (after reload/restart):
#        import uefn_tools as tb
#        print(tb.run("landscape_material_create_project_mic",
#                     asset_name="MI_MyTerrain"))
#      kwargs: template_mic_path, package_folder="/Game/Materials", asset_name=...
#   4. Bypass registry (always works once this file is on disk):
#        from uefn_tools.tools.landscape_tools import run_landscape_material_create_project_mic
#        print(run_landscape_material_create_project_mic(asset_name="MI_MyTerrain"))

DEFAULT_LANDSCAPE_TEMPLATE_MIC = (
    "/Game/Athena/Environments/Landscape/Creative/"
    "M_Athena_Terrain_TropicalBiome_Inst_Basic.M_Athena_Terrain_TropicalBiome_Inst_Basic"
)


@register_tool(
    name="landscape_material_create_project_mic",
    category="Landscape",
    description=(
        "Create a project MaterialInstanceConstant suitable for Landscape assignment by "
        "parenting it to an Athena terrain MIC template (full Landscape blend graph). "
        "Edit the new MIC in the Material Instance Editor — duplicate Epic templates "
        "via AssetTools can timeout on heavy master Materials; MIC parenting is reliable."
    ),
    tags=["landscape", "material", "mic", "terrain", "create"],
    example=(
        'tb.run("landscape_material_create_project_mic", '
        'asset_name="MI_MyIslandTerrain")'
    ),
)
def run_landscape_material_create_project_mic(
    template_mic_path: str = DEFAULT_LANDSCAPE_TEMPLATE_MIC,
    package_folder: str = "/Game/Materials",
    asset_name: str = "MI_CustomLandscape",
    **kwargs,
) -> dict:
    """
    Args:
        template_mic_path: Existing MIC asset path (Athena terrain instance recommended).
        package_folder:    Content folder for the new MIC (created if missing).
        asset_name:        Asset name without path (e.g. MI_CustomLandscape).

    Returns:
        {"status": "ok", "path": str} or {"status": "error", "message": str}
    """
    full_path = f"{package_folder}/{asset_name}"
    try:
        if not unreal.EditorAssetLibrary.does_directory_exist(package_folder):
            unreal.EditorAssetLibrary.make_directory(package_folder)

        parent = unreal.EditorAssetLibrary.load_asset(template_mic_path)
        if parent is None:
            msg = f"Could not load template MIC: {template_mic_path}"
            log_error(f"[landscape_material_create_project_mic] {msg}")
            return {"status": "error", "message": msg}

        if unreal.EditorAssetLibrary.does_asset_exist(full_path):
            unreal.EditorAssetLibrary.delete_asset(full_path)

        factory = unreal.MaterialInstanceConstantFactoryNew()
        at = unreal.AssetToolsHelpers.get_asset_tools()
        mi = at.create_asset(
            asset_name, package_folder,
            unreal.MaterialInstanceConstant, factory,
        )
        if mi is None:
            msg = f"create_asset failed for {full_path}"
            log_error(f"[landscape_material_create_project_mic] {msg}")
            return {"status": "error", "message": msg}

        unreal.MaterialEditingLibrary.set_material_instance_parent(mi, parent)
        unreal.MaterialEditingLibrary.update_material_instance(mi)
        unreal.EditorAssetLibrary.save_asset(mi.get_path_name())

        path_str = mi.get_path_name()
        log_info(f"[landscape_material_create_project_mic] Created → {path_str}")
        return {"status": "ok", "path": path_str, "template": template_mic_path}
    except Exception as e:
        log_error(f"[landscape_material_create_project_mic] {e}")
        return {"status": "error", "message": str(e)}


def _height_value(
    gx: int,
    gy: int,
    grid_size: int,
    max_height_cm: float,
    noise_scale: float,
    seed: int,
    falloff: float,
) -> float:
    """
    Generate a terrain-like height value with radial falloff + light noise.
    """
    cx = (grid_size - 1) * 0.5
    cy = (grid_size - 1) * 0.5
    dx = gx - cx
    dy = gy - cy
    dist = math.sqrt(dx * dx + dy * dy)
    max_dist = max(1.0, math.sqrt(cx * cx + cy * cy))
    radial = max(0.0, 1.0 - (dist / max_dist))
    radial = radial ** max(0.1, falloff)

    phase = float(seed) * 0.173
    n1 = math.sin((gx + phase) * noise_scale)
    n2 = math.cos((gy - phase) * noise_scale * 1.23)
    n3 = math.sin((gx + gy + phase) * noise_scale * 0.7)
    noise = (n1 + n2 + n3) / 3.0  # -1..1
    noise01 = 0.5 + 0.5 * noise

    return max_height_cm * (0.65 * radial + 0.35 * noise01)


@register_tool(
    name="terrain_blockout_generate",
    category="Landscape",
    description=(
        "Generate a fast terrain blockout from stacked StaticMesh columns "
        "(radial island + noise). Useful when Landscape sculpting tools are unavailable."
    ),
    tags=["terrain", "blockout", "procedural", "landscape", "island", "height"],
    example='tb.run("terrain_blockout_generate", grid_size=20, tile_size_cm=400)',
)
def run_terrain_blockout_generate(
    grid_size: int = 20,
    tile_size_cm: float = 400.0,
    max_height_cm: float = 2000.0,
    base_z: float = 0.0,
    center: tuple[float, float, float] = (0.0, 0.0, 0.0),
    noise_scale: float = 0.35,
    falloff: float = 1.35,
    min_column_height_cm: float = 80.0,
    mesh_path: str = "/Engine/BasicShapes/Cube",
    folder: str = "Terrain_Blockout",
    label_prefix: str = "TerrainTile",
    seed: int = 1337,
    focus: bool = True,
    **kwargs,
) -> dict:
    """
    Create a quick terrain massing using static mesh columns.
    """
    if grid_size < 2:
        return {"status": "error", "message": "grid_size must be >= 2"}
    if tile_size_cm <= 0 or max_height_cm <= 0:
        return {"status": "error", "message": "tile_size_cm and max_height_cm must be > 0"}

    rng = random.Random(seed)
    cx, cy, cz = center
    half = (grid_size - 1) * 0.5
    placed = []

    with undo_transaction(f"Terrain Blockout Generate ({grid_size}x{grid_size})"):
        for gx in range(grid_size):
            for gy in range(grid_size):
                h = _height_value(
                    gx=gx,
                    gy=gy,
                    grid_size=grid_size,
                    max_height_cm=max_height_cm,
                    noise_scale=noise_scale,
                    seed=seed,
                    falloff=falloff,
                )
                h = max(min_column_height_cm, h + rng.uniform(-40.0, 40.0))

                world_x = cx + (gx - half) * tile_size_cm
                world_y = cy + (gy - half) * tile_size_cm
                world_z = cz + base_z + h * 0.5

                actor = spawn_static_mesh_actor(
                    mesh_path,
                    unreal.Vector(world_x, world_y, world_z),
                    scale=unreal.Vector(
                        tile_size_cm / 100.0,
                        tile_size_cm / 100.0,
                        h / 100.0,
                    ),
                )
                if actor:
                    actor.set_folder_path(f"/{folder}")
                    actor.set_actor_label(f"{label_prefix}_{gx:02d}_{gy:02d}")
                    placed.append(actor)

    if focus and placed:
        try:
            _actor_sub().set_selected_level_actors(placed)
            unreal.SystemLibrary.execute_console_command(
                unreal.EditorLevelLibrary.get_editor_world(), "CAMERA ALIGN"
            )
        except Exception:
            pass

    log_info(f"[terrain_blockout_generate] Placed {len(placed)} actors in /{folder}")
    return {
        "status": "ok",
        "placed": len(placed),
        "grid_size": grid_size,
        "tile_size_cm": tile_size_cm,
        "folder": folder,
        "seed": seed,
    }


@register_tool(
    name="terrain_noise_selected",
    category="Landscape",
    description=(
        "Apply noise-based vertical sculpting to selected actors "
        "(great for roughing cliffs/hills after blockout generation)."
    ),
    tags=["terrain", "noise", "sculpt", "selected", "height", "blockout"],
    example='tb.run("terrain_noise_selected", amplitude_cm=250, frequency=0.002)',
)
def run_terrain_noise_selected(
    amplitude_cm: float = 250.0,
    frequency: float = 0.002,
    seed: int = 1337,
    world_axis_bias: tuple[float, float] = (1.0, 1.0),
    folder: str = "",
    label_contains: str = "",
    **kwargs,
) -> dict:
    selected = get_selected_actors()
    if not selected and (folder or label_contains):
        all_actors = _actor_sub().get_all_level_actors() or []
        f = folder.lower().strip()
        l = label_contains.lower().strip()
        selected = [
            a for a in all_actors
            if (not f or f in str(a.get_folder_path() or "").lower())
            and (not l or l in str(a.get_actor_label() or "").lower())
        ]
    if not selected:
        return {
            "status": "error",
            "message": "No target actors found. Select actors or pass folder/label_contains.",
        }
    if amplitude_cm == 0:
        return {"status": "error", "message": "amplitude_cm must be non-zero."}
    if frequency <= 0:
        return {"status": "error", "message": "frequency must be > 0."}

    ax, ay = world_axis_bias
    modified = 0

    with undo_transaction("Terrain Noise Sculpt Selected"):
        for actor in selected:
            try:
                loc = actor.get_actor_location()
                n = (
                    math.sin((loc.x * ax + seed * 17.0) * frequency)
                    + math.cos((loc.y * ay - seed * 23.0) * frequency * 1.3)
                ) * 0.5
                loc.z += n * amplitude_cm
                actor.set_actor_location(loc, False, False)
                modified += 1
            except Exception:
                continue

    log_info(f"[terrain_noise_selected] Modified {modified} actor(s)")
    return {
        "status": "ok",
        "modified": modified,
        "amplitude_cm": amplitude_cm,
        "target_mode": "selection" if not (folder or label_contains) else "query",
    }


@register_tool(
    name="terrain_blockout_clear",
    category="Landscape",
    description="Delete all generated terrain blockout actors in a folder (undoable).",
    tags=["terrain", "blockout", "clear", "cleanup", "delete"],
    example='tb.run("terrain_blockout_clear", folder="Terrain_Blockout")',
)
def run_terrain_blockout_clear(
    folder: str = "Terrain_Blockout",
    **kwargs,
) -> dict:
    all_actors = _actor_sub().get_all_level_actors() or []
    targets = [
        a for a in all_actors
        if folder.lower() in str(a.get_folder_path() or "").lower()
    ]

    if not targets:
        return {"status": "ok", "deleted": 0, "folder": folder}

    with undo_transaction(f"Terrain Blockout Clear ({folder})"):
        try:
            _actor_sub().destroy_actors(targets)
        except Exception:
            for actor in targets:
                try:
                    _actor_sub().destroy_actor(actor)
                except Exception:
                    pass

    log_info(f"[terrain_blockout_clear] Deleted {len(targets)} actor(s) from /{folder}")
    return {"status": "ok", "deleted": len(targets), "folder": folder}


def _resolve_terrain_targets(folder: str = "", label_contains: str = ""):
    """
    Resolve target actors from selection, or from folder/label filters.
    """
    targets = get_selected_actors()
    if targets:
        return targets, "selection"

    all_actors = _actor_sub().get_all_level_actors() or []
    f = folder.lower().strip()
    l = label_contains.lower().strip()
    targets = [
        a for a in all_actors
        if (not f or f in str(a.get_folder_path() or "").lower())
        and (not l or l in str(a.get_actor_label() or "").lower())
    ]
    return targets, "query"


def _distance_point_to_segment_2d(
    px: float, py: float, ax: float, ay: float, bx: float, by: float
) -> float:
    """
    Shortest 2D distance from point P to line segment AB.
    """
    abx = bx - ax
    aby = by - ay
    apx = px - ax
    apy = py - ay
    ab2 = abx * abx + aby * aby
    if ab2 <= 1e-6:
        return math.sqrt((px - ax) ** 2 + (py - ay) ** 2)
    t = max(0.0, min(1.0, (apx * abx + apy * aby) / ab2))
    qx = ax + abx * t
    qy = ay + aby * t
    return math.sqrt((px - qx) ** 2 + (py - qy) ** 2)


def _coerce_path_points(points: list) -> list[tuple[float, float, float]]:
    coerced = []
    for p in points or []:
        if not isinstance(p, (list, tuple)) or len(p) < 2:
            continue
        x = float(p[0])
        y = float(p[1])
        z = float(p[2]) if len(p) > 2 else 0.0
        coerced.append((x, y, z))
    return coerced


@register_tool(
    name="terrain_flatten",
    category="Landscape",
    description=(
        "Flatten terrain actors toward a target Z height with optional radial falloff. "
        "Uses selected actors, or folder/label query if nothing is selected."
    ),
    tags=["terrain", "flatten", "height", "sculpt", "blockout"],
    example='tb.run("terrain_flatten", target_z_cm=100, strength=0.5, folder="Terrain_Blockout")',
)
def run_terrain_flatten(
    target_z_cm: float = 0.0,
    strength: float = 1.0,
    center: tuple[float, float, float] = (0.0, 0.0, 0.0),
    radius_cm: float = 0.0,
    folder: str = "",
    label_contains: str = "",
    **kwargs,
) -> dict:
    """
    Pull actor Z toward a target elevation.
    """
    targets, mode = _resolve_terrain_targets(folder=folder, label_contains=label_contains)
    if not targets:
        return {"status": "error", "message": "No target actors found."}
    if not (0.0 <= strength <= 1.0):
        return {"status": "error", "message": "strength must be between 0 and 1."}

    cx, cy, _ = center
    modified = 0
    moved_avg = 0.0

    with undo_transaction("Terrain Flatten"):
        for actor in targets:
            try:
                loc = actor.get_actor_location()
                influence = 1.0
                if radius_cm > 0.0:
                    d = math.sqrt((loc.x - cx) ** 2 + (loc.y - cy) ** 2)
                    if d > radius_cm:
                        continue
                    influence = max(0.0, 1.0 - (d / radius_cm))

                alpha = strength * influence
                old_z = loc.z
                loc.z = old_z + (target_z_cm - old_z) * alpha
                actor.set_actor_location(loc, False, False)
                modified += 1
                moved_avg += abs(loc.z - old_z)
            except Exception:
                continue

    avg = moved_avg / modified if modified else 0.0
    log_info(f"[terrain_flatten] Modified {modified} actor(s), avg shift {avg:.1f}cm")
    return {
        "status": "ok",
        "modified": modified,
        "avg_shift_cm": round(avg, 2),
        "target_z_cm": target_z_cm,
        "target_mode": mode,
    }


@register_tool(
    name="terrain_ridge_line",
    category="Landscape",
    description=(
        "Raise terrain along a polyline to form ridges/hills. "
        "Uses selected actors, or folder/label query if nothing is selected."
    ),
    tags=["terrain", "ridge", "mountain", "line", "height", "sculpt"],
    example='tb.run("terrain_ridge_line", points=[[0,0,0],[4000,0,0]], height_cm=600, width_cm=900)',
)
def run_terrain_ridge_line(
    points: list | None = None,
    height_cm: float = 400.0,
    width_cm: float = 800.0,
    falloff_power: float = 1.5,
    folder: str = "",
    label_contains: str = "",
    **kwargs,
) -> dict:
    path = _coerce_path_points(points or [])
    if len(path) < 2:
        return {"status": "error", "message": "points must contain at least two [x,y,z] entries."}
    if width_cm <= 0.0:
        return {"status": "error", "message": "width_cm must be > 0."}

    targets, mode = _resolve_terrain_targets(folder=folder, label_contains=label_contains)
    if not targets:
        return {"status": "error", "message": "No target actors found."}

    modified = 0
    moved_avg = 0.0

    with undo_transaction("Terrain Ridge Line"):
        for actor in targets:
            try:
                loc = actor.get_actor_location()
                dmin = 10e9
                for i in range(len(path) - 1):
                    ax, ay, _ = path[i]
                    bx, by, _ = path[i + 1]
                    d = _distance_point_to_segment_2d(loc.x, loc.y, ax, ay, bx, by)
                    if d < dmin:
                        dmin = d
                if dmin > width_cm:
                    continue
                influence = max(0.0, 1.0 - (dmin / width_cm)) ** max(0.1, falloff_power)
                dz = height_cm * influence
                loc.z += dz
                actor.set_actor_location(loc, False, False)
                modified += 1
                moved_avg += abs(dz)
            except Exception:
                continue

    avg = moved_avg / modified if modified else 0.0
    log_info(f"[terrain_ridge_line] Modified {modified} actor(s), avg raise {avg:.1f}cm")
    return {
        "status": "ok",
        "modified": modified,
        "avg_raise_cm": round(avg, 2),
        "target_mode": mode,
    }


@register_tool(
    name="terrain_path_cut",
    category="Landscape",
    description=(
        "Cut a lowered path/trench along a polyline. "
        "Great for roads, rivers, and gameplay lanes."
    ),
    tags=["terrain", "path", "cut", "road", "river", "trench", "sculpt"],
    example='tb.run("terrain_path_cut", points=[[0,0,0],[4000,0,0]], depth_cm=300, width_cm=900)',
)
def run_terrain_path_cut(
    points: list | None = None,
    depth_cm: float = 300.0,
    width_cm: float = 900.0,
    shoulder_cm: float = 200.0,
    folder: str = "",
    label_contains: str = "",
    **kwargs,
) -> dict:
    path = _coerce_path_points(points or [])
    if len(path) < 2:
        return {"status": "error", "message": "points must contain at least two [x,y,z] entries."}
    if width_cm <= 0.0:
        return {"status": "error", "message": "width_cm must be > 0."}
    if depth_cm <= 0.0:
        return {"status": "error", "message": "depth_cm must be > 0."}

    targets, mode = _resolve_terrain_targets(folder=folder, label_contains=label_contains)
    if not targets:
        return {"status": "error", "message": "No target actors found."}

    inner = width_cm
    outer = width_cm + max(0.0, shoulder_cm)
    modified = 0
    moved_avg = 0.0

    with undo_transaction("Terrain Path Cut"):
        for actor in targets:
            try:
                loc = actor.get_actor_location()
                dmin = 10e9
                for i in range(len(path) - 1):
                    ax, ay, _ = path[i]
                    bx, by, _ = path[i + 1]
                    d = _distance_point_to_segment_2d(loc.x, loc.y, ax, ay, bx, by)
                    if d < dmin:
                        dmin = d
                if dmin > outer:
                    continue

                if dmin <= inner:
                    influence = 1.0
                else:
                    edge_t = (dmin - inner) / max(1.0, (outer - inner))
                    influence = max(0.0, 1.0 - edge_t)

                dz = depth_cm * influence
                loc.z -= dz
                actor.set_actor_location(loc, False, False)
                modified += 1
                moved_avg += abs(dz)
            except Exception:
                continue

    avg = moved_avg / modified if modified else 0.0
    log_info(f"[terrain_path_cut] Modified {modified} actor(s), avg lower {avg:.1f}cm")
    return {
        "status": "ok",
        "modified": modified,
        "avg_lower_cm": round(avg, 2),
        "target_mode": mode,
    }
