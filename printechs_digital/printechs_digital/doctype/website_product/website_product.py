# Copyright (c) 2026, Printechs and contributors

import re

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cstr, strip_html

from printechs_digital.utils.website_assets import (
	localize_child_table,
	localize_doc_fields,
	validate_child_table,
	validate_doc_fields,
)


def slugify(value: str) -> str:
	value = cstr(value).lower().strip()
	value = re.sub(r"[^\w\s-]", "", value)
	value = re.sub(r"[\s_]+", "-", value)
	value = re.sub(r"-+", "-", value)
	return value.strip("-")


class WebsiteProduct(Document):
	def autoname(self):
		if self.item:
			self.name = self.item
		elif self.slug:
			self.name = slugify(self.slug)
		else:
			frappe.throw(_("Item Code or Slug is required to name this Website Product"))

	def before_validate(self):
		if not self.hero_image_alt:
			self.hero_image_alt = self.display_name or self.website_product_name or self.item
		if not self.hero_image and self.item:
			self.hero_image = frappe.db.get_value("Item", self.item, "image")

		slug = self.slug or slugify(self.display_name or self.website_product_name or "product")
		localize_doc_fields(
			self,
			[
				("hero_image", f"product-{slug}-hero"),
				("card_image", f"product-{slug}-card"),
				("primary_download_file", f"product-{slug}-download"),
			],
		)
		localize_child_table(
			self,
			"applications",
			"image",
			lambda row, idx: f"product-{slug}-application-{idx}",
		)
		localize_child_table(
			self,
			"content_sections",
			"image",
			lambda row, idx: f"product-{slug}-section-{idx}",
		)
		localize_child_table(
			self,
			"ecosystem_items",
			"image",
			lambda row, idx: f"product-{slug}-ecosystem-{idx}",
		)
		localize_child_table(
			self,
			"related_products",
			"image",
			lambda row, idx: f"product-{slug}-related-{idx}",
		)
		localize_child_table(
			self,
			"visual_story_items",
			"image",
			lambda row, idx: f"product-{slug}-visual-{idx}",
		)
		localize_child_table(
			self,
			"downloads",
			"file",
			lambda row, idx: f"product-{slug}-file-{idx}",
		)

	def validate(self):
		if not self.slug:
			frappe.throw(_("Slug is required"))
		self.slug = slugify(self.slug)
		if not self.slug:
			frappe.throw(_("Slug is invalid"))

		filters = {"slug": self.slug}
		if self.name:
			filters["name"] = ("!=", self.name)
		if frappe.db.exists("Website Product", filters):
			frappe.throw(_("Website Product with slug {0} already exists").format(self.slug))

		if self.brand and not self.brand_name:
			self.brand_name = self.brand

		if self.product_type == "Software":
			self.canonical_path = f"/software/{self.slug}"
		else:
			self.canonical_path = f"/products/{self.slug}"

		validate_doc_fields(
			self,
			[
				("hero_image", "Hero Image"),
				("card_image", "Card Image"),
				("primary_download_file", "Primary Download File"),
			],
		)
		validate_child_table(self, "applications", "image", "Application Image")
		validate_child_table(self, "content_sections", "image", "Content Section Image")
		validate_child_table(self, "ecosystem_items", "image", "Ecosystem Image")
		validate_child_table(self, "related_products", "image", "Related Product Image")
		validate_child_table(self, "visual_story_items", "image", "Visual Story Image")
		validate_child_table(self, "downloads", "file", "Download File")


def infer_division(item_group: str | None, brand: str | None = None) -> str:
	item_group = cstr(item_group).lower()
	if "software" in item_group:
		return "Software"
	if "retail" in item_group:
		return "Retail"
	return "Industrial"


def infer_product_type(division: str) -> str:
	if division == "Software":
		return "Software"
	if division == "Retail":
		return "Retail Hardware"
	return "Industrial"


@frappe.whitelist()
def make_website_product(doc, save=True):
	"""Create Website Product from Item for the new website."""
	if isinstance(doc, str):
		doc = frappe.parse_json(doc)

	item_code = doc.get("name") or doc.get("item_code")
	if not item_code:
		frappe.throw(_("Item Code is required"))

	if frappe.db.exists("Website Product", {"item": item_code}):
		existing = frappe.db.get_value("Website Product", {"item": item_code}, "name")
		frappe.throw(
			_("Website Product {0} already exists for Item {1}").format(existing, item_code),
			title=_("Already Exists"),
		)

	item = frappe.get_doc("Item", item_code)
	division = infer_division(item.item_group, item.brand)
	product_type = infer_product_type(division)
	display_name = item.item_name
	slug = slugify(display_name)
	if frappe.db.exists("Website Product", {"slug": slug}):
		slug = slugify(f"{display_name}-{item_code}")

	website_product = frappe.new_doc("Website Product")
	website_product.website_product_name = display_name
	website_product.display_name = display_name
	website_product.item = item.name
	website_product.brand = item.brand
	website_product.category = item.item_group or "General"
	website_product.short_description = strip_html(item.description or display_name)[:500] or display_name
	website_product.long_description = item.description or display_name
	website_product.division = division
	website_product.product_type = product_type
	website_product.slug = slug
	website_product.published = 0

	website_item_name = frappe.db.get_value("Website Item", {"item_code": item.name}, "name")
	if website_item_name:
		website_product.website_item_reference = website_item_name
		prefill_from_website_item(website_product, website_item_name)

	if not website_product.hero_image and item.image:
		website_product.hero_image = item.image

	if not website_product.hero_image:
		frappe.throw(
			_("Please attach an image on the Item first. Website Product needs a hero image.")
		)

	if save:
		website_product.insert()
		return [website_product.name, website_product.display_name]

	return website_product


def prefill_from_website_item(website_product: Document, website_item_name: str):
	"""Copy marketing fields from legacy Website Item without changing it."""
	website_item = frappe.get_doc("Website Item", website_item_name)

	if website_item.short_description:
		website_product.short_description = website_item.short_description

	if website_item.web_long_description:
		website_product.long_description = website_item.web_long_description

	if website_item.website_image:
		website_product.hero_image = website_item.website_image
		website_product.hero_image_alt = website_item.website_image_alt or website_product.display_name

	if website_item.brand and not website_product.brand:
		website_product.brand = website_item.brand

	attach_doc = website_item.get("attach_doc")
	if attach_doc:
		website_product.primary_download_label = "Download Datasheet"
		website_product.primary_download_file = attach_doc


@frappe.whitelist()
def get_website_product_for_item(item_code: str):
	return frappe.db.get_value("Website Product", {"item": item_code}, "name")
