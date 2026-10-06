# Verification scripts

Run from the repo root. `verify-provenance.py` is the one that matters; the
other two are local-only tooling for looking at the built site.

## verify-provenance.py

The content guard. Fails (exit 1) if the site starts claiming more than the
resume does.

1. Every `highlights` string in `src/content/` must appear verbatim in
   `~/.claude/skills/job-app-tailor/resources/default_bullets.json` or in
   `Surendra_Kumar_Resume.docx`, unless the entry declares
   `provenance: approved-draft`.
2. Every number in an `improvement:` line must also appear in that same
   entry's own bullets. `improvement` is prose written for the site, so this
   is what stops a metric drifting upward during a rewrite.

```bash
python scripts/verify-provenance.py
```

Run it after editing any file under `src/content/`.

## shoot.py / interact.py

Screenshot and functional checks driven over the Chrome DevTools Protocol.
They need a preview server and a headless Chrome with a debugging port:

```bash
npm run build && npm run preview          # terminal 1

chrome --headless=new --disable-gpu --hide-scrollbars \
  --remote-debugging-port=9333 \
  --user-data-dir=/tmp/cdp-profile about:blank    # terminal 2

python scripts/shoot.py       # writes .shots/*.png (light + dark, 1440 + 390)
python scripts/interact.py    # mobile nav, theme toggle, console, network
```

`shoot.py` clears the stored theme before each capture, so the screenshots show
what a first-time visitor sees rather than whatever the last toggle left behind.
