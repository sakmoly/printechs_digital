# Copyright (c) 2026, Printechs and contributors


def execute():
	import frappe

	if not frappe.db.exists("DocType", "Website About Settings"):
		return

	doc = frappe.get_single("Website About Settings")
	if doc.get("company_profile_file"):
		return

	doc.company_profile_file = "/files/Company_Profile.pdf"
	doc.company_profile_label = doc.company_profile_label or "Download Profile"
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
