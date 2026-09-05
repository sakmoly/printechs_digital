"use client";

import { useRef, useState } from "react";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { withBasePath } from "@/lib/paths";
import { trackVideoEvent } from "@/lib/analytics/events";
import { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";

type PosterVideoProps = {
  type: "youtube" | "vimeo" | "hosted";
  source: string;
  title: string;
  poster?: string;
  className?: string;
  productName?: string;
  brand?: string;
};

export function PosterVideo({
  type,
  source,
  title,
  poster,
  className = "",
  productName,
  brand,
}: PosterVideoProps) {
  const [playing, setPlaying] = useState(false);
  const fired = useRef({ start: false, complete: false });
  const hostedMilestones = useRef({ p25: false, p50: false, p75: false });
  const posterSrc = poster
    ? withBasePath(poster)
    : "/images/placeholders/video-poster.svg";

  function videoParams() {
    return {
      video_title: title,
      product_name: productName,
      brand,
      page_title: getPageTitle(),
      page_location: getPageLocation(window.location.pathname, window.location.search),
    };
  }

  function handlePlayStart() {
    if (fired.current.start) return;
    fired.current.start = true;
    trackVideoEvent("video_start", videoParams());
  }

  function handleHostedTimeUpdate(currentTime: number, duration: number) {
    if (!duration) return;
    const ratio = currentTime / duration;
    const milestones = hostedMilestones.current;
    if (ratio >= 0.25 && !milestones.p25) {
      milestones.p25 = true;
      trackVideoEvent("video_25_percent", videoParams());
    }
    if (ratio >= 0.5 && !milestones.p50) {
      milestones.p50 = true;
      trackVideoEvent("video_50_percent", videoParams());
    }
    if (ratio >= 0.75 && !milestones.p75) {
      milestones.p75 = true;
      trackVideoEvent("video_75_percent", videoParams());
    }
  }

  if (playing) {
    if (type === "youtube" || type === "vimeo") {
      const embedSrc =
        type === "vimeo"
          ? `https://player.vimeo.com/video/${source}?autoplay=1`
          : `https://www.youtube-nocookie.com/embed/${source}?autoplay=1&rel=0`;
      return (
        <div className={`aspect-video overflow-hidden bg-ink ${className}`}>
          <iframe
            className="h-full w-full"
            src={embedSrc}
            title={title}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      );
    }

    return (
      <HostedTrackedVideo
        source={source}
        title={title}
        poster={posterSrc}
        className={className}
        onStart={handlePlayStart}
        onProgress={handleHostedTimeUpdate}
        onComplete={() => {
          if (fired.current.complete) return;
          fired.current.complete = true;
          trackVideoEvent("video_complete", videoParams());
        }}
      />
    );
  }

  return (
    <button
      type="button"
      onClick={() => {
        handlePlayStart();
        setPlaying(true);
      }}
      className={`group relative block aspect-video w-full overflow-hidden bg-ink text-left focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal ${className}`}
      aria-label={`Play video: ${title}`}
    >
      <ImageFrame
        src={posterSrc}
        alt=""
        spec={IMAGE_SPECS.videoPoster}
        fill
        className="h-full w-full"
        imageClassName="object-cover transition duration-700 ease-premium group-hover:scale-105"
        sizes="(max-width: 1440px) 100vw, 88rem"
        overlay={
          <>
            <div className="absolute inset-0 bg-ink/35 transition group-hover:bg-ink/25" />
            <span className="absolute left-1/2 top-1/2 flex h-16 w-16 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full bg-signal text-ink shadow-lift transition group-hover:scale-105 sm:h-20 sm:w-20">
              <span className="ml-1 border-y-[10px] border-l-[16px] border-y-transparent border-l-ink" />
            </span>
          </>
        }
      />
    </button>
  );
}

function HostedTrackedVideo({
  source,
  title,
  poster,
  className,
  onStart,
  onProgress,
  onComplete,
}: {
  source: string;
  title: string;
  poster: string;
  className: string;
  onStart: () => void;
  onProgress: (currentTime: number, duration: number) => void;
  onComplete: () => void;
}) {
  const started = useRef(false);

  return (
    <div className={`aspect-video overflow-hidden bg-ink ${className}`}>
      <video
        className="h-full w-full object-cover"
        controls
        autoPlay
        preload="metadata"
        poster={withBasePath(poster)}
        title={title}
        onPlay={() => {
          if (started.current) return;
          started.current = true;
          onStart();
        }}
        onTimeUpdate={(event) => {
          const video = event.currentTarget;
          onProgress(video.currentTime, video.duration);
        }}
        onEnded={onComplete}
      >
        <source src={withBasePath(source)} />
      </video>
    </div>
  );
}
