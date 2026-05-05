"""
uefn_tools — Prefab Asset Migrator
========================================
Exports prefab assets (+ all dependencies) to another UEFN project cleanly.

Two workflows:
  • Export tab    — select assets in Content Browser, resolve deps, export
  • Paste Export  — paste Ctrl+C prefab T3D clipboard text, auto-parse asset
                    paths, resolve deps, export

Key features vs. Epic's built-in migration:
  • Dependency graph walk via AssetRegistry — meshes, materials, textures,
    Verse components all come along automatically
  • Flatten option — copies everything into one destination folder instead of
    recreating the entire source project folder tree
  • Cross-project copy via raw .uasset file copy (shutil) — works even when
    migrate_packages() is sandboxed in UEFN
  • Diff-aware — skips assets that already exist at the destination (dry-run
    shows what would be copied before you commit)
"""

from __future__ import annotations

import os
import re
import shutil
from typing import List, Set, Dict, Tuple

import unreal

from ..core import log_info, log_error, log_warning
from ..registry import register_tool

# ── PySide6 guard ─────────────────────────────────────────────────────────────
try:
    from PySide6.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, QHBoxLayout,
        QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget,
        QListWidgetItem, QFileDialog, QCheckBox, QTabWidget,
        QSplitter, QFrame, QScrollArea,
    )
    from PySide6.QtCore import Qt, QThread, Signal
    from PySide6.QtGui import QColor, QFont
    _PYSIDE6 = True
except ImportError:
    _PYSIDE6 = False

# ── Asset path helpers ────────────────────────────────────────────────────────

# Matches any /MountPoint/... path in T3D text (quoted or unquoted).
# Catches /Game/, /SPUNCHBROTHUS/, /MyProject/ etc.
# Engine/Script/Transient paths are filtered out in _parse_t3d.
_T3D_PATH_RE = re.compile(
    r"['\"]?(\/[A-Za-z][A-Za-z0-9_]+(?:\/[A-Za-z0-9_\-\.]+)+)['\"]?",
)

# Mounts to ignore when parsing T3D — engine/runtime paths, not user assets
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
    """'/Game/Folder/SM_Wall' → '/Game/Folder/SM_Wall.SM_Wall'"""
    name = pkg.rsplit("/", 1)[-1]
    return f"{pkg}.{name}"


def _pkg_to_disk(pkg: str, content_dir: str) -> str:
    """'/MountPoint/Folder/SM_Wall' → '<content_dir>/Folder/SM_Wall.uasset'"""
    parts = pkg.lstrip("/").split("/", 1)
    relative = parts[1] if len(parts) > 1 else parts[0]
    return os.path.join(content_dir, relative.replace("/", os.sep) + ".uasset")


def _parse_t3d(text: str) -> List[str]:
    """
    Extract all unique project asset package paths from T3D clipboard text.
    Handles /Game/... paths AND project-mount paths like /SPUNCHBROTHUS/...
    Filters out engine, script, and transient runtime paths.
    """
    seen: Set[str] = set()
    for m in _T3D_PATH_RE.finditer(text):
        raw = m.group(1)
        pkg = _normalize_pkg(raw)
        # Skip engine/runtime mounts
        if any(pkg.startswith(s) for s in _T3D_SKIP_MOUNTS):
            continue
        # Must have at least two path segments to be a real asset
        if pkg.count("/") < 2:
            continue
        if pkg not in seen:
            seen.add(pkg)
    return sorted(seen)


# ── Dependency resolver ───────────────────────────────────────────────────────

def _resolve_deps(packages: List[str], include_deps: bool = True) -> Tuple[Set[str], List[str]]:
    """
    Walk the AssetRegistry dependency graph from the seed packages.
    Returns (resolved_set, warnings_list).
    Only /Game/ packages are included — Engine/FortniteGame paths are skipped.
    """
    ar = unreal.AssetRegistryHelpers.get_asset_registry()

    dep_options = unreal.AssetRegistryDependencyOptions()
    dep_options.include_hard_package_references = True
    dep_options.include_soft_package_references = True
    dep_options.include_game_package_references = True
    dep_options.include_editor_only_package_references = False
    dep_options.include_searchable_names = False
    dep_options.include_soft_management_references = False
    dep_options.include_hard_management_references = False

    # Skip engine/plugin paths — keep /Game/ and any project mount point (e.g. /MyProject/)
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


