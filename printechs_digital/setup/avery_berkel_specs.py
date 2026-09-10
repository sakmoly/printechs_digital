# Copyright (c) 2026, Printechs and contributors
"""Model-accurate Avery Berkel full specifications.

Sources: Avery Berkel XT Technical Specifications, XT Series datasheet,
Xs range datasheet, and current Avery Berkel product pages.
Do not put SKU-honesty notes ("not this page", "also quote") in these tables.
"""

# Shared XT cassette printer (base printer on weighing/terminal models).
_XT_PRINT = [
	("Printer", "Thermal label/receipt cassette in the base"),
	("Load", "Single-action cassette; spare cassette swaps in seconds"),
	("Print speed", "Up to 150 mm/s"),
	("Roll diameter", "120 mm"),
	("Max paper width", "72 mm"),
	("Max print width", "70 mm; edge-to-edge"),
	("Max print length", "300 mm"),
	("Graphics", "16-level greyscale; images, logos and custom fonts"),
	("Diagnostics", "CodeChecker print-head monitoring"),
	("Linerless", "Supported on compatible media"),
	("Backwind", "Yes; label-taken sensor as standard"),
]

_XT_NET = [
	("Ethernet", "10/100/1 Gb Base-T auto-switching"),
	("Wi-Fi", "Optional USB module; 802.11 b/g/n/ac compatible"),
	("USB", "Up to 5 × USB 2.0 (peripherals, Wi-Fi, mass storage)"),
	("Inter-scale", "Ethernet client/server or peer; floating operators"),
	("Software", "MXBusiness / MXi-Pro central product and price management"),
]

_XT_PLATFORM = [
	("Operating system", "Linux (XTs / XTi)"),
	("Processor", "Intel Atom, 1.46 GHz"),
	("Memory", "2 GB standard (up to 8 GB)"),
	("Storage", "16 GB solid-state (Linux)"),
	("Power", "100–240 V AC, 50/60 Hz, internal PSU"),
	("Sound", "Full speaker system"),
	("Touch", "5-wire resistive colour touchscreen"),
]

_XS_PRINT = [
	("Printer", "Thermal label and receipt printer in the base"),
	("Print speed", "Up to 150 mm/s"),
	("Roll diameter", "100 mm"),
	("Max roll width", "60 mm"),
	("Max print width", "56 mm"),
	("Max print length", "300 mm"),
	("Diagnostics", "CodeChecker print-head monitoring"),
	("Graphics", "Images and logos on labels"),
]

_XS_NET = [
	("Ethernet", "10/100 Base-T"),
	("Wi-Fi", "Optional; 802.11 b/g/n/ac compatible"),
	("USB", "2 × USB 2.0"),
	("Cash drawer", "RJ11/12"),
	("Inter-scale", "Ethernet; up to 31 scales; up to 99 operators"),
	("Software", "MXBusiness product, price and promotion management"),
]

_XS_KEYS = [
	("Preset PLU keys", "58-key pressure-sensitive membrane"),
	("Function keys", "23 full-travel tactile keys"),
	("Operator display", "320 × 128 dot-matrix, white LED backlight"),
]


def _xs(form, capacity, customer, dimensions, extra_weigh=None):
	weigh = [
		("Form factor", form),
		("Capacity", capacity),
		("Increment (15 kg AVR)", "2 g to 6 kg; 5 g from 6–15 kg"),
		("Weighing pan", "Stainless steel platter"),
	]
	if extra_weigh:
		weigh.extend(extra_weigh)
	return [
		("Weighing", weigh),
		("Operator interface", _XS_KEYS + [("Customer display", customer)]),
		("Printing", _XS_PRINT),
		("Data & networking", [
			("Memory", "2 MB standard; 4 MB with optional memory card"),
			("PLU capacity", "Up to 10,000 products"),
			("Operating modes", "Counter label, pre-pack, receipt and cash/ECR"),
			*_XS_NET,
		]),
		("Physical", [
			("Dimensions (W × D × H)", dimensions),
			("Power", "100–240 V AC, 50/60 Hz, integrated supply"),
			("Mounting", "On or off a cash drawer"),
		]),
	]


