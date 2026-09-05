import type { MetadataRoute } from "next";
import { analyticsConfig } from "@/lib/analytics/config";
import { siteConfig } from "@/config/site";

export default async function robots(): Promise<MetadataRoute.Robots> {
  const siteUrl = analyticsConfig.siteUrl;

  if (!siteConfig.allowIndexing) {
    return {
      rules: {
        userAgent: "*",
        disallow: "/",
      },
    };
  }

  return {
    rules: {
      userAgent: "*",
      allow: "/",
      disallow: ["/api/", "/request-quote", "/request-demo"],
    },
    sitemap: `${siteUrl}/sitemap.xml`,
  };
}
