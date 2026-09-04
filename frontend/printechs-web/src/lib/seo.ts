import type { Metadata } from "next";
import { siteConfig } from "@/config/site";
import { withBasePath } from "@/lib/paths";
import type { SeoFields } from "@/types/content";

/**
 * Demo / prototype environments are always noindex.
 * When production indexing is enabled later, flip siteConfig.allowIndexing
 * and pass indexPage: true on approved pages only.
 */
export function buildMetadata(seo?: Partial<SeoFields>): Metadata {
  const title = seo?.title ?? `${siteConfig.name} | ${siteConfig.tagline}`;
  const description = seo?.description ?? siteConfig.description;
  const indexable = Boolean(siteConfig.allowIndexing && seo?.indexPage);

  return {
    title,
    description,
    robots: indexable
      ? { index: true, follow: true }
      : { index: false, follow: false },
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
      ? { canonical: seo.canonicalPath }
      : undefined,
  };
}
