import { ContactPageView } from "@/components/contact/ContactPageView";
import { buildMetadata } from "@/lib/seo";
import { fetchContactPage } from "@/lib/contact-service";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

export async function generateMetadata() {
  const content = await fetchContactPage();
  return buildMetadata(content.seo);
}

export default async function ContactPage() {
  const content = await fetchContactPage();
  return <ContactPageView content={content} />;
}
