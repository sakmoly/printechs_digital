import Link from "next/link";
import type {
  ApplicationCard,
  CapabilityModule,
  IconSpecification,
  KeyValueCard,
  ProductReference,
  SupportServiceItem,
} from "@/types/content";
import { ProductIconFrame } from "@/components/products/ProductIcon";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

/** Mockup-style benefit row: large icon left, text right, 4 columns */
export function ProductBenefitIcons({ items }: { items: KeyValueCard[] }) {
  return (
    <ul className="grid gap-5 lg:grid-cols-4">
      {items.map((item) => (
        <li
          key={item.title}
          className="group flex gap-4 rounded-md border border-line bg-white p-5 shadow-soft transition duration-300 hover:-translate-y-0.5 hover:border-product-icon/25 hover:shadow-lift"
        >
          {item.icon ? <ProductIconFrame name={item.icon} variant="benefit" /> : null}
          <div className="min-w-0">
            <h3 className="font-display text-base font-semibold leading-snug text-ink">
              {item.title}
            </h3>
            <p className="mt-2 text-sm leading-relaxed text-slate">
              {item.description}
            </p>
          </div>
        </li>
      ))}
    </ul>
  );
}

/** Mockup-style spec strip: icon centered, label below */
export function ProductIconSpecGrid({ items }: { items: IconSpecification[] }) {
  return (
    <ul className="grid gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6">
      {items.map((item) => (
        <li
          key={item.title}
          className="rounded-md border border-line bg-white px-4 py-5 text-center shadow-soft"
        >
          {item.icon ? (
            <ProductIconFrame name={item.icon} variant="spec" />
          ) : null}
          <h3 className="mt-4 text-sm font-semibold text-product-icon">
            {item.title}
          </h3>
          <p className="mt-2 text-xs leading-relaxed text-slate">
            {item.description}
          </p>
        </li>
      ))}
    </ul>
  );
}

export function ProductCapabilityGrid({ modules }: { modules: CapabilityModule[] }) {
  return (
    <ul className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {modules.map((module) => (
        <li
          key={module.title}
          className="rounded-md border border-line bg-gradient-to-b from-product-icon/5 to-white p-5 shadow-soft"
        >
          <div className="flex items-center gap-3">
            {module.icon ? (
              <ProductIconFrame name={module.icon} variant="benefit" />
            ) : null}
            <h3 className="font-display text-lg font-semibold text-ink">
              {module.title}
            </h3>
          </div>
          <ul className="mt-4 space-y-2">
            {module.items.map((item) => (
              <li key={item} className="flex gap-2 text-sm text-slate">
                <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-product-icon" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  );
}

export function ProductApplicationCards({ cards }: { cards: ApplicationCard[] }) {
  return (
    <FeatureGrid columns={4}>
      {cards.map((card) => {
        const content = (
          <>
            <ImageFrame
              src={card.image.src}
              alt={card.image.alt}
              spec={IMAGE_SPECS.industry}
              fill
              className="aspect-[4/3] bg-mist"
              imageClassName="object-cover transition duration-500 group-hover:scale-[1.02]"
              sizes="(max-width: 768px) 100vw, 25vw"
              showSizeLabel={false}
            />
            <div className="p-5">
              <h3 className="font-display text-lg font-semibold text-ink">
                {card.title}
              </h3>
              <p className="mt-2 text-sm leading-relaxed text-slate">
                {card.description}
              </p>
            </div>
          </>
        );

        if (card.href) {
          return (
            <Link
              key={card.title}
              href={card.href}
              className="group block overflow-hidden rounded-md border border-line bg-white transition duration-300 hover:-translate-y-0.5 hover:border-line-strong hover:shadow-lift focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              {content}
            </Link>
          );
        }

        return (
          <article
            key={card.title}
            className="group overflow-hidden rounded-md border border-line bg-white shadow-soft"
          >
            {content}
          </article>
        );
      })}
    </FeatureGrid>
  );
}

export function ProductEcosystemStrip({ items }: { items: ProductReference[] }) {
  return (
    <ul className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
      {items.map((item) => (
        <li key={item.slug}>
          <Card
            href={item.href}
            title={item.name}
            description={item.summary ?? ""}
            cta="View"
            media={
              item.image ? (
                <ImageFrame
                  src={item.image.src}
                  alt={item.image.alt}
                  spec={IMAGE_SPECS.product}
                  fill
                  className="aspect-square bg-mist"
                  imageClassName="object-cover p-4"
                  sizes="160px"
                  showSizeLabel={false}
                />
              ) : undefined
            }
          />
        </li>
      ))}
    </ul>
  );
}

/** Mockup-style support row: centered icon, title, description */
export function ProductSupportGrid({ items }: { items: SupportServiceItem[] }) {
  return (
    <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
      {items.map((item) => (
        <li
          key={item.title}
          className="rounded-md border border-line bg-white px-5 py-6 text-center shadow-soft"
        >
          {item.icon ? (
            <ProductIconFrame name={item.icon} variant="support" />
          ) : null}
          <h3 className="mt-4 font-display text-base font-semibold text-ink">
            {item.title}
          </h3>
          <p className="mt-2 text-sm leading-relaxed text-slate">
            {item.description}
          </p>
        </li>
      ))}
    </ul>
  );
}
