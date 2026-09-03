# Copyright (c) 2026, Printechs and contributors

from printechs_digital.api.mappers.product_mapper import media_asset


def map_website_brand(doc) -> dict:
	name = doc.display_name or doc.brand
	logo = media_asset(doc.logo, name, 400, 160)
	canonical_path = f"/brands/{doc.slug}"

	return {
		"id": f"erp-{doc.slug}",
		"slug": doc.slug,
		"name": name,
		"summary": doc.summary or f"{name} technology supplied and supported by Printechs.",
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
