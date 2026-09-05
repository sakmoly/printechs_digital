function readEnv(name: string): string | undefined {
  const value = process.env[name]?.trim();
  return value || undefined;
}

export const analyticsConfig = {
  gtmId: readEnv("NEXT_PUBLIC_GTM_ID"),
  gaMeasurementId: readEnv("NEXT_PUBLIC_GA_MEASUREMENT_ID"),
  clarityProjectId: readEnv("NEXT_PUBLIC_CLARITY_PROJECT_ID"),
  googleSiteVerification: readEnv("NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION"),
  debug: readEnv("NEXT_PUBLIC_ANALYTICS_DEBUG") === "true",
  siteUrl: (readEnv("NEXT_PUBLIC_SITE_URL") || "https://printechs.com").replace(/\/$/, ""),
  allowIndexing: readEnv("NEXT_PUBLIC_ALLOW_INDEXING") === "true",
} as const;

export function isValidGtmId(id?: string): id is string {
  return Boolean(id && /^GTM-[A-Z0-9]+$/i.test(id));
}

export function isValidClarityId(id?: string): id is string {
  return Boolean(id && /^[a-z0-9]+$/i.test(id));
}
