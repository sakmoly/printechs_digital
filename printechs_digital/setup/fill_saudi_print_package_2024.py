# Copyright (c) 2026, Printechs and contributors
"""Seed Saudi Print & Package 2024 event album."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

import frappe
from frappe.utils import get_files_path
from PIL import Image

SLUG = "saudi-print-package-2024"

IMAGES = [
	{
		"url": "https://scontent.fdmm4-1.fna.fbcdn.net/v/t39.30808-6/480459914_947753920804104_8705565209700745100_n.jpg?stp=cp6_dst-jpg_tt6&cstp=mx2048x1536&ctp=s2048x1536&_nc_cat=104&ccb=1-7&_nc_sid=833d8c&_nc_ohc=zGdGi3o6rIoQ7kNvwGySeBf&_nc_oc=AdowHiTW1ziaZGSLEVJE2LfAvJM3_-H8b1M4MuRhYmr7Wj5NgR4OAhdjNHYfeX7SAb0fTRNOP3txHN6gs-pEKhlH&_nc_zt=23&_nc_ht=scontent.fdmm4-1.fna&_nc_gid=0vFIMrbhu_RgeEgfkp7b6w&_nc_ss=7b2a8&oh=00_AQITO65LfIC55hbmsKjyGKuBezji4UW-YX7EHUKLK0aq8Q&oe=6A9FB349",
		"filename": f"event-{SLUG}-cover.jpg",
		"alt": "Printechs team with High Plast at Saudi Print & Package 2024",
		"caption": "Printechs team with High Plast partners at the exhibition",
	},
	{
		"url": "https://scontent.fdmm4-1.fna.fbcdn.net/v/t39.30808-6/480233581_947753977470765_2236698818749675201_n.jpg?stp=cp6_dst-jpg_tt6&cstp=mx2048x1536&ctp=s2048x1536&_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=PL20ux7b6dUQ7kNvwF_n2sF&_nc_oc=Adp_r1TBwxCkf0l2nijd9qECwhqT2SzVNY0sPPrnwe5OZtMal4f7vEp-vCqU-C3ivf6jddjsL_i3sedM5Cxe5Pim&_nc_zt=23&_nc_ht=scontent.fdmm4-1.fna&_nc_gid=tzFyGy0p6MMvZCZ7XWhzMw&_nc_ss=7b2a8&oh=00_AQIS9Aq2Mj66-gGqxVcKrbStiDlZdD7V_RGhKXFyS6IyVw&oe=6A9FAF7A",
		"filename": f"event-{SLUG}-01.jpg",
		"alt": "Printechs exhibitors at High Plast and Datalogic booth",
		"caption": "Printechs team at the High Plast and Datalogic stand",
	},
	{
		"url": "https://scontent.fdmm4-1.fna.fbcdn.net/v/t39.30808-6/480446504_947753834137446_8156999841915587574_n.jpg?stp=cp6_dst-jpg_tt6&cstp=mx2048x1536&ctp=s2048x1536&_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=6NFp7kl3xsYQ7kNvwFHjvr2&_nc_oc=AdqhfGmkR_wHyg9wsokP41jkE84FtAi5INyKdKp5kHaUCFQ9wg-8_VzTxuXLfdgRQp1G5mwZPltclVmGvKN-YTP5&_nc_zt=23&_nc_ht=scontent.fdmm4-1.fna&_nc_gid=px06C_-fVFsAdVgp_6iT1g&_nc_ss=7b2a8&oh=00_AQK2tss4Q8jnkaUS2NrFrkzrxXtLurpLYUORK87cFoOaNQ&oe=6A9F9FFE",
		"filename": f"event-{SLUG}-02.jpg",
		"alt": "Printechs team dinner during Saudi Print & Package 2024",
		"caption": "Team celebration dinner after a successful exhibition day",
	},
	{
		"url": "https://scontent.fdmm4-1.fna.fbcdn.net/v/t39.30808-6/480309736_947753960804100_7650030918075577051_n.jpg?stp=cp6_dst-jpg_tt6&cstp=mx2048x1536&ctp=s2048x1536&_nc_cat=104&ccb=1-7&_nc_sid=833d8c&_nc_ohc=u0Zfb2drIhEQ7kNvwF3e-Pz&_nc_oc=Ador5IifvmFleYGTBIDYtIITtxIoumNcs6quDEaTHmzTWjpTrHErMQPIr4I9y1tqyCkcZjsMUcC9bm-0jEe1yXJA&_nc_zt=23&_nc_ht=scontent.fdmm4-1.fna&_nc_gid=h5tpmpXCp1xzuTILvr7raQ&_nc_ss=7b2a8&oh=00_AQKf3SC3_niP1m-cOk0EBGSDWNtWy4fUw0UupaRoPCIRRw&oe=6A9F94B5",
		"filename": f"event-{SLUG}-03.jpg",
		"alt": "Printechs and partners at the Datalogic booth",
		"caption": "Partners and customers visiting the Datalogic stand with Printechs",
	},
	{
		"url": "https://scontent.fdmm4-1.fna.fbcdn.net/v/t39.30808-6/480191969_947753820804114_5088140695645971528_n.jpg?stp=cp6_dst-jpg_tt6&cstp=mx1536x2048&ctp=s1536x2048&_nc_cat=106&ccb=1-7&_nc_sid=833d8c&_nc_ohc=E1kFPTvoWrwQ7kNvwE5QMNu&_nc_oc=AdrwHHsF-aHvLSbs-uFuB1bwnX6Xu_K3lY83zDB45psYRhWmzSGf_d32ProxAsUrF3lS3M5_CL2TtMj5WZVqHSy4&_nc_zt=23&_nc_ht=scontent.fdmm4-1.fna&_nc_gid=qmwz4yfqfSM9SoZ_gzmM_Q&_nc_ss=7b2a8&oh=00_AQIahZm5uES4p7wWXjjGste-ZFpNgIsD86FJGiQwJ91OQQ&oe=6A9FA7EA",
		"filename": f"event-{SLUG}-04.jpg",
		"alt": "Printechs team at the company exhibition booth",
		"caption": "The Printechs team at our booth — Datalogic, REA JET and Avery Berkel",
	},
]

DESCRIPTION = """What an amazing journey! Saudi Print & Package 2024 was a huge success.

