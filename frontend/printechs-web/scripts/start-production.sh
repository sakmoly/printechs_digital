#!/bin/bash
# Auto-start helper for Printechs Next.js website (demo /newwebsite)
set -euo pipefail

APP_DIR="/home/erpnext/frappe-bench/frontend/printechs-web"
NODE_BIN="/home/erpnext/.nvm/versions/node/v20.20.2/bin"

export PATH="${NODE_BIN}:${PATH}"
export NODE_ENV=production
export PORT=3000
export HOSTNAME=127.0.0.1

cd "${APP_DIR}"

if [ ! -d "${APP_DIR}/.next" ]; then
  echo "Missing .next build. Run: cd ${APP_DIR} && npm run build" >&2
  exit 1
fi

exec "${NODE_BIN}/node" ./node_modules/next/dist/bin/next start -H 127.0.0.1 -p 3000
