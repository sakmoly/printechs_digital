# Copyright (c) 2026, Printechs and contributors
"""XTi100–XTi600 model builders for the Avery Berkel lineup fill."""

from printechs_digital.setup.fill_avery_berkel_lineup import _ksa, _xt_model, support_items


def xti_models(m, r, food, bakery):
	return [
		_xti100(m, r, food),
		_xti200(m, r, food),
		_xti300(m, r, food),
		_xti400(m, r, food),
		_xti420(m, r, food),
		_xti600(m, r, bakery),
	]


def _xti100(m, r, food):
	return _xt_model(
		"avery-berkel-xti100", "Avery Berkel XTi100", "RET.SYS.AVR.4189",
		"Premium Touchscreen Scales", "TOUCHSCREEN RETAIL WEIGHING SCALE", "xti100", 0,
		tagline="Premium 10.1-inch monobloc — large touch where height is limited",
		short="Avery Berkel XTi100 delivers the advanced XT touchscreen in a compact monobloc: 10.1-inch operator display, 7-inch customer display, cassette printer and ValuMax. Capacities include 15 kg AVR on this Item, plus 6 kg and 30 kg family options.",
		long=(
			"<p>XTi100 is the premium monobloc: 10.1-inch operator touch, 7-inch customer "
			"display, cassette label/receipt printer, Ethernet, compatible Wi-Fi, five USB "
			"ports, Linux and linerless support. ValuMax keeps weighing accurate on an "
			"uneven counter. Avery Berkel lists 15 kg, 6 kg and 30 kg AVR for the model.</p>"
			"<p>This page is RET.SYS.AVR.4189 (XTi100 15 kg AVR, 10/7). Eco III 4603 is a "
			"different Item. Not XTs100 (7-inch) and not XTi200 (raised customer display).</p>"
			f"<p>{_ksa('XTi100')}</p>"
		),
		hero_alt="Avery Berkel XTi100 10.1-inch monobloc touchscreen scale",
		chips="10.1-inch operator touch\n7-inch customer display\n15 kg AVR this Item\nValuMax · 5× USB",
		story="Large-screen XTi without a tower",
		visual="XTi100",
		card_title="XTi100",
		card_summary="Premium 10.1-inch monobloc touchscale with 7-inch customer display. 15 kg AVR.",
		cta_h="Quote Avery Berkel XTi100",
		cta_d="Confirm 15 kg vs 6/30 kg family options and 4189 vs Eco III 4603.",
		meta_title="Avery Berkel XTi100 Touchscreen Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTi100 premium touchscreen retail weighing and label printing scale with customer display for supermarkets and fresh-food retailers in KSA.",
		benefits=[
			{"icon": "display", "title": "10.1-inch operator", "description": "Larger PLU photos than XTs100 in the same monobloc idea.", "sort_order": 1},
			{"icon": "device", "title": "Low height", "description": "Premium touch when a tower will not fit.", "sort_order": 2},
			{"icon": "speed", "title": "ValuMax", "description": "Automatic level correction on this weighing model.", "sort_order": 3},
			{"icon": "print", "title": "XT cassette printer", "description": "150 mm/sec-class, edge-to-edge, linerless options.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTi100", "image": m["xti100"], "image_alt": "XTi100", "caption": "10.1-inch monobloc — not XTs100.", "sort_order": 1},
			{"label": "Fresh food", "image": food, "image_alt": "Fresh food", "caption": "Supermarket and speciality counters.", "sort_order": 2},
			{"label": "Retail", "image": r, "image_alt": "Retail", "caption": "Linux XT with five USB ports.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "Operator", "description": "10.1-inch touch", "sort_order": 1},
			{"icon": "display", "title": "Customer", "description": "7-inch colour", "sort_order": 2},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 3},
			{"icon": "connectivity", "title": "USB", "description": "Five interfaces", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4189 — XTi100 15 kg AVR, 10/7"),
				("Also quote", "6 kg / 30 kg AVR family; Eco III 4603"),
				("Not this page", "XTs100, XTi200, XTi101 (no customer display)"),
			]),
			("Platform", [
				("OS / I/O", "Linux; Ethernet; compatible Wi-Fi; 5× USB"),
				("Print", "Cassette thermal; linerless support"),
			]),
		],
		apps=[
			{"title": "Compact premium counters", "description": "XTi screen without a column.", "image": food, "image_alt": "Counter", "industry_link": "retail", "sort_order": 1},
			{"title": "Supermarkets", "description": "Colour PLUs on a short run.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 2},
			{"title": "Speciality food", "description": "Large touch, small height.", "image": m["xti100"], "image_alt": "XTi100", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTi100 technology", "body": "10.1-inch XTi monobloc with ValuMax and five USB ports. Not the 7-inch XTs100.", "image": m["xti100"], "image_alt": "XTi100", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTi100 in KSA", "body": _ksa("XTi100"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "XTi100 or XTs100?", "answer": "XTi100 is 10.1/7. XTs100 is 7/7. Same monobloc idea, different screen class.", "sort_order": 1},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.4189, 15 kg AVR 10/7. Eco III is 4603.", "sort_order": 2},
			{"question": "6 kg or 30 kg?", "answer": "Family options. This page’s Item is 15 kg AVR. Ask if you need the others.", "sort_order": 3},
		],
		support=support_items("10/7 monobloc vs Eco III.", "Cassette labels.", "ValuMax.", "Large-touch PLUs."),
		pack=[{"item_description": "XTi100 15 kg AVR 10/7 as Item 4189", "sort_order": 1}],
	)


def _xti200(m, r, food):
	return _xt_model(
		"avery-berkel-xti200", "Avery Berkel XTi200", "RET.SYS.AVR.4190",
		"Premium Touchscreen Scales", "TOUCHSCREEN RETAIL SCALE", "xti200", 1,
		tagline="10.1-inch operator touch with a raised 7-inch customer display",
		short="Avery Berkel XTi200 is the general-purpose premium retail scale: 10.1-inch operator touchscreen, raised 7-inch customer display, cassette printing and MXBusiness. Strong for supermarket and speciality food counters in Saudi Arabia.",
		long=(
			"<p>XTi200 gives customers a clear view of name, weight and price and a place "
			"to show promotions during service. It supports counter labelling, pre-pack "
			"and other XT retail modes. 15 kg AVR, ValuMax, cassette printer, Ethernet/Wi-Fi, "
			"CodeChecker and 150 mm/sec-class printing.</p>"
			"<p>This page is RET.SYS.AVR.4190 (XTi200 15 kg AVR, 10/7). Eco III 4604 is a "
			"different Item. Featured as the everyday XTi for KSA stores.</p>"
			f"<p>{_ksa('XTi200')}</p>"
		),
		hero_alt="Avery Berkel XTi200 with raised customer display",
		chips="10.1-inch operator\nRaised 7-inch customer\n15 kg AVR this Item\nFeatured general-purpose XTi",
		story="The everyday premium XTi",
		visual="XTi200",
		card_title="XTi200",
		card_summary="Featured 10.1-inch XTi with raised customer display. 15 kg AVR, 10/7.",
		cta_h="Quote Avery Berkel XTi200",
		cta_d="Confirm 10/7 raised customer display and 4190 vs Eco III 4604.",
		meta_title="Avery Berkel XTi200 Retail Weighing Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTi200 retail touchscreen weighing scale with raised customer display, fast label printing and centralized retail management support.",
		benefits=[
			{"icon": "display", "title": "10.1-inch + raised 7-inch", "description": "Operator canvas and a customer-facing promotion screen.", "sort_order": 1},
			{"icon": "store", "title": "General-purpose XTi", "description": "Labelling, pre-pack and service modes on one Item.", "sort_order": 2},
			{"icon": "loyalty", "title": "Advertising during service", "description": "Use the raised colour display for offers, not only totals.", "sort_order": 3},
			{"icon": "cloud", "title": "MXBusiness", "description": "Central products and prices.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTi200", "image": m["xti200"], "image_alt": "XTi200", "caption": "Raised customer display on the 10.1-inch operator.", "sort_order": 1},
			{"label": "Promotions", "image": m["xti200_advert"], "image_alt": "Advert display", "caption": "Full-colour offers while the shopper waits.", "sort_order": 2},
			{"label": "Supermarket", "image": food, "image_alt": "Retail", "caption": "Featured general-purpose model for KSA.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "Operator", "description": "10.1-inch touch", "sort_order": 1},
			{"icon": "display", "title": "Customer", "description": "Raised 7-inch", "sort_order": 2},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 3},
			{"icon": "print", "title": "Print", "description": "Cassette · 150 mm/s", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4190 — XTi200 15 kg AVR, 10/7"),
				("Also quote", "Eco III 4604 — different Item"),
				("Not this page", "XTs200, XTi400 tower, XTi100 monobloc"),
			]),
			("Retail modes", [
				("Supported", "Counter labelling, pre-pack and other XT modes"),
				("Network", "Ethernet / Wi-Fi; MXBusiness"),
			]),
		],
		apps=[
			{"title": "Supermarket counters", "description": "Featured everyday XTi.", "image": food, "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 1},
			{"title": "Speciality food", "description": "Promotions on the raised display.", "image": m["xti200_advert"], "image_alt": "Advert", "industry_link": "retail", "sort_order": 2},
			{"title": "Pre-pack", "description": "Same station for service and batch labels.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTi200 technology", "body": "Raised customer advertising on the 10.1-inch XTi. Featured general-purpose model for Printechs.", "image": m["xti200"], "image_alt": "XTi200", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTi200 in Jeddah, Riyadh and Dammam", "body": "Avery Berkel XTi200 retail weighing scale in Saudi Arabia — " + _ksa("XTi200"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "Why is XTi200 featured?", "answer": "It is the balanced premium attended scale: large operator touch, raised customer display, one cassette printer.", "sort_order": 1},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.4190. Eco III is 4604.", "sort_order": 2},
			{"question": "XTi200 or XTi400?", "answer": "XTi400 raises the operator display too. XTi200 keeps the 10.1-inch screen on the deck.", "sort_order": 3},
		],
		support=support_items("10/7 vs Eco III.", "Cassette + advert content.", "Customer glass.", "Service vs pre-pack modes."),
		pack=[{"item_description": "XTi200 15 kg AVR 10/7 as Item 4190", "sort_order": 1}],
	)


def _xti300(m, r, food):
	return _xt_model(
		"avery-berkel-xti300", "Avery Berkel XTi300", "RET.SYS.AVR.4191",
		"Self-Service Scales", "SELF-SERVICE WEIGHING SCALE", "xti300", 1,
		tagline="18.5-inch self-service — shoppers weigh produce and print their own label",
		short="Avery Berkel XTi300 is the XT self-service scale: an 18.5-inch touchscreen for categories, product photos and buttons so customers identify items, weigh them and print labels. 15 kg AVR with ValuMax.",
		long=(
			"<p>Avery Berkel officially identifies XTi300 as the 18.5-inch self-service "
			"model. Fruit and vegetable departments, zero-waste stores and self-service "
			"fresh-food areas are the fit. Cassette printer, Ethernet/Wi-Fi, central "
			"product/price updates, images, barcode/QR and configurable workflows.</p>"
			"<p>This page is RET.SYS.AVR.4191 (XTi300 15 kg, OAR). Primary SEO keyword: "
			"self service weighing scale Saudi Arabia. Not a staffed XTi400 and not XTs.</p>"
			f"<p>{_ksa('XTi300')}</p>"
		),
		hero_alt="Avery Berkel XTi300 18.5-inch self-service produce scale",
		chips="18.5-inch self-service touch\n15 kg AVR this Item\nValuMax · cassette printer\nProduce / zero-waste",
		story="Shoppers weigh, you keep the queue moving",
		visual="XTi300",
		card_title="XTi300",
		card_summary="Featured 18.5-inch self-service produce scale. 15 kg AVR.",
		cta_h="Quote Avery Berkel XTi300",
		cta_d="Confirm produce photos, languages and Item 4191 placement in the aisle.",
		meta_title="Avery Berkel XTi300 Self Service Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTi300 self-service touchscreen weighing and label printing scale with large 18.5-inch display for supermarkets and fresh-food departments.",
		benefits=[
			{"icon": "display", "title": "18.5-inch canvas", "description": "Photos and large buttons for shoppers, not staff keys.", "sort_order": 1},
			{"icon": "loyalty", "title": "Self-service produce", "description": "Identify, weigh, print — faster checkout scanning.", "sort_order": 2},
			{"icon": "print", "title": "Fast labels", "description": "Same XT cassette printer as attended models.", "sort_order": 3},
			{"icon": "cloud", "title": "Central updates", "description": "Push new produce photos and prices from MXBusiness.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTi300", "image": m["xti300"], "image_alt": "XTi300", "caption": "18.5-inch self-service — not a staffed tower.", "sort_order": 1},
			{"label": "Produce", "image": food, "image_alt": "Produce", "caption": "Fruit, vegetables and zero-waste.", "sort_order": 2},
			{"label": "Aisle", "image": r, "image_alt": "Retail", "caption": "Self service weighing scale Saudi Arabia.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "Screen", "description": "18.5-inch touch", "sort_order": 1},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Cassette label", "sort_order": 3},
			{"icon": "loyalty", "title": "Mode", "description": "Self-service", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4191 — XTi300 15 kg, OAR"),
				("Not this page", "Staffed XTi400/XTi200, hanging XTs500"),
			]),
			("Self-service", [
				("Display", "18.5-inch touchscreen"),
				("Workflow", "Select photo → weigh → print barcode/QR label"),
			]),
		],
		apps=[
			{"title": "Fruit and vegetables", "description": "The defining XTi300 department.", "image": food, "image_alt": "Produce", "industry_link": "retail", "sort_order": 1},
			{"title": "Zero-waste", "description": "Customers buy only what they need.", "image": m["xti300"], "image_alt": "XTi300", "industry_link": "retail", "sort_order": 2},
			{"title": "Self-scan stores", "description": "Labels ready for SCO or handheld checkout.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTi300 technology", "body": "18.5-inch self-service XT. Featured distinctive application for Printechs — not a staffed deli scale.", "image": m["xti300"], "image_alt": "XTi300", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "Self-service weighing in KSA", "body": "Self service weighing scale Saudi Arabia: " + _ksa("XTi300"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "Is XTi300 for staff?", "answer": "No. It is the shopper-facing 18.5-inch self-service model.", "sort_order": 1},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.4191, 15 kg OAR.", "sort_order": 2},
			{"question": "Optional camera?", "answer": "XT self-service can take an optional item camera. Ask if that option is required on the quote.", "sort_order": 3},
		],
		support=support_items("Aisle placement and photo set.", "Produce label stock.", "Screen and printer.", "Shopper languages."),
		pack=[{"item_description": "XTi300 15 kg as Item 4191", "sort_order": 1}],
	)


def _xti400(m, r, food):
	return _xt_model(
		"avery-berkel-xti400", "Avery Berkel XTi400", "RET.SYS.AVR.4192",
		"Premium Touchscreen Scales", "PREMIUM RETAIL WEIGHING SCALE", "xti400", 1,
		tagline="Raised 10.1-inch operator and customer displays for premium counters",
		short="Avery Berkel XTi400 raises both displays above the platter so operators keep eye contact and the working area stays clear. 10.1-inch operator touch; 7-inch customer on this Item, 10.1-inch customer as Item 4221.",
		long=(
			"<p>XTi400 is the premium attended tower: 10.1-inch operator touchscreen, "
			"choice of 7-inch or 10.1-inch customer display, 15 kg AVR, ValuMax, cassette "
			"printer, multimedia advertising, Ethernet/Wi-Fi, USB and central management.</p>"
			"<p>This page is RET.SYS.AVR.4192 (XTi400 15 kg AVR, 10/7). RET.SYS.AVR.4221 "
			"is the 10/10 customer-display Item — quote it when both faces should be 10.1-inch. "
			"Eco III 4605 is another stock line. Dual printers are XTi420, not this page.</p>"
			f"<p>{_ksa('XTi400')}</p>"
		),
		hero_alt="Avery Berkel XTi400 raised 10.1-inch retail scale",
		chips="Raised 10.1-inch operator\n7-inch customer this Item\n15 kg AVR · ValuMax\nFeatured supermarket/deli tower",
		story="Premium eye-level XTi, one cassette printer",
		visual="XTi400",
		card_title="XTi400",
		card_summary="Featured raised 10.1-inch XTi tower. 15 kg AVR, 10/7 on this Item.",
		cta_h="Quote Avery Berkel XTi400",
		cta_d="Confirm 10/7 (4192) vs 10/10 (4221) and whether you actually need XTi420 dual printers.",
		meta_title="Avery Berkel XTi400 Retail Scale Saudi Arabia | Touchscreen Label Scale",
		meta_desc="Avery Berkel XTi400 touchscreen weighing scale with elevated operator and customer displays, label printing and advanced retail connectivity.",
		benefits=[
			{"icon": "display", "title": "Raised 10.1-inch", "description": "Operator and customer information at conversation height.", "sort_order": 1},
			{"icon": "device", "title": "Clear platter", "description": "Reduced footprint tower for premium counters.", "sort_order": 2},
			{"icon": "loyalty", "title": "Multimedia customer", "description": "7-inch on 4192; 10.1-inch customer on 4221.", "sort_order": 3},
			{"icon": "print", "title": "Single cassette", "description": "Need two printers? Specify XTi420.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTi400", "image": m["xti400"], "image_alt": "XTi400", "caption": "Raised 10.1-inch, one printer.", "sort_order": 1},
			{"label": "Service", "image": m["xti_series_counter"], "image_alt": "Counter", "caption": "Featured deli/butchery tower.", "sort_order": 2},
			{"label": "Supermarket", "image": food, "image_alt": "Retail", "caption": "Saudi premium fresh food.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "Operator", "description": "Raised 10.1-inch", "sort_order": 1},
			{"icon": "display", "title": "Customer", "description": "7-inch this Item", "sort_order": 2},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR", "sort_order": 3},
			{"icon": "print", "title": "Print", "description": "Single cassette", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4192 — XTi400 15 kg AVR, 10/7"),
				("Also quote", "4221 is 10/10; Eco III 4605"),
				("Not this page", "XTi420 dual printer, XTs400, XTi200"),
			]),
			("Displays", [
				("Operator", "10.1-inch colour touch, raised"),
				("Customer", "7-inch on 4192; 10.1-inch on 4221"),
			]),
		],
		apps=[
			{"title": "Supermarket deli", "description": "Featured attended tower.", "image": food, "image_alt": "Deli", "industry_link": "retail", "sort_order": 1},
			{"title": "Butchery", "description": "Eye contact, clear platter.", "image": m["xti_series_counter"], "image_alt": "Butchery", "industry_link": "retail", "sort_order": 2},
			{"title": "Cheese counters", "description": "Premium presentation.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTi400 technology", "body": "Raised XTi with ValuMax and one cassette. Featured supermarket/deli/butchery scale for Printechs.", "image": m["xti400"], "image_alt": "XTi400", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTi400 in Saudi Arabia", "body": _ksa("XTi400"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "4192 or 4221?", "answer": "4192 is 10/7 (this page). 4221 is 10/10. Same XTi400 family, different customer screen.", "sort_order": 1},
			{"question": "XTi400 or XTi420?", "answer": "XTi420 adds a second printer. Use 400 when one cassette is enough.", "sort_order": 2},
			{"question": "XTi400 or XTs400?", "answer": "XTi400 is 10.1-inch operator. XTs400 is 7-inch operator.", "sort_order": 3},
		],
		support=support_items("10/7 vs 10/10.", "Cassette media.", "Tower glass.", "Premium service."),
		pack=[{"item_description": "XTi400 15 kg AVR 10/7 as Item 4192", "sort_order": 1}],
	)


def _xti420(m, r, food):
	return _xt_model(
		"avery-berkel-xti420", "Avery Berkel XTi420", "",
		"Premium Touchscreen Scales", "DUAL PRINTER RETAIL WEIGHING SCALE", "xti420", 1,
		tagline="Flagship dual-printer XTi — weigh, label and receipt/POS at one station",
		short="Avery Berkel XTi420 is the reduced-footprint dual-printer premium scale: 10.1- or 13.1-inch operator touch, 10.1-inch customer display, two integrated printers and 15 kg AVR. The clearest Printechs Smart Retail workstation in the family.",
		long=(
			"<p>XTi420 is one of the most capable attended models in XTi. Avery Berkel’s "
			"technical documentation identifies it as the reduced-footprint model with dual "
			"label/receipt printers. Operator touch is approximately 10.1 or 13.1 inches "
			"with a 10.1-inch customer display. 15 kg AVR, ValuMax, high-speed thermal "
			"printing, Ethernet and compatible Wi-Fi, customer advertising, POS/receipt "
			"applications and central management.</p>"
			"<p>No XTi420 Item is listed yet — do not use XTi400 4192 as this page. "
			"Printechs features XTi420 because the business advantage is obvious: weigh + "
			"label + receipt/POS from one workstation, including Jeddah, Riyadh and Dammam "
			"supermarket and butchery counters.</p>"
			f"<p>{_ksa('XTi420')}</p>"
		),
		hero_alt="Avery Berkel XTi420 dual-printer premium retail scale",
		chips="Dual printers\n10.1 or 13.1-inch operator\n10.1-inch customer display\n15 kg AVR · featured flagship",
		story="Weigh, label and ticket without changing media",
		visual="XTi420",
		card_title="XTi420",
		card_summary="Featured dual-printer XTi workstation. 10.1/13.1-inch operator, 10.1-inch customer.",
		cta_h="Quote Avery Berkel XTi420",
		cta_d="Confirm 10.1 vs 13.1 operator touch and label vs receipt media in each printer.",
		meta_title="Avery Berkel XTi420 Dual Printer Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTi420 premium touchscreen weighing scale with dual label and receipt printers, customer display and advanced retail POS functionality.",
		benefits=[
			{"icon": "print", "title": "Two printers", "description": "Clamshell + cassette so two media stay loaded.", "sort_order": 1},
			{"icon": "checkout", "title": "Weigh + POS", "description": "Product label and customer receipt from one station.", "sort_order": 2},
			{"icon": "display", "title": "10.1 or 13.1-inch", "description": "Largest attended operator options in XTi, plus 10.1-inch customer.", "sort_order": 3},
			{"icon": "integration", "title": "Modern POS ready", "description": "Natural partner when the ticket should land in ERPNext.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTi420", "image": m["xti420"], "image_alt": "XTi420", "caption": "Official dual-printer tower — featured flagship.", "sort_order": 1},
			{"label": "On the counter", "image": m["xti_series_counter"], "image_alt": "Counter", "caption": "Raised customer face during service.", "sort_order": 2},
			{"label": "Saudi retail", "image": food, "image_alt": "Retail", "caption": "Supermarkets, butcheries and delis in KSA.", "sort_order": 3},
		],
		icons=[
			{"icon": "print", "title": "Printers", "description": "Dual thermal", "sort_order": 1},
			{"icon": "display", "title": "Operator", "description": "10.1 or 13.1-inch", "sort_order": 2},
			{"icon": "display", "title": "Customer", "description": "10.1-inch colour", "sort_order": 3},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "No XTi420 Item yet — quote 10.1 vs 13.1 operator"),
				("Not this page", "XTi400 single printer (4192/4221), XTs420 7-inch dual"),
			]),
			("Hardware", [
				("Displays", "10.1 or 13.1-inch operator; 10.1-inch customer"),
				("Printers", "Dual label/receipt — clamshell and cassette"),
				("Capacity", "15 kg AVR; ValuMax"),
			]),
		],
		apps=[
			{"title": "Weigh + POS counters", "description": "The demonstration workstation.", "image": m["xti420"], "image_alt": "XTi420", "industry_link": "retail", "sort_order": 1},
			{"title": "Supermarkets", "description": "Label the pack, print the ticket.", "image": food, "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 2},
			{"title": "Butcheries", "description": "Two media, one conversation.", "image": m["xti_series_counter"], "image_alt": "Butchery", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTi420 technology", "body": "Dual-printer reduced-footprint XTi. Featured flagship for Printechs — Avery Berkel XTi420 Saudi Arabia.", "image": m["xti420"], "image_alt": "XTi420", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTi420 with Modern POS", "body": "Avery Berkel XTi420 retail weighing scale in Saudi Arabia, including Jeddah, Riyadh and Dammam. Designed for supermarkets, butcheries and delis that need precision weighing, touchscreen operation and dual label/receipt printing. Land the ticket on Modern POS / ERPNext.", "image": r, "image_alt": "Retail", "link_label": "See Modern POS", "link_href": "/software/modern-pos", "sort_order": 2},
		],
		faqs=[
			{"question": "Why feature XTi420?", "answer": "It is the only XTi that clearly demonstrates weigh + label + receipt/POS without changing media.", "sort_order": 1},
			{"question": "Is there an Item?", "answer": "Not yet. Do not use XTi400 4192 — that Item has one printer.", "sort_order": 2},
			{"question": "10.1 or 13.1?", "answer": "Both are official operator options. Confirm on the quote with the 10.1-inch customer display.", "sort_order": 3},
		],
		support=support_items("10.1 vs 13.1 and two media.", "Cassette + clamshell stock.", "Two print heads.", "POS + label workflow."),
		pack=[{"item_description": "XTi420 dual-printer as quoted", "sort_order": 1}],
	)