Proud of our team and thankful for the incredible support from customers, partners and visitors throughout the exhibition.

Printechs showcased industrial coding, marking, retail technology and partner solutions alongside High Plast, Datalogic and other leading brands at Riyadh's premier print and packaging trade show."""


def download_and_save(url: str, filename: str) -> str:
	request = Request(
		url,
		headers={
			"User-Agent": (
				"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
				"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
			)
		},
	)
	with urlopen(request, timeout=60) as response:
		data = response.read()

	target = Path(get_files_path(filename, is_private=False))
	with Image.open(BytesIO(data)) as image:
		image = image.convert("RGB")
		width, height = image.size
		max_dim = 1600
		if max(width, height) > max_dim:
			scale = max_dim / max(width, height)
			image = image.resize(
				(int(width * scale), int(height * scale)),
				Image.Resampling.LANCZOS,
			)
		buffer = BytesIO()
		image.save(buffer, format="JPEG", optimize=True, quality=82)
		target.write_bytes(buffer.getvalue())

	return f"/files/{filename}"


def fill_saudi_print_package_2024():
	if frappe.db.exists("Website Event Album", SLUG):
		doc = frappe.get_doc("Website Event Album", SLUG)
	else:
		doc = frappe.new_doc("Website Event Album")
		doc.slug = SLUG

	doc.title = "Saudi Print & Package 2024"
	doc.published = 1
	doc.featured = 1
	doc.sort_order = 1
	doc.event_type = "Exhibition"
	doc.event_date = "2024-02-06"
	doc.location = "Riyadh, Saudi Arabia"
	doc.summary = (
		"What an amazing journey! Saudi Print & Package 2024 was a huge success. "
		"Proud of our team and thankful for the incredible support!"
	)
	doc.description = DESCRIPTION
	doc.meta_title = "Saudi Print & Package 2024 | Printechs Events"
	doc.meta_description = doc.summary

	saved_paths = []
	for item in IMAGES:
		saved_paths.append(download_and_save(item["url"], item["filename"]))

	doc.cover_image = saved_paths[0]
	doc.cover_image_alt = IMAGES[0]["alt"]

	gallery = []
	for idx, item in enumerate(IMAGES[1:], start=1):
		gallery.append(
			{
				"image": saved_paths[idx],
				"image_alt": item["alt"],
				"caption": item["caption"],
				"sort_order": idx,
			}
		)
	doc.set("gallery", gallery)

	doc.save(ignore_permissions=True)
	frappe.db.commit()
	frappe.msgprint(f"Published event album: {doc.name} ({len(saved_paths)} photos)")
	return doc.name


if __name__ == "__main__":
	fill_saudi_print_package_2024()
