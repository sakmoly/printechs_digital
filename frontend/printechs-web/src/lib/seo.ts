import type { Metadata } from "next";
import { siteConfig } from "@/config/site";
import { analyticsConfig } from "@/lib/analytics/config";
import { withBasePath } from "@/lib/paths";
import type { SeoFields } from "@/types/content";

function absoluteCanonical(path?: string): string | undefined {
  if (!path) return undefined;
  const normalized = path.startsWith("/") ? path : `/${path}`;
  return `${analyticsConfig.siteUrl}${normalized}`;
}

/**
 * Demo / prototype environments are always noindex unless NEXT_PUBLIC_ALLOW_INDEXING=true.
 * At production launch on printechs.com, set allowIndexing via env and indexPage on pages.
 */
export function buildMetadata(seo?: Partial<SeoFields>): Metadata {
  const title = seo?.title ?? `${siteConfig.name} | ${siteConfig.tagline}`;
  const description = seo?.description ?? siteConfig.description;
  const indexable = Boolean(siteConfig.allowIndexing && (seo?.indexPage ?? true));
  const verification = analyticsConfig.googleSiteVerification;

  return {
    title,
    description,
    robots: indexable
      ? { index: true, follow: true }
      : { index: false, follow: false },
    verification: verification ? { google: verification } : undefined,
    twitter: {
      card: "summary_large_image",
      title: seo?.openGraphTitle ?? title,
      description: seo?.openGraphDescription ?? description,
    },
    icons: {
      icon: [
        { url: withBasePath("/icon.png"), type: "image/png", sizes: "512x512" },
        { url: withBasePath("/favicon.ico"), sizes: "any" },
      ],
      apple: [{ url: withBasePath("/apple-icon.png"), sizes: "180x180", type: "image/png" }],
      shortcut: [withBasePath("/favicon.ico")],
    },
    openGraph: {
      title: seo?.openGraphTitle ?? title,
      description: seo?.openGraphDescription ?? description,
      images: seo?.openGraphImage ? [seo.openGraphImage] : undefined,
      type: "website",
      locale: "en_SA",
      siteName: siteConfig.name,
    },
    alternates: seo?.canonicalPath
      ? { canonical: absoluteCanonical(seo.canonicalPath) }
      : undefined,
  };
}
