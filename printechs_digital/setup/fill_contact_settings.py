# Copyright (c) 2026, Printechs and contributors
"""Seed Website Contact Settings with Riyadh, Jeddah and Dammam offices."""

import frappe

from printechs_digital.setup.fill_contact_specialist import SPECIALIST_DEFAULTS

OFFICES = [
	{
		"city": "Riyadh",
		"phone": "+966 11 206 2828 | +966 11 206 2929",
		"email": "info@printechs.com",
		"address": "Eastern Ring Branch Rd, Ar Rayyan, Riyadh 14211, KSA",
		"map_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5352.769116845449!2d46.76439432498705!3d24.709412486015196!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e2f01486d15003b%3A0x6e1aa5715ee39426!2sPrintechs%20Riyadh!5e0!3m2!1sen!2ssa!4v1668325833256!5m2!1sen!2ssa",
		"sort_order": 1,
	},
	{
		"city": "Jeddah",
		"phone": "+966 12 257 7799",
		"email": "info@printechs.com",
		"address": "AL HADA COMMERCIAL CENTER - Floor # 7 King Abdullah Street, with Touba Street Sharafiyah District P.O Box 8011, Jeddah 23216 KSA",
		"map_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3711.905713435053!2d39.1853851149408!3d21.51141278573892!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xacd84873cbbbd042!2zMjHCsDMwJzQxLjEiTiAzOcKwMTEnMTUuMyJF!5e0!3m2!1sen!2ssa!4v1668327573751!5m2!1sen!2ssa",
		"sort_order": 2,
	},
	{
		"city": "Dammam",
		"phone": "055 073 3441",
		"email": "info@printechs.com",
		"address": "7975 ابوعبد الله الهاشمي، Cordoba Commercial Center, Ground Floor Office# 101, behind Quick Pay, Dammam 34224, KSA",
		"map_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3574.793931855255!2d50.20025851453615!3d26.365526289779297!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e49ef40eb1d9935%3A0xf4e5b957aeb45986!2sPrintechs%20-%20Dammam!5e0!3m2!1sen!2ssa!4v1668327336833!5m2!1sen!2ssa",
		"sort_order": 3,
	},
]


def fill_contact_settings():
	if not frappe.db.exists("DocType", "Website Contact Settings"):
		frappe.throw("Website Contact Settings doctype is missing")

	doc = frappe.get_single("Website Contact Settings")
	if doc.get("offices"):
		return doc.name

	doc.published = 1
	doc.eyebrow = "Contact"
	doc.title = "Contact Printechs"
	doc.tagline = "Reach our teams in Riyadh, Jeddah and Dammam for sales, support and service across Saudi Arabia."
	doc.form_eyebrow = "Leave a message"
	doc.form_title = "Need Assistance?"
	doc.form_description = (
		"We are here to help and answer any question you might have. We look forward to hearing from you."
	)
	doc.meta_title = "Contact Printechs | Riyadh, Jeddah & Dammam"
	doc.meta_description = (
		"Contact Printechs offices in Riyadh, Jeddah and Dammam for industrial coding, "
		"retail technology and enterprise software solutions across Saudi Arabia."
	)
	for field, value in SPECIALIST_DEFAULTS.items():
		doc.set(field, value)
	doc.set("offices", OFFICES)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
