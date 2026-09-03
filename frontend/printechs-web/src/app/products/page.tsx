import { fetchCatalogProducts, fetchProductBrands } from "@/lib/catalog-service";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { ProductsCatalog } from "@/components/products/ProductsCatalog";
import { buildMetadata } from "@/lib/seo";

export const revalidate = 60;

export const metadata = buildMetadata({
  title: "Products | Printechs",
  description:
    "Browse industrial and retail technology products supplied by Printechs across Saudi Arabia.",
  canonicalPath: "/products",
});

export default async function ProductsPage() {
  const [catalogProducts, brands] = await Promise.all([
    fetchCatalogProducts(),
    fetchProductBrands(),
  ]);

  return (
    <>
      <PageIntro
        title="Products"
        description="Industrial coding, retail AutoID, weighing, and mobility technology — supplied and supported by Printechs. No pricing displayed; contact us for quotes and availability."
        crumbs={[{ label: "Home", href: "/" }, { label: "Products" }]}
      />
      <Section tone="white">
        <ProductsCatalog products={catalogProducts} brands={brands} />
      </Section>
    </>
  );
}
