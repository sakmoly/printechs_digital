# Copyright (c) 2026, Printechs and contributors
"""Cross-link related CAS label printing scales."""

import frappe


CAS_PRODUCTS = {
	"RET.SYS.CAS.3035": ["RET.SYS.CAS.3036", "RET.SYS.CAS.3677", "RET.SYS.CAS.1247"],
	"RET.SYS.CAS.3036": ["RET.SYS.CAS.3035", "RET.SYS.CAS.3677"],
	"RET.SYS.CAS.3677": ["RET.SYS.CAS.3035", "RET.SYS.CAS.1247"],
	"RET.SYS.CAS.1247": ["RET.SYS.CAS.1246", "RET.SYS.CAS.3677", "RET.SYS.CAS.3035"],
	"RET.SYS.CAS.1246": ["RET.SYS.CAS.1247", "RET.SYS.CAS.3677", "RET.SYS.CAS.3035"],
}


def related_product_row(name: str, sort_order: int) -> dict | None:
	if not frappe.db.exists("Website Product", name):
		return None

	product = frappe.get_doc("Website Product", name)
	return {
		"related_website_product": name,
		"display_name_override": product.display_name,
		"summary_override": product.card_summary or product.short_description or "",
		"href": f"/products/{product.slug}",
		"image": product.card_image or product.hero_image,
		"sort_order": sort_order,
	}


def link_cas_related_products():
	for source, targets in CAS_PRODUCTS.items():
		if not frappe.db.exists("Website Product", source):
			frappe.msgprint(f"Skipping missing product {source}")
			continue

		doc = frappe.get_doc("Website Product", source)
		related = []
		for idx, target in enumerate(targets, start=1):
			row = related_product_row(target, idx)
			if row:
				related.append(row)

		doc.set("related_products", related)
		doc.save(ignore_permissions=True)
		frappe.msgprint(f"Updated related products for {source} ({len(related)} links)")

	frappe.db.commit()


if __name__ == "__main__":
	link_cas_related_products()
