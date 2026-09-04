# Copyright (c) 2026, Printechs and contributors

import frappe

from printechs_digital.api.mappers.about_mapper import map_about_page
from printechs_digital.api.mappers.contact_mapper import map_contact_page
from printechs_digital.api.mappers.brand_mapper import map_website_brand
from printechs_digital.api.mappers.homepage_mapper import map_homepage
from printechs_digital.api.mappers.industry_mapper import map_industry
from printechs_digital.api.mappers.product_mapper import map_catalog_product, map_resolved_product
from printechs_digital.api.mappers.solution_mapper import map_featured_solution, map_solution
from printechs_digital.api.mappers.event_mapper import map_event_album, map_event_card
from printechs_digital.api.mappers.story_mapper import map_success_story, map_success_story_card
from printechs_digital.api.website_cache import (
	_cached_featured_products,
	_cached_featured_software,
	_cached_featured_solutions,
	_cached_featured_success_stories,
	_cached_home_industries,
	_cached_homepage,
	_cached_homepage_bundle,
	_cached_list_brands,
	_cached_list_event_albums,
)


@frappe.whitelist(allow_guest=True)
def get_product(slug: str):
	"""Return published Website Product as frontend ProductPageContent."""
	name = frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Product not found", frappe.DoesNotExistError)

	doc = frappe.get_doc("Website Product", name)
	return map_resolved_product(doc)


@frappe.whitelist(allow_guest=True)
def list_products(list: str = "products", division: str | None = None, brand: str | None = None, limit: int = 100):
	"""Return catalogue cards for products or software listings."""
	filters = {"published": 1}

	if list == "software":
		filters["show_on_software_list"] = 1
	else:
		filters["show_on_products_list"] = 1

	if division:
		filters["division"] = division

	rows = frappe.get_all(
		"Website Product",
		filters=filters,
		fields=["name"],
		order_by="modified desc",
		limit_page_length=limit,
	)

	products = [map_catalog_product(frappe.get_doc("Website Product", row.name)) for row in rows]
	if brand:
		brand_key = brand.strip().lower()
		products = [
			product
			for product in products
			if brand_key in (product.get("brand") or "").lower()
		]
	return products


@frappe.whitelist(allow_guest=True)
def get_featured_products(limit: int = 4):
	return _cached_featured_products(limit)


@frappe.whitelist(allow_guest=True)
def get_product_slugs():
	rows = frappe.get_all(
		"Website Product",
		filters={"published": 1},
		pluck="slug",
		order_by="modified desc",
	)
	return rows


@frappe.whitelist(allow_guest=True)
def get_quote_context(slug: str):
	name = frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Product not found", frappe.DoesNotExistError)

	doc = frappe.get_doc("Website Product", name)
	canonical_path = doc.canonical_path or f"/products/{doc.slug}"

	return {
		"productSlug": doc.slug,
		"product": doc.display_name,
		"code": doc.item_code,
		"brand": doc.brand_name or doc.brand,
		"category": doc.category,
		"sourceUrl": canonical_path,
	}


@frappe.whitelist(allow_guest=True)
def list_brands(limit: int = 50):
	return _cached_list_brands(limit)


