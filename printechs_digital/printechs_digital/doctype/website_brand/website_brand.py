# Copyright (c) 2026, Printechs and contributors

import re

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cstr


def slugify(value: str) -> str:
	value = cstr(value).lower().strip()
	value = re.sub(r"[^\w\s-]", "", value)
	value = re.sub(r"[\s_]+", "-", value)
	value = re.sub(r"-+", "-", value)
	return value.strip("-")


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
