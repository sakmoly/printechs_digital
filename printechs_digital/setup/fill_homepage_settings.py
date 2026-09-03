# Copyright (c) 2026, Printechs and contributors
"""Seed Website Homepage Settings with the current Home page copy."""

from pathlib import Path
from shutil import copy2

import frappe

HERO_SOURCE = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/hero/home-hero.png")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")


def copy_hero() -> str:
	target = SITE_FILES / "home-hero.png"
	if HERO_SOURCE.exists() and not target.exists():
		copy2(HERO_SOURCE, target)
	if target.exists():
		return "/files/home-hero.png"
	return "/images/hero/home-hero.png"


def fill_homepage_settings():
	if not frappe.db.exists("DocType", "Website Homepage Settings"):
		frappe.throw("Website Homepage Settings doctype is missing")

	doc = frappe.get_single("Website Homepage Settings")
	doc.published = 1
	doc.hero_eyebrow = "Printechs"
	doc.hero_headline = "Technology That Moves Business Forward"
	doc.hero_supporting_text = (
		"Industrial coding, retail technology and enterprise software solutions "
		"for businesses across Saudi Arabia."
	)
	doc.hero_chips = "Industrial\nRetail\nSoftware\nSaudi Arabia"
	doc.hero_media_kind = "Image"
	doc.hero_image = copy_hero()
	doc.hero_image_alt = "Industrial coding, retail technology and enterprise software solutions"
	doc.hero_primary_label = "Explore Solutions"
	doc.hero_primary_href = "/solutions"
	doc.hero_secondary_label = "Talk to a Specialist"
	doc.hero_secondary_href = "/contact"

	doc.show_why = 1
	doc.why_eyebrow = "Why Printechs"
	doc.why_title = "A partner for technology that has to work"
	doc.why_description = (
		"Premium systems, practical delivery and long-term support — without marketplace clutter."
	)
	doc.set(
		"why_points",
		[
			{
				"title": "Industrial depth",
				"body": "Coding, marking and identification expertise built around production realities.",
				"sort_order": 1,
			},
			{
				"title": "Retail systems",
				"body": "Hardware and software that keep stores accurate, connected and serviceable.",
				"sort_order": 2,
			},
			{
				"title": "Enterprise software",
				"body": "POS, ERP, WMS, loyalty and compliance platforms with local delivery support.",
				"sort_order": 3,
			},
			{
				"title": "Saudi focus",
				"body": "Built for B2B customers operating across the Kingdom’s industrial and retail economy.",
				"sort_order": 4,
			},
		],
	)

	doc.show_video = 1
	doc.video_eyebrow = "Digital experience"
	doc.video_title = "See the Printechs digital experience"
	doc.video_summary = (
		"A short look at how industrial systems, retail technology and enterprise software come together."
	)
	doc.video_type = "YouTube"
	doc.video_source = "dQw4w9WgXcQ"
	doc.video_poster = "/images/placeholders/video-poster.svg"

	doc.show_stories = 1
	doc.stories_eyebrow = "Case studies"
	doc.stories_title = "Technology deployed where performance matters"
	doc.stories_description = "Selected project stories from industrial and retail environments."
	doc.stories_limit = 2

	doc.show_cta = 1
	doc.cta_title = "Talk to a Printechs specialist"
	doc.cta_description = (
		"Request a quote, book a demo, or plan a site visit with our team in Saudi Arabia."
	)
	doc.cta_primary_label = "Request Quote"
	doc.cta_primary_href = "/request-quote"
	doc.cta_secondary_label = "Request Demo"
	doc.cta_secondary_href = "/request-demo"

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
