import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "About Printechs | Printechs",
  description: "Company overview foundation.",
});

export default function Page() {
  return (
    <StubPage
      title="About Printechs"
      description="Company overview foundation."
      crumbs={[{ label: "Home", href: "/" }, { label: "Company", href: "/company" }, { label: "About" }]}
    />
  );
}
