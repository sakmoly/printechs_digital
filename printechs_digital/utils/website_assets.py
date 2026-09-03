# Copyright (c) 2026, Printechs and contributors

from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import frappe
from frappe import _
from frappe.utils import cstr, get_files_path

ALLOWED_HOSTS = ("printechs.com", "demo.printechs.com")

ALLOWED_EXTENSIONS = {
	".png",
	".jpg",
	".jpeg",
	".webp",
	".svg",
	".gif",
	".mp4",
	".webm",
	".pdf",
	".doc",
	".docx",
	".xls",
	".xlsx",
	".zip",
}


def is_remote_url(path: str | None) -> bool:
	return cstr(path).startswith(("http://", "https://"))


def is_local_asset(path: str | None) -> bool:
	value = cstr(path)
	if not value:
		return True
	if value.startswith(("/files/", "/images/", "/private/files/")):
		return True
	if is_remote_url(value):
		host = (urlparse(value).hostname or "").lower()
		return host in ALLOWED_HOSTS and ("/files/" in value or "/images/" in value)
	return False


def localize_remote_file(path: str, filename: str) -> str:
	request = Request(
		path,
		headers={
			"User-Agent": (
				"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
				"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
			)
		},
	)
	suffix = Path(urlparse(path).path).suffix.lower() or Path(filename).suffix or ".png"
	if suffix not in ALLOWED_EXTENSIONS:
		suffix = Path(filename).suffix or ".png"
	target_name = f"{Path(filename).stem}{suffix}"
	target = Path(get_files_path(target_name, is_private=False))
	try:
		with urlopen(request, timeout=30) as response:
			data = response.read()
	except Exception:
		frappe.throw(
			_("This file URL cannot be used on the website. Upload the file instead of pasting an external link.")
		)
	if not data:
		frappe.throw(_("The uploaded file is empty."))
	target.write_bytes(data)
	return f"/files/{target_name}"


def ensure_local_asset(path: str | None, filename: str) -> str | None:
	value = cstr(path)
	if not value or is_local_asset(value):
		return value or None
	if is_remote_url(value):
		return localize_remote_file(value, filename)
	return value


def validate_local_asset(path: str | None, label: str) -> None:
	if cstr(path) and not is_local_asset(path):
		frappe.throw(
			_("Upload {0} as a file on this site. External links will not display on the website.").format(
				_(label)
			)
		)


def localize_doc_fields(doc, field_specs: list[tuple[str, str]]) -> None:
	for fieldname, filename in field_specs:
		value = ensure_local_asset(doc.get(fieldname), filename)
		if value is not None:
			doc.set(fieldname, value)


def validate_doc_fields(doc, field_specs: list[tuple[str, str]]) -> None:
	for fieldname, label in field_specs:
		validate_local_asset(doc.get(fieldname), label)


def localize_child_table(doc, table_field: str, attach_field: str, filename_fn) -> None:
	for idx, row in enumerate(doc.get(table_field) or [], start=1):
		value = ensure_local_asset(row.get(attach_field), filename_fn(row, idx))
		if value is not None:
			row.set(attach_field, value)


def validate_child_table(doc, table_field: str, attach_field: str, label: str) -> None:
	for row in doc.get(table_field) or []:
		validate_local_asset(row.get(attach_field), label)
