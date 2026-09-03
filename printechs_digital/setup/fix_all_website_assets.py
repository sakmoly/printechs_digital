# Copyright (c) 2026, Printechs and contributors
"""Localize external website attachment URLs into /files/ for all masters."""

import frappe

from printechs_digital.utils.website_assets import is_local_asset, is_remote_url


def _save_if_changed(doc):
	doc.flags.ignore_permissions = True
	doc.save()
	return doc.name


def fix_all_website_assets():
	updated = []

	for name in frappe.get_all("Website Brand", pluck="name"):
		doc = frappe.get_doc("Website Brand", name)
		before = frappe.as_json(doc.as_dict())
		doc.run_method("before_validate")
		if frappe.as_json(doc.as_dict()) != before:
			updated.append(_save_if_changed(doc))

	for name in frappe.get_all("Website Industry", pluck="name"):
		doc = frappe.get_doc("Website Industry", name)
		before = frappe.as_json(doc.as_dict())
		doc.run_method("before_validate")
		if frappe.as_json(doc.as_dict()) != before:
			updated.append(_save_if_changed(doc))

	for name in frappe.get_all("Website Solution", pluck="name"):
		doc = frappe.get_doc("Website Solution", name)
		before = frappe.as_json(doc.as_dict())
		doc.run_method("before_validate")
		if frappe.as_json(doc.as_dict()) != before:
			updated.append(_save_if_changed(doc))

	for name in frappe.get_all("Website Product", pluck="name"):
		doc = frappe.get_doc("Website Product", name)
		before = frappe.as_json(doc.as_dict())
		doc.run_method("before_validate")
		if frappe.as_json(doc.as_dict()) != before:
			updated.append(_save_if_changed(doc))

	for name in frappe.get_all("Website Success Story", pluck="name"):
		doc = frappe.get_doc("Website Success Story", name)
		before = frappe.as_json(doc.as_dict())
		doc.run_method("before_validate")
		if frappe.as_json(doc.as_dict()) != before:
			updated.append(_save_if_changed(doc))

	doc = frappe.get_single("Website Homepage Settings")
	before = frappe.as_json(doc.as_dict())
	doc.run_method("before_validate")
	if frappe.as_json(doc.as_dict()) != before:
		updated.append(_save_if_changed(doc))

	frappe.db.commit()
	return updated


def list_external_assets():
	rows = []
	checks = [
		("Website Brand", "logo"),
		("Website Industry", "image"),
		("Website Solution", "image"),
		("Website Product", "hero_image"),
		("Website Product", "card_image"),
		("Website Product", "primary_download_file"),
		("Website Success Story", "hero_image"),
	]
	for doctype, field in checks:
		for row in frappe.get_all(doctype, fields=["name", field]):
			value = row.get(field)
			if value and is_remote_url(value) and not is_local_asset(value):
				rows.append({"doctype": doctype, "name": row.name, "field": field, "value": value})
	return rows
