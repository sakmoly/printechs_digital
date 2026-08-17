/**
 * Content models for the Printechs Digital frontend.
 * These interfaces mirror the future ERPNext marketing content API shapes.
 * Replace mock data loaders with API clients without changing component contracts.
 */

export type SeoFields = {
  title: string;
  description: string;
  canonicalPath: string;
  openGraphTitle?: string;
  openGraphDescription?: string;
  openGraphImage?: string;
  indexPage?: boolean;
};

export type MediaAsset = {
  src: string;
  alt: string;
  width?: number;
  height?: number;
};

export type VideoAsset = {
  type: "youtube" | "hosted";
  /** YouTube ID or hosted video URL */
  source: string;
  title: string;
  poster?: string;
};

export type Cta = {
  label: string;
  href: string;
  variant?: "primary" | "secondary" | "ghost";
};

export type Product = {
  id: string;
  slug: string;
  name: string;
  brand: string;
  summary: string;
  category: string;
  division: "industrial" | "retail";
  image: MediaAsset;
  relatedIndustrySlugs?: string[];
  relatedSolutionSlugs?: string[];
  /** When set, this product is a category hub linking to other product slugs. */
  hubProductSlugs?: string[];
  seo: SeoFields;
};

export type ProductSpecItem = {
  label: string;
  value: string;
};

export type ProductSpecGroup = {
  title: string;
  items: ProductSpecItem[];
};

/** Phase F3 product types — one page architecture, conditional sections. */
export type ProductType =
  | "industrial"
  | "retail_hardware"
  | "software"
  | "generic";

export type TrustIndicator = {
  label: string;
  value: string;
};

/** Icon keys for product page sections — maps to inline SVGs in ProductIcon. */
export type ProductIconKey =
  | "speed"
  | "lines"
  | "shield"
  | "integration"
  | "battery"
  | "scan"
  | "android"
  | "checkout"
  | "inventory"
  | "store"
  | "loyalty"
  | "install"
  | "consumables"
  | "maintenance"
  | "training"
  | "display"
  | "connectivity"
  | "durability"
  | "zatca"
  | "cloud"
  | "report"
  | "device"
  | "rugged"
  | "print";

export type KeyValueCard = {
  icon?: ProductIconKey;
  title: string;
  description: string;
};

export type VisualStoryItem = {
  id: string;
  label: string;
  image: MediaAsset;
  caption?: string;
};

export type ApplicationCard = {
  title: string;
  description: string;
  image: MediaAsset;
  href?: string;
};

export type CapabilityModule = {
  icon?: ProductIconKey;
  title: string;
  items: string[];
};

export type SupportServiceItem = {
  icon?: ProductIconKey;
  title: string;
  description: string;
};

export type IconSpecification = {
  icon?: ProductIconKey;
  title: string;
  description: string;
};

export type ProductDownload = {
  label: string;
  href: string;
  type?: "datasheet" | "brochure" | "manual" | "other";
};

export type ProductReference = {
  slug: string;
  name: string;
  summary?: string;
  href: string;
  image?: MediaAsset;
};

/**
 * Universal product page content — mirrors future ERPNext marketing API shape.
 * Sections auto-hide when optional fields are empty.
 */
export type ProductPageContent = {
  slug: string;
  productType: ProductType;
  displayName: string;
  itemCode?: string;
  brand: string;
  brandSlug?: string;
  category: string;
  subcategory?: string;
  /** Small caps label above title, e.g. CONTINUOUS INKJET PRINTER */
  categoryLabel?: string;
  tagline?: string;
  shortDescription: string;
  longDescription: string;
  heroImage: MediaAsset;
  gallery?: MediaAsset[];
  videoUrl?: string;
  /** Short trust chips shown in hero below CTAs */
  heroTrustChips?: string[];
  /** Primary datasheet/brochure for hero download button */
  primaryDownload?: ProductDownload;
  showDemoCta?: boolean;
  trustIndicators?: TrustIndicator[];
  keyValueCards?: KeyValueCard[];
  visualStory?: {
    heading: string;
    items: VisualStoryItem[];
  };
  storyHeading?: string;
  features: string[];
  iconSpecifications?: IconSpecification[];
  keySpecifications?: ProductSpecItem[];
  fullSpecifications?: ProductSpecGroup[];
  collapsibleFullSpecs?: boolean;
  applications?: string[];
  applicationCards?: ApplicationCard[];
  industrySlugs?: string[];
  softwareCapabilities?: string[];
  capabilityModules?: CapabilityModule[];
  accessories?: ProductReference[];
  compatibleHardware?: ProductReference[];
  /** Combined accessories + compatible for ecosystem photo strip */
  ecosystemItems?: ProductReference[];
  supportServices?: string[];
  supportServiceItems?: SupportServiceItem[];
  downloads?: ProductDownload[];
  packageContents?: string[];
  relatedProducts?: ProductReference[];
  finalCta?: {
    heading: string;
    description: string;
  };
  seo: SeoFields;
  canonicalPath: string;
  breadcrumbRoot: { label: string; href: string };
};

