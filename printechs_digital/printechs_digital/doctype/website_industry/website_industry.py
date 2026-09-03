# Copyright (c) 2026, Printechs and contributors

from printechs_digital.printechs_digital.doctype.website_product.website_product import slugify
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cstr


class WebsiteIndustry(Document):
	def autoname(self):
		self.name = slugify(self.slug or self.industry_name)

	def before_validate(self):
		if not self.slug:
			self.slug = slugify(self.industry_name)
		if not self.image_alt:
			self.image_alt = self.industry_name

	def validate(self):
		if not self.slug:
			frappe.throw(_("Slug is required"))
		self.slug = slugify(self.slug)
		filters = {"slug": self.slug}
		if self.name:
			filters["name"] = ("!=", self.name)
		if frappe.db.exists("Website Industry", filters):
			frappe.throw(_("Website Industry with slug {0} already exists").format(self.slug))

		if cstr(self.image).startswith(("http://", "https://")) and "/files/" not in cstr(self.image):
			frappe.throw(_("Upload the industry image as a file on this site."))
