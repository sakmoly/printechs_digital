frappe.ui.form.on("Item", {
	refresh(frm) {
		if (frm.doc.__islocal) {
			return;
		}

		addDigitalWebsiteButtons(frm);
	},
});

function addDigitalWebsiteButtons(frm) {
	frappe.db
		.get_value("Website Product", { item: frm.doc.name }, "name")
		.then((r) => {
			const website_product = r.message?.name;
			if (website_product) {
				frm.add_custom_button(__("View Website Product"), () => {
					frappe.set_route("Form", "Website Product", website_product);
				});
			} else {
				frm.add_custom_button(__("Create Website Product"), () => {
					createWebsiteProduct(frm);
				});
			}
		})
		.catch(() => {
			frm.add_custom_button(__("Create Website Product"), () => {
				createWebsiteProduct(frm);
			});
		});
}

function createWebsiteProduct(frm) {
	frappe.call({
		method:
			"printechs_digital.printechs_digital.doctype.website_product.website_product.make_website_product",
		args: { doc: frm.doc },
		freeze: true,
		freeze_message: __("Creating Website Product..."),
		callback(result) {
			if (!result.message) {
				return;
			}

			const [name, title] = result.message;
			frappe.msgprint({
				message: __(
					"Website Product {0} has been created.",
					[
						repl(
							'<a href="/app/website-product/{item_encoded}" class="strong">{item}</a>',
							{
								item_encoded: encodeURIComponent(name),
								item: title,
							},
						),
					],
				),
				title: __("Created"),
				indicator: "green",
			});
			frappe.set_route("Form", "Website Product", name);
		},
	});
}
