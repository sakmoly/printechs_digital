# Copyright (c) 2026, Printechs and contributors

from printechs_digital.api.mappers.product_mapper import sorted_rows


def whatsapp_href(number: str) -> str | None:
	digits = "".join(char for char in number if char.isdigit())
	return f"https://wa.me/{digits}" if digits else None


def map_specialist_whatsapp(doc) -> dict | None:
	number = (doc.specialist_whatsapp_number or "").strip()
	href = whatsapp_href(number)
	if not href:
		return None

	return {
		"number": number,
		"label": doc.specialist_whatsapp_label or "Chat on WhatsApp",
		"href": href,
	}


def map_contact_page(doc) -> dict | None:
	if not doc.published:
		return None

	offices = []
	for row in sorted_rows(doc.offices):
		if not row.city or not row.address:
			continue

		offices.append(
			{
				"city": row.city.strip(),
				"phone": (row.phone or "").strip(),
				"email": (row.email or "").strip(),
				"address": row.address.strip(),
				"mapEmbedUrl": (row.map_embed_url or "").strip() or None,
			}
		)

	if not offices:
		return None

	return {
		"eyebrow": doc.eyebrow or "Contact",
		"title": doc.title or "Contact Printechs",
		"tagline": doc.tagline,
		"form": {
			"eyebrow": doc.form_eyebrow or "Leave a message",
			"title": doc.form_title or "Need Assistance?",
			"description": doc.form_description
			or "We are here to help and answer any question you might have. We look forward to hearing from you.",
		},
		"specialist": {
			"eyebrow": doc.specialist_eyebrow or "Printechs",
			"title": doc.specialist_title or "Talk to a specialist",
			"description": doc.specialist_description
			or "Industrial coding, retail technology, and enterprise software across Saudi Arabia.",
			"email": doc.specialist_email or "info@printechs.com",
			"phone": doc.specialist_phone or "+966 11 206 2828 | +966 11 206 2929",
			"location": doc.specialist_location or "Riyadh, Jeddah & Dammam, Kingdom of Saudi Arabia",
			"officeHours": doc.specialist_office_hours or "Sunday – Thursday, 9:00 AM – 6:00 PM (AST)",
			"whatsapp": map_specialist_whatsapp(doc),
			"pricing": {
				"title": doc.specialist_pricing_title or "Looking for pricing?",
				"linkLabel": doc.specialist_pricing_link_label or "Products",
				"linkHref": doc.specialist_pricing_link_href or "/products",
				"description": doc.specialist_pricing_description
				or "to open a product and request a quote with the correct item context.",
			},
		},
		"offices": offices,
		"seo": {
			"title": doc.meta_title or "Contact Printechs | Riyadh, Jeddah & Dammam",
			"description": doc.meta_description
			or "Contact Printechs offices in Riyadh, Jeddah and Dammam for industrial, retail and software solutions across Saudi Arabia.",
			"canonicalPath": "/contact",
		},
	}
