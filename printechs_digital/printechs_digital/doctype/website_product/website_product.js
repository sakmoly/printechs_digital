frappe.ui.form.on("Website Product", {
	refresh(frm) {
		if (frm.doc.slug && frm.doc.published) {
			const base =
				frm.doc.product_type === "Software"
					? "/newwebsite/software/"
					: "/newwebsite/products/";
			frm.add_custom_button(__("Preview on Website"), () => {
				window.open(`${base}${frm.doc.slug}`, "_blank");
			});
		}

		if (frm.doc.item && !frm.doc.__islocal) {
			frm.add_custom_button(__("Open Item"), () => {
				frappe.set_route("Form", "Item", frm.doc.item);
			});
		}

		if (!frm.is_new() && frm.doc.slug) {
			frm.add_custom_button(__("Create Newsletter"), () => {
				const default_subject = `${frm.doc.display_name || frm.doc.website_product_name} | Printechs`;
				const dialog = new frappe.ui.Dialog({
					title: __("Create Newsletter"),
					fields: [
						{
							fieldname: "email_group",
							fieldtype: "Link",
							options: "Email Group",
							label: __("Email Group"),
							reqd: 1,
							default: "Printechs-Staff",
							description: __(
								"Draft only — nothing is sent. Add more products below to include them in the same email.",
							),
						},
						{
							fieldname: "subject",
							fieldtype: "Small Text",
							label: __("Subject"),
							reqd: 1,
							default: default_subject,
						},
						{
							fieldname: "extra_products",
							fieldtype: "Table",
							label: __("Also include"),
							description: __("Optional. Add more Website Products to include them in the same email."),
							cannot_add_rows: false,
							in_place_edit: true,
							data: [],
							fields: [
								{
									fieldname: "website_product",
									fieldtype: "Link",
									options: "Website Product",
									in_list_view: 1,
									reqd: 1,
									label: __("Website Product"),
									get_query() {
										return {
											filters: {
												published: 1,
												name: ["!=", frm.doc.name],
											},
										};
									},
								},
							],
						},
					],
					primary_action_label: __("Create Draft"),
					primary_action(values) {
						const extras = (values.extra_products || [])
							.map((row) => row.website_product)
							.filter(Boolean);
						dialog.hide();
						frappe.call({
							method: "printechs_digital.api.product_newsletter.create_from_website_product",
							args: {
								website_product: frm.doc.name,
								email_group: values.email_group,
								subject: values.subject,
								extra_products: extras,
							},
							freeze: true,
							freeze_message: __("Creating draft newsletter…"),
							callback(r) {
								if (!r.message || !r.message.name) {
									return;
								}
								frappe.show_alert({
									message: __("Draft newsletter created. Review the design, then send."),
									indicator: "green",
								});
								frappe.set_route("Form", "Newsletter", r.message.name);
							},
						});
					},
				});
				dialog.show();
			});
		}
	},
});
