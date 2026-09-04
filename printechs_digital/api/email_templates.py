# Copyright (c) 2026, Printechs and contributors

from frappe.utils import cstr, escape_html, get_url


def _esc(value) -> str:
	return escape_html(cstr(value or "").strip())


def _configuration_rows(configuration: str) -> list[tuple[str, str]]:
	rows = []
	for line in cstr(configuration or "").splitlines():
		line = line.strip()
		if not line or line == "Configuration":
			continue
		if ": " in line:
			label, value = line.split(": ", 1)
			rows.append((label.strip(), value.strip()))
		else:
			rows.append((line, ""))
	return rows


def _section_heading(title: str) -> str:
	return (
		f'<p style="margin:28px 0 10px;font-size:11px;font-weight:700;'
		f'letter-spacing:0.14em;text-transform:uppercase;color:#1a7f4b;">'
		f"{_esc(title)}</p>"
	)


def _detail_table(rows: list[tuple[str, str]]) -> str:
	if not rows:
		return ""
	cells = []
	for label, value in rows:
		cells.append(
			f'<tr>'
			f'<td style="padding:10px 12px;border-bottom:1px solid #e8edf2;width:38%;'
			f'font-size:13px;font-weight:600;color:#475569;vertical-align:top;">{_esc(label)}</td>'
		 f'<td style="padding:10px 12px;border-bottom:1px solid #e8edf2;font-size:14px;'
			f'color:#0f172a;vertical-align:top;">{_esc(value or "—")}</td>'
			f"</tr>"
		)
	return (
		f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
		f'style="border:1px solid #e2e8f0;border-radius:6px;border-collapse:separate;'
		f'overflow:hidden;background:#ffffff;">'
		f"{''.join(cells)}"
		f"</table>"
	)


def _paragraph(text: str) -> str:
	return (
		f'<p style="margin:0;font-size:15px;line-height:1.65;color:#334155;">'
		f"{_esc(text)}</p>"
	)


def _button(label: str, href: str) -> str:
	return (
		f'<a href="{_esc(href)}" style="display:inline-block;margin-top:20px;padding:12px 20px;'
		f'background:#1a7f4b;color:#ffffff;text-decoration:none;border-radius:4px;'
		f'font-size:14px;font-weight:600;">{_esc(label)}</a>'
	)


def _email_shell(eyebrow: str, title: str, intro: str, body_html: str) -> str:
	return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{_esc(title)}</title>
</head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:Arial,Helvetica,sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f1f5f9;padding:24px 12px;">
    <tr>
      <td align="center">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:620px;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden;">
          <tr>
            <td style="background:#0f172a;padding:18px 24px;">
              <p style="margin:0;font-size:18px;font-weight:700;color:#ffffff;letter-spacing:0.02em;">Printechs</p>
              <p style="margin:6px 0 0;font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:#86efac;">{_esc(eyebrow)}</p>
            </td>
          </tr>
          <tr>
            <td style="padding:28px 24px 8px;">
              <h1 style="margin:0;font-size:24px;line-height:1.3;color:#0f172a;">{_esc(title)}</h1>
              <p style="margin:12px 0 0;font-size:15px;line-height:1.65;color:#475569;">{_esc(intro)}</p>
            </td>
          </tr>
          <tr>
            <td style="padding:8px 24px 28px;">
              {body_html}
            </td>
          </tr>
          <tr>
            <td style="padding:16px 24px;background:#f8fafc;border-top:1px solid #e2e8f0;">
              <p style="margin:0;font-size:12px;line-height:1.6;color:#64748b;">
                Printechs · Industrial coding, retail technology and enterprise software · Saudi Arabia
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""


def demo_sales_notification_html(lead, context: dict, message: str) -> str:
	product = _esc(context.get("product")) or "Software demo"
	configuration = context.get("configuration") or ""
	if configuration.startswith("Configuration\n"):
		configuration = configuration[len("Configuration\n") :]

	contact_rows = [
		("Name", lead.lead_name),
		("Company", lead.company_name or "—"),
		("Email", lead.email_id),
		("Phone", lead.mobile_no or "—"),
		("Lead", lead.name),
		("Product", product),
	]
	if context.get("sourceUrl"):
		contact_rows.append(("Source page", context.get("sourceUrl")))

	body_parts = [_section_heading("Contact"), _detail_table(contact_rows)]

	config_rows = _configuration_rows(configuration)
	if config_rows:
		body_parts.extend([_section_heading("Demo requirements"), _detail_table(config_rows)])

	if context.get("preferredTime"):
		body_parts.extend(
			[
				_section_heading("Preferred demo time"),
				f'<div style="padding:14px 16px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;">'
				f'{_paragraph(context.get("preferredTime"))}'
				f"</div>",
			]
		)

	if message:
		body_parts.extend(
			[
				_section_heading("Additional notes"),
				f'<div style="padding:14px 16px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;">'
				f'{_paragraph(message)}'
				f"</div>",
			]
		)

	lead_url = get_url(f"/app/lead/{lead.name}")
	body_parts.append(_button("Open lead in ERPNext", lead_url))

	return _email_shell(
		eyebrow="Website demo request",
		title=f"New demo request — {product}",
		intro="A visitor submitted a software demo request from the website.",
		body_html="".join(body_parts),
	)


def demo_customer_confirmation_html(lead, product: str) -> str:
	body = (
		f'<p style="margin:0 0 14px;font-size:15px;line-height:1.65;color:#334155;">'
		f"Dear {_esc(lead.lead_name)},"
		f"</p>"
		f'<p style="margin:0 0 14px;font-size:15px;line-height:1.65;color:#334155;">'
		f"Thank you for requesting a demonstration of <strong>{_esc(product)}</strong>. "
		f"We have received your details and our software team will contact you to schedule a session."
		f"</p>"
		f'<p style="margin:0;font-size:14px;line-height:1.65;color:#64748b;">'
		f"Business hours: Sunday–Thursday, 9:00 AM – 6:00 PM (AST)."
		f"</p>"
	)
	return _email_shell(
		eyebrow="Demo request received",
		title="We received your demo request",
		intro="Your request is with the Printechs software team.",
		body_html=body,
	)


def demo_sales_notification_text(lead, context: dict, message: str) -> str:
	product = _esc(context.get("product")) or "Software demo"
	configuration = context.get("configuration") or ""
	if configuration.startswith("Configuration\n"):
		configuration = configuration[len("Configuration\n") :]

	lines = [
		f"New demo request — {product}",
		"",
		"CONTACT",
		f"Name: {lead.lead_name}",
		f"Company: {lead.company_name or '-'}",
		f"Email: {lead.email_id}",
		f"Phone: {lead.mobile_no or '-'}",
		f"Lead: {lead.name}",
	]
	if configuration:
		lines.extend(["", "DEMO REQUIREMENTS", configuration])
	if context.get("preferredTime"):
		lines.extend(["", "PREFERRED DEMO TIME", context.get("preferredTime")])
	if message:
		lines.extend(["", "ADDITIONAL NOTES", message])
	lines.extend(["", f"Open in ERPNext: {get_url(f'/app/lead/{lead.name}')}"])
	return "\n".join(lines)
