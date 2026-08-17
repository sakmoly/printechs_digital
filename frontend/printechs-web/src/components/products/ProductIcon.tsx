import type { ReactNode } from "react";
import type { ProductIconKey } from "@/types/content";

type ProductIconProps = {
  name: ProductIconKey;
  className?: string;
  size?: "sm" | "md" | "lg";
};

const sizeClass = {
  sm: "h-5 w-5",
  md: "h-8 w-8",
  lg: "h-10 w-10",
};

function IconSvg({
  children,
  className = "",
  size = "md",
}: {
  children: ReactNode;
  className?: string;
  size?: "sm" | "md" | "lg";
}) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      className={`${sizeClass[size]} ${className}`}
      aria-hidden="true"
    >
      {children}
    </svg>
  );
}

export function ProductIcon({ name, className = "", size = "md" }: ProductIconProps) {
  switch (name) {
    case "speed":
      return (
        <IconSvg className={className} size={size}>
          <path d="M13 2 3 14h8l-1 8 10-12h-8l1-8z" />
        </IconSvg>
      );
    case "lines":
      return (
        <IconSvg className={className} size={size}>
          <path d="M4 6h16M4 12h16M4 18h10" />
        </IconSvg>
      );
    case "shield":
    case "rugged":
    case "durability":
      return (
        <IconSvg className={className} size={size}>
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
          <path d="m9 12 2 2 4-4" />
        </IconSvg>
      );
    case "integration":
      return (
        <IconSvg className={className} size={size}>
          <rect x="3" y="3" width="7" height="7" rx="1" />
          <rect x="14" y="3" width="7" height="7" rx="1" />
          <rect x="3" y="14" width="7" height="7" rx="1" />
          <path d="M17.5 14v7M14 17.5h7" />
        </IconSvg>
      );
    case "battery":
      return (
        <IconSvg className={className} size={size}>
          <rect x="2" y="7" width="18" height="10" rx="2" />
          <path d="M6 7V5h4v2M22 11v2" />
          <path d="M6 11h3M6 14h3" />
        </IconSvg>
      );
    case "scan":
      return (
        <IconSvg className={className} size={size}>
          <path d="M4 7V5a1 1 0 0 1 1-1h2M20 7V5a1 1 0 0 0-1-1h-2M4 17v2a1 1 0 0 0 1 1h2M20 17v2a1 1 0 0 1-1 1h-2" />
          <path d="M7 12h3M14 12h3" />
        </IconSvg>
      );
    case "android":
      return (
        <IconSvg className={className} size={size}>
          <path d="M8 8 7 5M16 8l1-3" />
          <rect x="7" y="9" width="10" height="10" rx="2" />
          <path d="M10 14h.01M14 14h.01" />
        </IconSvg>
      );
    case "checkout":
      return (
        <IconSvg className={className} size={size}>
          <circle cx="9" cy="20" r="1.5" fill="currentColor" stroke="none" />
          <circle cx="17" cy="20" r="1.5" fill="currentColor" stroke="none" />
          <path d="M2 3h2l2.5 11h11l2-7H6" />
        </IconSvg>
      );
    case "inventory":
      return (
        <IconSvg className={className} size={size}>
          <path d="m3 7 9-4 9 4-9 4-9-4z" />
          <path d="M3 12l9 4 9-4" />
          <path d="M3 17l9 4 9-4" />
        </IconSvg>
      );
    case "store":
      return (
        <IconSvg className={className} size={size}>
          <path d="M4 10V6l8-3 8 3v4" />
          <path d="M5 10v9h14v-9" />
          <path d="M10 14h4" />
        </IconSvg>
      );
    case "loyalty":
      return (
        <IconSvg className={className} size={size}>
          <path d="m12 3 2.5 5 5.5.8-4 3.9 1 5.5L12 15.5 6.9 18.2l1-5.5-4-3.9 5.5-.8L12 3z" />
        </IconSvg>
      );
    case "install":
      return (
        <IconSvg className={className} size={size}>
          <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8" />
          <path d="M3 21 9 15M12 22H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v8" />
        </IconSvg>
      );
    case "consumables":
      return (
        <IconSvg className={className} size={size}>
          <path d="M12 2.7 17.7 8.4a6 6 0 1 1-8.5 0L12 2.7z" />
        </IconSvg>
      );
    case "maintenance":
      return (
        <IconSvg className={className} size={size}>
          <circle cx="12" cy="12" r="3" />
          <path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" />
        </IconSvg>
      );
    case "training":
      return (
        <IconSvg className={className} size={size}>
          <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
          <circle cx="9" cy="7" r="4" />
          <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75" />
        </IconSvg>
      );
    case "display":
      return (
        <IconSvg className={className} size={size}>
          <rect x="4" y="3" width="16" height="12" rx="1.5" />
          <path d="M8 19h8M12 15v4" />
          <path d="M8 7h8M8 10h5" />
        </IconSvg>
      );
    case "connectivity":
      return (
        <IconSvg className={className} size={size}>
          <path d="M5 12.55a11 11 0 0 1 14.08 0" />
          <path d="M8.53 16.11a6.5 6.5 0 0 1 6.95 0" />
          <circle cx="12" cy="20" r="1" fill="currentColor" stroke="none" />
        </IconSvg>
      );
    case "zatca":
      return (
        <IconSvg className={className} size={size}>
          <circle cx="12" cy="12" r="9" />
          <path d="M9 12l2 2 4-4" />
        </IconSvg>
      );
    case "cloud":
      return (
        <IconSvg className={className} size={size}>
          <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z" />
        </IconSvg>
      );
    case "report":
      return (
        <IconSvg className={className} size={size}>
          <path d="M4 19h16M7 16V8m5 8V5m5 11v-6" />
        </IconSvg>
      );
    case "device":
      return (
        <IconSvg className={className} size={size}>
          <rect x="7" y="2" width="10" height="20" rx="2" />
          <circle cx="12" cy="18" r="0.5" fill="currentColor" stroke="none" />
        </IconSvg>
      );
    case "print":
      return (
        <IconSvg className={className} size={size}>
          <path d="M6 9V3h12v6M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2" />
          <rect x="6" y="14" width="12" height="8" rx="1" />
        </IconSvg>
      );
    default:
      return (
        <IconSvg className={className} size={size}>
          <circle cx="12" cy="12" r="8" />
        </IconSvg>
      );
  }
}

