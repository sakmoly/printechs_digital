# Copyright (c) 2026, Printechs and contributors

from printechs_digital.printechs_digital.doctype.website_product.website_product import slugify
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cstr


class WebsiteSolution(Document):
	def autoname(self):
		self.name = slugify(self.slug or self.solution_name)

	def before_validate(self):
		if not self.slug:
			self.slug = slugify(self.solution_name)
		if not self.image_alt:
			self.image_alt = self.solution_name
		if not self.href:
			self.href = f"/solutions/{self.slug}"

	def validate(self):
		if not self.slug:
			frappe.throw(_("Slug is required"))
		self.slug = slugify(self.slug)
		filters = {"slug": self.slug}
		if self.name:
			filters["name"] = ("!=", self.name)
		if frappe.db.exists("Website Solution", filters):
			frappe.throw(_("Website Solution with slug {0} already exists").format(self.slug))

		if cstr(self.image).startswith(("http://", "https://")) and "/files/" not in cstr(self.image):
			frappe.throw(_("Upload the solution image as a file on this site."))
