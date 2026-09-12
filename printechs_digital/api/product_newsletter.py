# Copyright (c) 2026, Printechs and contributors
"""Draft a Desk Newsletter from a published Website Product. Does not send."""

import json
import re
from pathlib import Path
from shutil import copy2

from PIL import Image, ImageDraw, ImageFont

import frappe
from frappe import _
from frappe.utils import cstr, escape_html, get_url, strip_html

DEFAULT_SENDER_NAME = "Printechs"
DEFAULT_SENDER_EMAIL = "support@printechs.com"
DEFAULT_EMAIL_GROUP = "Printechs-Staff"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
LOGO_SRC = Path(
	"/home/erpnext/frappe-bench/frontend/printechs-web/public/images/company/printechs-logo-full.png"
)
NEWSLETTER_WIDTH = 800

SOCIAL_LINKS = (
	("Facebook", "https://www.facebook.com/Printechs/", (24, 119, 242), "f"),
	("LinkedIn", "https://www.linkedin.com/company/printechs", (10, 102, 194), "in"),
	("X", "https://x.com/printechssaudi", (17, 24, 39), "X"),
	("Instagram", "https://www.instagram.com/printechssaudiarabia/", (219, 39, 119), "ig"),
	("WhatsApp", "https://wa.me/966550733441", (37, 211, 102), "W"),
)


def _esc(value) -> str:
	return escape_html(cstr(value or "").strip())


def _absolute_url(path: str) -> str:
	path = cstr(path).strip()
	if not path:
		return ""
	if path.startswith("http://") or path.startswith("https://"):
		url = path
	else:
		url = get_url(path)
	# Outlook/Microsoft 365 treats http:// image and link hosts as junk.
	if url.startswith("http://printechs.com"):
		url = "https://printechs.com" + url[len("http://printechs.com") :]
	elif url.startswith("http://www.printechs.com"):
		url = "https://www.printechs.com" + url[len("http://www.printechs.com") :]
	return url


def _first_office_phone(phone: str) -> str:
	first = cstr(phone).split("|")[0].split("/")[0].strip()
	for prefix in ("Tel:", "tel:", "Mob:", "Mobile:", "Phone:"):
		if first.lower().startswith(prefix.lower()):
			first = first[len(prefix) :].strip()
			break
	return _international_ksa_phone(first)


def _international_ksa_phone(phone: str) -> str:
	"""Show every branch number as +966 … so the footer stays one format."""
	raw = cstr(phone).strip()
	if not raw:
		return raw
	if raw.startswith("+966"):
		return raw
	digits = "".join(ch for ch in raw if ch.isdigit())
	if digits.startswith("966"):
		digits = digits[3:]
	elif digits.startswith("0"):
		digits = digits[1:]
	if not digits:
		return raw
	# +966 11 206 2828 / +966 12 257 7799 / +966 13 835 5339 / +966 55 073 3441
	if len(digits) >= 9:
		return f"+966 {digits[:2]} {digits[2:5]} {digits[5:]}"
	return f"+966 {digits}"


def _branch_phone_line() -> str:
	"""One footer line: Riyadh · Jeddah · Dammam from Website Contact Settings."""
	parts = []
	if frappe.db.exists("DocType", "Website Contact Settings"):
		doc = frappe.get_single("Website Contact Settings")
		rows = sorted(doc.get("offices") or [], key=lambda row: (row.sort_order or 0, row.idx or 0))
		for row in rows:
			city = cstr(row.city).strip()
			phone = _first_office_phone(row.phone)
			if city and phone:
				parts.append(f"{_esc(city)} {_esc(phone)}")

	if not parts:
		parts = [
			"Riyadh +966 11 206 2828",
			"Jeddah +966 12 257 7799",
			"Dammam +966 13 835 5339",
		]

	return "Tel: " + " · ".join(parts)


def _product_page_url(doc) -> str:
	if doc.canonical_path:
		return _absolute_url(doc.canonical_path)
	prefix = "/software/" if cstr(doc.product_type) == "Software" else "/products/"
	return _absolute_url(f"{prefix}{doc.slug}")