def _xt(
	form,
	operator,
	customer,
	capacity,
	valuemax,
	dimensions,
	usb="Up to 5 × USB 2.0",
	weighing=True,
	printers=None,
	modes=None,
	extra=None,
):
	weigh = [
		("Form factor", form),
		("Capacity", capacity if weighing else "Non-weighing — no on-board platter"),
		("ValuMax", valuemax),
	]
	if weighing:
		weigh.insert(2, ("Increment (15 kg AVR)", "2 g to 6 kg; 5 g from 6–15 kg"))
		weigh.append(("Metrology", "Sealed load cell; service without breaking W&M seals"))
	print_rows = printers or list(_XT_PRINT)
	net = [row if row[0] != "USB" else ("USB", usb) for row in _XT_NET]
	groups = [
		("Weighing", weigh),
		("Displays & controls", [
			("Operator display", operator),
			("Customer display", customer),
			("Touch technology", "5-wire resistive colour touch"),
		]),
		("Printing", print_rows),
		("Platform", _XT_PLATFORM),
		("Connectivity", net),
		("Retail functions", [
			("Operating modes", modes or "Label, pre-pack, receipt/ECR; networked floating clerks"),
			("Advertising", "Idle-time text, image or video on colour displays"),
			("Nutrition labels", "On the product label or a second label"),
			("Software", "MXBusiness / MXi-Pro"),
		]),
		("Physical", [
			("Dimensions (W × D × H)", dimensions),
			("Power", "100–240 V AC, 50/60 Hz, internal PSU"),
		]),
	]
	if extra:
		groups.extend(extra)
	return groups


