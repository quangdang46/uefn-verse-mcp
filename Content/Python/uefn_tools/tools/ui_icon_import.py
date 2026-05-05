"""
uefn_tools — UI Icon Importer (headless / MCP)
===============================================
Imports images as Texture2D assets and applies UI-friendly compression / mips /
LOD group presets. No editor window — use from MCP or REPL.

Tools:
  • ui_icon_import_open     Import from Windows clipboard (same as before, no UI).
  • ui_icon_import_file     Import from a filesystem image path.

For URL downloads use: import_image_from_url (asset_importer).
"""

from __future__ import annotations

import os
import tempfile

import unreal

from ..core import log_error, log_info, get_config, detect_project_mount
from ..core.safety_gate import SafetyGate
from ..registry import register_tool

from . import asset_importer as _ai

# ── Texture presets (applied after engine import) ─────────────────────────────
_PRESETS: dict[str, dict] = {
    "UI Icon  (TC_UserInterface2D · no mips · sRGB)": {
        "compression": "TC_USER_INTERFACE2D",
        "mip_gen":     "TMGS_NO_MIPMAPS",
        "srgb":        True,
        "lod_group":   "TEXTUREGROUP_UI",
    },
    "Sprite / 2D  (TC_BC7 · no mips · sRGB)": {
        "compression": "TC_BC7",
        "mip_gen":     "TMGS_NO_MIPMAPS",
        "srgb":        True,
        "lod_group":   "TEXTUREGROUP_UI",
    },
    "Thumbnail  (TC_BC7 · no mips · sRGB)": {
        "compression": "TC_BC7",
        "mip_gen":     "TMGS_NO_MIPMAPS",
        "srgb":        True,
        "lod_group":   "TEXTUREGROUP_UI",
    },
    "Normal Map  (TC_Normalmap · no mips · linear)": {
        "compression": "TC_NORMALMAP",
        "mip_gen":     "TMGS_NO_MIPMAPS",
        "srgb":        False,
        "lod_group":   "TEXTUREGROUP_WORLD",
    },
    "Default / Mipmapped  (TC_BC7 · standard mips)": {
        "compression": "TC_BC7",
        "mip_gen":     "TMGS_FROM_TEXTURE_GROUP",
        "srgb":        True,
        "lod_group":   "TEXTUREGROUP_WORLD",
    },
}


def _default_asset_dir() -> str:
    cfg = get_config().get("import.default_dir")
    if cfg:
        return str(cfg)
    mount = detect_project_mount()
    return f"/{mount}/UI/Icons" if mount else "/Game/UI/Icons"


def _pick_preset(preset: str = "") -> dict:
    q = (preset or "").strip().lower()
    if q:
        for label, cfg in _PRESETS.items():
            if q in label.lower():
                return cfg
    return next(iter(_PRESETS.values()))


def _apply_texture_settings(pkg_path: str, preset: dict) -> None:
    try:
        tex = unreal.EditorAssetLibrary.load_asset(pkg_path)
        if not tex:
            return

        comp = getattr(
            unreal.TextureCompressionSettings,
            preset["compression"],
            unreal.TextureCompressionSettings.TC_DEFAULT,
        )
        tex.set_editor_property("compression_settings", comp)

        mip = getattr(
            unreal.TextureMipGenSettings,
            preset["mip_gen"],
            unreal.TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP,
        )
        tex.set_editor_property("mip_gen_settings", mip)

        tex.set_editor_property("srgb", preset["srgb"])

        lod = getattr(
            unreal.TextureGroup,
            preset["lod_group"],
            unreal.TextureGroup.TEXTUREGROUP_UI,
        )
        tex.set_editor_property("lod_group", lod)

        tex.post_edit_change()
        unreal.EditorAssetLibrary.save_asset(pkg_path)
    except Exception as exc:
        log_error(f"[UI ICON] Could not apply texture settings to {pkg_path}: {exc}")


def _import_with_preset(
    source_file: str,
    asset_dir: str,
    asset_name: str,
    preset: str,
) -> dict:
    if not os.path.isfile(source_file):
        return {"status": "error", "message": f"Source file not found: {source_file}"}

    if not asset_dir:
        asset_dir = _default_asset_dir()

    SafetyGate.enforce_safety(asset_dir)

    clean = _ai._sanitize_asset_name(asset_name) or _ai._next_sequential_name(asset_dir)
    result_path = _ai._import_file_task(source_file, asset_dir, clean)
    if not result_path:
        return {"status": "error", "message": "Engine import failed."}

    _apply_texture_settings(result_path, _pick_preset(preset))
    log_info(f"[UI ICON] Imported with preset: {result_path}")
    return {"status": "ok", "asset_path": result_path, "preset": preset or "default"}


@register_tool(
    name="ui_icon_import_open",
    category="Asset Management",
    description=(
        "Import the current Windows clipboard image as a Texture2D under asset_dir "
        "(default: project mount /UI/Icons), then apply a UI preset. "
        "Optional preset substring matches _PRESETS keys (e.g. 'UI Icon', 'Normal Map'). "
        "No PySide window — MCP/REPL only."
    ),
    tags=["ui", "icon", "texture", "import", "clipboard", "paste", "image", "mcp"],
)
def ui_icon_import_open(
    asset_dir: str = "",
    asset_name: str = "",
    preset: str = "",
    **kwargs,
) -> dict:
    if not asset_dir:
        asset_dir = _default_asset_dir()

    SafetyGate.enforce_safety(asset_dir)

    clean = _ai._sanitize_asset_name(asset_name) or _ai._next_sequential_name(asset_dir)
    tmp_path = os.path.join(tempfile.gettempdir(), f"uefntoolbelt_ui_clip_{clean}.png")

    if not _ai._extract_clipboard_png(tmp_path):
        return {"status": "error", "message": "Clipboard extraction failed (no image or unsupported)."}

    return _import_with_preset(tmp_path, asset_dir, clean, preset)


@register_tool(
    name="ui_icon_import_file",
    category="Asset Management",
    description=(
        "Import a local image file (.png, .jpg, etc.) as Texture2D and apply a UI preset. "
        "Same preset matching rules as ui_icon_import_open."
    ),
    tags=["ui", "icon", "texture", "import", "file", "mcp"],
)
def ui_icon_import_file(
    file_path: str = "",
    asset_dir: str = "",
    asset_name: str = "",
    preset: str = "",
    **kwargs,
) -> dict:
    if not file_path.strip():
        return {"status": "error", "message": "Provide file_path."}
    base = os.path.basename(file_path)
    stem = os.path.splitext(base)[0]
    if not asset_name:
        asset_name = stem
    return _import_with_preset(os.path.abspath(file_path), asset_dir, asset_name, preset)
