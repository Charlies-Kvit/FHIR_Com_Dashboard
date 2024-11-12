import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";
import adapter from "@sveltejs/adapter-static";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter(),
    // files: {
    //   routes: "src/app/routes",
    //   lib: "src",
    //   appTemplate: "src/app/index.html",
    //   assets: "public",
    // },
    // alias: {
    //   "@/*": "src/*", // Create an alias for the src directory
    // },
  },
};

export default config;
