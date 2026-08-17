import type { Brand } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { LogoGrid } from "@/components/ui/LogoGrid";
import { Button } from "@/components/ui/Button";

export function BrandsSection({ brands }: { brands: Brand[] }) {
  return (
    <Section tone="white">
      <div className="mb-10 flex flex-col gap-6 md:mb-12 md:flex-row md:items-end md:justify-between">
        <Heading
          eyebrow="Brands"
          title="Browse by brand"
          description="Explore the global technology brands Printechs represents across industrial and retail solutions."
          className="mb-0"
        />
        <Button href="/brands" variant="ghost" className="shrink-0">
          View all brands
        </Button>
      </div>
      <LogoGrid brands={brands} />
    </Section>
  );
}
