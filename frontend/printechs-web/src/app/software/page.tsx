import { softwareSolutions } from "@/data/software";
import { SoftwarePageView } from "@/components/software/SoftwarePageView";
import { buildMetadata } from "@/lib/seo";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

export const metadata = buildMetadata({
  title: "Software Solutions | Printechs",
  description:
    "Enterprise software platforms from Printechs — Modern POS, ERPNext, WMS, ZATCA, loyalty, and custom development.",
  canonicalPath: "/software",
});

export default function Page() {
  return <SoftwarePageView items={softwareSolutions} />;
}
