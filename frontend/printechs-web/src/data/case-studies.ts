import type { CaseStudy } from "@/types/content";

export const caseStudies: CaseStudy[] = [
  {
    id: "cs-dairy-coding",
    slug: "dairy-line-coding-upgrade",
    title: "Dairy line coding upgrade",
    customer: "Regional dairy producer",
    summary:
      "Improved code quality and line reliability across high-speed dairy packaging operations.",
    industrySlug: "dairy",
    image: {
      src: "/images/placeholders/case-study.svg",
      alt: "Dairy packaging production line",
      width: 1600,
      height: 900,
    },
    seo: {
      title: "Dairy Line Coding Upgrade | Printechs",
      description: "Case study: dairy packaging coding upgrade by Printechs.",
      canonicalPath: "/resources/case-studies/dairy-line-coding-upgrade",
    },
  },
  {
    id: "cs-retail-pos",
    slug: "multi-store-pos-rollout",
    title: "Multi-store POS rollout",
    customer: "Specialty retail group",
    summary:
      "Rolled out modern POS workflows across stores with clearer operations visibility.",
    industrySlug: "retail",
    image: {
      src: "/images/placeholders/case-study.svg",
      alt: "Retail store technology deployment",
      width: 1600,
      height: 900,
    },
    seo: {
      title: "Multi-Store POS Rollout | Printechs",
      description: "Case study: multi-store POS rollout by Printechs.",
      canonicalPath: "/resources/case-studies/multi-store-pos-rollout",
    },
  },
];
