import type { ReactNode } from "react";

export function Badge({ children }: { children: ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-sm border border-ink/10 bg-mist px-2.5 py-1 text-xs font-medium uppercase tracking-wide text-slate">
      {children}
    </span>
  );
}
