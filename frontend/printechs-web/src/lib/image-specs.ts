export type ImageSpec = {
  /** Display label for designers, e.g. "1200 × 800" */
  label: string;
  /** Optional aspect ratio hint */
  ratio?: string;
};

/** Recommended export sizes for homepage and listing imagery. */
export const IMAGE_SPECS = {
  hero: { label: "1920 × 1080", ratio: "16:9" },
  division: { label: "1200 × 900", ratio: "4:3" },
  product: { label: "1200 × 1200", ratio: "1:1" },
  software: { label: "1600 × 1000", ratio: "16:10" },
  solution: { label: "1600 × 1000", ratio: "16:10" },
  industry: { label: "1200 × 800", ratio: "3:2" },
  caseStudy: { label: "1600 × 900", ratio: "16:9" },
  videoPoster: { label: "1920 × 1080", ratio: "16:9" },
  brandLogo: { label: "400 × 160", ratio: "PNG · transparent" },
} as const satisfies Record<string, ImageSpec>;

export function isPlaceholderAsset(src: string): boolean {
  return src.includes("/placeholders/") || src.endsWith(".svg");
}

export function shouldShowImageSizeLabel(
  src: string,
  showSizeLabel?: boolean,
): boolean {
  if (showSizeLabel === false) return false;
  if (showSizeLabel === true) return true;
  return isPlaceholderAsset(src);
}
