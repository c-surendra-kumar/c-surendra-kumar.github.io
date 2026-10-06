# Design Language Reference — LangChain-inspired

> Visual reference for the portfolio rebuild. Extracted from the original
> `langchain-theme-redesign-spec.md`.
>
> **Note on provenance:** that original file carried a §2 "Feature-by-Feature
> Change List — Implemented" claiming a retheme had been applied across
> `styles.css`, `index.html`, `cv.html` and `blog.html`. It had not been — git
> reported no modifications to any of them, and `styles.css` still held the
> Bootstrap-blue palette (`--accent: #007bff`) and Roboto. That section has been
> removed so it cannot be mistaken for a record of the file state again. What
> follows (the design language itself) is the part that was always usable.

---

## 1. Design Language Reference (LangChain.com)

LangChain's marketing site reads as **calm, technical, and confident** — warm neutral background instead of stark white, restrained color, one accent color used sparingly, and generous whitespace. It leans editorial/documentation-like rather than "flashy SaaS."

### 1.1 Color Palette

| Token | Approx. Value | Usage |
|---|---|---|
| `--bg-primary` | `#F7F4EE` (warm off-white / cream) | Page background |
| `--bg-secondary` | `#FFFFFF` | Cards, elevated panels |
| `--text-primary` | `#1A1A18` (near-black, warm) | Headings, body copy |
| `--text-secondary` | `#5C5A54` (warm gray) | Subtext, captions |
| `--accent` | `#DA5F35` / burnt terracotta-orange | CTA highlights, links, small accents only |
| `--border` | `#E5E1D8` | 1px hairline borders on cards/dividers |
| `--dark-panel` | `#1A1A18` | Dark section backgrounds (footer, contrast sections), off-white text on top |

*Note: exact hex values are best-effort from visual reference, not pixel-sampled. Recommend confirming/adjusting against the live site with a color picker before final implementation — I can also do this directly if you re-enable browser access.*

**Rule of restraint:** the accent color is used sparingly — one CTA button, a link hover, a small tag/badge. It is never used as a large background fill. This is the single most important visual habit to copy.

### 1.2 Typography

- **Headings:** clean geometric/grotesque sans-serif, bold weight, tight letter-spacing, large size jumps between H1/H2 (e.g., H1 ~56–72px desktop, H2 ~36–40px).
- **Body:** same sans-serif family, regular weight, comfortable line-height (~1.6), text-secondary color for supporting copy.
- **Recommended stack:** `Inter`, `"Public Sans"`, or `"Geist Sans"` (all free, close to LangChain's grotesque feel). Avoid serif or playful fonts.
- No decorative fonts anywhere — one font family for the whole site, weight does the differentiation (400 / 500 / 600 / 700).

### 1.3 Layout & Spacing

- Wide, generous section padding (80–120px vertical between sections on desktop).
- Content max-width constrained (~1200px), lots of side margin on large screens.
- Grid-based feature sections: icon/label + short headline + 1–2 line description, repeated in a 2–4 column grid.
- Hairline `1px` borders instead of heavy shadows to separate cards.
- Rounded corners are subtle (6–10px), never pill-shaped except on small tags/badges.

### 1.4 Components

| Component | LangChain Pattern |
|---|---|
| **Navbar** | Sticky, transparent/cream background, logo left, nav links center/left, 1–2 CTA buttons right (one ghost/outline, one solid dark or accent). Minimal height. |
| **Primary Button** | Solid near-black background, white text, small rounded corners, no shadow. |
| **Secondary Button** | Outline/ghost, 1px border, same text color as body. |
| **Cards** | White or cream background, 1px hairline border, no/low shadow, icon top-left, headline, 2–3 line description. |
| **Section headers** | Small uppercase eyebrow label (accent or gray) above a large bold headline. |
| **Footer** | Dark panel (`--dark-panel`), multi-column link groups, small logo, legal links at the very bottom in a thin lighter row. |
| **Logos/social-proof strip** | Grayscale/monochrome logos in a single row, muted, no color. |

### 1.5 Motion / Interaction

- Subtle only: fade/slide-in on scroll for sections, hover states that shift opacity or underline (not color-inverting whole buttons dramatically), no bouncy/playful easing.

