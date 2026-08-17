import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Industries | Printechs",
  description: "Industry-led entry points into Printechs capabilities.",
});

export default function Page() {
  return (
    <StubPage
      title="Industries"
      description="Industry-led entry points into Printechs capabilities."
      crumbs={[{ label: "Home", href: "/" }, { label: "Industries" }]}
    />
  );
}
