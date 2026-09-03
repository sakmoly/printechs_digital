import { notFound } from "next/navigation";
import Link from "next/link";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";
import { fetchIndustry, fetchIndustrySlugs } from "@/lib/industry-service";
import { fetchSuccessStories } from "@/lib/success-story-service";

export const revalidate = 60;

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

function slugLabel(slug: string) {
  return slug.replace(/-/g, " ").replace(/\b\w/g, (char) => char.toUpperCase());
}

export default async function IndustryDetailPage({ params }: Props) {
  const industry = await fetchIndustry(params.slug);
  if (!industry) notFound();

  const stories = await fetchSuccessStories({ industry: industry.slug });
  const relatedSolutions = industry.relatedSolutionSlugs ?? [];
  const relatedProducts = industry.relatedProductSlugs ?? [];
  const relatedSoftware = industry.relatedSoftwareSlugs ?? [];

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
            <p className="text-base leading-relaxed text-slate">{industry.summary}</p>
            <div className="mt-8 flex flex-wrap gap-3">
              {stories.stories.length ? (
                <Button href={`/success-stories?industry=${industry.slug}`} variant="ghost">
                  Success Stories
                </Button>
              ) : null}
              <Button href="/contact" variant="primary">
                Talk to a Specialist
              </Button>
            </div>
          </div>
        </div>
      </Section>
      {relatedSolutions.length || relatedProducts.length || relatedSoftware.length ? (
        <Section tone="muted">
          <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
            Related capabilities
          </h2>
          <div className="mt-6 grid gap-6 sm:grid-cols-3">
            {relatedSolutions.length ? (
              <RelatedList
                title="Solutions"
                items={relatedSolutions.map((slug) => ({
                  href: `/solutions/${slug}`,
                  label: slugLabel(slug),
                }))}
              />
            ) : null}
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
