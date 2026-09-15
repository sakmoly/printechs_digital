import { cache } from "react";
import { siteConfig } from "@/config/site";
import { erpnextMethod } from "@/lib/erpnext-client";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

type SiteIdentity = {
  brandName?: string;
  legalName?: string;
};

export const fetchLegalName = cache(async (): Promise<string> => {
  const fromErp = await erpnextMethod<SiteIdentity>(
    "printechs_digital.api.website.get_site_identity",
    {},
    REVALIDATE_SECONDS,
  );
  const legalName = fromErp?.legalName?.trim();
  return legalName || siteConfig.legalName;
});
