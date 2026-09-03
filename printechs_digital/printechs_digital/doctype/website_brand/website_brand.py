# Copyright (c) 2026, Printechs and contributors

import re
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cstr, get_files_path

ALLOWED_LOGO_HOSTS = ("printechs.com", "demo.printechs.com")


def slugify(value: str) -> str:
	value = cstr(value).lower().strip()
	value = re.sub(r"[^\w\s-]", "", value)
	value = re.sub(r"[\s_]+", "-", value)
	value = re.sub(r"-+", "-", value)
	return value.strip("-")


def is_local_logo(path: str | None) -> bool:
	value = cstr(path)
	if not value:
		return False
	if value.startswith("/files/"):
		return True
	if value.startswith(("http://", "https://")):
		host = (urlparse(value).hostname or "").lower()
		return host in ALLOWED_LOGO_HOSTS and "/files/" in value
	return False


def localize_remote_logo(path: str, slug: str) -> str:
	"""Copy a remote logo into public /files/ so Next.js can serve it."""
	request = Request(
		path,
		headers={
			"User-Agent": (
				"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
				"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
			)
		},
	)
	suffix = Path(urlparse(path).path).suffix.lower() or ".png"
	if suffix not in {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"}:
		suffix = ".png"
	filename = f"brand-{slugify(slug)}{suffix}"
	target = Path(get_files_path(filename, is_private=False))
	try:
		with urlopen(request, timeout=30) as response:
			data = response.read()
	except Exception:
		frappe.throw(
			_(
				"This logo URL cannot be used on the website. "
				"Upload a PNG or SVG file instead of pasting an external link."
			)
		)
	if not data:
		frappe.throw(_("The logo file is empty. Upload a local image file."))
	target.write_bytes(data)
	return f"/files/{filename}"


class WebsiteBrand(Document):
	def autoname(self):
		self.name = slugify(self.slug or self.brand)

	def before_validate(self):
		if self.brand and not self.display_name:
			self.display_name = self.brand
		if not self.slug:
			self.slug = slugify(self.display_name or self.brand)
		if not self.logo and self.brand:
			self.logo = frappe.db.get_value("Brand", self.brand, "image")
		if self.logo and not is_local_logo(self.logo):
			if self.logo.startswith(("http://", "https://")):
				self.logo = localize_remote_logo(self.logo, self.slug or self.brand or "brand")

	def validate(self):
		if not self.slug:
			frappe.throw(_("Slug is required"))
		self.slug = slugify(self.slug)
		if not self.slug:
			frappe.throw(_("Slug is invalid"))

		filters = {"slug": self.slug}
		if self.name:
			filters["name"] = ("!=", self.name)
		if frappe.db.exists("Website Brand", filters):
			frappe.throw(_("Website Brand with slug {0} already exists").format(self.slug))

		if self.brand:
			existing = frappe.db.get_value(
				"Website Brand",
				{"brand": self.brand, "name": ("!=", self.name or "")},
				"name",
			)
			if existing:
				frappe.throw(
					_("Website Brand {0} is already linked to Brand {1}").format(existing, self.brand)
				)

		if self.logo and not is_local_logo(self.logo):
			frappe.throw(
				_(
					"Upload the logo as a file on this site (PNG or SVG). "
					"External image links are not shown on the website."
				)
			)
