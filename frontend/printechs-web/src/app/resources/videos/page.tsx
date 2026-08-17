import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Videos | Printechs",
  description: "Marketing and demonstration video library foundation.",
});

export default function Page() {
  return (
    <StubPage
      title="Videos"
      description="Marketing and demonstration video library foundation."
      crumbs={[{ label: "Home", href: "/" }, { label: "Resources", href: "/resources" }, { label: "Videos" }]}
    />
  );
}
