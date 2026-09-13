# Copyright (c) 2026, Printechs and contributors
"""Fill remaining industry pages with unique images. No videos, no product names.

Coding industries use official Hitachi print samples that are not on product,
dairy or packaging pages. Bakery, retail, fashion and warehouse use unique
application photos. Egg / poultry uses the official food-grade eggshell sample
plus a related farm-egg photo.
"""

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe

from printechs_digital.setup.copy_website_asset import copy_public_image

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
PUBLIC_INDUSTRIES = Path(
	"/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries"
)
REPO_INDUSTRIES = Path(
	"/home/erpnext/frappe-bench/apps/printechs_digital/frontend/printechs-web/public/images/industries"
)
H = "https://hitachi-industrial.eu/wp-content/uploads"
U = "https://images.unsplash.com/photo"
UA = "Mozilla/5.0 (compatible; Printechs/1.0)"


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
	for folder in (PUBLIC_INDUSTRIES, REPO_INDUSTRIES):
		folder.mkdir(parents=True, exist_ok=True)
		im.save(folder / filename, "JPEG", quality=90, optimize=True)
	return f"/files/{filename}"


def download_wide(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(url, headers={"User-Agent": UA})
		with urlopen(request, timeout=45) as response:
			data = response.read()
		if len(data) < 2000:
			frappe.throw(f"Download too small ({len(data)} bytes): {url}")
		im = Image.open(BytesIO(data)).convert("RGB")
		return _save_wide(im, filename)
	return f"/files/{filename}"


def from_local(filename: str, src: Path) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		im = Image.open(src).convert("RGB")
		return _save_wide(im, filename)
	return f"/files/{filename}"


def media(mapping: dict[str, str]) -> dict[str, str]:
	return {name: download_wide(name, url) for name, url in mapping.items()}


def section(
	heading: str,
	body: str,
	image: str,
	image_alt: str,
	sort_order: int,
	image_side: str | None = None,
) -> dict:
	return {
		"section_type": "Industry Solution",
		"heading": heading,
		"body": body,
		"image": image,
		"image_alt": image_alt,
		"image_side": image_side or ("Left" if sort_order % 2 else "Right"),
		"sort_order": sort_order,
		"video_url": "",
		"link_label": "",
		"link_href": "",
	}


def update_industry(
	slug: str,
	industry_name: str,
	summary: str,
	overview: str,
	image_alt: str,
	meta_title: str,
	meta_description: str,
	solution_slugs: str,
	sections: list[dict],
) -> dict:
	name = frappe.db.get_value("Website Industry", {"slug": slug}, "name")
	if not name:
		frappe.throw(f"Website Industry {slug} is missing")

	doc = frappe.get_doc("Website Industry", name)
	doc.published = 1
	doc.show_on_home = 1
	doc.industry_name = industry_name
	doc.summary = summary
	doc.overview = overview
	doc.image = copy_public_image(f"industries/industry-{slug}.jpg")
	doc.image_alt = image_alt
	doc.related_product_slugs = ""
	doc.related_software_slugs = ""
	doc.related_solution_slugs = solution_slugs
	doc.meta_title = meta_title
	doc.meta_description = meta_description
	doc.set("content_sections", sections)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return {"status": "updated", "slug": slug, "sections": len(doc.content_sections)}


def fill_food_beverage() -> dict:
	m = media(
		{
			"food-bev-wet-pet.jpg": f"{H}/2025/05/Beverage_Print-Sample-1.webp",
			"food-bev-can-base.jpg": f"{H}/2025/05/Beverage_Print-Sample-2.webp",
			"food-bev-pet-line.jpg": f"{H}/2025/05/Beverage_-Print-Sample-3.webp",
			"food-bev-glass-neck.jpg": f"{H}/2025/05/Beverage_Print-Sample-5.webp",
			"food-bev-screw-cap.jpg": f"{H}/2025/05/Beverage_Print-Sample-6.webp",
		}
	)
	return update_industry(
		slug="food-beverage",
		industry_name="Food & Beverage",
		summary=(
			"Lot, expiry and time codes on wet PET, can bases, high-speed bottle lines, "
			"glass necks and screw caps — for F&B halls in Saudi Arabia."
		),
		overview=(
			"Beverage and prepared-food lines need a code that keys to wet PET, cold aluminium "
			"and glass — then stays readable after condensation, crate packing and the chill chain.\n\n"
			"Printechs surveys the filler, the pack and the hall, then specifies coding for "
			"producers in Riyadh, Jeddah and Dammam. The same duty applies whichever industrial "
			"inkjet or laser sits on the line.\n\n"
			"This page is the food and beverage application, not a product list. We match ink, "
			"throw and photocell to the pack when you enquire."
		),
		image_alt="Food and beverage production line with coded meal containers and bottles",
		meta_title="Food & Beverage Industry Solutions | Printechs",
		meta_description=(
			"Food and beverage coding samples for wet PET, cans, high-speed bottles, glass "
			"necks and screw caps. Printechs specifies readable lot and expiry marks in Saudi Arabia."
		),
		solution_slugs="coding-marking\ntraceability",
		sections=[
			section(
				"Wet PET and condensation",
				"Lot and time on a wet bottle after the filler and the cooler.\n\n"
				"Condensation is the usual failure. The ink has to key to PET through the film "
				"of water and stay sharp in the crate and the chill store.",
				m["food-bev-wet-pet.jpg"],
				"Lot and time code on a wet PET bottle",
				1,
			),
			section(
				"Can bases and energy drinks",
				"Date and lot on the concave base of an aluminium can, after fill and seamer.\n\n"
				"The print window is tight and the metal is cold. A compact, high-contrast code "
				"is what the warehouse and the retailer both need to read.",
				m["food-bev-can-base.jpg"],
				"Date and lot code on an aluminium can base",
				2,
			),
			section(
				"High-speed bottle lines",
				"Expiry and lot on PET at filler speed — the code has to land in the same "
				"window on every bottle.\n\n"
				"Encoder and photocell set the throw. A smear here becomes a rejected crate "
				"and a hold on the lot.",
				m["food-bev-pet-line.jpg"],
				"Lot and expiry codes on PET bottles moving on a filler",
				3,
			),
			section(
				"Glass necks and crown finishes",
				"Time and lot on the neck foil or label, next to the crown.\n\n"
				"Glass and foil are curved and often wet. The mark still has to be obvious "
				"on the retail shelf and in a recall scan.",
				m["food-bev-glass-neck.jpg"],
				"Time and lot code on a glass bottle neck label",
				4,
			),
			section(
				"Screw caps and spirit bottles",
				"A compact code on the cap skirt or the shoulder, after capper.\n\n"
				"The print area is small and the cap is shiny. We set the head to the finish "
				"so the code does not walk off the thread.",
				m["food-bev-screw-cap.jpg"],
				"Lot code on a spirit-bottle screw cap",
				5,
			),
		],
	)


def fill_bakery() -> dict:
	m = media(
		{
			"bakery-croissant.jpg": f"{U}-1555507036-ab1f4038808a?auto=format&fit=crop&w=2000&q=80",
			"bakery-sliced-loaf.jpg": f"{U}-1549931319-a545dcf3bc73?auto=format&fit=crop&w=2000&q=80",
			"bakery-counter.jpg": f"{U}-1568254183919-78a4f43a2877?auto=format&fit=crop&w=2000&q=80",
			"bakery-cookies.jpg": f"{U}-1558961363-fa8fdf82db35?auto=format&fit=crop&w=2000&q=80",
		}
	)
	return update_industry(
		slug="bakery",
		industry_name="Bakery",
		summary=(
			"Coding, weighing and store identification for pastry, sliced bread, "
			"counter service and confectionery — for bakery brands in Saudi Arabia."
		),
		overview=(
			"Bakery lines move from oven to bag to counter in a short window. The pack needs "
			"a lot and a best-before that survives warm film, flour dust and a retail shelf.\n\n"
			"Printechs specifies coding, weighing and store identification for industrial and "
			"retail bakeries in Riyadh, Jeddah and Dammam. This page is the bakery application, "
			"not a product list.\n\n"
			"We match the mark and the label to the loaf, the pastry and the counter when you enquire."
		),
		image_alt="Bakery production line with coded bread packaging on a conveyor",
		meta_title="Bakery Industry Solutions | Printechs",
		meta_description=(
			"Bakery coding, weighing and store identification for pastry, sliced bread, "
			"counters and confectionery in Saudi Arabia."
		),
		solution_slugs="coding-marking\nretail-automation",
		sections=[
			section(
				"Pastry and laminated goods",
				"Lot and time on the bag or the tray after bake and cool.\n\n"
				"Warm pastry and thin film change the print window. The code has to stay "
				"readable after the pack is stacked and sent to the store.",
				m["bakery-croissant.jpg"],
				"Fresh croissants ready for bakery packing and date coding",
				1,
			),
			section(
				"Sliced bread and loaf bags",
				"Best-before and lot on the bag clip, the film or the label after the slicer.\n\n"
				"Soft film and a moving loaf need a head that tracks the bag. A missed code "
				"is a wasted crate at the DC.",
				m["bakery-sliced-loaf.jpg"],
				"Sliced loaf ready for bag coding and shelf-life marking",
				2,
			),
			section(
				"Counter and shop bakeries",
				"Weighing, labelling and a readable price or lot at the counter.\n\n"
				"The same hall that bakes also sells. Staff need a fast, clean mark that "
				"the till and the customer can both read.",
				m["bakery-counter.jpg"],
				"Bakery shop display of breads and pastries",
				3,
			),
			section(
				"Cookies and confectionery packs",
				"Date and lot on a small tray, tub or film pack.\n\n"
				"The print area is tight and the film is often glossy. A compact, high-contrast "
				"code is what the retailer needs on the shelf.",
				m["bakery-cookies.jpg"],
				"Cookies ready for confectionery packing and date coding",
				4,
			),
		],
	)


def fill_egg_poultry() -> dict:
	m = media(
		{
			"egg-shell-code.jpg": f"{H}/2025/05/Food-Grade-Ink_Example.webp",
			"egg-farm-eggs.jpg": (
				"https://images.pexels.com/photos/162712/egg-white-food-protein-162712.jpeg"
				"?auto=compress&cs=tinysrgb&w=2000"
			),
		}
	)
	return update_industry(
		slug="egg-poultry",
		industry_name="Egg / Poultry",
		summary=(
			"Food-grade eggshell codes, carton identification and poultry-pack traceability "
			"for producers in Saudi Arabia."
		),
		overview=(
			"Egg and poultry halls need a mark that keys to a porous shell, a pulp carton and "
			"a chilled tray — then stays readable after wash, grade and the cold chain.\n\n"
			"Printechs specifies food-grade coding and pack identification for farms and "
			"processors in Riyadh, Jeddah and Dammam. This page is the application, not a "
			"product list.\n\n"
			"We match ink and throw to the shell and the carton when you enquire."
		),
		image_alt="Egg packaging line with traceability coding on cartons and shells",
		meta_title="Egg & Poultry Industry Solutions | Printechs",
		meta_description=(
			"Eggshell coding, carton identification and poultry-pack traceability for "
			"producers in Saudi Arabia."
		),
		solution_slugs="coding-marking\ntraceability",
		sections=[
			section(
				"Food-grade eggshell codes",
				"A farm or packer code on the shell, after wash and grade.\n\n"
				"The shell is porous and curved. Food-grade ink has to key without smearing "
				"into the crate or the retail carton.",
				m["egg-shell-code.jpg"],
				"Food-grade identification code printed on an eggshell",
				1,
			),
			section(
				"Farm eggs and packer lots",
				"Lot and grade on the carton, the tray and the farm pack.\n\n"
				"A missed carton code breaks the chain from house to retailer. We set the "
				"mark so the crate, the store and a recall scan all read the same lot.",
				m["egg-farm-eggs.jpg"],
				"Farm eggs ready for carton coding and lot identification",
				2,
			),
		],
	)


def fill_pharmaceutical() -> dict:
	m = media(
		{
			"pharma-folding-carton.jpg": f"{H}/2025/05/Cosmetics_Print-Sample-1.webp",
			"pharma-stick-qr.jpg": f"{H}/2025/05/Cosmetics_Print-Sample-2.webp",
			"pharma-pump-bottle.jpg": f"{H}/2025/05/Cosmetics_Print-Sample-3.webp",
			"pharma-vial-2d.jpg": (
				f"{H}/2025/06/applicationphoto_medical_laser_2d_code_on_medical_vials.webp"
			),
			"pharma-bottle-base.jpg": f"{H}/2025/05/Cosmetics_Print-Sample-6.webp",
		}
	)
	return update_industry(
		slug="pharmaceutical",
		industry_name="Pharmaceutical",
		summary=(
			"Lot, expiry and 2D codes on folding cartons, small packs, pump bottles, "
			"vials and bottle bases — for regulated packs in Saudi Arabia."
		),
		overview=(
			"Regulated packs need a lot, an expiry and often a 2D code that grades after "
			"carton, bottle and vial — on glossy board, plastic and glass.\n\n"
			"Printechs specifies coding and identification for pharmaceutical and cosmetics "
			"packaging halls in Riyadh, Jeddah and Dammam. This page is the application, "
			"not a product list.\n\n"
			"We match the mark to the carton, the bottle and the vial when you enquire."
		),
		image_alt="Pharmaceutical packaging line with batch-coded product boxes",
		meta_title="Pharmaceutical Industry Solutions | Printechs",
		meta_description=(
			"Pharmaceutical and regulated-pack coding samples for cartons, small packs, "
			"bottles and vials in Saudi Arabia."
		),
		solution_slugs="coding-marking\ntraceability",
		sections=[
			section(
				"Folding cartons and late-stage codes",
				"Lot, expiry and batch on the carton flap or end panel after cartoner.\n\n"
				"Printed board is low-contrast. The code still has to be obvious for the "
				"warehouse scan and a recall.",
				m["pharma-folding-carton.jpg"],
				"Lot and expiry code on a regulated folding carton",
				1,
			),
			section(
				"Small packs and 2D codes",
				"A compact lot and a QR or DataMatrix on the base of a stick or tube.\n\n"
				"The print area is tight. Human-readable and 2D have to land together so "
				"the pack grades and the store can scan it.",
				m["pharma-stick-qr.jpg"],
				"Lot and 2D code on the base of a small pack",
				2,
			),
			section(
				"Pump bottles and curved plastics",
				"Date and lot on the bottle shoulder, after fill and pump fitment.\n\n"
				"White PE and a curve change the throw. The mark has to stay readable "
				"after wipe-down and the retail shelf.",
				m["pharma-pump-bottle.jpg"],
				"Date and lot code on a pump bottle",
				3,
			),
			section(
				"Vials and cap 2D marks",
				"A small 2D code on the vial cap or ferrule for unit-level identity.\n\n"
				"The mark is tiny and the metal is reflective. Placement and contrast "
				"are what a vision check and a hospital scan both need.",
				m["pharma-vial-2d.jpg"],
				"2D identification codes on pharmaceutical vial caps",
				4,
			),
			section(
				"Bottle bases and lot strings",
				"A compact lot on the glass or PET base, next to the barcode panel.\n\n"
				"The print window sits under the pack. The code still has to survive "
				"packing into the carton and the DC scan.",
				m["pharma-bottle-base.jpg"],
				"Lot code on the base of a pharmaceutical bottle",
				5,
			),
		],
	)


def fill_pipe() -> dict:
	m = media(
		{
			"pipe-marked-tubes.jpg": f"{H}/2025/05/Wire-Cable_Print-Sample-1.webp",
			"pipe-cable-jackets.jpg": f"{H}/2025/05/Wire-Cable_Print-Sample-5.webp",
			"pipe-fine-wire.jpg": f"{H}/2025/05/Wire-Cable_Print-Sample-2.webp",
		}
	)
	return update_industry(
		slug="pipe",
		industry_name="Pipe",
		summary=(
			"Batch, size and metre marks on tubes, pipes, cable jackets and fine wire "
			"— for extrusion halls in Saudi Arabia."
		),
		overview=(
			"Pipe, tube and cable lines need a continuous mark that keys to HDPE, copper, "
			"PVC and jacket compound — at extrusion speed, often in dust and heat.\n\n"
			"Printechs specifies large-character and industrial coding for pipe and cable "
			"plants in Riyadh, Jeddah and Dammam. This page is the application, not a "
			"product list.\n\n"
			"We match ink and throw to the diameter and the line speed when you enquire."
		),
		image_alt="Industrial pipe with batch number and size marking",
		meta_title="Pipe Industry Solutions | Printechs",
		meta_description=(
			"Pipe, tube and cable coding samples for batch, size and metre marks in Saudi Arabia."
		),
		solution_slugs="coding-marking\ntraceability",
		sections=[
			section(
				"Tubes and pipelines",
				"Batch, size and a human-readable string along the tube after extrusion.\n\n"
				"Round stock turns under the head. The mark has to stay in register for "
				"the full length the yard will cut.",
				m["pipe-marked-tubes.jpg"],
				"Batch and size codes on plastic and metal tubes",
				1,
			),
			section(
				"Cable jackets",
				"Legend and metre mark on the jacket after the extruder.\n\n"
				"Dark and light jackets need different contrast. The code has to survive "
				"the reel, the yard and a field install.",
				m["pipe-cable-jackets.jpg"],
				"Identification marking on cable jackets",
				2,
			),
			section(
				"Fine wire and small diameters",
				"A compact legend on a thin jacket, often white pigment on black.\n\n"
				"The print area is a few millimetres. Throw and ink density are what keep "
				"the mark readable after rewind.",
				m["pipe-fine-wire.jpg"],
				"White identification mark on fine wire jackets",
				3,
			),
		],
	)


def fill_plastic() -> dict:
	m = media(
		{
			"plastic-extrusion-profile.jpg": f"{H}/2025/05/Wire-Cable_Print-Sample-3.webp",
			"plastic-color-strips.jpg": f"{H}/2025/05/Wire-Cable_Print-Sample-4.webp",
			"plastic-uv-bottle.jpg": f"{H}/2025/05/UV_Ink_Example.webp",
			"plastic-headlamp.jpg": f"{H}/2025/05/Automotive_Print-Sample-5.webp",
		}
	)
	return update_industry(
		slug="plastic",
		industry_name="Plastic",
		summary=(
			"Durable lot and part codes on extruded profiles, colour strips, bottles "
			"and moulded housings — for plastics halls in Saudi Arabia."
		),
		overview=(
			"Plastics halls mark PE, PP, ABS and filled compounds — profiles, bottles and "
			"moulded parts — often while the part is still warm from the tool or the die.\n\n"
			"Printechs specifies coding for extrusion and moulding plants in Riyadh, Jeddah "
			"and Dammam. This page is the application, not a product list.\n\n"
			"We match ink and throw to the resin and the colour when you enquire."
		),
		image_alt="Plastic bottles on a production line with lot and expiry coding",
		meta_title="Plastic Industry Solutions | Printechs",
		meta_description=(
			"Plastic coding samples for extruded profiles, colour strips, bottles and "
			"moulded housings in Saudi Arabia."
		),
		solution_slugs="coding-marking\ntraceability",
		sections=[
			section(
				"Extruded profiles",
				"Logo and lot along a hollow or solid profile after the calibrator.\n\n"
				"The surface can be glossy or filled. The mark has to stay readable after "
				"cut-to-length and a yard stack.",
				m["plastic-extrusion-profile.jpg"],
				"Lot and logo code on an extruded plastic profile",
				1,
			),
			section(
				"Colour strips and flat stock",
				"A pigmented code on blue, yellow or dark strip after the die.\n\n"
				"Contrast is the duty. White or yellow on dark, dark on light — the "
				"warehouse still has to read the lot.",
				m["plastic-color-strips.jpg"],
				"Pigmented codes on coloured plastic strips",
				2,
			),
			section(
				"Bottles and UV-readable marks",
				"Lot and time on a dark bottle — sometimes a UV or high-contrast mark "
				"that only shows under inspection.\n\n"
				"Black PE hides a standard black code. We set the ink so the pack still "
				"identifies in the hall and the DC.",
				m["plastic-uv-bottle.jpg"],
				"High-contrast lot code on a dark plastic bottle",
				3,
			),
			section(
				"Moulded housings and parts",
				"Part number and date on a moulded housing after the tool.\n\n"
				"Ribs and a curve change the throw. The mark has to survive assembly "
				"and a field service scan.",
				m["plastic-headlamp.jpg"],
				"Part number and date code on a moulded plastic housing",
				4,
			),
		],
	)


def fill_steel() -> dict:
	m = media(
		{
			"steel-metal-strut.jpg": f"{H}/2025/05/Automotive_Print-Sample-4.webp",
			"steel-dark-strip.jpg": f"{H}/2025/05/Automotive_-Print-Sample-3.webp",
			"steel-blade-mark.jpg": f"{H}/2025/05/Medical_Print-Sample-1.webp",
			"steel-stamped-part.jpg": f"{H}/2025/05/Oil-Gas_Print-Sample-3.webp",
		}
	)
	return update_industry(
		slug="steel",
		industry_name="Steel",
		summary=(
			"High-contrast and durable marks on tubes, coated strip, blades and "
			"stamped parts — for steel and metals halls in Saudi Arabia."
		),
		overview=(
			"Steel and metals halls need a mark that survives oil, scale, heat and handling "
			"— on tube, strip, coil and a finished part.\n\n"
			"Printechs specifies rugged identification for metals plants in Riyadh, Jeddah "
			"and Dammam. This page is the application, not a product list.\n\n"
			"We match the process to the surface — ink, pigment or a permanent mark — when you enquire."
		),
		image_alt="Steel coil with batch number, production date and QR code marking",
		meta_title="Steel Industry Solutions | Printechs",
		meta_description=(
			"Steel and metals marking samples for tubes, coated strip, blades and stamped "
			"parts in Saudi Arabia."
		),
		solution_slugs="coding-marking\ntraceability",
		sections=[
			section(
				"Tubes and painted metal",
				"Part and lot on a painted or coated tube after finish.\n\n"
				"Dark paint needs a light pigment. The mark has to stay readable after "
				"assembly and a service scan.",
				m["steel-metal-strut.jpg"],
				"Lot and part code on a painted metal tube",
				1,
			),
			section(
				"Coated strip and dark stock",
				"A white or pigmented string on dark coated strip.\n\n"
				"Contrast and adhesion are the duty. The warehouse still has to read "
				"the lot after slitting and a coil wrap.",
				m["steel-dark-strip.jpg"],
				"High-contrast identification on dark coated strip",
				2,
			),
			section(
				"Blades and bright metal",
				"A compact part number on bright or ground metal.\n\n"
				"The surface is reflective. Placement and contrast are what keep the "
				"mark readable after grind and pack.",
				m["steel-blade-mark.jpg"],
				"Part number marked on a steel blade",
				3,
			),
			section(
				"Stamped and handled parts",
				"A durable lot on a painted or weathered casting or forging.\n\n"
				"Oil, paint and handling wear a weak mark. The identity still has to "
				"be there in the yard and in the field.",
				m["steel-stamped-part.jpg"],
				"Durable lot mark on a stamped metal part",
				4,
			),
		],
	)


def fill_retail() -> dict:
	m = media(
		{
			"retail-grocery-aisle.jpg": f"{U}-1578916171728-46686eac8d58?auto=format&fit=crop&w=2000&q=80",
			"retail-supermarket.jpg": f"{U}-1604719312566-8912e9227c6a?auto=format&fit=crop&w=2000&q=80",
			"retail-checkout.jpg": f"{U}-1556742111-a301076d9d18?auto=format&fit=crop&w=2000&q=80",
		}
	)
	m["retail-fresh-produce.jpg"] = from_local(
		"retail-fresh-produce.jpg", SITE_FILES / "Vehitable Store.jpg"
	)
	m["retail-shop-floor.jpg"] = from_local(
		"retail-shop-floor.jpg", SITE_FILES / "SuperMarket1.png"
	)
	return update_industry(
		slug="retail",
		industry_name="Retail",
		summary=(
			"Aisle identification, supermarket operations, shop-floor systems, fresh "
			"counters and checkout — for retailers in Saudi Arabia."
		),
		overview=(
			"Retail halls need a price, a scan and a stock figure that match the shelf — "
			"from grocery aisle to fresh counter to checkout.\n\n"
			"Printechs specifies store hardware, identification and retail systems for "
			"chains and independents in Riyadh, Jeddah and Dammam. This page is the "
			"retail application, not a product list.\n\n"
			"We match the aisle, the counter and the till when you enquire."
		),
		image_alt="Retail checkout scanning product with lot and expiry traceability data",
		meta_title="Retail Industry Solutions | Printechs",
		meta_description=(
			"Retail aisle, supermarket, shop-floor, fresh-counter and checkout systems "
			"for stores in Saudi Arabia."
		),
		solution_slugs="retail-automation\npos-retail-software",
		sections=[
			section(
				"Grocery aisles",
				"A price and a barcode that match the planogram, on every bay.\n\n"
				"A wrong label is a lost sale and a compliance hold. We set aisle "
				"identification so the shelf and the till agree.",
				m["retail-grocery-aisle.jpg"],
				"Grocery aisle with shelf labels and packaged goods",
				1,
			),
			section(
				"Supermarket operations",
				"Stock, price and a scan that hold across a full-format store.\n\n"
				"Receiving, shelf and checkout have to share the same item identity. "
				"That is the retail duty in a busy hall.",
				m["retail-supermarket.jpg"],
				"Supermarket interior with shoppers and stocked aisles",
				2,
			),
			section(
				"Shop-floor and specialty retail",
				"A clean scan and a fast till on a smaller floor.\n\n"
				"Independents and specialty stores still need the same identification "
				"discipline as a chain — without a heavy hall.",
				m["retail-shop-floor.jpg"],
				"Specialty grocery bay with packaged goods and electronic shelf labels",
				3,
			),
			section(
				"Fresh counters",
				"Weighing, a price label and a lot on loose produce and deli.\n\n"
				"The counter is wet and fast. The label has to print clean and scan "
				"at the till before the bag leaves the bay.",
				m["retail-fresh-produce.jpg"],
				"Fresh produce bay with electronic shelf labels",
				4,
			),
			section(
				"Checkout",
				"A scan, a receipt and a till that keep the queue moving.\n\n"
				"Checkout is where aisle errors become a customer wait. We specify "
				"the counter so the scan matches the shelf.",
				m["retail-checkout.jpg"],
				"Retail checkout counter in a store",
				5,
			),
		],
	)


def fill_fashion() -> dict:
	m = media(
		{
			"fashion-garments.jpg": f"{U}-1445205170230-053b83016050?auto=format&fit=crop&w=2000&q=80",
			"fashion-look.jpg": f"{U}-1490481651871-ab68de25d43d?auto=format&fit=crop&w=2000&q=80",
			"fashion-boutique.jpg": f"{U}-1567401893414-76b7b1e5a7a5?auto=format&fit=crop&w=2000&q=80",
			"fashion-store-floor.jpg": f"{U}-1441984904996-e0b6ba687e04?auto=format&fit=crop&w=2000&q=80",
		}
	)
	m["fashion-shopping.jpg"] = from_local(
		"fashion-shopping.jpg", SITE_FILES / "Fashion Store.png"
	)
	return update_industry(
		slug="fashion",
		industry_name="Fashion",
		summary=(
			"Ticketing, garment identification, boutique floors and store systems "
			"for fashion retail in Saudi Arabia."
		),
		overview=(
			"Fashion floors need a ticket, a scan and a stock figure that follow the "
			"garment from DC to rail to till — including returns and a size run.\n\n"
			"Printechs specifies labelling, mobility and store systems for fashion "
			"retailers in Riyadh, Jeddah and Dammam. This page is the application, "
			"not a product list.\n\n"
			"We match the ticket and the floor when you enquire."
		),
		image_alt="Fashion retail checkout with modern POS terminal and store display",
		meta_title="Fashion Retail Solutions | Printechs",
		meta_description=(
			"Fashion ticketing, garment identification, boutique and store-floor systems "
			"for retailers in Saudi Arabia."
		),
		solution_slugs="retail-automation",
		sections=[
			section(
				"Shopping floors",
				"A ticket the customer and the till can both read, on every garment.\n\n"
				"Season and size change the SKU count. The identity still has to match "
				"the rail and the stock file.",
				m["fashion-shopping.jpg"],
				"Folded garments on a fashion table with an electronic shelf label",
				1,
			),
			section(
				"Garment identification",
				"A hang tag, a size label and a barcode that survive the rail.\n\n"
				"The ticket is the item. A missed or swapped tag is a wrong size at "
				"the till and a broken stock count.",
				m["fashion-garments.jpg"],
				"Hanging garments ready for ticketing and store identification",
				2,
			),
			section(
				"Merchandising rails",
				"Price and identity that stay with the look, not only the back stock.\n\n"
				"A displayed piece still needs a scan path back to the SKU. That is "
				"how the floor and the DC stay in step.",
				m["fashion-look.jpg"],
				"Garments merchandised on a retail rail",
				3,
			),
			section(
				"Boutiques",
				"A compact till and a clean scan on a smaller floor.\n\n"
				"Boutiques still need the same ticket discipline as a chain — without "
				"a large back-of-house.",
				m["fashion-boutique.jpg"],
				"Fashion boutique interior with clothing displays",
				4,
			),
			section(
				"Store floor and rails",
				"Mobility on the rail for count, pick and a return.\n\n"
				"Staff walk the floor with the same identity the DC printed. That is "
				"the fashion retail duty.",
				m["fashion-store-floor.jpg"],
				"Fashion store floor with clothing rails",
				5,
			),
		],
	)


def fill_warehouse() -> dict:
	m = media(
		{
			"warehouse-racking.jpg": f"{U}-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=2000&q=80",
			"warehouse-aisle.jpg": f"{U}-1553413077-190dd305871c?auto=format&fit=crop&w=2000&q=80",
			"warehouse-parcels.jpg": f"{U}-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=2000&q=80",
			"warehouse-fulfillment.jpg": f"{U}-1587293852726-70cdb56c2866?auto=format&fit=crop&w=2000&q=80",
			"warehouse-shipping.jpg": f"{U}-1578575437130-527eed3abbec?auto=format&fit=crop&w=2000&q=80",
		}
	)
	return update_industry(
		slug="warehouse-logistics",
		industry_name="Warehouse & Logistics",
		summary=(
			"Racking identity, aisle mobility, parcel labelling, fulfilment and "
			"shipping — for distribution centres in Saudi Arabia."
		),
		overview=(
			"A DC needs a location, a licence plate and a scan that follow the pallet "
			"from inbound to pick to the dock.\n\n"
			"Printechs specifies barcode mobility, labelling and warehouse systems for "
			"distribution centres in Riyadh, Jeddah and Dammam. This page is the "
			"application, not a product list.\n\n"
			"We match the aisle, the tote and the shipper when you enquire."
		),
		image_alt="Warehouse logistics with conveyor, forklift and pallet racking",
		meta_title="Warehouse & Logistics Solutions | Printechs",
		meta_description=(
			"Warehouse racking, aisle mobility, parcel labelling, fulfilment and shipping "
			"systems for distribution centres in Saudi Arabia."
		),
		solution_slugs="warehouse-automation\nbarcode-mobility",
		sections=[
			section(
				"Racking and locations",
				"A location label the truck and the handheld both read, on every bay.\n\n"
				"A faded or missing location is a lost pallet. We set rack identity so "
				"putaway and pick agree.",
				m["warehouse-racking.jpg"],
				"Pallet racking in a distribution warehouse",
				1,
			),
			section(
				"Aisle mobility",
				"A scan on the move — inbound, count and pick in the same aisle.\n\n"
				"Staff walk or ride with the same licence plate the dock printed. That "
				"is the mobility duty.",
				m["warehouse-aisle.jpg"],
				"Warehouse aisle with pallet locations",
				2,
			),
			section(
				"Outbound freight",
				"A shipper label and a licence plate that leave with the truck.\n\n"
				"The carrier and the store both scan the same identity. A weak print "
				"is a missort and a claim.",
				m["warehouse-parcels.jpg"],
				"Outbound freight truck leaving a distribution centre",
				3,
			),
			section(
				"Fulfilment",
				"Pick, pack and a label that leave the DC in one flow.\n\n"
				"The tote, the order and the shipper have to share identity. That is "
				"how fulfilment stays on time.",
				m["warehouse-fulfillment.jpg"],
				"Fulfilment floor with packed goods in a warehouse",
				4,
			),
			section(
				"Shipping and docks",
				"A dock door, a pallet and a scan that close the wave.\n\n"
				"The last scan is the hand-off to the carrier. We specify the dock so "
				"the load and the ASN match.",
				m["warehouse-shipping.jpg"],
				"Container terminal and outbound ocean freight",
				5,
			),
		],
	)


def fill_remaining_industries() -> list[dict]:
	results = [
		fill_food_beverage(),
		fill_bakery(),
		fill_egg_poultry(),
		fill_pharmaceutical(),
		fill_pipe(),
		fill_plastic(),
		fill_steel(),
		fill_retail(),
		fill_fashion(),
		fill_warehouse(),
	]
	return results
