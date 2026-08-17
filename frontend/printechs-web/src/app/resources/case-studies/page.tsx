import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Case Studies | Printechs",
  description: "Customer outcome stories foundation.",
});

export default function Page() {
  return (
    <StubPage
      title="Case Studies"
      description="Customer outcome stories foundation."
      crumbs={[{ label: "Home", href: "/" }, { label: "Resources", href: "/resources" }, { label: "Case Studies" }]}
    />
  );
}
