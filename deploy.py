#!/usr/bin/env python3
"""
deploy.py — Deploy uefn_tools to a UEFN project.

Usage:
    python deploy.py
    python deploy.py --project "MyIsland"
    python deploy.py --path "D:\\Projects\\MyIsland"
    python deploy.py --path=D:\\Projects\\MyIsland

--project matches a folder name under Documents/Fortnite Projects.
--path is the full path to the UEFN project root (any drive or parent folder).

This copies:
    - uefn_tools/     -> {project}/Content/Python/uefn_tools/   (includes mcp_bridge HTTP listener)
    - init_unreal.py  -> {project}/Content/Python/init_unreal.py
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def find_fortnite_projects() -> list[tuple[str, str]]:
    """Find all Fortnite Projects folders."""
    base = Path(os.path.expanduser("~/Documents/Fortnite Projects"))
    if not base.exists():
        return []
    return [(p.name, str(p)) for p in sorted(base.iterdir()) if p.is_dir()]


def resolve_existing_dir(raw: str) -> Path | None:
    """If raw is an existing directory path, return resolved Path; else None."""
    if not raw or not raw.strip():
        return None
    p = Path(raw.strip().strip('"').strip("'")).expanduser()
    try:
        p = p.resolve(strict=False)
    except OSError:
        return None
    if p.is_dir():
        return p
    return None


def deploy(project_path: str, dry_run: bool = False) -> None:
    repo_root = Path(__file__).parent.resolve()
    
    uefn_tools_src = repo_root / "Content" / "Python" / "uefn_tools"
    init_src = repo_root / "init_unreal.py"
    
    dest_base = Path(project_path) / "Content" / "Python"
    
    if dry_run:
        print(f"[DRY RUN] Would deploy to: {dest_base}")
        print(f"  uefn_tools/     -> {dest_base}/uefn_tools/")
        print(f"  init_unreal.py  -> {dest_base}/init_unreal.py")
        return
    
    dest_base.mkdir(parents=True, exist_ok=True)
    
    # Deploy uefn_tools
    uefn_tools_dest = dest_base / "uefn_tools"
    if uefn_tools_dest.exists():
        shutil.rmtree(uefn_tools_dest)
    shutil.copytree(uefn_tools_src, uefn_tools_dest)
    print(f"[OK] uefn_tools/ -> {uefn_tools_dest}")

    # Deploy init_unreal.py
    init_dest = dest_base / "init_unreal.py"
    shutil.copy2(init_src, init_dest)
    print(f"[OK] init_unreal.py -> {init_dest}")
    
    print()
    print("Deploy complete!")
    print()
    print("Next steps:")
    print("  1. Open UEFN")
    print("  2. Open Python Console (Output Log -> type 'py')")
    print("  3. Run: import uefn_tools as ut; ut.register(); ut.run('mcp_start')")
    print()


def _cli_path_and_project() -> tuple[str | None, str | None]:
    """
    Parse --path and --project from argv.

    Supports both forms:
      --path=C:\\foo\\bar
      --path C:\\foo\\bar
    (same for --project).
    """
    argv = sys.argv[1:]
    path_arg: str | None = None
    project_arg: str | None = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--path="):
            path_arg = a.split("=", 1)[1]
            i += 1
        elif a == "--path":
            if i + 1 >= len(argv):
                print("ERROR: --path requires a directory argument.")
                sys.exit(1)
            path_arg = argv[i + 1]
            i += 2
        elif a.startswith("--project="):
            project_arg = a.split("=", 1)[1]
            i += 1
        elif a == "--project":
            if i + 1 >= len(argv):
                print("ERROR: --project requires a name or path argument.")
                sys.exit(1)
            project_arg = argv[i + 1]
            i += 2
        else:
            i += 1
    return path_arg, project_arg


def main():
    projects = find_fortnite_projects()

    path_arg, project_arg = _cli_path_and_project()

    project_path: str | None = None

    if path_arg:
        resolved = resolve_existing_dir(path_arg)
        if not resolved:
            print(f"ERROR: Not a valid folder: {path_arg}")
            sys.exit(1)
        project_path = str(resolved)
    elif project_arg:
        resolved = resolve_existing_dir(project_arg)
        if resolved:
            project_path = str(resolved)
        else:
            for name, path in projects:
                if name == project_arg or path.endswith(project_arg):
                    project_path = path
                    break
            if not project_path:
                print(f"ERROR: Project '{project_arg}' not found under Documents/Fortnite Projects.")
                print("Tip: use full path with --path=... if the project lives elsewhere.")
                sys.exit(1)
    else:
        if projects:
            print("Available Fortnite Projects (Documents/Fortnite Projects):")
            for i, (name, _) in enumerate(projects, 1):
                print(f"  [{i}] {name}")
            custom_idx = len(projects) + 1
            print(f"  [{custom_idx}] Custom project folder (enter full path, e.g. D:\\Projects\\MyIsland)")
            print()
            try:
                choice = int(input("Select option number: "))
            except (ValueError, EOFError):
                print("Invalid selection.")
                sys.exit(1)

            if choice == custom_idx:
                raw = input("Project folder path: ").strip()
                resolved = resolve_existing_dir(raw)
                if not resolved:
                    print(f"ERROR: Not a valid folder: {raw!r}")
                    sys.exit(1)
                project_path = str(resolved)
            elif 1 <= choice <= len(projects):
                project_path = projects[choice - 1][1]
            else:
                print("Invalid selection.")
                sys.exit(1)
        else:
            print("No projects found under ~/Documents/Fortnite Projects.")
            print("Enter your UEFN project root folder (must contain Content/Python after deploy),")
            print("for example: D:\\Projects\\MyIsland")
            print()
            raw = input("Project folder path: ").strip()
            resolved = resolve_existing_dir(raw)
            if not resolved:
                print(f"ERROR: Not a valid folder: {raw!r}")
                sys.exit(1)
            project_path = str(resolved)

    print()
    print(f"Deploying to: {project_path}")
    deploy(project_path)


if __name__ == "__main__":
    main()
