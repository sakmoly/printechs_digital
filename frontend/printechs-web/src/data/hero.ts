import type { HeroContent } from "@/types/content";

export const homeHero: HeroContent = {
  headline: "Technology That Moves Business Forward",
  supportingText:
    "Industrial coding, retail technology and enterprise software solutions for businesses across Saudi Arabia.",
  media: {
    kind: "image",
    src: "/images/hero/home-hero.png",
    alt: "Industrial coding, retail technology and enterprise software solutions",
  },
  primaryCta: {
    label: "Explore Solutions",
    href: "/solutions",
    variant: "primary",
  },
  secondaryCta: {
    label: "Talk to a Specialist",
    href: "/contact",
    variant: "secondary",
  },
};
