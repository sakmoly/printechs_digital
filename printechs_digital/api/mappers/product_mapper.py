# Copyright (c) 2026, Printechs and contributors

import re

import frappe
from frappe.utils import cstr, get_url, strip_html

from printechs_digital.constants.product_page_sections import DEFAULT_PAGE_SECTION_ORDER

PRODUCT_TYPE_MAP = {
	"Industrial": "industrial",
	"Retail Hardware": "retail_hardware",
	"Software": "software",
	"Generic": "generic",
}

DIVISION_MAP = {
	"Industrial": "industrial",
	"Retail": "retail",
	"Software": "retail",
}

DOWNLOAD_TYPE_MAP = {
	"Datasheet": "datasheet",
	"Brochure": "brochure",
	"Manual": "manual",
	"Other": "other",
}


def slugify(value: str) -> str:
	value = cstr(value).lower().strip()
	value = re.sub(r"[^\w\s-]", "", value)
	value = re.sub(r"[\s_]+", "-", value)
	value = re.sub(r"-+", "-", value)
	return value.strip("-")


def absolute_url(path: str | None) -> str | None:
	if not path:
		return None
	if path.startswith(("http://", "https://")):
		return path.replace("http://", "https://", 1)
	url = get_url(path)
	return url.replace("http://", "https://", 1) if url else url


def media_asset(path: str | None, alt: str, width: int = 1200, height: int = 1200) -> dict | None:
	src = absolute_url(path)
	if not src:
		return None
	return {"src": src, "alt": alt or "", "width": width, "height": height}


def html_to_paragraphs(html: str | None) -> str:
	if not html:
		return ""
	text = cstr(html)
	text = re.sub(r"</p>\s*", "\n\n", text, flags=re.IGNORECASE)
	text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
	return strip_html(text).strip()


def split_lines(value: str | None) -> list[str]:
	if not value:
		return []
	return [line.strip() for line in cstr(value).splitlines() if line.strip()]


def map_page_section_order(doc) -> list[str]:
	rows = sorted_rows(doc.get("page_section_order"))
	if rows:
		order = [cstr(row.section).strip() for row in rows if cstr(row.section).strip()]
		if order:
			return order
	return list(DEFAULT_PAGE_SECTION_ORDER)


def sorted_rows(rows: list | None, field: str = "sort_order") -> list:
	if not rows:
		return []
	return sorted(rows, key=lambda row: (row.get(field) or 0, row.idx or 0))


def normalize_icon(icon: str | None) -> str | None:
	if not icon:
		return None
	return cstr(icon).strip().lower() or None


def map_product_type(product_type: str | None) -> str:
	return PRODUCT_TYPE_MAP.get(product_type or "", "generic")


def map_division(division: str | None) -> str:
	return DIVISION_MAP.get(division or "", "industrial")


def breadcrumb_root(product_type: str | None) -> dict:
	if product_type == "Software":
		return {"label": "Software", "href": "/software"}
	return {"label": "Products", "href": "/products"}


def get_website_brand_row(brand_link: str | None, brand_name: str | None) -> dict | None:
	fields = ["name", "slug", "display_name", "logo"]
	if brand_link:
		row = frappe.db.get_value(
			"Website Brand",
			{"brand": brand_link, "published": 1},
			fields,
			as_dict=True,
		)
		if row:
			return row

	slug = slugify(brand_name or brand_link or "")
	if not slug:
		return None

	return frappe.db.get_value(
		"Website Brand",
		{"slug": slug, "published": 1},
		fields,
		as_dict=True,
	)


def get_brand_payload(brand_link: str | None, brand_name: str | None) -> dict | None:
	name = brand_name or brand_link
	if not name:
		return None

	website_brand = get_website_brand_row(brand_link, brand_name)
	logo_src = website_brand.logo if website_brand else None
	display_name = (website_brand.display_name if website_brand else None) or name
	slug = (website_brand.slug if website_brand else None) or slugify(name)

	if not logo_src and brand_link and frappe.db.exists("Brand", brand_link):
		logo_src = frappe.db.get_value("Brand", brand_link, "image")

	if not logo_src:
		return None

	return {
		"slug": slug,
		"name": display_name,
		"logo": media_asset(logo_src, f"{display_name} logo", 400, 160),
	}


def get_product_reference(linked_name: str | None, overrides: dict | None = None) -> dict | None:
	if not linked_name or not frappe.db.exists("Website Product", linked_name):
		return None

	linked = frappe.get_doc("Website Product", linked_name)
	if not linked.published:
		return None

	overrides = overrides or {}
	base = "/software" if linked.product_type == "Software" else "/products"
	image_path = linked.card_image or linked.hero_image
	image_alt = linked.hero_image_alt or linked.display_name

	return {
		"slug": linked.slug,
		"name": overrides.get("name") or linked.card_title or linked.display_name,
		"summary": overrides.get("summary") or linked.card_summary or linked.short_description,
		"href": f"{base}/{linked.slug}",
		"image": media_asset(image_path, image_alt),
	}


