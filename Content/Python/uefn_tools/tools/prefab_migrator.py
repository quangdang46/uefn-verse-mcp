"""
uefn_tools — Prefab Asset Migrator (headless / MCP)
====================================================
Dependency-aware asset export with no editor UI.

Use from MCP, scripts, or REPL via registered tools:
  • prefab_parse_refs           — T3D clipboard text -> package paths
  • prefab_resolve_deps         — seeds -> full dependency closure
  • prefab_export_to_disk       — copy .uasset files to another folder (cross-project)
  • prefab_export_within_project — duplicate assets under a /Mount/... folder (same project)

Features:
  • AssetRegistry dependency walk (meshes, materials, textures, etc.)
  • Flatten option for single-folder output
  • Cross-project raw .uasset copy via shutil
  • Dry-run previews on export tools
"""

from __future__ import annotations

import os
import re
import shutil
from typing import List, Set, Dict, Tuple

import unreal

from ..registry import register_tool

# ── Asset path helpers ────────────────────────────────────────────────────────

_T3D_PATH_RE = re.compile(
    r"['\"]?(\/[A-Za-z][A-Za-z0-9_]+(?:\/[A-Za-z0-9_\-\.]+)+)['\"]?",
)

_T3D_SKIP_MOUNTS = {
    "/Engine", "/Script", "/Transient", "/FortniteGame", "/Fortnite",
    "/Paper2D", "/Plugin", "/Plugins", "/Epic", "/Fortnite.com",
}


def _normalize_pkg(path: str) -> str:
    """Strip .AssetName suffix so we always work with package paths."""
    if "." in path.rsplit("/", 1)[-1]:
        path = path.rsplit(".", 1)[0]
    return path.rstrip("/")


def _pkg_to_asset(pkg: str) -> str:
    name = pkg.rsplit("/", 1)[-1]
    return f"{pkg}.{name}"


def _pkg_to_disk(pkg: str, content_dir: str) -> str:
    parts = pkg.lstrip("/").split("/", 1)
    relative = parts[1] if len(parts) > 1 else parts[0]
    return os.path.join(content_dir, relative.replace("/", os.sep) + ".uasset")


def _parse_t3d(text: str) -> List[str]:
    seen: Set[str] = set()
    for m in _T3D_PATH_RE.finditer(text):
        raw = m.group(1)
        pkg = _normalize_pkg(raw)
        if any(pkg.startswith(s) for s in _T3D_SKIP_MOUNTS):
            continue
        if pkg.count("/") < 2:
            continue
        if pkg not in seen:
            seen.add(pkg)
    return sorted(seen)


def _resolve_deps(packages: List[str], include_deps: bool = True) -> Tuple[Set[str], List[str]]:
    ar = unreal.AssetRegistryHelpers.get_asset_registry()

    dep_options = unreal.AssetRegistryDependencyOptions()
    dep_options.include_hard_package_references = True
    dep_options.include_soft_package_references = True
    dep_options.include_game_package_references = True
    dep_options.include_editor_only_package_references = False
    dep_options.include_searchable_names = False
    dep_options.include_soft_management_references = False
    dep_options.include_hard_management_references = False

    _SKIP_PREFIXES = ("/Engine/", "/FortniteGame/", "/Paper2D/", "/Script/")

    visited: Set[str] = set()
    warnings: List[str] = []
    queue = [_normalize_pkg(p) for p in packages]

    while queue:
        pkg = queue.pop()
        if pkg in visited:
            continue
        visited.add(pkg)

        if not include_deps:
            continue

        try:
            deps = ar.get_dependencies(pkg, dep_options) or []
            for dep in deps:
                dep_str = _normalize_pkg(str(dep))
                if dep_str and not any(dep_str.startswith(s) for s in _SKIP_PREFIXES) and dep_str not in visited:
                    queue.append(dep_str)
        except Exception as exc:
            warnings.append(f"dep scan failed for {pkg}: {exc}")

    return visited, warnings


def _export_to_disk(
    packages: Set[str],
    src_content: str,
    dst_content: str,
    flatten: bool,
    overwrite: bool,
    dry_run: bool,
) -> Dict[str, List[str]]:
    results: Dict[str, List[str]] = {"ok": [], "skip": [], "missing": [], "error": []}

    for pkg in sorted(packages):
        src_file = _pkg_to_disk(pkg, src_content)

        if not os.path.exists(src_file):
            results["missing"].append(pkg)
            continue

        asset_name = pkg.rsplit("/", 1)[-1]
        if flatten:
            dst_file = os.path.join(dst_content, asset_name + ".uasset")
        else:
            parts = pkg.lstrip("/").split("/", 1)
            relative = parts[1] if len(parts) > 1 else asset_name
            dst_file = os.path.join(dst_content, relative.replace("/", os.sep) + ".uasset")

        if os.path.exists(dst_file) and not overwrite:
            results["skip"].append(pkg)
            continue

        if dry_run:
            results["ok"].append(f"[DRY] {pkg}")
            continue

        try:
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)
            results["ok"].append(pkg)
        except Exception as exc:
            results["error"].append(f"{pkg}: {exc}")

    return results


