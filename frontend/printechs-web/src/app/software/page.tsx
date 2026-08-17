import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Software Solutions | Printechs",
  description: "Enterprise software platforms separate from retail hardware.",
});

export default function Page() {
  return (
    <StubPage
      title="Software Solutions"
      description="Enterprise software platforms separate from retail hardware."
      crumbs={[{ label: "Home", href: "/" }, { label: "Software" }]}
    />
  );
}
