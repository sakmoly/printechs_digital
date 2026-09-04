# Copyright (c) 2026, Printechs and contributors
"""Create or update the ERPNext Website Product."""

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


def get_or_create_erpnext():
	name = frappe.db.get_value("Website Product", {"slug": "erpnext"}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "ERPNext"
	doc.display_name = "ERPNext"
	doc.slug = "erpnext"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "ERP Software"
	doc.short_description = (
		"Integrated ERP for finance, inventory, manufacturing and service operations."
	)
	doc.long_description = "<p>ERPNext</p>"
	doc.hero_image = copy_software_image("software-erpnext.jpg")
	doc.hero_image_alt = "ERPNext business dashboard with sales, inventory and finance metrics"
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_erpnext():
	doc = get_or_create_erpnext()

	hero = copy_software_image("software-erpnext.jpg")
	wms_image = copy_software_image("software-warehouse-management-system.jpg")
	pos_image = copy_software_image("software-modern-pos.jpg")
	zatca_image = copy_software_image("software-zatca-integration.jpg")

	doc.website_product_name = "ERPNext"
	doc.display_name = "ERPNext"
	doc.slug = "erpnext"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.brand = "Printechs"
	doc.category = "ERP Software"
	doc.subcategory = "Enterprise Resource Planning"
	doc.category_label = "ENTERPRISE RESOURCE PLANNING"
	doc.tagline = "Integrated ERP for finance, inventory, manufacturing and service operations"
	doc.short_description = (
		"One operational system for accounting, stock, sales, purchasing, and manufacturing — "
		"implemented and supported by Printechs in Saudi Arabia, with ZATCA e-invoicing."
	)
	doc.long_description = (
		"<p>ERPNext is the business system Printechs deploys for companies that need finance, "
		"inventory, and operations in one place. Teams share a single source of truth for "
		"orders, stock, invoices, and production — instead of disconnected spreadsheets and "
		"standalone apps.</p>"
		"<p>Printechs implements, customises, and supports ERPNext across Saudi Arabia, "
		"including ZATCA Phase 2 e-invoicing, POS and WMS connectivity, data migration, "
		"and local training in English and Arabic.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "ERPNext business dashboard with sales, inventory and finance metrics"
	doc.hero_trust_chips = "Unified operations\nLocal expertise\nZATCA e-invoicing ready"
	doc.show_demo_cta = 1
	doc.configure_on_demo = 1
	doc.set(
		"demo_options",
		[
			{
				"group_label": "Your environment",
				"label": "Company size",
				"option_type": "Select",
				"required": 1,
				"sort_order": 1,
				"choices": "1–10 users\n11–50 users\n51–200 users\n200+ users",
			},
			{
				"group_label": "Your environment",
				"label": "Deployment preference",
				"option_type": "Select",
				"required": 1,
				"sort_order": 2,
				"choices": "Cloud SaaS\nOn-premise\nNot sure yet",
			},
			{
				"group_label": "Modules to demo",
				"label": "Modules to demo",
				"option_type": "Checkbox",
				"required": 1,
				"sort_order": 3,
				"choices": "Finance & Accounting\nInventory & Warehousing\nSales & CRM\nPurchasing\nManufacturing\nHR & Payroll\nProjects",
			},
			{
				"group_label": "Integrations",
				"label": "Integrations needed",
				"option_type": "Checkbox",
				"required": 0,
				"sort_order": 4,
				"choices": "Modern POS\nWMS\nZATCA e-invoicing\nE-commerce\nBanking",
			},
			{
				"group_label": "Current setup",
				"label": "Current system",
				"option_type": "Select",
				"required": 1,
				"sort_order": 5,
				"choices": "Spreadsheets / manual processes\nBasic accounting software\nOther ERP\nNew implementation",
			},
		],
	)
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = "Finance, inventory, and operations in one system"
	doc.visual_story_heading = "See ERPNext in action"
	doc.card_title = "ERPNext"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Integrated ERP for finance, inventory, manufacturing and service operations."
	)
	doc.card_image = hero
	doc.final_cta_heading = "See ERPNext in your business environment"
	doc.final_cta_description = (
		"Book a demo with Printechs to explore finance, inventory, ZATCA compliance, "
		"and integration with POS and warehouse systems."
	)
	doc.meta_title = "ERPNext | Printechs Software"
	doc.meta_description = "ERPNext implementation and support with Printechs."
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "integration",
				"title": "Unified operations",
				"description": "Finance, inventory, sales, and purchasing share one live data model.",
				"sort_order": 1,
			},
			{
				"icon": "inventory",
				"title": "Stock & fulfilment",
				"description": "Real-time inventory, warehouses, and order status across locations.",
				"sort_order": 2,
			},
			{
				"icon": "zatca",
				"title": "ZATCA compliance",
				"description": "Phase 2 e-invoicing configured and validated for Saudi operations.",
				"sort_order": 3,
			},
			{
				"icon": "cloud",
				"title": "Local expertise",
				"description": "Printechs implements, trains, and supports ERPNext in Saudi Arabia.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Finance",
				"image": hero,
				"image_alt": "ERPNext business dashboard with sales and finance metrics",
				"caption": "Accounts, invoices, and management reports in one dashboard.",
				"sort_order": 1,
			},
			{
				"label": "Inventory",
				"image": wms_image,
				"image_alt": "Inventory and warehouse operations connected to ERPNext",
				"caption": "Live stock, warehouses, and fulfilment linked to sales and purchasing.",
				"sort_order": 2,
			},
			{
				"label": "ZATCA",
				"image": zatca_image,
				"image_alt": "ZATCA e-invoicing compliance dashboard",
				"caption": "Automated ZATCA Phase 2 e-invoicing from ERP documents.",
				"sort_order": 3,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "cloud",
				"title": "Deployment",
				"description": "Cloud SaaS or on-premise · multi-company ready",
				"sort_order": 1,
			},
			{
				"icon": "zatca",
				"title": "Compliance",
				"description": "ZATCA Phase 2 e-invoicing · audit-ready workflows",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "Integrations",
				"description": "POS, WMS, e-commerce, and API connectivity",
				"sort_order": 3,
			},
			{
				"icon": "report",
				"title": "Languages",
				"description": "English and Arabic interface support",
				"sort_order": 4,
			},
			{
				"icon": "store",
				"title": "Modules",
				"description": "Accounting · Stock · Selling · Buying · Manufacturing · HR",
				"sort_order": 5,
			},
			{
				"icon": "device",
				"title": "Access",
				"description": "Web, desktop, and mobile workflows for office and floor teams",
				"sort_order": 6,
			},
		],
	)

	capability_rows = []
	modules = [
		("Finance", "report", [
			"General ledger, receivables, and payables",
			"VAT and ZATCA e-invoice submission",
			"Budgets, costing, and management reports",
		]),
		("Inventory", "inventory", [
			"Multi-warehouse stock and valuations",
			"Serial, batch, and lot tracking",
			"Reorder rules and stock reconciliation",
		]),
		("Sales & Purchase", "checkout", [
			"Quotations, sales orders, and invoices",
			"Purchase orders and supplier management",
			"Pricing rules and customer credit control",
		]),
		("Manufacturing", "print", [
			"BOM, work orders, and job cards",
			"Material consumption and finished goods",
			"Production planning and subcontracting",
		]),
		("People & Projects", "loyalty", [
			"HR, payroll, and leave management",
			"Projects, timesheets, and billing",
			"Role-based permissions and approvals",
		]),
		("Integrations", "integration", [
			"Modern POS sales and stock sync",
			"WMS inbound and outbound postings",
			"API layer for e-commerce and banks",
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
				"description": "Multi-store inventory, purchasing, and finance connected to POS.",
				"image": copy_industry_image("industry-retail.jpg"),
				"image_alt": "Retail operations supported by ERPNext",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Warehouse & logistics",
				"description": "Central stock control with WMS and handheld warehouse workflows.",
				"image": copy_industry_image("industry-warehouse-logistics.jpg"),
				"image_alt": "Warehouse logistics connected to ERPNext",
				"industry_link": "warehouse-logistics",
				"sort_order": 2,
			},
			{
				"title": "Manufacturing",
				"description": "BOMs, work orders, and material planning for production plants.",
				"image": copy_industry_image("industry-packaging.jpg"),
				"image_alt": "Manufacturing and packaging operations",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Food & beverage",
				"description": "Batch tracking, costing, and compliance for F&B businesses.",
				"image": copy_industry_image("industry-food-beverage.jpg"),
				"image_alt": "Food and beverage production",
				"industry_link": "food-beverage",
				"sort_order": 4,
			},
		],
	)

	pos_name = published_name("modern-pos")
	wms_name = published_name("warehouse-management-system")
	doc.set(
		"ecosystem_items",
		[
			{
				"related_website_product": pos_name,
				"display_name_override": "Modern POS",
				"summary_override": "Store checkout",
				"href": "/software/modern-pos",
				"image": pos_image,
				"sort_order": 1,
			},
			{
				"related_website_product": wms_name,
				"display_name_override": "Warehouse Management",
				"summary_override": "Inbound & picking",
				"href": "/software/warehouse-management-system",
				"image": wms_image,
				"sort_order": 2,
			},
			{
				"display_name_override": "ZATCA Integration",
				"summary_override": "e-Invoicing compliance",
				"href": "/software/zatca-integration",
				"image": zatca_image,
				"sort_order": 3,
			},
			{
				"display_name_override": "Mobile Applications",
				"summary_override": "Field & warehouse apps",
				"href": "/software/mobile-applications",
				"image": copy_software_image("software-mobile-applications.jpg"),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Discovery & implementation",
				"description": "Process mapping, chart of accounts, and phased go-live.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "Data migration",
				"description": "Customers, items, opening balances, and historical documents.",
				"sort_order": 2,
			},
			{
				"icon": "zatca",
				"title": "ZATCA compliance",
				"description": "e-Invoicing configuration and compliance validation.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Ongoing support",
				"description": "User training, help desk, and continuous improvement.",
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
				"related_website_product": pos_name,
				"display_name_override": "Modern POS",
				"summary_override": "Retail checkout connected to ERPNext inventory",
				"href": "/software/modern-pos",
				"image": pos_image,
				"sort_order": 1,
			},
			{
				"related_website_product": wms_name,
				"display_name_override": "Warehouse Management System",
				"summary_override": "Warehouse execution connected to ERP stock",
				"href": "/software/warehouse-management-system",
				"image": wms_image,
				"sort_order": 2,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