def map_reference_row(row, image_width: int = 1200, image_height: int = 1200) -> dict | None:
	overrides = {
		"name": row.get("display_name_override"),
		"summary": row.get("summary_override"),
	}
	linked = get_product_reference(row.get("related_website_product"), overrides)
	if linked:
		if row.get("href"):
			linked["href"] = row.href
		if row.get("image"):
			linked["image"] = media_asset(
				row.image, linked["name"], image_width, image_height
			)
		return linked

	name = cstr(row.get("display_name_override")).strip()
	if not name:
		return None

	image = media_asset(row.get("image"), name, image_width, image_height)
	return {
		"slug": slugify(name),
		"name": name,
		"summary": cstr(row.get("summary_override")).strip() or None,
		"href": row.get("href") or "#",
		"image": image,
	}


def map_capability_modules(rows: list | None) -> list:
	modules = []
	for row in sorted_rows(rows):
		title = cstr(row.module_title).strip()
		item_text = cstr(row.item_text).strip()
		if not title or not item_text:
			continue
		if not modules or modules[-1]["title"] != title:
			modules.append({
				"icon": normalize_icon(row.icon),
				"title": title,
				"items": [],
			})
		elif row.icon and not modules[-1].get("icon"):
			modules[-1]["icon"] = normalize_icon(row.icon)
		modules[-1]["items"].append(item_text)
	return modules


def map_website_product(doc) -> dict:
	product_type = map_product_type(doc.product_type)
	brand_name = doc.brand_name or doc.brand
	hero_w, hero_h = (1600, 1000) if product_type == "software" else (1200, 1200)
	hero_image = media_asset(doc.hero_image, doc.hero_image_alt or doc.display_name, hero_w, hero_h)
	card_image = media_asset(
		doc.card_image or doc.hero_image,
		doc.hero_image_alt or doc.display_name,
		hero_w,
		hero_h,
	)

	primary_download = None
	if doc.primary_download_file:
		primary_download = {
			"label": doc.primary_download_label or "Download",
			"href": absolute_url(doc.primary_download_file),
			"type": "datasheet",
		}

	benefits = [
		{
			"icon": normalize_icon(row.icon),
			"title": row.title,
			"description": row.description,
		}
		for row in sorted_rows(doc.benefits)
	]

	visual_story_items = [
		{
			"id": slugify(row.label) or f"story-{idx + 1}",
			"label": row.label,
			"image": media_asset(row.image, row.image_alt or row.label, hero_w, hero_h),
			"caption": row.caption or None,
		}
		for idx, row in enumerate(sorted_rows(doc.visual_story_items))
		if row.image
	]

	icon_specifications = [
		{
			"icon": normalize_icon(row.icon),
			"title": row.title,
			"description": row.description,
		}
		for row in sorted_rows(doc.icon_specifications)
	]

	full_specifications = []
	for row in sorted_rows(doc.full_specifications):
		if not row.label:
			continue
		group_title = row.group_title or "Specifications"
		if not full_specifications or full_specifications[-1]["title"] != group_title:
			full_specifications.append({"title": group_title, "items": []})
		full_specifications[-1]["items"].append({"label": row.label, "value": row.value})

	application_cards = [
		{
			"title": row.title,
			"description": row.description,
			"image": media_asset(row.image, row.image_alt or row.title, 1200, 800),
			"href": f"/industries/{row.industry_link}" if row.industry_link else None,
		}
		for row in sorted_rows(doc.applications)
		if row.image
	]

	industry_slugs = [
		row.industry_link for row in sorted_rows(doc.applications) if row.industry_link
	]

	ecosystem_items = [
		ref
		for row in sorted_rows(doc.ecosystem_items)
		if (ref := map_reference_row(row))
	]

	related_w, related_h = (1600, 1000) if product_type == "software" else (1200, 1200)
	related_products = [
		ref
		for row in sorted_rows(doc.related_products)
		if (ref := map_reference_row(row, related_w, related_h))
	]

	capability_modules = map_capability_modules(doc.get("capability_items"))

	support_service_items = [
		{
			"icon": normalize_icon(row.icon),
			"title": row.title,
			"description": row.description,
		}
		for row in sorted_rows(doc.support_items)
	]

	downloads = [
		{
			"label": row.label,
			"href": absolute_url(row.file),
			"type": DOWNLOAD_TYPE_MAP.get(row.download_type or "", "other"),
		}
		for row in sorted_rows(doc.downloads)
		if row.file
	]

	package_contents = [row.item_description for row in sorted_rows(doc.package_contents)]

	content_sections = []
	for row in sorted_rows(doc.get("content_sections")):
		heading = cstr(row.heading).strip()
		body = html_to_paragraphs(row.body)
		if not heading or not body:
			continue
		section = {
			"heading": heading,
			"body": body,
			"image": media_asset(row.image, row.image_alt or heading, 1600, 1000),
			"videoUrl": cstr(row.video_url).strip() or None,
		}
		if row.link_label and row.link_href:
			section["link"] = {"label": row.link_label, "href": row.link_href}
		content_sections.append(section)

	product_tour = None
	if getattr(doc, "enable_product_tour", 0):
		tour_sections = []
		for idx, row in enumerate(sorted_rows(doc.get("tour_sections"))):
			heading = cstr(row.heading).strip()
			body = cstr(row.body).strip()
			if not heading or not body:
				continue
			eyebrow = cstr(row.eyebrow).strip() or heading
			tour_sections.append(
				{
					"id": slugify(eyebrow) or f"tour-{idx + 1}",
					"eyebrow": eyebrow,
					"title": heading,
					"description": body,
					"features": split_lines(getattr(row, "features", None)),
					"image": media_asset(
						row.image,
						row.image_alt or heading,
						1600,
						1000,
					),
				}
			)
		if tour_sections:
			product_tour = {
				"heading": cstr(doc.product_tour_heading).strip()
				or doc.visual_story_heading
				or "See it in action",
				"subheading": cstr(doc.product_tour_subheading).strip() or None,
				"sections": tour_sections,
			}

	faqs = [
		{"question": row.question, "answer": html_to_paragraphs(row.answer)}
		for row in sorted_rows(doc.get("faq_items"))
		if row.question and row.answer
	]

	canonical_path = doc.canonical_path or (
		f"/software/{doc.slug}" if doc.product_type == "Software" else f"/products/{doc.slug}"
	)

	page = {
		"slug": doc.slug,
		"productType": product_type,
		"displayName": doc.display_name,
		"brand": brand_name or "",
		"brandSlug": slugify(brand_name) if brand_name else None,
		"category": doc.category,
		"subcategory": doc.subcategory or None,
		"categoryLabel": doc.category_label or None,
		"tagline": doc.tagline or None,
		"shortDescription": doc.short_description,
		"longDescription": html_to_paragraphs(doc.long_description),
		"heroImage": hero_image
		or {
			"src": absolute_url("/files/placeholder-product.png"),
			"alt": doc.display_name,
			"width": 1200,
			"height": 1200,
		},
		"heroTrustChips": split_lines(doc.hero_trust_chips) or None,
		"primaryDownload": primary_download,
		"showDemoCta": bool(doc.show_demo_cta),
		"keyValueCards": benefits or None,
		"visualStory": {
			"heading": doc.visual_story_heading or "See it in action",
			"items": visual_story_items,
		}
		if visual_story_items
		else None,
		"storyHeading": doc.story_heading or None,
		"features": [],
		"iconSpecifications": icon_specifications or None,
		"fullSpecifications": full_specifications or None,
		"collapsibleFullSpecs": bool(doc.collapsible_full_specs),
		"applicationCards": application_cards or None,
		"industrySlugs": industry_slugs or None,
		"capabilityModules": capability_modules or None,
		"ecosystemItems": ecosystem_items or None,
		"supportServiceItems": support_service_items or None,
		"downloads": downloads or None,
		"packageContents": package_contents or None,
		"contentSections": content_sections or None,
		"productTour": product_tour,
		"pageSectionOrder": map_page_section_order(doc),
		"faqs": faqs or None,
		"relatedProducts": related_products or None,
		"finalCta": {
			"heading": doc.final_cta_heading or f"Ready to deploy {doc.display_name}?",
			"description": doc.final_cta_description
			or "Contact Printechs for pricing, installation, and support across Saudi Arabia.",
		},
		"seo": {
			"title": doc.meta_title or f"{doc.display_name} | Printechs",
			"description": doc.meta_description or doc.short_description,
			"canonicalPath": canonical_path,
			"indexPage": bool(doc.index_page),
		},
		"canonicalPath": canonical_path,
		"breadcrumbRoot": breadcrumb_root(doc.product_type),
	}

	if doc.show_item_code_on_website and doc.item_code:
		page["itemCode"] = doc.item_code

	return page


