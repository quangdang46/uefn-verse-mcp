#!/usr/bin/env python3
"""
deploy.py — Deploy uefn_tools to a UEFN project.

Usage:
    python deploy.py
    python deploy.py --project "MyIsland"
    python deploy.py --path "D:\\Projects\\MyIsland"
    python deploy.py --path=D:\\Projects\\MyIsland
    python deploy.py --project "MyIsland" --link-kind junction
    python deploy.py --path "D:\\Projects\\MyIsland" --link-kind symlink

--project matches a folder name under Documents/Fortnite Projects.
--path is the full path to the UEFN project root (any drive or parent folder).
--link-kind creates a junction or symlink instead of copying (opt-in, local dev only).

By default this copies:
    - uefn_tools/     -> {project}/Content/Python/uefn_tools/   (includes mcp_bridge HTTP listener)
    - init_unreal.py  -> {project}/Content/Python/init_unreal.py

With --link-kind, uefn_tools/ is linked (junction or symlink) instead of copied.
init_unreal.py is always copied as a real file.

Also ensures {project}/.urcignore contains Content/Python/* so URC does not try to sync
editor-only Python tooling to the cloud.
"""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

LINK_KINDS = ("junction", "symlink")

URCIGNORE_PYTHON_GLOB = "Content/Python/*"


def _ensure_urcignore_python(project_root: Path, dry_run: bool) -> None:
    """Append Content/Python/* to .urcignore at project root if missing."""
    urc = project_root / ".urcignore"
    if urc.exists():
        text = urc.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if line.strip() == URCIGNORE_PYTHON_GLOB:
                return
        if dry_run:
            print(f"[DRY RUN] Would append {URCIGNORE_PYTHON_GLOB!r} to {urc}")
            return
        ending = "" if text.endswith("\n") or not text else "\n"
        urc.write_text(text + ending + URCIGNORE_PYTHON_GLOB + "\n", encoding="utf-8")
        print(f"[OK] Appended {URCIGNORE_PYTHON_GLOB!r} to {urc}")
    else:
        if dry_run:
            print(f"[DRY RUN] Would create {urc} with {URCIGNORE_PYTHON_GLOB!r}")
            return
        urc.write_text(URCIGNORE_PYTHON_GLOB + "\n", encoding="utf-8")
        print(f"[OK] Created {urc} with {URCIGNORE_PYTHON_GLOB!r}")


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


def _is_junction(path: Path) -> bool:
    """Return True if *path* is a Windows junction (reparse point)."""
    if platform.system() != "Windows":
        return False
    try:
        import ctypes
        attrs = ctypes.windll.kernel32.GetFileAttributesW(str(path))  # type: ignore[union-attr]
        return attrs != -1 and bool(attrs & 0x400)  # FILE_ATTRIBUTE_REPARSE_POINT
    except Exception:
        return False


def _remove_existing(dest: Path) -> None:
    """Remove *dest* whether it is a real dir, junction, or symlink."""
    if dest.is_symlink() or _is_junction(dest):
        if platform.system() == "Windows":
            try:
                dest.rmdir()
            except OSError:
                subprocess.check_call(["cmd", "/c", "rmdir", str(dest)])
        else:
            dest.unlink()
        print(f"[OK] Removed existing link: {dest}")
    elif dest.exists():
        shutil.rmtree(dest)
        print(f"[OK] Removed existing directory: {dest}")


def _create_link(src: Path, dest: Path, kind: str) -> None:
    """Create a junction or symlink from *dest* -> *src*."""
    if kind == "junction":
        if platform.system() == "Windows":
            subprocess.check_call(["cmd", "/c", "mklink", "/J", str(dest), str(src)])
        else:
            dest.symlink_to(src, target_is_directory=True)
            print("  (junctions are Windows-only; created symlink as equivalent)")
    elif kind == "symlink":
        dest.symlink_to(src, target_is_directory=True)
    else:
        raise ValueError(f"Unknown link kind: {kind!r}")


def deploy(
    project_path: str,
    dry_run: bool = False,
    link_kind: str | None = None,
) -> None:
    repo_root = Path(__file__).parent.resolve()

    uefn_tools_src = repo_root / "Content" / "Python" / "uefn_tools"
    init_src = repo_root / "init_unreal.py"

    dest_base = Path(project_path) / "Content" / "Python"

    mode_label = f"link ({link_kind})" if link_kind else "copy"

    if dry_run:
        print(f"[DRY RUN] Would deploy to: {dest_base}  (mode: {mode_label})")
        print(f"  uefn_tools/     -> {dest_base}/uefn_tools/")
        print(f"  init_unreal.py  -> {dest_base}/init_unreal.py")
        _ensure_urcignore_python(Path(project_path), dry_run=True)
        return

    dest_base.mkdir(parents=True, exist_ok=True)

    # Deploy uefn_tools
    uefn_tools_dest = dest_base / "uefn_tools"
    _remove_existing(uefn_tools_dest)

    if link_kind:
        _create_link(uefn_tools_src, uefn_tools_dest, link_kind)
        print(f"[OK] uefn_tools/ -> {uefn_tools_dest}  ({link_kind} -> {uefn_tools_src})")
    else:
        shutil.copytree(uefn_tools_src, uefn_tools_dest)
        print(f"[OK] uefn_tools/ -> {uefn_tools_dest}  (copy)")

    # Deploy init_unreal.py (always a real file copy)
    init_dest = dest_base / "init_unreal.py"
    shutil.copy2(init_src, init_dest)
    print(f"[OK] init_unreal.py -> {init_dest}")

    _ensure_urcignore_python(Path(project_path), dry_run=False)

    print()
    print(f"Deploy complete!  (mode: {mode_label})")
    if link_kind:
        print()
        print(f"  Link target: {uefn_tools_src}")
        print("  Edits in the repo checkout are immediately visible to UEFN.")
        print("  This mode is for local iteration only — do not use for")
        print("  shared or team projects.")
    print()
    print("Next steps:")
    print("  1. Open UEFN")
    print("  2. Open Python Console (Output Log -> type 'py')")
    print("  3. Run: import uefn_tools as ut; ut.register(); ut.run('mcp_start')")
    print()


def _cli_parse_args() -> tuple[str | None, str | None, str | None]:
    """
    Parse --path, --project, and --link-kind from argv.

    Supports both forms:
      --path=C:\\foo\\bar
      --path C:\\foo\\bar
    (same for --project and --link-kind).

    Returns (path_arg, project_arg, link_kind).
    """
    argv = sys.argv[1:]
    path_arg: str | None = None
    project_arg: str | None = None
    link_kind: str | None = None
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
        elif a.startswith("--link-kind="):
            link_kind = a.split("=", 1)[1]
            i += 1
        elif a == "--link-kind":
            if i + 1 >= len(argv):
                print("ERROR: --link-kind requires 'junction' or 'symlink'.")
                sys.exit(1)
            link_kind = argv[i + 1]
            i += 2
        else:
            i += 1

    if link_kind and link_kind not in LINK_KINDS:
        print(f"ERROR: --link-kind must be one of {LINK_KINDS}, got {link_kind!r}.")
        sys.exit(1)

    return path_arg, project_arg, link_kind


def main():
    projects = find_fortnite_projects()

    path_arg, project_arg, link_kind = _cli_parse_args()

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
    mode_label = f"link ({link_kind})" if link_kind else "copy"
    print(f"Deploying to: {project_path}  (mode: {mode_label})")
    deploy(project_path, link_kind=link_kind)


if __name__ == "__main__":
    main()
