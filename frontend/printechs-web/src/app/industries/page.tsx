import Link from "next/link";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";
import { fetchIndustries } from "@/lib/industry-service";

export const revalidate = 60;

export const metadata = buildMetadata({
  title: "Industries | Printechs",
  description: "Industry-led entry points into Printechs capabilities across Saudi Arabia.",
  canonicalPath: "/industries",
});

export default async function IndustriesPage() {
  const industries = await fetchIndustries();

  return (
    <>
      <PageIntro
        title="Industries"
        description="From dairy and packaging to retail and logistics — technology mapped to the realities of each sector."
        crumbs={[{ label: "Home", href: "/" }, { label: "Industries" }]}
      />
      <Section tone="white">
        <ul className="grid grid-cols-2 gap-3 sm:gap-4 lg:grid-cols-4">
          {industries.map((item) => (
            <li key={item.id}>
              <Link
                href={`/industries/${item.slug}`}
                className="group block rounded-sm bg-mist focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
              >
                <ImageFrame
                  src={item.image.src}
                  alt={item.image.alt}
                  spec={IMAGE_SPECS.industry}
                  fill
                  className="aspect-[3/2] rounded-sm"
                  imageClassName="media-zoom object-cover"
                  sizes="(max-width: 1024px) 50vw, 25vw"
                  overlay={
                    <>
                      <div className="absolute inset-0 bg-gradient-to-t from-ink/75 via-ink/20 to-transparent" />
                      <span className="absolute inset-x-0 bottom-0 p-4 font-display text-base font-semibold text-paper sm:text-lg">
                        {item.name}
                      </span>
                    </>
                  }
                />
              </Link>
            </li>
          ))}
        </ul>
      </Section>
    </>
  );
}
