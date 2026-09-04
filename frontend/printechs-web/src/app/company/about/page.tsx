import { AboutPageView } from "@/components/company/AboutPageView";
import { buildMetadata } from "@/lib/seo";
import { fetchAboutPage } from "@/lib/about-service";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

export async function generateMetadata() {
  const content = await fetchAboutPage();
  return buildMetadata(content.seo);
}

export default async function AboutPage() {
  const content = await fetchAboutPage();
  return <AboutPageView content={content} />;
}
