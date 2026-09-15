# Copyright (c) 2026, Printechs and contributors
"""Create or update the E-Commerce Solutions Website Product.

Live reference store built on this stack: https://shoearena.sa/en
"""

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe

from printechs_digital.constants.product_page_sections import default_page_section_order_rows

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
SOFTWARE_DIRS = (
	Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/software"),
	Path("/home/erpnext/frappe-bench/apps/printechs_digital/frontend/printechs-web/public/images/software"),
)
UA = "Mozilla/5.0 (compatible; Printechs/1.0)"
SLUG = "e-commerce-solutions"
PATH = "/software/e-commerce-solutions"
LIVE_STORE = "https://shoearena.sa/en"

IMAGES = {
	"software-e-commerce-solutions.jpg": (
		"https://shoearena.sa/files/265%20E.webp"
	),
	"ecommerce-catalog.jpg": (
		"https://shoearena.sa/files/262%20E.webp"
	),
	"ecommerce-kids.jpg": (
		"https://shoearena.sa/files/263%20E.webp"
	),
	"ecommerce-shopper.jpg": (
		"https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=2000&q=80"
	),
	"ecommerce-checkout.jpg": (
		"https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=2000&q=80"
	),
	"ecommerce-mobile.jpg": (
		"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=2000&q=80"
	),
	"ecommerce-promotions.jpg": (
		"https://images.unsplash.com/photo-1607082349566-187342175e2f?auto=format&fit=crop&w=2000&q=80"
	),
	"ecommerce-fulfilment.jpg": (
		"https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=2000&q=80"
	),
	"ecommerce-delivery.jpg": (
		"https://images.unsplash.com/photo-1473445730015-841f29a9490b?auto=format&fit=crop&w=2000&q=80"
	),
	"ecommerce-browse.jpg": (
		"https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&w=2000&q=80"
	),
}


def _save_wide(im: Image.Image, filename: str) -> str:
	target_ratio = 16 / 10
	width, height = im.size
	if width / height > target_ratio:
		new_w = int(height * target_ratio)
		left = (width - new_w) // 2
		im = im.crop((left, 0, left + new_w, height))
	else:
		new_h = int(width / target_ratio)
		top = (height - new_h) // 2
		im = im.crop((0, top, width, top + new_h))
	im = im.resize((1600, 1000), Image.Resampling.LANCZOS)
	target = SITE_FILES / filename
	im.save(target, "JPEG", quality=90, optimize=True)
	for folder in SOFTWARE_DIRS:
		folder.mkdir(parents=True, exist_ok=True)
		im.save(folder / filename, "JPEG", quality=90, optimize=True)
	return f"/files/{filename}"


def download_wide(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if target.exists():
		return f"/files/{filename}"
	request = Request(url, headers={"User-Agent": UA})
	with urlopen(request, timeout=45) as response:
		data = response.read()
	if len(data) < 2000:
		frappe.throw(f"Download too small ({len(data)} bytes): {url}")
	im = Image.open(BytesIO(data)).convert("RGB")
	return _save_wide(im, filename)


def media() -> dict[str, str]:
	return {name: download_wide(name, url) for name, url in IMAGES.items()}


def published_name(slug: str) -> str | None:
	return frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "name")


