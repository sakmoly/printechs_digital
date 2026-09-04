# Copyright (c) 2026, Printechs and contributors

import frappe
from frappe.utils import cstr


def _split_choices(value: str | None) -> list[str]:
	if not value:
		return []
	return [line.strip() for line in cstr(value).splitlines() if line.strip()]


def map_quote_option(row) -> dict:
	option_type = "checkbox" if cstr(row.option_type) == "Checkbox" else "select"
	return {
		"id": cstr(row.name or row.label),
		"group": cstr(row.group_label or ""),
		"label": cstr(row.label),
		"type": option_type,
		"choices": _split_choices(row.choices),
		"required": bool(row.required),
	}


def _product_configuration(slug: str, configure_field: str, options_field: str) -> dict:
	name = frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Product not found", frappe.DoesNotExistError)

	doc = frappe.get_doc("Website Product", name)
	configure = bool(getattr(doc, configure_field, 0))
	rows = doc.get(options_field) if configure else []
	options = [
		map_quote_option(row)
		for row in sorted(rows or [], key=lambda item: (item.sort_order or 0, item.idx or 0))
		if row.label
	]

	return {
		"productSlug": doc.slug,
		"product": doc.display_name,
		"code": doc.item_code,
		"brand": doc.brand_name or doc.brand,
		"category": doc.category,
		"sourceUrl": doc.canonical_path or f"/products/{doc.slug}",
		"configureOnQuote": configure,
		"generateLead": bool(getattr(doc, "generate_lead", 0)),
		"quoteOptions": options,
	}


@frappe.whitelist(allow_guest=True)
def get_quote_configuration(slug: str):
	"""Return quote configuration questions when the Website Product flag is on."""
	return _product_configuration(slug, "configure_on_quote", "quote_options")


@frappe.whitelist(allow_guest=True)
def get_demo_configuration(slug: str):
	"""Return demo questionnaire when Configure on Demo is enabled."""
	return _product_configuration(slug, "configure_on_demo", "demo_options")
