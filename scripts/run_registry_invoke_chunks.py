#!/usr/bin/env python3
"""
Run registry_invoke_all_tools in chunks against a live UEFN MCP bridge.

Prerequisites:
  - UEFN open with listener: import uefn_tools as ut; ut.run("mcp_start")
  - Deploy latest uefn_tools (includes diagnostics.registry_invoke_all_tools)

Environment:
  REGISTRY_INVOKE_MODE   safe | full   (default: full)
  REGISTRY_INVOKE_CHUNKS int           (default: 24)
  UEFN_MCP_REQUEST_TIMEOUT seconds    (default: 120)

Usage (repo root):
  python scripts/run_registry_invoke_chunks.py
"""
from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

os.environ.setdefault("UEFN_MCP_REQUEST_TIMEOUT", "120")

from server import bridge  # noqa: E402


def main() -> int:
    mode = os.environ.get("REGISTRY_INVOKE_MODE", "full").strip().lower()
    chunks = int(os.environ.get("REGISTRY_INVOKE_CHUNKS", "24"))
    timeout = float(os.environ.get("UEFN_MCP_REQUEST_TIMEOUT", "120"))

    if mode not in ("safe", "full"):
        print("REGISTRY_INVOKE_MODE must be safe or full")
        return 1
    if chunks < 1:
        print("REGISTRY_INVOKE_CHUNKS must be >= 1")
        return 1

    for idx in range(chunks):
        code = f"""
import importlib
import uefn_tools.diagnostics as d
importlib.reload(d)
import uefn_tools as ut
print(ut.run("registry_invoke_all_tools", mode="{mode}", chunk_index={idx}, chunk_total={chunks}))
""".strip()
        print(f"--- chunk {idx + 1}/{chunks} ---")
        try:
            out = bridge.send_command(
                "execute_python",
                {"code": code},
                timeout=timeout,
            )
            print(out)
        except Exception as e:
            print(f"FAILED chunk {idx}: {e}")
            return 1

    print("Done. Report: Saved/uefn_tools/registry_invoke_all_report.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
