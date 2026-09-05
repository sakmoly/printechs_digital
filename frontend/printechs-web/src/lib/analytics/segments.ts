import type { ProductPageContent } from "@/types/content";

export function deriveBusinessSegment(page: Pick<ProductPageContent, "productType" | "category" | "slug" | "brand">): string {
  const category = (page.category || "").toLowerCase();
  const slug = (page.slug || "").toLowerCase();
  const brand = (page.brand || "").toLowerCase();

  if (page.productType === "software") {
    if (slug.includes("erpnext") || slug.includes("erp")) return "erpnext";
    if (slug.includes("wms") || category.includes("warehouse")) return "wms";
    if (slug.includes("modern-pos") || category.includes("pos")) return "modern_pos";
    if (slug.includes("zatca")) return "software";
    if (category.includes("manufacturing")) return "manufacturing_erp";
    return "software";
  }

  if (category.includes("weigh") || slug.includes("scale")) return "weighing";
  if (category.includes("mobile") || brand.includes("datalogic") || brand.includes("zebra")) {
    return "barcode_mobility";
  }

  if (brand.includes("hitachi") || slug.includes("hitachi")) return "hitachi_cij";
  if (brand.includes("anser") || slug.includes("anser")) return "anser_tij";
  if (category.includes("laser") || slug.includes("laser")) return "laser";
  if (category.includes("case") || slug.includes("case")) return "case_coding";

  if (page.productType === "retail_hardware") return "retail";
  if (page.productType === "industrial") return "industrial";
  return page.productType || "generic";
}