def get_or_create(hero: str):
	name = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "E-Commerce Solutions"
	doc.display_name = "E-Commerce Solutions"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "Retail Software"
	doc.short_description = (
		"ERPNext-connected online store, mobile apps, and Aramex delivery for Saudi retail."
	)
	doc.long_description = "<p>E-Commerce Solutions</p>"
	doc.hero_image = hero
	doc.hero_image_alt = (
		"ShoeArena storefront built by Printechs — ERPNext e-commerce for Saudi retail"
	)
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_ecommerce():
	m = media()
	hero = m["software-e-commerce-solutions.jpg"]
	doc = get_or_create(hero)
	catalog = m["ecommerce-catalog.jpg"]
	kids = m["ecommerce-kids.jpg"]
	shopper = m["ecommerce-shopper.jpg"]
	checkout = m["ecommerce-checkout.jpg"]
	mobile = m["ecommerce-mobile.jpg"]
	promos = m["ecommerce-promotions.jpg"]
	fulfil = m["ecommerce-fulfilment.jpg"]
	delivery = m["ecommerce-delivery.jpg"]
	browse = m["ecommerce-browse.jpg"]

	erpnext_image = "/files/software-erpnext.jpg"
	pos_image = "/files/software-modern-pos.jpg"
	zatca_image = "/files/software-zatca-integration.jpg"
	wms_image = "/files/software-warehouse-management-system.jpg"

	doc.website_product_name = "E-Commerce Solutions"
	doc.display_name = "E-Commerce Solutions"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	if frappe.db.exists("Brand", "Printechs"):
		doc.brand = "Printechs"
	doc.category = "Retail Software"
	doc.subcategory = "E-Commerce"
	doc.category_label = "ERPNext E-COMMERCE"
	doc.tagline = (
		"Online store, Android and iOS apps, and Aramex delivery — stock and orders "
		"live in ERPNext"
	)
	doc.short_description = (
		"Build a bilingual web store and mobile app connected to ERPNext inventory, "
		"ZATCA invoices, and Aramex shipment status in real time."
	)
	doc.long_description = (
		"<p>Printechs E-Commerce Solutions puts a Saudi-ready storefront on the same "
		"ERPNext company you already run for stock, sales, and finance. Catalogue, "
		"price, and availability come from ERPNext. Orders write back as sales orders "
		"and invoices — no second stock book.</p>"
		"<p>Customers shop on the website or the Android and iOS apps, pay online, "
		"and receive live Aramex delivery updates. A live example is "
		f'<a href="{LIVE_STORE}">ShoeArena</a> — a multi-brand footwear store Printechs '
		"built on this stack.</p>"
		"<p>Printechs designs the catalogue, checkout, payments, ZATCA e-invoicing, "
		"warehouse pick, and last-mile integration, then supports the store after go-live "
		"in Riyadh, Jeddah and Dammam.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"ShoeArena storefront built by Printechs — ERPNext e-commerce for Saudi retail"
	)
	doc.hero_trust_chips = (
		"ERPNext catalogue & stock\nAramex live tracking\nAndroid and iOS apps"
	)
	doc.show_demo_cta = 1
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.featured = 0
	doc.index_page = 1
	doc.collapsible_full_specs = 1
	doc.story_heading = "One catalogue. One warehouse. One customer order."
	doc.visual_story_heading = "See the store customers actually use"
	doc.card_title = "E-Commerce Solutions"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"ERPNext-connected web store and mobile apps with Aramex delivery and live tracking."
	)
	doc.card_image = hero
	doc.final_cta_heading = "See an ERPNext store running in Saudi Arabia"
	doc.final_cta_description = (
		"Book a demo of the ShoeArena-style stack: catalogue sync, checkout, Aramex "
		"status, and Android / iOS apps on your ERPNext company."
	)
	doc.final_cta_secondary_label = "Talk to Our Software Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "E-Commerce Solutions | ERPNext Store | Printechs"
	doc.meta_description = (
		"ERPNext e-commerce for Saudi retail: bilingual store, Android and iOS apps, "
		"ZATCA invoices, and Aramex delivery with real-time customer tracking."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "integration",
				"title": "ERPNext is the source of truth",
				"description": "Items, prices, stock and orders stay in ERPNext — the store does not keep a second inventory.",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "Web plus Android and iOS",
				"description": "The same catalogue and cart on the website and native mobile apps.",
				"sort_order": 2,
			},
			{
				"icon": "cloud",
				"title": "Aramex, live to the customer",
				"description": "Shipments create on Aramex; pickup, transit and delivery status update the order in real time.",
				"sort_order": 3,
			},
			{
				"icon": "checkout",
				"title": "Checkout that posts to finance",
				"description": "Payments, VAT and ZATCA invoices come from the same sales document as the warehouse pick.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Live store",
				"image": hero,
				"image_alt": "ShoeArena National Day campaign on the Printechs ERPNext storefront",
				"caption": "ShoeArena.sa — a live multi-brand store on this ERPNext stack.",
				"sort_order": 1,
			},
			{
				"label": "Catalogue",
				"image": catalog,
				"image_alt": "Pegada footwear campaign on the ShoeArena ERPNext store",
				"caption": "Category, brand, size and colour from ERPNext item variants.",
				"sort_order": 2,
			},
			{
				"label": "Mobile apps",
				"image": mobile,
				"image_alt": "Smartphone used for the Android and iOS shopping apps",
				"caption": "Android and iOS apps share the same cart, orders and tracking.",
				"sort_order": 3,
			},
			{
				"label": "Aramex delivery",
				"image": delivery,
				"image_alt": "Outbound delivery truck for last-mile e-commerce shipments",
				"caption": "Aramex AWB on the order — status pushed back to the customer.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "integration",
				"title": "ERP",
				"description": "ERPNext items, warehouses, sales orders and invoices",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "Storefronts",
				"description": "Responsive web · Android app · iOS app",
				"sort_order": 2,
			},
			{
				"icon": "cloud",
				"title": "Delivery",
				"description": "Aramex create-shipment · live status · customer notifications",
				"sort_order": 3,
			},
			{
				"icon": "zatca",
				"title": "Saudi compliance",
				"description": "ZATCA Phase 2 e-invoices · VAT · Arabic / English",
				"sort_order": 4,
			},
			{
				"icon": "checkout",
				"title": "Payments",
				"description": "Cards, local gateways, COD and refunds posted to ERPNext",
				"sort_order": 5,
			},
			{
				"icon": "inventory",
				"title": "Fulfilment",
				"description": "Pick, pack and ship from ERPNext / WMS stock",
				"sort_order": 6,
			},
		],
	)

	capability_rows = []
	modules = [
		(
			"Catalogue",
			"inventory",
			[
				"ERPNext items, variants, brands and categories on the store",
				"Arabic and English product pages",
				"Stock shown from live warehouse quantity — hide or mark sold-out automatically",
			],
		),
		(
			"Shopping",
			"checkout",
			[
				"Search, filters, size and colour selection",
				"Wishlist, recently viewed and related products",
				"Guest or registered checkout with saved addresses",
			],
		),
		(
			"Promotions",
			"loyalty",
			[
				"Sale badges, percentage and amount offers",
				"Coupon codes and campaign landing pages",
				"Member pricing aligned with ERPNext price lists",
			],
		),
		(
			"Orders & finance",
			"zatca",
			[
				"Sales order created in ERPNext at checkout",
				"ZATCA Phase 2 tax invoice and QR on the order",
				"Payments, COD, refunds and credit notes in the same ledger",
			],
		),
		(
			"Aramex last mile",
			"cloud",
			[
				"Shipment created in Aramex from the packed order",
				"AWB and tracking number stored on the ERPNext delivery",
				"Pickup, in-transit and delivered status written back in real time",
				"Customer sees the same status in the account page and mobile app",
			],
		),
		(
			"Mobile apps",
			"device",
			[
				"Android and iOS apps on the same ERPNext catalogue",
				"Push notifications for order and Aramex status changes",
				"Login, orders, returns and address book on the phone",
			],
		),
	]
	sort_order = 1
	for title, icon, items in modules:
		for item_text in items:
			capability_rows.append(
				{
					"module_title": title,
					"icon": icon,
					"item_text": item_text,
					"sort_order": sort_order,
				}
			)
			sort_order += 1
	doc.set("capability_items", capability_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Fashion & footwear",
				"description": "Multi-brand size runs, as live on ShoeArena — men, women and kids.",
				"image": catalog,
				"image_alt": "Pegada men’s sneaker campaign on the ShoeArena ERPNext store",
				"industry_link": "fashion",
				"sort_order": 1,
			},
			{
				"title": "Retail chains",
				"description": "One ERPNext price list for web, app and store; stock shared with Modern POS.",
				"image": shopper,
				"image_alt": "Retail shopper with bags after an omnichannel purchase",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Warehouse fulfilment",
				"description": "Pick and pack from ERPNext / WMS so the website never oversells.",
				"image": fulfil,
				"image_alt": "Ecommerce fulfilment aisle with packed cartons",
				"industry_link": "warehouse-logistics",
				"sort_order": 3,
			},
			{
				"title": "Last-mile delivery",
				"description": "Aramex AWB on every packed order; customer tracking updates as the courier moves.",
				"image": delivery,
				"image_alt": "Delivery truck on the road for ecommerce last-mile",
				"industry_link": "warehouse-logistics",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Live store: ShoeArena",
				"body": (
					"ShoeArena is a Saudi multi-brand footwear store Printechs built on this "
					"ERPNext e-commerce stack — English and Arabic, men / women / kids, "
					"brands, offers and checkout.\n\n"
					"Open the live site to see catalogue, cart and account flows that post "
					"into ERPNext rather than a disconnected shop engine."
				),
				"image": hero,
				"image_alt": "ShoeArena live storefront developed by Printechs on ERPNext",
				"link_label": "Open ShoeArena",
				"link_href": LIVE_STORE,
				"sort_order": 1,
			},
			{
				"section_type": "Core Module",
				"heading": "Catalogue and stock stay in ERPNext",
				"body": (
					"Items, variants, barcodes, price lists and warehouse qty are ERPNext "
					"records. The website and apps read that data. When a customer buys, "
					"the sales order reserves stock so the store, the app and the till "
					"cannot sell the same pair twice."
				),
				"image": fulfil,
				"image_alt": "Warehouse stock that the storefront reads from ERPNext",
				"link_label": "See ERPNext",
				"link_href": "/software/erpnext",
				"sort_order": 2,
			},
			{
				"section_type": "Core Module",
				"heading": "Checkout, payments and ZATCA invoices",
				"body": (
					"Card gateways and cash-on-delivery both create an ERPNext sales invoice. "
					"VAT and ZATCA Phase 2 signing use the same invoice the finance team "
					"already knows — not a separate web-shop tax file."
				),
				"image": checkout,
				"image_alt": "Card payment at ecommerce checkout posted to ERPNext",
				"link_label": "See ZATCA Integration",
				"link_href": "/software/zatca-integration",
				"sort_order": 3,
			},
			{
				"section_type": "Core Module",
				"heading": "Aramex delivery with live customer status",
				"body": (
					"When the warehouse marks the order packed, the integration creates the "
					"Aramex shipment and stores the AWB on the ERPNext delivery note.\n\n"
					"Aramex status events — booked, picked up, in transit, out for delivery, "
					"delivered — write back to the order. The customer sees the same timeline "
					"in My Account and in the mobile app, without calling the store."
				),
				"image": delivery,
				"image_alt": "Last-mile delivery integrated with Aramex and ERPNext",
				"sort_order": 4,
			},
			{
				"section_type": "Core Module",
				"heading": "Android and iOS apps",
				"body": (
					"The mobile apps use the same ERPNext catalogue, cart, coupons and order "
					"history as the website. Customers get push updates when payment clears "
					"and when Aramex moves the parcel.\n\n"
					"Printechs publishes and maintains the Android and iOS builds for the "
					"merchant brand — ShoeArena is the reference store already in market."
				),
				"image": mobile,
				"image_alt": "Native Android and iOS shopping apps on the ERPNext store",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Promotions and multi-brand campaigns",
				"body": (
					"Sale landing pages, brand shops and category banners are content on the "
					"store, while price and stock remain ERPNext. That is how ShoeArena runs "
					"men, women, kids and dozens of brands without a second product master."
				),
				"image": kids,
				"image_alt": "Ipanema summer campaign banner from the live ShoeArena store",
				"link_label": "Talk to Our Software Team",
				"link_href": "/contact",
				"sort_order": 6,
			},
		],
	)

	related = []
	for sort, slug, label, summary, href, image in (
		(1, "erpnext", "ERPNext", "Items, stock, orders and invoices", "/software/erpnext", erpnext_image),
		(2, "modern-pos", "Modern POS", "Same stock at the store till", "/software/modern-pos", pos_image),
		(3, "zatca-integration", "ZATCA Integration", "Phase 2 invoices from web orders", "/software/zatca-integration", zatca_image),
		(4, "warehouse-management-system", "Warehouse Management", "Pick, pack and ship web orders", "/software/warehouse-management-system", wms_image),
	):
		name = published_name(slug)
		if not name:
			continue
		related.append(
			{
				"related_website_product": name,
				"display_name_override": label,
				"summary_override": summary,
				"href": href,
				"image": image,
				"sort_order": sort,
			}
		)
	doc.set("ecosystem_items", related)
	doc.set("related_products", related)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Store design",
				"description": "Catalogue structure, Arabic/English UX, and brand theme on web and apps.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "ERPNext & Aramex",
				"description": "Item sync, checkout posting, ZATCA invoices and Aramex AWB status.",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "App release",
				"description": "Android and iOS store listing, push notifications and updates.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Go-live support",
				"description": "Ops training and support from Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Is this a separate shop, or is it ERPNext?",
				"answer": (
					"The storefront is the customer face. Items, stock, prices, sales orders "
					"and invoices live in ERPNext. That is the same model running on ShoeArena."
				),
				"sort_order": 1,
			},
			{
				"question": "How does Aramex tracking reach the customer?",
				"answer": (
					"Packed orders create an Aramex shipment. Status events write back to the "
					"ERPNext delivery and show in My Account and the mobile app in real time."
				),
				"sort_order": 2,
			},
			{
				"question": "Are Android and iOS apps included?",
				"answer": (
					"Yes. The apps use the same catalogue, cart and order status as the website. "
					"Printechs builds and publishes them under the merchant brand."
				),
				"sort_order": 3,
			},
			{
				"question": "Can we see a live store?",
				"answer": (
					f"Yes. ShoeArena ({LIVE_STORE}) is a production store Printechs developed "
					"on this ERPNext e-commerce stack."
				),
				"sort_order": 4,
			},
			{
				"question": "Does web checkout create a ZATCA invoice?",
				"answer": (
					"Yes. The sales invoice is an ERPNext document, signed and submitted with "
					"the same ZATCA Phase 2 flow as counter or B2B sales."
				),
				"sort_order": 5,
			},
		],
	)

	doc.set("downloads", [])
	doc.set("package_contents", [])
	doc.set("full_specifications", [])
	doc.set("page_section_order", default_page_section_order_rows())

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
