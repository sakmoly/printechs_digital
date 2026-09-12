frappe.ui.form.on("Newsletter", {
	refresh(frm) {
		const from_product = cint(frm.doc.pd_from_website_product);
		frm.toggle_display(["content_type", "message", "message_md", "message_html"], !from_product);
	},
});
