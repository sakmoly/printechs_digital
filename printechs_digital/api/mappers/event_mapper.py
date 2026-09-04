# Copyright (c) 2026, Printechs and contributors

from printechs_digital.api.mappers.product_mapper import absolute_url, html_to_paragraphs, media_asset, sorted_rows


def map_event_card(doc) -> dict:
	cover = media_asset(doc.cover_image, doc.cover_image_alt or doc.title)
	image_count = len(doc.get("gallery") or []) + (1 if doc.cover_image else 0)

	return {
		"id": doc.name,
		"slug": doc.slug,
		"title": doc.title,
		"summary": doc.summary or "",
		"eventType": doc.event_type or "Other",
		"eventDate": doc.event_date,
		"location": doc.location or "",
		"image": cover,
		"imageCount": image_count,
		"href": f"/company/events/{doc.slug}",
		"seo": {
			"title": doc.meta_title or f"{doc.title} | Printechs Events",
			"description": doc.meta_description or doc.summary or doc.title,
			"canonicalPath": f"/company/events/{doc.slug}",
		},
	}


def map_event_album(doc) -> dict:
	card = map_event_card(doc)
	gallery = [
		media_asset(row.image, row.image_alt or row.caption or doc.title)
		for row in sorted_rows(doc.get("gallery"))
		if row.image
	]

	description = html_to_paragraphs(doc.description) if doc.description else ""

	return {
		**card,
		"description": description,
		"gallery": gallery,
	}
