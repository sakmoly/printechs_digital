# Copyright (c) 2026, Printechs and contributors
"""Fill Website Brand record for ERPNext."""

import frappe

SLUG = "erpnext"
BRAND = "ERPNext"


def fill_website_brand_erpnext():
	if not frappe.db.exists("Brand", BRAND):
		frappe.throw(f"ERP Brand {BRAND} was not found")

	if not frappe.db.exists("Website Brand", SLUG):
		frappe.throw(f"Website Brand {SLUG} was not found — create it in Desk first")

	doc = frappe.get_doc("Website Brand", SLUG)
	doc.brand = BRAND
	doc.display_name = "ERPNext"
	doc.slug = SLUG
	doc.published = 1
	doc.sort_order = 7
	doc.logo = doc.logo or "/files/ERPNext.png"
	doc.summary = (
		"Open-source ERP for finance, inventory, manufacturing, and service operations — "
		"implemented, customised, and supported by Printechs across Saudi Arabia, "
		"including ZATCA e-invoicing and integration with POS and warehouse systems."
	)
	doc.meta_title = "ERPNext | Printechs Brands"
	doc.meta_description = (
		"ERPNext implementation, customisation, and support from Printechs in Saudi Arabia. "
		"Unified finance, inventory, manufacturing, and ZATCA e-invoicing with local training "
		"and integration to POS, WMS, and retail systems."
	)
	doc.save(ignore_permissions=True)

	# Link the published ERPNext software product to this brand for /brands/erpnext listing.
	if frappe.db.exists("Website Product", "erpnext"):
		product = frappe.get_doc("Website Product", "erpnext")
		if product.brand != BRAND:
			product.brand = BRAND
			product.card_brand_label = BRAND
			product.save(ignore_permissions=True)

	frappe.db.commit()
	frappe.msgprint(f"Updated Website Brand: {doc.name}")
	return doc.name


if __name__ == "__main__":
	fill_website_brand_erpnext()
