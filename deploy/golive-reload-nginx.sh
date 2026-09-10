#!/bin/bash
# Run as root: sudo /home/erpnext/frappe-bench/apps/printechs_digital/deploy/golive-reload-nginx.sh
set -euo pipefail
nginx -t
systemctl reload nginx
echo "nginx reloaded"
