#!/usr/bin/env bash
# Sync the live Next.js frontend into this repo before commit/push.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LIVE_DIR="${LIVE_FRONTEND_DIR:-/home/erpnext/frappe-bench/frontend/printechs-web}"
REPO_DIR="${REPO_FRONTEND_DIR:-${REPO_ROOT}/frontend/printechs-web}"
DRY_RUN=0

usage() {
	cat <<EOF
Usage: $(basename "$0") [--dry-run]

Copy the live frontend into frontend/printechs-web/ in this repo.

Environment overrides:
  LIVE_FRONTEND_DIR   Source directory (default: ${LIVE_DIR})
  REPO_FRONTEND_DIR   Target directory (default: ${REPO_DIR})
EOF
}

while [[ $# -gt 0 ]]; do
	case "$1" in
	--dry-run)
		DRY_RUN=1
		shift
		;;
	-h | --help)
		usage
		exit 0
		;;
	*)
		echo "Unknown option: $1" >&2
		usage
		exit 1
		;;
	esac
done

if [[ ! -d "${LIVE_DIR}" ]]; then
	echo "Live frontend not found: ${LIVE_DIR}" >&2
	exit 1
fi

mkdir -p "${REPO_DIR}"

RSYNC_FLAGS=(-av --delete
	--exclude node_modules
	--exclude .next
	--exclude .git
	--exclude tsconfig.tsbuildinfo
)

if [[ "${DRY_RUN}" -eq 1 ]]; then
	RSYNC_FLAGS=(--dry-run "${RSYNC_FLAGS[@]}")
	echo "Dry run: ${LIVE_DIR}/ -> ${REPO_DIR}/"
else
	echo "Syncing: ${LIVE_DIR}/ -> ${REPO_DIR}/"
fi

rsync "${RSYNC_FLAGS[@]}" "${LIVE_DIR}/" "${REPO_DIR}/"

if [[ "${DRY_RUN}" -eq 1 ]]; then
	echo "Dry run complete. Re-run without --dry-run to apply changes."
else
	echo "Frontend synced. Commit from ${REPO_ROOT}:"
	echo "  git add frontend/printechs-web"
	echo "  git commit -m \"Sync frontend\""
	echo "  git push origin develop"
fi
