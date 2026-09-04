import type { ContactPageContent } from "@/types/content";
import { contactPageFallback } from "@/data/contact";
import { erpnextMethod } from "@/lib/erpnext-client";

export async function fetchContactPage(): Promise<ContactPageContent> {
  const fromErp = await erpnextMethod<ContactPageContent | null>(
    "printechs_digital.api.website.get_contact_page",
  );

  if (!fromErp?.offices?.length) {
    return contactPageFallback;
  }

  return {
    ...fromErp,
    specialist: {
      ...(fromErp.specialist ?? contactPageFallback.specialist),
      whatsapp:
        fromErp.specialist?.whatsapp ?? contactPageFallback.specialist.whatsapp ?? null,
    },
  };
}
