# Copyright (c) 2026, Printechs and contributors
"""Create or update the Modern POS Website Product from the static software page."""

from pathlib import Path
from shutil import copy2

import frappe

from printechs_digital.constants.product_page_sections import default_page_section_order_rows

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


def get_or_create_modern_pos():
	name = frappe.db.get_value("Website Product", {"slug": "modern-pos"}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "Modern POS"
	doc.display_name = "Modern POS"
	doc.slug = "modern-pos"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "Retail Software"
	doc.short_description = (
		"Cloud-ready POS software for multi-store retail — unified checkout, inventory sync, "
		"loyalty, and ZATCA-compliant invoicing."
	)
	doc.long_description = "<p>Modern POS</p>"
	doc.hero_image = copy_software_image("software-modern-pos.jpg")
	doc.hero_image_alt = "Modern POS checkout with scanner, terminal and payment system"
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_modern_pos():
	doc = get_or_create_modern_pos()

	hero = copy_software_image("software-modern-pos.jpg")
	inventory_image = copy_software_image("software-warehouse-management-system.jpg")
	zatca_image = copy_software_image("software-zatca-integration.jpg")
	erpnext_image = copy_software_image("software-erpnext.jpg")
	loyalty_image = copy_software_image("software-printechs-loyalty-management-system.jpg")

	doc.website_product_name = "Modern POS"
	doc.display_name = "Modern POS"
	doc.slug = "modern-pos"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.brand = "Printechs"
	doc.category = "Retail Software"
	doc.subcategory = "Point of Sale"
	doc.category_label = "RETAIL POS SYSTEM"
	doc.tagline = (
		"Powerful retail POS software designed for supermarkets, grocery stores, "
		"fashion retailers and multi-store businesses in Saudi Arabia."
	)
	doc.short_description = (
		"Powerful retail POS software designed for supermarkets, grocery stores, "
		"fashion retailers and multi-store businesses in Saudi Arabia."
	)
	doc.long_description = (
		"<p>Modern POS is Printechs' retail point of sale software for stores that need "
		"fast checkout, accurate stock, and ZATCA-ready invoicing in one system. Cashiers "
		"scan, weigh, and take payment at the counter while head office sees sales and "
		"inventory across every branch.</p>"
		"<p>It is used as a retail POS system for grocery, supermarket, hypermarket, and "
		"fashion stores. Promotions, loyalty, returns, and manager overrides sit in the "
		"same register workflow, and sales post to ERPNext so finance and warehouse teams "
		"work from the same numbers.</p>"
		"<p>Printechs implements, trains, and supports Modern POS in Saudi Arabia — "
		"including hardware, ERP integration, and ZATCA Phase 2 e-invoicing.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "Modern POS checkout with scanner, terminal and payment system"
	doc.hero_trust_chips = "ZATCA e-invoicing ready\nERPNext connected\nPrintechs Saudi Arabia"
	doc.show_demo_cta = 1
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = "Complete retail point of sale software"
	doc.visual_story_heading = "See Modern POS in action"
	doc.card_title = "Modern POS"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Retail POS system for grocery, fashion, supermarket, and hypermarket checkout."
	)
	doc.card_image = hero
	doc.final_cta_heading = "See Modern POS in your store environment"
	doc.final_cta_description = (
		"Book a demo with Printechs to explore checkout workflows, ERP integration, "
		"and ZATCA compliance for your retail operation."
	)
	doc.meta_title = "Retail POS System Saudi Arabia | POS Software | Printechs"
	doc.meta_description = (
		"Retail POS software in Saudi Arabia for supermarkets, grocery, fashion and "
		"retail stores. Manage sales, inventory, loyalty, promotions and ZATCA "
		"e-invoicing with Printechs."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "checkout",
				"title": "Fast checkout",
				"description": "Streamlined register workflows with barcode, search, and weighed-item support.",
				"sort_order": 1,
			},
			{
				"icon": "inventory",
				"title": "Inventory control",
				"description": "Real-time stock visibility across stores, warehouses, and back office.",
				"sort_order": 2,
			},
			{
				"icon": "store",
				"title": "Multi-store management",
				"description": "Centralised pricing, promotions, and reporting for every location.",
				"sort_order": 3,
			},
			{
				"icon": "loyalty",
				"title": "Loyalty & promotions",
				"description": "Member pricing, points, and campaign tools built into checkout.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Checkout",
				"image": hero,
				"image_alt": "Modern POS checkout screen",
				"caption": "Fast register workflows with barcode, search, and weighed items.",
				"sort_order": 1,
			},
			{
				"label": "Inventory",
				"image": inventory_image,
				"image_alt": "Inventory visibility dashboard",
				"caption": "Real-time stock lookup across stores and warehouses.",
				"sort_order": 2,
			},
			{
				"label": "ZATCA",
				"image": zatca_image,
				"image_alt": "ZATCA e-invoicing compliance",
				"caption": "Automated ZATCA Phase 2 e-invoicing from the register.",
				"sort_order": 3,
			},
		],
	)

	doc.enable_product_tour = 1
	doc.product_tour_heading = "See Modern POS in action"
	doc.product_tour_subheading = (
		"Explore the checkout, payments, promotions, inventory and "
		"management tools your retail team uses every day."
	)
	doc.set(
		"tour_sections",
		[
			{
				"eyebrow": "Checkout",
				"heading": "Fast, cashier-friendly checkout",
				"body": (
					"Give cashiers a clean, responsive sales screen designed for "
					"high-volume retail operations."
				),
				"features": (
					"Barcode and item search\n"
					"Weighed and variant items\n"
					"Automatic pricing and promotions\n"
					"Fast tender processing"
				),
				"image_alt": "Modern POS retail checkout screen for Saudi Arabia",
				"sort_order": 1,
			},
			{
				"eyebrow": "Payment",
				"heading": "Flexible payment processing",
				"body": (
					"Complete transactions using multiple payment methods from a "
					"single checkout workflow."
				),
				"features": (
					"Cash and card payments\n"
					"Multiple tender types\n"
					"Split / multi-tender payments\n"
					"Controlled payment completion"
				),
				"image_alt": "Modern POS multi-payment checkout screen",
				"sort_order": 2,
			},
			{
				"eyebrow": "Customer",
				"heading": "Customer and loyalty at checkout",
				"body": (
					"Identify customers directly from the register and provide "
					"personalised pricing and loyalty benefits."
				),
				"features": (
					"Customer lookup\n"
					"Member identification\n"
					"Loyalty points\n"
					"Purchase history"
				),
				"image_alt": "Modern POS customer lookup and loyalty screen at checkout",
				"sort_order": 3,
			},
			{
				"eyebrow": "Promotions",
				"heading": "Powerful retail promotions",
				"body": (
					"Apply centrally managed offers automatically during checkout "
					"without slowing down the cashier."
				),
				"features": (
					"Percentage and amount discounts\n"
					"Mix-and-match promotions\n"
					"Member pricing\n"
					"Manager-controlled overrides"
				),
				"image_alt": "Modern POS retail promotions and discount screen",
				"sort_order": 4,
			},
			{
				"eyebrow": "Inventory",
				"heading": "Real-time inventory visibility",
				"body": (
					"Allow store teams to check available stock without leaving the "
					"sales workflow."
				),
				"features": (
					"Current store stock\n"
					"Other branch availability\n"
					"Warehouse visibility\n"
					"Variant-level inventory"
				),
				"image_alt": "Modern POS real-time retail inventory lookup",
				"sort_order": 5,
			},
			{
				"eyebrow": "Returns",
				"heading": "Controlled returns and exchanges",
				"body": (
					"Process customer returns through a controlled workflow linked "
					"to the original transaction."
				),
				"features": (
					"Original invoice lookup\n"
					"Return validation\n"
					"Refund processing\n"
					"Supervisor controls"
				),
				"image_alt": "Modern POS returns and exchange screen",
				"sort_order": 6,
			},
			{
				"eyebrow": "Manager",
				"heading": "Store management and control",
				"body": (
					"Give supervisors visibility and control over sensitive "
					"register operations."
				),
				"features": (
					"Manager overrides\n"
					"Discount approval\n"
					"Void controls\n"
					"Cashier and store monitoring"
				),
				"image_alt": "Modern POS store manager controls and supervisor screen",
				"sort_order": 7,
			},
			{
				"eyebrow": "ERPNext",
				"heading": "Connected to ERPNext",
				"body": (
					"Connect retail transactions with finance, inventory, "
					"purchasing and warehouse operations."
				),
				"features": (
					"Sales synchronization\n"
					"Item and price synchronization\n"
					"Inventory synchronization\n"
					"Centralised back-office operations"
				),
				"image_alt": "Modern POS ERPNext retail integration",
				"sort_order": 8,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "cloud",
				"title": "Deployment",
				"description": "Cloud SaaS or on-premise · unlimited registers per store",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "ERP integration",
				"description": "ERPNext native · real-time sales and stock sync",
				"sort_order": 2,
			},
			{
				"icon": "zatca",
				"title": "Compliance",
				"description": "ZATCA Phase 2 e-invoicing · audit-ready workflows",
				"sort_order": 3,
			},
			{
				"icon": "device",
				"title": "Device support",
				"description": "Windows and Android POS terminals",
				"sort_order": 4,
			},
			{
				"icon": "report",
				"title": "Languages",
				"description": "English and Arabic interface support",
				"sort_order": 5,
			},
			{
				"icon": "connectivity",
				"title": "Offline mode",
				"description": "Continue selling when connectivity is interrupted",
				"sort_order": 6,
			},
		],
	)

	capability_rows = []
	modules = [
		("Sales", "checkout", [
			"Quick billing and barcode scanning",
			"Multiple payment methods",
			"Returns, refunds, and void controls",
		]),
		("Inventory", "inventory", [
			"Real-time stock lookup",
			"Inter-store transfers",
			"Weighed and variant items",
		]),
		("Customers", "loyalty", [
			"Member profiles and loyalty points",
			"Campaign redemption at register",
			"Customer purchase history",
		]),
		("Promotions", "store", [
			"Centralised offer management",
			"Mix-and-match deals",
			"Manager override controls",
		]),
		("Reports", "report", [
			"End-of-day reconciliation",
			"Store-level KPI dashboards",
			"Cashier performance tracking",
		]),
		("Integrations", "integration", [
			"ERPNext native sync",
			"E-commerce and API layer",
			"Payment terminal connectivity",
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
				"title": "Grocery",
				"description": "POS software for grocery — high-volume checkout with weighed items and promotions.",
				"image": copy_industry_image("industry-retail.jpg"),
				"image_alt": "POS software for grocery retail",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Fashion stores",
				"description": "POS software for fashion stores — variants, loyalty, and multi-store inventory.",
				"image": copy_industry_image("industry-fashion.jpg"),
				"image_alt": "POS software for fashion store",
				"industry_link": "fashion",
				"sort_order": 2,
			},
			{
				"title": "Specialty retail",
				"description": "Checkout counter software for deli, bakery, and fresh-food counters with scales.",
				"image": copy_industry_image("industry-bakery.jpg"),
				"image_alt": "Specialty food retail POS",
				"industry_link": "bakery",
				"sort_order": 3,
			},
			{
				"title": "Supermarkets & hypermarkets",
				"description": "POS for supermarket and hypermarket chains — centralised pricing and reporting.",
				"image": copy_industry_image("industry-food-beverage.jpg"),
				"image_alt": "POS for supermarket and hypermarket",
				"industry_link": "food-beverage",
				"sort_order": 4,
			},
		],
	)

	memor_name = frappe.db.get_value(
		"Website Product", {"slug": "datalogic-memor-17", "published": 1}, "name"
	)
	doc.set(
		"ecosystem_items",
		[
			{
				"display_name_override": "POS Terminal",
				"summary_override": "Checkout hardware",
				"href": "#",
				"image": "/files/POS-systems.jpg" if (SITE_FILES / "POS-systems.jpg").exists() else hero,
				"sort_order": 1,
			},
			{
				"related_website_product": memor_name,
				"display_name_override": "Handheld Device",
				"summary_override": "Floor inventory",
				"href": "/products/datalogic-memor-17" if memor_name else "/products/datalogic-memor-12",
				"image": "/files/Memor17_front.jpg" if (SITE_FILES / "Memor17_front.jpg").exists() else None,
				"sort_order": 2,
			},
			{
				"display_name_override": "Weighing Scale",
				"summary_override": "Deli & fresh food",
				"href": "#",
				"image": copy_industry_image("industry-bakery.jpg"),
				"sort_order": 3,
			},
			{
				"display_name_override": "Barcode Scanner",
				"summary_override": "Retail scanning",
				"href": "#",
				"image": hero,
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Discovery & rollout",
				"description": "Process mapping, store deployment, and cashier training.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "ERP integration",
				"description": "ERPNext setup, data migration, and API connectivity.",
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
				"description": "Help desk, updates, and continuous improvement.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set("package_contents", [])
	doc.set("full_specifications", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "POS software for supermarkets and grocery stores",
				"body": (
					"Grocery and supermarket checkout is high volume: barcodes, weighed items, "
					"mix-and-match offers, and multiple tenders in one queue. Modern POS keeps "
					"that workflow on the register so cashiers do not leave the sale to look up "
					"price or stock.\n\n"
					"Supervisors see lane performance and end-of-day totals. Head office updates "
					"prices and promotions once, then every supermarket or grocery branch uses "
					"the same rules. That is how multi-store food retail stays consistent without "
					"slowing the counter."
				),
				"image": copy_industry_image("industry-food-beverage.jpg"),
				"image_alt": "Supermarket and grocery checkout with retail POS software",
				"link_label": "Food and beverage retail solutions",
				"link_href": "/industries/food-beverage",
				"sort_order": 1,
			},
			{
				"heading": "Fashion retail POS system",
				"body": (
					"Fashion stores need size, colour, and season handled at the checkout — not "
					"in a separate back-office tool. Modern POS looks up variants, member prices, "
					"and store stock so a salesperson can finish the sale or move a customer to "
					"another branch.\n\n"
					"Loyalty points and campaign prices apply on the same screen. Returns and "
					"exchanges keep the original ticket, which matters when fashion retailers "
					"run frequent promotions across mall and high-street locations."
				),
				"image": copy_industry_image("industry-fashion.jpg"),
				"image_alt": "Fashion store retail POS system at the checkout counter",
				"link_label": "Fashion retail solutions",
				"link_href": "/industries/fashion",
				"sort_order": 2,
			},
			{
				"heading": "ZATCA e-invoicing from the checkout",
				"body": (
					"Printechs Retail POS integrates retail transactions with ZATCA-compliant "
					"invoicing requirements in Saudi Arabia. Sales, returns, VAT and invoice "
					"information can be processed directly from the retail checkout environment.\n\n"
					"Simplified tax invoices and QR codes are produced with the receipt. B2B "
					"and return documents follow the same audit trail, so finance does not "
					"re-key counter sales into a separate e-invoicing tool."
				),
				"image": zatca_image,
				"image_alt": "ZATCA e-invoicing dashboard connected to retail POS checkout",
				"link_label": "ZATCA Integration",
				"link_href": "/software/zatca-integration",
				"sort_order": 3,
			},
			{
				"heading": "Inventory, promotions, and head-office control",
				"body": (
					"Stock on the register is the same stock finance and the warehouse see. "
					"Cashiers get a live lookup; managers approve discounts and voids; head "
					"office sets promotions and reviews store KPIs without waiting for a "
					"manual export.\n\n"
					"When Modern POS is connected to ERPNext, purchases, transfers, and "
					"invoices stay in one operational picture — from the checkout counter "
					"to the back office."
				),
				"image": inventory_image,
				"image_alt": "Retail inventory and head-office dashboard for multi-store POS",
				"link_label": "ERPNext for retail operations",
				"link_href": "/software/erpnext",
				"sort_order": 4,
			},
			{
				"heading": "Why choose Printechs retail POS?",
				"body": (
					"Printechs supplies the software, the checkout hardware, and the local "
					"team that puts them into a Saudi store. That includes cashier training, "
					"ERPNext and ZATCA setup, and support after go-live — not a remote licence "
					"with no one on the floor.\n\n"
					"If you run grocery, fashion, or multi-store retail, we map the register "
					"workflow first, then deploy Modern POS so the counter, stock room, and "
					"head office use the same system."
				),
				"image": hero,
				"image_alt": "Modern POS checkout counter software supplied by Printechs",
				"link_label": "Talk to Printechs",
				"link_href": "/contact",
				"sort_order": 5,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Is Modern POS a retail POS system for Saudi Arabia?",
				"answer": (
					"Yes. Modern POS is retail POS software implemented and supported by "
					"Printechs in Saudi Arabia, including ZATCA Phase 2 e-invoicing, English "
					"and Arabic screens, and local cashier training."
				),
				"sort_order": 1,
			},
			{
				"question": "Can it be used as POS software for grocery and supermarkets?",
				"answer": (
					"Yes. Grocery and supermarket stores use barcode scanning, weighed items, "
					"promotions, and multi-tender checkout. Prices and offers can be managed "
					"centrally for every branch."
				),
				"sort_order": 2,
			},
			{
				"question": "Does it work as POS software for fashion stores?",
				"answer": (
					"Yes. Fashion retailers can sell size and colour variants, apply member "
					"pricing and campaigns, and look up stock in other stores from the same "
					"register."
				),
				"sort_order": 3,
			},
			{
				"question": "How does ZATCA e-invoicing work at the checkout?",
				"answer": (
					"Sales, returns, and VAT from the register can generate ZATCA-compliant "
					"invoices with QR codes. Printechs configures the flow with ERPNext or "
					"the ZATCA Integration service so finance does not re-type counter sales."
				),
				"sort_order": 4,
			},
			{
				"question": "Can we connect Modern POS to ERPNext and warehouse stock?",
				"answer": (
					"Yes. Sales and inventory can sync with ERPNext. Retailers that also run "
					"a warehouse can connect Warehouse Management so store replenishment and "
					"head-office stock stay aligned."
				),
				"sort_order": 5,
			},
		],
	)

	zatca_name = frappe.db.get_value(
		"Website Product", {"slug": "zatca-integration", "published": 1}, "name"
	)
	erp_name = frappe.db.get_value(
		"Website Product", {"slug": "erpnext", "published": 1}, "name"
	)
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
				"related_website_product": zatca_name,
				"display_name_override": "ZATCA Integration",
				"summary_override": "Phase 2 e-invoicing for Saudi retail and finance",
				"href": "/software/zatca-integration",
				"image": zatca_image,
				"sort_order": 2,
			},
			{
				"display_name_override": "Printechs Loyalty Management",
				"summary_override": "Customer loyalty and engagement platform",
				"href": "/software/printechs-loyalty-management-system",
				"image": loyalty_image,
				"sort_order": 3,
			},
		],
	)

	doc.set("page_section_order", default_page_section_order_rows())

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
