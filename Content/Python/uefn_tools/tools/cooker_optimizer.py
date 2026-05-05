"""
uefn_tools — cooker_optimizer.py
=====================================
Manage "Editor Only" actor flags to help large projects cook successfully.

When a project fails to cook due to out-of-memory errors, exclude actor batches
from the cooked build progressively until the cook succeeds, then restore them.
Confidence estimates are built from your cook feedback history across sessions.

Workflow:
  1. tb.run("cooker_scan")                             # audit level actors
  2. tb.run("cooker_mark_batch", percent=50, dry_run=True)  # preview
  3. tb.run("cooker_mark_batch", percent=50, dry_run=False) # apply
  4. Launch session in UEFN — note cook success/fail (Output Log or your own notes)
  5. Iterate percent up or down until cook succeeds
  6. tb.run("cooker_unmark_all")                       # ALWAYS restore before publishing

Credits:
  Original concept & tool: BiomeForge (CookerOptimizer)
  Native uefn_tools implementation: Ocean Bennett (UEFN uefn_tools v1.9.8+)
"""

import os
import json
import math
import unreal
from ..registry import register_tool
from ..core import log_info, log_warning, log_error

# ── Module-level scan cache (shared between cooker_* headless tools) ────────────
_scan_cache: dict = {
    "rows":    [],    # [{label, class_name, actor_type, is_editor_only, actor}]
    "scanned": False,
}

# ─────────────────────────────────────────────────────────────────────────────
#  Cook feedback — persisted across sessions
# ─────────────────────────────────────────────────────────────────────────────

def _feedback_path() -> str:
    return os.path.join(
        unreal.Paths.project_saved_dir(), "uefn_tools", "cooker_feedback.json"
    )


def _load_feedback() -> list:
    try:
        p = _feedback_path()
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        pass
    return []


def _save_feedback(history: list) -> None:
    try:
        p = _feedback_path()
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        log_warning(f"cooker: could not save feedback history: {e}")


# ─────────────────────────────────────────────────────────────────────────────
#  Actor helpers
# ─────────────────────────────────────────────────────────────────────────────

def _all_actors() -> list:
    try:
        sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        return list(sub.get_all_level_actors() or [])
    except Exception:
        return list(unreal.EditorLevelLibrary.get_all_level_actors() or [])


def _selected_actors() -> list:
    try:
        sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        return list(sub.get_selected_level_actors() or [])
    except Exception:
        return list(unreal.EditorLevelLibrary.get_selected_level_actors() or [])


def _is_blueprint(actor) -> bool:
    try:
        return not str(actor.get_class().get_path_name()).startswith("/Script/")
    except Exception:
        return False


def _is_static_mesh(actor) -> bool:
    try:
        return actor.get_class().get_name() == "StaticMeshActor"
    except Exception:
        return False


def _is_landscape(actor) -> bool:
    try:
        return actor.get_class().get_name() in {
            "Landscape", "LandscapeProxy", "LandscapeStreamingProxy"
        }
    except Exception:
        return False


def _get_editor_only(actor) -> bool:
    try:
        return bool(actor.get_editor_property("is_editor_only_actor"))
    except Exception:
        return False


def _set_editor_only(actor, value: bool) -> bool:
    try:
        actor.set_editor_property("is_editor_only_actor", value)
        return True
    except Exception:
        return False


def _save_level() -> None:
    try:
        unreal.EditorLevelLibrary.save_current_level()
    except Exception as e:
        log_warning(f"cooker: level save failed: {e}")


# ─────────────────────────────────────────────────────────────────────────────
#  Confidence estimator — weighted nearest-neighbour
# ─────────────────────────────────────────────────────────────────────────────