def _brand_logo_url(doc) -> str:
	filters = []
	if doc.brand:
		filters.append({"brand": doc.brand})
	label = cstr(doc.card_brand_label or doc.brand_name).strip()
	if label:
		filters.append({"display_name": label})
	for filt in filters:
		logo = frappe.db.get_value("Website Brand", filt, "logo")
		if logo:
			return _absolute_url(logo)
	slug = cstr(label or doc.brand).lower().replace(" ", "-")
	candidate = SITE_FILES / f"brand-{slug}.png"
	if slug and candidate.exists():
		return _absolute_url(f"/files/brand-{slug}.png")
	return ""


def install_newsletter_assets() -> dict[str, str]:
	SITE_FILES.mkdir(parents=True, exist_ok=True)
	logo_dest = SITE_FILES / "printechs-logo-full.png"
	if LOGO_SRC.exists() and (not logo_dest.exists() or logo_dest.stat().st_size < 1000):
		copy2(LOGO_SRC, logo_dest)

	assets = {"logo": _absolute_url("/files/printechs-logo-full.png")}
	for label, _href, color, glyph in SOCIAL_LINKS:
		filename = f"newsletter-social-{label.lower()}.png"
		dest = SITE_FILES / filename
		if not dest.exists():
			canvas = Image.new("RGBA", (72, 72), (0, 0, 0, 0))
			draw = ImageDraw.Draw(canvas)
			draw.ellipse((0, 0, 71, 71), fill=color)
			try:
				font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26 if len(glyph) < 3 else 20)
			except OSError:
				font = ImageFont.load_default()
			bbox = draw.textbbox((0, 0), glyph, font=font)
			tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
			draw.text(((72 - tw) / 2 - bbox[0], (72 - th) / 2 - bbox[1]), glyph, fill=(255, 255, 255), font=font)
			canvas.save(dest, "PNG")
		assets[label.lower()] = _absolute_url(f"/files/{filename}")
	return assets


def _product_title(doc) -> str:
	return cstr(doc.display_name or doc.website_product_name or "Product")


def _product_intro(doc) -> str:
	intro = cstr(doc.short_description or doc.card_summary).strip()
	if intro:
		return intro
	return strip_html(cstr(doc.long_description))[:420]


def _subject_from_docs(docs) -> str:
	names = [_product_title(doc) for doc in docs]
	if len(names) == 1:
		return f"{names[0]} | Printechs"
	if len(names) == 2:
		return f"{names[0]} and {names[1]} | Printechs"
	return f"{', '.join(names[:-1])} and {names[-1]} | Printechs"


def _heading_from_docs(docs) -> str:
	return _subject_from_docs(docs).removesuffix(" | Printechs")


def _brand_html(doc) -> str:
	brand = cstr(doc.card_brand_label or doc.brand_name or doc.brand or "Printechs")
	brand_logo = _brand_logo_url(doc)
	if brand_logo:
		return (
			f"<p style='margin:0 0 18px;text-align:center;'>"
			f"<img src='{_esc(brand_logo)}' alt='{_esc(brand)}' width='160' "
			f"style='display:inline-block;max-width:160px;height:auto;border:0;' />"
			f"</p>"
		)
	return (
		f"<p style='margin:0 0 12px;text-align:center;font-size:12px;font-weight:700;"
		f"letter-spacing:0.18em;text-transform:uppercase;color:#64748b;'>{_esc(brand)}</p>"
	)


def _shared_brand_html(docs) -> str:
	keys = []
	for doc in docs:
		keys.append(_brand_logo_url(doc) or cstr(doc.card_brand_label or doc.brand_name or doc.brand))
	if len(set(keys)) == 1:
		return _brand_html(docs[0])
	return ""


def _benefits_html(doc, limit: int) -> str:
	benefits = sorted(doc.get("benefits") or [], key=lambda row: (row.sort_order or 0, row.idx or 0))
	rows = []
	for row in benefits[:limit]:
		if not row.title:
			continue
		rows.append(
			"<tr>"
			f"<td style='padding:10px 0 10px 0;border-bottom:1px solid #e8edf2;'>"
			f"<p style='margin:0;font-size:16px;font-weight:700;color:#0f172a;'>{_esc(row.title)}</p>"
			f"<p style='margin:4px 0 0;font-size:14px;line-height:1.55;color:#475569;'>{_esc(row.description)}</p>"
			"</td></tr>"
		)
	if not rows:
		return ""
	return (
		"<p style='margin:28px 0 10px;font-size:12px;font-weight:700;letter-spacing:0.16em;"
		"text-transform:uppercase;color:#1a7f4b;'>Highlights</p>"
		f"<table role='presentation' width='100%' cellpadding='0' cellspacing='0'>{''.join(rows)}</table>"
	)


