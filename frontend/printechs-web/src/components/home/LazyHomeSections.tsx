import dynamic from "next/dynamic";
import type { Brand } from "@/types/content";
import type { Video } from "@/types/content";

const VideoSectionClient = dynamic(
  () => import("@/components/home/VideoSection").then((mod) => mod.VideoSection),
  { loading: () => <div className="min-h-[320px] bg-ink" aria-hidden /> },
);

const BrandsSectionClient = dynamic(
  () => import("@/components/home/BrandsSection").then((mod) => mod.BrandsSection),
  { loading: () => <div className="min-h-[240px] bg-white" aria-hidden /> },
);

export function LazyVideoSection({
  video,
  eyebrow,
}: {
  video: Video;
  eyebrow?: string;
}) {
  return <VideoSectionClient video={video} eyebrow={eyebrow} />;
}

export function LazyBrandsSection({ brands }: { brands: Brand[] }) {
  return <BrandsSectionClient brands={brands} />;
}