# ── Export engines ────────────────────────────────────────────────────────────

def _export_to_disk(
    packages: Set[str],
    src_content: str,
    dst_content: str,
    flatten: bool,
    overwrite: bool,
    dry_run: bool,
) -> Dict[str, List[str]]:
    """
    Copy raw .uasset files from src_content to dst_content.
    Returns {"ok": [...], "skip": [...], "missing": [...], "error": [...]}.
    """
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
            relative = pkg[len("/Game/"):]
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
    """
    Duplicate assets within the same project to dest_folder (/Game/... path).
    """
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
            # Strip whatever mount point prefix the pkg uses (/Game/, /MyProject/, etc.)
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

    # Sync Content Browser so new folder appears immediately
    if not dry_run and results["ok"]:
        try:
            unreal.AssetRegistryHelpers.get_asset_registry().search_all_assets(True)
        except Exception:
            pass

    return results


# ── PySide6 window ────────────────────────────────────────────────────────────

if _PYSIDE6:
    try:
    except Exception:
        _DASH_QSS = ""

    try:
    except Exception:

    _LABEL_CSS  = "color:#AAAAAA; font-size:9pt;"
    _MUTED_CSS  = "color:#666666; font-size:8pt;"
    _INPUT_CSS  = (
        "background:#1A1A1A; color:#E0E0E0; border:1px solid #3A3A3A;"
        "border-radius:3px; padding:4px 6px; font-size:9pt;"
    )
    _BTN_CSS    = (
        "QPushButton{background:#252525; color:#E0E0E0; border:1px solid #3A3A3A;"
        "border-radius:3px; padding:4px 10px; font-size:9pt;}"
        "QPushButton:hover{background:#2E2E2E; border-color:#555;}"
        "QPushButton:pressed{background:#1A1A1A;}"
    )
    _ACCENT_CSS = (
        "QPushButton{background:#2A6099; color:#FFFFFF; border:1px solid #3A8FC7;"
        "border-radius:3px; padding:4px 10px; font-size:9pt; font-weight:600;}"
        "QPushButton:hover{background:#3A8FC7;}"
        "QPushButton:pressed{background:#1A4A70;}"
        "QPushButton:disabled{background:#1A1A1A; color:#555; border-color:#2A2A2A;}"
    )
    _LIST_CSS   = (
        "QListWidget{background:#141414; color:#CCCCCC; border:1px solid #2A2A2A;"
        "border-radius:3px; font-family:Consolas; font-size:8pt;}"
        "QListWidget::item:selected{background:#1E3A5F; color:#FFFFFF;}"
        "QListWidget::item:hover{background:#1A1A1A;}"
    )
    _LOG_CSS    = (
        "background:#0E0E0E; color:#AAAAAA; border:1px solid #2A2A2A;"
        "border-radius:3px; font-family:Consolas; font-size:8pt; padding:4px;"
    )

    def _div() -> QFrame:
        f = QFrame()
        f.setFrameShape(QFrame.HLine)
        f.setStyleSheet("color:#2A2A2A;")
        return f

    def _lbl(text: str, muted: bool = False) -> QLabel:
        w = QLabel(text)
        w.setStyleSheet(_MUTED_CSS if muted else _LABEL_CSS)
        return w

    def _btn(text: str, accent: bool = False) -> QPushButton:
        b = QPushButton(text)
        b.setStyleSheet(_ACCENT_CSS if accent else _BTN_CSS)
        b.setCursor(Qt.PointingHandCursor)
        return b

    def _inp(placeholder: str = "", fixed_width: int = 0) -> QLineEdit:
        w = QLineEdit()
        w.setPlaceholderText(placeholder)
        w.setStyleSheet(_INPUT_CSS)
        w.setFixedHeight(28)
        if fixed_width:
            w.setFixedWidth(fixed_width)
        return w

    # ── Worker thread ──────────────────────────────────────────────────────

    class _ExportWorker(QThread):
        progress = Signal(str)   # log line
        finished = Signal(dict)  # results dict

        def __init__(self, packages, src_content, dst_content,
                     dest_game_folder, flatten, overwrite, dry_run,
                     cross_project):
            super().__init__()
            self._packages       = packages
            self._src_content    = src_content
            self._dst_content    = dst_content
            self._dest_folder    = dest_game_folder
            self._flatten        = flatten
            self._overwrite      = overwrite
            self._dry_run        = dry_run
            self._cross_project  = cross_project

        def run(self):
            if self._cross_project:
                r = _export_to_disk(
                    self._packages, self._src_content, self._dst_content,
                    self._flatten, self._overwrite, self._dry_run,
                )
            else:
                r = _export_within_project(
                    self._packages, self._dest_folder,
                    self._flatten, self._overwrite, self._dry_run,
                )
            self.finished.emit(r)

    # ── Shared path-row widget ─────────────────────────────────────────────

    class _PathRow(QWidget):
        def __init__(self, label: str, placeholder: str,
                     browse_dir: bool = True, parent=None):
            super().__init__(parent)
            lay = QHBoxLayout(self)
            lay.setContentsMargins(0, 0, 0, 0)
            lay.setSpacing(6)
            lay.addWidget(_lbl(label))
            self.edit = _inp(placeholder)
            lay.addWidget(self.edit, 1)
            self._browse_dir = browse_dir
            btn = _btn("…")
            btn.setFixedWidth(32)
            btn.clicked.connect(self._browse)
            lay.addWidget(btn)

        def _browse(self):
            if self._browse_dir:
                path = QFileDialog.getExistingDirectory(self, "Select Folder")
            else:
                path, _ = QFileDialog.getOpenFileName(self, "Select File")
            if path:
                self.edit.setText(path)

        @property
        def text(self) -> str:
            return self.edit.text().strip()

    # ── Help dialog ───────────────────────────────────────────────────────────

