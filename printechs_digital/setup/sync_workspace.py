# Copyright (c) 2026, Printechs and contributors
"""Sync Printechs Digital workspace links/shortcuts from app JSON."""

import json
from pathlib import Path

import frappe


def sync_printechs_digital_workspace():
	ws_path = (
		Path(frappe.get_app_path("printechs_digital"))
		/ "printechs_digital/workspace/printechs_digital/printechs_digital.json"
	)
	data = json.loads(ws_path.read_text())

	doc = frappe.get_doc("Workspace", "Printechs Digital") if frappe.db.exists(
		"Workspace", "Printechs Digital"
	) else frappe.new_doc("Workspace")

	skip = {"name", "doctype", "creation", "owner", "modified", "modified_by", "links", "shortcuts"}
	for key, value in data.items():
		if key in skip:
			continue
		setattr(doc, key, value)

	doc.set("links", data.get("links", []))
	doc.set("shortcuts", data.get("shortcuts", []))
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
