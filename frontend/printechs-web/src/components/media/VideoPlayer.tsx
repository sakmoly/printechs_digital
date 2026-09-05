"use client";

import { useEffect, useRef } from "react";
import { withBasePath } from "@/lib/paths";
import { trackVideoEvent } from "@/lib/analytics/events";
import { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";

type VideoPlayerProps = {
  type: "youtube" | "hosted";
  source: string;
  title: string;
  poster?: string;
  className?: string;
  productName?: string;
  brand?: string;
};

export function VideoPlayer({
  type,
  source,
  title,
  poster,
  className = "",
  productName,
  brand,
}: VideoPlayerProps) {
  const started = useRef(false);
  const milestones = useRef({ p25: false, p50: false, p75: false, complete: false });

  function videoParams() {
    return {
      video_title: title,
      product_name: productName,
      brand,
      page_title: getPageTitle(),
      page_location: getPageLocation(window.location.pathname, window.location.search),
    };
  }

  useEffect(() => {
    if (type !== "youtube" || started.current) return;
    started.current = true;
    trackVideoEvent("video_start", videoParams());
  }, [type, title, productName, brand]);

  const posterSrc = poster ? withBasePath(poster) : undefined;

  if (type === "youtube") {
    return (
      <div className={`aspect-video overflow-hidden bg-ink ${className}`}>
        <iframe
          className="h-full w-full"
          src={`https://www.youtube-nocookie.com/embed/${source}`}
          title={title}
          loading="lazy"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        />
      </div>
    );
  }

  return (
    <div className={`aspect-video overflow-hidden bg-ink ${className}`}>
      <video
        className="h-full w-full object-cover"
        controls
        preload="metadata"
        poster={posterSrc}
        title={title}
        onPlay={() => {
          if (started.current) return;
          started.current = true;
          trackVideoEvent("video_start", videoParams());
        }}
        onTimeUpdate={(event) => {
          const video = event.currentTarget;
          if (!video.duration) return;
          const ratio = video.currentTime / video.duration;
          if (ratio >= 0.25 && !milestones.current.p25) {
            milestones.current.p25 = true;
            trackVideoEvent("video_25_percent", videoParams());
          }
          if (ratio >= 0.5 && !milestones.current.p50) {
            milestones.current.p50 = true;
            trackVideoEvent("video_50_percent", videoParams());
          }
          if (ratio >= 0.75 && !milestones.current.p75) {
            milestones.current.p75 = true;
            trackVideoEvent("video_75_percent", videoParams());
          }
        }}
        onEnded={() => {
          if (milestones.current.complete) return;
          milestones.current.complete = true;
          trackVideoEvent("video_complete", videoParams());
        }}
      >
        <source src={source.startsWith("http") ? source : withBasePath(source)} />
        Your browser does not support the video tag.
      </video>
    </div>
  );
}
