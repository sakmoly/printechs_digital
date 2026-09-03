# Copyright (c) 2026, Printechs and contributors
"""Point Kezojet Website Brand at the local logo file."""

from pathlib import Path

import frappe
from frappe.utils import get_files_path

LOGO = "/files/brand-kezojet.png"


def fix_kezojet_logo():
	path = Path(get_files_path("brand-kezojet.png", is_private=False))
	if not path.exists() or path.stat().st_size == 0:
		frappe.throw(f"Missing local logo at {path}")

	doc = frappe.get_doc("Website Brand", "kezojet")
	doc.logo = LOGO
	if doc.meta_title and "Keojet" in doc.meta_title:
		doc.meta_title = "Kezojet | Printechs Brands"
	doc.flags.ignore_permissions = True
	doc.save()

	if not frappe.db.exists(
		"File",
		{
			"file_url": LOGO,
			"attached_to_doctype": "Website Brand",
			"attached_to_name": "kezojet",
		},
	):
		file_doc = frappe.get_doc(
			{
				"doctype": "File",
				"file_name": "brand-kezojet.png",
				"file_url": LOGO,
				"attached_to_doctype": "Website Brand",
				"attached_to_name": "kezojet",
				"attached_to_field": "logo",
				"is_private": 0,
			}
		)
		file_doc.flags.ignore_permissions = True
		file_doc.insert()

	frappe.db.commit()
	return doc.logo
