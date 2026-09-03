# Copyright (c) 2026, Printechs and contributors
"""Create or update the ZATCA Integration Website Product."""

from pathlib import Path
from shutil import copy2

import frappe

SOFTWARE_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/software")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")


def copy_image(source_dir: Path, filename: str) -> str:
	source = source_dir / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def copy_software_image(filename: str) -> str:
	return copy_image(SOFTWARE_DIR, filename)


def copy_industry_image(filename: str) -> str:
	return copy_image(INDUSTRY_DIR, filename)


def published_name(slug: str) -> str | None:
	return frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "name")


def get_or_create_zatca():
	name = frappe.db.get_value("Website Product", {"slug": "zatca-integration"}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "ZATCA Integration"
	doc.display_name = "ZATCA Integration"
	doc.slug = "zatca-integration"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "Compliance Software"
	doc.short_description = (
		"e-Invoicing compliance integration aligned with Saudi ZATCA requirements."
	)
	doc.long_description = "<p>ZATCA Integration</p>"
	doc.hero_image = copy_software_image("software-zatca-integration.jpg")
	doc.hero_image_alt = (
		"ZATCA e-invoicing compliance dashboard across desktop, laptop and mobile"
	)
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_zatca():
	doc = get_or_create_zatca()

	hero = copy_software_image("software-zatca-integration.jpg")
	erpnext_image = copy_software_image("software-erpnext.jpg")
	pos_image = copy_software_image("software-modern-pos.jpg")
	wms_image = copy_software_image("software-warehouse-management-system.jpg")

	doc.website_product_name = "ZATCA Integration"
	doc.display_name = "ZATCA Integration"
	doc.slug = "zatca-integration"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.brand = "Printechs"
	doc.category = "Compliance Software"
	doc.subcategory = "e-Invoicing"
	doc.category_label = "SAUDI E-INVOICING COMPLIANCE"
	doc.tagline = "e-Invoicing compliance integration aligned with Saudi ZATCA requirements"
	doc.short_description = (
		"Connect ERP, POS, and billing systems to ZATCA Phase 2 — generate, sign, submit, "
		"and archive e-invoices with audit-ready workflows."
	)
	doc.long_description = (
		"<p>Printechs ZATCA Integration helps businesses in Saudi Arabia meet Phase 2 "
		"e-invoicing requirements without disrupting day-to-day sales and finance work. "
		"Invoices are generated from ERPNext, Modern POS, or other billing systems, then "
		"signed, submitted, and tracked against ZATCA clearance and reporting rules.</p>"
		"<p>Printechs configures onboarding, XML and QR generation, device and unit mapping, "
		"and exception handling — with local support for compliance validation, go-live, "
		"and ongoing updates as ZATCA requirements evolve.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"ZATCA e-invoicing compliance dashboard across desktop, laptop and mobile"
	)
	doc.hero_trust_chips = "Compliance workflows\nERP connectivity\nAudit readiness"
	doc.show_demo_cta = 1
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = "e-Invoicing that stays aligned with ZATCA"
	doc.visual_story_heading = "See ZATCA Integration in action"
	doc.card_title = "ZATCA Integration"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"e-Invoicing compliance integration aligned with Saudi ZATCA requirements."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Get your invoicing ready for ZATCA Phase 2"
	doc.final_cta_description = (
		"Book a demo with Printechs to review e-invoice generation, ERP and POS connectivity, "
		"and compliance validation for your Saudi operation."
	)
	doc.meta_title = "ZATCA Integration | Printechs Software"
	doc.meta_description = "ZATCA e-invoicing integration services from Printechs."
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "zatca",
				"title": "Phase 2 ready",
				"description": "Clearance and reporting workflows aligned with current ZATCA rules.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "ERP & POS connected",
				"description": "Invoices flow from ERPNext, Modern POS, and other billing systems.",
				"sort_order": 2,
			},
			{
				"icon": "shield",
				"title": "Signed & submitted",
				"description": "XML generation, cryptographic signing, QR codes, and submission status.",
				"sort_order": 3,
			},
			{
				"icon": "report",
				"title": "Audit ready",
				"description": "Archived invoices, responses, and exception logs for compliance review.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Invoices",
				"image": hero,
				"image_alt": "ZATCA e-invoicing compliance dashboard",
				"caption": "Generate, sign, and track e-invoices from a single compliance view.",
				"sort_order": 1,
			},
			{
				"label": "ERP",
				"image": erpnext_image,
				"image_alt": "ERPNext finance dashboard connected to ZATCA",
				"caption": "Sales invoices from ERPNext submitted automatically to ZATCA.",
				"sort_order": 2,
			},
			{
				"label": "POS",
				"image": pos_image,
				"image_alt": "Modern POS checkout with ZATCA invoicing",
				"caption": "Register invoices issued with QR codes and Phase 2 reporting.",
				"sort_order": 3,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "zatca",
				"title": "Standard",
				"description": "ZATCA Phase 2 e-invoicing · clearance and reporting",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "Source systems",
				"description": "ERPNext · Modern POS · other billing APIs",
				"sort_order": 2,
			},
			{
				"icon": "shield",
				"title": "Security",
				"description": "Invoice signing, device onboarding, and access control",
				"sort_order": 3,
			},
			{
				"icon": "cloud",
				"title": "Deployment",
				"description": "Cloud or on-premise · connected to ZATCA endpoints",
				"sort_order": 4,
			},
			{
				"icon": "report",
				"title": "Languages",
				"description": "English and Arabic invoice and interface support",
				"sort_order": 5,
			},
			{
				"icon": "connectivity",
				"title": "Resilience",
				"description": "Retry, queue, and exception handling when submission fails",
				"sort_order": 6,
			},
		],
	)

	capability_rows = []
	modules = [
		("Onboarding", "install", [
			"Taxpayer and device registration support",
			"Unit and branch mapping",
			"Sandbox testing before production",
		]),
		("Invoice generation", "zatca", [
			"Standard and simplified tax invoices",
			"Credit and debit notes",
			"QR code and XML output",
		]),
		("Submission", "cloud", [
			"Clearance for B2B invoices",
			"Reporting for B2C invoices",
			"Status tracking and acknowledgements",
		]),
		("Exceptions", "shield", [
			"Failed-submission queues",
			"Validation error handling",
			"Manual retry and audit notes",
		]),
		("Archive", "report", [
			"Invoice and response storage",
			"Search by customer, date, or status",
			"Export for accountants and auditors",
		]),
		("Integrations", "integration", [
			"ERPNext native invoice sync",
			"Modern POS register invoicing",
			"API layer for other billing systems",
		]),
	]
	sort_order = 1
	for title, icon, items in modules:
		for item_text in items:
			capability_rows.append({
				"module_title": title,
				"icon": icon,
				"item_text": item_text,
				"sort_order": sort_order,
			})
			sort_order += 1
	doc.set("capability_items", capability_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Retail",
				"description": "Store and chain invoicing from POS with Phase 2 QR and reporting.",
				"image": copy_industry_image("industry-retail.jpg"),
				"image_alt": "Retail invoicing operations",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Food & beverage",
				"description": "High-volume B2C invoices from restaurants and F&B brands.",
				"image": copy_industry_image("industry-food-beverage.jpg"),
				"image_alt": "Food and beverage retail invoicing",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Pharmaceutical",
				"description": "B2B clearance invoices with batch and credit-note control.",
				"image": copy_industry_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmaceutical billing operations",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Fashion retail",
				"description": "Multi-store invoicing connected to ERP and loyalty systems.",
				"image": copy_industry_image("industry-fashion.jpg"),
				"image_alt": "Fashion retail checkout and invoicing",
				"industry_link": "fashion",
				"sort_order": 4,
			},
		],
	)

	pos_name = published_name("modern-pos")
	erp_name = published_name("erpnext")
	wms_name = published_name("warehouse-management-system")
	doc.set(
		"ecosystem_items",
		[
			{
				"related_website_product": erp_name,
				"display_name_override": "ERPNext",
				"summary_override": "Finance & invoices",
				"href": "/software/erpnext",
				"image": erpnext_image,
				"sort_order": 1,
			},
			{
				"related_website_product": pos_name,
				"display_name_override": "Modern POS",
				"summary_override": "Register invoices",
				"href": "/software/modern-pos",
				"image": pos_image,
				"sort_order": 2,
			},
			{
				"related_website_product": wms_name,
				"display_name_override": "Warehouse Management",
				"summary_override": "Fulfilment documents",
				"href": "/software/warehouse-management-system",
				"image": wms_image,
				"sort_order": 3,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Compliance discovery",
				"description": "Invoice types, branches, and current billing-system review.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "System integration",
				"description": "ERPNext, POS, and API connectivity for invoice flow.",
				"sort_order": 2,
			},
			{
				"icon": "zatca",
				"title": "Validation",
				"description": "Sandbox tests, production onboarding, and compliance checks.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Ongoing support",
				"description": "Monitoring, ZATCA updates, and finance-team training.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set("package_contents", [])
	doc.set("full_specifications", [])

	doc.set(
		"related_products",
		[
			{
				"related_website_product": erp_name,
				"display_name_override": "ERPNext",
				"summary_override": "Integrated ERP for finance, inventory, and operations",
				"href": "/software/erpnext",
				"image": erpnext_image,
				"sort_order": 1,
			},
			{
				"related_website_product": pos_name,
				"display_name_override": "Modern POS",
				"summary_override": "Retail checkout with ZATCA-ready invoicing",
				"href": "/software/modern-pos",
				"image": pos_image,
				"sort_order": 2,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
