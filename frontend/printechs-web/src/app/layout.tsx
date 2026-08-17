import type { Metadata } from "next";
import { Sora, Source_Sans_3 } from "next/font/google";
import { SiteShell } from "@/components/layout/SiteShell";
import { buildMetadata } from "@/lib/seo";
import "./globals.css";

const display = Sora({
  subsets: ["latin"],
  variable: "--font-display",
  weight: ["500", "600", "700"],
});

const body = Source_Sans_3({
  subsets: ["latin"],
  variable: "--font-body",
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = buildMetadata({
  title: "Printechs | Technology That Moves Business Forward",
  description:
    "Industrial coding, retail technology and enterprise software solutions for businesses across Saudi Arabia.",
  canonicalPath: "/",
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${display.variable} ${body.variable} font-body antialiased`}>
        <SiteShell>{children}</SiteShell>
      </body>
    </html>
  );
}
