import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Resources | Printechs",
  description: "Videos, case studies and articles.",
});

export default function Page() {
  return (
    <StubPage
      title="Resources"
      description="Videos, case studies and articles."
      crumbs={[{ label: "Home", href: "/" }, { label: "Resources" }]}
    />
  );
}
