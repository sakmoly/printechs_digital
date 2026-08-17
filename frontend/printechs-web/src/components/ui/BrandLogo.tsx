import Image from "next/image";
import Link from "next/link";
import { siteConfig } from "@/config/site";
import { withBasePath } from "@/lib/paths";

type BrandLogoProps = {
  className?: string;
  priority?: boolean;
  /** header = large nav mark, footer = compact */
  size?: "header" | "footer";
};

const sizeClass = {
  header: "h-9 w-auto object-contain object-left sm:h-10 lg:h-11",
  footer: "h-11 w-auto object-contain object-left sm:h-12",
} as const;

export function BrandLogo({
  className = "",
  priority = false,
  size = "footer",
}: BrandLogoProps) {
  return (
    <Link
      href="/"
      className={`inline-flex items-center focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal ${className}`}
      aria-label={siteConfig.name}
    >
      <Image
        src={withBasePath("/images/company/printechs-logo.png")}
        alt={siteConfig.name}
        width={size === "header" ? 220 : 320}
        height={size === "header" ? 96 : 140}
        priority={priority}
        className={sizeClass[size]}
      />
    </Link>
  );
}
