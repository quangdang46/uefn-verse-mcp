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

import unreal
from ..registry import register_tool
from ..core import log_info, log_error, log_warning


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
