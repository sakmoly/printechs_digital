export type QuoteOption = {
  id: string;
  group?: string;
  label: string;
  type: "select" | "checkbox";
  choices: string[];
  required?: boolean;
};

export type QuoteConfiguration = {
  productSlug: string;
  product: string;
  code?: string;
  brand?: string;
  category?: string;
  sourceUrl?: string;
  configureOnQuote: boolean;
  generateLead: boolean;
  quoteOptions: QuoteOption[];
};
