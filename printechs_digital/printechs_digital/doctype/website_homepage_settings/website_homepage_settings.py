# Copyright (c) 2026, Printechs and contributors

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


class WebsiteHomepageSettings(Document):
	def before_validate(self):
		localize_doc_fields(
			self,
			[
				("hero_image", "home-hero"),
				("hero_video", "home-hero-video"),
				("hero_video_poster", "home-hero-poster"),
				("video_poster", "home-video-poster"),
			],
		)

		localize_child_table(
			self,
			"divisions",
			"image",
			lambda row, idx: f"home-division-{idx}",
		)
		for row in self.get("divisions") or []:
			if not row.image_alt:
				row.image_alt = row.title

		localize_child_table(
			self,
			"extra_blocks",
			"image",
			lambda row, idx: f"home-extra-block-{idx}",
		)
		for row in self.get("extra_blocks") or []:
			if row.image and not row.image_alt:
				row.image_alt = row.heading

	def validate(self):
		if self.hero_media_kind == "Image" and not self.hero_image:
			frappe.throw(_("Hero Image is required when Hero Media is Image"))
		if self.hero_media_kind == "Hosted Video" and not self.hero_video:
			frappe.throw(_("Hero Video is required when Hero Media is Hosted Video"))

		validate_doc_fields(
			self,
			[
				("hero_image", "Hero Image"),
				("hero_video", "Hero Video"),
				("hero_video_poster", "Hero Video Poster"),
				("video_poster", "Poster Image"),
			],
		)
		validate_child_table(self, "divisions", "image", "Division Image")
		validate_child_table(self, "extra_blocks", "image", "Extra Block Image")
