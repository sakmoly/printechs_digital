# Copyright (c) 2026, Printechs and contributors
"""Create the Beauty Cloud salon page and refresh the ERPNext industry teaser."""

import frappe

from printechs_digital.setup.fill_erpnext import (
	copy_industry_image,
	copy_software_image,
	published_name,
)

BEAUTY_PATH = "/software/erpnext/beauty-salon-management"
WHATSAPP_HREF = "https://wa.me/966550733441"

PARENT_TEASER = (
	"Beauty Cloud manages the salon journey from booking and service execution to POS, "
	"consumables, commissions, packages and loyalty — with a mobile app and a paperless "
	"reception kiosk.\n\n"
	"Appointments, beauticians, inventory and accounting stay on one platform instead of "
	"separate salon and finance systems."
)

SECTION_ORDER = [
	"overview",
	"process_steps",
	"key_features",
	"benefits",
	"icon_specifications",
	"content_sections",
	"localization",
	"reports",
	"dashboard",
	"applications",
	"related_products",
	"support",
	"faqs",
]


def get_or_create_beauty():
	name = frappe.db.get_value("Website Product", {"slug": "beauty-salon-management"}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "Beauty Cloud"
	doc.display_name = "Beauty Cloud"
	doc.slug = "beauty-salon-management"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "ERP Software"
	doc.short_description = (
		"Beauty salon management software for appointments, beauticians, POS, "
		"inventory, commissions, packages and loyalty."
	)
	doc.long_description = "<p>Beauty Cloud</p>"
	doc.hero_image = copy_industry_image("industry-fashion.jpg")
	doc.hero_image_alt = "Beauty Cloud salon operations for appointments, POS and inventory"
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def _link_parent_beauty_section(parent_name: str):
	parent = frappe.get_doc("Website Product", parent_name)
	updated = False
	for row in parent.get("content_sections") or []:
		if (row.get("section_type") or "") != "Industry Solution":
			continue
		if (row.heading or "").strip().lower() != "beauty salon management":
			continue
		row.body = PARENT_TEASER
		row.link_label = ""
		row.link_href = BEAUTY_PATH
		updated = True
		break
	if updated:
		parent.flags.ignore_permissions = True
		parent.flags.ignore_validate = True
		parent.save()


def fill_erpnext_beauty_salon():
	parent_name = published_name("erpnext") or frappe.db.get_value(
		"Website Product", {"slug": "erpnext"}, "name"
	)
	if not parent_name:
		frappe.throw("ERPNext Website Product must exist before creating Beauty Cloud")

	hero = copy_industry_image("industry-fashion.jpg")
	pos = copy_software_image("software-modern-pos.jpg")
	mobile = copy_software_image("software-mobile-applications.jpg")
	dashboard = copy_software_image("software-erpnext.jpg")
	inventory = copy_software_image("software-warehouse-management-system.jpg")
	finance_img = copy_software_image("software-zatca-integration.jpg")

	doc = get_or_create_beauty()
	doc.website_product_name = "Beauty Cloud"
	doc.display_name = "Beauty Cloud"
	doc.slug = "beauty-salon-management"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.parent_software = parent_name
	doc.brand = "Printechs"
	doc.category = "ERP Software"
	doc.subcategory = "Industry Solutions"
	doc.category_label = "Beauty Salon Management Software"
	doc.tagline = "Beauty salon management software built for modern salon operations"
	doc.short_description = (
		"Manage appointments, customers, beauticians, service consumption, commissions, "
		"POS billing, inventory, packages, loyalty and business performance from one "
		"connected platform."
	)
	doc.long_description = (
		"Running a beauty salon is more than managing appointments. Every service involves "
		"customers, beauticians, products, consumables, commissions, inventory, payments "
		"and follow-up.\n\n"
		"Beauty Cloud by Printechs — powered by ERPNext — brings these operations together "
		"so management sees daily activity while the floor stays faster. From a haircut to "
		"a facial with several consumables, each transaction stays tied to the customer, "
		"beautician, inventory usage and bill.\n\n"
		"The same journey can stay paperless: customers book on the mobile app, check in at "
		"a reception kiosk, and leave with a digital invoice instead of printed slips moving "
		"between stations."
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Beauty Cloud salon software for appointments, beauticians, POS and inventory"
	)
	doc.hero_trust_chips = (
		"Appointments & Beauticians\nService Consumption\nMobile App & Reception Kiosk\nPOS, Packages & Loyalty"
	)
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Request a Demo"
	doc.hero_primary_cta_href = "/request-demo"
	doc.hero_secondary_cta_label = "Explore Beauty Cloud"
	doc.hero_secondary_cta_href = "/software/erpnext/beauty-salon-management#applications"
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 0
	doc.show_on_products_list = 0
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = "One platform for your complete salon operation"
	doc.card_title = "Beauty Cloud"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Appointments, beauticians, consumables, POS, packages and loyalty on one salon platform."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Ready to transform the way your salon operates?"
	doc.final_cta_description = (
		"Manage appointments, customers, beauticians, inventory, commissions, billing and "
		"performance from one Beauty Cloud platform — from appointment to accounting. "
		"Beauty Cloud by Printechs."
	)
	doc.final_cta_primary_label = "Request a Demo"
	doc.final_cta_primary_href = "/request-demo"
	doc.final_cta_secondary_label = "Talk to Our Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "Beauty Cloud | Beauty Salon Management Software Saudi Arabia | Printechs"
	doc.meta_description = (
		"Beauty Cloud salon software: appointments, beauticians, service consumption, "
		"commissions, POS, packages, loyalty, inventory and multi-branch control — plus a "
		"mobile app and paperless reception kiosk for salons in Saudi Arabia."
	)
	doc.canonical_path = BEAUTY_PATH
	doc.index_page = 1
	doc.published = 1
	doc.enable_product_tour = 0

	doc.set(
		"page_section_order",
		[{"section": section, "sort_order": idx} for idx, section in enumerate(SECTION_ORDER, start=1)],
	)

	doc.connection_heading = "Manage everything from one system"
	doc.connection_center_label = "Beauty Cloud — from appointment to accounting"
	doc.set(
		"connection_items",
		[
			{"title": "Appointments", "sort_order": 1},
			{"title": "Customers", "sort_order": 2},
			{"title": "Beauticians & Staff", "sort_order": 3},
			{"title": "Services & Consumables", "sort_order": 4},
			{"title": "Salon POS", "sort_order": 5},
			{"title": "Packages & Memberships", "sort_order": 6},
			{"title": "Loyalty & Wallet", "sort_order": 7},
			{"title": "Inventory & Purchasing", "sort_order": 8},
			{"title": "Mobile App", "sort_order": 9},
			{"title": "Reception Kiosk", "sort_order": 10},
			{"title": "HR & Payroll", "href": "/software/erpnext/hr-project-management", "sort_order": 11},
			{"title": "Accounting", "href": "/software/erpnext/finance", "sort_order": 12},
		],
	)

	doc.process_heading = "From appointment to accounting — everything connected"
	doc.process_subheading = (
		"No separate apps for appointments, POS, stock and commission. Customers can book "
		"on mobile, check in at a paperless kiosk, and pay at POS on the same visit."
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "Book",
				"title": "Book appointment → customer check-in",
				"description": "Customer picks a service, beautician and time — on the app, at a reception kiosk or with the receptionist — then arrival opens the visit.",
				"sort_order": 1,
			},
			{
				"group_title": "Serve",
				"title": "Assign beautician → perform service → consume products",
				"description": "The service is assigned by skill and availability. Standard consumables deduct from stock; the beautician can confirm actual usage.",
				"sort_order": 2,
			},
			{
				"group_title": "Pay",
				"title": "Complete service → POS checkout → payment & invoice",
				"description": "Services, retail, packages and membership benefits consolidate at POS — cash, card, Mada, wallet or loyalty — without re-typing the ticket.",
				"sort_order": 3,
			},
			{
				"group_title": "Retain",
				"title": "Commission → loyalty → next visit",
				"description": "Eligible commission posts automatically. Package balance, points and history update so the next booking is already on the profile.",
				"sort_order": 4,
			},
		],
	)

	doc.key_features_heading = "What Beauty Cloud covers on the salon floor"
	doc.set(
		"key_features",
		[
			{
				"icon": "report",
				"title": "Smart appointment calendar",
				"description": "Daily and weekly views by beautician, duration, shifts, conflict prevention, walk-ins, check-in, no-shows and rebooking.",
				"sort_order": 1,
			},
			{
				"icon": "loyalty",
				"title": "Beautician skills and performance",
				"description": "Profiles, service eligibility, shifts, attendance, sales, rebooking and service or retail commission on one employee.",
				"sort_order": 2,
			},
			{
				"icon": "inventory",
				"title": "Automatic service consumption",
				"description": "Each service can carry a standard recipe of products. Completion reduces stock; actual vs expected usage is visible.",
				"sort_order": 3,
			},
			{
				"icon": "zatca",
				"title": "Automated commissions",
				"description": "Percentage, fixed, employee-specific, retail, tier, package and membership rules — with reversal on refunds.",
				"sort_order": 4,
			},
			{
				"icon": "checkout",
				"title": "Salon POS and packages",
				"description": "Services, retail, packages, memberships, gift cards, wallet, split payments and Mada in one checkout.",
				"sort_order": 5,
			},
			{
				"icon": "android",
				"title": "Mobile app",
				"description": "Customers book, view history and keep the visit paperless. Staff can follow assigned services from the phone.",
				"sort_order": 6,
			},
			{
				"icon": "device",
				"title": "Reception kiosk",
				"description": "A paperless kiosk at reception for self check-in, appointment confirmation and queue — less paper at the desk.",
				"sort_order": 7,
			},
			{
				"icon": "store",
				"title": "Multi-branch control",
				"description": "Appointments, staff, prices, inventory and POS by branch, with consolidated performance for the group.",
				"sort_order": 8,
			},
		],
	)

	doc.set(
		"benefits",
		[
			{
				"icon": "speed",
				"title": "Fewer appointment conflicts",
				"description": "Duration, shifts and beautician calendars keep the book honest.",
				"sort_order": 1,
			},
			{
				"icon": "inventory",
				"title": "Know what each service consumes",
				"description": "Standard recipes and actual usage cut wastage and stock leakage.",
				"sort_order": 2,
			},
			{
				"icon": "zatca",
				"title": "Commission without spreadsheets",
				"description": "Rules post when the visit is complete and reverse on refunds.",
				"sort_order": 3,
			},
			{
				"icon": "device",
				"title": "Paperless reception",
				"description": "Mobile booking plus a kiosk at reception — check-in without printed slips.",
				"sort_order": 4,
			},
			{
				"icon": "loyalty",
				"title": "Customers come back",
				"description": "Packages, memberships, points, wallet and rebooking stay on the profile.",
				"sort_order": 5,
			},
			{
				"icon": "report",
				"title": "Real service profitability",
				"description": "Revenue minus consumables minus commission — by service and branch.",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{"icon": "report", "title": "Appointments", "description": "Calendar, status and rebooking", "sort_order": 1},
			{"icon": "loyalty", "title": "Beauticians", "description": "Skills, shifts and performance", "sort_order": 2},
			{"icon": "print", "title": "Services", "description": "Price, duration and recipe", "sort_order": 3},
			{"icon": "inventory", "title": "Consumables", "description": "Expected vs actual usage", "sort_order": 4},
			{"icon": "checkout", "title": "Salon POS", "description": "Services, retail and Mada", "sort_order": 5},
			{"icon": "cloud", "title": "Packages", "description": "Sessions and redemptions", "sort_order": 6},
			{"icon": "shield", "title": "Memberships", "description": "Prices and renewals", "sort_order": 7},
			{"icon": "loyalty", "title": "Loyalty & wallet", "description": "Points, credit and gifts", "sort_order": 8},
			{"icon": "store", "title": "Inventory", "description": "Retail and back-bar stock", "sort_order": 9},
			{"icon": "android", "title": "Mobile app", "description": "Book and follow the visit", "sort_order": 10},
			{"icon": "device", "title": "Reception kiosk", "description": "Paperless self check-in", "sort_order": 11},
			{"icon": "integration", "title": "ERPNext back office", "description": "Accounts, HR and purchase", "sort_order": 12},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Smart appointment management",
				"body": (
					"Simplify appointments. Reduce conflicts. Improve staff utilization. The "
					"calendar is built for salon work: daily and weekly views, appointment by "
					"beautician, service duration, availability, shift hours, conflict prevention, "
					"walk-ins, check-in, reschedule, cancel, no-show, preferred beautician, "
					"multiple services, room or chair, reminders and rebooking.\n\n"
					"Status moves Booked → Confirmed → Arrived → Waiting → In Service → "
					"Completed — or Cancelled / No Show. Customers can book on the mobile app "
					"or confirm at the reception kiosk so the desk stays paperless."
				),
				"image": dashboard,
				"image_alt": "Beauty Cloud appointment calendar by beautician and service duration",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Beauticians, services and consumable recipes",
				"body": (
					"Put the right beautician on the right service. Each person has a profile, "
					"skill level, service eligibility, shifts, attendance, leave, hours, assigned "
					"and completed work, sales, rebooking, and service or retail commission.\n\n"
					"Every service carries name, category, price, tax, duration, required skill, "
					"branch, room or chair, equipment, standard consumables and commission rule — "
					"hair cutting and colouring, facial, waxing, nails, makeup, massage and "
					"treatments. A Premium Facial can deduct cleanser 10 ml, scrub 8 g, mask 15 g, "
					"serum 3 ml and a headband when the visit completes, or the beautician can "
					"confirm a different actual quantity."
				),
				"image": inventory,
				"image_alt": "Service recipes and beautician skill assignment in Beauty Cloud",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Beautician stock and automated commission",
				"body": (
					"Professional products often leave the main store into beautician custody. "
					"Track Main Salon Stock → Issue to Beautician → Services → Expected "
					"consumption → Actual consumption → Remaining beautician stock. Compare "
					"expected versus actual to see variance or excess usage.\n\n"
					"Commission no longer lives in a spreadsheet: percentage or fixed by service, "
					"employee-specific, product, tier, team, package or membership. Example: "
					"Premium Facial SAR 250 at 12% posts when the visit is complete; refunds can "
					"reverse the line automatically."
				),
				"image": dashboard,
				"image_alt": "Beautician stock variance and commission rules",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Customer 360°, POS, packages and loyalty",
				"body": (
					"The customer profile holds contact details, preferred branch and beautician, "
					"services, appointment and purchase history, package balances, membership, "
					"loyalty, wallet, discounts, feedback, last visit, next appointment, average "
					"spend and visit frequency.\n\n"
					"POS combines services, retail, packages, memberships, gift cards, loyalty "
					"redemption, wallet, discounts, split payments, cash, card, Mada and returns. "
					"A 6-session facial package shows purchased, used and remaining sessions. "
					"Memberships can carry member prices, included services, priority booking and "
					"renewal on the same profile."
				),
				"image": pos,
				"image_alt": "Beauty Cloud POS for services, packages, wallet and Mada",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Mobile app and paperless reception kiosk",
				"body": (
					"Beauty Cloud is built for a paperless salon floor. Customers use the mobile "
					"app to book, choose a beautician, see upcoming visits and keep history on "
					"their phone — no paper appointment card.\n\n"
					"A kiosk at reception lets arriving guests check in, confirm the service and "
					"join the queue without a printed slip. Beauticians start and complete "
					"services digitally; checkout sends a digital invoice. Paper stays the "
					"exception, not the process."
				),
				"image": mobile,
				"image_alt": "Beauty Cloud mobile app and paperless reception kiosk",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Retail, back-bar inventory and purchasing",
				"body": (
					"Control both products you sell and products you consume. Retail covers "
					"shampoo, serums, creams and cosmetics. Professional / back-bar covers colour, "
					"developer, wax, masks, treatment creams and disposables — plus beautician "
					"stock, service consumption and wastage.\n\n"
					"Stock by branch and warehouse, transfers, counts, reorder alerts, batch and "
					"expiry, purchase request through receipt and supplier invoice. Replenish "
					"from actual usage instead of overstocking the back room."
				),
				"image": inventory,
				"image_alt": "Retail and professional salon inventory with purchase",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Service profitability, HR and accounting",
				"body": (
					"Service revenue alone does not show profit. Beauty Cloud can compare Service "
					"Revenue minus Consumable Cost minus Beautician Commission to get service "
					"contribution — so you see which treatments actually earn.\n\n"
					"HR and payroll cover records, attendance, shifts, leave, salary, commission, "
					"incentives, deductions and advances. Approved commission can move into "
					"payroll. Because Beauty Cloud sits on ERPNext, sales, payments, payables, "
					"VAT, cash, bank, stock valuation, P&L and branch financials stay in the "
					"same books — not a second accounting product."
				),
				"image": finance_img,
				"image_alt": "Service contribution, payroll commission and salon financials",
				"sort_order": 7,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Multi-branch, roles and Beauty Cloud + ERPNext",
				"body": (
					"Growing groups manage appointments, beauticians, customers, services, "
					"pricing, inventory, cashiers, POS, sales and expenses by branch, then view "
					"consolidated performance. Receptionists see bookings and check-in; "
					"beauticians see assigned work and consumption; cashiers close POS; managers "
					"approve discounts and commissions; owners see revenue, retention and KPIs.\n\n"
					"Beauty Cloud extends ERPNext with salon workflows and grows with accounting, "
					"inventory, purchasing, CRM, HR, payroll, payments, reporting, a customer "
					"portal and e-commerce in later phases — instead of another isolated salon app."
				),
				"image": dashboard,
				"image_alt": "Multi-branch salon performance on Beauty Cloud and ERPNext",
				"sort_order": 8,
			},
		],
	)

	doc.localization_heading = "Built for beauty businesses in Saudi Arabia"
	doc.localization_body = (
		"Configure Beauty Cloud for salon operations in Saudi Arabia: Arabic and English, "
		"Saudi VAT, ZATCA e-invoicing integration, Mada and card payments, multi-branch "
		"control, role-based security and local implementation support from Printechs — "
		"on the same ERPNext back office as the rest of the company."
	)
	doc.localization_chips = (
		"Arabic & English\nSaudi VAT\nZATCA Integration\nMada & Card Payments\nMulti-Branch\nLocal Support"
	)

	doc.reports_heading = "Turn daily salon activity into management information"
	doc.reports_image = dashboard
	doc.reports_image_alt = "Beauty Cloud reports for sales, appointments, commission and stock"
	doc.set(
		"report_items",
		[
			{"title": title, "sort_order": idx}
			for idx, title in enumerate(
				[
					"Daily sales",
					"Service and retail revenue",
					"Appointments and no-shows",
					"Beautician productivity",
					"Staff utilization",
					"Commission",
					"Top services and products",
					"Customer retention",
					"Rebooking rate",
					"Package sales and redemptions",
					"Inventory consumption",
					"Stock variance",
					"Branch performance",
					"Average customer spend",
				],
				start=1,
			)
		],
	)

	doc.dashboard_heading = "See the salon as it runs — not at month end"
	doc.dashboard_body = (
		"Watch daily sales, service versus retail mix, completed visits, cancellations, "
		"no-shows, beautician load, commission, top services, package redemptions, "
		"consumption, stock variance, branch performance and average spend while the floor "
		"is still open."
	)
	doc.dashboard_image = dashboard
	doc.dashboard_image_alt = "Beauty Cloud dashboard with sales, appointments and staff KPIs"

	doc.audience_heading = "Built for salons, spas and wellness groups"
	doc.set(
		"audience_items",
		[
			{"title": "Hair salons", "description": "Cuts, colour, treatments, chair allocation and retail.", "sort_order": 1},
			{"title": "Beauty salons", "description": "Facials, waxing, makeup and multi-step consumable recipes.", "sort_order": 2},
			{"title": "Nail studios", "description": "Manicure, pedicure and treatment sessions with timed chairs.", "sort_order": 3},
			{"title": "Spas & wellness", "description": "Massage and skin treatments with room booking and packages.", "sort_order": 4},
			{"title": "Multi-branch groups", "description": "Shared customers and loyalty with stock and POS per location.", "sort_order": 5},
			{"title": "Ladies' salons", "description": "Preferred beautician, privacy-aware booking and memberships.", "sort_order": 6},
			{"title": "Barbers & men's grooming", "description": "Walk-ins, kiosk check-in and fast POS.", "sort_order": 7},
			{"title": "Franchise networks", "description": "Central pricing, commission rules and branch scorecards.", "sort_order": 8},
		],
	)

	doc.integration_heading = "Beauty Cloud + ERPNext back office"
	related = [
		{
			"related_website_product": published_name("modern-pos"),
			"display_name_override": "Modern POS",
			"summary_override": "Retail checkout connected to the same stock",
			"href": "/software/modern-pos",
			"sort_order": 1,
		},
		{
			"related_website_product": frappe.db.get_value("Website Product", {"slug": "finance"}, "name"),
			"display_name_override": "Finance",
			"summary_override": "VAT, ZATCA and salon P&L",
			"href": "/software/erpnext/finance",
			"sort_order": 2,
		},
		{
			"display_name_override": "Inventory",
			"summary_override": "Retail and back-bar warehouses",
			"href": "/software/erpnext/inventory",
			"sort_order": 3,
		},
		{
			"display_name_override": "HR & Payroll",
			"summary_override": "Shifts, leave and commission in payroll",
			"href": "/software/erpnext/hr-project-management",
			"sort_order": 4,
		},
	]
	doc.set("related_products", [row for row in related if row.get("href")])

	doc.implementation_heading = "Why Beauty Cloud?"
	doc.implementation_cta_label = "WhatsApp Us"
	doc.implementation_cta_href = WHATSAPP_HREF
	doc.set(
		"support_items",
		[
			{"icon": "loyalty", "title": "Complete customer journey", "description": "From booking and kiosk check-in to POS, loyalty and the next visit.", "sort_order": 1},
			{"icon": "report", "title": "Fewer conflicts, better utilization", "description": "Calendars, skills and duration keep the book and the floor aligned.", "sort_order": 2},
			{"icon": "inventory", "title": "Consumables you can trust", "description": "Recipes, beautician stock and variance instead of leakage.", "sort_order": 3},
			{"icon": "zatca", "title": "Commission in the system", "description": "Rules post with the visit and flow toward payroll.", "sort_order": 4},
			{"icon": "device", "title": "Mobile app and reception kiosk", "description": "Paperless booking and self check-in at the front desk.", "sort_order": 5},
			{"icon": "store", "title": "Multi-branch ready", "description": "POS, stock and staff by location with group dashboards.", "sort_order": 6},
			{"icon": "integration", "title": "ERPNext back office", "description": "Accounting, purchase, HR and reporting as the salon grows.", "sort_order": 7},
			{"icon": "training", "title": "Saudi implementation", "description": "Arabic/English, VAT, ZATCA, Mada and local support.", "sort_order": 8},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Is Beauty Cloud only an appointment book?",
				"answer": (
					"<p>No. It covers the full salon operation: appointments, beauticians, "
					"service recipes, consumables, POS, packages, loyalty, inventory, commission, "
					"HR and accounting on ERPNext.</p>"
				),
				"sort_order": 1,
			},
			{
				"question": "Can customers book on a mobile app?",
				"answer": (
					"<p>Yes. Customers can book a service and beautician from the mobile app, "
					"see upcoming visits and keep history on their phone.</p>"
				),
				"sort_order": 2,
			},
			{
				"question": "What does the reception kiosk do?",
				"answer": (
					"<p>The kiosk at reception is for paperless self check-in: confirm the "
					"appointment, join the queue and start the visit without a printed slip.</p>"
				),
				"sort_order": 3,
			},
			{
				"question": "How does service consumption work?",
				"answer": (
					"<p>Each service can have a standard product recipe. When the visit completes, "
					"stock reduces automatically. Beauticians can confirm a different actual "
					"quantity so you compare expected versus used.</p>"
				),
				"sort_order": 4,
			},
			{
				"question": "Can commission go to payroll?",
				"answer": (
					"<p>Yes. Configurable commission posts with the completed visit and approved "
					"amounts can transfer into the ERPNext payroll process.</p>"
				),
				"sort_order": 5,
			},
			{
				"question": "Is it ready for Saudi salons?",
				"answer": (
					"<p>Beauty Cloud can be configured for Arabic and English, Saudi VAT, ZATCA "
					"e-invoicing integration, Mada and card payments, and multi-branch operations "
					"with Printechs implementation support.</p>"
				),
				"sort_order": 6,
			},
		],
	)

	doc.set("visual_story_items", [])
	doc.set("capability_items", [])

	doc.flags.ignore_permissions = True
	doc.save()
	_link_parent_beauty_section(parent_name)
	return {"slug": "beauty-salon-management", "canonical_path": doc.canonical_path}