SPECS_BY_SLUG = {
	"avery-berkel": [
		("Xs tactile family", [
			("Models", "Xs100 monobloc, Xs200 raised customer, Xs400 tower, Xs500 hanging"),
			("Interface", "58 PLU keys + 23 tactile function keys"),
			("Displays", "320 × 128 LED-backlit operator and customer"),
			("Typical capacity", "15 kg AVR (2 g / 5 g). Family options 6 kg AVR and 25 kg × 5 g"),
			("Printer", "Thermal label/receipt; 150 mm/s; 56 mm print; 100 mm roll"),
		]),
		("XTs 7-inch family", [
			("Models", "XTs100/200/400/420/500 plus XTs600 terminal and XTs700 printer"),
			("Operator", "7-inch colour 800 × 480 plus tactile keys"),
			("OS / print", "Linux; cassette printer 150 mm/s; 70 mm edge-to-edge"),
			("ValuMax", "On weighing XTs except hanging XTs500"),
		]),
		("XTi premium family", [
			("Models", "XTi100/200/400/420, XTi300 self-service, XTi600 terminal"),
			("Operator", "10.1-inch typical; 13.1-inch option on XTi420; 18.5-inch on XTi300"),
			("OS / I/O", "Linux; 5 × USB; Ethernet and compatible Wi-Fi"),
			("Flagship", "XTi420 dual printers for weigh + label + receipt"),
		]),
		("Shared retail platform", [
			("Networking", "Ethernet inter-scale and host; optional Wi-Fi"),
			("Software", "MXBusiness / MXi-Pro"),
			("Modes", "Counter label, pre-pack, receipt/POS — by model"),
		]),
	],
	"avery-berkel-xs-series": [
		("Family", [
			("Range", "Xs100, Xs200, Xs400, Xs500"),
			("Interface", "Tactile PLU keyboard — not a colour touchscreen"),
			("Standard capacity", "15 kg AVR"),
			("Family options", "6 kg AVR and 25 kg × 5 g on selected models"),
		]),
		("Displays & keyboard", [
			("Operator / customer", "320 × 128 dot-matrix, white LED backlight"),
			("Preset keys", "58 membrane PLU keys"),
			("Function keys", "23 full-travel tactile keys"),
		]),
		("Printing", _XS_PRINT),
		("Data & networking", [
			("Memory", "2 MB standard; 4 MB optional"),
			("PLUs", "Up to 10,000"),
			*_XS_NET,
		]),
	],
	"avery-berkel-xts-series": [
		("Family", [
			("Weighing models", "XTs100, XTs200, XTs400, XTs420, XTs500"),
			("Non-weighing", "XTs600 terminal; XTs700 complementary USB printer"),
			("Operator", "7-inch colour touch 800 × 480 plus tactile keys"),
			("OS", "Linux"),
		]),
		("Weighing", [
			("Standard capacity", "15 kg AVR on weighing models"),
			("Family options", "6 kg AVR (XTs100); 30 kg × 5 g on selected towers"),
			("ValuMax", "Yes on bench XTs; not on hanging XTs500 or XTs600"),
		]),
		("Printing", _XT_PRINT),
		("Platform & I/O", _XT_PLATFORM + [
			("Ethernet", "10/100/1 Gb Base-T"),
			("USB", "Up to 5 × USB 2.0 (3 on XTs500)"),
		]),
	],
	"avery-berkel-xti-series": [
		("Family", [
			("Attended", "XTi100, XTi200, XTi400, XTi420"),
			("Self-service", "XTi300 18.5-inch"),
			("Non-weighing", "XTi600 label / EPOS terminal"),
			("OS", "Linux"),
		]),
		("Displays", [
			("Typical operator", "10.1-inch colour 1024 × 600"),
			("XTi420 option", "13.1-inch operator; 10.1-inch customer"),
			("XTi300", "18.5-inch self-service touchscreen"),
		]),
		("Weighing", [
			("Standard capacity", "15 kg AVR on weighing models"),
			("Family options", "6 kg AVR and 30 kg × 5 g on selected models"),
			("ValuMax", "Yes on weighing XTi; not applicable on XTi600"),
		]),
		("Printing", _XT_PRINT),
		("Platform & I/O", _XT_PLATFORM + [
			("USB", "Five USB 2.0 interfaces"),
			("Ethernet", "10/100/1 Gb Base-T"),
		]),
	],
	"avery-berkel-xs100": _xs(
		"Compact monobloc — platform, keys, displays and printer in one unit",
		"15 kg AVR on this page (2 g / 5 g). Family options: 6 kg AVR, 25 kg × 5 g",
		"Integrated in the monobloc, 320 × 128 LED-backlit",
		"Approx. 384 × 469 × 182 mm",
		[("Pan size", "Approx. 300 × 374 mm")],
	),
	"avery-berkel-xs200": _xs(
		"Xs platform with raised customer-facing display; keys stay at counter level",
		"15 kg AVR on this page. Family option: 25 kg × 5 g",
		"Raised column display, 320 × 128 LED-backlit",
		"Approx. 384 × 540 × 509 mm",
		[("Pan size", "Approx. 300 × 374 mm")],
	),
	"avery-berkel-xs400": _xs(
		"Two-piece tower — raised keyboard and displays, platter left clear",
		"15 kg AVR on this page. Family options: 6 kg AVR, 25 kg × 5 g",
		"Elevated with the operator display, 320 × 128 LED-backlit",
		"Approx. 384 × 406 × 527 mm",
		[("Pan size", "Approx. 300 × 374 mm")],
	),
	"avery-berkel-xs500": [
		("Weighing", [
			("Form factor", "Hanging scale for wet / seafood counters"),
			("Capacity", "15 kg × 5 g on this page. Family option: 15 kg AVR"),
			("Pan", "Suspended stainless scoop — not a bench platter"),
			("Environment", "Specified for wet-area retail"),
		]),
		("Operator interface", [
			("Preset PLU keys", "Tactile product keyboard in the hanging head"),
			("Function keys", "23 full-travel tactile keys"),
			("Vendor display", "320 × 128 dot-matrix, white LED backlight"),
			("Customer display", "Matching customer display in the head"),
		]),
		("Printing", _XS_PRINT),
		("Data & networking", [
			("Memory", "2 MB standard; 4 MB with optional card"),
			("PLU capacity", "Up to 10,000 products"),
			("Operating modes", "Counter label, receipt and networked prices"),
			*_XS_NET,
		]),
		("Physical", [
			("Design", "Hanging head with suspended pan"),
			("Power", "100–240 V AC, 50/60 Hz, integrated supply"),
		]),
	],
	"avery-berkel-xts100": _xt(
		"Compact monobloc for limited vertical space",
		"7-inch colour WVGA 800 × 480 plus tactile numeric and 20 programmable keys",
		"Integrated 7-inch colour 800 × 480",
		"15 kg AVR on this page. Family option: 6 kg AVR",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 466 × 156 mm",
	),
	"avery-berkel-xts200": _xt(
		"Compact operator station with raised customer display",
		"7-inch colour WVGA 800 × 480 plus tactile keys at the deck",
		"Raised 7-inch colour 800 × 480; advertising capable",
		"15 kg AVR",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 493 × 528 mm",
	),
	"avery-berkel-xts400": _xt(
		"Raised two-piece tower; reduced footprint; single cassette printer",
		"Raised 7-inch colour 800 × 480 plus tactile keys",
		"7-inch on this page; 10.1-inch customer is a family option",
		"15 kg AVR. Selected family configurations: 30 kg × 5 g",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 405 × 528 mm",
	),
	"avery-berkel-xts420": _xt(
		"Raised two-piece tower with dual printers",
		"Raised 7-inch colour 800 × 480 plus tactile keys",
		"Raised colour customer display (7-inch; 10.1-inch family option)",
		"15 kg AVR",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 478 × 502 mm",
		printers=[
			("Base printer", "Cassette label/receipt; 150 mm/s; 70 mm; 120 mm roll"),
			("Upper printer", "Clamshell receipt/label; 100 mm/s; 56 mm; 100 mm roll"),
			("Upper linerless", "Special roller for linerless adhesive paper as standard"),
			("Typical setup", "Product labels from the base; receipts from the upper printer"),
			("Diagnostics", "CodeChecker on the XT print platform"),
		],
		modes="Weigh + label + receipt/POS without changing media",
	),
	"avery-berkel-xts500": _xt(
		"Hanging scale for fish, seafood and wet counters",
		"7-inch colour 800 × 480 in the elevated head plus tactile keys",
		"7-inch colour customer display",
		"15 kg AVR",
		"Not available on hanging XTs500 (Avery Berkel technical specification)",
		"Approx. 408 × 312 × 775 mm including scoop fitting",
		usb="3 × USB 2.0 (front compartment and top cover)",
		modes="Staffed seafood labelling and receipt; networked PLUs",
	),
	"avery-berkel-xts600": [
		("Role", [
			("Type", "Non-weighing 7-inch label printer and EPOS terminal"),
			("Weighing", "None on-board. Optional external platform or wrapper"),
			("ValuMax", "Not applicable — no on-board weigh platform"),
		]),
		("Displays & controls", [
			("Operator", "7-inch colour 800 × 480 plus tactile keys"),
			("Customer display", "Not a raised weigh-station display on this terminal"),
		]),
		("Printing", _XT_PRINT),
		("Platform", _XT_PLATFORM),
		("Connectivity", _XT_NET),
		("Functions", [
			("Modes", "Standalone labels, bakery/pre-pack and EPOS"),
			("Software", "MXBusiness / MXi-Pro"),
		]),
		("Physical", [
			("Dimensions (W × D × H)", "Approx. 268 × 325 × 364 mm"),
			("Power", "100–240 V AC, 50/60 Hz, internal PSU"),
		]),
	],
	"avery-berkel-xts700": [
		("Role", [
			("Type", "Complementary USB label/receipt printer — not a scale"),
			("Weighing", "None. Attaches to a host XTs or XTi"),
			("Use", "Second label size (price + nutrition) without changing host stock"),
		]),
		("Printing", [
			("Mechanism", "Same XT cassette thermal printer as the family"),
			("Print speed", "Up to 150 mm/s"),
			("Roll diameter", "120 mm"),
			("Max print width", "70 mm; edge-to-edge"),
			("Max print length", "300 mm"),
			("Diagnostics", "CodeChecker print-head monitoring"),
			("Connection", "USB to compatible XT equipment"),
		]),
		("Physical", [
			("Dimensions (W × D × H)", "Approx. 268 × 325 × 176 mm"),
			("Power", "From the host XT USB / supplied PSU as quoted"),
		]),
	],
	"avery-berkel-xti100": _xt(
		"Compact premium monobloc",
		"10.1-inch colour 1024 × 600 touchscreen",
		"Integrated 7-inch colour 800 × 480",
		"15 kg AVR on this page. Family options: 6 kg AVR, 30 kg × 5 g",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 466 × 156 mm",
	),
	"avery-berkel-xti200": _xt(
		"10.1-inch operator with raised customer display",
		"10.1-inch colour 1024 × 600 touchscreen",
		"Raised 7-inch colour 800 × 480; advertising capable",
		"15 kg AVR. Family option: 30 kg × 5 g",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 493 × 528 mm",
	),
	"avery-berkel-xti300": _xt(
		"Self-service produce / fresh-food scale — not a staffed deli keyboard",
		"18.5-inch colour 1024 × 600 shopper touchscreen",
		"Shopper-facing 18.5-inch canvas (no separate staff pole)",
		"15 kg AVR",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 410 × 610 mm",
		modes="Self-service: select product photo, weigh, print barcode/QR label",
	),
	"avery-berkel-xti400": _xt(
		"Raised two-piece tower; single cassette printer",
		"Raised 10.1-inch colour 1024 × 600 touchscreen",
		"7-inch on this page; 10.1-inch customer is a family option",
		"15 kg AVR",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 405 × 528 mm",
	),
	"avery-berkel-xti420": _xt(
		"Raised dual-printer flagship workstation",
		"10.1-inch or 13.1-inch colour 1024 × 600, raised",
		"10.1-inch colour customer display",
		"15 kg AVR",
		"Yes — automatic out-of-level correction",
		"Approx. 408 × 478 × 502 mm",
		printers=[
			("Base printer", "Cassette label/receipt; 150 mm/s; 70 mm; 120 mm roll"),
			("Upper printer", "Clamshell receipt/label; 100 mm/s; 56 mm; 100 mm roll"),
			("Upper linerless", "Linerless adhesive roller as standard"),
			("Typical setup", "Pack label from the base; receipt/POS from the upper printer"),
			("Diagnostics", "CodeChecker on the XT print platform"),
		],
		modes="Weigh + label + receipt/POS from one station",
	),
	"avery-berkel-xti600": [
		("Role", [
			("Type", "Non-weighing 10.1-inch label printer and EPOS terminal"),
			("Weighing", "None on-board. Optional external platform or wrapper"),
			("ValuMax", "Not applicable — no on-board weigh platform"),
		]),
		("Displays & controls", [
			("Operator", "10.1-inch colour 1024 × 600 touchscreen"),
			("Customer display", "Optional 10.1-inch depending on configuration"),
		]),
		("Printing", _XT_PRINT),
		("Platform", _XT_PLATFORM),
		("Connectivity", _XT_NET),
		("Functions", [
			("Modes", "Standalone labels, bakery/pre-pack and EPOS"),
			("Software", "MXBusiness / MXi-Pro"),
		]),
		("Physical", [
			("Dimensions (W × D × H)", "Approx. 268 × 325 × 364 mm"),
			("Power", "100–240 V AC, 50/60 Hz, internal PSU"),
		]),
	],
}


def specs_for(slug: str):
	groups = SPECS_BY_SLUG.get(slug)
	if not groups:
		raise ValueError(f"No Avery Berkel full specifications mapped for {slug}")
	return groups
