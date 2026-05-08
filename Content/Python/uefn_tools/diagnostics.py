import unreal
import json
from .registry import register_tool

@register_tool(
    name="debug_dump_verse_actor",
    category="Utilities",
    description="Dump all internal properties of a selected Verse actor for discovery.",
    tags=["debug", "verse", "discovery"],
)
def dump_actor_info(**kwargs) -> dict:
    sel = unreal.EditorLevelLibrary.get_selected_level_actors()
    if not sel:
        unreal.log_warning("[DIAGNOSTIC] No actor selected.")
        return {"status": "error", "message": "No actor selected."}
        
    actor = sel[0]
    unreal.log(f"[DIAGNOSTIC] Actor Label: {actor.get_actor_label()}")
    unreal.log(f"[DIAGNOSTIC] Actor Full Name: {actor.get_full_name()}")
    unreal.log(f"[DIAGNOSTIC] Class Name: {actor.get_class().get_name()}")
    unreal.log(f"[DIAGNOSTIC] Class Path: {actor.get_class().get_path_name()}")
    
    # 1. Inspect Class Hierarchy
    unreal.log("[DIAGNOSTIC] Class Hierarchy:")
    try:
        curr_cls = actor.get_class()
        while curr_cls:
            unreal.log(f"  <- {curr_cls.get_name()} ({curr_cls.get_path_name()})")
            # In Unreal Python, it is get_super_class()
            if hasattr(curr_cls, "get_super_class"):
                curr_cls = curr_cls.get_super_class()
            else:
                break
    except Exception as e:
        unreal.log_warning(f"  Class hierarchy inspection failed: {e}")

    # 2. Inspect Components
    unreal.log("[DIAGNOSTIC] Inspecting Components...")
    try:
        # Get all components using the standard Unreal method
        components = actor.get_components_by_class(unreal.ActorComponent)
        for comp in components:
            unreal.log(f"  • Component: {comp.get_name()} (Class: {comp.get_class().get_name()})")
            # If it's a Verse-related component, dump its properties
            if "verse" in comp.get_class().get_name().lower():
                unreal.log(f"    - Full Path: {comp.get_class().get_path_name()}")
    except Exception as e:
        unreal.log_warning(f"  Failed to get components: {e}")

    # 3. Aggressive property dump (all strings)
    unreal.log("[DIAGNOSTIC] Aggressive String Search in Properties...")
    # Safe alternative to inspect.getmembers on Unreal objects
    for name in dir(actor):
        if name.startswith("__") or name.startswith("get_") or name.startswith("set_"):
            continue
        try:
            value = getattr(actor, name)
            s_val = str(value)
            # If the name or value contains "hello" or "verse", highlight it
            if "hello" in name.lower() or "hello" in s_val.lower() or "verse" in name.lower() or "verse" in s_val.lower():
                unreal.log(f"  [MATCH] {name}: {s_val}")
        except Exception:
            pass

    # 4. Check specific internal Verse fields
    unreal.log("[DIAGNOSTIC] Checking known Verse-internal fields...")
    try:
        # These are often used in UEFN 5.1+
        if hasattr(actor, "ScriptClass"):
             unreal.log(f"  • ScriptClass: {actor.ScriptClass}")
        if hasattr(actor, "VerseClass"):
             unreal.log(f"  • VerseClass: {actor.VerseClass}")
    except Exception:
        pass

    unreal.log("[DIAGNOSTIC] Dump Complete.")
    return {"status": "ok", "actor": actor.get_actor_label()}

