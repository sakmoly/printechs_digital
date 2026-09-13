# Copyright (c) 2026, Printechs and contributors
"""Desk metadata for the ERP & Business Automation solution page.

Software slugs only. Does not use set_related() and does not change featured products.
"""

import frappe

SOFTWARE_SLUGS = [
	"erpnext",
	"modern-pos",
	"warehouse-management-system",
	"zatca-integration",
]


def fill_erp_business_automation_solution() -> dict:
	name = frappe.db.get_value("Website Solution", {"slug": "erp-business-automation"}, "name")
	if not name:
		frappe.throw("Website Solution erp-business-automation is missing")

	existing = {
		row.slug
		for row in frappe.get_all(
			"Website Product",
			filters={"slug": ["in", SOFTWARE_SLUGS], "published": 1},
			fields=["slug"],
		)
	}
	slugs = [slug for slug in SOFTWARE_SLUGS if slug in existing]

	doc = frappe.get_doc("Website Solution", name)
	doc.published = 1
	doc.show_on_list = 1
	doc.solution_name = "ERP & Business Automation"
	doc.card_title = "ERP & Business Automation"
	doc.card_summary = (
		"ERPNext, Modern POS, warehouse management and ZATCA e-invoicing "
		"for companies in Saudi Arabia."
	)
	doc.summary = (
		"Business systems that unify finance, inventory, the store and the warehouse."
	)
	doc.href = "/solutions/erp-business-automation"
	doc.image = "/files/featured-erp-business-automation.jpg"
	doc.image_alt = "Office laptop showing a business operations dashboard"
	doc.related_product_slugs = ""
	doc.related_software_slugs = "\n".join(slugs)
	doc.meta_title = "ERP & Business Automation | Printechs"
	doc.meta_description = (
		"ERPNext, Modern POS, warehouse management and ZATCA e-invoicing "
		"for companies in Saudi Arabia."
	)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return {"status": "updated", "slug": "erp-business-automation", "software": slugs}
