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
	},
});
