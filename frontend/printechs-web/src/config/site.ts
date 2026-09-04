export const siteConfig = {
  name: "Printechs",
  legalName: "Printechs",
  tagline: "Technology That Moves Business Forward",
  description:
    "Industrial coding, retail technology and enterprise software solutions for businesses across Saudi Arabia.",
  locale: "en",
  /** Demo / prototype environments must never be indexed. */
  allowIndexing: false,
  contactEmail: "info@printechs.com",
  contactLocation: "Riyadh, Kingdom of Saudi Arabia",
  officeHours: "Sunday – Thursday, 9:00 AM – 6:00 PM (AST)",
  whatsapp: {
    label: "Chat on WhatsApp",
    href: "https://wa.me/966550733441",
  },
  primaryCta: {
    label: "Request Quote",
    href: "/request-quote",
  },
  social: [
    {
      platform: "facebook",
      label: "Facebook",
      href: "https://www.facebook.com/Printechs/",
    },
    {
      platform: "x",
      label: "X",
      href: "https://x.com/printechssaudi",
    },
    {
      platform: "linkedin",
      label: "LinkedIn",
      href: "https://www.linkedin.com/company/printechs",
    },
    {
      platform: "instagram",
      label: "Instagram",
      href: "https://www.instagram.com/printechssaudiarabia/",
    },
  ],
  navigation: [
    { label: "Products", href: "/products" },
    { label: "Brands", href: "/brands" },
    { label: "Solutions", href: "/solutions" },
    { label: "Industries", href: "/industries" },
    { label: "Software", href: "/software" },
    { label: "Success Stories", href: "/success-stories" },
    { label: "Company", href: "/company" },
    { label: "Contact", href: "/contact" },
  ],
  footer: {
    columns: [
      {
        title: "Solutions",
        links: [
          { label: "Coding & Marking", href: "/solutions/coding-marking" },
          { label: "Retail Automation", href: "/solutions/retail-automation" },
          { label: "Warehouse Automation", href: "/solutions/warehouse-automation" },
          { label: "ERP & Business Automation", href: "/solutions/erp-business-automation" },
        ],
      },
      {
        title: "Software",
        links: [
          { label: "Modern POS", href: "/software/modern-pos" },
          { label: "ERPNext", href: "/software/erpnext" },
          { label: "WMS", href: "/software/warehouse-management-system" },
          { label: "ZATCA Integration", href: "/software/zatca-integration" },
        ],
      },
      {
        title: "Brands",
        links: [
          { label: "All Brands", href: "/brands" },
          { label: "Hitachi", href: "/brands/hitachi" },
          { label: "Zebra", href: "/brands/zebra" },
          { label: "Datalogic", href: "/brands/datalogic" },
        ],
      },
      {
        title: "Company",
        links: [
          { label: "About", href: "/company/about" },
          { label: "Events", href: "/company/events" },
          { label: "Partners", href: "/brands" },
          { label: "Success Stories", href: "/success-stories" },
          { label: "Contact", href: "/contact" },
        ],
      },
    ],
  },
} as const;