def _cta_html(page_url: str) -> str:
	return (
		"<table role='presentation' cellpadding='0' cellspacing='0' align='center' style='margin:28px auto 0;'>"
		"<tr>"
		"<td align='center' style='background:#0f172a;border-radius:28px;'>"
		f"<a href='{_esc(page_url)}' style='display:inline-block;padding:14px 28px;font-size:15px;"
		"font-weight:700;color:#ffffff;text-decoration:none;'>View product details</a>"
		"</td></tr></table>"
	)


def _product_section_html(doc, compact: bool = False) -> str:
	title = _product_title(doc)
	tagline = cstr(doc.tagline or "")
	intro = _product_intro(doc)
	image = _absolute_url(doc.hero_image or doc.card_image)
	image_alt = cstr(doc.hero_image_alt or title)
	page_url = _product_page_url(doc)
	image_width = 640 if compact else 720
	heading_tag = "h2" if compact else "h1"
	heading_size = "26px" if compact else "30px"
	pad_top = "8px" if compact else "36px"

	image_html = ""
	if image:
		image_html = (
			f"<p style='margin:8px 0 0;text-align:center;'>"
			f"<img src='{_esc(image)}' alt='{_esc(image_alt)}' width='{image_width}' "
			f"style='display:block;margin:0 auto;max-width:100%;width:{image_width}px;height:auto;border:0;' />"
			f"</p>"
		)

	title_html = (
		f"<{heading_tag} style='margin:0 0 12px;text-align:center;font-size:{heading_size};"
		f"line-height:1.25;font-weight:700;color:#0f172a;'>{_esc(title)}</{heading_tag}>"
	)
	tagline_html = ""
	if tagline or (not compact and intro):
		tagline_html = (
			f"<p style='margin:0 auto 8px;max-width:680px;text-align:center;font-size:17px;"
			f"line-height:1.55;color:#475569;'>{_esc(tagline or intro)}</p>"
		)
	intro_html = ""
	if tagline and intro:
		intro_html = (
			f"<p style='margin:16px 0 0;font-size:16px;line-height:1.7;color:#334155;'>{_esc(intro)}</p>"
		)

	return (
		f"<tr><td style='padding:{pad_top} 48px 8px;background:#ffffff;'>"
		f"{title_html}{tagline_html}</td></tr>"
		f"<tr><td style='padding:8px 40px 8px;background:#ffffff;'>{image_html}</td></tr>"
		f"<tr><td style='padding:8px 48px 36px;background:#ffffff;'>"
		f"{intro_html}{_benefits_html(doc, 3 if compact else 4)}{_cta_html(page_url)}"
		f"</td></tr>"
	)


ALLOWED_STORY_TAGS = {
	"p",
	"br",
	"strong",
	"b",
	"em",
	"i",
	"u",
	"h1",
	"h2",
	"h3",
	"h4",
	"ul",
	"ol",
	"li",
	"a",
	"img",
	"span",
	"div",
	"blockquote",
}
ALLOWED_STORY_ATTRS = {"href", "src", "alt", "title", "target"}


def _is_blank_story(html: str) -> bool:
	raw = cstr(html) or ""
	if "<img" in raw.lower():
		return False
	return not strip_html(raw).replace("\xa0", " ").strip()


