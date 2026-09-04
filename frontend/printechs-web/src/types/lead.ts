export type LeadType = "quote" | "contact" | "demo";

export type LeadContext = {
  productSlug?: string;
  solutionSlug?: string;
  product?: string;
  code?: string;
  brand?: string;
  category?: string;
  sourceUrl?: string;
  preferredTime?: string;
  inquiryType?: string;
  preferredContactMethod?: string;
  configuration?: string;
  generateLead?: boolean;
};

export type LeadSubmission = {
  type: LeadType;
  name: string;
  company: string;
  email: string;
  phone: string;
  message?: string;
  context?: LeadContext;
};

export type LeadSubmissionResult = {
  ok: true;
  reference: string;
  message: string;
};
