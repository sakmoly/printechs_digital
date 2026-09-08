# Copyright (c) 2026, Printechs and contributors
"""
Reusable Website Product page script for another client site.

How to use
----------
1. Copy this file to fill_<client>_<product>.py
2. Edit the PAGE dict only (name, slug, copy, images, buttons).
3. Create / update the page:

   bench --site site1.local execute \\
     printechs_digital.setup.fill_client_website_page.fill_client_website_page

   If you renamed the file, change the module path to match.

Page building blocks (what the frontend already renders)
--------------------------------------------------------
Hero
  - Title, tagline, short description, hero image, trust chips
  - Custom buttons: Book Now / Book a Consultation / Back to parent
  - Or default Request Quote + Book a Demo (when use_custom_hero_ctas = 0)

Product Tour
  - Screenshot + text rows
  - image_side: "Left" or "Right" (empty = auto: 1 Left, 2 Right, 3 Left...)
  - cta_placement: "Above Demo Bar" or "Below Demo Bar"
  - Grey bar in the middle: Book a Demo (+ optional Request a Quote)

Content sections
  - Heading + 2 paragraphs + image
  - image_side: "Left" or "Right"
  - Optional link (leave link_label empty to hide the link, like ERPNext teasers)

Benefits, icon specs, FAQs, support, related products, final CTA

Icons you can use
-----------------
speed, lines, shield, integration, battery, scan, android, checkout, inventory,
store, loyalty, install, consumables, maintenance, training, display,
connectivity, durability, zatca, cloud, report, device, rugged, print

Image paths
-----------
Use site files: /files/your-image.jpg
Copy a file from frontend/printechs-web/public/images/software/ with copy_software_image().
"""

from pathlib import Path
from shutil import copy2

import frappe

from printechs_digital.constants.product_page_sections import default_page_section_order_rows

SOFTWARE_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/software")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")


def copy_software_image(filename: str) -> str:
	source = SOFTWARE_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def resolve_image(value: str | None) -> str:
	path = (value or "").strip()
	if not path:
		return ""
	if path.startswith("/files/") or path.startswith("http://") or path.startswith("https://"):
		return path
	return copy_software_image(path)


# =============================================================================
# EDIT THIS BLOCK FOR THE NEW CLIENT PAGE
# =============================================================================

