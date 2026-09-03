# Copyright (c) 2026, Printechs and contributors

from pathlib import Path
from shutil import copy2

FRONTEND_IMAGES = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")


def copy_public_image(relative_src: str, dest_name: str | None = None) -> str:
	"""Copy a frontend public image into site files. Falls back to /images/ if missing."""
	src = FRONTEND_IMAGES / relative_src
	name = dest_name or Path(relative_src).name
	target = SITE_FILES / name
	if src.exists() and not target.exists():
		copy2(src, target)
	if target.exists():
		return f"/files/{name}"
	return f"/images/{relative_src}"
