# Copyright (c) 2026, Printechs and contributors

from frappe.utils import cstr

from printechs_digital.api.mappers.product_mapper import media_asset, sorted_rows, split_lines

VIDEO_TYPE_MAP = {
	"YouTube": "youtube",
	"Vimeo": "vimeo",
	"Hosted": "hosted",
}


def homepage_asset(path: str | None, alt: str, width: int, height: int) -> dict | None:
	value = cstr(path)
	if not value:
		return None
	if value.startswith("/images/"):
		return {"src": value, "alt": alt or "", "width": width, "height": height}
	return media_asset(value, alt, width, height)


def map_homepage(doc) -> dict | None:
	if not doc.published:
		return None

	if doc.hero_media_kind == "Hosted Video":
		media = {
			"kind": "hosted-video",
			"src": cstr(doc.hero_video),
			"poster": cstr(doc.hero_video_poster) or None,
			"alt": doc.hero_image_alt or doc.hero_headline,
		}
	else:
		image = homepage_asset(doc.hero_image, doc.hero_image_alt or doc.hero_headline, 1920, 1080)
		media = {
			"kind": "image",
			"src": image["src"] if image else "",
			"alt": image["alt"] if image else doc.hero_headline,
		}

	hero = {
		"headline": doc.hero_headline,
		"supportingText": doc.hero_supporting_text,
		"eyebrow": doc.hero_eyebrow or "Printechs",
		"chips": split_lines(doc.hero_chips),
		"media": media,
		"primaryCta": {
			"label": doc.hero_primary_label or "Explore Solutions",
			"href": doc.hero_primary_href or "/solutions",
			"variant": "primary",
		},
		"secondaryCta": {
			"label": doc.hero_secondary_label or "Talk to a Specialist",
			"href": doc.hero_secondary_href or "/contact",
			"variant": "secondary",
		},
	}

	why = None
	points = [
		{"title": row.title, "body": row.body}
		for row in sorted_rows(doc.why_points)
		if row.title and row.body
	]
	if doc.show_why and (doc.why_title or points):
		why = {
			"eyebrow": doc.why_eyebrow or "Why Printechs",
			"title": doc.why_title or "A partner for technology that has to work",
			"description": doc.why_description
			or "Premium systems, practical delivery and long-term support — without marketplace clutter.",
			"points": points,
		}

	video = None
	if doc.show_video and doc.video_source:
		poster = homepage_asset(doc.video_poster, doc.video_title or "Video", 1920, 1080)
		video = {
			"id": "homepage-video",
			"slug": "homepage-video",
			"title": doc.video_title or "See the Printechs digital experience",
			"summary": doc.video_summary or "",
			"eyebrow": doc.video_eyebrow or "Digital experience",
			"video": {
				"type": VIDEO_TYPE_MAP.get(doc.video_type, "youtube"),
				"source": doc.video_source,
				"title": doc.video_title or "Printechs Digital Experience",
				"poster": poster["src"] if poster else None,
			},
			"seo": {
				"title": doc.video_title or "Printechs Digital Experience Video",
				"description": doc.video_summary or "",
				"canonicalPath": "/",
			},
		}

	stories = None
	if doc.get("show_stories"):
		stories = {
			"eyebrow": doc.stories_eyebrow or "Case studies",
			"title": doc.stories_title or "Technology deployed where performance matters",
			"description": doc.stories_description
			or "Selected project stories from industrial and retail environments.",
			"limit": int(doc.stories_limit or 2),
		}

	cta = None
	if doc.show_cta:
		cta = {
			"title": doc.cta_title or "Talk to a Printechs specialist",
			"description": doc.cta_description
			or "Request a quote, book a demo, or plan a site visit with our team in Saudi Arabia.",
			"primaryLabel": doc.cta_primary_label or "Request Quote",
			"primaryHref": doc.cta_primary_href or "/request-quote",
			"secondaryLabel": doc.cta_secondary_label or "Request Demo",
			"secondaryHref": doc.cta_secondary_href or "/request-demo",
		}

	divisions = None
	if doc.get("show_divisions"):
		items = []
		for row in sorted_rows(doc.get("divisions")):
			image = homepage_asset(row.image, row.image_alt or row.title, 1200, 900)
			if not row.title or not image:
				continue
			items.append(
				{
					"id": f"division-{row.idx}",
					"title": row.title,
					"summary": row.summary or "",
					"href": row.href or "/solutions",
					"items": split_lines(row.items),
					"image": image,
				}
			)
		divisions = {
			"eyebrow": doc.divisions_eyebrow or "Capabilities",
			"title": doc.divisions_title or "Three divisions. One technology partner.",
			"description": doc.divisions_description
			or "Industrial systems, retail technology and enterprise software — each with a clear focus and deep delivery expertise.",
			"items": items,
		}

	featured_solutions = None
	if doc.get("show_featured_solutions"):
		featured_solutions = {
			"eyebrow": doc.featured_solutions_eyebrow or "Featured solutions",
			"title": doc.featured_solutions_title or "Technology built for real operations",
			"description": doc.featured_solutions_description
			or "From production floors to retail stores and enterprise systems, our solutions help businesses improve accuracy, visibility and operational control.",
			"limit": int(doc.featured_solutions_limit or 4),
		}

	industries = None
	if doc.get("show_industries"):
		industries = {
			"eyebrow": doc.industries_eyebrow or "Industries",
			"title": doc.industries_title or "Industries we serve",
			"description": doc.industries_description
			or "From dairy and packaging to retail and logistics — technology mapped to the realities of each sector.",
			"limit": int(doc.industries_limit or 12),
		}

	extra_blocks = []
	for row in sorted_rows(doc.get("extra_blocks")):
		if not row.heading or not row.body:
			continue
		image = homepage_asset(row.image, row.image_alt or row.heading, 1600, 900) if row.image else None
		extra_blocks.append(
			{
				"id": f"extra-{row.idx}",
				"heading": row.heading,
				"body": row.body,
				"image": image,
				"linkLabel": row.link_label or "",
				"linkHref": row.link_href or "",
			}
		)

	return {
		"hero": hero,
		"why": why,
		"video": video,
		"stories": stories,
		"cta": cta,
		"divisions": divisions,
		"featuredSolutions": featured_solutions,
		"industries": industries,
		"extraBlocks": extra_blocks,
	}
