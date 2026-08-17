import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

type Props = { params: { slug: string } };

export function generateMetadata({ params }: Props) {
  return buildMetadata({
    title: `${params.slug} | Printechs Industries`,
    description: "Detail page foundation for industry content.",
    canonicalPath: `/industries/${params.slug}`,
  });
}

export default function Page({ params }: Props) {
  const title = params.slug.replace(/-/g, " ");
  return (
    <StubPage
      title={title}
      description="Detail page foundation — full design follows homepage approval."
      crumbs={[
        { label: "Home", href: "/" },
        { label: "Industries", href: "/industries" },
        { label: title },
      ]}
    />
  );
}
