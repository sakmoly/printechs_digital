import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Request Demo | Printechs",
  description: "Demo request interface foundation — mockup only.",
});

export default function Page() {
  return (
    <StubPage
      title="Request Demo"
      description="Demo request interface foundation — mockup only."
      crumbs={[{ label: "Home", href: "/" }, { label: "Request Demo" }]}
    />
  );
}
