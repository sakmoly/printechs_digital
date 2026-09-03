/** @type {import('next').NextConfig} */
const basePath = "/newwebsite";

const nextConfig = {
  // Temporary demo preview path. Change or remove later for root/subdomain deploy.
  basePath,
  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "printechs.com",
        pathname: "/files/**",
      },
      {
        protocol: "https",
        hostname: "demo.printechs.com",
        pathname: "/files/**",
      },
    ],
  },
};

export default nextConfig;
