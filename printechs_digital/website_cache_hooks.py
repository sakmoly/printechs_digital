# Copyright (c) 2026, Printechs and contributors

import frappe

WEBSITE_CONTENT_DOCTYPES = (
	"Website Product",
	"Website Brand",
	"Website Solution",
	"Website Industry",
	"Website Success Story",
	"Website Event Album",
	"Website Homepage Settings",
	"Website About Settings",
	"Website Contact Settings",
)


def clear_website_cache(doc, method=None):
	from printechs_digital.api.website_cache import clear_website_api_cache

	clear_website_api_cache()
