# Copyright (c) 2026, Printechs and contributors
"""Fill the Hitachi UX-D161 Website Product with sample marketing content."""

from pathlib import Path
from shutil import copy2

import frappe

INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def fill_hitachi_sample(slug: str = "hitachi-ux-d161"):
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if not name:
		frappe.throw(f"Website Product with slug {slug} was not found")

	doc = frappe.get_doc("Website Product", name)

	doc.display_name = "Hitachi UX-D161W"
	doc.website_product_name = "Hitachi UX-D161W"
	doc.category = "Coding & Marking"
	doc.subcategory = "Continuous Inkjet"
	doc.category_label = "CONTINUOUS INKJET PRINTER"
	doc.tagline = "Reliable coding for demanding production environments"
	doc.short_description = (
		"High-performance continuous inkjet printer for production line marking on "
		"metal, plastic, film, and packaging — with wireless connectivity and easy maintenance."
	)
	doc.long_description = (
		"<p>The Hitachi UX-D161W is an industrial continuous inkjet (CIJ) printer designed "
		"for demanding manufacturing environments. Using a non-contact printing method, "
		"it applies codes, dates, and batch data to products moving on production lines at high speed.</p>"
		"<p>Built for reliability in harsh conditions, the UX-D161W combines advanced ink delivery, "
		"automatic nozzle cleaning, and remote monitoring capability. Printechs supplies, installs, "
		"and supports Hitachi UX systems across Saudi Arabia with local expertise and service coverage.</p>"
	)
	doc.hero_image_alt = "Hitachi UX-D161W continuous inkjet printer"
	doc.hero_trust_chips = "IP65 rated\nUp to 600 dpi\nPrintechs Saudi Arabia"
	doc.story_heading = "Built for production line coding"
	doc.visual_story_heading = "See the print quality"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.featured = 1
	doc.featured_sort_order = 1
	doc.card_title = "UX-Series"
	doc.card_brand_label = "Hitachi"
	doc.card_summary = "Continuous inkjet coder designed for high-speed industrial production lines."
	doc.card_image = doc.hero_image
	doc.final_cta_heading = "Get pricing, availability, and integration advice"
	doc.final_cta_description = (
		"Printechs supports Hitachi UX systems from specification through installation, "
		"training, and ongoing service across Saudi Arabia."
	)
	doc.meta_title = "Hitachi UX-D161W | Printechs"
	doc.meta_description = (
		"Discover Hitachi UX-D161W continuous inkjet coding solutions from Printechs."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "speed",
				"title": "High-speed coding",
				"description": "Print at line speeds up to 5 m/s without compromising code quality on fast-moving conveyors.",
				"sort_order": 1,
			},
			{
				"icon": "lines",
				"title": "Up to 6 print lines",
				"description": "Flexible multi-line printing from a single printhead for dates, batch data, and logos.",
				"sort_order": 2,
			},
			{
				"icon": "shield",
				"title": "Industrial reliability",
				"description": "Stainless steel IP65 construction built for washdown and harsh production environments.",
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "Flexible integration",
				"description": "Wi-Fi 5 and Ethernet for remote monitoring, diagnostics, and plant system connectivity.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Production dates",
				"image": copy_public_image("industry-dairy.jpg"),
				"image_alt": "Production date codes on dairy bottles",
				"caption": "Clear, high-contrast date codes on fast-moving dairy lines.",
				"sort_order": 1,
			},
			{
				"label": "Expiry dates",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Expiry date marking on beverage packaging",
				"caption": "Legible expiry and best-before marking on bottles and packs.",
				"sort_order": 2,
			},
			{
				"label": "Batch codes",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Batch codes on secondary packaging",
				"caption": "Batch and lot traceability on cartons and flexible film.",
				"sort_order": 3,
			},
			{
				"label": "Barcodes",
				"image": copy_public_image("industry-plastic.jpg"),
				"image_alt": "Barcode printing on plastic containers",
				"caption": "1D and 2D codes for supply chain traceability.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "print",
				"title": "Print technology",
				"description": "Continuous inkjet (CIJ) · up to 600 dpi · 1–12 mm character height",
				"sort_order": 1,
			},
			{
				"icon": "lines",
				"title": "Print lines",
				"description": "Up to 6 lines from a single printhead",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "Touchscreen",
				"description": '10.4" colour LCD operator interface',
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Connectivity",
				"description": "Ethernet · Wi-Fi 5 · USB 2.0 host/device",
				"sort_order": 4,
			},
			{
				"icon": "speed",
				"title": "Applications",
				"description": "Dates · lot · batch · barcode · Data Matrix",
				"sort_order": 5,
			},
			{
				"icon": "durability",
				"title": "Suitable for",
				"description": "Packaging · dairy · beverage · plastic · metal",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Printing performance",
			[
				("Print resolution", "Up to 600 dpi"),
				("Print speed", "Up to 5 m/s"),
				("Character height", "1–12 mm"),
				("Print lines", "Up to 6 lines"),
			],
		),
		(
			"Connectivity",
			[
				("Wireless", "Wi-Fi 5 (802.11ac)"),
				("Ethernet", "10/100/1000BASE-T"),
				("USB", "2.0 Host / Device"),
			],
		),
		(
			"Ink system",
			[
				("Ink type", "MEK-based / solvent"),
				("Ink capacity", "2 L smart bottle"),
				("Drying time", "0.3–3 seconds"),
			],
		),
		(
			"Durability & environment",
			[
				("IP rating", "IP65"),
				("Operating temperature", "0–40 °C"),
				("Construction", "Stainless steel"),
			],
		),
		(
			"Compliance",
			[
				("Safety", "CE, FCC, RoHS"),
				("Explosion protection", "ATEX Zone 2"),
			],
		),
	]
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			spec_rows.append(
				{
					"group_title": group_title,
					"label": label,
					"value": value,
					"sort_order": sort,
				}
			)
			sort += 1
	doc.set("full_specifications", spec_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Dairy",
				"description": "Date and batch coding on bottles and pouches at high line speeds.",
				"image": copy_public_image("industry-dairy.jpg"),
				"image_alt": "Dairy production line coding",
				"industry_link": "dairy",
				"sort_order": 1,
			},
			{
				"title": "Food & Beverage",
				"description": "Expiry and production marking on bottles, cans, and flexible packaging.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Food and beverage packaging line",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Pharmaceutical",
				"description": "Traceability codes for regulated packaging and secondary cartons.",
				"image": copy_public_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmaceutical packaging line",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Pipe & Plastic",
				"description": "Durable marking on extruded products, pipes, and plastic containers.",
				"image": copy_public_image("industry-plastic.jpg"),
				"image_alt": "Plastic manufacturing line",
				"industry_link": "plastic",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Installation",
				"description": "Site survey, mounting, commissioning, and line integration.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Consumables",
				"description": "Ink supply, smart bottle management, and spare parts.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Maintenance",
				"description": "Preventive service plans and emergency response across KSA.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "Hands-on training for operators and maintenance teams.",
				"sort_order": 4,
			},
		],
	)

	datasheet = doc.primary_download_file or "/files/hitachi ink jet .pdf"
	doc.primary_download_label = "Download Datasheet"
	doc.primary_download_file = datasheet
	doc.set(
		"downloads",
		[
			{
				"label": "UX-D161W Product Datasheet",
				"file": datasheet,
				"download_type": "Datasheet",
				"sort_order": 1,
			},
		],
	)

	doc.set(
		"package_contents",
		[
			{"item_description": "UX-D161W printer main unit", "sort_order": 1},
			{"item_description": "2 L starter ink smart bottle", "sort_order": 2},
			{"item_description": "Mounting kit", "sort_order": 3},
			{"item_description": "Power and interface cabling", "sort_order": 4},
		],
	)

	# Related / ecosystem need other Website Product records — leave empty as a teaching example.
	doc.set("ecosystem_items", [])
	doc.set("related_products", [])

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name


