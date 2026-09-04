import Link from "next/link";
import type { ResolvedProductPage } from "@/lib/product-service";
import { ProductHero } from "@/components/products/ProductHero";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { ProductVisualStory } from "@/components/products/ProductVisualStory";
import { ModernPosProductTour } from "@/components/products/ModernPosProductTour";
import { ProductFullSpecs } from "@/components/products/ProductFullSpecs";
import {
  ProductApplicationCards,
  ProductBenefitIcons,
  ProductCapabilityGrid,
  ProductEcosystemStrip,
  ProductIconSpecGrid,
  ProductSupportGrid,
} from "@/components/products/ProductSections";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { ProductContentSections } from "@/components/products/ProductContentSections";
import { ProductFaq } from "@/components/products/ProductFaq";
import { JsonLd } from "@/components/seo/JsonLd";
import { buildProductDemoUrl, buildProductQuoteUrl } from "@/lib/product-quote";
import { productSectionTone } from "@/lib/product-page-theme";

type ProductPageViewProps = ResolvedProductPage;

export function ProductPageView({
  page,
  brand,
  linkedIndustries,
  successStoriesHref,
}: ProductPageViewProps) {
  const crumbs = [
    { label: "Home", href: "/" },
    page.breadcrumbRoot,
    { label: page.displayName },
  ];

  const quoteUrl = buildProductQuoteUrl(page);
  const demoUrl = buildProductDemoUrl(page);
  const isModernPosTour = page.slug === "modern-pos";
  const relatedImageSpec =
    page.productType === "software" ? IMAGE_SPECS.software : IMAGE_SPECS.product;

  const ecosystemItems =
    page.ecosystemItems ??
    [...(page.accessories ?? []), ...(page.compatibleHardware ?? [])];

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
  const relatedColumns =
    page.relatedProducts && page.relatedProducts.length >= 3 ? 3 : 2;
  const hasRichSections = Boolean(
    benefitItems.length ||
      page.visualStory?.items.length ||
      page.iconSpecifications?.length ||
      page.fullSpecifications?.length ||
      page.capabilityModules?.length ||
      page.softwareCapabilities?.length ||
      applicationCards.length ||
      ecosystemItems.length ||
      page.supportServiceItems?.length ||
      page.downloads?.length ||
      page.packageContents?.length ||
      page.relatedProducts?.length ||
      page.contentSections?.length ||
      page.faqs?.length,
  );

  return (
    <>
      <ProductHero
        page={page}
        brand={brand}
        crumbs={crumbs}
        successStoriesHref={successStoriesHref}
      />

      {benefitItems.length > 0 ? (
        <Section tone="white" pad="compact" className="!pt-0">
          <ProductBenefitIcons items={benefitItems} />
        </Section>
      ) : null}

      {isModernPosTour ? (
        <Section pad="compact" tone={nextTone()}>
          <ModernPosProductTour demoHref={demoUrl} quoteHref={quoteUrl} />
        </Section>
      ) : page.visualStory?.items.length ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductVisualStory
            heading={page.visualStory.heading}
            items={page.visualStory.items}
          />
        </Section>
      ) : null}

      <Section pad="compact" tone={nextTone()}>
        <ProductSectionHeader
          eyebrow="Product overview"
          title={page.storyHeading ?? "Built for your operation"}
        />
        <div className="mt-5 max-w-3xl space-y-4 text-base leading-relaxed text-slate">
          {page.longDescription.split("\n\n").map((paragraph) => (
            <p key={paragraph.slice(0, 48)}>{paragraph}</p>
          ))}
        </div>
        {brand ? (
          <p className="mt-5 text-sm leading-relaxed text-slate">
            Supplied and supported by Printechs across Saudi Arabia.
          </p>
        ) : null}
      </Section>

      {page.iconSpecifications?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <ProductSectionHeader
              eyebrow="Key features & specifications"
              title="Technical highlights"
            />
          </div>
          <div className="mt-6">
            <ProductIconSpecGrid items={page.iconSpecifications} />
          </div>
          {page.fullSpecifications?.length ? (
            <div className="mt-8 border-t border-line pt-6">
              <ProductFullSpecs
                groups={page.fullSpecifications}
                defaultExpanded={page.collapsibleFullSpecs === false}
              />
            </div>
          ) : null}
        </Section>
      ) : page.fullSpecifications?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductFullSpecs
            groups={page.fullSpecifications}
            defaultExpanded={page.collapsibleFullSpecs === false}
          />
        </Section>
      ) : null}

      {page.capabilityModules?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductSectionHeader
            eyebrow="Platform modules"
            title="What this platform helps you manage"
          />
          <div className="mt-6">
            <ProductCapabilityGrid modules={page.capabilityModules} />
          </div>
        </Section>
      ) : null}

      {page.softwareCapabilities?.length && !page.capabilityModules?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductSectionHeader
            eyebrow="Software capabilities"
            title="Key capabilities"
          />
          <ul className="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {page.softwareCapabilities.map((capability) => (
              <li
                key={capability}
                className="flex gap-3 rounded-sm border border-line bg-paper p-4 text-sm leading-relaxed text-ink"
              >
                <span className="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-signal/15 text-xs font-bold text-signal-deep">
                  ✓
                </span>
                <span>{capability}</span>
              </li>
            ))}
          </ul>
        </Section>
      ) : null}

      {applicationCards.length > 0 ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductSectionHeader
            eyebrow="Applications"
            title={
              page.category.toLowerCase().includes("warehouse")
                ? "Built for warehouse operations"
                : page.category.toLowerCase().includes("erp") ||
                    page.category.toLowerCase().includes("business")
                  ? "Built for business operations"
                  : page.category.toLowerCase().includes("compliance") ||
                      page.category.toLowerCase().includes("zatca")
                    ? "Built for compliant invoicing"
                    : page.productType === "software"
                      ? "Built for retail operations"
                      : "Built for production environments"
            }
          />
          <div className="mt-6">
            <ProductApplicationCards cards={applicationCards} />
          </div>
        </Section>
      ) : null}

      {page.contentSections?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductContentSections sections={page.contentSections} />
        </Section>
      ) : null}

      {ecosystemItems.length > 0 ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductSectionHeader
            eyebrow="Ecosystem"
            title={
              page.category.toLowerCase().includes("warehouse")
                ? "Works with your warehouse hardware"
                : page.category.toLowerCase().includes("erp") ||
                    page.category.toLowerCase().includes("business") ||
                    page.category.toLowerCase().includes("compliance") ||
                    page.category.toLowerCase().includes("zatca")
                  ? "Works with your systems and devices"
                  : page.productType === "software"
                    ? "Works with your retail hardware"
                    : "Compatible products & accessories"
            }
          />
          <div className="mt-6">
            <ProductEcosystemStrip items={ecosystemItems} />
          </div>
        </Section>
      ) : null}

      {page.supportServiceItems?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <ProductSectionHeader
            eyebrow="Services & support"
            title="Support & services"
          />
          <div className="mt-6">
            <ProductSupportGrid items={page.supportServiceItems} />
          </div>
        </Section>
      ) : null}

      {page.downloads?.length || page.packageContents?.length ? (
        <Section pad="compact" tone={nextTone()}>
          {page.downloads?.length ? (
            <>
              <ProductSectionHeader eyebrow="Downloads" title="Resources" />
              <ul className="mt-5 flex flex-wrap gap-3">
                {page.downloads.map((download) => (
                  <li key={download.label}>
                    <a
                      href={download.href}
                      className="inline-flex items-center gap-2 rounded-sm border border-line bg-white px-4 py-3 text-sm font-semibold text-ink transition hover:border-line-strong hover:shadow-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
                    >
                      <span aria-hidden="true">↓</span>
                      {download.label}
                    </a>
                  </li>
                ))}
              </ul>
            </>
          ) : null}

          {page.packageContents?.length ? (
            <div className={page.downloads?.length ? "mt-8 border-t border-line pt-8" : ""}>
              <ProductSectionHeader
                eyebrow="Package contents"
                title="What's included"
              />
              <ul className="mt-5 space-y-2 text-base text-slate">
                {page.packageContents.map((item) => (
                  <li key={item} className="flex gap-2">
                    <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-signal-deep" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          ) : null}
        </Section>
      ) : null}

      {page.relatedProducts?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <div className="mb-6 flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
            <ProductSectionHeader
              eyebrow="Related products"
              title="You may also consider"
            />
            <Link
              href={page.breadcrumbRoot.href}
              className="text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
            >
              View all {page.breadcrumbRoot.label.toLowerCase()}
            </Link>
          </div>
          <FeatureGrid columns={relatedColumns as 2 | 3} gap="md">
            {page.relatedProducts.map((related) => (
              <Card
                key={related.slug}
                href={related.href}
                title={related.name}
                description={related.summary ?? ""}
                cta="View product"
                media={
                  related.image ? (
                    <ImageFrame
                      src={related.image.src}
                      alt={related.image.alt}
                      spec={relatedImageSpec}
                      fill
                      className={
                        page.productType === "software"
                          ? "aspect-[16/10] bg-mist"
                          : "aspect-square bg-mist"
                      }
                      imageClassName="object-cover"
                      sizes="(max-width: 768px) 100vw, 33vw"
                    />
                  ) : undefined
                }
              />
            ))}
          </FeatureGrid>
        </Section>
      ) : null}

      {page.faqs?.length ? (
        <Section pad="compact" tone={nextTone()}>
          <JsonLd
            data={{
              "@context": "https://schema.org",
              "@type": "FAQPage",
              mainEntity: page.faqs.map((item) => ({
                "@type": "Question",
                name: item.question,
                acceptedAnswer: {
                  "@type": "Answer",
                  text: item.answer,
                },
              })),
            }}
          />
          <ProductFaq items={page.faqs} />
        </Section>
      ) : null}

      {hasRichSections ? (
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
                <Button href={quoteUrl} variant="on-dark">
                  {page.productType === "software"
                    ? "Talk to a Specialist →"
                    : "Request Quote →"}
                </Button>
                <Button href="/contact" variant="secondary">
                  Contact Printechs
                </Button>
              </div>
            </div>
          </div>
        </Section>
      ) : null}
    </>
  );
}
