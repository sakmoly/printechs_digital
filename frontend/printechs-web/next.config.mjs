/** @type {import('next').NextConfig} */
const basePath = process.env.NEXT_PUBLIC_BASE_PATH ?? "/newwebsite";

const nextConfig = {
  // Temporary demo preview path. Change or remove later for root/subdomain deploy.
  basePath,
  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },
  async redirects() {
    return [
      {
        source: "/resources",
        destination: "/success-stories",
        permanent: true,
      },
      {
        source: "/resources/:path*",
        destination: "/success-stories",
        permanent: true,
      },
      {
        source: "/company/partners",
        destination: "/brands",
        permanent: true,
      },
      {
        source: "/company/partners/:path*",
        destination: "/brands",
        permanent: true,
      },
      {
        source: "/brands/erpnext",
        destination: "/software/erpnext",
        permanent: true,
      },
    ];
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
