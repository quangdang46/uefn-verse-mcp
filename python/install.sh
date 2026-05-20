#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# verse-docs-mcp installer
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/quangdang46/uefn-verse-mcp/main/python/install.sh | bash
#
# Options (via env vars):
#   BRANCH=main            Git branch to install from (default: main)
#   REGISTER=1             Auto-register MCP server in detected hosts
#   VERSE_MCP_HOST=cursor  Comma-separated hosts to register
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

OWNER="quangdang46"
REPO="uefn-verse-mcp"
BRANCH="${BRANCH:-main}"
PKG_NAME="verse-docs-mcp"
REGISTER="${REGISTER:-0}"
MIN_PYTHON="3.10"

log_info()    { echo "[${PKG_NAME}] $*" >&2; }
log_success() { echo "✓ $*" >&2; }
die()         { echo "ERROR: $*" >&2; exit 1; }

# ── Check Python ──────────────────────────────────────────────────────────────

find_python3() {
    for cmd in python3 python; do
        if command -v "$cmd" >/dev/null 2>&1; then
            local ver
            ver=$("$cmd" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null) || continue
            local major minor
            major="${ver%%.*}"
            minor="${ver#*.}"
            if [ "$major" -ge 3 ] && [ "$minor" -ge 10 ]; then
                echo "$cmd"
                return 0
            fi
        fi
    done
    return 1
}

PYTHON=$(find_python3) || die "Python >= ${MIN_PYTHON} is required. Install from https://python.org"
log_info "Using $PYTHON ($($PYTHON --version 2>&1))"

# ── Install package ──────────────────────────────────────────────────────────

GIT_URL="git+https://github.com/${OWNER}/${REPO}.git@${BRANCH}#subdirectory=python"

install_with_uv() {
    log_info "Installing with uv tool install ..."
    uv tool install "${PKG_NAME}" --from "${GIT_URL}" --force
}

install_with_pipx() {
    log_info "Installing with pipx ..."
    pipx install "${GIT_URL}" --force
}

install_with_pip() {
    log_info "Installing with pip ..."
    "$PYTHON" -m pip install --user "${GIT_URL}"
}

if command -v uv >/dev/null 2>&1; then
    install_with_uv
elif command -v pipx >/dev/null 2>&1; then
    install_with_pipx
else
    log_info "Neither uv nor pipx found — falling back to pip install --user."
    install_with_pip
fi

# ── Verify ────────────────────────────────────────────────────────────────────

if command -v verse-docs-mcp >/dev/null 2>&1; then
    log_success "verse-docs-mcp $(verse-docs-mcp --version 2>&1 | head -1) installed successfully!"
else
    log_info "Binary not on PATH yet — try: export PATH=\"\$HOME/.local/bin:\$PATH\""
fi

# ── Optional: register in MCP hosts ──────────────────────────────────────────

BINARY_PATH="$(command -v verse-docs-mcp 2>/dev/null || echo "")"

if [ "${REGISTER}" = "1" ] && [ -n "${BINARY_PATH}" ]; then
    PYTHON_CMD=$(find_python3) || true

    append_unique_host() {
        local host="$1"
        for existing in "${MCP_HOSTS[@]:-}"; do
            [ "$existing" = "$host" ] && return 0
        done
        MCP_HOSTS+=("$host")
    }

    detect_mcp_hosts() {
        MCP_HOSTS=()
        if [ -n "${VERSE_MCP_HOST:-}" ]; then
            IFS=',' read -r -a raw <<< "${VERSE_MCP_HOST}"
            for host in "${raw[@]}"; do
                host="$(printf '%s' "$host" | xargs)"
                [ -n "$host" ] && append_unique_host "$host"
            done
        else
            [ -f "$HOME/.claude.json" ] && append_unique_host "claude-code"
            [ -d "$HOME/.cursor" ] && append_unique_host "cursor"
            [ -d "$HOME/.codeium/windsurf" ] && append_unique_host "windsurf"
            [ -d "$HOME/.codex" ] && append_unique_host "codex"
        fi
    }

    upsert_json_mcp() {
        local path="$1" servers_key="$2"
        "$PYTHON_CMD" - "$path" "$servers_key" "$PKG_NAME" "$BINARY_PATH" <<'PY'
import json, os, sys
path, servers_key, server_name, command = sys.argv[1:5]
entry = {"command": command, "args": []}
data = {}
if os.path.exists(path):
    with open(path, "r") as f:
        data = json.load(f)
servers = data.setdefault(servers_key, {})
servers[server_name] = entry
with open(path, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")
print("registered")
PY
    }

    detect_mcp_hosts

    for host in "${MCP_HOSTS[@]:-}"; do
        case "$host" in
            claude-code)
                status=$(upsert_json_mcp "$HOME/.claude.json" "mcpServers" 2>&1) || true
                log_info "Claude Code: $status"
                ;;
            cursor)
                mkdir -p "$HOME/.cursor"
                status=$(upsert_json_mcp "$HOME/.cursor/mcp.json" "mcpServers" 2>&1) || true
                log_info "Cursor: $status"
                ;;
            windsurf)
                mkdir -p "$HOME/.codeium/windsurf"
                status=$(upsert_json_mcp "$HOME/.codeium/windsurf/mcp_config.json" "mcpServers" 2>&1) || true
                log_info "Windsurf: $status"
                ;;
            codex)
                mkdir -p "$HOME/.codex"
                status=$(upsert_json_mcp "$HOME/.codex/config.json" "mcpServers" 2>&1) || true
                log_info "Codex: $status"
                ;;
        esac
    done
fi

log_success "Done! Run: verse-docs-mcp serve"
