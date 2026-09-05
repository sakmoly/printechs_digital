"use client";

import { useEffect, useRef } from "react";
import { trackVideoEvent } from "@/lib/analytics/events";
import { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";

type TrackedVideoProps = {
  videoTitle: string;
  productName?: string;
  brand?: string;
  children: (bind: {
    onPlay: () => void;
    onTimeUpdate: (currentTime: number, duration: number) => void;
    onEnded: () => void;
  }) => React.ReactNode;
};

export function TrackedVideo({
  videoTitle,
  productName,
  brand,
  children,
}: TrackedVideoProps) {
  const fired = useRef({
    start: false,
    p25: false,
    p50: false,
    p75: false,
    complete: false,
  });

  useEffect(() => {
    fired.current = { start: false, p25: false, p50: false, p75: false, complete: false };
  }, [videoTitle]);

  function baseParams() {
    return {
      video_title: videoTitle,
      product_name: productName,
      brand,
      page_title: getPageTitle(),
      page_location: getPageLocation(window.location.pathname, window.location.search),
    };
  }

  return (
    <>
      {children({
        onPlay: () => {
          if (fired.current.start) return;
          fired.current.start = true;
          trackVideoEvent("video_start", baseParams());
        },
        onTimeUpdate: (currentTime, duration) => {
          if (!duration || duration <= 0) return;
          const ratio = currentTime / duration;
          if (ratio >= 0.25 && !fired.current.p25) {
            fired.current.p25 = true;
            trackVideoEvent("video_25_percent", baseParams());
          }
          if (ratio >= 0.5 && !fired.current.p50) {
            fired.current.p50 = true;
            trackVideoEvent("video_50_percent", baseParams());
          }
          if (ratio >= 0.75 && !fired.current.p75) {
            fired.current.p75 = true;
            trackVideoEvent("video_75_percent", baseParams());
          }
        },
        onEnded: () => {
          if (fired.current.complete) return;
          fired.current.complete = true;
          trackVideoEvent("video_complete", baseParams());
        },
      })}
    </>
  );
}
