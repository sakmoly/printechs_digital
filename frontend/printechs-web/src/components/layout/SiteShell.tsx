import type { ReactNode } from "react";
import { SiteHeader } from "@/components/navigation/SiteHeader";
import { SiteFooter } from "@/components/layout/SiteFooter";
import { getHeaderContactActions } from "@/lib/header-contact";

export async function SiteShell({ children }: { children: ReactNode }) {
  const contact = getHeaderContactActions();

  return (
    <div className="flex min-h-screen flex-col bg-paper text-ink">
      <SiteHeader contact={contact} />
      <main className="flex-1">{children}</main>
      <SiteFooter />
    </div>
  );
}
