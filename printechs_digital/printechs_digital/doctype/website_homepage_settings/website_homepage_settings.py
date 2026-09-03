# Copyright (c) 2026, Printechs and contributors

from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cstr, get_files_path

ALLOWED_HOSTS = ("printechs.com", "demo.printechs.com")


def is_local_asset(path: str | None) -> bool:
	value = cstr(path)
	if not value:
		return True
	if value.startswith(("/files/", "/images/", "/private/files/")):
		return True
	if value.startswith(("http://", "https://")):
		host = (urlparse(value).hostname or "").lower()
		return host in ALLOWED_HOSTS and ("/files/" in value or "/images/" in value)
	return False


def localize_remote_file(path: str, filename: str) -> str:
	request = Request(
		path,
		headers={
			"User-Agent": (
				"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
				"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
			)
		},
	)
	suffix = Path(urlparse(path).path).suffix.lower() or Path(filename).suffix or ".png"
	if suffix not in {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".mp4", ".webm"}:
		suffix = Path(filename).suffix or ".png"
	target_name = f"{Path(filename).stem}{suffix}"
	target = Path(get_files_path(target_name, is_private=False))
	try:
		with urlopen(request, timeout=30) as response:
			data = response.read()
	except Exception:
		frappe.throw(
			_("This file URL cannot be used on the website. Upload the file instead of pasting an external link.")
		)
	if not data:
		frappe.throw(_("The uploaded file is empty."))
	target.write_bytes(data)
	return f"/files/{target_name}"


class WebsiteHomepageSettings(Document):
	def before_validate(self):
		for field, filename in (
			("hero_image", "home-hero"),
			("hero_video_poster", "home-hero-poster"),
			("video_poster", "home-video-poster"),
		):
			value = cstr(self.get(field))
			if value and not is_local_asset(value) and value.startswith(("http://", "https://")):
				self.set(field, localize_remote_file(value, filename))

		for idx, row in enumerate(self.get("divisions") or [], start=1):
			value = cstr(row.image)
			if value and not is_local_asset(value) and value.startswith(("http://", "https://")):
				row.image = localize_remote_file(value, f"home-division-{idx}")
			if not row.image_alt:
				row.image_alt = row.title

		for idx, row in enumerate(self.get("extra_blocks") or [], start=1):
			value = cstr(row.image)
			if value and not is_local_asset(value) and value.startswith(("http://", "https://")):
				row.image = localize_remote_file(value, f"home-extra-block-{idx}")
			if row.image and not row.image_alt:
				row.image_alt = row.heading

	def validate(self):
		if self.hero_media_kind == "Image" and not self.hero_image:
			frappe.throw(_("Hero Image is required when Hero Media is Image"))
		if self.hero_media_kind == "Hosted Video" and not self.hero_video:
			frappe.throw(_("Hero Video is required when Hero Media is Hosted Video"))

		for field in ("hero_image", "hero_video_poster", "video_poster"):
			value = cstr(self.get(field))
			if value and not is_local_asset(value):
				frappe.throw(
					_("Upload {0} as a file on this site. External image links are not shown on the website.").format(
						_(self.meta.get_label(field))
					)
				)

		for row in self.get("divisions") or []:
			if cstr(row.image) and not is_local_asset(row.image):
				frappe.throw(_("Upload each division image as a file on this site."))

		for row in self.get("extra_blocks") or []:
			if cstr(row.image) and not is_local_asset(row.image):
				frappe.throw(_("Upload each extra block image as a file on this site."))
