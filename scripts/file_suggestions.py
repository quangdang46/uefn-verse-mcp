"""
fileSuggestion command — outputs key UEFN Toolbelt files for @ mention in Claude Code.
Runs when the user types @ in the prompt box.
"""
files = [
    "Content/Python/uefn_tools/__init__.py",
    "Content/Python/uefn_tools/tools/__init__.py",
    "Content/Python/uefn_tools/core/__init__.py",
    "scripts/drift_check.py",
    "deploy.bat",
    "CLAUDE.md",
    "TOOL_STATUS.md",
    "ARCHITECTURE.md",
    "docs/UEFN_QUIRKS.md",
    "docs/PIPELINE.md",
    "docs/ui_style_guide.md",
    ".claude/tool_tables.md",
    ".claude/mcp_reference.md",
    "mcp_server.py",
    "client.py",
]

print("\n".join(files))
