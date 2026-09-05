import Link from "next/link";
import type { ReactNode } from "react";
import type { ResolvedProductPage } from "@/lib/product-service";
import { ProductHero } from "@/components/products/ProductHero";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { ProductVisualStory } from "@/components/products/ProductVisualStory";
import { ProductTourSections } from "@/components/products/ProductTourSections";
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
import { ProductPageTracker } from "@/components/analytics/ProductPageTracker";
import { JsonLd } from "@/components/seo/JsonLd";
import { buildProductDemoUrl, buildProductQuoteUrl } from "@/lib/product-quote";
import { productSectionTone } from "@/lib/product-page-theme";
import {
  resolveProductPageSectionOrder,
  type ProductPageSectionKey,
} from "@/lib/product-page-section-order";
import type { ProductPageContent } from "@/types/content";

type ProductPageViewProps = ResolvedProductPage;

type SectionRenderContext = {
  page: ProductPageContent;
  brand: ResolvedProductPage["brand"];
  applicationCards: NonNullable<ProductPageContent["applicationCards"]>;
  benefitItems: NonNullable<ProductPageContent["keyValueCards"]>;
  demoUrl: string;
  ecosystemItems: NonNullable<ProductPageContent["ecosystemItems"]>;
  quoteUrl: string;
  relatedColumns: 2 | 3;
  relatedImageSpec: (typeof IMAGE_SPECS)[keyof typeof IMAGE_SPECS];
};

function applicationSectionTitle(page: ProductPageContent): string {
  const category = page.category.toLowerCase();
  if (category.includes("warehouse")) return "Built for warehouse operations";
  if (category.includes("erp") || category.includes("business")) {
    return "Built for business operations";
  }
  if (category.includes("compliance") || category.includes("zatca")) {
    return "Built for compliant invoicing";
  }
  if (page.productType === "software") return "Built for retail operations";
  return "Built for production environments";
}

function ecosystemSectionTitle(page: ProductPageContent): string {
  const category = page.category.toLowerCase();
  if (category.includes("warehouse")) return "Works with your warehouse hardware";
  if (
    category.includes("erp") ||
    category.includes("business") ||
    category.includes("compliance") ||
    category.includes("zatca")
  ) {
    return "Works with your systems and devices";
  }
  if (page.productType === "software") return "Works with your retail hardware";
  return "Compatible products & accessories";
}

