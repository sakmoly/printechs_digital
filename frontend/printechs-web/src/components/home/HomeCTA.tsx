import type { HomepageCta } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { CTA } from "@/components/ui/CTA";

export function HomeCTA({ content }: { content?: HomepageCta | null }) {
  return (
    <Section>
      <CTA
        title={content?.title}
        description={content?.description}
        primaryLabel={content?.primaryLabel}
        primaryHref={content?.primaryHref}
        secondaryLabel={content?.secondaryLabel}
        secondaryHref={content?.secondaryHref}
      />
    </Section>
  );
}
