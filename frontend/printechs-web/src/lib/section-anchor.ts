export function sectionAnchorId(heading: string): string {
  return heading
    .toLowerCase()
    .replace(/&/g, "")
    .replace(/[^\w\s-]/g, "")
    .trim()
    .replace(/[\s_]+/g, "-")
    .replace(/-+/g, "-");
}

/** Avoid clashing with industry blocks that share a heading (e.g. Manufacturing). */
export function coreSectionAnchorId(heading: string): string {
  return `core-${sectionAnchorId(heading)}`;
}
