#!/usr/bin/env bash
set -euo pipefail

REPO="${REPO:-tvmaly/retrieval-ready-markdown-skills}"
REF="${REF:-main}"
SCOPE="user"
PROJECT_DIR="."
INSTALL_CLAUDE=1
INSTALL_CODEX=1

usage() {
  cat <<USAGE
Usage: install.sh [options]

Options:
  --user              Install to user skill directories. Default.
  --project [PATH]    Install to a repository/project directory. Default path: .
  --claude-only       Install only the Claude Code skill.
  --codex-only        Install only the Codex skill.
  --repo OWNER/REPO   Override GitHub repository. Default: tvmaly/retrieval-ready-markdown-skills
  --ref REF           Override git ref/branch. Default: main
  -h, --help          Show this help.

Examples:
  curl -fsSL https://raw.githubusercontent.com/tvmaly/retrieval-ready-markdown-skills/main/install.sh | bash
  curl -fsSL https://raw.githubusercontent.com/tvmaly/retrieval-ready-markdown-skills/main/install.sh | bash -s -- --project .
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --user)
      SCOPE="user"
      shift
      ;;
    --project)
      SCOPE="project"
      if [[ $# -gt 1 && "${2:-}" != --* ]]; then
        PROJECT_DIR="$2"
        shift 2
      else
        PROJECT_DIR="."
        shift
      fi
      ;;
    --claude-only)
      INSTALL_CLAUDE=1
      INSTALL_CODEX=0
      shift
      ;;
    --codex-only)
      INSTALL_CLAUDE=0
      INSTALL_CODEX=1
      shift
      ;;
    --repo)
      REPO="$2"
      shift 2
      ;;
    --ref)
      REF="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
  }
}

need curl
need tar
need mktemp
need cp

TMP_DIR="$(mktemp -d)"
cleanup() { rm -rf "$TMP_DIR"; }
trap cleanup EXIT

ARCHIVE_URL="https://github.com/${REPO}/archive/refs/heads/${REF}.tar.gz"
echo "Downloading ${REPO}@${REF}..."
curl -fsSL "$ARCHIVE_URL" | tar -xz -C "$TMP_DIR"

REPO_NAME="${REPO##*/}"
SRC_ROOT="${TMP_DIR}/${REPO_NAME}-${REF}"

if [[ ! -d "$SRC_ROOT" ]]; then
  echo "Could not find extracted repo at $SRC_ROOT" >&2
  exit 1
fi

CLAUDE_SRC="$SRC_ROOT/skills/claude-code/dci-markdown-retrieval-writer"
CODEX_SRC="$SRC_ROOT/skills/codex/dci-markdown-retrieval-writer"

if [[ "$SCOPE" == "project" ]]; then
  PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
  CLAUDE_DEST="$PROJECT_DIR/.claude/skills/dci-markdown-retrieval-writer"
  CODEX_DEST="$PROJECT_DIR/.agents/skills/dci-markdown-retrieval-writer"
else
  CLAUDE_DEST="$HOME/.claude/skills/dci-markdown-retrieval-writer"
  CODEX_DEST="$HOME/.agents/skills/dci-markdown-retrieval-writer"
fi

install_skill() {
  local src="$1"
  local dest="$2"
  local label="$3"

  if [[ ! -d "$src" ]]; then
    echo "Missing source skill: $src" >&2
    exit 1
  fi

  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  cp -R "$src" "$dest"
  echo "Installed ${label}: ${dest}"
}

if [[ "$INSTALL_CLAUDE" == "1" ]]; then
  install_skill "$CLAUDE_SRC" "$CLAUDE_DEST" "Claude Code skill"
fi

if [[ "$INSTALL_CODEX" == "1" ]]; then
  install_skill "$CODEX_SRC" "$CODEX_DEST" "Codex skill"
fi

echo "Done. Restart your agent if it does not pick up the skill automatically."
