/**
 * Product page visual theme — switch variants while design is being reviewed.
 *
 * "white-blue"  → pure white sections, blue display headings (current trial)
 * "classic"     → alternating white/mist sections, ink headings
 */
export type ProductPageThemeId = "white-blue" | "classic";

/** Change this single value to preview a different product page style. */
export const PRODUCT_PAGE_THEME: ProductPageThemeId = "white-blue";

export const productPageTheme = {
  id: PRODUCT_PAGE_THEME,
  pureWhiteBackground: PRODUCT_PAGE_THEME === "white-blue",
  blueHeadings: PRODUCT_PAGE_THEME === "white-blue",
  minimalHero: PRODUCT_PAGE_THEME === "white-blue",
} as const;

export function productHeadingClass(level: "display" | "section" | "card" = "section") {
  if (!productPageTheme.blueHeadings) {
    return level === "display"
      ? "text-ink"
      : level === "card"
        ? "text-ink"
        : "text-ink";
  }

  switch (level) {
    case "display":
      return "text-product-icon";
    case "section":
      return "text-product-icon";
    case "card":
      return "text-ink";
    default:
      return "text-product-icon";
  }
}

export function productEyebrowClass() {
  return productPageTheme.blueHeadings
    ? "text-product-icon"
    : "text-signal-deep";
}

export function productSectionTone(
  _index: number,
): "white" | "muted" {
  return productPageTheme.pureWhiteBackground ? "white" : _index % 2 === 0 ? "white" : "muted";
}
