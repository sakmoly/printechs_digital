import { notFound } from "next/navigation";
import { solutions } from "@/data/solutions";
import { resolveSolutionPage } from "@/lib/solution-service";
import { SolutionPageView } from "@/components/solutions/SolutionPageView";
import { StubPage } from "@/components/ui/StubPage";
import { buildMetadata } from "@/lib/seo";

type Props = { params: { slug: string } };

export function generateStaticParams() {
  return solutions.map((solution) => ({ slug: solution.slug }));
}

export function generateMetadata({ params }: Props) {
  const resolved = resolveSolutionPage(params.slug);

  if (resolved) {
    return buildMetadata({
      ...resolved.page.seo,
      title: resolved.page.seo.title,
      description: resolved.page.shortDescription,
    });
  }

  const title = params.slug.replace(/-/g, " ");
  return buildMetadata({
    title: `${title} | Printechs Solutions`,
    description: "Detail page foundation for solution content.",
    canonicalPath: `/solutions/${params.slug}`,
  });
}

export default function SolutionDetailPage({ params }: Props) {
  const resolved = resolveSolutionPage(params.slug);
  if (resolved) {
    return <SolutionPageView {...resolved} />;
  }

  const solution = solutions.find((item) => item.slug === params.slug);
  if (!solution) notFound();

  const title = solution.name;
  return (
    <StubPage
      title={title}
      description="Detail page foundation — full design follows homepage approval."
      crumbs={[
        { label: "Home", href: "/" },
        { label: "Solutions", href: "/solutions" },
        { label: title },
      ]}
    />
  );
}
