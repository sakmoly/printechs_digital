import Link from "next/link";
import { brands } from "@/data";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";

export const metadata = buildMetadata({
  title: "Brands | Printechs",
  description:
    "Browse industrial and retail technology brands represented by Printechs across Saudi Arabia.",
  canonicalPath: "/brands",
});

export default function BrandsPage() {
  return (
    <>
      <PageIntro
        title="Brands"
        description="Printechs represents leading global technology brands across coding, marking, barcode, mobility, weighing and retail systems."
        crumbs={[{ label: "Home", href: "/" }, { label: "Brands" }]}
      />
      <Section tone="white">
        <ul className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {brands.map((brand) => (
            <li key={brand.id}>
              <Link
                href={`/brands/${brand.slug}`}
                className="group flex h-full flex-col rounded-sm border border-line bg-paper p-6 transition duration-300 hover:-translate-y-0.5 hover:border-line-strong hover:bg-white hover:shadow-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
              >
                <div className="flex h-16 w-full items-center justify-center">
                  <ImageFrame
                    src={brand.logo.src}
                    alt={brand.logo.alt}
                    spec={IMAGE_SPECS.brandLogo}
                    width={200}
                    height={64}
                    showSizeLabel={false}
                    className="flex h-full w-full items-center justify-center"
                    imageClassName="max-h-11 w-auto max-w-full object-contain object-center transition duration-300 group-hover:scale-[1.02]"
                  />
                </div>
                <h2 className="mt-5 font-display text-2xl font-semibold tracking-tight text-ink">
                  {brand.name}
                </h2>
                <p className="mt-3 flex-1 text-sm leading-relaxed text-slate">
                  {brand.summary}
                </p>
                <span className="mt-5 text-sm font-semibold text-signal-deep underline-offset-4 group-hover:underline">
                  View brand
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </Section>
    </>
  );
}
