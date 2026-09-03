# Copyright (c) 2026, Printechs and contributors

from frappe.utils import cstr

from printechs_digital.api.mappers.product_mapper import media_asset, split_lines


def map_solution(doc) -> dict:
	image = media_asset(doc.image, doc.image_alt or doc.solution_name, 1600, 1000)
	href = cstr(doc.href) or f"/solutions/{doc.slug}"
	return {
		"id": f"erp-{doc.slug}",
		"slug": doc.slug,
		"name": doc.solution_name,
		"summary": doc.summary or "",
		"href": href,
		"image": image
		or {
			"src": "/images/placeholders/solution.svg",
			"alt": doc.solution_name,
			"width": 1600,
			"height": 1000,
		},
		"relatedProductSlugs": split_lines(doc.related_product_slugs),
		"relatedSoftwareSlugs": split_lines(doc.related_software_slugs),
		"seo": {
			"title": doc.meta_title or f"{doc.solution_name} | Printechs",
			"description": doc.meta_description or doc.summary or doc.solution_name,
			"canonicalPath": href if href.startswith("/") else f"/solutions/{doc.slug}",
		},
	}


def map_featured_solution(doc) -> dict:
	solution = map_solution(doc)
	return {
		"id": solution["id"],
		"title": doc.card_title or doc.solution_name,
		"description": doc.card_summary or doc.summary or "",
		"href": solution["href"],
		"image": solution["image"],
	}
