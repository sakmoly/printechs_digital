# Copyright (c) 2026, Printechs and contributors

from printechs_digital.api.mappers.product_mapper import media_asset, split_lines


def map_industry(doc) -> dict:
	image = media_asset(doc.image, doc.image_alt or doc.industry_name, 1200, 800)
	return {
		"id": f"erp-{doc.slug}",
		"slug": doc.slug,
		"name": doc.industry_name,
		"summary": doc.summary or "",
		"image": image
		or {
			"src": "/images/placeholders/industry.svg",
			"alt": doc.industry_name,
			"width": 1200,
			"height": 800,
		},
		"relatedProductSlugs": split_lines(doc.related_product_slugs),
		"relatedSoftwareSlugs": split_lines(doc.related_software_slugs),
		"relatedSolutionSlugs": split_lines(doc.related_solution_slugs),
		"seo": {
			"title": doc.meta_title or f"{doc.industry_name} Industry Solutions | Printechs",
			"description": doc.meta_description or doc.summary or doc.industry_name,
			"canonicalPath": f"/industries/{doc.slug}",
		},
	}