@frappe.whitelist(allow_guest=True)
def get_brand(slug: str):
	name = frappe.db.get_value("Website Brand", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Brand not found", frappe.DoesNotExistError)

	return map_website_brand(frappe.get_doc("Website Brand", name))


@frappe.whitelist(allow_guest=True)
def get_homepage():
	return _cached_homepage()


@frappe.whitelist(allow_guest=True)
def get_homepage_bundle():
	"""Single payload for the marketing homepage (settings + featured sections)."""
	return _cached_homepage_bundle()


@frappe.whitelist(allow_guest=True)
def get_about_page():
	if not frappe.db.exists("DocType", "Website About Settings"):
		return None
	try:
		doc = frappe.get_single("Website About Settings")
	except Exception:
		return None
	return map_about_page(doc)


@frappe.whitelist(allow_guest=True)
def get_contact_page():
	if not frappe.db.exists("DocType", "Website Contact Settings"):
		return None
	try:
		doc = frappe.get_single("Website Contact Settings")
	except Exception:
		return None
	return map_contact_page(doc)


@frappe.whitelist(allow_guest=True)
def get_brand_slugs():
	return frappe.get_all(
		"Website Brand",
		filters={"published": 1},
		pluck="slug",
		order_by="sort_order asc, display_name asc",
	)


def _published_story_filters(product: str | None = None, brand: str | None = None, industry: str | None = None):
	filters = {"published": 1}
	if product:
		filters["product_slug"] = product
	if brand:
		filters["brand_slug"] = brand
	if industry:
		from printechs_digital.printechs_digital.doctype.website_success_story.website_success_story import (
			industry_slug,
		)

		filters["industry_slug"] = industry_slug(industry)
	return filters


@frappe.whitelist(allow_guest=True)
def list_success_stories(
	product: str | None = None,
	brand: str | None = None,
	industry: str | None = None,
	limit: int = 50,
):
	rows = frappe.get_all(
		"Website Success Story",
		filters=_published_story_filters(product, brand, industry),
		fields=["name"],
		order_by="featured desc, sort_order asc, modified desc",
		limit_page_length=limit,
	)
	stories = [map_success_story_card(frappe.get_doc("Website Success Story", row.name)) for row in rows]

	facet_rows = frappe.get_all(
		"Website Success Story",
		filters={"published": 1},
		fields=["brand", "brand_slug", "industry", "industry_slug"],
	)
	brands = []
	seen_brands = set()
	industries = []
	seen_industries = set()
	for row in facet_rows:
		if row.brand_slug and row.brand_slug not in seen_brands:
			seen_brands.add(row.brand_slug)
			brands.append({"slug": row.brand_slug, "name": row.brand or row.brand_slug})
		if row.industry_slug and row.industry_slug not in seen_industries:
			seen_industries.add(row.industry_slug)
			industries.append({"slug": row.industry_slug, "name": row.industry or row.industry_slug})

	return {"stories": stories, "brands": brands, "industries": industries}


@frappe.whitelist(allow_guest=True)
def get_success_story(slug: str):
	name = frappe.db.get_value("Website Success Story", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Success story not found", frappe.DoesNotExistError)

	doc = frappe.get_doc("Website Success Story", name)
	story = map_success_story(doc)

	related_filters = {"published": 1, "name": ["!=", doc.name]}
	or_filters = []
	if doc.brand_slug:
		or_filters.append(["brand_slug", "=", doc.brand_slug])
	if doc.industry_slug:
		or_filters.append(["industry_slug", "=", doc.industry_slug])
	related_args = {
		"filters": related_filters,
		"fields": ["name"],
		"order_by": "featured desc, sort_order asc, modified desc",
		"limit_page_length": 3,
	}
	if or_filters:
		related_args["or_filters"] = or_filters
	related = frappe.get_all("Website Success Story", **related_args)
	story["related"] = [
		map_success_story_card(frappe.get_doc("Website Success Story", row.name)) for row in related
	]
	return story


@frappe.whitelist(allow_guest=True)
def get_featured_success_stories(limit: int = 2):
	return _cached_featured_success_stories(limit)


@frappe.whitelist(allow_guest=True)
def get_success_story_slugs():
	return frappe.get_all(
		"Website Success Story",
		filters={"published": 1},
		pluck="slug",
		order_by="sort_order asc, modified desc",
	)


@frappe.whitelist(allow_guest=True)
def list_event_albums(event_type: str | None = None, limit: int = 50):
	return _cached_list_event_albums(event_type, limit)


@frappe.whitelist(allow_guest=True)
def get_event_album(slug: str):
	if not frappe.db.exists("DocType", "Website Event Album"):
		frappe.throw("Event album not found", frappe.DoesNotExistError)

	name = frappe.db.get_value("Website Event Album", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Event album not found", frappe.DoesNotExistError)

	return map_event_album(frappe.get_doc("Website Event Album", name))


@frappe.whitelist(allow_guest=True)
def get_event_album_slugs():
	if not frappe.db.exists("DocType", "Website Event Album"):
		return []

	return frappe.get_all(
		"Website Event Album",
		filters={"published": 1},
		pluck="slug",
		order_by="event_date desc, sort_order asc",
	)


@frappe.whitelist(allow_guest=True)
def list_industries(home: int = 0, limit: int = 50):
	if int(home or 0):
		return _cached_home_industries(limit)

	if not frappe.db.exists("DocType", "Website Industry"):
		return []

	rows = frappe.get_all(
		"Website Industry",
		filters={"published": 1},
		fields=["name"],
		order_by="sort_order asc, industry_name asc",
		limit_page_length=limit,
	)
	return [map_industry(frappe.get_doc("Website Industry", row.name)) for row in rows]


@frappe.whitelist(allow_guest=True)
def get_industry(slug: str):
	name = frappe.db.get_value("Website Industry", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Industry not found", frappe.DoesNotExistError)
	return map_industry(frappe.get_doc("Website Industry", name))


@frappe.whitelist(allow_guest=True)
def get_industry_slugs():
	if not frappe.db.exists("DocType", "Website Industry"):
		return []
	return frappe.get_all(
		"Website Industry",
		filters={"published": 1},
		pluck="slug",
		order_by="sort_order asc, industry_name asc",
	)


@frappe.whitelist(allow_guest=True)
def list_solutions(limit: int = 50):
	if not frappe.db.exists("DocType", "Website Solution"):
		return []
	rows = frappe.get_all(
		"Website Solution",
		filters={"published": 1, "show_on_list": 1},
		fields=["name"],
		order_by="sort_order asc, solution_name asc",
		limit_page_length=limit,
	)
	return [map_solution(frappe.get_doc("Website Solution", row.name)) for row in rows]


@frappe.whitelist(allow_guest=True)
def get_featured_solutions(limit: int = 4):
	return _cached_featured_solutions(limit)


@frappe.whitelist(allow_guest=True)
def get_solution(slug: str):
	name = frappe.db.get_value("Website Solution", {"slug": slug, "published": 1}, "name")
	if not name:
		frappe.throw("Solution not found", frappe.DoesNotExistError)
	return map_solution(frappe.get_doc("Website Solution", name))


@frappe.whitelist(allow_guest=True)
def get_solution_slugs():
	if not frappe.db.exists("DocType", "Website Solution"):
		return []
	return frappe.get_all(
		"Website Solution",
		filters={"published": 1},
		pluck="slug",
		order_by="sort_order asc, solution_name asc",
	)