def _story_block_html(story_html: str) -> str:
	"""Email-safe optional story inserted above the product blocks."""
	if _is_blank_story(story_html):
		return ""

	from bs4 import BeautifulSoup

	soup = BeautifulSoup(cstr(story_html), "html.parser")
	heading_used = False
	for tag in soup.find_all(True):
		if tag.name not in ALLOWED_STORY_TAGS:
			tag.unwrap()
			continue
		for attr in list(tag.attrs):
			if attr not in ALLOWED_STORY_ATTRS:
				del tag.attrs[attr]
		if tag.name == "a" and tag.get("href"):
			tag["href"] = _absolute_url(tag.get("href"))
			tag["style"] = "color:#1a7f4b;text-decoration:underline;"
		elif tag.name == "img":
			src = tag.get("src") or ""
			if src:
				tag["src"] = _absolute_url(src)
			tag["alt"] = tag.get("alt") or "Newsletter image"
			tag["style"] = "display:block;margin:20px auto 8px;max-width:100%;height:auto;border:0;"
			if not tag.get("width"):
				tag["width"] = "640"
		elif tag.name in {"h1", "h2", "h3", "h4"}:
			label = strip_html(tag.get_text() or "").strip()
			if not heading_used and len(label) <= 28:
				tag["style"] = (
					"margin:0 0 14px;font-size:12px;line-height:1.4;font-weight:700;"
					"letter-spacing:0.16em;text-transform:uppercase;color:#1a7f4b;"
				)
			else:
				tag["style"] = (
					"margin:0 0 14px;font-size:24px;line-height:1.3;font-weight:700;color:#0f172a;"
				)
			heading_used = True
		elif tag.name == "p":
			tag["style"] = "margin:0 0 14px;font-size:16px;line-height:1.75;color:#334155;"
		elif tag.name in {"ul", "ol"}:
			tag["style"] = "margin:0 0 14px;padding-left:20px;color:#334155;font-size:16px;line-height:1.75;"
		elif tag.name == "li":
			tag["style"] = "margin:0 0 6px;color:#334155;"

	inner = "".join(str(child) for child in soup.contents).strip()
	if _is_blank_story(inner):
		return ""
	return (
		"<tr><td style='padding:32px 48px 8px;background:#ffffff;font-family:Arial,Helvetica,sans-serif;'>"
		f"{inner}</td></tr>"
		"<tr><td style='padding:8px 48px 16px;background:#ffffff;'>"
		"<div style='border-top:1px solid #e8edf2;height:1px;line-height:1px;'>&nbsp;</div>"
		"</td></tr>"
	)


def _docs_from_stored_names(raw) -> list:
	names = _parse_extra_products(raw)
	docs = []
	for name in names:
		if frappe.db.exists("Website Product", name):
			docs.append(frappe.get_doc("Website Product", name))
	return docs


def _absolutize_story_images(story_html: str) -> str:
	raw = cstr(story_html)
	if "<img" not in raw.lower():
		return raw
	from bs4 import BeautifulSoup

	soup = BeautifulSoup(raw, "html.parser")
	for tag in soup.find_all("img"):
		src = tag.get("src") or ""
		if src and not src.startswith(("http://", "https://")):
			tag["src"] = _absolute_url(src)
	return str(soup)


def apply_campaign_message(doc, method=None):
	"""Rebuild product-newsletter HTML when the optional story is saved. No-op otherwise."""
	if not doc.get("pd_from_website_product") or doc.email_sent:
		return
	if doc.flags.get("pd_rebuilding_newsletter"):
		return

	docs = _docs_from_stored_names(doc.get("pd_website_products"))
	if not docs:
		docs = _docs_from_newsletter_body(cstr(doc.message_html or doc.message))
	if not docs:
		return

	doc.pd_campaign_message = _absolutize_story_images(doc.get("pd_campaign_message"))
	doc.content_type = "HTML"
	doc.message_html = build_product_newsletter_html(docs, story_html=doc.get("pd_campaign_message"))
	if not doc.get("pd_website_products"):
		doc.pd_website_products = json.dumps([row.name for row in docs])


