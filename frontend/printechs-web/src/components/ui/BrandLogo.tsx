import Image from "next/image";
import Link from "next/link";
import { siteConfig } from "@/config/site";
import { withBasePath } from "@/lib/paths";

type BrandLogoProps = {
  className?: string;
  priority?: boolean;
  /** header = nav bar, footer = site footer */
  size?: "header" | "footer";
};

/** Official transparent logo from printechs.com (3268×800). */
const LOGO_WIDTH = 3268;
const LOGO_HEIGHT = 800;
const LOGO_SRC = "/images/company/printechs-logo-full.png";

const frameClass = {
  /** Fixed aspect box prevents Next.js / CSS from squeezing the wide logo. */
  header:
    "relative block h-10 w-[10.75rem] shrink-0 sm:h-11 sm:w-[11.75rem] lg:h-12 lg:w-[12.875rem]",
  footer:
    "relative block h-11 w-[11.75rem] shrink-0 sm:h-12 sm:w-[12.875rem]",
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
      <span className={frameClass[size]}>
        <Image
          src={withBasePath(LOGO_SRC)}
          alt={siteConfig.name}
          width={LOGO_WIDTH}
          height={LOGO_HEIGHT}
          priority={priority}
          unoptimized
          className="object-contain object-left"
          fill
          sizes="(max-width: 1024px) 188px, 206px"
        />
      </span>
    </Link>
  );
}
