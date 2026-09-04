# Copyright (c) 2026, Printechs and contributors
from frappe.model.document import Document

from printechs_digital.utils.website_assets import localize_doc_fields, validate_doc_fields


class WebsiteAboutSettings(Document):
	def before_validate(self):
		localize_doc_fields(
			self,
			[("company_profile_file", "company-profile")],
		)

	def validate(self):
		validate_doc_fields(self, [("company_profile_file", "Company Profile PDF")])