/** @deprecated Use ProductPageContent — kept for transitional imports. */
export type ProductDetailContent = {
  displayName: string;
  itemCode?: string;
  tagline?: string;
  overview: string;
  description: string;
  features: string[];
  specGroups: ProductSpecGroup[];
  packageContents?: string[];
  relatedProductSlugs?: string[];
};

export type SoftwareSolution = {
  id: string;
  slug: string;
  name: string;
  summary: string;
  highlights: string[];
  image: MediaAsset;
  relatedIndustrySlugs?: string[];
  seo: SeoFields;
};

export type Industry = {
  id: string;
  slug: string;
  name: string;
  summary: string;
  image: MediaAsset;
  relatedProductSlugs?: string[];
  relatedSoftwareSlugs?: string[];
  relatedSolutionSlugs?: string[];
  relatedVideoIds?: string[];
  relatedCaseStudySlugs?: string[];
  seo: SeoFields;
};

export type Solution = {
  id: string;
  slug: string;
  name: string;
  summary: string;
  image: MediaAsset;
  relatedProductSlugs?: string[];
  relatedSoftwareSlugs?: string[];
  seo: SeoFields;
};

/** Technology / product-type group on a solution hub page (Model B). */
export type SolutionProductCategory = {
  slug: string;
  title: string;
  shortTitle?: string;
  description: string;
  image: MediaAsset;
  productSlugs: string[];
};

/**
 * Solution detail page content — hub that routes to product pages.
 * Mirrors future ERPNext marketing API shape.
 */
export type SolutionPageContent = {
  slug: string;
  displayName: string;
  categoryLabel?: string;
  tagline?: string;
  shortDescription: string;
  longDescription: string;
  heroImage: MediaAsset;
  heroTrustChips?: string[];
  keyValueCards?: KeyValueCard[];
  visualStory?: {
    heading: string;
    items: VisualStoryItem[];
  };
  storyHeading?: string;
  productCategories: SolutionProductCategory[];
  applicationCards?: ApplicationCard[];
  industrySlugs?: string[];
  supportServiceItems?: SupportServiceItem[];
  finalCta?: {
    heading: string;
    description: string;
  };
  seo: SeoFields;
  canonicalPath: string;
};

/** Homepage featured solution cards — operational outcomes, not division categories. */
export type FeaturedSolution = {
  id: string;
  title: string;
  description: string;
  href: string;
  image: MediaAsset;
};

export type Brand = {
  id: string;
  slug: string;
  name: string;
  summary: string;
  logo: MediaAsset;
  seo: SeoFields;
};

export type Video = {
  id: string;
  slug: string;
  title: string;
  summary: string;
  video: VideoAsset;
  seo: SeoFields;
};

export type CaseStudy = {
  id: string;
  slug: string;
  title: string;
  customer: string;
  summary: string;
  industrySlug?: string;
  image: MediaAsset;
  seo: SeoFields;
};

export type Resource = {
  id: string;
  slug: string;
  title: string;
  summary: string;
  type: "article" | "brochure" | "guide";
  href: string;
  seo: SeoFields;
};

export type HeroContent = {
  headline: string;
  supportingText: string;
  media: {
    kind: "image" | "hosted-video" | "external-video";
    src: string;
    poster?: string;
    alt?: string;
  };
  primaryCta: Cta;
  secondaryCta: Cta;
};

export type BusinessDivision = {
  id: string;
  title: string;
  summary: string;
  href: string;
  items: string[];
  image: MediaAsset;
};
