import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Articles | Printechs",
  description: "Editorial and technical resources foundation.",
});

export default function Page() {
  return (
    <StubPage
      title="Articles"
      description="Editorial and technical resources foundation."
      crumbs={[{ label: "Home", href: "/" }, { label: "Resources", href: "/resources" }, { label: "Articles" }]}
    />
  );
}
