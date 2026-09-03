import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Channel form enables Tailwind opacity modifiers (bg-ink/95, text-paper/75).
        background: "rgb(var(--background-rgb) / <alpha-value>)",
        foreground: "rgb(var(--foreground-rgb) / <alpha-value>)",
        ink: "rgb(var(--ink-rgb) / <alpha-value>)",
        steel: "rgb(var(--steel-rgb) / <alpha-value>)",
        slate: "rgb(var(--slate-rgb) / <alpha-value>)",
        paper: "rgb(var(--paper-rgb) / <alpha-value>)",
        mist: "rgb(var(--mist-rgb) / <alpha-value>)",
        white: "rgb(var(--white-rgb) / <alpha-value>)",
        signal: {
          DEFAULT: "rgb(var(--signal-rgb) / <alpha-value>)",
          bright: "rgb(var(--signal-bright-rgb) / <alpha-value>)",
          deep: "rgb(var(--signal-deep-rgb) / <alpha-value>)",
        },
        accent: {
          DEFAULT: "rgb(var(--accent-rgb) / <alpha-value>)",
          bright: "rgb(var(--accent-bright-rgb) / <alpha-value>)",
        },
        line: "var(--line)",
        "line-strong": "var(--line-strong)",
        "product-icon": "rgb(var(--product-icon-rgb) / <alpha-value>)",
      },
      fontFamily: {
        display: ["var(--font-display)", "Sora", "sans-serif"],
        body: ["var(--font-body)", "Source Sans 3", "sans-serif"],
      },
      maxWidth: {
        content: "90rem",
      },
      boxShadow: {
        soft: "0 18px 50px rgba(11, 18, 32, 0.08)",
        lift: "0 22px 40px rgba(11, 18, 32, 0.12)",
      },
      transitionTimingFunction: {
        premium: "cubic-bezier(0.22, 1, 0.36, 1)",
      },
    },
  },
  plugins: [],
};
export default config;
