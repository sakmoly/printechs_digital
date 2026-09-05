# Copyright (c) 2026, Printechs and contributors
"""Custom fields on Lead for website UTM / acquisition attribution."""

from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


LEAD_ATTRIBUTION_FIELDS = {
	"Lead": [
		{
			"fieldname": "website_attribution_section",
			"fieldtype": "Section Break",
			"label": "Website Attribution",
			"insert_after": "source",
			"collapsible": 1,
		},
		{
			"fieldname": "web_utm_source",
			"fieldtype": "Data",
			"label": "UTM Source",
			"insert_after": "website_attribution_section",
			"read_only": 1,
		},
		{
			"fieldname": "web_utm_medium",
			"fieldtype": "Data",
			"label": "UTM Medium",
			"insert_after": "web_utm_source",
			"read_only": 1,
		},
		{
			"fieldname": "web_utm_campaign",
			"fieldtype": "Data",
			"label": "UTM Campaign",
			"insert_after": "web_utm_medium",
			"read_only": 1,
		},
		{
			"fieldname": "web_utm_content",
			"fieldtype": "Data",
			"label": "UTM Content",
			"insert_after": "web_utm_campaign",
			"read_only": 1,
		},
		{
			"fieldname": "web_utm_term",
			"fieldtype": "Data",
			"label": "UTM Term",
			"insert_after": "web_utm_content",
			"read_only": 1,
		},
		{
			"fieldname": "web_landing_page",
			"fieldtype": "Small Text",
			"label": "Landing Page",
			"insert_after": "web_utm_term",
			"read_only": 1,
		},
		{
			"fieldname": "web_referrer",
			"fieldtype": "Small Text",
			"label": "Referrer",
			"insert_after": "web_landing_page",
			"read_only": 1,
		},
		{
			"fieldname": "web_first_visit_at",
			"fieldtype": "Datetime",
			"label": "First Website Visit",
			"insert_after": "web_referrer",
			"read_only": 1,
		},
		{
			"fieldname": "web_product_slug",
			"fieldtype": "Data",
			"label": "Product Slug",
			"insert_after": "web_first_visit_at",
			"read_only": 1,
		},
		{
			"fieldname": "web_source_url",
			"fieldtype": "Data",
			"label": "Form Page URL",
			"insert_after": "web_product_slug",
			"read_only": 1,
		},
		{
			"fieldname": "website_attribution_column",
			"fieldtype": "Column Break",
			"insert_after": "web_source_url",
		},
	]
}


def ensure_lead_attribution_fields():
	create_custom_fields(LEAD_ATTRIBUTION_FIELDS, update=True)
