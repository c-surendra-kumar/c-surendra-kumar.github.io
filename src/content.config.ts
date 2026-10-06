import { defineCollection } from 'astro:content';
import { glob, file } from 'astro/loaders';
import { z } from 'astro/zod';

/**
 * Where a claim came from. Every bullet on this site is traceable to one of
 * these, which is what stops the resume and the site drifting apart again.
 *
 *  resume          - verbatim from resources/Surendra_Kumar_Resume.docx
 *  default_bullets - verbatim from resources/default_bullets.json
 *                    (rewrites, alternates, or presets)
 *  approved-draft  - drafted here and explicitly approved, then written back
 *                    into default_bullets.json so both stay in sync
 *  site-carryover  - a non-metric fact carried from the previous site that
 *                    appears in neither source (e.g. a lab name, a patent)
 */
const provenance = z.enum([
  'resume',
  'default_bullets',
  'approved-draft',
  'site-carryover',
]);

const projects = defineCollection({
  loader: glob({ base: './src/content/projects', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    tagline: z.string(),
    start: z.string(),
    end: z.string(),
    stack: z.array(z.string()).min(1),
    highlights: z.array(z.string()).min(1),
    /* One Problem / Solution / Improvement triple per distinct problem the
       role or project tackled. Several of these involved genuinely separate
       problems (Kaar had three bottlenecks, CaseSage four modules), and
       collapsing them into one paragraph hid that.

       `problem` is authored framing of the domain and carries no claim about
       Surendra's results. `solution`, `improvement` and every `metrics` value
       stay grounded in `highlights`; scripts/verify-provenance.py enforces
       that each figure also appears in a sanctioned bullet. `direction` is the
       direction of the change, not a judgement: all of these are
       improvements. */
    segments: z
      .array(
        z.object({
          label: z.string().optional(),
          problem: z.string(),
          solution: z.string(),
          improvement: z.string().optional(),
          metrics: z
            .array(
              z.object({
                value: z.string(),
                label: z.string(),
                direction: z.enum(['up', 'down', 'flat']).default('flat'),
              }),
            )
            .default([]),
        }),
      )
      .min(1),
    provenance,
    figuresFrom: z.string().optional(),
    /* Live demos, writeups, repos. Rendered only when present, so a project
       without one shows nothing rather than a dead affordance. */
    links: z
      .array(z.object({ label: z.string(), url: z.url() }))
      .default([]),
    featured: z.boolean().default(true),
    order: z.number(),
  }),
});

const experience = defineCollection({
  loader: glob({ base: './src/content/experience', pattern: '**/*.md' }),
  schema: z.object({
    role: z.string(),
    org: z.string(),
    orgUrl: z.url().optional(),
    /** 1-3 chars for the monogram tile when no logo file is present. */
    mark: z.string().max(3),
    start: z.string(),
    end: z.string(),
    current: z.boolean().default(false),
    stack: z.array(z.string()).min(1),
    highlights: z.array(z.string()).min(1),
    /* One Problem / Solution / Improvement triple per distinct problem the
       role or project tackled. Several of these involved genuinely separate
       problems (Kaar had three bottlenecks, CaseSage four modules), and
       collapsing them into one paragraph hid that.

       `problem` is authored framing of the domain and carries no claim about
       Surendra's results. `solution`, `improvement` and every `metrics` value
       stay grounded in `highlights`; scripts/verify-provenance.py enforces
       that each figure also appears in a sanctioned bullet. `direction` is the
       direction of the change, not a judgement: all of these are
       improvements. */
    segments: z
      .array(
        z.object({
          label: z.string().optional(),
          problem: z.string(),
          solution: z.string(),
          improvement: z.string().optional(),
          metrics: z
            .array(
              z.object({
                value: z.string(),
                label: z.string(),
                direction: z.enum(['up', 'down', 'flat']).default('flat'),
              }),
            )
            .default([]),
        }),
      )
      .min(1),
    provenance,
    /* Where this entry's figures come from when they are not in the resume or
       default_bullets - e.g. the author's own paper. verify-provenance.py
       reports these as a declared source instead of failing, so the exception
       stays visible rather than becoming an invisible allowlist. */
    figuresFrom: z.string().optional(),
    order: z.number(),
  }),
});

const publications = defineCollection({
  loader: file('./src/content/publications.json'),
  schema: z.object({
    title: z.string(),
    venue: z.string(),
    venueShort: z.string(),
    year: z.number(),
    authors: z.array(z.string()).min(1),
    self: z.string(),
    url: z.url().optional(),
    abstract: z.string(),
    order: z.number(),
  }),
});

const posts = defineCollection({
  loader: glob({ base: './src/content/posts', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects, experience, publications, posts };
