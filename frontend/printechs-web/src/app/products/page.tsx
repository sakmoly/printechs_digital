import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Products | Printechs",
  description: "Representative physical product catalogue foundation — no pricing.",
});

export default function Page() {
  return (
    <StubPage
      title="Products"
      description="Representative physical product catalogue foundation — no pricing."
      crumbs={[{ label: "Home", href: "/" }, { label: "Products" }]}
    />
  );
}