def fill_ux_d151():
	"""Fill Hitachi UX-D151W (IND.SYS.HIJ.3581) with sample marketing content."""
	name = "IND.SYS.HIJ.3581"
	if not frappe.db.exists("Website Product", name):
		frappe.throw(f"Website Product {name} was not found")

	doc = frappe.get_doc("Website Product", name)
	hero = doc.hero_image or "/files/UX-D151W.jpg"
	datasheet = doc.primary_download_file or "/files/hitachi ink jet .pdf"

	doc.display_name = "Hitachi UX-D151W"
	doc.website_product_name = "Hitachi UX-D151W"
	doc.slug = "hitachi-ux-d151"
	doc.category = "Coding & Marking"
	doc.subcategory = "Continuous Inkjet"
	doc.category_label = "CONTINUOUS INKJET PRINTER"
	doc.tagline = "UX2-series coding with simpler operation and reliable uptime"
	doc.short_description = (
		"The Hitachi UX-D151W (UX2) continuous inkjet printer combines Hitachi reliability "
		"with easier setup, cleaner maintenance, and high-quality codes on production lines."
	)
	doc.long_description = (
		"<p>The Hitachi UX-D151W is part of the UX2 continuous inkjet range. It is designed "
		"for manufacturers who need clear date, batch, and barcode marking on metal, plastic, "
		"film, and packaging — with a simpler operator experience than previous UX models.</p>"
		"<p>UX2 enhancements focus on print quality, reduced downtime, and easier ink handling. "
		"Printechs supplies, installs, and supports Hitachi UX2 systems across Saudi Arabia "
		"with local service and genuine consumables.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "Hitachi UX-D151W UX2 continuous inkjet printer"
	doc.hero_trust_chips = "UX2 series\nHigh-contrast codes\nPrintechs Saudi Arabia"
	doc.story_heading = "Built for everyday production coding"
	doc.visual_story_heading = "See UX2 print quality"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.featured = 0
	doc.card_title = "UX-D151W"
	doc.card_brand_label = "Hitachi"
	doc.card_summary = "UX2 continuous inkjet printer for reliable date, batch, and barcode coding."
	doc.card_image = hero
	doc.final_cta_heading = "Get pricing and line-integration advice for UX-D151W"
	doc.final_cta_description = (
		"Printechs supports Hitachi UX2 printers from specification through installation, "
		"training, and ongoing service across Saudi Arabia."
	)
	doc.meta_title = "Hitachi UX-D151W | Printechs"
	doc.meta_description = (
		"Hitachi UX-D151W UX2 continuous inkjet printer supplied and supported by Printechs."
	)
	doc.primary_download_label = "Download Datasheet"
	doc.primary_download_file = datasheet
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "print",
				"title": "UX2 print quality",
				"description": "Sharp date, lot, and barcode codes on fast-moving packaging and industrial parts.",
				"sort_order": 1,
			},
			{
				"icon": "maintenance",
				"title": "Easier maintenance",
				"description": "UX2 design reduces routine cleaning time and helps keep the line running.",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "Simple operation",
				"description": "Colour touchscreen and guided setup so operators can change jobs quickly.",
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "Plant connectivity",
				"description": "Ethernet and USB for message download, monitoring, and factory integration.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Metal marking",
				"image": copy_public_image("industry-steel.jpg"),
				"image_alt": "Coding on metal production line",
				"caption": "Durable codes on metal components and formed products.",
				"sort_order": 1,
			},
			{
				"label": "Plastic & film",
				"image": copy_public_image("industry-plastic.jpg"),
				"image_alt": "Plastic container coding",
				"caption": "Clear marking on extruded plastics, bottles, and flexible film.",
				"sort_order": 2,
			},
			{
				"label": "Pharmaceutical",
				"image": copy_public_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmaceutical packaging coding",
				"caption": "Batch and expiry codes for regulated packaging lines.",
				"sort_order": 3,
			},
			{
				"label": "Packaging",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Secondary packaging coding",
				"caption": "Carton and secondary packaging codes for logistics.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "print",
				"title": "Print technology",
				"description": "Continuous inkjet (CIJ) · UX2 platform · 1–10 mm character height",
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "Line speed",
				"description": "High-speed production coding without stopping the conveyor",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "Touchscreen",
				"description": "Colour operator interface with guided job setup",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Connectivity",
				"description": "Ethernet · USB · optional wireless",
				"sort_order": 4,
			},
			{
				"icon": "durability",
				"title": "Industrial build",
				"description": "Production-floor enclosure for daily manufacturing use",
				"sort_order": 5,
			},
			{
				"icon": "lines",
				"title": "Code types",
				"description": "Dates · lot · batch · barcode · 2D / Data Matrix",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Printing performance",
			[
				("Platform", "Hitachi UX2"),
				("Print technology", "Continuous inkjet (CIJ)"),
				("Character height", "1–10 mm"),
				("Print lines", "Up to 5 lines"),
			],
		),
		(
			"Connectivity",
			[
				("Ethernet", "Standard"),
				("USB", "Host / Device"),
				("Wireless", "Optional"),
			],
		),
		(
			"Ink system",
			[
				("Ink type", "MEK-based / solvent options"),
				("Applications", "Porous and non-porous substrates"),
				("Drying", "Fast-dry industrial inks"),
			],
		),
		(
			"Environment",
			[
				("Use", "Indoor production environments"),
				("Support", "Printechs Saudi Arabia"),
			],
		),
	]
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			spec_rows.append(
				{"group_title": group_title, "label": label, "value": value, "sort_order": sort}
			)
			sort += 1
	doc.set("full_specifications", spec_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Pharmaceutical",
				"description": "Traceability codes for regulated packaging and secondary cartons.",
				"image": copy_public_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmaceutical packaging line",
				"industry_link": "pharmaceutical",
				"sort_order": 1,
			},
			{
				"title": "Pipe & Plastic",
				"description": "Durable marking on extruded products, pipes, and plastic containers.",
				"image": copy_public_image("industry-plastic.jpg"),
				"image_alt": "Plastic manufacturing line",
				"industry_link": "plastic",
				"sort_order": 2,
			},
			{
				"title": "Steel",
				"description": "Production marking on metal products and industrial components.",
				"image": copy_public_image("industry-steel.jpg"),
				"image_alt": "Steel production line",
				"industry_link": "steel",
				"sort_order": 3,
			},
			{
				"title": "Packaging",
				"description": "Carton and secondary packaging coding for warehouse and retail.",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Packaging production",
				"industry_link": "packaging",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Installation",
				"description": "Site survey, mounting, commissioning, and line integration.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Consumables",
				"description": "UX2 ink, makeup, filters, and genuine spare parts.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Maintenance",
				"description": "Preventive service plans and emergency response across KSA.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "Hands-on training for operators and maintenance teams.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"downloads",
		[
			{
				"label": "UX-D151W Product Datasheet",
				"file": datasheet,
				"download_type": "Datasheet",
				"sort_order": 1,
			},
		],
	)

	doc.set(
		"package_contents",
		[
			{"item_description": "UX-D151W printer main unit", "sort_order": 1},
			{"item_description": "Starter ink and makeup set", "sort_order": 2},
			{"item_description": "Mounting kit", "sort_order": 3},
			{"item_description": "Power and interface cabling", "sort_order": 4},
		],
	)

	related = []
	if frappe.db.exists("Website Product", "IND.SYS.HIJ.3622"):
		related.append({"related_website_product": "IND.SYS.HIJ.3622", "sort_order": 1})
	doc.set("related_products", related)
	doc.set(
		"ecosystem_items",
		[
			{
				"related_website_product": "IND.SYS.HIJ.3622",
				"display_name_override": "UX-D161W",
				"summary_override": "High-speed UX platform for demanding lines",
				"sort_order": 1,
			}
		]
		if frappe.db.exists("Website Product", "IND.SYS.HIJ.3622")
		else [],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name


def fill_memor_17():
	"""Fill Datalogic Memor 17 (RET.SYS.DLG.4708) with sample marketing content."""
	name = "RET.SYS.DLG.4708"
	if not frappe.db.exists("Website Product", name):
		frappe.throw(f"Website Product {name} was not found")

	doc = frappe.get_doc("Website Product", name)
	hero = doc.hero_image or "/files/Memor17_front.jpg"

	doc.display_name = "Datalogic Memor 17"
	doc.website_product_name = "Datalogic Memor 17"
	doc.slug = "datalogic-memor-17"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Mobile Computers"
	doc.category_label = "MOBILE COMPUTER"
	doc.tagline = "Full-touch Android PDA for store, warehouse, and field teams"
	doc.short_description = (
		"Enterprise full-touch PDA with standard-range 2D imager, Green Spot feedback, "
		"Wi-Fi 6E, 5G, and IP65/IP67 protection for retail and logistics workflows."
	)
	doc.long_description = (
		"<p>The Datalogic Memor 17 is a full-touch mobile computer built for price checks, "
		"inventory, picking, and assisted selling. It combines a standard-range 2D imager "
		"with Green Spot good-read feedback, a 13 MP rear camera, and an 8 MP front camera.</p>"
		"<p>The device runs Android 13 on a Qualcomm octa-core 2.4 GHz platform with 6 GB RAM "
		"and 64 GB storage. Wi-Fi 6E, 5G, NFC, and push-to-talk help teams stay connected. "
		"IP65/IP67 sealing supports store floor and warehouse use. Printechs supplies Memor 17 "
		"with staging, MDM configuration, and integration support across Saudi Arabia.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic Memor 17 full-touch mobile computer"
	doc.hero_trust_chips = "Android 13\nIP65 / IP67\nWi-Fi 6E + 5G\nPrintechs Saudi Arabia"
	doc.story_heading = "Mobility for connected store and warehouse teams"
	doc.visual_story_heading = "Memor 17 in real operations"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_on_products_list = 1
	doc.featured = 0
	doc.card_title = "Memor 17"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = "Full-touch Android PDA with 2D imager, 5G, and IP65/IP67 protection."
	doc.card_image = hero
	doc.final_cta_heading = "Get pricing and deployment advice for Memor 17"
	doc.final_cta_description = (
		"Printechs supplies Datalogic mobility devices with staging, integration, "
		"and local support across Saudi Arabia."
	)
	doc.meta_title = "Datalogic Memor 17 | Printechs"
	doc.meta_description = (
		"Datalogic Memor 17 full-touch PDA with 2D imager, Wi-Fi 6E and 5G — supplied by Printechs."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "scan",
				"title": "Fast. Accurate. Every time.",
				"description": "Standard-range 2D imager with Green Spot feedback confirms a good read instantly.",
				"sort_order": 1,
			},
			{
				"icon": "rugged",
				"title": "Rugged mobility",
				"description": "IP65 and IP67 sealing for store, warehouse, and outdoor receiving areas.",
				"sort_order": 2,
			},
			{
				"icon": "android",
				"title": "Android 13 enterprise",
				"description": "Qualcomm octa-core, 6 GB / 64 GB, Google Mobile Services, and MDM-ready rollout.",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Always connected",
				"description": "Wi-Fi 6E, 5G, NFC, and push-to-talk for store and field communication.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Retail floor",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Mobile computer used in retail store",
				"caption": "Price checks, shelf management, and assisted selling on the shop floor.",
				"sort_order": 1,
			},
			{
				"label": "Warehouse",
				"image": copy_public_image("industry-warehouse-logistics.jpg"),
				"image_alt": "Warehouse picking with mobile computer",
				"caption": "Receiving, picking, and inventory counts in warehouse operations.",
				"sort_order": 2,
			},
			{
				"label": "Fashion",
				"image": copy_public_image("industry-fashion.jpg"),
				"image_alt": "Fashion retail inventory with mobile device",
				"caption": "Stock lookups and click-and-collect order fulfilment.",
				"sort_order": 3,
			},
			{
				"label": "Food retail",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Food retail stock check",
				"caption": "Stock checks and expiry management in fresh-food retail.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "scan",
				"title": "Scanning",
				"description": "Std-range 2D imager · Green Spot feedback",
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "Display",
				"description": "Full-touch display · glove capable",
				"sort_order": 2,
			},
			{
				"icon": "android",
				"title": "Platform",
				"description": "Android 13 · Qualcomm octa-core 2.4 GHz",
				"sort_order": 3,
			},
			{
				"icon": "device",
				"title": "Memory",
				"description": "6 GB RAM · 64 GB storage",
				"sort_order": 4,
			},
			{
				"icon": "connectivity",
				"title": "Wireless",
				"description": "Wi-Fi 6E · 5G · NFC · PTT",
				"sort_order": 5,
			},
			{
				"icon": "durability",
				"title": "Durability",
				"description": "IP65 · IP67",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Computing",
			[
				("Processor", "Qualcomm octa-core, 2.4 GHz"),
				("Memory", "6 GB RAM / 64 GB storage"),
				("Operating system", "Android 13 with Google Mobile Services"),
			],
		),
		(
			"Scanning & camera",
			[
				("Scan engine", "Standard-range 2D imager"),
				("Good-read feedback", "Green Spot"),
				("Rear camera", "13 MP"),
				("Front camera", "8 MP"),
			],
		),
		(
			"Connectivity",
			[
				("WLAN", "Wi-Fi 6E"),
				("Cellular", "5G"),
				("Short range", "NFC · push-to-talk"),
			],
		),
		(
			"Power & durability",
			[
				("Battery", "4000 mAh"),
				("IP rating", "IP65 / IP67"),
				("Colour", "Black"),
			],
		),
	]
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			spec_rows.append(
				{"group_title": group_title, "label": label, "value": value, "sort_order": sort}
			)
			sort += 1
	doc.set("full_specifications", spec_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Retail",
				"description": "Shelf management, price verification, and assisted selling.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail store operations",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Warehousing",
				"description": "Receiving, put-away, picking, and cycle counting.",
				"image": copy_public_image("industry-warehouse-logistics.jpg"),
				"image_alt": "Warehouse logistics",
				"industry_link": "warehouse-logistics",
				"sort_order": 2,
			},
			{
				"title": "Fashion",
				"description": "Inventory lookups and click-and-collect fulfilment.",
				"image": copy_public_image("industry-fashion.jpg"),
				"image_alt": "Fashion retail",
				"industry_link": "fashion",
				"sort_order": 3,
			},
			{
				"title": "Food & Beverage",
				"description": "Stock checks and expiry management in fresh-food retail.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Food retail",
				"industry_link": "food-beverage",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Device staging",
				"description": "MDM configuration, app deployment, and rollout planning.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "Integration",
				"description": "Connect to POS, WMS, and ERPNext platforms.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Warranty & repair",
				"description": "Swap-device programs and repair coordination.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "User training",
				"description": "Operator training for store and warehouse teams.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "Memor 17 PDA main unit", "sort_order": 1},
			{"item_description": "4000 mAh battery", "sort_order": 2},
			{"item_description": "USB charging cable", "sort_order": 3},
			{"item_description": "Quick-start documentation", "sort_order": 4},
		],
	)
	doc.set("related_products", [])
	doc.set("ecosystem_items", [])

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name


