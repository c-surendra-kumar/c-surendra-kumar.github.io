// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://c-surendra-kumar.github.io',
  // No `base`: the repo name matches the <username>.github.io pattern, so the
  // site root is "/". Setting `base` here would break every asset path.
  integrations: [sitemap()],
  vite: { plugins: [tailwindcss()] },
});