WHAT IS THIS?

The Prefab Asset Migrator copies assets — and all of their dependencies — from
your project to a new destination in one click. Where UEFN's built-in migration
can silently drop meshes, materials, or textures, this tool walks the full
dependency graph via the Asset Registry so every referenced asset comes along.

─────────────────────────────────────────────────────────────────────────

WHY IT WAS MADE

Working with prefabs across UEFN projects is painful. Copy-pasting actors between
projects leaves them broken because the assets they reference don't transfer.
Epic's migrate tool works but can drag in unwanted parent folders and gives no
dry-run preview. This tool was built to solve both problems cleanly.

─────────────────────────────────────────────────────────────────────────

TWO WORKFLOWS

  EXPORT TAB — start from the Content Browser
    1. Select assets in the UEFN Content Browser
    2. Click  + Add Selected from CB  — paths appear in the list
       (or select actors in the viewport → + Add Selected from Viewport
        to extract asset paths directly from placed actors using your assets)
    3. Click  Resolve Dependencies  — the full dependency closure is shown
       below. Review what will be copied before committing.
    4. Set the destination:
         Same-project copy  →  /YourProject/SomeFolder/
           Assets appear in your Content Browser under that folder.
         Cross-project copy  →  C:/OtherProject/Content
           Raw .uasset files are copied to disk — open the other project
           and the assets will appear on next load.
    5. Check  Dry run  first to preview exactly what would be copied.
    6. Uncheck  Dry run  and click  Export.

  PASTE EXPORT TAB — start from the viewport clipboard
    1. In the UEFN viewport, select actors and press  Ctrl+C
    2. Switch to the Paste Export tab and paste the clipboard text
    3. Click  Parse References  — asset paths are extracted from the T3D data
    4. Click  Resolve Dependencies, then  Export  as above

─────────────────────────────────────────────────────────────────────────