def build_product_newsletter_html(docs, story_html: str | None = None) -> str:
	if not isinstance(docs, (list, tuple)):
		docs = [docs]
	docs = [doc for doc in docs if doc]
	if not docs:
		frappe.throw(_("Select at least one Website Product."))

	assets = install_newsletter_assets()
	home = _absolute_url("/")
	contact = _absolute_url("/contact")
	multi = len(docs) > 1
	shared_brand = _shared_brand_html(docs)

	social_cells = []
	for label, href, _color, _glyph in SOCIAL_LINKS:
		icon = assets.get(label.lower())
		social_cells.append(
			"<td align='center' style='padding:0 7px;'>"
			f"<a href='{_esc(href)}' style='text-decoration:none;'>"
			f"<img src='{_esc(icon)}' alt='{_esc(label)}' width='32' height='32' "
			f"style='display:block;border:0;width:32px;height:32px;' />"
			f"</a></td>"
		)

	story_row = _story_block_html(story_html)

	if multi:
		product_rows = [
			"<tr><td style='padding:28px 48px 8px;background:#ffffff;'>"
			f"{shared_brand}"
			f"<h1 style='margin:0 0 8px;text-align:center;font-size:28px;line-height:1.25;"
			f"font-weight:700;color:#0f172a;'>{_esc(_heading_from_docs(docs))}</h1>"
			"</td></tr>"
		]
		for idx, doc in enumerate(docs):
			if idx:
				product_rows.append(
					"<tr><td style='padding:0 48px;background:#ffffff;'>"
					"<div style='border-top:1px solid #e8edf2;height:1px;line-height:1px;'>&nbsp;</div>"
					"</td></tr>"
				)
			product_rows.append(_product_section_html(doc, compact=True))
	else:
		first = _product_section_html(docs[0], compact=False)
		if shared_brand:
			first = first.replace(
				"<tr><td style='padding:36px 48px 8px;background:#ffffff;'>",
				f"<tr><td style='padding:36px 48px 8px;background:#ffffff;'>{shared_brand}",
				1,
			)
		product_rows = [first]

	# Table fragment only. Do not add <!--[if mso]> here — Frappe's inliner
	# escapes nested Outlook comments and some tenants then drop the mail.
	return f"""<table role="presentation" align="center" width="{NEWSLETTER_WIDTH}" cellpadding="0" cellspacing="0" border="0" style="width:{NEWSLETTER_WIDTH}px;max-width:{NEWSLETTER_WIDTH}px;background:#ffffff;font-family:Arial,Helvetica,sans-serif;">
          <tr>
            <td style="padding:22px 36px 18px;background:#ffffff;border-bottom:3px solid #1a7f4b;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="left" valign="middle">
                    <a href="{_esc(home)}" style="text-decoration:none;">
                      <img src="{_esc(assets['logo'])}" alt="Printechs" width="220" style="display:block;border:0;max-width:220px;height:auto;" />
                    </a>
                  </td>
                  <td align="right" valign="middle" style="font-size:12px;line-height:1.45;color:#64748b;">
                    Industrial · Retail · Software<br />Saudi Arabia
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          {story_row}{"".join(product_rows)}
          <tr>
            <td style="background:#0f172a;padding:32px 40px 20px;">
              <p style="margin:0 0 6px;font-size:16px;font-weight:700;color:#ffffff;">Printechs</p>
              <p style="margin:0 0 16px;font-size:13px;line-height:1.6;color:#cbd5e1;">
                Advanced Printing Trading Co.<br />
                Industrial coding, retail technology and enterprise software<br />
                Riyadh, Jeddah and Dammam, Kingdom of Saudi Arabia
              </p>
              <p style="margin:0 0 6px;font-size:13px;line-height:1.7;color:#e2e8f0;">
                {_branch_phone_line()}
              </p>
              <p style="margin:0 0 18px;font-size:13px;line-height:1.7;color:#e2e8f0;">
                Email: <a href="mailto:info@printechs.com" style="color:#86efac;text-decoration:none;">info@printechs.com</a>
                · <a href="{_esc(contact)}" style="color:#86efac;text-decoration:none;">Contact us</a>
              </p>
              <table role="presentation" cellpadding="0" cellspacing="0" align="center">
                <tr>
                  {''.join(social_cells)}
                </tr>
              </table>
              <p style="margin:18px 0 0;text-align:center;">
                <a href="{_esc(home)}" style="color:#ffffff;font-size:14px;font-weight:700;text-decoration:none;">www.printechs.com</a>
              </p>
            </td>
          </tr>
          <tr>
            <td style="background:#020617;padding:14px 40px;">
              <p style="margin:0;font-size:11px;line-height:1.6;color:#94a3b8;text-align:center;">
                You received this email because you are a Printechs contact.
                An unsubscribe link is added automatically when the newsletter is sent.
              </p>
            </td>
          </tr>
  </table>"""


def _parse_extra_products(extra_products) -> list[str]:
	if not extra_products:
		return []
	if isinstance(extra_products, str):
		raw = extra_products.strip()
		if raw.startswith("["):
			extra_products = json.loads(raw)
		else:
			extra_products = [part.strip() for part in raw.split(",") if part.strip()]
	return [cstr(name).strip() for name in extra_products if cstr(name).strip()]


