import type { ReactNode } from "react";

type FeatureGridProps = {
  children: ReactNode;
  columns?: 2 | 3 | 4;
};

const columnClass = {
  2: "sm:grid-cols-2",
  3: "sm:grid-cols-2 lg:grid-cols-3",
  4: "sm:grid-cols-2 lg:grid-cols-4",
};

export function FeatureGrid({ children, columns = 3 }: FeatureGridProps) {
  return (
    <div className={`grid items-stretch gap-8 ${columnClass[columns]}`}>{children}</div>
  );
}
