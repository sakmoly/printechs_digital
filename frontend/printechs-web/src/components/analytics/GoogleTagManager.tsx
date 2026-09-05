import Script from "next/script";
import { analyticsConfig, isValidGtmId } from "@/lib/analytics/config";

export function GoogleTagManager() {
  const gtmId = analyticsConfig.gtmId;
  if (!isValidGtmId(gtmId)) return null;

  return (
    <>
      <Script id="gtm-init" strategy="afterInteractive">
        {`
          window.dataLayer = window.dataLayer || [];
          window.dataLayer.push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
        `}
      </Script>
      <Script
        id="gtm-script"
        strategy="afterInteractive"
        src={`https://www.googletagmanager.com/gtm.js?id=${gtmId}`}
      />
      <noscript>
        <iframe
          src={`https://www.googletagmanager.com/ns.html?id=${gtmId}`}
          height="0"
          width="0"
          style={{ display: "none", visibility: "hidden" }}
          title="Google Tag Manager"
        />
      </noscript>
    </>
  );
}
