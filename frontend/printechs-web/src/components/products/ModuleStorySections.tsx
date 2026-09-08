import type { ProductPageContent } from "@/types/content";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { ProductIconFrame } from "@/components/products/ProductIcon";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { Button } from "@/components/ui/Button";
import { withBasePath } from "@/lib/paths";

function resolveHref(href?: string | null) {
  if (!href) return undefined;
  if (
    href.startsWith("#") ||
    href.startsWith("http") ||
    href.startsWith("mailto:")
  ) {
    return href;
  }
  return withBasePath(href);
}

export function ModuleConnectionHub({ page }: { page: ProductPageContent }) {
  if (!page.connectionItems?.length) return null;

  return (
    <div className="mt-10">
      <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
        {page.connectionItems.map((item) => {
          const href = resolveHref(item.href);
          const className =
            "flex min-h-[4.5rem] items-center justify-center rounded-md border border-line bg-white px-4 py-3 text-center text-sm font-semibold text-ink shadow-soft";
          return (
            <li key={item.title}>
              {href ? (
                <a href={href} className={`${className} transition hover:border-product-icon/30`}>
                  {item.title}
                  <span className="ml-1 text-product-icon">→</span>
                </a>
              ) : (
                <div className={className}>{item.title}</div>
              )}
            </li>
          );
        })}
      </ul>
      {page.connectionCenterLabel ? (
        <p className="mt-5 text-center font-display text-lg font-semibold text-product-icon">
          {page.connectionCenterLabel}
        </p>
      ) : null}
    </div>
  );
}

export function ModuleKeyFeatures({ page }: { page: ProductPageContent }) {
  if (!page.keyFeatures?.length) return null;

  return (
    <>
      <ProductSectionHeader
        eyebrow="Key features"
        title={page.keyFeaturesHeading ?? "What this module covers"}
      />
      <ol className="mt-8 grid gap-4 sm:grid-cols-2">
        {page.keyFeatures.map((feature, index) => (
          <li
            key={feature.title}
            className="flex gap-4 rounded-md border border-line bg-white p-5 shadow-soft"
          >
            <span className="font-display text-sm font-semibold text-product-icon">
              {String(index + 1).padStart(2, "0")}
            </span>
            <div className="min-w-0">
              <div className="flex items-start gap-3">
                {feature.icon ? (
                  <ProductIconFrame name={feature.icon} variant="benefit" />
                ) : null}
                <h3 className="font-display text-lg font-semibold text-ink">{feature.title}</h3>
              </div>
              <p className="mt-3 text-sm leading-relaxed text-slate">{feature.description}</p>
            </div>
          </li>
        ))}
      </ol>
    </>
  );
}

export function ModuleProcessSteps({ page }: { page: ProductPageContent }) {
  if (!page.processSteps?.length) return null;

  const groups = page.processSteps.reduce<
    Array<{ title: string; items: typeof page.processSteps }>
  >((acc, step) => {
    const current = acc[acc.length - 1];
    if (!current || current.title !== step.groupTitle) {
      acc.push({ title: step.groupTitle, items: [step] });
    } else {
      current.items.push(step);
    }
    return acc;
  }, []);

  return (
    <>
      <ProductSectionHeader
        eyebrow="How it works"
        title={page.processHeading ?? "Connected to the transaction"}
        description={page.processSubheading}
      />
      <ol className="mt-8 space-y-5">
        {groups.map((group) => (
          <li
            key={group.title}
            className="rounded-md border border-line bg-white p-5 shadow-soft"
          >
            <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-product-icon">
              {group.title}
            </p>
            {group.items.map((step) => (
              <div key={step.title} className="mt-3">
                <h3 className="font-display text-lg font-semibold text-ink">{step.title}</h3>
                {step.description ? (
                  <p className="mt-2 text-sm leading-relaxed text-slate">{step.description}</p>
                ) : null}
              </div>
            ))}
          </li>
        ))}
      </ol>
    </>
  );
}

export function ModuleLocalization({ page }: { page: ProductPageContent }) {
  if (!page.localizationHeading && !page.localizationBody) return null;

  return (
    <>
      <ProductSectionHeader
        eyebrow="Saudi Arabia"
        title={page.localizationHeading ?? "Built for local operations"}
      />
      {page.localizationBody ? (
        <p className="mt-5 max-w-3xl text-base leading-relaxed text-slate">
          {page.localizationBody}
        </p>
      ) : null}
      {page.localizationChips?.length ? (
        <ul className="mt-6 flex flex-wrap gap-3">
          {page.localizationChips.map((chip) => (
            <li
              key={chip}
              className="rounded-full border border-line bg-white px-4 py-2 text-sm font-semibold text-ink"
            >
              {chip}
            </li>
          ))}
        </ul>
      ) : null}
    </>
  );
}

