# Copyright (c) 2026, Printechs and contributors

from printechs_digital.api.mappers.product_mapper import media_asset


def resolve_brand_href(slug: str) -> str:
	"""Software platform brands link to /software/{slug}; hardware brands to /brands/{slug}."""
	import frappe

	if frappe.db.exists(
		"Website Product",
		{"slug": slug, "published": 1, "show_on_software_list": 1},
	):
		return f"/software/{slug}"
	return f"/brands/{slug}"


def map_website_brand(doc) -> dict:
	name = doc.display_name or doc.brand
	logo = media_asset(doc.logo, name, 400, 160)
	href = resolve_brand_href(doc.slug)
	canonical_path = href

	return {
		"id": f"erp-{doc.slug}",
		"slug": doc.slug,
		"name": name,
		"summary": doc.summary or f"{name} technology supplied and supported by Printechs.",
		"href": href,
		"logo": logo
		or {
			"src": "/images/placeholders/brand.svg",
			"alt": name,
			"width": 400,
			"height": 160,
		},
		"seo": {
			"title": doc.meta_title or f"{name} | Printechs Brands",
			"description": doc.meta_description
			or f"{name} products supplied and supported by Printechs.",
			"canonicalPath": canonical_path,
		},
	}
