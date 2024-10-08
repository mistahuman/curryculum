import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

export default {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter({
      pages: 'dist',
      assets: 'dist',
      fallback: null,
      precompress: false,
      strict: true,
    }),
    // Set base for GitHub Pages deployment via env variable:
    // PUBLIC_BASE_PATH=/template-svelte-skeleton npm run build
    paths: {
      base: process.env.PUBLIC_BASE_PATH ?? '',
    },
    files: {
      assets: 'public',
    },
    alias: {
      '@components': 'src/components',
      '@layouts': 'src/layouts',
      '@styles': 'src/styles',
      '@assets': 'src/assets',
    },
  },
};