def map_catalog_product(doc) -> dict:
	brand_name = doc.brand_name or doc.brand
	image_path = doc.card_image or doc.hero_image
	canonical_path = doc.canonical_path or (
		f"/software/{doc.slug}" if doc.product_type == "Software" else f"/products/{doc.slug}"
	)

	return {
		"id": f"erp-{doc.slug}",
		"slug": doc.slug,
		"name": doc.display_name,
		"brand": doc.card_brand_label or brand_name or "",
		"summary": doc.card_summary or doc.short_description,
		"category": doc.category,
		"division": map_division(doc.division),
		"image": media_asset(image_path, doc.hero_image_alt or doc.display_name)
		or {
			"src": "/images/placeholders/product.svg",
			"alt": doc.display_name,
			"width": 1200,
			"height": 1200,
		},
		"seo": {
			"title": doc.meta_title or f"{doc.display_name} | Printechs",
			"description": doc.meta_description or doc.short_description,
			"canonicalPath": canonical_path,
		},
	}


def map_resolved_product(doc) -> dict:
	page = map_website_product(doc)
	brand = get_brand_payload(doc.brand, doc.brand_name)
	has_success_stories = bool(
		frappe.db.exists("DocType", "Website Success Story")
		and frappe.db.exists("Website Success Story", {"product_slug": doc.slug, "published": 1})
	)
	return {
		"page": page,
		"brand": brand,
		"linkedIndustries": [],
		"hasSuccessStories": has_success_stories,
	}
