import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Solutions | Printechs",
  description: "Solution areas spanning industrial, retail and software.",
});

export default function Page() {
  return (
    <StubPage
      title="Solutions"
      description="Solution areas spanning industrial, retail and software."
      crumbs={[{ label: "Home", href: "/" }, { label: "Solutions" }]}
    />
  );
}
