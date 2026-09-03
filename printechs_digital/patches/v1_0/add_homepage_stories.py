# Copyright (c) 2026, Printechs and contributors


def execute():
	import frappe

	if not frappe.db.exists("DocType", "Website Homepage Settings"):
		return

	doc = frappe.get_single("Website Homepage Settings")
	if doc.get("stories_title"):
		return

	doc.show_stories = 1
	doc.stories_eyebrow = "Case studies"
	doc.stories_title = "Technology deployed where performance matters"
	doc.stories_description = "Selected project stories from industrial and retail environments."
	doc.stories_limit = 2
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