PAGE = {
	# --- identity / URL ---
	"website_product_name": "Client Software",
	"display_name": "Client Software",
	"slug": "client-software",  # URL: /software/client-software  (or /software/{parent}/{slug})
	"product_type": "Software",  # Industrial | Retail Hardware | Software | Generic
	"division": "Software",  # Industrial | Retail | Software
	"brand": "Printechs",
	"category": "ERP Software",
	"subcategory": "Core Platform",
	"category_label": "CLIENT PLATFORM",
	"parent_software": None,  # set to "erpnext" (name or slug) for /software/erpnext/{slug}
	# Keep unpublished until copy and images are ready
	"published": 0,
	"show_on_software_list": 0,
	"show_on_products_list": 0,
	# --- hero ---
	"tagline": "One system for finance, inventory, sales and operations",
	"short_description": (
		"A connected business platform for finance, inventory, sales and purchasing — "
		"with local implementation and support."
	),
	"long_description": (
		"<p>This page follows the same layout as the Printechs software pages: hero, "
		"benefits, product tour, then image-and-text sections.</p>"
		"<p>Replace this copy with the client story. Keep two short paragraphs in the "
		"hero overview so the page stays scannable.</p>"
	),
	"hero_image": "software-erpnext.jpg",
	"hero_image_alt": "Business dashboard with sales, inventory and finance metrics",
	"hero_trust_chips": "Unified operations\nLocal implementation\nBook a live walkthrough",
	# Hero buttons. Relative paths stay on this site (/contact, /software/erpnext).
	# Do not use https://printechs.com/... or /newwebsite will be dropped.
	"use_custom_hero_ctas": 1,
	"hero_primary_cta_label": "Book Now",
	"hero_primary_cta_href": "/contact",
	"hero_secondary_cta_label": "See the tour",
	"hero_secondary_cta_href": "#product-tour",
	"show_demo_cta": 1,  # enables Book a Demo in the tour bar and default hero
	"show_quote_in_hero": 0,  # ignored when custom hero buttons are on
	"show_quote_in_product_tour": 0,  # 1 = also show Request a Quote in the tour bar
	# --- listing + SEO + bottom CTA ---
	"story_heading": "Finance, inventory and operations in one system",
	"card_title": "Client Software",
	"card_brand_label": "Printechs",
	"card_summary": "Integrated platform for finance, inventory, sales and operations.",
	"final_cta_heading": "Book a walkthrough of this platform",
	"final_cta_description": (
		"We can walk through your documents, roles and reporting before you decide on go-live."
	),
	"meta_title": "Client Software | Implementation",
	"meta_description": (
		"Client software page template: hero, Book Now, product tour and left/right image sections."
	),
	# --- benefits (4 cards under the hero) ---
	"benefits": [
		("integration", "Unified operations", "Finance, inventory, sales and purchasing share one live data model."),
		("inventory", "Stock and fulfilment", "Real-time inventory, warehouses and order status across locations."),
		("report", "Live reporting", "Managers see the same numbers operations already posted."),
		("cloud", "Local expertise", "Implementation, training and support with your team."),
	],
	# --- product tour (screenshot + text; Book a Demo sits after Above Demo Bar rows) ---
	"enable_product_tour": 1,
	"product_tour_heading": "Explore the platform in action",
	"product_tour_subheading": (
		"These three tour blocks are the live ERPNext tour structure: dashboard, "
		"connected operations, and local requirements."
	),
	"tour_sections": [
		{
			"cta_placement": "Above Demo Bar",
			"image_side": "Left",
			"eyebrow": "DASHBOARD",
			"heading": "One view of your business",
			"body": (
				"See sales, purchasing, receivables, payables, inventory and operational KPIs "
				"from one connected dashboard."
			),
			"features": (
				"Sales and purchase visibility\n"
				"Receivables and payables\n"
				"Inventory overview\n"
				"Business KPIs"
			),
			"image": "software-erpnext.jpg",
			"image_alt": "Business dashboard with sales and finance metrics",
			"sort_order": 1,
		},
		{
			"cta_placement": "Above Demo Bar",
			"image_side": "Right",
			"eyebrow": "FINANCE & OPERATIONS",
			"heading": "Connect transactions across your business",
			"body": (
				"Manage finance, inventory, sales and purchasing through connected workflows "
				"with real-time operational data across departments."
			),
			"features": (
				"Accounting and finance\n"
				"Inventory and warehouses\n"
				"Sales and purchasing\n"
				"Real-time transaction flow"
			),
			"image": "software-warehouse-management-system.jpg",
			"image_alt": "Inventory and warehouse operations connected to finance",
			"sort_order": 2,
		},
		{
			"cta_placement": "Below Demo Bar",
			"image_side": "Left",
			"eyebrow": "LOCAL OPERATIONS",
			"heading": "Built for local business requirements",
			"body": (
				"Configure tax, invoicing and operational requirements, with implementation "
				"and support for the team that will post every day."
			),
			"features": (
				"Tax and e-invoicing\n"
				"Arabic and English support\n"
				"Role-based approvals\n"
				"Local implementation and training"
			),
			"image": "software-zatca-integration.jpg",
			"image_alt": "Local tax and invoicing configuration",
			"sort_order": 3,
		},
	],
	# --- image + text sections (same layout as ERPNext Core Platform teasers) ---
	# Leave link_label empty for title + body + image only (no Learn more under the text).
	"content_sections": [
		{
			"section_type": "Industry Solution",
			"image_side": "Left",
			"heading": "Sales & Purchase",
			"body": (
				"Quotations, sales orders, delivery notes and invoices share one item and pricing "
				"master with purchase orders and supplier bills.\n\n"
				"Credit limits, pricing rules and landing costs are enforced in the same system "
				"that posts to stock and accounts, so sales and procurement do not drift apart."
			),
			"image": "software-modern-pos.jpg",
			"image_alt": "Sales orders, invoices and purchase workflows",
			"link_label": "",
			"link_href": "",
			"sort_order": 1,
		},
		{
			"section_type": "Industry Solution",
			"image_side": "Right",
			"heading": "Inventory",
			"body": (
				"Inventory tracks stock across warehouses, bins and companies with serial, batch "
				"and valuation methods that match how you buy and sell.\n\n"
				"Reorder rules, stock reconciliation and transfers stay visible to purchasing, "
				"sales and finance — so warehouse balances match the ledger."
			),
			"image": "software-warehouse-management-system.jpg",
			"image_alt": "Multi-warehouse inventory and stock valuation",
			"link_label": "",
			"link_href": "",
			"sort_order": 2,
		},
		{
			"section_type": "Industry Solution",
			"image_side": "Left",
			"heading": "Need a deeper module page?",
			"body": (
				"Add a link only when this block should open another page. Cards can still use "
				"the URL when link_href is set and link_label is empty.\n\n"
				"Example below shows a visible button under the text."
			),
			"image": "software-erpnext.jpg",
			"image_alt": "Module detail page example",
			"link_label": "Book Now",
			"link_href": "/contact",
			"sort_order": 3,
		},
	],
	"icon_specifications": [
		("cloud", "Deployment", "Cloud or on-premise"),
		("integration", "Connected apps", "POS, warehouse and tax"),
		("report", "Languages", "English and Arabic"),
		("device", "Roles", "Approvals by department"),
		("store", "Locations", "Multi-company, multi-warehouse"),
		("training", "Go-live", "Training and hypercare"),
	],
	"support_items": [
		("install", "Process design", "Map how the team works today before documents go live."),
		("training", "Training", "Role-based sessions for the people who will post every day."),
		("integration", "Connected system", "Keep items, parties and the ledger in one place."),
	],
	"faq_items": [
		(
			"Can we start with one module?",
			"<p>Yes. Start with finance and inventory, then add sales, purchasing or manufacturing when the team is ready.</p>",
		),
		(
			"How do we book a walkthrough?",
			"<p>Use Book Now on this page. We will schedule a session against your documents and roles.</p>",
		),
	],
}


