# Copyright (c) 2026, Printechs and contributors
"""Create (or update) the internal website-launch Newsletter. Does not send."""

from pathlib import Path

import frappe

SUBJECT = "Our New Printechs Website Is Live – A New Digital Platform for Growth"
HTML_PATH = Path("/tmp/printechs-website-launch-newsletter.html")
EXISTING_NAME = "our-new-printechs-website-is-live-a-new-digital-platform-for-growth"


def create_newsletter():
	html = HTML_PATH.read_text(encoding="utf-8")
	name = EXISTING_NAME if frappe.db.exists("Newsletter", EXISTING_NAME) else None
	doc = frappe.get_doc("Newsletter", name) if name else frappe.new_doc("Newsletter")
	doc.subject = SUBJECT
	doc.content_type = "HTML"
	doc.message_html = html
	doc.sender_name = "Mohammed Sakeer"
	doc.sender_email = "marketing@printechs.com"
	doc.send_unsubscribe_link = 0
	doc.send_webview_link = 0
	doc.published = 0
	doc.email_sent = 0
	doc.schedule_sending = 0
	if not name:
		doc.append("email_group", {"email_group": "Printechs-Staff"})
	elif not any(row.email_group == "Printechs-Staff" for row in doc.email_group):
		doc.append("email_group", {"email_group": "Printechs-Staff"})
	doc.save(ignore_permissions=True)
	frappe.db.commit()
	print(doc.name)
	return doc.name
