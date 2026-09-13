# Copyright (c) 2026, Printechs and contributors
"""Citizen 3-inch (80 mm) POS printers from the official overview.

Source: https://www.citizen-systems.com/en/products/printer/pos/overview

This fill publishes the ten 80 mm models only — not 4-inch CT-S4500 and not
CBM-910II impact. Each page uses unique official photos. Hero video_url stays
empty. featured stays 0 so the homepage featured list is unchanged.

Do not attach spare-part Items (IF2-WF05, Y-cables).
Do not attach a single CT-E301 / CT-E601 Item — those SKUs differ by interface
and colour.
"""

from printechs_digital.setup.citizen_common import (
	BASE,
	apply_identity,
	catalog_card,
	download_file,
	get_or_create,
	ksa_section,
	prepare_citizen_logo,
	save_product,
	set_related,
	set_specs,
	support_items,
	update_website_brand,
	video_section,
)

# Official Citizen Systems Japan film that demonstrates receipt-logo setup on CT-S751.
VIDEO_S751_LOGO = "https://youtu.be/9t7DVOvpWOo"

PREVIEW = f"{BASE}/media/images/printer/POS/Preview"
PROC = f"{BASE}/media/_processed_"

IMAGES = {
	"citizen-ct-e301-hero.jpg": f"{PREVIEW}/Citizen_CT-E301_Black_06_Upper_front_view_210308.jpg",
	"citizen-ct-e301-angle.jpg": f"{PROC}/b/4/csm_CT-E301_Black_01_3-4_angle_with_printout_210415_2faa813d29.jpg",
	"citizen-ct-e301-open.jpg": f"{PROC}/e/f/csm_CT-E301_Black_04_3-4_open_case_without_media_210308_66dd8599ab.jpg",
	"citizen-ct-e301-panel.jpg": f"{PROC}/6/2/csm_CT-E301_Black_07_Panel_close-up_with_lights_210308_4390fc424c.jpg",
	"citizen-ct-e351-hero.jpg": f"{PREVIEW}/Citizen_CT-E351_Black_POS_Upperfront.jpg",
	"citizen-ct-e351-front.jpg": f"{PROC}/5/b/csm_Citizen_CT-E351_Black_POS_Front_2977efeb7e.jpg",
	"citizen-ct-e351-print.jpg": f"{PROC}/6/e/csm_Citizen_CT-E351_Black_POS_Printout_52a1a321a2.jpg",
	"citizen-ct-e351-open.jpg": f"{PROC}/8/6/csm_Citizen_CT-E351_Black_POS_Open_7e5a238c9e.jpg",
	"citizen-ct-e601-hero.jpg": f"{PREVIEW}/Citizen_CT-E601_Black_POS_Front.jpg",
	"citizen-ct-e601-print.jpg": f"{PROC}/5/4/csm_Citizen_CT-E601_Black_POS_Printout_2b2f71ccb7.jpg",
	"citizen-ct-e601-open.jpg": f"{PROC}/7/3/csm_Citizen_CT-E601_Black_POS_Open_be132930d8.jpg",
	"citizen-ct-e601-panel.jpg": f"{PROC}/e/8/csm_Citizen_CT-E601_Black_POS_Panel_Close_Up_09e3d30245.jpg",
	"citizen-ct-e651-hero.jpg": f"{PREVIEW}/Citizen_CT-E651_Black_POS_Upperfront.jpg",
	"citizen-ct-e651-print.jpg": f"{PROC}/8/5/csm_Citizen_CT-E651_Black_POS_Printout_487fbe756b.jpg",
	"citizen-ct-e651-front.jpg": f"{PROC}/0/b/csm_Citizen_CT-E651_Black_POS_Front_c2c49eea4b.jpg",
	"citizen-ct-e651-open.jpg": f"{PROC}/1/3/csm_Citizen_CT-E651_Black_POS_Open_9aba736761.jpg",
	"citizen-ct-e651l-hero.jpg": f"{PROC}/b/3/csm_Citizen_CT-E651L_White_POS_Front_47f2222444.jpg",
	"citizen-ct-e651l-print.jpg": f"{PROC}/0/f/csm_Citizen_CT-E651L_Black_POS_Printout_50aa6e7c1f.jpg",
	"citizen-ct-s310ii-hero.jpg": f"{PREVIEW}/Citizen_CT-S310ii_Black_POS.jpg",
	"citizen-ct-s310ii-open.jpg": f"{PROC}/4/c/csm_Citizen_CT-S310ii_Black_POS_Open_0ebd6ddc85.jpg",
	"citizen-ct-s310ii-ports.jpg": f"{PROC}/b/6/csm_Citizen_CT-S310ii_Black_POS_Connections_e2499996f3.jpg",
	"citizen-ct-s310ii-retail.jpg": f"{PROC}/a/1/csm_Retail_Fresh_Produce_ae38f56f22.jpeg",
	"citizen-ct-s601iir-hero.jpg": f"{PREVIEW}/Citizen_CT-S601IIR_Black_POS_Front.jpg",
	"citizen-ct-s601iir-feed.jpg": f"{PROC}/7/c/csm_Citizen_CT-S601IIR_Black_POS_Feed_98b6b5f1a8.jpg",
	"citizen-ct-s601iir-open.jpg": f"{PROC}/9/8/csm_Citizen_CT-S601IIR_Black_POS_Open_d2390a1c52.jpg",
	"citizen-ct-s601iir-bar.jpg": f"{PROC}/2/3/csm_Hospitality_Bar_Pub_62ed1ac2d6.jpg",
	"citizen-ct-s751-hero.jpg": f"{PREVIEW}/Citizen_CT-S751_White_POS_Front.jpg",
	"citizen-ct-s751-print.jpg": f"{PROC}/4/1/csm_Citizen_CT-S751_Black_White_POS_Printout_cd2abf8751.jpg",
	"citizen-ct-s751-open.jpg": f"{PROC}/b/0/csm_Citizen_CT-S751_Black_POS_Open_7749c63411.jpg",
	"citizen-ct-s751-food.jpg": f"{PROC}/f/4/csm_Hospitality_Food_Court_ef6116877e.jpeg",
	"citizen-ct-s801iii-hero.jpg": f"{PREVIEW}/Citizen_CT-S801III-BK.jpg",
	"citizen-ct-s801iii-oblique.jpg": f"{PROC}/e/1/csm_CT-S801III-BK_Oblique_f25ad4ee0c.jpg",
	"citizen-ct-s801iii-open.jpg": f"{PROC}/a/1/csm_CT-S801III-BK_Open-Paper_a18efd7568.jpg",
	"citizen-ct-s801iii-lcd.jpg": f"{PROC}/f/f/csm_CT-S801III-BK_Display-Online_fd67ca5a8e.jpg",
	"citizen-ct-s851iii-hero.jpg": f"{PREVIEW}/Citizen_CT-S851III-BK.jpg",
	"citizen-ct-s851iii-oblique.jpg": f"{PROC}/9/0/csm_CT-S851III-BK_Oblique_Seperate_50791ca419.jpg",
	"citizen-ct-s851iii-open.jpg": f"{PROC}/c/8/csm_CT-S851III-BK_Open-Paper_d0e8c6cc17.jpg",
	"citizen-ct-s851iii-lcd.jpg": f"{PROC}/a/5/csm_CT-S851III-BK_Oblique_Online_642722f1a9.jpg",
}