export function ModuleReports({ page }: { page: ProductPageContent }) {
  if (!page.reportItems?.length && !page.reportsImage) return null;

  return (
    <div className="grid items-center gap-8 lg:grid-cols-2 lg:gap-12">
      <div>
        <ProductSectionHeader
          eyebrow="Financial reporting"
          title={page.reportsHeading ?? "Reports when management needs them"}
        />
        {page.reportItems?.length ? (
          <ul className="mt-6 grid gap-2 sm:grid-cols-2">
            {page.reportItems.map((item) => (
              <li key={item} className="flex gap-2 text-sm text-slate">
                <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-signal" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        ) : null}
      </div>
      {page.reportsImage ? (
        <ImageFrame
          src={page.reportsImage.src}
          alt={page.reportsImage.alt}
          spec={IMAGE_SPECS.software}
          fill
          className="aspect-[16/10] overflow-hidden rounded-md border border-line bg-mist"
          imageClassName="object-cover object-center"
          sizes="(max-width: 1024px) 100vw, 44rem"
          showSizeLabel={false}
        />
      ) : null}
    </div>
  );
}

export function ModuleDashboard({ page }: { page: ProductPageContent }) {
  if (!page.dashboardHeading && !page.dashboardBody) return null;

  return (
    <div className="grid items-center gap-8 lg:grid-cols-2 lg:gap-12">
      {page.dashboardImage ? (
        <ImageFrame
          src={page.dashboardImage.src}
          alt={page.dashboardImage.alt}
          spec={IMAGE_SPECS.software}
          fill
          className="aspect-[16/10] overflow-hidden rounded-md border border-line bg-mist"
          imageClassName="object-cover object-center"
          sizes="(max-width: 1024px) 100vw, 44rem"
          showSizeLabel={false}
        />
      ) : null}
      <div>
        <ProductSectionHeader
          eyebrow="Management dashboard"
          title={page.dashboardHeading ?? "From transactions to insight"}
        />
        {page.dashboardBody ? (
          <p className="mt-5 max-w-xl text-base leading-relaxed text-slate">
            {page.dashboardBody}
          </p>
        ) : null}
      </div>
    </div>
  );
}

export function ModuleAudience({ page }: { page: ProductPageContent }) {
  if (!page.audienceItems?.length) return null;

  return (
    <>
      <ProductSectionHeader
        eyebrow="Who it is for"
        title={page.audienceHeading ?? "Built for growing and complex businesses"}
      />
      <ul className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {page.audienceItems.map((item) => (
          <li key={item.title} className="rounded-md border border-line bg-white p-5 shadow-soft">
            <h3 className="font-display text-lg font-semibold text-ink">{item.title}</h3>
            {item.description ? (
              <p className="mt-2 text-sm leading-relaxed text-slate">{item.description}</p>
            ) : null}
          </li>
        ))}
      </ul>
    </>
  );
}

export function ModuleIntegration({ page }: { page: ProductPageContent }) {
  if (!page.relatedProducts?.length) return null;

  return (
    <>
      <ProductSectionHeader
        eyebrow="Connected ERP"
        title={page.integrationHeading ?? "Works with the rest of the platform"}
      />
      <ul className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        {page.relatedProducts.map((item) => {
          const href = resolveHref(item.href);
          const className =
            "block h-full rounded-md border border-line bg-white p-4 shadow-soft transition hover:border-product-icon/30";
          const body = (
            <>
              <h3 className="font-display text-base font-semibold text-ink">{item.name}</h3>
              {item.summary ? (
                <p className="mt-2 text-sm leading-relaxed text-slate">{item.summary}</p>
              ) : null}
            </>
          );
          return (
            <li key={item.slug}>
              {href ? (
                <a href={href} className={className}>
                  {body}
                </a>
              ) : (
                <div className={className}>{body}</div>
              )}
            </li>
          );
        })}
      </ul>
    </>
  );
}

export function ModuleImplementationCta({ page }: { page: ProductPageContent }) {
  if (!page.implementationCta) return null;

  return (
    <div className="mt-8">
      <Button
        href={page.implementationCta.href}
        variant="primary"
        analyticsEvent="hero_cta_click"
        analyticsLocation="implementation"
        analyticsProduct={page.displayName}
      >
        {page.implementationCta.label}
      </Button>
    </div>
  );
}
