import { CompanyPageView } from "@/components/company/CompanyPageView";
import { buildMetadata } from "@/lib/seo";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

export const metadata = buildMetadata({
  title: "Company | Printechs",
  description:
    "About Printechs, brand partners, events, and contact information across Saudi Arabia.",
  canonicalPath: "/company",
});

export default function Page() {
  return <CompanyPageView />;
}
