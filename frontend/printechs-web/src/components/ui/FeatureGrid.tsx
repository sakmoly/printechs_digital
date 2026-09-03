import type { ReactNode } from "react";

type FeatureGridProps = {
  children: ReactNode;
  columns?: 2 | 3 | 4;
  gap?: "sm" | "md" | "lg";
};

const columnClass = {
  2: "sm:grid-cols-2",
  3: "sm:grid-cols-2 lg:grid-cols-3",
  4: "sm:grid-cols-2 lg:grid-cols-4",
};

const gapClass = {
  sm: "gap-4",
  md: "gap-6",
  lg: "gap-8",
};

export function FeatureGrid({ children, columns = 3, gap = "lg" }: FeatureGridProps) {
  return (
    <div className={`grid items-stretch ${gapClass[gap]} ${columnClass[columns]}`}>
      {children}
    </div>
  );
}
