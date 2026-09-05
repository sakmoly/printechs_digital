import type { ResolvedSolutionPage } from "@/lib/solution-service";
import { SolutionPageTracker } from "@/components/analytics/SolutionPageTracker";
import { SolutionHero } from "@/components/solutions/SolutionHero";
import { SolutionCategoryGrid } from "@/components/solutions/SolutionCategoryGrid";
import { SolutionCategoryProducts } from "@/components/solutions/SolutionCategoryProducts";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { ProductVisualStory } from "@/components/products/ProductVisualStory";
import {
  ProductApplicationCards,
  ProductBenefitIcons,
  ProductSupportGrid,
} from "@/components/products/ProductSections";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { buildSolutionQuoteUrl } from "@/lib/solution-quote";
import { productSectionTone } from "@/lib/product-page-theme";

type SolutionPageViewProps = ResolvedSolutionPage;

export function SolutionPageView({
  page,
  categories,
  linkedIndustries,
}: SolutionPageViewProps) {
  const crumbs = [
    { label: "Home", href: "/" },
    { label: "Solutions", href: "/solutions" },
    { label: page.displayName },
  ];

  const quoteUrl = buildSolutionQuoteUrl(page);

  let sectionIndex = 0;
  const nextTone = () => {
    const tone = productSectionTone(sectionIndex);
    sectionIndex += 1;
    return tone;
  };

  const applicationCards =
    page.applicationCards ??
    linkedIndustries.slice(0, 4).map((industry) => ({
      title: industry.name,
      description: industry.summary,
      image: industry.image,
      href: `/industries/${industry.slug}`,
    }));

  const benefitItems = page.keyValueCards ?? [];

  return (
    <>
      <SolutionPageTracker slug={page.slug} name={page.displayName} />
      <SolutionHero page={page} crumbs={crumbs} />

      {benefitItems.length > 0 ? (
        <Section tone="white">
          <ProductBenefitIcons items={benefitItems} />
        </Section>
      ) : null}

      {page.productCategories.length > 0 ? (
        <Section tone={nextTone()}>
          <SolutionCategoryGrid categories={page.productCategories} />
        </Section>
      ) : null}

      {categories.length > 0 ? (
        <Section tone={nextTone()}>
          <SolutionCategoryProducts categories={categories} />
        </Section>
      ) : null}

      <Section tone={nextTone()}>
        <ProductSectionHeader
          eyebrow="Solution overview"
          title={page.storyHeading ?? "Built for your operation"}
        />
        <div className="mt-6 max-w-3xl space-y-4 text-base leading-relaxed text-slate">
          {page.longDescription.split("\n\n").map((paragraph) => (
            <p key={paragraph.slice(0, 48)}>{paragraph}</p>
          ))}
        </div>
        <p className="mt-6 text-sm leading-relaxed text-slate">
          Supplied and supported by Printechs across Saudi Arabia.
        </p>
      </Section>

      {page.visualStory?.items.length ? (
        <Section tone={nextTone()}>
          <ProductVisualStory
            heading={page.visualStory.heading}
            items={page.visualStory.items}
          />
        </Section>
      ) : null}

      {applicationCards.length > 0 ? (
        <Section tone={nextTone()}>
          <ProductSectionHeader
            eyebrow="Industries"
            title="Built for production environments"
          />
          <div className="mt-8">
            <ProductApplicationCards cards={applicationCards} />
          </div>
        </Section>
      ) : null}

      {page.supportServiceItems?.length ? (
        <Section tone={nextTone()}>
          <ProductSectionHeader
            eyebrow="Services & support"
            title="Support & services"
          />
          <div className="mt-8">
            <ProductSupportGrid items={page.supportServiceItems} />
          </div>
        </Section>
      ) : null}

      <Section tone="ink" flush className="!py-10 sm:!py-12 lg:!py-14">
        <div className="mx-auto w-full max-w-content px-[var(--gutter)]">
          <div className="flex flex-col gap-8 lg:flex-row lg:items-center lg:gap-12">
            <div className="max-w-2xl lg:flex-1">
              <p className="text-[0.7rem] font-semibold uppercase tracking-[0.18em] text-signal-bright">
                Next step
              </p>
              <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight text-paper">
                {page.finalCta?.heading ??
                  "Get pricing, availability, and integration advice"}
              </h2>
              <p className="mt-3 text-base leading-relaxed text-paper/72">
                {page.finalCta?.description ??
                  "Contact Printechs for specification support, deployment planning, and ongoing service."}
              </p>
            </div>
            <div className="flex shrink-0 flex-wrap gap-3 lg:justify-end">
              <Button
                href={quoteUrl}
                variant="on-dark"
                analyticsEvent="request_quote_click"
                analyticsLocation="bottom_cta"
                analyticsSolution={page.displayName}
              >
                Request Quote →
              </Button>
              <Button href="/contact" variant="secondary" analyticsLocation="bottom_cta">
                Contact Printechs
              </Button>
            </div>
          </div>
        </div>
      </Section>
    </>
  );
}