RELATED = {
	"citizen-ct-e301": ["citizen-ct-e601", "citizen-ct-e351", "citizen-ct-s310ii"],
	"citizen-ct-e351": ["citizen-ct-e651", "citizen-ct-e301", "citizen-ct-s751"],
	"citizen-ct-e601": ["citizen-ct-e301", "citizen-ct-e651", "citizen-ct-s801iii"],
	"citizen-ct-e651": ["citizen-ct-e651l", "citizen-ct-e351", "citizen-ct-e601"],
	"citizen-ct-e651l": ["citizen-ct-e651", "citizen-ct-s601iir", "citizen-ct-s751"],
	"citizen-ct-s310ii": ["citizen-ct-e301", "citizen-ct-s751", "citizen-ct-e351"],
	"citizen-ct-s601iir": ["citizen-ct-e651l", "citizen-ct-s751", "citizen-ct-e651"],
	"citizen-ct-s751": ["citizen-ct-s801iii", "citizen-ct-s851iii", "citizen-ct-e351"],
	"citizen-ct-s801iii": ["citizen-ct-s851iii", "citizen-ct-s751", "citizen-ct-e601"],
	"citizen-ct-s851iii": ["citizen-ct-s801iii", "citizen-ct-s751", "citizen-ct-e651"],
}


def _media():
	paths = {}
	for filename, url in IMAGES.items():
		paths[filename] = download_file(filename, url)
	cards = {}
	for slug, src in (
		("e301", "citizen-ct-e301-hero.jpg"),
		("e351", "citizen-ct-e351-hero.jpg"),
		("e601", "citizen-ct-e601-hero.jpg"),
		("e651", "citizen-ct-e651-hero.jpg"),
		("e651l", "citizen-ct-e651l-hero.jpg"),
		("s310ii", "citizen-ct-s310ii-hero.jpg"),
		("s601iir", "citizen-ct-s601iir-hero.jpg"),
		("s751", "citizen-ct-s751-hero.jpg"),
		("s801iii", "citizen-ct-s801iii-hero.jpg"),
		("s851iii", "citizen-ct-s851iii-hero.jpg"),
	):
		cards[slug] = catalog_card(src, f"citizen-ct-{slug}-card.jpg")
	paths["cards"] = cards
	return paths


