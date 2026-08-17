import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Contact | Printechs",
  description: "Talk to a Printechs specialist.",
});

export default function Page() {
  return (
    <StubPage
      title="Contact"
      description="Talk to a Printechs specialist."
      crumbs={[{ label: "Home", href: "/" }, { label: "Contact" }]}
    />
  );
}
