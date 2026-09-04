# Copyright (c) 2026, Printechs and contributors

DEFAULT_PAGE_SECTION_ORDER = [
	"benefits",
	"overview",
	"product_tour",
	"icon_specifications",
	"capability_modules",
	"software_capabilities",
	"applications",
	"content_sections",
	"ecosystem",
	"support",
	"downloads",
	"related_products",
	"faqs",
]

PAGE_SECTION_LABELS = {
	"benefits": "Benefits",
	"overview": "Product Overview",
	"product_tour": "Product Tour / Visual Story",
	"icon_specifications": "Technical Highlights",
	"capability_modules": "Platform Modules",
	"software_capabilities": "Software Capabilities",
	"applications": "Applications",
	"content_sections": "Content Sections",
	"ecosystem": "Ecosystem",
	"support": "Support & Services",
	"downloads": "Downloads & Package",
	"related_products": "Related Products",
	"faqs": "FAQ",
}

PAGE_SECTION_SELECT_OPTIONS = "\n".join(DEFAULT_PAGE_SECTION_ORDER)


def default_page_section_order_rows() -> list[dict]:
	return [
		{"section": section, "sort_order": index + 1}
		for index, section in enumerate(DEFAULT_PAGE_SECTION_ORDER)
	]
