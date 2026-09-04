import { notFound } from "next/navigation";
import Link from "next/link";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { ImageFrame } from "@/components/media/ImageFrame";
import { SolutionPageView } from "@/components/solutions/SolutionPageView";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";
import {
  fetchSolution,
  fetchSolutionSlugs,
  resolveSolutionPage,
} from "@/lib/solution-service";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await fetchSolutionSlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const resolved = resolveSolutionPage(params.slug);
  if (resolved) {
    return buildMetadata({
      ...resolved.page.seo,
      title: resolved.page.seo.title,
      description: resolved.page.shortDescription,
    });
  }

  const solution = await fetchSolution(params.slug);
  if (solution) {
    return buildMetadata(solution.seo);
  }

  return buildMetadata({
    title: "Solution | Printechs",
    description: "Solution detail from Printechs.",
  });
}

function slugLabel(slug: string) {
  return slug.replace(/-/g, " ").replace(/\b\w/g, (char) => char.toUpperCase());
}

export default async function SolutionDetailPage({ params }: Props) {
  const resolved = resolveSolutionPage(params.slug);
  if (resolved) {
    return <SolutionPageView {...resolved} />;
  }

  const solution = await fetchSolution(params.slug);
  if (!solution) notFound();

  const relatedProducts = solution.relatedProductSlugs ?? [];
  const relatedSoftware = solution.relatedSoftwareSlugs ?? [];

  return (
    <>
      <PageIntro
        title={solution.name}
        description={solution.summary}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Solutions", href: "/solutions" },
          { label: solution.name },
        ]}
      />
      <Section tone="white">
        <div className="grid gap-8 lg:grid-cols-2 lg:items-start">
          <ImageFrame
            src={solution.image.src}
            alt={solution.image.alt}
            spec={IMAGE_SPECS.solution}
            fill
            className="aspect-[16/10]"
            imageClassName="object-cover"
            sizes="(max-width: 1024px) 100vw, 50vw"
          />
          <div>
            <p className="text-base leading-relaxed text-slate">{solution.summary}</p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Button href="/contact" variant="primary">
                Talk to a Specialist
              </Button>
              <Button href="/request-quote" variant="ghost">
                Request Quote
              </Button>
            </div>
          </div>
        </div>
      </Section>
      {relatedProducts.length || relatedSoftware.length ? (
        <Section tone="muted">
          <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
            Related capabilities
          </h2>
          <div className="mt-6 grid gap-6 sm:grid-cols-2">
            {relatedProducts.length ? (
              <RelatedList
                title="Products"
                items={relatedProducts.map((slug) => ({
                  href: `/products/${slug}`,
                  label: slugLabel(slug),
                }))}
              />
            ) : null}
            {relatedSoftware.length ? (
              <RelatedList
                title="Software"
                items={relatedSoftware.map((slug) => ({
                  href: `/software/${slug}`,
                  label: slugLabel(slug),
                }))}
              />
            ) : null}
          </div>
        </Section>
      ) : null}
    </>
  );
}

function RelatedList({
  title,
  items,
}: {
  title: string;
  items: { href: string; label: string }[];
}) {
  return (
    <div>
      <p className="text-[0.7rem] font-semibold uppercase tracking-[0.2em] text-signal-deep">
        {title}
      </p>
      <ul className="mt-3 space-y-2">
        {items.map((item) => (
          <li key={item.href}>
            <Link
              href={item.href}
              className="text-sm font-semibold text-ink underline-offset-4 hover:text-signal-deep hover:underline"
            >
              {item.label}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
