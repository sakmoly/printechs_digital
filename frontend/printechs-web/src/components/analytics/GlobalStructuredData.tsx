import { analyticsConfig } from "@/lib/analytics/config";
import { JsonLd } from "@/components/seo/JsonLd";

export function GlobalStructuredData() {
  const siteUrl = analyticsConfig.siteUrl;

  return (
    <>
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "Organization",
          name: "Printechs",
          url: siteUrl,
          logo: `${siteUrl}/icon.png`,
          contactPoint: {
            "@type": "ContactPoint",
            contactType: "sales",
            email: "info@printechs.com",
            areaServed: "SA",
            availableLanguage: ["English", "Arabic"],
          },
        }}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "WebSite",
          name: "Printechs",
          url: siteUrl,
        }}
      />
    </>
  );
}
