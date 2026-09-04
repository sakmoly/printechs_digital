import { siteConfig } from "@/config/site";

export type HeaderContactActions = {
  whatsapp?: {
    label: string;
    href: string;
  } | null;
};

export function getHeaderContactActions(): HeaderContactActions {
  return {
    whatsapp: siteConfig.whatsapp,
  };
}