type ProductIconFrameProps = ProductIconProps & {
  variant?: "benefit" | "spec" | "support";
};

const frameClass = {
  benefit:
    "inline-flex h-16 w-16 shrink-0 items-center justify-center rounded-md border border-product-icon/15 bg-product-icon/8 text-product-icon",
  spec: "mx-auto inline-flex h-14 w-14 items-center justify-center rounded-md border border-product-icon/15 bg-product-icon/8 text-product-icon",
  support:
    "mx-auto inline-flex h-14 w-14 items-center justify-center rounded-md border border-product-icon/15 bg-product-icon/8 text-product-icon",
};

export function ProductIconFrame({
  name,
  variant = "benefit",
  className = "",
}: ProductIconFrameProps) {
  return (
    <span className={`${frameClass[variant]} ${className}`}>
      <ProductIcon name={name} size="lg" />
    </span>
  );
}

/** @deprecated Use ProductIconFrame */
export function ProductIconBadge({
  name,
  className = "",
}: ProductIconProps) {
  return <ProductIconFrame name={name} variant="benefit" className={className} />;
}

export const trustChipIcons: Record<string, ProductIconKey> = {
  "Enterprise grade": "shield",
  "Global support": "connectivity",
  "2-Year warranty": "shield",
  "Printechs Saudi Arabia": "store",
  "IP65 rated": "shield",
  "Up to 600 dpi": "print",
  "ZATCA e-invoicing ready": "zatca",
  "ERPNext connected": "integration",
};
