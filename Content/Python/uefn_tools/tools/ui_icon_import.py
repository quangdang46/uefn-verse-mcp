"""
uefn_tools — UI Icon Importer
========================================
Clipboard-first image importer for UEFN UI/icon textures.

Copy any image (from a browser, Figma, Photoshop, Paint) and paste it
directly into the window — it imports with the correct Mip/compression
settings for UI work in one click. No Photoshop export step, no manual
texture settings panel.

Three ways to feed an image:
  1. Ctrl+V  — paste from clipboard
  2. Click   — open file browser
  3. Drag    — drop an image file onto the zone

Presets cover the most common UEFN UI needs:
  • UI Icon (default)  — TC_UserInterface2D · NoMipmaps · sRGB · TextureGroup_UI
  • Sprite / 2D        — TC_BC7 · NoMipmaps · sRGB · TextureGroup_UI
  • Thumbnail          — TC_BC7 · NoMipmaps · sRGB · TextureGroup_UI
  • Normal Map         — TC_Normalmap · NoMipmaps · no sRGB · TextureGroup_World
  • Default / Mipmapped — TC_BC7 · standard mip chain · TextureGroup_World

Registered tools:
  ui_icon_import_open   Open the import window
"""

from __future__ import annotations

import os
import tempfile

import unreal

from ..core import log_info, log_warning, log_error, detect_project_mount
from ..registry import register_tool

# ── PySide6 guard ─────────────────────────────────────────────────────────────
_PYSIDE6 = False
try:
    from PySide6.QtWidgets import (
        QApplication, QVBoxLayout, QHBoxLayout,
        QLabel, QLineEdit, QComboBox, QFrame,
        QFileDialog, QSizePolicy, QTextEdit,
    )
    from PySide6.QtGui import QPixmap, QImage, QDragEnterEvent, QDropEvent
    from PySide6.QtCore import Qt
    _PYSIDE6 = True
except ImportError:
    pass


# ── Texture presets ───────────────────────────────────────────────────────────
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

# ── Helpers ───────────────────────────────────────────────────────────────────


def _apply_texture_settings(pkg_path: str, preset: dict) -> None:
    """Apply Mip/compression/LOD settings to an already-imported texture."""
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
    except Exception as e:
        log_warning(f"[UI ICON] Could not apply texture settings to {pkg_path}: {e}")


# ── PySide6 classes ───────────────────────────────────────────────────────────

if _PYSIDE6:

    # ── Help dialog ───────────────────────────────────────────────────────────

UI ICON IMPORTER — Quick Reference
══════════════════════════════════════════════════════════════════════

WHAT IT DOES
  Imports any image into your UEFN project with the correct Mip and
  compression settings for UI textures — in one step.
  No Photoshop export. No texture settings panel. Just paste and import.

THREE WAYS TO LOAD AN IMAGE
  1. Ctrl+V  — copy an image in your browser, Figma, Photoshop, or
               Paint, then press Ctrl+V inside this window.
  2. Click   — click the drop zone to open a file browser (.png, .jpg,
               .tga, .bmp).
  3. Drag    — drag any image file directly onto the drop zone.

PRESETS
  UI Icon (default)
    → TC_UserInterface2D · NoMipmaps · sRGB · TextureGroup UI
    → Best for HUD icons, button art, inventory images, crosshairs.

  Sprite / 2D
    → TC_BC7 · NoMipmaps · sRGB · TextureGroup UI
    → Best for 2D game sprites or flat cutout textures.

  Thumbnail
    → TC_BC7 · NoMipmaps · sRGB · TextureGroup UI
    → Best for preview images, map art, loading screens.

  Normal Map
    → TC_Normalmap · NoMipmaps · linear (no sRGB) · TextureGroup World
    → Best for tangent-space normal maps.

  Default / Mipmapped
    → TC_BC7 · standard mip chain · TextureGroup World
    → Best for in-world textures that need LOD mipmapping.

DESTINATION
  Defaults to /[ProjectMount]/UI/Icons/ where [ProjectMount] is
  auto-detected from your Content Browser on open.
  You can type any valid Content Browser path.
  The folder is created automatically if it does not exist.

FILENAME
  Auto-filled from the source file name, or T_Paste_001 for clipboard
  pastes. The T_ prefix follows Epic naming conventions.
  Edit this field before importing to rename the asset.

WHY NO MIPMAPS FOR UI?
  UI textures are always displayed at a fixed pixel size — mipmaps waste
  memory and can cause blurry renders at certain resolutions.
  TC_UserInterface2D also preserves the full alpha channel correctly,
  which BC7/DXT5 may not in all cases.

TIPS
  • Transparent PNGs keep their alpha — use UI Icon preset.
  • For web images: right-click → Copy Image → Ctrl+V in this window.
  • The imported asset is auto-selected in the Content Browser so you
    can drag it onto a Widget Blueprint immediately.
  • Supports PNG, JPG, TGA, BMP.
