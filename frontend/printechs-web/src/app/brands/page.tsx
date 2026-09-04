import Link from "next/link";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";
import { fetchBrands, brandHref } from "@/lib/brand-service";

import { REVALIDATE_STABLE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_STABLE_SECONDS;

export const metadata = buildMetadata({
  title: "Brands | Printechs",
  description:
    "Browse industrial and retail technology brands represented by Printechs across Saudi Arabia.",
  canonicalPath: "/brands",
});

export default async function BrandsPage() {
  const brands = await fetchBrands();

  return (
    <>
      <PageIntro
        title="Brands"
        description="Printechs represents leading global technology brands across coding, marking, barcode, mobility, weighing and retail systems."
        crumbs={[{ label: "Home", href: "/" }, { label: "Brands" }]}
      />
      <Section tone="white">
        <ul className="grid gap-3 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
          {brands.map((brand) => (
            <li key={brand.id}>
              <Link
                href={brandHref(brand)}
                aria-label={`${brand.name} products`}
                className="group flex h-full flex-col items-center rounded-sm border border-line bg-white px-4 py-4 transition duration-300 hover:-translate-y-0.5 hover:border-line-strong hover:shadow-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
              >
                <div className="flex h-16 w-full items-center justify-center">
                  <ImageFrame
                    src={brand.logo.src}
                    alt=""
                    spec={IMAGE_SPECS.brandLogo}
                    width={200}
                    height={64}
                    showSizeLabel={false}
                    className="flex h-full w-full items-center justify-center"
                    imageClassName="max-h-14 w-auto max-w-full object-contain object-center transition duration-300 group-hover:scale-[1.02]"
                  />
                </div>
                <h2 className="sr-only">{brand.name}</h2>
                <span className="mt-3 text-sm font-semibold text-signal-deep underline-offset-4 group-hover:underline">
                  View Products
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </Section>
    </>
  );
}
