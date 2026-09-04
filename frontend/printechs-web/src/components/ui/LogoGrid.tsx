import Link from "next/link";
import type { Brand } from "@/types/content";
import { brandHref } from "@/lib/brand-service";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

function BrandMark({ brand }: { brand: Brand }) {
  return (
    <div className="relative aspect-[5/2] w-full">
      <ImageFrame
        src={brand.logo.src}
        alt={brand.logo.alt}
        spec={IMAGE_SPECS.brandLogo}
        fill
        sizes="(max-width: 640px) 45vw, (max-width: 1024px) 30vw, 16vw"
        showSizeLabel={false}
        className="relative h-full w-full"
        imageClassName="object-contain object-center p-1 transition duration-300 ease-out group-hover:scale-[1.02]"
      />
    </div>
  );
}

export function LogoGrid({
  brands,
  linked = true,
}: {
  brands: Brand[];
  linked?: boolean;
}) {
  return (
    <ul className="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-6">
      {brands.map((brand) => {
        const cardClass =
          "group block rounded-sm border border-line bg-white p-2 transition duration-300 hover:border-line-strong hover:shadow-soft focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal";

        return (
          <li key={brand.id}>
            {linked ? (
              <Link href={brandHref(brand)} className={cardClass} aria-label={brand.name}>
                <BrandMark brand={brand} />
              </Link>
            ) : (
              <div className={cardClass}>
                <BrandMark brand={brand} />
              </div>
            )}
          </li>
        );
      })}
    </ul>
  );
}