def _export_within_project(
    packages: Set[str],
    dest_folder: str,
    flatten: bool,
    overwrite: bool,
    dry_run: bool,
) -> Dict[str, List[str]]:
    eal = unreal.EditorAssetLibrary
    results: Dict[str, List[str]] = {"ok": [], "skip": [], "missing": [], "error": []}
    dest_folder = dest_folder.rstrip("/")

    for pkg in sorted(packages):
        asset_path = _pkg_to_asset(pkg)

        if not eal.does_asset_exist(asset_path):
            results["missing"].append(pkg)
            continue

        asset_name = pkg.rsplit("/", 1)[-1]
        if flatten:
            dst_pkg = f"{dest_folder}/{asset_name}"
        else:
            parts = pkg.lstrip("/").split("/", 1)
            relative = parts[1] if len(parts) > 1 else asset_name
            dst_pkg = f"{dest_folder}/{relative}"

        dst_asset = _pkg_to_asset(dst_pkg)

        if eal.does_asset_exist(dst_asset) and not overwrite:
            results["skip"].append(pkg)
            continue

        if dry_run:
            results["ok"].append(f"[DRY] {pkg} → {dst_pkg}")
            continue

        try:
            eal.duplicate_asset(asset_path, dst_pkg)
            eal.save_asset(dst_pkg, only_if_is_dirty=False)
            results["ok"].append(pkg)
        except Exception as exc:
            results["error"].append(f"{pkg}: {exc}")

    if not dry_run and results["ok"]:
        try:
            unreal.AssetRegistryHelpers.get_asset_registry().search_all_assets(True)
        except Exception:
            pass

    return results


# ── Registered tools (MCP / headless only) ────────────────────────────────────


@register_tool(
    name="prefab_parse_refs",
    category="Asset Management",
    description=(
        "Parse a T3D prefab / actor clipboard string and return project asset "
        "package paths (excludes Engine/Fortnite mounts). MCP-friendly."
    ),
    tags=["prefab", "parse", "references", "headless", "mcp"],
)
def prefab_parse_refs(t3d_text: str = "", **kwargs) -> dict:
    if not t3d_text:
        return {"status": "error", "message": "Provide t3d_text parameter."}
    paths = _parse_t3d(t3d_text)
    return {"status": "ok", "paths": paths, "count": len(paths)}


@register_tool(
    name="prefab_resolve_deps",
    category="Asset Management",
    description=(
        "Given package paths, walk AssetRegistry dependencies and return the full "
        "closure. Set include_deps=False to return only the seed set. MCP-friendly."
    ),
    tags=["prefab", "dependency", "resolve", "headless", "mcp"],
)
def prefab_resolve_deps(packages: list = None, include_deps: bool = True, **kwargs) -> dict:
    if not packages:
        return {"status": "error", "message": "Provide packages list."}
    resolved, warnings = _resolve_deps(packages, include_deps)
    return {
        "status": "ok",
        "resolved": sorted(resolved),
        "count": len(resolved),
        "warnings": warnings,
    }


@register_tool(
    name="prefab_export_to_disk",
    category="Asset Management",
    description=(
        "Copy resolved package .uassets from this project's Content directory to a "
        "filesystem folder (other project's Content). Use dry_run=True first. MCP-friendly."
    ),
    tags=["prefab", "export", "disk", "headless", "mcp"],
)
def prefab_export_to_disk(
    packages: list = None,
    dst_content: str = "",
    flatten: bool = False,
    overwrite: bool = False,
    dry_run: bool = True,
    **kwargs,
) -> dict:
    if not packages:
        return {"status": "error", "message": "Provide packages list."}
    if not dst_content:
        return {"status": "error", "message": "Provide dst_content path."}
    src_content = unreal.Paths.project_content_dir().rstrip("/\\")
    results = _export_to_disk(
        set(packages), src_content, dst_content,
        flatten, overwrite, dry_run,
    )
    return {
        "status": "ok",
        "exported": len(results["ok"]),
        "skipped": len(results["skip"]),
        "missing": len(results["missing"]),
        "errors": results["error"],
        "dry_run": dry_run,
    }


@register_tool(
    name="prefab_export_within_project",
    category="Asset Management",
    description=(
        "Duplicate packages into dest_folder inside the current project "
        "(e.g. /YourMount/Migrated). Same as Editor duplicate; use dry_run=True first. MCP-friendly."
    ),
    tags=["prefab", "export", "duplicate", "headless", "mcp"],
)
def prefab_export_within_project(
    packages: list = None,
    dest_folder: str = "",
    flatten: bool = False,
    overwrite: bool = False,
    dry_run: bool = True,
    **kwargs,
) -> dict:
    if not packages:
        return {"status": "error", "message": "Provide packages list."}
    if not dest_folder:
        return {"status": "error", "message": "Provide dest_folder (/Mount/... path)."}
    dest_folder = dest_folder.rstrip("/")
    results = _export_within_project(
        set(packages), dest_folder, flatten, overwrite, dry_run,
    )
    return {
        "status": "ok",
        "exported": len(results["ok"]),
        "skipped": len(results["skip"]),
        "missing": len(results["missing"]),
        "errors": results["error"],
        "dry_run": dry_run,
    }
