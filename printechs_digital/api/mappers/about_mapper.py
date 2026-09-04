# Copyright (c) 2026, Printechs and contributors

from printechs_digital.api.mappers.product_mapper import absolute_url, sorted_rows


def map_about_page(doc) -> dict | None:
	if not doc.published:
		return None

	paragraphs = [row.body.strip() for row in sorted_rows(doc.paragraphs) if row.body and row.body.strip()]
	if not paragraphs:
		return None

	meta_description = doc.meta_description or paragraphs[0]
	profile_href = absolute_url(doc.company_profile_file) if doc.company_profile_file else None

	return {
		"eyebrow": doc.eyebrow or "Printechs",
		"title": "About Printechs",
		"tagline": doc.tagline,
		"paragraphs": paragraphs,
		"closingLine": doc.closing_line or "",
		"profileDownload": {
			"label": doc.company_profile_label or "Download Profile",
			"href": profile_href,
		}
		if profile_href
		else None,
		"seo": {
			"title": doc.meta_title or "About Printechs | Industrial, Retail & Software Solutions Saudi Arabia",
			"description": meta_description,
			"canonicalPath": "/company/about",
		},
	}