"""

        def __init__(self, parent=None):
            super().__init__(title="UEFN uefn_tools — UI Icon Importer Help", width=580, height=580, parent=parent)
            self._build_ui()

        def _build_ui(self):
            central = QFrame()
            self.setCentralWidget(central)
            vl = QVBoxLayout(central)
            vl.setContentsMargins(14, 14, 14, 14)
            vl.setSpacing(8)

            editor = QTextEdit()
            editor.setReadOnly(True)
            editor.setLineWrapMode(QTextEdit.NoWrap)
            editor.setPlainText(self._HELP)
            editor.setStyleSheet(
                f"background:{self.hex('panel')}; color:{self.hex('text')}; "
                f"font-family:Consolas; font-size:9pt; "
                f"border:1px solid {self.hex('border')}; padding:8px;"
            )
            vl.addWidget(editor)

            close_row = QHBoxLayout()
            close_row.addStretch()
            close_row.addWidget(self.make_btn("Close", cb=self.close))
            vl.addLayout(close_row)

    # ── Drop Zone ─────────────────────────────────────────────────────────────

    class _DropZone(QLabel):
        """Paste / drag-and-drop target that accepts images and image files."""

        def __init__(self, palette: dict, parent=None):
            super().__init__(parent)
            self._P = palette
            self._has_image = False
            self.setAcceptDrops(True)
            self.setAlignment(Qt.AlignCenter)
            self.setMinimumHeight(180)
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.setScaledContents(False)
            self._show_empty()

        def _show_empty(self):
            self._has_image = False
            self.clear()
            self.setText("Click to browse  ·  Ctrl+V to paste  ·  or drop an image here")
            self.setStyleSheet(
                f"background:{self._P['panel']}; color:{self._P['muted']}; "
                f"border:2px dashed {self._P['border2']}; border-radius:6px; "
                f"font-size:11pt; padding:24px;"
            )

        def _show_image(self, img: QImage):
            self._has_image = True
            pm = QPixmap.fromImage(img)
            # Scale to fit, leaving a margin
            maxw = max(self.width() - 32, 200)
            maxh = max(self.height() - 32, 160)
            pm = pm.scaled(maxw, maxh, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(pm)
            self.setStyleSheet(
                f"background:{self._P['bg']}; "
                f"border:2px solid {self._P['accent']}; "
                f"border-radius:6px; padding:8px;"
            )

        def load_image(self, img: QImage):
            if not img.isNull():
                self._show_image(img)

        def clear_zone(self):
            self._show_empty()

        # Drag-and-drop
        def dragEnterEvent(self, event: QDragEnterEvent):
            md = event.mimeData()
            if md.hasUrls() or md.hasImage():
                event.acceptProposedAction()
                self.setStyleSheet(
                    f"background:{self._P['panel']}; color:{self._P['text']}; "
                    f"border:2px dashed {self._P['accent']}; border-radius:6px; "
                    f"font-size:11pt; padding:24px;"
                )
            else:
                event.ignore()

        def dragLeaveEvent(self, event):
            if not self._has_image:
                self._show_empty()

        def dropEvent(self, event: QDropEvent) -> tuple[QImage | None, str]:
            """Emits via _on_drop callback set by parent."""
            md = event.mimeData()
            if md.hasUrls():
                for url in md.urls():
                    local = url.toLocalFile()
                    if local and os.path.isfile(local):
                        img = QImage(local)
                        if not img.isNull():
                            self._on_drop(img, local)
                            return
            if md.hasImage():
                img = QImage(md.imageData())
                if not img.isNull():
                    self._on_drop(img, "")

        def set_drop_handler(self, fn):
            self._on_drop = fn

    # ── Main window ───────────────────────────────────────────────────────────

# ── Registered tool ───────────────────────────────────────────────────────────

@register_tool(
    name="ui_icon_import_open",
    category="Asset Management",
    description=(
        "Open the UI Icon Importer — paste any image from the clipboard "
        "(browser, Figma, Photoshop) and import it as a UEFN texture with "
        "correct Mip/compression settings. Supports file browse and drag-drop. "
        "No Photoshop export step required."
    ),
    tags=["ui", "icon", "texture", "import", "clipboard", "paste", "image", "mip", "sprite"],
)
def ui_icon_import_open(**kwargs) -> dict:
    """
    Open the clipboard-first UI icon importer.
    Paste from browser, Figma, or Photoshop → imports with correct UEFN UI texture settings.
    """
    if not _PYSIDE6:
        return {"status": "error", "message": "PySide6 is not installed."}
    win = _UIIconImportWindow()
    win.show_in_uefn()
    return {"status": "ok", "message": "UI Icon Importer opened."}
