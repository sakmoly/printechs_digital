# Copyright (c) 2026, Printechs and contributors

import frappe


def rename_website_products_to_item_code():
	"""Rename Website Product docs to their linked Item Code."""
	rows = frappe.get_all(
		"Website Product",
		fields=["name", "item", "slug"],
	)
	renamed = []
	for row in rows:
		new_name = row.item or row.slug
		if not new_name or new_name == row.name:
			continue
		if frappe.db.exists("Website Product", new_name):
			continue
		frappe.rename_doc("Website Product", row.name, new_name, force=True)
		renamed.append(f"{row.name} -> {new_name}")
	frappe.db.commit()
	return renamed