def _estimate_confidence(history: list, percent: float, pool: int):
    """Return (pct_int | None, basis_str)."""
    if not history:
        return None, "Awaiting first cook result"
    if pool <= 0:
        return None, "No scanned pool"

    # Exact match
    exact = [h for h in history
             if abs(h["percent"] - percent) < 0.0001 and h["pool"] == pool]
    if exact:
        avg = sum(1.0 if h["success"] else 0.0 for h in exact) / len(exact)
        return (
            int(round(avg * 100)),
            f"Exact match from {len(exact)} result(s) at {percent:g}% with pool {pool}",
        )

    # Weighted interpolation
    ws = wt = 0.0
    for h in history:
        pd = abs(h["percent"] - percent) / 100.0
        qd = abs(h["pool"] - pool) / float(max(pool, 1))
        w  = 1.0 / (1.0 + pd * 6.0 + qd * 2.5)
        ws += (1.0 if h["success"] else 0.0) * w
        wt += w

    if wt <= 0:
        return None, "Insufficient history"
    return (
        int(round((ws / wt) * 100)),
        f"Rough estimate from {len(history)} result(s), weighted by setting similarity",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  Headless tools
# ─────────────────────────────────────────────────────────────────────────────

@register_tool(
    name="cooker_scan",
    category="Optimization",
    description=(
        "Scan level actors and return a count breakdown by type and editor-only status. "
        "Run before cooker_mark_batch. Filters: blueprints, static_meshes, landscapes."
    ),
    tags=["cooker", "cook", "editor-only", "optimization", "scan", "memory", "oom"],
    example='tb.run("cooker_scan", blueprints=True, static_meshes=True)',
)
def cooker_scan(
    blueprints: bool = True,
    static_meshes: bool = True,
    landscapes: bool = False,
    exclude_already_editor_only: bool = False,
    **kwargs,
) -> dict:
    """
    Scan level actors for cooker optimization.

    Args:
        blueprints:                  Include Blueprint actors (default True)
        static_meshes:               Include StaticMesh actors (default True)
        landscapes:                  Include Landscape actors (default False — use cautiously)
        exclude_already_editor_only: Skip actors already marked editor-only (default False)

    Returns:
        {
          "status": "ok",
          "total": int, "editor_only": int, "not_editor_only": int,
          "blueprints": int, "static_meshes": int, "landscapes": int
        }
    """
    if not (blueprints or static_meshes or landscapes):
        return {"status": "error", "error": "Enable at least one actor type filter."}

    rows = []
    for actor in _all_actors():
        if actor is None:
            continue
        is_eo = _get_editor_only(actor)
        if exclude_already_editor_only and is_eo:
            continue

        if blueprints and _is_blueprint(actor):
            atype = "blueprint"
        elif static_meshes and _is_static_mesh(actor):
            atype = "static_mesh"
        elif landscapes and _is_landscape(actor):
            atype = "landscape"
        else:
            continue

        try:
            label = actor.get_actor_label()
        except Exception:
            label = "<unknown>"
        try:
            cls = actor.get_class().get_name()
        except Exception:
            cls = "unknown"

        rows.append({
            "actor":          actor,
            "label":          label,
            "class_name":     cls,
            "actor_type":     atype,
            "is_editor_only": is_eo,
        })

    rows.sort(key=lambda r: (r["actor_type"], r["class_name"].lower(), r["label"].lower()))
    _scan_cache["rows"]    = rows
    _scan_cache["scanned"] = True

    total  = len(rows)
    eo_cnt = sum(1 for r in rows if r["is_editor_only"])
    bp_cnt = sum(1 for r in rows if r["actor_type"] == "blueprint")
    sm_cnt = sum(1 for r in rows if r["actor_type"] == "static_mesh")
    ls_cnt = sum(1 for r in rows if r["actor_type"] == "landscape")

    log_info(f"cooker_scan: {total} eligible (bp={bp_cnt} sm={sm_cnt} ls={ls_cnt} eo={eo_cnt})")
    return {
        "status":          "ok",
        "total":           total,
        "editor_only":     eo_cnt,
        "not_editor_only": total - eo_cnt,
        "blueprints":      bp_cnt,
        "static_meshes":   sm_cnt,
        "landscapes":      ls_cnt,
        "tip": "Run cooker_mark_batch(percent=50, dry_run=True) to preview which actors would be marked.",
    }


@register_tool(
    name="cooker_mark_batch",
    category="Optimization",
    description=(
        "Mark a percentage of scanned actors as editor-only to reduce cook load. "
        "Run cooker_scan first. Always use dry_run=True to preview before applying. "
        "Start at percent=50, iterate down until cook succeeds, then cooker_unmark_all."
    ),
    tags=["cooker", "cook", "editor-only", "optimization", "batch", "mark"],
    example='tb.run("cooker_mark_batch", percent=50, dry_run=True)',
)
def cooker_mark_batch(
    percent: float = 50.0,
    dry_run: bool = True,
    **kwargs,
) -> dict:
    """
    Mark a percentage of scanned actors as editor-only.

    Args:
        percent:  Percentage of scanned pool to mark (1-100). Start at 50.
        dry_run:  Preview without changes if True (default True — always preview first).

    Returns:
        {
          "status": "ok", "dry_run": bool, "percent": float,
          "pool": int, "target_count": int, "changed": int, "failed": int,
          "actors": [str, ...]  -- first 50 labels
        }
    """
    if not _scan_cache["scanned"] or not _scan_cache["rows"]:
        return {"status": "error", "error": "Run cooker_scan first."}
    if percent <= 0 or percent > 100:
        return {"status": "error", "error": "percent must be between 1 and 100."}

    rows   = _scan_cache["rows"]
    total  = len(rows)
    target = max(1, math.floor(total * (percent / 100.0)))

    # Even distribution across sorted pool (mirrors original algorithm)
    step    = total / float(target)
    indices: set = set()
    for i in range(target):
        indices.add(min(int(round(i * step)), total - 1))
    candidate = 0
    while len(indices) < target and candidate < total:
        indices.add(candidate)
        candidate += 1

    chosen = [rows[i] for i in sorted(indices)]
    labels = [r["label"] for r in chosen]

    if dry_run:
        log_info(f"cooker_mark_batch DRY RUN: {len(chosen)}/{total} at {percent:g}%")
        return {
            "status":       "ok",
            "dry_run":      True,
            "percent":      percent,
            "pool":         total,
            "target_count": len(chosen),
            "changed":      0,
            "failed":       0,
            "actors":       labels[:50],
            "tip": "Set dry_run=False to apply. Run cooker_unmark_all before publishing.",
        }

    changed = 0
    failed  = []
    with unreal.ScopedEditorTransaction("Cooker Optimizer — mark editor-only") as _t:
        for row in chosen:
            if _set_editor_only(row["actor"], True):
                row["is_editor_only"] = True
                changed += 1
            else:
                failed.append(row["label"])

    _save_level()
    log_info(f"cooker_mark_batch: marked {changed}/{len(chosen)} at {percent:g}%  failed={len(failed)}")
    return {
        "status":        "ok",
        "dry_run":       False,
        "percent":       percent,
        "pool":          total,
        "target_count":  len(chosen),
        "changed":       changed,
        "failed":        len(failed),
        "failed_labels": failed[:20],
        "tip": "Launch a session. If cook fails, increase percent. If succeeds, reduce or run cooker_unmark_all.",
    }


@register_tool(
    name="cooker_unmark_all",
    category="Optimization",
    description=(
        "Clear the editor-only flag from all scanned actors. "
        "Always run this before publishing your map."
    ),
    tags=["cooker", "cook", "editor-only", "optimization", "restore", "unmark"],
    example='tb.run("cooker_unmark_all")',
)
def cooker_unmark_all(**kwargs) -> dict:
    """
    Remove editor-only flag from every actor in the current scan cache.

    Returns:
        {"status": "ok", "changed": int, "failed": int}
    """
    if not _scan_cache["scanned"] or not _scan_cache["rows"]:
        return {"status": "error", "error": "Run cooker_scan first."}

    changed = 0
    failed  = []
    with unreal.ScopedEditorTransaction("Cooker Optimizer — unmark all") as _t:
        for row in _scan_cache["rows"]:
            if row["is_editor_only"]:
                if _set_editor_only(row["actor"], False):
                    row["is_editor_only"] = False
                    changed += 1
                else:
                    failed.append(row["label"])

    _save_level()
    log_info(f"cooker_unmark_all: cleared {changed}  failed={len(failed)}")
    return {
        "status":        "ok",
        "changed":       changed,
        "failed":        len(failed),
        "failed_labels": failed[:20],
    }


@register_tool(
    name="cooker_mark_selection",
    category="Optimization",
    description=(
        "Mark or clear editor-only on the current viewport selection. "
        "mark=True excludes actors from cook, mark=False restores them."
    ),
    tags=["cooker", "cook", "editor-only", "selection", "mark", "optimization"],
    example='tb.run("cooker_mark_selection", mark=True)',
)
def cooker_mark_selection(mark: bool = True, **kwargs) -> dict:
    """
    Apply or remove editor-only flag on the current viewport selection.

    Args:
        mark: True to mark as editor-only, False to clear (default True).

    Returns:
        {"status": "ok", "action": str, "changed": int, "failed": int}
    """
    actors = _selected_actors()
    if not actors:
        return {"status": "error", "error": "No actors selected in the viewport."}

    changed = 0
    failed  = []
    action  = "mark" if mark else "clear"

    with unreal.ScopedEditorTransaction(f"Cooker Optimizer — {action} selection") as _t:
        for actor in actors:
            if _set_editor_only(actor, mark):
                changed += 1
                # Sync scan cache if populated
                try:
                    lbl = actor.get_actor_label()
                    for row in _scan_cache["rows"]:
                        if row["label"] == lbl:
                            row["is_editor_only"] = mark
                except Exception:
                    pass
            else:
                try:
                    failed.append(actor.get_actor_label())
                except Exception:
                    failed.append("<unknown>")

    _save_level()
    log_info(f"cooker_mark_selection: {action} {changed}/{len(actors)}  failed={len(failed)}")
    return {
        "status":        "ok",
        "action":        action,
        "changed":       changed,
        "failed":        len(failed),
        "failed_labels": failed[:20],
    }


# ─────────────────────────────────────────────────────────────────────────────
#  cooker_open — MCP guidance (no PySide window)
# ─────────────────────────────────────────────────────────────────────────────

@register_tool(
    name="cooker_open",
    category="Optimization",
    description=(
        "MCP / headless only: no editor window. Use cooker_scan on the current level, then "
        "cooker_mark_batch / cooker_mark_selection / cooker_unmark_all to tune editor-only "
        "flags and reduce cook load. Based on CookerOptimizer by BiomeForge."
    ),
    tags=["cooker", "cook", "editor-only", "optimization", "mcp", "headless"],
    example='tb.run("cooker_scan") then tb.run("cooker_mark_batch", ...) ',
)
def cooker_open(**kwargs) -> dict:
    log_info(
        "cooker_open: no UI — use cooker_scan, cooker_mark_batch, cooker_mark_selection, cooker_unmark_all."
    )
    return {
        "status": "ok",
        "message": "Cooker Optimizer has no PySide window; use headless cooker_* tools.",
        "headless_tools": [
            "cooker_scan",
            "cooker_mark_batch",
            "cooker_mark_selection",
            "cooker_unmark_all",
        ],
    }


