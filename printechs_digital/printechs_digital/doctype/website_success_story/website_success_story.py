# Copyright (c) 2026, Printechs and contributors

import re

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cstr

from printechs_digital.utils.website_assets import (
	localize_child_table,
	localize_doc_fields,
	validate_child_table,
	validate_doc_fields,
)

INDUSTRY_SLUGS = {
	"Dairy": "dairy",
	"Food & Beverage": "food-beverage",
	"Bakery": "bakery",
	"Egg / Poultry": "egg-poultry",
	"Pharmaceutical": "pharmaceutical",
	"Pipe": "pipe",
	"Plastic": "plastic",
	"Steel": "steel",
	"Packaging": "packaging",
	"Retail": "retail",
	"Fashion": "fashion",
	"Warehouse & Logistics": "warehouse-logistics",
}


def slugify(value: str) -> str:
	value = cstr(value).lower().strip()
	value = re.sub(r"[^\w\s-]", "", value)
	value = re.sub(r"[\s_]+", "-", value)
	value = re.sub(r"-+", "-", value)
	return value.strip("-")


def industry_slug(value: str | None) -> str:
	if not value:
		return ""
	if value in INDUSTRY_SLUGS:
		return INDUSTRY_SLUGS[value]
	if value in INDUSTRY_SLUGS.values():
		return value
	return slugify(value)


class WebsiteSuccessStory(Document):
	def autoname(self):
		self.name = slugify(self.slug or self.title)

	def before_validate(self):
		if self.website_product:
			product = frappe.db.get_value(
				"Website Product",
				self.website_product,
				["slug", "brand", "display_name"],
				as_dict=True,
			)
			if product:
				self.product_slug = product.slug
				if not self.brand and product.brand:
					self.brand = product.brand

		if self.brand:
			self.brand_slug = (
				frappe.db.get_value("Website Brand", {"brand": self.brand}, "slug")
				or slugify(self.brand)
			)

		if not self.slug:
			self.slug = slugify(self.title)
		if not self.hero_image_alt:
			self.hero_image_alt = self.title
		self.industry_slug = industry_slug(self.industry)

		story_slug = self.slug or "story"
		localize_doc_fields(self, [("hero_image", f"success-story-{story_slug}")])
		localize_child_table(
			self,
			"gallery",
			"image",
			lambda row, idx: f"success-story-{story_slug}-gallery-{idx}",
		)
		localize_child_table(
			self,
			"videos",
			"poster",
			lambda row, idx: f"success-story-{story_slug}-video-poster-{idx}",
		)
		localize_child_table(
			self,
			"videos",
			"video_file",
			lambda row, idx: f"success-story-{story_slug}-video-{idx}",
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
		if frappe.db.exists("Website Success Story", filters):
			frappe.throw(_("Website Success Story with slug {0} already exists").format(self.slug))

		validate_doc_fields(self, [("hero_image", "Hero Image")])
		validate_child_table(self, "gallery", "image", "Gallery Image")
		validate_child_table(self, "videos", "poster", "Video Poster")
		validate_child_table(self, "videos", "video_file", "Video File")