OPTIONS

  Include dependencies  (default ON)
      Walk the Asset Registry dep graph from each seed asset.
      Meshes pull in materials. Materials pull in textures.
      Turn OFF only to copy a single asset with no deps.

  Flatten folder structure
      Copies everything into one flat destination folder instead of
      recreating the source subfolder tree. Useful when you want a
      clean drop-in without nested paths.

  Overwrite existing
      By default, existing assets at the destination are skipped.
      Turn ON to replace them.

  Dry run
      Simulates the entire export and prints the result log without
      writing anything. Always run this first on large exports.

─────────────────────────────────────────────────────────────────────────

DESTINATION PATHS

  /YourProject/Migrated/       same-project copy — visible in Content Browser
  C:/Projects/Other/Content    cross-project disk copy — raw .uasset files

  The destination auto-fills from your project's mount point the first time
  you add an asset from the Content Browser.

  NOTE: In UEFN, /Game/ is an internal mount NOT visible in the Content
  Browser. Always use your project's named mount (e.g. /Device_API_Mapping/)
  for same-project copies. See UEFN_QUIRKS.md Quirk #23.

─────────────────────────────────────────────────────────────────────────

WHAT IT DOES NOT MIGRATE

  Verse source files (.verse) — not tracked by the Asset Registry.
    Copy them manually from your project's Verse source directory.

  Fortnite / Engine built-ins — already exist in every project.

  Level or World Partition data — export the level file itself for that.
"""

        def __init__(self) -> None:
            super().__init__(title="UEFN uefn_tools — Prefab Asset Migrator Help",
                             width=700, height=760)
            self._build_ui()

        def _build_ui(self) -> None:
            root = QWidget()
            self.setCentralWidget(root)
            vl = QVBoxLayout(root)
            vl.setContentsMargins(0, 0, 0, 0)
            vl.setSpacing(0)
            editor = QTextEdit()
            editor.setReadOnly(True)
            editor.setPlainText(self._CONTENT)
            editor.setFont(QFont("Consolas", 9))
            editor.setLineWrapMode(QTextEdit.NoWrap)
            editor.setStyleSheet(
                f"background:{self.hex('panel')}; color:{self.hex('text')};"
                f"border:none; padding:16px;"
            )
            vl.addWidget(editor)

    # ── Main window ────────────────────────────────────────────────────────

# ── Registered tools ──────────────────────────────────────────────────────────

@register_tool(
    name="prefab_migrate_open",
    category="Asset Management",
    description=(
        "Open the Prefab Asset Migrator — paste Ctrl+C prefab T3D text to "
        "auto-extract all asset references, resolve the full dependency closure "
        "(meshes, materials, textures, Verse components), and export cleanly to "
        "another project with optional folder flattening."
    ),
    tags=["prefab", "migrate", "export", "dependency", "asset", "copy"],
)
def prefab_migrate_open(**kwargs) -> dict:
    if not _PYSIDE6:
        return {"status": "error", "message": "PySide6 not installed."}
    try:
        win = _PrefabMigratorWindow()
        win.show_in_uefn()
        return {"status": "ok", "message": "Prefab Asset Migrator opened."}
    except Exception as exc:
        log_error(f"prefab_migrate_open: {exc}")
        return {"status": "error", "message": str(exc)}


@register_tool(
    name="prefab_parse_refs",
    category="Asset Management",
    description=(
        "Headless: parse a T3D prefab text string and return all /Game/ asset "
        "package paths found. No UI — MCP/script friendly."
    ),
    tags=["prefab", "parse", "references", "headless"],
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
        "Headless: given a list of /Game/ package paths, walk the AssetRegistry "
        "dependency graph and return the full closure of all required assets. "
        "MCP/script friendly."
    ),
    tags=["prefab", "dependency", "resolve", "headless"],
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
        "Headless: copy resolved .uasset files from this project's Content folder "
        "to a destination disk directory. Set dry_run=True to preview without "
        "copying. MCP/script friendly."
    ),
    tags=["prefab", "export", "disk", "headless"],
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
        "exported":  len(results["ok"]),
        "skipped":   len(results["skip"]),
        "missing":   len(results["missing"]),
        "errors":    results["error"],
        "dry_run":   dry_run,
    }
