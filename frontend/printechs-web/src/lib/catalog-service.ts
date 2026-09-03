import type { Product, SoftwareSolution } from "@/types/content";
import { getCatalogProducts, getFeaturedProducts, products } from "@/data/products";
import { getFeaturedSoftware, softwareSolutions } from "@/data/software";
import { erpnextMethod, normalizeCatalogProduct } from "@/lib/erpnext-client";

function mergeProducts(erpProducts: Product[], mockProducts: Product[]): Product[] {
  const erpSlugs = new Set(erpProducts.map((product) => product.slug));
  const mockOnly = mockProducts.filter((product) => !erpSlugs.has(product.slug));
  return [...erpProducts.map(normalizeCatalogProduct), ...mockOnly];
}

export async function fetchCatalogProducts(): Promise<Product[]> {
  const erpProducts =
    (await erpnextMethod<Product[]>("printechs_digital.api.website.list_products", {
      list: "products",
      limit: 200,
    })) ?? [];

  return mergeProducts(erpProducts, getCatalogProducts());
}

export async function fetchFeaturedProducts(limit = 4): Promise<Product[]> {
  const erpProducts =
    (await erpnextMethod<Product[]>("printechs_digital.api.website.get_featured_products", {
      limit,
    })) ?? [];

  if (erpProducts.length >= limit) {
    return erpProducts.slice(0, limit).map(normalizeCatalogProduct);
  }

  const merged = mergeProducts(erpProducts, getFeaturedProducts(limit));
  return merged.slice(0, limit);
}

export async function fetchSoftwareCatalog(): Promise<Product[]> {
  const erpProducts =
    (await erpnextMethod<Product[]>("printechs_digital.api.website.list_products", {
      list: "software",
      limit: 200,
    })) ?? [];

  const mockSoftware: Product[] = softwareSolutions.map((item) => ({
    id: item.id,
    slug: item.slug,
    name: item.name,
    brand: "Printechs",
    summary: item.summary,
    category: "Software",
    division: "retail" as const,
    image: item.image,
    seo: item.seo,
  }));

  return mergeProducts(erpProducts, mockSoftware);
}

export async function fetchFeaturedSoftware(limit = 6): Promise<SoftwareSolution[]> {
  const erpProducts =
    (await erpnextMethod<Product[]>("printechs_digital.api.website.list_products", {
      list: "software",
      limit,
    })) ?? [];

  const erpAsSoftware: SoftwareSolution[] = erpProducts.map((product) => {
    const mock = softwareSolutions.find((item) => item.slug === product.slug);
    return {
      id: product.id,
      slug: product.slug,
      name: product.name,
      summary: product.summary,
      highlights: mock?.highlights ?? [],
      image: normalizeCatalogProduct(product).image,
      seo: product.seo,
      relatedIndustrySlugs: mock?.relatedIndustrySlugs,
    };
  });

  const erpSlugs = new Set(erpAsSoftware.map((item) => item.slug));
  const mockOnly = getFeaturedSoftware(limit).filter((item) => !erpSlugs.has(item.slug));
  return [...erpAsSoftware, ...mockOnly].slice(0, limit);
}

export async function fetchProductsByBrand(brandName: string): Promise<Product[]> {
  const catalog = await fetchCatalogProducts();
  const brandKey = brandName.trim().toLowerCase();
  const matches = catalog.filter((product) =>
    (product.brand || "").toLowerCase().includes(brandKey),
  );
  const fromErp = matches.filter((product) => product.id.startsWith("erp-"));
  return fromErp.length ? fromErp : matches;
}

export async function fetchProductBrands(): Promise<string[]> {
  const catalog = await fetchCatalogProducts();
  return Array.from(new Set(catalog.map((product) => product.brand))).sort();
}

export async function fetchPublishedProductSlugs(): Promise<string[]> {
  const slugs =
    (await erpnextMethod<string[]>("printechs_digital.api.website.get_product_slugs")) ?? [];
  const mockSlugs = products.map((product) => product.slug);
  return Array.from(new Set([...slugs, ...mockSlugs]));
}

export function getCatalogProductsMock(): Product[] {
  return getCatalogProducts();
}

export function getFeaturedProductsMock(limit = 4): Product[] {
  return getFeaturedProducts(limit);
}
