import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Partners | Printechs",
  description: "Technology and business partners foundation.",
});

export default function Page() {
  return (
    <StubPage
      title="Partners"
      description="Technology and business partners foundation."
      crumbs={[{ label: "Home", href: "/" }, { label: "Company", href: "/company" }, { label: "Partners" }]}
    />
  );
}