def _get_or_create(slug: str, display_name: str, hero: str, alt: str):
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = display_name
	doc.display_name = display_name
	doc.slug = slug
	doc.product_type = PAGE["product_type"]
	doc.division = PAGE["division"]
	doc.category = PAGE["category"]
	doc.short_description = PAGE["short_description"]
	doc.long_description = PAGE["long_description"]
	doc.hero_image = hero
	doc.hero_image_alt = alt
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def _resolve_parent(parent_ref: str | None) -> str | None:
	if not parent_ref:
		return None
	if frappe.db.exists("Website Product", parent_ref):
		return parent_ref
	return frappe.db.get_value("Website Product", {"slug": parent_ref}, "name")


def fill_client_website_page(page: dict | None = None):
	"""Create or update the Website Product described in PAGE (or a passed dict)."""
	spec = page or PAGE
	hero = resolve_image(spec["hero_image"])
	doc = _get_or_create(spec["slug"], spec["display_name"], hero, spec["hero_image_alt"])

	parent_name = _resolve_parent(spec.get("parent_software"))
	canonical = (
		f"/software/{frappe.db.get_value('Website Product', parent_name, 'slug')}/{spec['slug']}"
		if parent_name
		else f"/software/{spec['slug']}"
	)

	doc.website_product_name = spec["website_product_name"]
	doc.display_name = spec["display_name"]
	doc.slug = spec["slug"]
	doc.product_type = spec["product_type"]
	doc.division = spec["division"]
	doc.parent_software = parent_name
	doc.brand = spec.get("brand")
	doc.category = spec["category"]
	doc.subcategory = spec.get("subcategory")
	doc.category_label = spec.get("category_label")
	doc.tagline = spec["tagline"]
	doc.short_description = spec["short_description"]
	doc.long_description = spec["long_description"]
	doc.hero_image = hero
	doc.hero_image_alt = spec["hero_image_alt"]
	doc.hero_trust_chips = spec.get("hero_trust_chips")
	doc.use_custom_hero_ctas = spec.get("use_custom_hero_ctas") or 0
	doc.hero_primary_cta_label = spec.get("hero_primary_cta_label") or ""
	doc.hero_primary_cta_href = spec.get("hero_primary_cta_href") or ""
	doc.hero_secondary_cta_label = spec.get("hero_secondary_cta_label") or ""
	doc.hero_secondary_cta_href = spec.get("hero_secondary_cta_href") or ""
	doc.show_demo_cta = spec.get("show_demo_cta") or 0
	doc.show_quote_in_hero = spec.get("show_quote_in_hero") or 0
	doc.show_quote_in_product_tour = spec.get("show_quote_in_product_tour") or 0
	doc.show_on_products_list = spec.get("show_on_products_list") or 0
	doc.show_on_software_list = spec.get("show_on_software_list") or 0
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = spec.get("story_heading")
	doc.card_title = spec.get("card_title") or spec["display_name"]
	doc.card_brand_label = spec.get("card_brand_label") or spec.get("brand")
	doc.card_summary = spec.get("card_summary") or spec["short_description"][:140]
	doc.card_image = hero
	doc.final_cta_heading = spec.get("final_cta_heading")
	doc.final_cta_description = spec.get("final_cta_description")
	doc.meta_title = spec.get("meta_title")
	doc.meta_description = spec.get("meta_description")
	doc.canonical_path = canonical
	doc.index_page = 1
	doc.published = spec.get("published") or 0
	doc.enable_product_tour = spec.get("enable_product_tour") or 0
	doc.product_tour_heading = spec.get("product_tour_heading")
	doc.product_tour_subheading = spec.get("product_tour_subheading")

	if not doc.get("page_section_order"):
		doc.set("page_section_order", default_page_section_order_rows())

	doc.set(
		"benefits",
		[
			{"icon": icon, "title": title, "description": desc, "sort_order": idx}
			for idx, (icon, title, desc) in enumerate(spec.get("benefits") or [], start=1)
		],
	)
	doc.set(
		"tour_sections",
		[
			{
				"cta_placement": row.get("cta_placement") or "Above Demo Bar",
				"image_side": row.get("image_side") or "",
				"eyebrow": row["eyebrow"],
				"heading": row["heading"],
				"body": row["body"],
				"features": row.get("features") or "",
				"image": resolve_image(row.get("image")),
				"image_alt": row.get("image_alt") or row["heading"],
				"sort_order": row.get("sort_order") or idx,
			}
			for idx, row in enumerate(spec.get("tour_sections") or [], start=1)
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": row.get("section_type") or "Industry Solution",
				"heading": row["heading"],
				"body": row["body"],
				"image": resolve_image(row.get("image")),
				"image_alt": row.get("image_alt") or row["heading"],
				"image_side": row.get("image_side") or "",
				"link_label": row.get("link_label") or "",
				"link_href": row.get("link_href") or "",
				"sort_order": row.get("sort_order") or idx,
			}
			for idx, row in enumerate(spec.get("content_sections") or [], start=1)
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": icon, "title": title, "description": desc, "sort_order": idx}
			for idx, (icon, title, desc) in enumerate(spec.get("icon_specifications") or [], start=1)
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": icon, "title": title, "description": desc, "sort_order": idx}
			for idx, (icon, title, desc) in enumerate(spec.get("support_items") or [], start=1)
		],
	)
	doc.set(
		"faq_items",
		[
			{"question": question, "answer": answer, "sort_order": idx}
			for idx, (question, answer) in enumerate(spec.get("faq_items") or [], start=1)
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	return {
		"name": doc.name,
		"slug": doc.slug,
		"canonical_path": doc.canonical_path,
		"published": doc.published,
	}
