import type { AboutPageContent } from "@/types/content";
import { aboutPageFallback } from "@/data/about";
import { erpnextMethod, resolvePublicAssetUrl } from "@/lib/erpnext-client";

export async function fetchAboutPage(): Promise<AboutPageContent> {
  const fromErp = await erpnextMethod<AboutPageContent | null>(
    "printechs_digital.api.website.get_about_page",
  );

  if (!fromErp?.paragraphs?.length) {
    return aboutPageFallback;
  }

  return {
    ...fromErp,
    profileDownload: fromErp.profileDownload
      ? {
          ...fromErp.profileDownload,
          href:
            resolvePublicAssetUrl(fromErp.profileDownload.href) ??
            fromErp.profileDownload.href,
        }
      : null,
  };
}
