#!/usr/bin/env python3
# Copyright (c) 2026, Printechs and contributors
"""Compress website product images in Frappe /files/ and update DB paths."""

from __future__ import annotations

import sys
from io import BytesIO
from pathlib import Path

from PIL import Image


FILES_DIR = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
MAX_DIMENSION = 1600
JPEG_QUALITY = 82
PNG_TO_JPEG_MIN_BYTES = 80_000

TARGETS = [
	"CAS-CL5200B.png",
	"anser-sph-smart-printhead.png",
	"kezojet-kt10-hero.png",
	"software-erpnext.jpg",
	"software-modern-pos.jpg",
	"software-warehouse-management-system.jpg",
	"software-zatca-integration.jpg",
	"CL5500P.jpg",
	"CL5200.jpg",
	"CL5500H-60.jpg",
	"CN.jpg",
	"UX-D151W.jpg",
	"uxd161.jpg",
	"Memor17_front.jpg",
	"ZT421.jpg",
]


def to_rgb(image: Image.Image) -> Image.Image:
	if image.mode in ("RGBA", "P", "LA"):
		background = Image.new("RGB", image.size, (255, 255, 255))
		if image.mode in ("RGBA", "LA"):
			background.paste(image.convert("RGBA"), mask=image.split()[-1])
		else:
			background.paste(image.convert("RGB"))
		return background
	if image.mode != "RGB":
		return image.convert("RGB")
	return image


def optimize_image(path: Path) -> tuple[int, int, Path]:
	original_size = path.stat().st_size
	suffix = path.suffix.lower()

	with Image.open(path) as image:
		image.load()
		image = to_rgb(image)

		width, height = image.size
		if max(width, height) > MAX_DIMENSION:
			scale = MAX_DIMENSION / max(width, height)
			image = image.resize(
				(int(width * scale), int(height * scale)),
				Image.Resampling.LANCZOS,
			)

		should_convert_png = suffix == ".png" and original_size >= PNG_TO_JPEG_MIN_BYTES
		target_path = path.with_suffix(".jpg") if should_convert_png else path

		buffer = BytesIO()
		image.save(buffer, format="JPEG", optimize=True, quality=JPEG_QUALITY)
		new_bytes = buffer.getvalue()

		if len(new_bytes) >= original_size and not should_convert_png:
			return original_size, original_size, path

		if should_convert_png and target_path != path:
			path.unlink(missing_ok=True)
			target_path.write_bytes(new_bytes)
			return original_size, len(new_bytes), target_path

		path.write_bytes(new_bytes)
		return original_size, len(new_bytes), path


def update_file_references(old_name: str, new_name: str) -> None:
	import frappe

	old_path = f"/files/{old_name}"
	new_path = f"/files/{new_name}"
	if old_path == new_path:
		return

	for doctype, fields in (
		("Website Product", ("hero_image", "card_image")),
		("Website Success Story", ("hero_image", "card_image")),
	):
		if not frappe.db.exists("DocType", doctype):
			continue
		for field in fields:
			if not frappe.db.has_column(doctype, field):
				continue
			frappe.db.sql(
				f"""
				UPDATE `tab{doctype}`
				SET `{field}` = %s
				WHERE `{field}` = %s
				""",
				(new_path, old_path),
			)


def main() -> int:
	if not FILES_DIR.is_dir():
		print(f"Files directory not found: {FILES_DIR}", file=sys.stderr)
		return 1

	total_before = 0
	total_after = 0
	processed = 0
	renamed: list[tuple[str, str]] = []

	for name in TARGETS:
		path = FILES_DIR / name
		if not path.exists():
			print(f"skip missing: {name}")
			continue

		before, after, final_path = optimize_image(path)
		total_before += before
		total_after += after
		processed += 1
		print(f"{name}: {before // 1024}KB -> {after // 1024}KB")

		if final_path.name != name:
			renamed.append((name, final_path.name))

	if renamed:
		import frappe

		frappe.init(site="site1.local")
		frappe.connect()
		for old_name, new_name in renamed:
			update_file_references(old_name, new_name)
			print(f"updated DB refs: {old_name} -> {new_name}")
		frappe.db.commit()
		frappe.destroy()

	print(f"Processed {processed} files: {total_before // 1024}KB -> {total_after // 1024}KB")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
