/**
 * Prefix public asset paths for the current Next.js basePath.
 * Keep content data paths as root-relative (/images/...) and resolve here.
 */
export function withBasePath(path: string): string {
  if (!path || path.startsWith("http://") || path.startsWith("https://")) {
    return path;
  }

  const base = process.env.NEXT_PUBLIC_BASE_PATH || "";
  if (!base) return path;
  if (path.startsWith(base + "/") || path === base) return path;
  return `${base}${path.startsWith("/") ? path : `/${path}`}`;
}