def _fill(m, *, slug, display, label, official, card_key, hero_key, hero_alt, tagline, short, long,
		chips, story, visual, card_title, card_summary, cta, meta_t, meta_d, benefits, stories,
		icons, specs, apps, sections):
	card = m["cards"][card_key]
	hero = card
	doc = get_or_create(slug, display, hero)
	apply_identity(doc, slug=slug, display_name=display, category_label=label)
	doc.tagline = tagline
	doc.short_description = short
	doc.long_description = (
		f"<p>{long}</p>"
		f"<p>Official: <a href=\"{official}\">{display}</a> on Citizen Systems. "
		"Printechs supplies and supports the range in Saudi Arabia.</p>"
	)
	doc.hero_image = hero
	doc.card_image = card
	doc.hero_image_alt = hero_alt
	doc.hero_trust_chips = chips
	doc.story_heading = story
	doc.visual_story_heading = visual
	doc.card_title = card_title
	doc.card_summary = card_summary
	doc.final_cta_heading = cta
	doc.final_cta_description = (
		"Tell us the POS application, interface and media. We will quote the matching "
		"Citizen 80 mm printer — not a mixed family box."
	)
	doc.meta_title = meta_t
	doc.meta_description = meta_d
	doc.set("benefits", benefits)
	doc.set("visual_story_items", stories)
	doc.set("icon_specifications", icons)
	set_specs(doc, specs)
	doc.set("applications", apps)
	doc.set("content_sections", sections)
	doc.set("support_items", support_items())
	doc.set(
		"package_contents",
		[
			{"item_description": f"{display} with the quoted interface and colour", "sort_order": 1},
			{"item_description": "Starter 80 mm media, driver and KSA commissioning as surveyed", "sort_order": 2},
		],
	)
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_e301(m):
	return _fill(
		m,
		slug="citizen-ct-e301",
		display="Citizen CT-E301",
		label="TOP-EXIT 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-e301",
		card_key="e301",
		hero_key="citizen-ct-e301-hero.jpg",
		hero_alt="Citizen CT-E301 black top-exit 80 mm POS printer",
		tagline="Compact top-exit 80 mm printer with SIAA antimicrobial housing",
		short=(
			"Citizen CT-E301 is a compact top-exit 80 mm thermal POS printer with "
			"self-protective SIAA (ISO 22196) housing. USB-only or USB + serial + Ethernet."
		),
		long=(
			"CT-E301 is Citizen’s compact top-exit 80 mm printer for tight checkout "
			"and cash-drawer stacks. Official copy highlights one-hand media change, "
			"a small footprint beside POS systems, and SIAA-marked housing that fulfils "
			"ISO 22196. Choose the USB-only model or the triple USB, serial and Ethernet "
			"model — those are interface options, not separate product pages."
		),
		chips="Top-exit 80 mm\nSIAA / ISO 22196 housing\nUSB or USB · serial · Ethernet\nOne-hand media change",
		story="The compact top-exit Citizen for a clean counter",
		visual="Official CT-E301 — unique to this page",
		card_title="CT-E301",
		card_summary="Compact Citizen top-exit 80 mm POS printer with antimicrobial housing.",
		cta="Specify CT-E301 for a tight checkout",
		meta_t="Citizen CT-E301 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-E301 compact top-exit 80 mm thermal POS printer with SIAA housing. From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "shield", "title": "SIAA housing", "description": "Self-protective body marked to ISO 22196 for wipe-down counters.", "sort_order": 1},
			{"icon": "print", "title": "Top-exit 80 mm", "description": "Receipts exit upward beside a POS or cash drawer.", "sort_order": 2},
			{"icon": "connectivity", "title": "USB or triple I/O", "description": "USB-only, or USB + serial + Ethernet on the quoted model.", "sort_order": 3},
			{"icon": "checkout", "title": "One-hand load", "description": "Official one-hand media change for busy lanes.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-E301", "image": m["citizen-ct-e301-hero.jpg"], "image_alt": "CT-E301 front", "caption": "Official black top-exit CT-E301.", "sort_order": 1},
			{"label": "Printout", "image": m["citizen-ct-e301-angle.jpg"], "image_alt": "CT-E301 with receipt", "caption": "3/4 view with a receipt.", "sort_order": 2},
			{"label": "Open", "image": m["citizen-ct-e301-open.jpg"], "image_alt": "CT-E301 open", "caption": "One-hand media path.", "sort_order": 3},
			{"label": "Panel", "image": m["citizen-ct-e301-panel.jpg"], "image_alt": "CT-E301 panel", "caption": "Status lights on the control panel.", "sort_order": 4},
		],
		icons=[
			{"icon": "print", "title": "80 mm", "description": "Top-exit thermal", "sort_order": 1},
			{"icon": "shield", "title": "SIAA", "description": "ISO 22196 housing", "sort_order": 2},
			{"icon": "connectivity", "title": "USB / triple", "description": "Quoted interface", "sort_order": 3},
			{"icon": "device", "title": "Compact", "description": "Beside the POS", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm thermal POS — top exit"),
				("Housing", "Self-protective SIAA housing, ISO 22196"),
				("Media", "One-hand change; small footprint beside POS / cash drawer"),
				("Interfaces", "USB-only model, or USB + serial + Ethernet model"),
				("Not this page", "CT-E601 (card-slot I/O), CT-E351 front-exit, 4-inch CT-S4500"),
			]),
		],
		apps=[
			{"title": "Retail checkout", "description": "Compact top-exit receipts on grocery and specialty lanes.", "image": m["citizen-ct-e301-angle.jpg"], "image_alt": "CT-E301 on a receipt", "industry_link": "retail", "sort_order": 1},
			{"title": "Hospitality", "description": "Wipe-down counters that need SIAA housing.", "image": m["citizen-ct-e301-hero.jpg"], "image_alt": "CT-E301 housing", "industry_link": "food-beverage", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-e301-panel.jpg"], "CT-E301 control panel", 1)],
	)


def fill_e351(m):
	return _fill(
		m,
		slug="citizen-ct-e351",
		display="Citizen CT-E351",
		label="FRONT-EXIT 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-e351",
		card_key="e351",
		hero_key="citizen-ct-e351-hero.jpg",
		hero_alt="Citizen CT-E351 black front-exit 80 mm POS printer",
		tagline="Stylish front-exit 80 mm printer — 250 mm/s for boutiques and bars",
		short=(
			"Citizen CT-E351 is a compact front-exit 80 mm thermal POS printer. Official "
			"speed is 250 mm/s; body 125 × 170 × 108 mm, 1.26 kg. Ethernet, serial or USB."
		),
		long=(
			"CT-E351 is Citizen’s stylish front-exit 80 mm printer for boutiques, bars and "
			"restaurants. Official figures are 250 mm/s, 125 × 170 × 108 mm and 1.26 kg, "
			"with Ethernet, serial or USB. It is not CT-E651 (300 mm/s, richer I/O) and "
			"not the top-exit CT-E301."
		),
		chips="Front-exit 80 mm\n250 mm/s\n125 × 170 × 108 mm · 1.26 kg\nEthernet · serial · USB",
		story="Front-exit Citizen for boutiques, bars and restaurants",
		visual="Official CT-E351 — unique to this page",
		card_title="CT-E351",
		card_summary="Stylish Citizen front-exit 80 mm POS printer, 250 mm/s, 1.26 kg.",
		cta="Specify CT-E351 for hospitality and boutiques",
		meta_t="Citizen CT-E351 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-E351 front-exit 80 mm thermal POS printer, 250 mm/s. From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "speed", "title": "250 mm/s", "description": "Official ultra-fast receipts for boutique and bar tickets.", "sort_order": 1},
			{"icon": "print", "title": "Front exit", "description": "Receipts present toward the operator, not over the POS.", "sort_order": 2},
			{"icon": "device", "title": "1.26 kg", "description": "125 × 170 × 108 mm — low space on a crowded bar.", "sort_order": 3},
			{"icon": "connectivity", "title": "Ethernet / serial / USB", "description": "Pick the interface on the quote.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-E351", "image": m["citizen-ct-e351-hero.jpg"], "image_alt": "CT-E351", "caption": "Official black front-exit CT-E351.", "sort_order": 1},
			{"label": "Front", "image": m["citizen-ct-e351-front.jpg"], "image_alt": "CT-E351 front", "caption": "Front presentation to the operator.", "sort_order": 2},
			{"label": "Printout", "image": m["citizen-ct-e351-print.jpg"], "image_alt": "CT-E351 receipt", "caption": "250 mm/s thermal receipt.", "sort_order": 3},
			{"label": "Open", "image": m["citizen-ct-e351-open.jpg"], "image_alt": "CT-E351 open", "caption": "Open case and media path.", "sort_order": 4},
		],
		icons=[
			{"icon": "speed", "title": "250 mm/s", "description": "Front-exit thermal", "sort_order": 1},
			{"icon": "device", "title": "1.26 kg", "description": "125 × 170 × 108 mm", "sort_order": 2},
			{"icon": "connectivity", "title": "3 I/O", "description": "Ethernet · serial · USB", "sort_order": 3},
			{"icon": "store", "title": "Hospitality", "description": "Boutiques, bars, restaurants", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm thermal POS — front exit"),
				("Speed", "250 mm/sec (official)"),
				("Body", "125 × 170 × 108 mm, 1.26 kg"),
				("Interfaces", "Ethernet, serial or USB"),
				("Typical use", "Boutiques, bars and restaurants"),
				("Not this page", "CT-E651 300 mm/s, CT-E301 top-exit, CT-S751 350 mm/s"),
			]),
		],
		apps=[
			{"title": "Boutiques", "description": "Compact front-exit receipts on fashion counters.", "image": m["citizen-ct-e351-front.jpg"], "image_alt": "CT-E351 boutique", "industry_link": "fashion", "sort_order": 1},
			{"title": "Bars & restaurants", "description": "Fast tickets where space is tight.", "image": m["citizen-ct-e351-print.jpg"], "image_alt": "CT-E351 hospitality", "industry_link": "food-beverage", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-e351-print.jpg"], "CT-E351 receipt printout", 1)],
	)


def fill_e601(m):
	return _fill(
		m,
		slug="citizen-ct-e601",
		display="Citizen CT-E601",
		label="TOP-EXIT 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-e601",
		card_key="e601",
		hero_key="citizen-ct-e601-hero.jpg",
		hero_alt="Citizen CT-E601 black top-exit 80 mm POS printer",
		tagline="Top-exit 80 mm printer with SIAA housing and a card-slot interface",
		short=(
			"Citizen CT-E601 is the flexible top-exit 80 mm thermal POS printer: SIAA / "
			"ISO 22196 housing, USB plus an optional card for serial, Bluetooth, Ethernet, "
			"WLAN or Lightning."
		),
		long=(
			"CT-E601 shares CT-E301’s self-protective SIAA housing and top-exit layout, "
			"then adds an interface card slot. Official options are serial, Bluetooth, "
			"Ethernet, wireless LAN and Lightning for iPad / iPhone lanes. USB is standard. "
			"Do not treat a Wi-Fi spare (RET.SPA.CTZ.4670) as this printer."
		),
		chips="Top-exit 80 mm\nSIAA / ISO 22196\nUSB + interface card slot\nSerial · BT · LAN · WLAN · Lightning",
		story="The top-exit Citizen when the interface must stay optional",
		visual="Official CT-E601 — unique to this page",
		card_title="CT-E601",
		card_summary="Citizen top-exit 80 mm POS printer with SIAA housing and a card-slot interface.",
		cta="Specify CT-E601 for mixed POS I/O",
		meta_t="Citizen CT-E601 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-E601 top-exit 80 mm POS printer with USB and optional serial, Bluetooth, LAN, WLAN or Lightning. From Printechs.",
		benefits=[
			{"icon": "shield", "title": "SIAA housing", "description": "Same disinfectant-ready family as CT-E301, ISO 22196.", "sort_order": 1},
			{"icon": "connectivity", "title": "Card-slot I/O", "description": "USB plus serial, Bluetooth, Ethernet, WLAN or Lightning.", "sort_order": 2},
			{"icon": "print", "title": "Top-exit 80 mm", "description": "One-hand media change beside the POS.", "sort_order": 3},
			{"icon": "integration", "title": "iPad lanes", "description": "Lightning option for iOS hospitality counters.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-E601", "image": m["citizen-ct-e601-hero.jpg"], "image_alt": "CT-E601", "caption": "Official black top-exit CT-E601.", "sort_order": 1},
			{"label": "Printout", "image": m["citizen-ct-e601-print.jpg"], "image_alt": "CT-E601 receipt", "caption": "Top-exit receipt.", "sort_order": 2},
			{"label": "Open", "image": m["citizen-ct-e601-open.jpg"], "image_alt": "CT-E601 open", "caption": "Open case, one-hand load.", "sort_order": 3},
			{"label": "Panel", "image": m["citizen-ct-e601-panel.jpg"], "image_alt": "CT-E601 panel", "caption": "Control panel close-up.", "sort_order": 4},
		],
		icons=[
			{"icon": "print", "title": "80 mm", "description": "Top-exit thermal", "sort_order": 1},
			{"icon": "shield", "title": "SIAA", "description": "ISO 22196 housing", "sort_order": 2},
			{"icon": "connectivity", "title": "Card slot", "description": "USB + optional I/O", "sort_order": 3},
			{"icon": "device", "title": "Lightning", "description": "iOS hospitality option", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm thermal POS — top exit"),
				("Housing", "Self-protective SIAA housing, ISO 22196"),
				("Standard I/O", "USB, plus interface card slot"),
				("Optional I/O", "Serial, Bluetooth, Ethernet, wireless LAN, Lightning"),
				("Not this page", "CT-E301 fixed triple I/O, CT-E651 front-exit, Wi-Fi spare 4670"),
			]),
		],
		apps=[
			{"title": "Retail POS", "description": "Top-exit receipts where the interface is still being chosen.", "image": m["citizen-ct-e601-print.jpg"], "image_alt": "CT-E601 retail", "industry_link": "retail", "sort_order": 1},
			{"title": "iPad hospitality", "description": "Lightning card for iOS order counters.", "image": m["citizen-ct-e601-hero.jpg"], "image_alt": "CT-E601 hospitality", "industry_link": "food-beverage", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-e601-open.jpg"], "CT-E601 open media path", 1)],
	)


def fill_e651(m):
	return _fill(
		m,
		slug="citizen-ct-e651",
		display="Citizen CT-E651",
		label="FRONT-EXIT 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-e651",
		card_key="e651",
		hero_key="citizen-ct-e651-hero.jpg",
		hero_alt="Citizen CT-E651 black front-exit 80 mm POS printer",
		tagline="Front-exit 80 mm printer — 300 mm/s with USB, Ethernet and serial",
		short=(
			"Citizen CT-E651 is the faster front-exit 80 mm thermal POS printer: 300 mm/s, "
			"USB + Ethernet + serial as standard, optional Wi-Fi or Bluetooth. Receipts only "
			"— labels are CT-E651L."
		),
		long=(
			"CT-E651 is Citizen’s high-endurance front-exit 80 mm receipt printer. Official "
			"speed is 300 mm/s. USB, Ethernet and serial ship as standard; Wi-Fi or Bluetooth "
			"are options. This page is receipts, not the two-in-one CT-E651L label/receipt model."
		),
		chips="Front-exit 80 mm\n300 mm/s\nUSB · Ethernet · serial\nOptional Wi-Fi or Bluetooth",
		story="The 300 mm/s front-exit Citizen for busy receipt lanes",
		visual="Official CT-E651 — unique to this page",
		card_title="CT-E651",
		card_summary="Citizen front-exit 80 mm POS printer, 300 mm/s, USB + Ethernet + serial.",
		cta="Specify CT-E651 for fast front-exit receipts",
		meta_t="Citizen CT-E651 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-E651 front-exit 80 mm thermal POS printer, 300 mm/s, USB Ethernet serial. From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "speed", "title": "300 mm/s", "description": "Official ultra-fast front-exit receipts.", "sort_order": 1},
			{"icon": "connectivity", "title": "USB + LAN + serial", "description": "Three interfaces standard; Wi-Fi or Bluetooth optional.", "sort_order": 2},
			{"icon": "rugged", "title": "High endurance", "description": "Citizen positions E651 for exceptional reliability.", "sort_order": 3},
			{"icon": "print", "title": "Receipts, not labels", "description": "Need liner-free or die-cut labels? That is CT-E651L.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-E651", "image": m["citizen-ct-e651-hero.jpg"], "image_alt": "CT-E651", "caption": "Official black front-exit CT-E651.", "sort_order": 1},
			{"label": "Front", "image": m["citizen-ct-e651-front.jpg"], "image_alt": "CT-E651 front", "caption": "Front presentation.", "sort_order": 2},
			{"label": "Printout", "image": m["citizen-ct-e651-print.jpg"], "image_alt": "CT-E651 receipt", "caption": "300 mm/s thermal receipt.", "sort_order": 3},
			{"label": "Open", "image": m["citizen-ct-e651-open.jpg"], "image_alt": "CT-E651 open", "caption": "Open case.", "sort_order": 4},
		],
		icons=[
			{"icon": "speed", "title": "300 mm/s", "description": "Front-exit thermal", "sort_order": 1},
			{"icon": "connectivity", "title": "3 standard", "description": "USB · Ethernet · serial", "sort_order": 2},
			{"icon": "print", "title": "Receipts", "description": "Not CT-E651L labels", "sort_order": 3},
			{"icon": "rugged", "title": "Endurance", "description": "High-duty front exit", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm thermal POS — front exit, receipts"),
				("Speed", "300 mm/sec (official)"),
				("Standard I/O", "USB, Ethernet and serial"),
				("Optional I/O", "Wi-Fi or Bluetooth"),
				("Not this page", "CT-E651L label+receipt, CT-E351 250 mm/s, CT-S851III 500 mm/s"),
			]),
		],
		apps=[
			{"title": "Retail checkout", "description": "Fast front-exit receipts on grocery and specialty POS.", "image": m["citizen-ct-e651-print.jpg"], "image_alt": "CT-E651 retail", "industry_link": "retail", "sort_order": 1},
			{"title": "Hospitality", "description": "Kitchen or bar tickets that must present forward.", "image": m["citizen-ct-e651-front.jpg"], "image_alt": "CT-E651 hospitality", "industry_link": "food-beverage", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-e651-open.jpg"], "CT-E651 open media path", 1)],
	)


def fill_e651l(m):
	return _fill(
		m,
		slug="citizen-ct-e651l",
		display="Citizen CT-E651L",
		label="LABEL + RECEIPT 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-e651l",
		card_key="e651l",
		hero_key="citizen-ct-e651l-hero.jpg",
		hero_alt="Citizen CT-E651L white front-exit label and receipt POS printer",
		tagline="Two-in-one front-exit — labels and receipts on one 80 mm printer",
		short=(
			"Citizen CT-E651L is the label-capable front-exit 80 mm POS printer for pharmacy, "
			"retail and hospitality. Official speeds: labels up to 200 mm/s, receipts up to 300 mm/s."
		),
		long=(
			"CT-E651L is not the receipt-only CT-E651. Official copy: a front-exit printer "
			"that supports both labels and receipts — up to 200 mm/s on labels and 300 mm/s "
			"on receipts — for pharmacy, retail and hospitality. Quote the media (receipt "
			"roll vs label) with the printer; do not mix liner-free CT-S601IIR onto this page."
		),
		chips="Label + receipt\n200 mm/s labels · 300 mm/s receipts\nFront-exit 80 mm\nPharmacy · retail · hospitality",
		story="One Citizen that prints a receipt or a label",
		visual="Official CT-E651L — unique to this page",
		card_title="CT-E651L",
		card_summary="Citizen two-in-one 80 mm POS printer: labels to 200 mm/s, receipts to 300 mm/s.",
		cta="Specify CT-E651L for label-and-receipt counters",
		meta_t="Citizen CT-E651L Label & Receipt POS Printer | Printechs",
		meta_d="Citizen CT-E651L front-exit 80 mm printer for labels (200 mm/s) and receipts (300 mm/s). From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "print", "title": "Label + receipt", "description": "One front-exit printer, two media jobs — not two devices.", "sort_order": 1},
			{"icon": "speed", "title": "200 / 300 mm/s", "description": "Official: labels to 200 mm/s, receipts to 300 mm/s.", "sort_order": 2},
			{"icon": "store", "title": "Pharmacy & retail", "description": "Citizen names pharmacy, retail and hospitality.", "sort_order": 3},
			{"icon": "inventory", "title": "Not liner-free 601IIR", "description": "Need MAXStick liner-free? That is CT-S601IIR.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-E651L", "image": m["citizen-ct-e651l-hero.jpg"], "image_alt": "CT-E651L white", "caption": "Official white CT-E651L front.", "sort_order": 1},
			{"label": "Printout", "image": m["citizen-ct-e651l-print.jpg"], "image_alt": "CT-E651L print", "caption": "Official label/receipt printout.", "sort_order": 2},
		],
		icons=[
			{"icon": "print", "title": "2-in-1", "description": "Label and receipt", "sort_order": 1},
			{"icon": "speed", "title": "200 / 300", "description": "mm/s official", "sort_order": 2},
			{"icon": "store", "title": "Pharmacy", "description": "Retail · hospitality", "sort_order": 3},
			{"icon": "device", "title": "Front exit", "description": "80 mm Citizen", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm — front-exit label and receipt"),
				("Label speed", "Up to 200 mm/sec (official)"),
				("Receipt speed", "Up to 300 mm/sec (official)"),
				("Typical use", "Pharmacy, retail and hospitality"),
				("Not this page", "CT-E651 receipt-only, CT-S601IIR liner-free, 4-inch CT-S4500"),
			]),
		],
		apps=[
			{"title": "Pharmacy", "description": "Dispense labels and a receipt from one front-exit printer.", "image": m["citizen-ct-e651l-print.jpg"], "image_alt": "CT-E651L pharmacy", "industry_link": "pharmaceutical", "sort_order": 1},
			{"title": "Retail", "description": "Shelf or bag labels plus the customer receipt.", "image": m["citizen-ct-e651l-hero.jpg"], "image_alt": "CT-E651L retail", "industry_link": "retail", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-e651l-print.jpg"], "CT-E651L official printout", 1)],
	)


def fill_s310ii(m):
	return _fill(
		m,
		slug="citizen-ct-s310ii",
		display="Citizen CT-S310II",
		label="VALUE 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-s310ii",
		card_key="s310ii",
		hero_key="citizen-ct-s310ii-hero.jpg",
		hero_alt="Citizen CT-S310II black 80 mm POS printer",
		tagline="Cost-conscious 80 mm printer — 160 mm/s with paper-save functions",
		short=(
			"Citizen CT-S310II is the environmentally minded 80 mm thermal POS printer: "
			"160 mm/s, variable paper widths, receipt and barcode printing, power- and paper-save."
		),
		long=(
			"CT-S310II is Citizen’s value 80 mm printer when the lane does not need 300–500 mm/s. "
			"Official points: 160 mm/s, choice of paper widths, receipt and barcode printing, "
			"and power / paper-save functions. Step up to CT-E351 or CT-S751 when the ticket "
			"volume needs more speed."
		),
		chips="160 mm/s\nVariable paper widths\nReceipt + barcode\nPower and paper save",
		story="The economical Citizen 80 mm for everyday receipts",
		visual="Official CT-S310II — unique to this page",
		card_title="CT-S310II",
		card_summary="Citizen value 80 mm POS printer: 160 mm/s, variable widths, paper-save.",
		cta="Specify CT-S310II for cost-conscious lanes",
		meta_t="Citizen CT-S310II 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-S310II 80 mm thermal POS printer, 160 mm/s, variable paper widths. From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "print", "title": "160 mm/s", "description": "Official speed for everyday receipts and barcodes.", "sort_order": 1},
			{"icon": "lines", "title": "Variable widths", "description": "Choice of paper widths on the same family.", "sort_order": 2},
			{"icon": "cloud", "title": "Paper save", "description": "Official power- and paper-save functions.", "sort_order": 3},
			{"icon": "checkout", "title": "Receipt + barcode", "description": "Tickets and codes from one 80 mm printer.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-S310II", "image": m["citizen-ct-s310ii-hero.jpg"], "image_alt": "CT-S310II", "caption": "Official black CT-S310II.", "sort_order": 1},
			{"label": "Open", "image": m["citizen-ct-s310ii-open.jpg"], "image_alt": "CT-S310II open", "caption": "Open media path.", "sort_order": 2},
			{"label": "Ports", "image": m["citizen-ct-s310ii-ports.jpg"], "image_alt": "CT-S310II connections", "caption": "Rear connections.", "sort_order": 3},
			{"label": "Fresh retail", "image": m["citizen-ct-s310ii-retail.jpg"], "image_alt": "Fresh produce retail", "caption": "Official fresh-produce retail scene.", "sort_order": 4},
		],
		icons=[
			{"icon": "speed", "title": "160 mm/s", "description": "Everyday thermal", "sort_order": 1},
			{"icon": "lines", "title": "Widths", "description": "Variable paper", "sort_order": 2},
			{"icon": "print", "title": "Barcode", "description": "Receipt + code", "sort_order": 3},
			{"icon": "store", "title": "Value", "description": "Cost-conscious POS", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm thermal POS — value / eco"),
				("Speed", "160 mm/sec (official)"),
				("Media", "Variable paper widths; receipt and barcode printing"),
				("Eco", "Power-save and paper-save functions"),
				("Not this page", "CT-E351 250 mm/s, CT-S751 350 mm/s, CT-S801III 500 mm/s"),
			]),
		],
		apps=[
			{"title": "Fresh retail", "description": "Everyday receipts on produce and grocery counters.", "image": m["citizen-ct-s310ii-retail.jpg"], "image_alt": "Fresh produce", "industry_link": "retail", "sort_order": 1},
			{"title": "General POS", "description": "Barcode tickets where speed is secondary to cost.", "image": m["citizen-ct-s310ii-hero.jpg"], "image_alt": "CT-S310II POS", "industry_link": "retail", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-s310ii-ports.jpg"], "CT-S310II rear connections", 1)],
	)


def fill_s601iir(m):
	return _fill(
		m,
		slug="citizen-ct-s601iir",
		display="Citizen CT-S601IIR",
		label="LINER-FREE 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-s601iir",
		card_key="s601iir",
		hero_key="citizen-ct-s601iir-hero.jpg",
		hero_alt="Citizen CT-S601IIR black liner-free 80 mm POS printer",
		tagline="Liner-free re-stick labels — 175 mm/s, 203 dpi, top exit",
		short=(
			"Citizen CT-S601IIR is the liner-free, re-stick version of CT-S601II. Official: "
			"175 mm/s, 203 dpi, MAXStick and Nakagawa media, continuous roll labels, top exit."
		),
		long=(
			"CT-S601IIR is not a standard receipt printer and not CT-E651L die-cut labels. "
			"Citizen calls it a special re-stick, liner-free CT-S601II: print–stick–done "
			"labels from a top exit, 175 mm/s, 203 dpi, compatible with MAXStick® and "
			"Nakagawa media. Quote the liner-free roll with the printer."
		),
		chips="Liner-free labels\n175 mm/s · 203 dpi\nMAXStick · Nakagawa\nTop-exit continuous roll",
		story="Print, stick, done — without a liner",
		visual="Official CT-S601IIR — unique to this page",
		card_title="CT-S601IIR",
		card_summary="Citizen liner-free 80 mm POS label printer: 175 mm/s, 203 dpi, top exit.",
		cta="Specify CT-S601IIR for liner-free labels",
		meta_t="Citizen CT-S601IIR Liner-Free POS Printer | Printechs",
		meta_d="Citizen CT-S601IIR liner-free 80 mm POS label printer, 175 mm/s, 203 dpi, MAXStick/Nakagawa. From Printechs.",
		benefits=[
			{"icon": "print", "title": "Liner-free", "description": "Re-stick labels without a silicone liner waste stream.", "sort_order": 1},
			{"icon": "speed", "title": "175 mm/s · 203 dpi", "description": "Official speed and resolution for continuous rolls.", "sort_order": 2},
			{"icon": "consumables", "title": "MAXStick / Nakagawa", "description": "Official media families — quoted with the printer.", "sort_order": 3},
			{"icon": "store", "title": "Hospitality prep", "description": "Temporary labels across kitchen and bar stations.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-S601IIR", "image": m["citizen-ct-s601iir-hero.jpg"], "image_alt": "CT-S601IIR", "caption": "Official black CT-S601IIR.", "sort_order": 1},
			{"label": "Feed", "image": m["citizen-ct-s601iir-feed.jpg"], "image_alt": "CT-S601IIR feed", "caption": "Top-exit liner-free feed.", "sort_order": 2},
			{"label": "Open", "image": m["citizen-ct-s601iir-open.jpg"], "image_alt": "CT-S601IIR open", "caption": "Open case.", "sort_order": 3},
			{"label": "Bar", "image": m["citizen-ct-s601iir-bar.jpg"], "image_alt": "Hospitality bar", "caption": "Official hospitality bar scene.", "sort_order": 4},
		],
		icons=[
			{"icon": "print", "title": "Liner-free", "description": "Re-stick labels", "sort_order": 1},
			{"icon": "speed", "title": "175 mm/s", "description": "203 dpi", "sort_order": 2},
			{"icon": "consumables", "title": "MAXStick", "description": "Nakagawa media", "sort_order": 3},
			{"icon": "store", "title": "Prep labels", "description": "Kitchen and bar", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm — liner-free top-exit labels"),
				("Speed", "175 mm/sec (official)"),
				("Resolution", "203 dpi"),
				("Media", "MAXStick® and Nakagawa liner-free; continuous roll"),
				("Not this page", "CT-E651L die-cut/receipt, standard CT-S601II, receipt-only E-series"),
			]),
		],
		apps=[
			{"title": "Hospitality prep", "description": "Temporary liner-free labels on bar and kitchen tickets.", "image": m["citizen-ct-s601iir-bar.jpg"], "image_alt": "Bar labels", "industry_link": "food-beverage", "sort_order": 1},
			{"title": "Retail", "description": "Re-stick price or bag labels without liner waste.", "image": m["citizen-ct-s601iir-feed.jpg"], "image_alt": "Liner-free feed", "industry_link": "retail", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-s601iir-open.jpg"], "CT-S601IIR open case", 1)],
	)


def fill_s751(m):
	return _fill(
		m,
		slug="citizen-ct-s751",
		display="Citizen CT-S751",
		label="350 MM/S 80 MM",
		official=f"{BASE}/en/products/printer/pos/ct-s751",
		card_key="s751",
		hero_key="citizen-ct-s751-hero.jpg",
		hero_alt="Citizen CT-S751 white 80 mm POS printer",
		tagline="Ultra-fast 350 mm/s 80 mm printer with under-counter mounting",
		short=(
			"Citizen CT-S751 is a compact 80 mm direct-thermal POS printer: 350 mm/s at 203 dpi, "
			"USB plus serial / Ethernet / Bluetooth / Wi-Fi options, full or partial guillotine, "
			"black or white, optional under-counter bracket."
		),
		long=(
			"CT-S751 is Citizen’s adaptable high-speed 80 mm printer. Official: 350 mm/s at "
			"203 dpi, compact black or white body, standard USB with serial, Ethernet, "
			"Bluetooth and Wi-Fi options, full or partial guillotine, and an optional "
			"secure under-counter bracket. It is not the 500 mm/s CT-S801III / CT-S851III."
		),
		chips="350 mm/s · 203 dpi\nUSB + optional I/O\nFull or partial cutter\nUnder-counter bracket",
		story="The 350 mm/s Citizen that can hide under the counter",
		visual="Official CT-S751 — unique to this page",
		card_title="CT-S751",
		card_summary="Citizen 80 mm POS printer: 350 mm/s, 203 dpi, optional under-counter mount.",
		cta="Specify CT-S751 for fast hidden printers",
		meta_t="Citizen CT-S751 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-S751 80 mm thermal POS printer, 350 mm/s, 203 dpi, under-counter option. From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "speed", "title": "350 mm/s", "description": "Official 203 dpi direct thermal — faster than E351, short of 801III.", "sort_order": 1},
			{"icon": "install", "title": "Under-counter", "description": "Optional secure bracket for a hidden printer.", "sort_order": 2},
			{"icon": "print", "title": "Guillotine", "description": "Full or partial cutter on the quote.", "sort_order": 3},
			{"icon": "connectivity", "title": "USB + options", "description": "Serial, Ethernet, Bluetooth and Wi-Fi cards.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-S751", "image": m["citizen-ct-s751-hero.jpg"], "image_alt": "CT-S751 white", "caption": "Official white CT-S751.", "sort_order": 1},
			{"label": "Pair", "image": m["citizen-ct-s751-print.jpg"], "image_alt": "CT-S751 black and white", "caption": "Black and white with printout.", "sort_order": 2},
			{"label": "Open", "image": m["citizen-ct-s751-open.jpg"], "image_alt": "CT-S751 open", "caption": "Open black CT-S751.", "sort_order": 3},
			{"label": "Food court", "image": m["citizen-ct-s751-food.jpg"], "image_alt": "Food court", "caption": "Official food-court scene.", "sort_order": 4},
		],
		icons=[
			{"icon": "speed", "title": "350 mm/s", "description": "203 dpi thermal", "sort_order": 1},
			{"icon": "install", "title": "Under counter", "description": "Optional bracket", "sort_order": 2},
			{"icon": "print", "title": "Guillotine", "description": "Full or partial", "sort_order": 3},
			{"icon": "device", "title": "B / W", "description": "Black or white", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm direct thermal POS"),
				("Speed", "350 mm/sec at 203 dpi (official)"),
				("Cutter", "Full and partial guillotine"),
				("Interfaces", "USB standard; serial, Ethernet, Bluetooth, Wi-Fi options"),
				("Mounting", "Optional secure under-counter bracket"),
				("Not this page", "CT-S801III / CT-S851III 500 mm/s, CT-E351 250 mm/s"),
			]),
		],
		apps=[
			{"title": "Food court", "description": "Fast tickets that can sit under the counter.", "image": m["citizen-ct-s751-food.jpg"], "image_alt": "Food court", "industry_link": "food-beverage", "sort_order": 1},
			{"title": "Retail checkout", "description": "Hidden 80 mm printer on a clean lane.", "image": m["citizen-ct-s751-hero.jpg"], "image_alt": "CT-S751 retail", "industry_link": "retail", "sort_order": 2},
		],
		sections=[
			video_section(
				heading="Official receipt-logo setup",
				body=(
					"Citizen Systems Japan’s official film shows how to register a shop logo "
					"on a receipt printer, using CT-S751 as the example. Plays in this section "
					"— not on the hero photo. Unique to this page."
				),
				video_url=VIDEO_S751_LOGO,
				image=m["citizen-ct-s751-print.jpg"],
				image_alt="CT-S751 black and white printers",
				sort_order=1,
			),
			ksa_section(m["citizen-ct-s751-open.jpg"], "CT-S751 open case", 2),
		],
	)


def fill_s801iii(m):
	return _fill(
		m,
		slug="citizen-ct-s801iii",
		display="Citizen CT-S801III",
		label="500 MM/S TOP-EXIT",
		official=f"{BASE}/en/products/printer/pos/ct-s801iii",
		card_key="s801iii",
		hero_key="citizen-ct-s801iii-hero.jpg",
		hero_alt="Citizen CT-S801III black top-exit 80 mm POS printer with LCD",
		tagline="Classic POS reimagined — 500 mm/s top-exit with a customisable LCD",
		short=(
			"Citizen CT-S801III is the top-exit 80 mm flagship: up to 500 mm/s, customisable "
			"LCD, internal detachable PSU, USB plus optional Wi-Fi, serial, Bluetooth, Ethernet "
			"or parallel. Front-exit 500 mm/s is CT-S851III."
		),
		long=(
			"CT-S801III is Citizen’s top-exit 500 mm/s 80 mm printer. Official highlights: "
			"customisable LCD operating panel, backwards compatibility with earlier CT-S "
			"models, internal detachable power supply, standard USB and optional Wi-Fi, "
			"serial, Bluetooth, Ethernet or parallel. Spill-proof front-exit at the same "
			"speed is CT-S851III — a different page."
		),
		chips="Up to 500 mm/s\nTop-exit 80 mm\nCustomisable LCD\nInternal detachable PSU",
		story="The 500 mm/s top-exit Citizen with an LCD the operator can read",
		visual="Official CT-S801III — unique to this page",
		card_title="CT-S801III",
		card_summary="Citizen top-exit 80 mm flagship: 500 mm/s, LCD panel, internal PSU.",
		cta="Specify CT-S801III for top-exit flagship lanes",
		meta_t="Citizen CT-S801III 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-S801III top-exit 80 mm POS printer, 500 mm/s, LCD panel. From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "speed", "title": "500 mm/s", "description": "Official super-fast top-exit receipts.", "sort_order": 1},
			{"icon": "display", "title": "Custom LCD", "description": "Operating panel the supervisor can tailor.", "sort_order": 2},
			{"icon": "device", "title": "Internal PSU", "description": "Detachable power supply inside the printer.", "sort_order": 3},
			{"icon": "integration", "title": "CT-S compatible", "description": "Backwards compatibility with previous CT-S models.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-S801III", "image": m["citizen-ct-s801iii-hero.jpg"], "image_alt": "CT-S801III", "caption": "Official black CT-S801III.", "sort_order": 1},
			{"label": "Oblique", "image": m["citizen-ct-s801iii-oblique.jpg"], "image_alt": "CT-S801III angle", "caption": "LCD top-exit body.", "sort_order": 2},
			{"label": "Open", "image": m["citizen-ct-s801iii-open.jpg"], "image_alt": "CT-S801III open", "caption": "Open with paper loaded.", "sort_order": 3},
			{"label": "LCD", "image": m["citizen-ct-s801iii-lcd.jpg"], "image_alt": "CT-S801III LCD", "caption": "Online LCD status.", "sort_order": 4},
		],
		icons=[
			{"icon": "speed", "title": "500 mm/s", "description": "Top-exit thermal", "sort_order": 1},
			{"icon": "display", "title": "LCD", "description": "Customisable panel", "sort_order": 2},
			{"icon": "device", "title": "Internal PSU", "description": "Detachable supply", "sort_order": 3},
			{"icon": "connectivity", "title": "USB + cards", "description": "Wi-Fi · BT · LAN", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm thermal POS — top-exit flagship"),
				("Speed", "Up to 500 mm/sec (official)"),
				("Panel", "Customisable LCD operating panel"),
				("Power", "Internal detachable power supply"),
				("Interfaces", "USB standard; Wi-Fi, serial, Bluetooth, Ethernet, parallel options"),
				("Not this page", "CT-S851III front-exit 500 mm/s, CT-S751 350 mm/s"),
			]),
		],
		apps=[
			{"title": "High-volume retail", "description": "Top-exit flagship receipts on grocery and specialty POS.", "image": m["citizen-ct-s801iii-oblique.jpg"], "image_alt": "CT-S801III retail", "industry_link": "retail", "sort_order": 1},
			{"title": "Hospitality", "description": "LCD status the pass can read at a glance.", "image": m["citizen-ct-s801iii-lcd.jpg"], "image_alt": "CT-S801III LCD", "industry_link": "food-beverage", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-s801iii-open.jpg"], "CT-S801III open with paper", 1)],
	)


def fill_s851iii(m):
	return _fill(
		m,
		slug="citizen-ct-s851iii",
		display="Citizen CT-S851III",
		label="500 MM/S FRONT-EXIT",
		official=f"{BASE}/en/products/printer/pos/ct-s851iii",
		card_key="s851iii",
		hero_key="citizen-ct-s851iii-hero.jpg",
		hero_alt="Citizen CT-S851III black front-exit 80 mm POS printer with LCD",
		tagline="Front-exit 500 mm/s with a spill-proof cover — hospitality flagship",
		short=(
			"Citizen CT-S851III is the only front-exit POS printer Citizen lists at 500 mm/s. "
			"Spill-proof cover, customisable LCD, internal PSU, USB plus optional Wi-Fi, serial, "
			"Bluetooth, Ethernet or parallel. Top-exit twin is CT-S801III."
		),
		long=(
			"CT-S851III is designed for hospitality: a spill-proof cover and front paper exit "
			"at 500 mm/s — Citizen calls it the only front-exit POS printer at that speed. "
			"It shares the CT-S801III LCD, internal detachable PSU and interface card options. "
			"Do not quote 801III when the ticket must present forward and survive a wet bar."
		),
		chips="Up to 500 mm/s\nFront-exit · spill-proof\nCustomisable LCD\nHospitality flagship",
		story="The 500 mm/s front-exit Citizen for wet hospitality counters",
		visual="Official CT-S851III — unique to this page",
		card_title="CT-S851III",
		card_summary="Citizen front-exit 80 mm flagship: 500 mm/s, spill-proof cover, LCD.",
		cta="Specify CT-S851III for front-exit flagship lanes",
		meta_t="Citizen CT-S851III 80mm POS Printer Saudi Arabia | Printechs",
		meta_d="Citizen CT-S851III front-exit 80 mm POS printer, 500 mm/s, spill-proof cover. From Printechs in Saudi Arabia.",
		benefits=[
			{"icon": "speed", "title": "500 mm/s front exit", "description": "Citizen’s only front-exit printer at this official speed.", "sort_order": 1},
			{"icon": "rugged", "title": "Spill-proof cover", "description": "Hospitality body for wet bars and pass stations.", "sort_order": 2},
			{"icon": "display", "title": "Custom LCD", "description": "Same customisable panel language as CT-S801III.", "sort_order": 3},
			{"icon": "connectivity", "title": "USB + cards", "description": "Wi-Fi, serial, Bluetooth, Ethernet or parallel.", "sort_order": 4},
		],
		stories=[
			{"label": "CT-S851III", "image": m["citizen-ct-s851iii-hero.jpg"], "image_alt": "CT-S851III", "caption": "Official black CT-S851III.", "sort_order": 1},
			{"label": "Oblique", "image": m["citizen-ct-s851iii-oblique.jpg"], "image_alt": "CT-S851III angle", "caption": "Front-exit LCD body.", "sort_order": 2},
			{"label": "Open", "image": m["citizen-ct-s851iii-open.jpg"], "image_alt": "CT-S851III open", "caption": "Open with paper loaded.", "sort_order": 3},
			{"label": "LCD", "image": m["citizen-ct-s851iii-lcd.jpg"], "image_alt": "CT-S851III LCD", "caption": "Online LCD, unique to this page.", "sort_order": 4},
		],
		icons=[
			{"icon": "speed", "title": "500 mm/s", "description": "Front-exit thermal", "sort_order": 1},
			{"icon": "rugged", "title": "Spill-proof", "description": "Hospitality cover", "sort_order": 2},
			{"icon": "display", "title": "LCD", "description": "Customisable panel", "sort_order": 3},
			{"icon": "store", "title": "Hospitality", "description": "Bar and pass", "sort_order": 4},
		],
		specs=[
			("Printer", [
				("Family", "Citizen 3-inch / 80 mm thermal POS — front-exit flagship"),
				("Speed", "Up to 500 mm/sec (official) — only Citizen front-exit at this speed"),
				("Cover", "Spill-proof cover for hospitality"),
				("Panel", "Customisable LCD operating panel"),
				("Power", "Internal detachable power supply"),
				("Not this page", "CT-S801III top-exit, CT-S751 350 mm/s, CT-E651 300 mm/s"),
			]),
		],
		apps=[
			{"title": "Hospitality pass", "description": "Front-exit tickets that survive a wet bar.", "image": m["citizen-ct-s851iii-oblique.jpg"], "image_alt": "CT-S851III hospitality", "industry_link": "food-beverage", "sort_order": 1},
			{"title": "Retail checkout", "description": "Operator-facing 500 mm/s receipts.", "image": m["citizen-ct-s851iii-hero.jpg"], "image_alt": "CT-S851III retail", "industry_link": "retail", "sort_order": 2},
		],
		sections=[ksa_section(m["citizen-ct-s851iii-open.jpg"], "CT-S851III open with paper", 1)],
	)


def fill_citizen_pos_80mm():
	logo = prepare_citizen_logo()
	update_website_brand(logo)
	media = _media()
	names = {
		"e301": fill_e301(media),
		"e351": fill_e351(media),
		"e601": fill_e601(media),
		"e651": fill_e651(media),
		"e651l": fill_e651l(media),
		"s310ii": fill_s310ii(media),
		"s601iir": fill_s601iir(media),
		"s751": fill_s751(media),
		"s801iii": fill_s801iii(media),
		"s851iii": fill_s851iii(media),
	}
	# Related rows need sibling docs — refresh once.
	media = _media()
	fill_e301(media)
	fill_e351(media)
	fill_e601(media)
	fill_e651(media)
	fill_e651l(media)
	fill_s310ii(media)
	fill_s601iir(media)
	fill_s751(media)
	fill_s801iii(media)
	fill_s851iii(media)
	return names
