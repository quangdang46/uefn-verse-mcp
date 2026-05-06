"""
uefn_tools — Entity Kits
========================================
"Quick-Add" macros for standard UEFN device combinations and logic sets.
Bypasses the multi-step manual placement process.
"""

from __future__ import annotations

import unreal
from ..core import log_info, log_error, log_warning, undo_transaction
from ..registry import register_tool

# ─── Kit Definitions ─────────────────────────────────────────────────────────
#
# Class paths must `unreal.load_class(None, path)` on your engine build. Several
# legacy *Creative names were renamed or removed; see CLASS_FALLBACKS below.
# Item spawner / vending / capture-area devices are often V2 Blueprint-only in
# recent UEFN — if all fallbacks fail, that kit entry is skipped (logged).

KITS = {
    "Lobby Starter": [
        {"class": "/Script/FortniteGame.FortPlayerStartCreative", "loc": (0, 0, 0), "label": "Lobby_Spawn_01"},
        {"class": "/Script/FortniteGame.FortItemSpawnerCreative", "loc": (200, 0, 0), "label": "Lobby_Weapon_Spawner"},
        {"class": "/Script/FortniteGame.FortVendingMachineCreative", "loc": (-200, 0, 0), "label": "Lobby_Vending"},
    ],
    # Paired pads — same blueprint as in-editor Creative Teleporter device (Verse `teleporter_device`).
    "Teleport Link": [
        {
            "class": "/Game/Creative/Devices/Teleporter/BP_Creative_Device_Teleporter.BP_Creative_Device_Teleporter_C",
            "loc": (0, 0, 0),
            "label": "Teleport_A",
        },
        {
            "class": "/Game/Creative/Devices/Teleporter/BP_Creative_Device_Teleporter.BP_Creative_Device_Teleporter_C",
            "loc": (1000, 0, 0),
            "label": "Teleport_B",
        },
    ],
    "Objective Hub": [
        {"class": "/Script/FortniteGame.FortCaptureAreaCreative", "loc": (0, 0, 0), "label": "Objective_Point"},
        {"class": "/Script/FortniteGame.FortCreativeTimerDevice", "loc": (0, 200, 500), "label": "Objective_Timer"},
    ],
    # Creative Button — Verse `button_device`; blueprint shipped with UEFN (see device_catalog hint Creative).
    "Button": [
        {
            "class": "/Game/Creative/Devices/Button/BP_Creative_Button.BP_Creative_Button_C",
            "loc": (0, 0, 0),
            "label": "Button_Device",
        },
    ],
    # Single Creative Teleporter — Verse `teleporter_device`; wire A/B targets in Details or use kit "Teleport Link".
    "Teleport": [
        {
            "class": "/Game/Creative/Devices/Teleporter/BP_Creative_Device_Teleporter.BP_Creative_Device_Teleporter_C",
            "loc": (0, 0, 0),
            "label": "Teleport_Device",
        },
    ],
}

# Primary kit path -> alternate paths (tried in order) when load_class fails.
CLASS_FALLBACKS: dict[str, list[str]] = {
    "/Game/Creative/Devices/Teleporter/BP_Creative_Device_Teleporter.BP_Creative_Device_Teleporter_C": [
        "/Script/FortniteGame.FortCreativeTeleporter",
    ],
    "/Script/FortniteGame.FortTeleporterCreative": [
        "/Script/FortniteGame.FortCreativeTeleporter",
    ],
    "/Script/FortniteGame.FortTimerCreative": [
        "/Script/FortniteGame.FortCreativeTimerDevice",
    ],
}

# ─────────────────────────────────────────────────────────────────────────────

def _load_uefn_class(name: str) -> unreal.Class | None:
    """Helper to find a UEFN class by name or full path."""
    if "/" in name:
        return unreal.load_class(None, name)

    # Try common Fortnite/Engine prefixes
    for prefix in ["/Script/FortniteGame.", "/Script/Engine."]:
        cls = unreal.load_class(None, f"{prefix}{name}")
        if cls:
            return cls
    return None


def _resolve_kit_actor_class(cls_spec: str) -> unreal.Class | None:
    """Load class for a kit entry: primary path, then CLASS_FALLBACKS, then fuzzy name search."""
    to_try = [cls_spec]
    to_try.extend(CLASS_FALLBACKS.get(cls_spec, []))

    for path in to_try:
        if "/" in path:
            cls = unreal.load_class(None, path)
            if cls:
                return cls

    cls_name = cls_spec.split(".")[-1] if "." in cls_spec else cls_spec
    cls = _load_uefn_class(cls_name)
    if cls:
        return cls

    # Strip Fort*/…Creative*Device* suffixes and match first unreal.Class containing term.
    search_term = cls_name
    for pfx in ("Fort", "Fortnite"):
        if search_term.startswith(pfx):
            search_term = search_term[len(pfx) :]
            break
    for sfx in ("CreativeDevice", "Creative", "Device"):
        if search_term.endswith(sfx):
            search_term = search_term[: -len(sfx)]
            break
    search_term = search_term.lower()
    for attr in dir(unreal):
        if search_term in attr.lower():
            maybe_cls = getattr(unreal, attr)
            if isinstance(maybe_cls, unreal.Class):
                return maybe_cls

    return None

@register_tool(
    name="entity_spawn_kit",
    category="Entities",
    description="Spawns a pre-configured 'Standard Kit' of devices in one click.",
    tags=["entity", "kit", "device", "quickadd", "spawn"]
)
def run_entity_spawn_kit(kit_name: str = "Lobby Starter", **kwargs) -> dict:
    """
    Spawns a named kit from the pre-defined dictionary.
    """
    if kit_name not in KITS:
        log_error(f"Kit not found: {kit_name}. Available: {list(KITS.keys())}")
        return {"status": "error", "message": f"Kit '{kit_name}' not found.", "available": list(KITS.keys())}

    kit_data = KITS[kit_name]
    
    # Get current cursor location or absolute zero
    selected = unreal.EditorLevelLibrary.get_selected_level_actors()
    base_loc = selected[0].get_actor_location() if selected else unreal.Vector(0, 0, 0)

    spawned_count = 0
    with undo_transaction(f"Spawn Entity Kit: {kit_name}"):
        for item in kit_data:
            cls_spec = item["class"]
            cls = _resolve_kit_actor_class(cls_spec)

            if not cls:
                log_warning(f"Could not load class for kit: {cls_spec}")
                continue

            loc = unreal.Vector(base_loc.x + item["loc"][0], base_loc.y + item["loc"][1], base_loc.z + item["loc"][2])
            
            actor = unreal.EditorLevelLibrary.spawn_actor_from_class(cls, loc)
            if actor:
                actor.set_actor_label(item["label"])
                spawned_count += 1

    log_info(f"✓ Successfully spawned entity kit '{kit_name}' with {spawned_count} devices.")
    return {"status": "ok", "kit": kit_name, "count": spawned_count}

@register_tool(
    name="entity_list_kits",
    category="Entities",
    description="List all available 'Standard Kits' for the quick-spawn tool.",
    tags=["list", "kit", "entity"]
)
def run_entity_list_kits(**kwargs) -> dict:
    kits = list(KITS.keys())
    for k in kits:
        log_info(f"  • {k}")
    return {"status": "ok", "count": len(kits), "kits": kits}
