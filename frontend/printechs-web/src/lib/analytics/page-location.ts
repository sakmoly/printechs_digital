import { analyticsConfig } from "@/lib/analytics/config";
import { withBasePath } from "@/lib/paths";

export function getPageLocation(pathname: string, search = ""): string {
  const path = withBasePath(pathname.startsWith("/") ? pathname : `/${pathname}`);
  return `${analyticsConfig.siteUrl}${path}${search}`;
}

export function getPageTitle(): string {
  if (typeof document === "undefined") return "";
  return document.title || "";
}