def fill_zt421():
	"""Fill Zebra ZT421 (RET.SYS.ZEB.3626) with sample marketing content."""
	name = "RET.SYS.ZEB.3626"
	if not frappe.db.exists("Website Product", name):
		frappe.throw(f"Website Product {name} was not found")

	doc = frappe.get_doc("Website Product", name)
	hero = doc.hero_image or "/files/ZT421.jpg"

	doc.display_name = "Zebra ZT421"
	doc.website_product_name = "Zebra ZT421"
	doc.slug = "zebra-zt421"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Industrial Label Printers"
	doc.category_label = "INDUSTRIAL LABEL PRINTER"
	doc.tagline = "High-performance 6-inch industrial printing for warehouse and production"
	doc.short_description = (
		"Zebra ZT421 industrial printer at 203 dpi with colour display, ZPL/EPL languages, "
		"and USB, serial, Bluetooth, and Ethernet connectivity for high-volume label printing."
	)
	doc.long_description = (
		"<p>The Zebra ZT421 is a 6-inch industrial label printer designed for warehouses, "
		"distribution centres, and manufacturing lines that need durable barcodes, shipping "
		"labels, and compliance marks at volume. This configuration prints at 203 dpi "
		"(8 dots/mm) with a colour display and real-time clock.</p>"
		"<p>It supports EPL, ZPL, and ZPL II, so existing Zebra label formats can move across "
		"with minimal change. USB, RS-232, Bluetooth, and Ethernet cover stand-alone and "
		"networked deployments. Printechs supplies ZT421 printers with ribbons, labels, "
		"installation, and local support across Saudi Arabia.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "Zebra ZT421 industrial label printer"
	doc.hero_trust_chips = "203 dpi\n6-inch print width\nZPL / EPL\nPrintechs Saudi Arabia"
	doc.story_heading = "Built for high-volume industrial labelling"
	doc.visual_story_heading = "ZT421 in operation"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_on_products_list = 1
	doc.featured = 0
	doc.card_title = "ZT421"
	doc.card_brand_label = "Zebra"
	doc.card_summary = "6-inch industrial label printer with colour display, ZPL, and Ethernet."
	doc.card_image = hero
	doc.final_cta_heading = "Get pricing and media advice for ZT421"
	doc.final_cta_description = (
		"Printechs supplies Zebra industrial printers with labels, ribbons, installation, "
		"and service across Saudi Arabia."
	)
	doc.meta_title = "Zebra ZT421 | Printechs"
	doc.meta_description = (
		"Zebra ZT421 6-inch industrial label printer (203 dpi) supplied and supported by Printechs."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "print",
				"title": "6-inch industrial printing",
				"description": "Wide-format labels for shipping, compliance, and production identification.",
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "Built for volume",
				"description": "Industrial mechanism designed for long print runs in warehouse and factory use.",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "Colour display",
				"description": "On-printer colour interface and real-time clock for easier operator control.",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Ready to connect",
				"description": "USB, RS-232, Bluetooth, and Ethernet for stand-alone or networked printing.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Warehouse",
				"image": copy_public_image("industry-warehouse-logistics.jpg"),
				"image_alt": "Warehouse shipping label printing",
				"caption": "Shipping and carton labels for outbound logistics.",
				"sort_order": 1,
			},
			{
				"label": "Retail DC",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail distribution labelling",
				"caption": "Case and pallet labels for store replenishment.",
				"sort_order": 2,
			},
			{
				"label": "Packaging",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Packaging line label print",
				"caption": "Product and carton identification on packing lines.",
				"sort_order": 3,
			},
			{
				"label": "Manufacturing",
				"image": copy_public_image("industry-steel.jpg"),
				"image_alt": "Industrial identification labels",
				"caption": "Work-in-progress and compliance labels on the shop floor.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "print",
				"title": "Print resolution",
				"description": "203 dpi (8 dots/mm)",
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "Display",
				"description": "Colour display · real-time clock",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Interfaces",
				"description": "USB · RS-232 · Bluetooth · Ethernet",
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "Languages",
				"description": "EPL · ZPL · ZPL II",
				"sort_order": 4,
			},
			{
				"icon": "durability",
				"title": "Class",
				"description": "Industrial metal-frame printer",
				"sort_order": 5,
			},
			{
				"icon": "inventory",
				"title": "Applications",
				"description": "Shipping · compliance · WIP · carton labels",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Printing",
			[
				("Model", "Zebra ZT421"),
				("Resolution", "203 dpi (8 dots/mm)"),
				("Print width", "Up to 6 inches (168 mm class)"),
				("Print method", "Thermal transfer / direct thermal"),
			],
		),
		(
			"Control & languages",
			[
				("Display", "Colour"),
				("Clock", "Real-time clock (RTC)"),
				("Command languages", "EPL, ZPL, ZPL II"),
			],
		),
		(
			"Connectivity",
			[
				("USB", "Standard"),
				("Serial", "RS-232"),
				("Wireless", "Bluetooth"),
				("Network", "Ethernet"),
			],
		),
		(
			"Typical use",
			[
				("Environments", "Warehouse · DC · manufacturing"),
				("Support", "Printechs Saudi Arabia"),
			],
		),
	]
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			spec_rows.append(
				{"group_title": group_title, "label": label, "value": value, "sort_order": sort}
			)
			sort += 1
	doc.set("full_specifications", spec_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Warehousing",
				"description": "Shipping, receiving, and carton labels for high-volume DCs.",
				"image": copy_public_image("industry-warehouse-logistics.jpg"),
				"image_alt": "Warehouse logistics labelling",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Retail",
				"description": "Store replenishment and distribution labelling.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail distribution",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Packaging",
				"description": "Product, case, and pallet identification on packing lines.",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Packaging production",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Manufacturing",
				"description": "WIP, component, and compliance labels on the shop floor.",
				"image": copy_public_image("industry-steel.jpg"),
				"image_alt": "Manufacturing identification",
				"industry_link": "steel",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Installation",
				"description": "Printer setup, network connection, and label format check.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Labels & ribbons",
				"description": "Matched media and thermal-transfer ribbons for ZT421.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Service",
				"description": "Preventive maintenance, printhead care, and repair coordination.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "Media loading, calibration, and everyday operator training.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZT421 industrial printer", "sort_order": 1},
			{"item_description": "Power cable", "sort_order": 2},
			{"item_description": "USB cable", "sort_order": 3},
			{"item_description": "Quick-start documentation", "sort_order": 4},
		],
	)

	related = []
	if frappe.db.exists("Website Product", "RET.SYS.DLG.4708"):
		related.append({"related_website_product": "RET.SYS.DLG.4708", "sort_order": 1})
	doc.set("related_products", related)
	doc.set("ecosystem_items", [])

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
