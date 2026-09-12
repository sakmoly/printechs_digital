# Copyright (c) 2026, Printechs and contributors
"""Custom Newsletter fields for the optional campaign message editor."""

from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def install_newsletter_editor_fields():
	create_custom_fields(
		{
			"Newsletter": [
				{
					"fieldname": "pd_from_website_product",
					"label": "From Website Product",
					"fieldtype": "Check",
					"default": "0",
					"hidden": 1,
					"insert_after": "subject",
				},
				{
					"fieldname": "pd_website_products",
					"label": "Website Products",
					"fieldtype": "Small Text",
					"hidden": 1,
					"insert_after": "pd_from_website_product",
				},
				{
					"fieldname": "pd_campaign_message",
					"label": "Email Message",
					"fieldtype": "Text Editor",
					"insert_after": "pd_website_products",
					"depends_on": "eval:doc.pd_from_website_product",
					"description": (
						"Optional. This message appears above the products. "
						"Leave it blank to send the products only. "
						"The email layout updates when you save."
					),
				},
			]
		},
		update=True,
	)
