export type ModernPosTourTab = {
  id: string;
  label: string;
  imageSrc: string;
  imageAlt: string;
  title: string;
  description: string;
  features: string[];
};

const SCREEN_BASE = "/images/software/modern-pos/screens";

export const MODERN_POS_TOUR_HEADING = "See Modern POS in action";

export const MODERN_POS_TOUR_SUBHEADING =
  "Explore the checkout, payments, promotions, inventory and management tools your retail team uses every day.";

export const MODERN_POS_PRODUCT_TOUR_TABS: ModernPosTourTab[] = [
  {
    id: "checkout",
    label: "Checkout",
    imageSrc: `${SCREEN_BASE}/checkout.webp`,
    imageAlt: "Modern POS retail checkout screen for Saudi Arabia",
    title: "Fast, cashier-friendly checkout",
    description:
      "Give cashiers a clean, responsive sales screen designed for high-volume retail operations.",
    features: [
      "Barcode and item search",
      "Weighed and variant items",
      "Automatic pricing and promotions",
      "Fast tender processing",
    ],
  },
  {
    id: "payment",
    label: "Payment",
    imageSrc: `${SCREEN_BASE}/payment.webp`,
    imageAlt: "Modern POS multi-payment checkout screen",
    title: "Flexible payment processing",
    description:
      "Complete transactions using multiple payment methods from a single checkout workflow.",
    features: [
      "Cash and card payments",
      "Multiple tender types",
      "Split / multi-tender payments",
      "Controlled payment completion",
    ],
  },
  {
    id: "customer",
    label: "Customer",
    imageSrc: `${SCREEN_BASE}/customer.webp`,
    imageAlt: "Modern POS customer lookup and loyalty screen at checkout",
    title: "Customer and loyalty at checkout",
    description:
      "Identify customers directly from the register and provide personalised pricing and loyalty benefits.",
    features: [
      "Customer lookup",
      "Member identification",
      "Loyalty points",
      "Purchase history",
    ],
  },
  {
    id: "promotions",
    label: "Promotions",
    imageSrc: `${SCREEN_BASE}/promotions.webp`,
    imageAlt: "Modern POS retail promotions and discount screen",
    title: "Powerful retail promotions",
    description:
      "Apply centrally managed offers automatically during checkout without slowing down the cashier.",
    features: [
      "Percentage and amount discounts",
      "Mix-and-match promotions",
      "Member pricing",
      "Manager-controlled overrides",
    ],
  },
  {
    id: "inventory",
    label: "Inventory",
    imageSrc: `${SCREEN_BASE}/inventory.webp`,
    imageAlt: "Modern POS real-time retail inventory lookup",
    title: "Real-time inventory visibility",
    description:
      "Allow store teams to check available stock without leaving the sales workflow.",
    features: [
      "Current store stock",
      "Other branch availability",
      "Warehouse visibility",
      "Variant-level inventory",
    ],
  },
  {
    id: "returns",
    label: "Returns",
    imageSrc: `${SCREEN_BASE}/returns.webp`,
    imageAlt: "Modern POS returns and exchange screen",
    title: "Controlled returns and exchanges",
    description:
      "Process customer returns through a controlled workflow linked to the original transaction.",
    features: [
      "Original invoice lookup",
      "Return validation",
      "Refund processing",
      "Supervisor controls",
    ],
  },
  {
    id: "manager",
    label: "Manager",
    imageSrc: `${SCREEN_BASE}/manager.webp`,
    imageAlt: "Modern POS store manager controls and supervisor screen",
    title: "Store management and control",
    description:
      "Give supervisors visibility and control over sensitive register operations.",
    features: [
      "Manager overrides",
      "Discount approval",
      "Void controls",
      "Cashier and store monitoring",
    ],
  },
  {
    id: "erpnext",
    label: "ERPNext",
    imageSrc: `${SCREEN_BASE}/erpnext.webp`,
    imageAlt: "Modern POS ERPNext retail integration",
    title: "Connected to ERPNext",
    description:
      "Connect retail transactions with finance, inventory, purchasing and warehouse operations.",
    features: [
      "Sales synchronization",
      "Item and price synchronization",
      "Inventory synchronization",
      "Centralised back-office operations",
    ],
  },
];
