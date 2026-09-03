# Copyright (c) 2026, Printechs and contributors

import re

import frappe

from printechs_digital.api.mappers.product_mapper import (
	absolute_url,
	html_to_paragraphs,
	media_asset,
	sorted_rows,
)
from printechs_digital.printechs_digital.doctype.website_success_story.website_success_story import (
	INDUSTRY_SLUGS,
)

INDUSTRY_NAMES = {slug: name for name, slug in INDUSTRY_SLUGS.items()}


def parse_video_source(url: str | None, file_path: str | None) -> dict | None:
	if url:
		value = url.strip()
		youtube = extract_youtube_id(value)
		if youtube:
			return {"type": "youtube", "source": youtube}
		vimeo = extract_vimeo_id(value)
		if vimeo:
			return {"type": "vimeo", "source": vimeo}
		if value.startswith(("http://", "https://")):
			return {"type": "hosted", "source": value.replace("http://", "https://", 1)}

	if file_path:
		src = absolute_url(file_path)
		if src:
			return {"type": "hosted", "source": src}

	return None


def extract_youtube_id(url: str) -> str | None:
	patterns = [
		r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/shorts/)([A-Za-z0-9_-]{6,})",
	]
	for pattern in patterns:
		match = re.search(pattern, url)
		if match:
			return match.group(1)
	return None


def extract_vimeo_id(url: str) -> str | None:
	match = re.search(r"(?:vimeo\.com/|player\.vimeo\.com/video/)(\d+)", url)
	return match.group(1) if match else None


def map_story_video(row) -> dict | None:
	parsed = parse_video_source(row.video_url, row.video_file)
	if not parsed:
		return None
	poster = media_asset(row.poster, row.title, 1600, 900) if row.poster else None
	return {
		"type": parsed["type"],
		"source": parsed["source"],
		"title": row.title,
		"poster": poster["src"] if poster else None,
	}


def map_story_image(row) -> dict | None:
	return media_asset(row.image, row.image_alt or row.caption or "", 1600, 900)


def map_success_story_card(doc) -> dict:
	hero = media_asset(doc.hero_image, doc.hero_image_alt or doc.title, 1600, 900)
	industry_name = doc.industry or INDUSTRY_NAMES.get(doc.industry_slug or "", "")
	product_name = None
	if doc.website_product:
		product_name = doc.get("product_name") or None
		if not product_name:
			product_name = frappe.db.get_value("Website Product", doc.website_product, "display_name")

	return {
		"id": f"erp-{doc.slug}",
		"slug": doc.slug,
		"title": doc.title,
		"summary": doc.summary
		or (html_to_paragraphs(doc.story).split("\n\n")[0] if doc.story else ""),
		"customer": doc.customer_name or "",
		"location": doc.location or "",
		"brand": doc.brand or "",
		"brandSlug": doc.brand_slug or "",
		"industry": industry_name,
		"industrySlug": doc.industry_slug or "",
		"productSlug": doc.product_slug or "",
		"productName": product_name or "",
		"image": hero
		or {
			"src": "/images/placeholders/case-study.svg",
			"alt": doc.title,
			"width": 1600,
			"height": 900,
		},
		"href": f"/success-stories/{doc.slug}",
		"seo": {
			"title": doc.meta_title or f"{doc.title} | Printechs",
			"description": doc.meta_description or doc.summary or doc.title,
			"canonicalPath": f"/success-stories/{doc.slug}",
		},
	}


def map_success_story(doc) -> dict:
	card = map_success_story_card(doc)
	videos = [
		video
		for video in (map_story_video(row) for row in sorted_rows(doc.get("videos")))
		if video
	]
	gallery = [
		image
		for image in (map_story_image(row) for row in sorted_rows(doc.get("gallery")))
		if image
	]
	card.update(
		{
			"story": html_to_paragraphs(doc.story),
			"videos": videos,
			"gallery": gallery,
		}
	)
	return card
