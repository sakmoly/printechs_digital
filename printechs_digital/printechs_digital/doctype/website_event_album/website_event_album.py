# Copyright (c) 2026, Printechs and contributors

import re

import frappe
from frappe import _
from frappe.model.document import Document

from printechs_digital.utils.website_assets import (
	localize_child_table,
	localize_doc_fields,
	validate_child_table,
	validate_doc_fields,
)


def slugify(value: str) -> str:
	value = frappe.utils.cstr(value).lower().strip()
	value = re.sub(r"[^\w\s-]", "", value)
	value = re.sub(r"[\s_]+", "-", value)
	value = re.sub(r"-+", "-", value)
	return value.strip("-")


class WebsiteEventAlbum(Document):
	def autoname(self):
		if self.slug:
			self.name = slugify(self.slug)
		else:
			frappe.throw(_("Slug is required to name this Website Event Album"))

	def before_validate(self):
		if not self.cover_image_alt:
			self.cover_image_alt = self.title

		slug = self.slug or slugify(self.title or "event")
		localize_doc_fields(self, [("cover_image", f"event-{slug}-cover")])
		localize_child_table(
			self,
			"gallery",
			"image",
			lambda row, idx: f"event-{slug}-gallery-{idx}",
		)

	def validate(self):
		if not self.slug:
			self.slug = slugify(self.title)

		validate_doc_fields(self, [("cover_image", "Cover Image")])
		validate_child_table(self, "gallery", "image", "Gallery Image")

		if frappe.db.exists("Website Event Album", {"slug": self.slug, "name": ["!=", self.name]}):
			frappe.throw(_("Website Event Album with slug {0} already exists").format(self.slug))
