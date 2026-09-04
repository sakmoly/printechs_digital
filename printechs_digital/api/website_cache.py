# Copyright (c) 2026, Printechs and contributors

import frappe
from frappe.utils.caching import redis_cache

from printechs_digital.api.mappers.brand_mapper import map_website_brand
from printechs_digital.api.mappers.event_mapper import map_event_card
from printechs_digital.api.mappers.homepage_mapper import map_homepage
from printechs_digital.api.mappers.industry_mapper import map_industry
from printechs_digital.api.mappers.product_mapper import map_catalog_product
from printechs_digital.api.mappers.solution_mapper import map_featured_solution
from printechs_digital.api.mappers.story_mapper import map_success_story_card

WEBSITE_CACHE_TTL = 300


def clear_website_api_cache():
	"""Clear Redis-backed website API caches after Desk content changes."""
	for func in (
		_cached_list_brands,
		_cached_featured_products,
		_cached_featured_software,
		_cached_featured_solutions,
		_cached_home_industries,
		_cached_featured_success_stories,
		_cached_homepage,
		_cached_homepage_bundle,
	):
		func.clear_cache()


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_list_brands(limit: int = 50):
	rows = frappe.get_all(
		"Website Brand",
		filters={"published": 1},
		fields=["name"],
		order_by="sort_order asc, display_name asc",
		limit_page_length=limit,
	)
	return [map_website_brand(frappe.get_doc("Website Brand", row.name)) for row in rows]


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_featured_products(limit: int = 4):
	rows = frappe.get_all(
		"Website Product",
		filters={"published": 1, "featured": 1},
		fields=["name"],
		order_by="featured_sort_order asc, modified desc",
		limit_page_length=limit,
	)
	return [map_catalog_product(frappe.get_doc("Website Product", row.name)) for row in rows]


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_featured_software(limit: int = 6):
	rows = frappe.get_all(
		"Website Product",
		filters={"published": 1, "show_on_software_list": 1},
		fields=["name"],
		order_by="modified desc",
		limit_page_length=limit,
	)
	return [map_catalog_product(frappe.get_doc("Website Product", row.name)) for row in rows]


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_featured_solutions(limit: int = 4):
	if not frappe.db.exists("DocType", "Website Solution"):
		return []
	rows = frappe.get_all(
		"Website Solution",
		filters={"published": 1, "featured": 1},
		fields=["name"],
		order_by="sort_order asc, modified desc",
		limit_page_length=limit,
	)
	return [map_featured_solution(frappe.get_doc("Website Solution", row.name)) for row in rows]


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_home_industries(limit: int = 12):
	if not frappe.db.exists("DocType", "Website Industry"):
		return []
	rows = frappe.get_all(
		"Website Industry",
		filters={"published": 1, "show_on_home": 1},
		fields=["name"],
		order_by="sort_order asc, industry_name asc",
		limit_page_length=limit,
	)
	return [map_industry(frappe.get_doc("Website Industry", row.name)) for row in rows]


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_featured_success_stories(limit: int = 2):
	rows = frappe.get_all(
		"Website Success Story",
		filters={"published": 1},
		fields=["name"],
		order_by="featured desc, sort_order asc, modified desc",
		limit_page_length=limit,
	)
	return [map_success_story_card(frappe.get_doc("Website Success Story", row.name)) for row in rows]


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_homepage():
	if not frappe.db.exists("DocType", "Website Homepage Settings"):
		return None
	try:
		doc = frappe.get_single("Website Homepage Settings")
	except Exception:
		return None
	return map_homepage(doc)


def _homepage_limits(homepage: dict | None):
	defaults = {
		"products": 4,
		"software": 6,
		"solutions": 4,
		"industries": 12,
		"stories": 2,
	}
	if not homepage:
		return defaults

	if homepage.get("featuredSolutions") is None:
		defaults["solutions"] = 0
	elif homepage.get("featuredSolutions"):
		defaults["solutions"] = int(homepage["featuredSolutions"].get("limit") or 4)

	if homepage.get("industries") is None:
		defaults["industries"] = 0
	elif homepage.get("industries"):
		defaults["industries"] = int(homepage["industries"].get("limit") or 12)

	if homepage.get("stories") is None:
		defaults["stories"] = 0
	elif homepage.get("stories"):
		defaults["stories"] = int(homepage["stories"].get("limit") or 2)

	return defaults


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_homepage_bundle():
	homepage = _cached_homepage()
	limits = _homepage_limits(homepage)

	return {
		"homepage": homepage,
		"featuredProducts": _cached_featured_products(limits["products"]),
		"featuredSoftware": _cached_featured_software(limits["software"]),
		"brands": _cached_list_brands(50),
		"featuredSolutions": _cached_featured_solutions(limits["solutions"])
		if limits["solutions"]
		else [],
		"industries": _cached_home_industries(limits["industries"]) if limits["industries"] else [],
		"successStories": _cached_featured_success_stories(limits["stories"])
		if limits["stories"]
		else [],
	}


@redis_cache(ttl=WEBSITE_CACHE_TTL)
def _cached_list_event_albums(event_type: str | None = None, limit: int = 50):
	if not frappe.db.exists("DocType", "Website Event Album"):
		return {"albums": [], "eventTypes": []}

	filters = {"published": 1}
	if event_type:
		filters["event_type"] = event_type

	rows = frappe.get_all(
		"Website Event Album",
		filters=filters,
		fields=["name"],
		order_by="featured desc, event_date desc, sort_order asc, modified desc",
		limit_page_length=limit,
	)
	albums = [map_event_card(frappe.get_doc("Website Event Album", row.name)) for row in rows]
	event_types = frappe.get_all(
		"Website Event Album",
		filters={"published": 1},
		pluck="event_type",
		distinct=True,
		order_by="event_type asc",
	)
	return {"albums": albums, "eventTypes": [value for value in event_types if value]}
