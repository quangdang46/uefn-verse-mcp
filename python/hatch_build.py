"""Hatch build hook: pre-build the SQLite FTS5 docs DB.

Runs during ``hatch build`` / ``pip install .`` and embeds the compiled
database into the wheel as ``verse_docs_mcp/data/verse-docs.db``.
"""

from __future__ import annotations

import sys
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface  # type: ignore[import-not-found]


class CustomBuildHook(BuildHookInterface):
    PLUGIN_NAME = "custom"

    def initialize(self, version: str, build_data: dict) -> None:  # noqa: ARG002
        db_path = Path(self.root) / "src" / "verse_docs_mcp" / "data" / "verse-docs.db"
        if db_path.exists():
            return

        repo_root = _find_repo_root(Path(self.root))
        if repo_root is None:
            print(
                "WARNING: could not locate docs directories — shipping without pre-built DB.",
                file=sys.stderr,
            )
            db_path.parent.mkdir(parents=True, exist_ok=True)
            db_path.touch()
            return

        sys.path.insert(0, str(Path(self.root) / "src"))
        from verse_docs_mcp.index import build_database

        db_path.parent.mkdir(parents=True, exist_ok=True)
        build_database(repo_root, db_path)
        print(f"Built docs database ({db_path.stat().st_size:,} bytes)")


def _find_repo_root(start: Path) -> Path | None:
    current = start.resolve()
    for _ in range(10):
        if (current / "verse-api-pages-canonical").is_dir():
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent
    return None