def _xti600(m, r, bakery):
	return _xt_model(
		"avery-berkel-xti600", "Avery Berkel XTi600", "RET.SYS.AVR.4606",
		"Label Printers & Terminals", "TOUCHSCREEN LABEL PRINTING TERMINAL", "xti600", 1,
		tagline="Non-weighing 10.1-inch terminal — bakery, pre-pack and EPOS",
		short="Avery Berkel XTi600 is the non-weighing XTi: 10.1-inch touchscreen, cassette printer and optional customer display for pre-weighed, fixed-price or externally weighed products. Featured bakery / pre-pack / EPOS terminal.",
		long=(
			"<p>XTi600 has no platter. It provides the XT touchscreen, processing and "
			"printing environment for bakery, pre-pack and EPOS, and can connect to an "
			"external weighing platform. 10.1-inch touch, optional customer display, "
			"Ethernet/Wi-Fi, USB, high-speed printing, custom logos/fonts/images and "
			"linerless capability.</p>"
			"<p>This page is RET.SYS.AVR.4606 (XTi600 Non Weighing). Do not describe it as "
			"a weighing scale. XTs600 is the 7-inch non-weighing sibling (no Item yet).</p>"
			f"<p>{_ksa('XTi600')}</p>"
		),
		hero_alt="Avery Berkel XTi600 non-weighing 10.1-inch label terminal",
		chips="Non-weighing XTi\n10.1-inch touch\nItem 4606\nBakery · pre-pack · EPOS",
		story="XTi printing without a weigh platter",
		visual="XTi600",
		card_title="XTi600",
		card_summary="Featured 10.1-inch non-weighing label/EPOS terminal. Item 4606.",
		cta_h="Quote Avery Berkel XTi600",
		cta_d="Confirm standalone labels vs EPOS vs an external platform on Item 4606.",
		meta_title="Avery Berkel XTi600 Label Printer & EPOS Terminal Saudi Arabia",
		meta_desc="Avery Berkel XTi600 touchscreen retail label printer and EPOS terminal for bakery, pre-pack and food retail operations. Available from Printechs Saudi Arabia.",
		benefits=[
			{"icon": "print", "title": "Terminal, not a scale", "description": "Item 4606 is explicitly non-weighing.", "sort_order": 1},
			{"icon": "display", "title": "10.1-inch XTi", "description": "Larger canvas than XTs600 for bakery keys and images.", "sort_order": 2},
			{"icon": "integration", "title": "External platform", "description": "Add a bench or floor scale when weight is still required.", "sort_order": 3},
			{"icon": "store", "title": "EPOS capable", "description": "Receipts, logos and linerless options on XT Linux.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTi600", "image": m["xti600"], "image_alt": "XTi600", "caption": "No platter — featured bakery/pre-pack terminal.", "sort_order": 1},
			{"label": "Bakery", "image": bakery, "image_alt": "Bakery", "caption": "Fixed-price and pre-weighed packs.", "sort_order": 2},
			{"label": "Retail", "image": r, "image_alt": "Retail", "caption": "EPOS workstation on the XT network.", "sort_order": 3},
		],
		icons=[
			{"icon": "print", "title": "Role", "description": "Non-weighing terminal", "sort_order": 1},
			{"icon": "display", "title": "Screen", "description": "10.1-inch touch", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Cassette thermal", "sort_order": 3},
			{"icon": "connectivity", "title": "I/O", "description": "Ethernet · Wi-Fi · USB", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4606 — XTi600 Non Weighing"),
				("Not this page", "XTs600 7-inch terminal, any weighing XTi"),
			]),
			("Functions", [
				("Modes", "Standalone labels, bakery/pre-pack, EPOS"),
				("Customer display", "Optional depending on configuration"),
				("Weighing", "None on-board; optional external platform"),
			]),
		],
		apps=[
			{"title": "Bakeries", "description": "Featured printing/EPOS application.", "image": bakery, "image_alt": "Bakery", "industry_link": "retail", "sort_order": 1},
			{"title": "Pre-pack", "description": "Labels without a platter on this device.", "image": r, "image_alt": "Pre-pack", "industry_link": "retail", "sort_order": 2},
			{"title": "Food EPOS", "description": "Receipts on the XTi network.", "image": m["xti600"], "image_alt": "XTi600", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTi600 technology", "body": "Non-weighing XTi terminal with linerless-capable XT printing. Featured bakery/pre-pack page — not a weighing scale.", "image": m["xti600"], "image_alt": "XTi600", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTi600 in Saudi bakeries", "body": _ksa("XTi600"), "image": bakery, "image_alt": "Bakery", "sort_order": 2},
		],
		faqs=[
			{"question": "Does XTi600 weigh?", "answer": "No. Item 4606 is non-weighing. Add an external platform if needed.", "sort_order": 1},
			{"question": "XTi600 or XTs600?", "answer": "XTi600 is 10.1-inch (this Item). XTs600 is 7-inch and has no Item yet.", "sort_order": 2},
			{"question": "Customer display?", "answer": "Optional depending on configuration. Confirm on the quote.", "sort_order": 3},
		],
		support=support_items("4606 vs external platform.", "Bakery/linerless media.", "Cassette printer.", "EPOS keys."),
		pack=[{"item_description": "XTi600 non-weighing as Item 4606", "sort_order": 1}],
	)
