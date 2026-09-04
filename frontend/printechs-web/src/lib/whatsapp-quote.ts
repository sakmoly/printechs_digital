export function buildWhatsAppQuoteLink(
  whatsappHref: string,
  details: {
    name: string;
    company: string;
    phone: string;
    email: string;
    message: string;
  },
) {
  const base = whatsappHref.split("?")[0];
  const text = [
    "Hello Printechs, I submitted a quote request on your website.",
    "",
    `Name: ${details.name}`,
    `Company: ${details.company}`,
    `Phone: ${details.phone}`,
    `Email: ${details.email}`,
    "",
    "Details:",
    details.message,
  ].join("\n");

  return `${base}?text=${encodeURIComponent(text)}`;
}
