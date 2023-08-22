import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import nodejs from "@astrojs/node";

import node from "@astrojs/node";

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  adapter: node({
    mode: "standalone",
  }),
  output: "hybrid",
  redirects: {
    "/course": "/",
  },
});
