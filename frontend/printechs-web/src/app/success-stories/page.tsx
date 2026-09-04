import Link from "next/link";
import { Section } from "@/components/ui/Section";
import { Container } from "@/components/ui/Container";
import { Breadcrumb } from "@/components/ui/Breadcrumb";
import { SuccessStoryAccordion } from "@/components/stories/SuccessStoryAccordion";
import { buildMetadata } from "@/lib/seo";
import { fetchSuccessStories } from "@/lib/success-story-service";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type SearchParams = {
  product?: string;
  brand?: string;
  industry?: string;
};

function filterHref(next: SearchParams) {
  const params = new URLSearchParams();
  if (next.product) params.set("product", next.product);
  if (next.brand) params.set("brand", next.brand);
  if (next.industry) params.set("industry", next.industry);
  const query = params.toString();
  return query ? `/success-stories?${query}` : "/success-stories";
}

function FilterChip({
  href,
  label,
  active,
}: {
  href: string;
  label: string;
  active: boolean;
}) {
  return (
    <Link
      href={href}
      className={
        active
          ? "rounded-sm bg-signal px-3 py-1.5 text-sm font-semibold text-white"
          : "rounded-sm border border-line bg-white px-3 py-1.5 text-sm font-semibold text-slate hover:border-line-strong hover:text-ink"
      }
    >
      {label}
    </Link>
  );
}

export async function generateMetadata({
  searchParams,
}: {
  searchParams: SearchParams;
}) {
  const suffix = searchParams.brand
    ? ` for ${searchParams.brand}`
    : searchParams.industry
      ? ` in ${searchParams.industry}`
      : "";
  return buildMetadata({
    title: `Success Stories${suffix} | Printechs`,
    description:
      "Installation and customer success stories from Printechs across Saudi Arabia.",
    canonicalPath: "/success-stories",
  });
}

export default async function SuccessStoriesPage({
  searchParams,
}: {
  searchParams: SearchParams;
}) {
  const { stories, brands, industries } = await fetchSuccessStories({
    product: searchParams.product,
    brand: searchParams.brand,
    industry: searchParams.industry,
  });

  const productName = stories.find((story) => story.productName)?.productName;
  const brandName =
    brands.find((item) => item.slug === searchParams.brand)?.name ?? searchParams.brand;
  const industryName =
    industries.find((item) => item.slug === searchParams.industry)?.name ??
    searchParams.industry;

  const filteredHeading = searchParams.product
    ? `${productName || "Product"} stories`
    : searchParams.brand
      ? `${brandName} stories`
      : searchParams.industry
        ? `${industryName} stories`
        : null;

  const showBrandFilters = brands.length > 1 || Boolean(searchParams.brand);
  const showIndustryFilters = industries.length > 1 || Boolean(searchParams.industry);

  return (
    <>
      <section className="border-b border-ink/10 bg-mist py-6 sm:py-8">
        <Container>
          <Breadcrumb
            className="mb-3"
            items={[
              { label: "Home", href: "/" },
              { label: "Success Stories" },
            ]}
          />
          <h1 className="font-display text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
            Success Stories
          </h1>
          <p className="mt-2 max-w-2xl text-sm leading-relaxed text-slate sm:text-base">
            {filteredHeading
              ? filteredHeading
              : "Customer installations across Saudi Arabia."}
          </p>
        </Container>
      </section>

      <Section tone="white" pad="compact">
        {showBrandFilters || showIndustryFilters ? (
          <div className="mb-8 flex flex-col gap-3 sm:flex-row sm:flex-wrap sm:items-center">
            {showBrandFilters ? (
              <div className="flex flex-wrap items-center gap-2">
                <FilterChip
                  href={filterHref({ industry: searchParams.industry })}
                  label="All brands"
                  active={!searchParams.brand && !searchParams.product}
                />
                {brands.map((brand) => (
                  <FilterChip
                    key={brand.slug}
                    href={filterHref({
                      brand: brand.slug,
                      industry: searchParams.industry,
                    })}
                    label={brand.name}
                    active={searchParams.brand === brand.slug}
                  />
                ))}
              </div>
            ) : null}
            {showIndustryFilters ? (
              <div className="flex flex-wrap items-center gap-2">
                <FilterChip
                  href={filterHref({ brand: searchParams.brand })}
                  label="All industries"
                  active={!searchParams.industry}
                />
                {industries.map((industry) => (
                  <FilterChip
                    key={industry.slug}
                    href={filterHref({
                      brand: searchParams.brand,
                      industry: industry.slug,
                    })}
                    label={industry.name}
                    active={searchParams.industry === industry.slug}
                  />
                ))}
              </div>
            ) : null}
          </div>
        ) : null}

        {stories.length > 0 ? (
          <SuccessStoryAccordion stories={stories} />
        ) : (
          <div className="rounded-sm border border-line bg-mist p-8">
            <p className="text-base text-slate">
              Success stories will appear here as technicians publish
              installations from the field.
            </p>
            {searchParams.product || searchParams.brand || searchParams.industry ? (
              <Link
                href="/success-stories"
                className="mt-4 inline-flex text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
              >
                View all success stories
              </Link>
            ) : null}
          </div>
        )}
      </Section>
    </>
  );
}
