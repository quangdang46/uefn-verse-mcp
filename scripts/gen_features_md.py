"""Regenerate FEATURES.md MCP / run_tool checklist tables."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UEFN_TOOLS = ROOT / "Content/Python/uefn_tools"
FEATURES = ROOT / "FEATURES.md"

NATIVE_MCP: list[tuple[str, str]] = [
    ("ping", "System"),
    ("get_status", "System"),
    ("execute_python", "System"),
    ("get_log", "System"),
    ("shutdown", "System"),
    ("get_all_actors", "Actors"),
    ("get_selected_actors", "Actors"),
    ("spawn_actor", "Actors"),
    ("delete_actors", "Actors"),
    ("set_actor_transform", "Actors"),
    ("get_actor_properties", "Actors"),
    ("set_actor_properties", "Actors"),
    ("select_actors", "Actors"),
    ("focus_selected", "Actors"),
    ("list_assets", "Assets"),
    ("get_asset_info", "Assets"),
    ("get_selected_assets", "Assets"),
    ("rename_asset", "Assets"),
    ("delete_asset", "Assets"),
    ("duplicate_asset", "Assets"),
    ("does_asset_exist", "Assets"),
    ("save_asset", "Assets"),
    ("search_assets", "Assets"),
    ("get_project_info", "Project / level"),
    ("save_current_level", "Project / level"),
    ("get_level_info", "Project / level"),
    ("get_viewport_camera", "Viewport"),
    ("set_viewport_camera", "Viewport"),
    ("run_tool", "Escape hatch"),
    ("list_tools", "Escape hatch"),
    ("describe_tool", "Escape hatch"),
]


def extract_register_meta(text: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    i = 0
    while True:
        j = text.find("@register_tool", i)
        if j == -1:
            break
        k = text.find("(", j)
        if k == -1:
            i = j + 14
            continue
        depth = 0
        idx = k
        while idx < len(text):
            if text[idx] == "(":
                depth += 1
            elif text[idx] == ")":
                depth -= 1
                if depth == 0:
                    block = text[k : idx + 1]
                    m = re.search(r'name\s*=\s*"([^"]+)"', block)
                    if m:
                        cat_m = re.search(r'category\s*=\s*"([^"]+)"', block)
                        cat = cat_m.group(1) if cat_m else "—"
                        out.append((m.group(1), cat))
                    i = idx + 1
                    break
            idx += 1
        else:
            break
    return out


def md_escape_cell(s: str) -> str:
    return s.replace("|", "\\|")


def main() -> None:
    flat: list[tuple[str, str, str]] = []
    for p in sorted(UEFN_TOOLS.rglob("*.py")):
        # Docstrings in registry.py contain example `@register_tool(...)` blocks; skip.
        if p.name == "registry.py":
            continue
        rel = str(p.relative_to(UEFN_TOOLS))
        text = p.read_text(encoding="utf-8", errors="replace")
        for name, cat in extract_register_meta(text):
            flat.append((name, cat, rel))

    reg_tools: dict[str, str] = {}
    for name, cat, _rel in flat:
        reg_tools.setdefault(name, cat)
    reg_tools.pop("my_tool", None)  # safety if docstring scan ever picks up examples

    by_name: defaultdict[str, list[str]] = defaultdict(list)
    for name, _cat, rel in flat:
        by_name[name].append(rel)
    dup_note = ""
    dup_names = sorted(n for n, paths in by_name.items() if len(paths) > 1 and n != "my_tool")
    if dup_names:
        lines_dup = [
            "",
            "### Duplicate `@register_tool` names",
            "",
            "The table lists each tool name once; these names appear in more than one file "
            "(typically mirrored paths under `Content/Python/`):",
            "",
        ]
        for n in dup_names:
            uniq = sorted(set(by_name[n]))
            lines_dup.append(f"- `{n}`: {', '.join(uniq)}")
        dup_note = "\n".join(lines_dup)

    lines: list[str] = [
        "# Features checklist",
        "",
        "Auto-generated inventory of MCP surfaces for **verse-mcp** (FastMCP server + UEFN `uefn_tools`). "
        "Update the **Status** column as you verify behavior in-editor.",
        "",
        "## Status legend",
        "",
        "| Value | Meaning |",
        "| --- | --- |",
        "| Untested | Not verified in this environment |",
        "| Working | Verified OK |",
        "| BUG | Broken or incorrect behavior (note in issue tracker) |",
        "",
        f"## Native MCP tools ({len(NATIVE_MCP)})",
        "",
        "Exposed directly on the MCP server (`server/main.py`). Default status is **Untested**.",
        "",
        "| Tool | Category | Status |",
        "| --- | --- | --- |",
    ]
    for name, cat in NATIVE_MCP:
        lines.append(f"| `{md_escape_cell(name)}` | {md_escape_cell(cat)} | Untested |")

    lines.extend(
        [
            "",
            f"## `run_tool` registry ({len(reg_tools)})",
            "",
            "Registered `uefn_tools` entries (invoke via MCP `run_tool` or `list_tools` / `describe_tool`). "
            "`registry.py` is excluded from discovery (documentation-only decorator examples).",
            "",
            "| Tool | Category | Status |",
            "| --- | --- | --- |",
        ]
    )
    for name in sorted(reg_tools):
        cat = reg_tools[name]
        lines.append(f"| `{md_escape_cell(name)}` | {md_escape_cell(cat)} | Untested |")

    if dup_note:
        lines.append(dup_note)

    lines.append("")
    lines.extend(
        [
            "---",
            "",
            "Regenerate: `python scripts/gen_features_md.py`",
            "",
        ]
    )
    FEATURES.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {FEATURES} ({len(NATIVE_MCP)} native + {len(reg_tools)} run_tool)")


if __name__ == "__main__":
    main()
