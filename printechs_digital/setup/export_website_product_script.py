# Copyright (c) 2026, Printechs and contributors
"""Dump a live Website Product into a fill-script PAGE dict.

  bench --site site1.local execute \\
    printechs_digital.setup.export_website_product_script.export_page \\
    --kwargs "{'slug': 'erpnext'}"

  bench --site site1.local execute \\
    printechs_digital.setup.export_website_product_script.export_page \\
    --kwargs "{'slug': 'modern-pos', 'path': '/tmp/fill_modern_pos_export.py'}"
"""

from pathlib import Path

import frappe
from frappe.utils import cstr


def _lines(value) -> str:
	return cstr(value)


def _row(doc_row, fields: list[str]) -> dict:
	data = {}
	for field in fields:
		data[field] = cstr(doc_row.get(field))
	if "sort_order" in data:
		data["sort_order"] = int(doc_row.get("sort_order") or 0)
	return data


def export_page(slug: str, path: str | None = None) -> str:
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if not name:
		frappe.throw(f"Website Product not found: {slug}")

	doc = frappe.get_doc("Website Product", name)
	parent_slug = None
	if doc.parent_software:
		parent_slug = frappe.db.get_value("Website Product", doc.parent_software, "slug")

	payload = {
		"website_product_name": doc.website_product_name,
		"display_name": doc.display_name,
		"slug": doc.slug,
		"product_type": doc.product_type,
		"division": doc.division,
		"brand": doc.brand,
		"category": doc.category,
		"subcategory": doc.subcategory,
		"category_label": doc.category_label,
		"parent_software": parent_slug,
		"published": int(doc.published or 0),
		"show_on_software_list": int(doc.show_on_software_list or 0),
		"show_on_products_list": int(doc.show_on_products_list or 0),
		"tagline": doc.tagline,
		"short_description": doc.short_description,
		"long_description": doc.long_description,
		"hero_image": doc.hero_image,
		"hero_image_alt": doc.hero_image_alt,
		"hero_trust_chips": doc.hero_trust_chips,
		"use_custom_hero_ctas": int(doc.use_custom_hero_ctas or 0),
		"hero_primary_cta_label": doc.hero_primary_cta_label,
		"hero_primary_cta_href": doc.hero_primary_cta_href,
		"hero_secondary_cta_label": doc.hero_secondary_cta_label,
		"hero_secondary_cta_href": doc.hero_secondary_cta_href,
		"show_demo_cta": int(doc.show_demo_cta or 0),
		"show_quote_in_hero": int(getattr(doc, "show_quote_in_hero", 0) or 0),
		"show_quote_in_product_tour": int(getattr(doc, "show_quote_in_product_tour", 0) or 0),
		"story_heading": doc.story_heading,
		"card_title": doc.card_title,
		"card_brand_label": doc.card_brand_label,
		"card_summary": doc.card_summary,
		"final_cta_heading": doc.final_cta_heading,
		"final_cta_description": doc.final_cta_description,
		"meta_title": doc.meta_title,
		"meta_description": doc.meta_description,
		"enable_product_tour": int(doc.enable_product_tour or 0),
		"product_tour_heading": doc.product_tour_heading,
		"product_tour_subheading": doc.product_tour_subheading,
		"benefits": [
			(row.icon, row.title, row.description)
			for row in doc.get("benefits") or []
		],
		"tour_sections": [
			_row(
				row,
				[
					"cta_placement",
					"image_side",
					"eyebrow",
					"heading",
					"body",
					"features",
					"image",
					"image_alt",
					"sort_order",
				],
			)
			for row in doc.get("tour_sections") or []
		],
		"content_sections": [
			_row(
				row,
				[
					"section_type",
					"image_side",
					"heading",
					"body",
					"image",
					"image_alt",
					"link_label",
					"link_href",
					"sort_order",
				],
			)
			for row in doc.get("content_sections") or []
		],
		"icon_specifications": [
			(row.icon, row.title, row.description)
			for row in doc.get("icon_specifications") or []
		],
		"support_items": [
			(row.icon, row.title, row.description)
			for row in doc.get("support_items") or []
		],
		"faq_items": [
			(row.question, row.answer)
			for row in doc.get("faq_items") or []
		],
	}

	body = (
		"# Auto-exported Website Product. Change slug before running or it overwrites the source.\n"
		"from printechs_digital.setup.fill_client_website_page import fill_client_website_page\n\n"
		f"PAGE = {repr(payload)}\n\n"
		"def execute():\n"
		"\treturn fill_client_website_page(PAGE)\n"
	)

	if path:
		out = Path(path)
		out.write_text(body, encoding="utf-8")
		return str(out)

	print(body)
	return body
