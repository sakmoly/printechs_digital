"use client";

import { useEffect } from "react";

/** Scroll to #locations (or other hash) when landing on the contact page. */
export function ContactHashScroll() {
  useEffect(() => {
    const hash = window.location.hash;
    if (!hash.startsWith("#")) return;

    const scroll = () => {
      const target = document.getElementById(hash.slice(1));
      if (!target) return false;
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      return true;
    };

    if (scroll()) return;

    let attempts = 0;
    const retry = window.setInterval(() => {
      attempts += 1;
      if (scroll() || attempts >= 15) {
        window.clearInterval(retry);
      }
    }, 100);

    return () => window.clearInterval(retry);
  }, []);

  return null;
}
