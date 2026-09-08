import type { ProductContentSection } from "@/types/content";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { coreSectionAnchorId, sectionAnchorId } from "@/lib/section-anchor";
import { withBasePath } from "@/lib/paths";

function youtubeEmbedSrc(url: string): string | null {
  try {
    const parsed = new URL(url);
    if (parsed.hostname.includes("youtu.be")) {
      const id = parsed.pathname.replace("/", "").trim();
      return id ? `https://www.youtube.com/embed/${id}` : null;
    }
    const id = parsed.searchParams.get("v");
    return id ? `https://www.youtube.com/embed/${id}` : null;
  } catch {
    return null;
  }
}

type ProductContentSectionsProps = {
  sections: ProductContentSection[];
  eyebrow?: string;
};

export function ProductContentSections({
  sections,
  eyebrow = "In more detail",
}: ProductContentSectionsProps) {
  return (
    <div className="space-y-12 lg:space-y-16">
      {sections.map((section, index) => {
        const embedSrc = section.videoUrl ? youtubeEmbedSrc(section.videoUrl) : null;
        const hasMedia = Boolean(section.image || embedSrc);
        const imageOnRight = section.imageSide
          ? section.imageSide === "right"
          : index % 2 === 1;

        return (
          <article
            key={section.heading}
            id={
              section.sectionType === "core_module"
                ? coreSectionAnchorId(section.heading)
                : sectionAnchorId(section.heading)
            }
            className={
              hasMedia
                ? "scroll-mt-28 grid items-center gap-8 lg:grid-cols-2 lg:gap-12"
                : "scroll-mt-28 max-w-3xl"
            }
          >
            {hasMedia ? (
            <div className={imageOnRight ? "lg:order-2" : ""}>
              {section.image ? (
                <ImageFrame
                  src={section.image.src}
                  alt={section.image.alt}
                  spec={IMAGE_SPECS.software}
                  fill
                  className="aspect-[16/10] overflow-hidden rounded-md border border-line bg-mist"
                  imageClassName="object-cover object-center"
                  sizes="(max-width: 1024px) 100vw, 44rem"
                  showSizeLabel={false}
                />
              ) : null}
              {embedSrc ? (
                <div
                  className={`overflow-hidden rounded-md border border-line bg-ink ${
                    section.image ? "mt-4" : ""
                  }`}
                >
                  <iframe
                    src={embedSrc}
                    title={section.heading}
                    className="aspect-video w-full"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                  />
                </div>
              ) : null}
            </div>
            ) : null}
            <div className={imageOnRight && hasMedia ? "lg:order-1" : ""}>
              <ProductSectionHeader eyebrow={eyebrow} title={section.heading} />
              <div className="mt-5 max-w-xl space-y-4 text-base leading-relaxed text-slate">
                {section.body.split("\n\n").map((paragraph) => (
                  <p key={paragraph.slice(0, 48)}>{paragraph}</p>
                ))}
              </div>
              {section.link?.href && section.link.label ? (
                <a
                  href={
                    section.link.href.startsWith("#") ||
                    section.link.href.startsWith("http") ||
                    section.link.href.startsWith("mailto:")
                      ? section.link.href
                      : withBasePath(section.link.href)
                  }
                  className="mt-5 inline-flex text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
                >
                  {section.link.label} →
                </a>
              ) : null}
            </div>
          </article>
        );
      })}
    </div>
  );
}
