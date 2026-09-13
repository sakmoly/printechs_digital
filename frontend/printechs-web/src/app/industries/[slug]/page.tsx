import { notFound } from "next/navigation";
import Link from "next/link";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { ProductContentSections } from "@/components/products/ProductContentSections";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";
import { fetchIndustry, fetchIndustrySlugs } from "@/lib/industry-service";
import { fetchCatalogProducts, fetchSoftwareCatalog } from "@/lib/catalog-service";
import { fetchSolution } from "@/lib/solution-service";
import { fetchSuccessStories } from "@/lib/success-story-service";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await fetchIndustrySlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const industry = await fetchIndustry(params.slug);
  if (!industry) {
    return buildMetadata({
      title: "Industry | Printechs",
      description: "Industry solutions from Printechs.",
    });
  }
  return buildMetadata(industry.seo);
}

export default async function IndustryDetailPage({ params }: Props) {
  const industry = await fetchIndustry(params.slug);
  if (!industry) notFound();

  const stories = await fetchSuccessStories({ industry: industry.slug });
  const relatedSolutionSlugs = industry.relatedSolutionSlugs ?? [];
  const relatedProductSlugs = industry.relatedProductSlugs ?? [];
  const relatedSoftwareSlugs = industry.relatedSoftwareSlugs ?? [];
  const overview = industry.overview || industry.summary;
  const contentSections = industry.contentSections ?? [];

  const [catalog, software, relatedSolutions] = await Promise.all([
    relatedProductSlugs.length ? fetchCatalogProducts() : Promise.resolve([]),
    relatedSoftwareSlugs.length ? fetchSoftwareCatalog() : Promise.resolve([]),
    Promise.all(relatedSolutionSlugs.map((slug) => fetchSolution(slug))),
  ]);

  const relatedProducts = relatedProductSlugs
    .map((slug) => catalog.find((product) => product.slug === slug))
    .filter((product): product is NonNullable<typeof product> => Boolean(product));
  const relatedSoftware = relatedSoftwareSlugs
    .map((slug) => software.find((item) => item.slug === slug))
    .filter((item): item is NonNullable<typeof item> => Boolean(item));
  const solutions = relatedSolutions.filter((item): item is NonNullable<typeof item> => Boolean(item));

  return (
    <>
      <PageIntro
        title={industry.name}
        description={industry.summary}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Industries", href: "/industries" },
          { label: industry.name },
        ]}
      />
      <Section tone="white">
        <div className="grid gap-8 lg:grid-cols-2 lg:items-start">
          <ImageFrame
            src={industry.image.src}
            alt={industry.image.alt}
            spec={IMAGE_SPECS.industry}
            fill
            className="aspect-[3/2]"
            imageClassName="object-cover"
            sizes="(max-width: 1024px) 100vw, 50vw"
          />
          <div>
            <div className="space-y-4 text-base leading-relaxed text-slate">
              {overview.split("\n\n").map((paragraph) => (
                <p key={paragraph.slice(0, 48)}>{paragraph}</p>
              ))}
            </div>
            <div className="mt-8 flex flex-wrap gap-3">
              {stories.stories.length ? (
                <Button href={`/success-stories?industry=${industry.slug}`} variant="ghost">
                  Success Stories
                </Button>
              ) : null}
              <Button href="/contact" variant="primary">
                Talk to a Specialist
              </Button>
              <Button href="/request-quote" variant="ghost">
                Request a Quote
              </Button>
            </div>
          </div>
        </div>
      </Section>
      {contentSections.length ? (
        <Section tone="muted">
          <ProductContentSections sections={contentSections} eyebrow="Industry solutions" />
        </Section>
      ) : null}
      {relatedProducts.length ? (
        <Section tone="white">
          <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
            Products for this industry
          </h2>
          <div className="mt-8">
            <FeatureGrid columns={3}>
              {relatedProducts.map((product) => (
                <Card
                  key={product.id}
                  href={`/products/${product.slug}`}
                  title={product.name}
                  description={product.summary}
                  meta={product.brand}
                  cta="View product"
                  media={
                    <ImageFrame
                      src={product.image.src}
                      alt={product.image.alt}
                      spec={IMAGE_SPECS.product}
                      fill
                      className="aspect-square bg-mist"
                      imageClassName="object-contain p-6"
                      sizes="(max-width: 768px) 100vw, 33vw"
                    />
                  }
                />
              ))}
            </FeatureGrid>
          </div>
        </Section>
      ) : null}
      {solutions.length || relatedSoftware.length ? (
        <Section tone={relatedProducts.length ? "muted" : "white"}>
          <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
            Related capabilities
          </h2>
          <div className="mt-6 grid gap-6 sm:grid-cols-2">
            {solutions.length ? (
              <RelatedList
                title="Solutions"
                items={solutions.map((item) => ({
                  href: item.href || `/solutions/${item.slug}`,
                  label: item.name,
                }))}
              />
            ) : null}
            {relatedSoftware.length ? (
              <RelatedList
                title="Software"
                items={relatedSoftware.map((item) => ({
                  href: `/software/${item.slug}`,
                  label: item.name,
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
