import type { MetadataRoute } from "next";
import { analyticsConfig } from "@/lib/analytics/config";
import { fetchPublishedProductSlugs, fetchSoftwareCatalog } from "@/lib/catalog-service";
import { industries } from "@/data/industries";
import { solutions } from "@/data/solutions";
import { solutionPages } from "@/data/solution-pages";
import { brands } from "@/data/brands";
import { caseStudies } from "@/data/case-studies";

const staticRoutes = [
  "/",
  "/products",
  "/software",
  "/solutions",
  "/industries",
  "/brands",
  "/success-stories",
  "/contact",
  "/company/about",
  "/company/events",
  "/request-quote",
  "/request-demo",
];

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const siteUrl = analyticsConfig.siteUrl;
  const now = new Date();

  const productSlugs = await fetchPublishedProductSlugs();
  const softwareCatalog = await fetchSoftwareCatalog();
  const softwareSlugs = new Set(softwareCatalog.map((item) => item.slug));

  const productRoutes = productSlugs
    .filter((slug) => !softwareSlugs.has(slug))
    .map((slug) => `/products/${slug}`);

  const softwareRoutes = Array.from(softwareSlugs).map((slug) => `/software/${slug}`);

  const solutionRoutes = Array.from(
    new Set([
      ...solutions.map((item) => item.slug),
      ...Object.values(solutionPages).map((item) => item.slug),
    ]),
  ).map((slug) => `/solutions/${slug}`);

  const industryRoutes = industries.map((item) => `/industries/${item.slug}`);
  const brandRoutes = brands.map((item) => `/brands/${item.slug}`);
  const storyRoutes = caseStudies.map((item) => `/success-stories/${item.slug}`);

  const allRoutes = [
    ...staticRoutes,
    ...productRoutes,
    ...softwareRoutes,
    ...solutionRoutes,
    ...industryRoutes,
    ...brandRoutes,
    ...storyRoutes,
  ];

  return allRoutes.map((path) => ({
    url: `${siteUrl}${path}`,
    lastModified: now,
    changeFrequency: path === "/" ? "weekly" : "monthly",
    priority: path === "/" ? 1 : path.split("/").length <= 2 ? 0.8 : 0.6,
  }));
}