@register_tool(
    name="debug_audit_verse_assets",
    category="Utilities",
    description="Search the project asset registry for all Verse-generated Blueprints.",
    tags=["debug", "verse", "audit"],
)
def audit_verse_assets(**kwargs) -> dict:
    ar = unreal.AssetRegistryHelpers.get_asset_registry()
    unreal.log("[ASSET AUDIT] Searching for Verse-related assets...")
    
    # Search for anything in the project content
    filter = unreal.ARFilter(package_paths=["/TOOL_TEST"], recursive_paths=True)
    assets = ar.get_assets(filter)
    
    found = False
    for asset in assets:
        name = str(asset.asset_name)
        # Class path is now a TopLevelAssetPath in 5.1+
        cls = str(asset.asset_class_path.asset_name)
        if "hello" in name.lower() or "verse" in name.lower() or "device" in name.lower():
            # Skip the base VerseDevice class
            if name == "VerseDevice" or name == "CreativeDevice":
                continue
            unreal.log(f"  • Asset: {name} (Class: {cls})")
            unreal.log(f"    - Path: {asset.package_name}")
            found = True
            
    if not found:
        unreal.log_warning("[ASSET AUDIT] No student Verse assets found in /TOOL_TEST. Ensure Verse is compiled.")
    
    return {"status": "ok", "found": found}


# ── Batch invoke (smoke / audit): calls each tool with {} once ─────────────────

_HARD_SKIP = frozenset({
    "shutdown",
    "mcp_stop",
    "mcp_restart",
    "toolbelt_integration_test",
})

_SAFE_EXTRA_SKIP = frozenset({
    "smoke_test",
    "registry_invoke_all_tools",
})


def _tool_meta_invasive(meta: dict) -> bool:
    tags = meta.get("tags") or []
    desc = (meta.get("description") or "").upper()
    if "INVASIVE" in desc or "WARNING:" in desc:
        return True
    return any("invasive" in str(t).lower() for t in tags)


