import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Company | Printechs",
  description: "About Printechs and partnership information.",
});

export default function Page() {
  return (
    <StubPage
      title="Company"
      description="About Printechs and partnership information."
      crumbs={[{ label: "Home", href: "/" }, { label: "Company" }]}
    />
  );
}
