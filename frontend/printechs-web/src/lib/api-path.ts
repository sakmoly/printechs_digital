/** Prefix API paths with Next.js basePath (e.g. /newwebsite). */
export function apiPath(path: string): string {
  const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
  return `${base}${path.startsWith("/") ? path : `/${path}`}`;
}
