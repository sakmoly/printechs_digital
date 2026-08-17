/** @type {import('next').NextConfig} */
const basePath = "/newwebsite";

const nextConfig = {
  // Temporary demo preview path. Change or remove later for root/subdomain deploy.
  basePath,
  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },
};

export default nextConfig;