@register_tool(
    name="registry_invoke_all_tools",
    category="Utilities",
    description=(
        "Invoke every registered tool once with empty kwargs ({}). "
        "Always skips MCP-breaking tools (shutdown/mcp_stop/mcp_restart) and "
        "toolbelt_integration_test. mode='safe' also skips smoke_test, this tool, "
        "and any tool whose manifest tags/description mark it invasive. "
        "Writes Saved/uefn_tools/registry_invoke_all_report.json (after last chunk). "
        "Use chunk_index + chunk_total (e.g. 20 chunks) so each HTTP/MCP call stays under timeouts. "
        "Expect many type_errors (tools needing arguments) and level edits in 'full' mode."
    ),
    tags=["registry", "batch", "smoke", "audit", "invoke"],
    example='tb.run("registry_invoke_all_tools", mode="safe")',
)
def registry_invoke_all_tools(
    mode: str = "safe",
    chunk_index: int = 0,
    chunk_total: int = 1,
    **kwargs,
) -> dict:
    import json
    import os
    import traceback

    from .registry import get_registry

    mode_n = (mode or "safe").strip().lower()
    if mode_n not in ("safe", "full"):
        return {"status": "error", "message": "mode must be 'safe' or 'full'."}
    if chunk_total < 1:
        return {"status": "error", "message": "chunk_total must be >= 1."}
    if chunk_index < 0 or chunk_index >= chunk_total:
        return {"status": "error", "message": f"chunk_index must be in [0, {chunk_total - 1}]."}

    reg = get_registry()
    manifest = reg.to_manifest()

    to_invoke: list[str] = []
    skip_hard: list[str] = []
    skip_safe: list[str] = []

    for name in sorted(manifest.keys()):
        if name in _HARD_SKIP:
            skip_hard.append(name)
            continue
        meta = manifest[name]
        if mode_n == "safe":
            if name in _SAFE_EXTRA_SKIP or _tool_meta_invasive(meta):
                skip_safe.append(name)
                continue
        to_invoke.append(name)

    n = len(to_invoke)
    size = (n + chunk_total - 1) // chunk_total
    start = chunk_index * size
    end = min(start + size, n)
    batch = to_invoke[start:end]

    out_dir = os.path.join(unreal.Paths.project_saved_dir(), "uefn_tools")
    os.makedirs(out_dir, exist_ok=True)
    state_path = os.path.join(out_dir, "registry_invoke_all_state.json")
    report_path = os.path.join(out_dir, "registry_invoke_all_report.json")

    ok: list[str] = []
    type_errors: list[dict] = []
    errors: list[dict] = []

    if chunk_index == 0:
        state = {
            "mode": mode_n,
            "chunk_total": chunk_total,
            "skip_hard": skip_hard,
            "skip_safe": skip_safe,
            "to_invoke_total": n,
            "ok": [],
            "type_errors": [],
            "errors": [],
            "chunks_completed": [],
        }
    else:
        if not os.path.isfile(state_path):
            return {
                "status": "error",
                "message": "Missing registry_invoke_all_state.json — run chunk_index=0 first with same mode/chunk_total.",
            }
        try:
            with open(state_path, "r", encoding="utf-8") as sf:
                state = json.load(sf)
        except Exception as ex:
            return {"status": "error", "message": f"Cannot read state file: {ex}"}
        if state.get("mode") != mode_n or int(state.get("chunk_total", -1)) != int(chunk_total):
            return {
                "status": "error",
                "message": (
                    "State mismatch (mode or chunk_total). Delete "
                    "Saved/uefn_tools/registry_invoke_all_state.json and restart from chunk 0."
                ),
            }

    already_done = chunk_index in state["chunks_completed"]
    if not already_done:
        for name in batch:
            entry = reg._tools[name]
            try:
                entry.fn(**{})
                ok.append(name)
            except TypeError as e:
                msg = str(e)
                type_errors.append({"name": name, "error": msg[:400]})
            except Exception as e:
                errors.append({
                    "name": name,
                    "error": str(e)[:500],
                    "traceback": traceback.format_exc()[-1200:],
                })
        state["ok"].extend(ok)
        state["type_errors"].extend(type_errors)
        state["errors"].extend(errors)
        state["chunks_completed"].append(chunk_index)

    done_ct = len(state["chunks_completed"])
    merged_skip_hard = state.get("skip_hard") or skip_hard
    merged_skip_safe = state.get("skip_safe") or skip_safe

    with open(state_path, "w", encoding="utf-8") as sf:
        json.dump(state, sf, indent=2)

    if done_ct >= chunk_total:
        payload = {
            "mode": mode_n,
            "totals": {
                "registered": len(manifest),
                "skip_hard": len(merged_skip_hard),
                "skip_safe": len(merged_skip_safe),
                "invoked_slots": state.get("to_invoke_total", n),
                "ok": len(state["ok"]),
                "type_errors": len(state["type_errors"]),
                "errors": len(state["errors"]),
            },
            "skip_hard": merged_skip_hard,
            "skip_safe": merged_skip_safe,
            "ok": state["ok"],
            "type_errors": state["type_errors"],
            "errors": state["errors"],
        }
        with open(report_path, "w", encoding="utf-8") as rf:
            json.dump(payload, rf, indent=2)
        try:
            os.remove(state_path)
        except Exception:
            pass

        unreal.log(
            f"[registry_invoke_all_tools] FINAL mode={mode_n} "
            f"ok={len(state['ok'])} type_errors={len(state['type_errors'])} "
            f"errors={len(state['errors'])} report={report_path}"
        )

        return {
            "status": "ok",
            "phase": "complete",
            "mode": mode_n,
            "report_path": report_path,
            "chunk_index": chunk_index,
            "chunk_total": chunk_total,
            **payload["totals"],
        }

    unreal.log(
        f"[registry_invoke_all_tools] chunk {chunk_index + 1}/{chunk_total} "
        f"batch={start}-{end} ok_chunk={len(ok)} "
        f"cumulative_ok={len(state['ok'])} state={state_path}"
    )

    return {
        "status": "ok",
        "phase": "chunk",
        "mode": mode_n,
        "chunk_index": chunk_index,
        "chunk_total": chunk_total,
        "batch_range": [start, end],
        "chunk_tools": len(batch),
        "chunk_ok": len(ok),
        "chunk_type_errors": len(type_errors),
        "chunk_errors": len(errors),
        "chunks_completed": done_ct,
        "state_path": state_path,
    }