function renderProductPageSection(
  key: ProductPageSectionKey,
  context: SectionRenderContext,
): ReactNode | null {
  const {
    page,
    brand,
    applicationCards,
    benefitItems,
    demoUrl,
    ecosystemItems,
    quoteUrl,
    relatedColumns,
    relatedImageSpec,
  } = context;

  switch (key) {
    case "benefits":
      if (!benefitItems.length) return null;
      return (
        <Section tone="white" pad="compact" className="!pt-0">
          <ProductBenefitIcons items={benefitItems} />
        </Section>
      );

    case "overview":
      return (
        <>
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
        </>
      );

    case "product_tour":
      if (page.productTour?.sections.length) {
        return (
          <ProductTourSections
            tour={page.productTour}
            demoHref={demoUrl}
            quoteHref={quoteUrl}
            productName={page.displayName}
          />
        );
      }
      if (page.visualStory?.items.length) {
        return (
          <ProductVisualStory
            heading={page.visualStory.heading}
            items={page.visualStory.items}
          />
        );
      }
      return null;

    case "icon_specifications":
      if (page.iconSpecifications?.length) {
        return (
          <>
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
          </>
        );
      }
      if (page.fullSpecifications?.length) {
        return (
          <ProductFullSpecs
            groups={page.fullSpecifications}
            defaultExpanded={page.collapsibleFullSpecs === false}
          />
        );
      }
      return null;

    case "capability_modules":
      if (!page.capabilityModules?.length) return null;
      return (
        <>
          <ProductSectionHeader
            eyebrow="Platform modules"
            title="What this platform helps you manage"
          />
          <div className="mt-6">
            <ProductCapabilityGrid modules={page.capabilityModules} />
          </div>
        </>
      );

    case "software_capabilities":
      if (!page.softwareCapabilities?.length || page.capabilityModules?.length) return null;
      return (
        <>
          <ProductSectionHeader eyebrow="Software capabilities" title="Key capabilities" />
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
        </>
      );

    case "applications":
      if (!applicationCards.length) return null;
      return (
        <>
          <ProductSectionHeader
            eyebrow="Applications"
            title={applicationSectionTitle(page)}
          />
          <div className="mt-6">
            <ProductApplicationCards cards={applicationCards} />
          </div>
        </>
      );

    case "content_sections":
      if (!page.contentSections?.length) return null;
      return <ProductContentSections sections={page.contentSections} />;

    case "ecosystem":
      if (!ecosystemItems.length) return null;
      return (
        <>
          <ProductSectionHeader eyebrow="Ecosystem" title={ecosystemSectionTitle(page)} />
          <div className="mt-6">
            <ProductEcosystemStrip items={ecosystemItems} />
          </div>
        </>
      );

    case "support":
      if (!page.supportServiceItems?.length) return null;
      return (
        <>
          <ProductSectionHeader eyebrow="Services & support" title="Support & services" />
          <div className="mt-6">
            <ProductSupportGrid items={page.supportServiceItems} />
          </div>
        </>
      );

    case "downloads":
      if (!page.downloads?.length && !page.packageContents?.length) return null;
      return (
        <>
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
              <ProductSectionHeader eyebrow="Package contents" title="What's included" />
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
        </>
      );

    case "related_products":
      if (!page.relatedProducts?.length) return null;
      return (
        <>
          <div className="mb-6 flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
            <ProductSectionHeader eyebrow="Related products" title="You may also consider" />
            <Link
              href={page.breadcrumbRoot.href}
              className="text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
            >
              View all {page.breadcrumbRoot.label.toLowerCase()}
            </Link>
          </div>
          <FeatureGrid columns={relatedColumns} gap="md">
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
        </>
      );

    case "faqs":
      if (!page.faqs?.length) return null;
      return (
        <>
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
        </>
      );

    default:
      return null;
  }
}

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
  const relatedImageSpec =
    page.productType === "software" ? IMAGE_SPECS.software : IMAGE_SPECS.product;

  const ecosystemItems =
    page.ecosystemItems ??
    [...(page.accessories ?? []), ...(page.compatibleHardware ?? [])];

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
  const sectionOrder = resolveProductPageSectionOrder(page.pageSectionOrder);

  let sectionIndex = 0;
  const nextTone = () => {
    const tone = productSectionTone(sectionIndex);
    sectionIndex += 1;
    return tone;
  };

  const sectionContext: SectionRenderContext = {
    page,
    brand,
    applicationCards,
    benefitItems,
    demoUrl,
    ecosystemItems,
    quoteUrl,
    relatedColumns,
    relatedImageSpec,
  };

  const hasRichSections = Boolean(
    benefitItems.length ||
      page.visualStory?.items.length ||
      page.productTour?.sections.length ||
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
      <ProductPageTracker page={page} />
      <ProductHero
        page={page}
        brand={brand}
        crumbs={crumbs}
        successStoriesHref={successStoriesHref}
      />

      {sectionOrder.map((sectionKey) => {
        const content = renderProductPageSection(sectionKey, sectionContext);
        if (!content) return null;

        if (sectionKey === "benefits") {
          return <div key={sectionKey}>{content}</div>;
        }

        return (
          <Section key={sectionKey} pad="compact" tone={nextTone()}>
            {content}
          </Section>
        );
      })}

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
                <Button
                  href={quoteUrl}
                  variant="on-dark"
                  analyticsEvent="request_quote_click"
                  analyticsLocation="bottom_cta"
                  analyticsProduct={page.displayName}
                  analyticsBrand={page.brand}
                  analyticsCategory={page.category}
                >
                  {page.productType === "software"
                    ? "Talk to a Specialist →"
                    : "Request Quote →"}
                </Button>
                <Button href="/contact" variant="secondary" analyticsLocation="bottom_cta">
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