def _load_newsletter_products(website_product: str, extra_products=None):
	names = []
	for name in [cstr(website_product).strip(), *_parse_extra_products(extra_products)]:
		if name and name not in names:
			names.append(name)

	docs = []
	for name in names:
		if not frappe.db.exists("Website Product", name):
			frappe.throw(_("Website Product {0} was not found.").format(name))
		doc = frappe.get_doc("Website Product", name)
		if not doc.slug:
			frappe.throw(_("{0} needs a slug before it can be added to a newsletter.").format(_product_title(doc)))
		docs.append(doc)
	if not docs:
		frappe.throw(_("Select at least one Website Product."))
	return docs


def _docs_from_newsletter_body(body: str):
	products = frappe.get_all("Website Product", fields=["name", "slug"])
	by_slug = {row.slug: row.name for row in products if row.slug}
	found = []
	seen = set()
	for slug in re.findall(r"/(?:products|software)/([a-z0-9-]+)", body):
		name = by_slug.get(slug)
		if name and name not in seen:
			seen.add(name)
			found.append(frappe.get_doc("Website Product", name))
	return found


@frappe.whitelist()
def create_from_website_product(
	website_product: str,
	email_group: str,
	subject: str | None = None,
	extra_products=None,
	sender_email: str | None = None,
	sender_name: str | None = None,
):
	"""Create a draft Newsletter from one or more Website Products. Does not send."""
	if not frappe.has_permission("Newsletter", "create"):
		frappe.throw(_("You need the Newsletter Manager role to create a newsletter."))

	if frappe.flags.in_import or frappe.flags.in_migrate:
		frappe.throw(_("Cannot create a newsletter during import or migrate."))

	docs = _load_newsletter_products(website_product, extra_products)

	email_group = cstr(email_group).strip()
	if not email_group or not frappe.db.exists("Email Group", email_group):
		frappe.throw(_("Please choose a valid Email Group."))

	default_single = f"{_product_title(docs[0])} | Printechs"
	subject = cstr(subject).strip()
	if not subject or (len(docs) > 1 and subject == default_single):
		subject = _subject_from_docs(docs)
	sender_email = cstr(sender_email).strip() or DEFAULT_SENDER_EMAIL
	sender_name = cstr(sender_name).strip() or DEFAULT_SENDER_NAME

	from printechs_digital.setup.newsletter_fields import install_newsletter_editor_fields

	install_newsletter_editor_fields()

	newsletter = frappe.new_doc("Newsletter")
	newsletter.subject = subject
	newsletter.content_type = "HTML"
	newsletter.pd_from_website_product = 1
	newsletter.pd_website_products = json.dumps([doc.name for doc in docs])
	newsletter.pd_campaign_message = ""
	newsletter.message_html = build_product_newsletter_html(docs)
	newsletter.sender_name = sender_name
	newsletter.sender_email = sender_email
	newsletter.send_unsubscribe_link = 1
	newsletter.send_webview_link = 0
	newsletter.published = 0
	newsletter.email_sent = 0
	newsletter.schedule_sending = 0
	newsletter.append("email_group", {"email_group": email_group})
	newsletter.insert()

	return {
		"name": newsletter.name,
		"subject": newsletter.subject,
		"email_group": email_group,
		"products": [doc.name for doc in docs],
	}


def refresh_unsent_drafts():
	"""Rebuild unsent product newsletters with the current email layout."""
	updated = []
	for name in frappe.get_all("Newsletter", filters={"email_sent": 0}, pluck="name"):
		newsletter = frappe.get_doc("Newsletter", name)
		body = cstr(newsletter.message_html or newsletter.message)
		docs = _docs_from_newsletter_body(body)
		if not docs:
			continue
		newsletter.pd_from_website_product = 1
		newsletter.pd_website_products = json.dumps([row.name for row in docs])
		newsletter.content_type = "HTML"
		newsletter.message_html = build_product_newsletter_html(
			docs, story_html=newsletter.get("pd_campaign_message")
		)
		newsletter.flags.ignore_permissions = True
		newsletter.save()
		updated.append(name)
	frappe.db.commit()
	return updated
