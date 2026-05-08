#!/usr/bin/env python3
"""
Static audit for uefn_tools (no Unreal required).

Run from repo root:
  python scripts/audit_uefn_tools.py

Checks:
  - py_compile every tools/*.py
  - Every @register_tool-decorated function accepts **kwargs
  - Unique tool names across Content/Python/uefn_tools
  - Unique category strings (informational)
"""
from __future__ import annotations

import ast
import py_compile
import sys
from collections import defaultdict
from pathlib import Path


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    pkg = repo / "Content" / "Python" / "uefn_tools"
    tools_dir = pkg / "tools"

    errors_compile: list[tuple[str, str]] = []
    errors_kwargs: list[tuple[str, str, int]] = []
    names: dict[str, list[str]] = defaultdict(list)
    categories: set[str] = set()
    scanned: set[Path] = set()

    def scan_file(py: Path) -> None:
        py = py.resolve()
        if py in scanned:
            return
        scanned.add(py)
        try:
            py_compile.compile(str(py), doraise=True)
        except py_compile.PyCompileError as e:
            errors_compile.append((str(py.relative_to(repo)), str(e)))
            return
        src = py.read_text(encoding="utf-8", errors="replace")
        try:
            tree = ast.parse(src, filename=str(py))
        except SyntaxError as e:
            errors_compile.append((str(py.relative_to(repo)), str(e)))
            return

        for node in tree.body:
            if not isinstance(node, ast.FunctionDef):
                continue
            has_register = False
            tool_name: str | None = None
            tool_cat: str | None = None
            for dec in node.decorator_list:
                if not isinstance(dec, ast.Call):
                    continue
                if not (isinstance(dec.func, ast.Name) and dec.func.id == "register_tool"):
                    continue
                has_register = True
                for kw in dec.keywords:
                    if kw.arg == "name" and isinstance(kw.value, ast.Constant):
                        if isinstance(kw.value.value, str):
                            tool_name = kw.value.value
                    if kw.arg == "category" and isinstance(kw.value, ast.Constant):
                        if isinstance(kw.value.value, str):
                            tool_cat = kw.value.value
            if not has_register:
                continue
            has_kw = node.args.kwarg is not None and getattr(node.args.kwarg, "arg", None) == "kwargs"
            if not has_kw:
                errors_kwargs.append(
                    (str(py.relative_to(repo)), node.name, node.lineno),
                )
            if tool_name:
                names[tool_name].append(f"{py.relative_to(repo)}:{node.lineno}")
            if tool_cat:
                categories.add(tool_cat)

    for py in sorted(tools_dir.glob("*.py")):
        if py.name == "__init__.py":
            continue
        scan_file(py)

    for py in sorted(pkg.glob("*.py")):
        if py.name == "__init__.py":
            continue
        scan_file(py)

    diag = pkg / "diagnostics.py"
    if diag.exists():
        scan_file(diag)

    core = pkg / "core" / "safety_gate.py"
    if core.exists():
        scan_file(core)

    reg = pkg / "registry.py"
    if reg.exists():
        scan_file(reg)

    dups = {k: v for k, v in names.items() if len(v) > 1}

    print("uefn_tools static audit")
    print("  repo:", repo)
    print("  compile_errors:", len(errors_compile))
    for p, msg in errors_compile[:20]:
        print("   ", p, "->", msg[:200])
    print("  missing_kwargs:", len(errors_kwargs))
    for p, fn, ln in errors_kwargs[:30]:
        print("   ", p, fn, "line", ln)
    print("  duplicate_tool_names:", len(dups))
    for k, v in sorted(dups.items())[:20]:
        print("   ", k, v)
    print("  unique_tools:", len(names))
    print("  unique_categories:", len(categories))

    if errors_compile or errors_kwargs or dups:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
