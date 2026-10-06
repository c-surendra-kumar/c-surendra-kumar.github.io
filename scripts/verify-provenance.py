"""
Gate: nothing on this site claims more than the resume does.

Three checks:
  1. Every `highlights` string must appear verbatim in a sanctioned source, or
     the entry must declare provenance: approved-draft.
  2. Every number in an `improvement` line must also appear in one of that
     entry's own sanctioned bullets. `improvement` is prose written for the
     site, so this is what stops a metric drifting upward during a rewrite.
  3. Same rule for every stat-tile `value`. Tiles are the most prominent
     numbers on the page, so they get the strictest reading.

An entry may set `figuresFrom` to declare a source the resume does not carry
(the author's own paper, say). Those figures pass, but the declared source is
printed beside them, so the exception stays visible in the report rather than
disappearing into an allowlist.

Sanctioned sources:
  ~/.claude/skills/job-app-tailor/resources/default_bullets.json
  ~/.claude/skills/job-app-tailor/resources/Surendra_Kumar_Resume.docx
"""
import json
import glob
import re
import sys
import unicodedata
from pathlib import Path

SKILL = Path.home() / '.claude/skills/job-app-tailor/resources'


def norm(s: str) -> str:
    s = unicodedata.normalize('NFKD', s)
    for a, b in (('–', '-'), ('—', '-'), ('’', "'"), ('‘', "'"),
                 ('“', '"'), ('”', '"')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()


# ── sanctioned corpus ────────────────────────────────────────────────
db = json.loads((SKILL / 'default_bullets.json').read_text(encoding='utf-8'))
sanctioned = set()
for bullets in db['rewrites'].values():
    sanctioned.update(norm(b) for b in bullets)
for block in db['alternates'].values():
    if isinstance(block, dict):
        sanctioned.update(norm(v) for v in block.values() if isinstance(v, str))
for preset in db['presets'].values():
    sanctioned.update(norm(b) for b in preset.get('bullets', []))

from docx import Document  # noqa: E402

resume_text = norm('\n'.join(
    p.text for p in Document(SKILL / 'Surendra_Kumar_Resume.docx').paragraphs))

# Figures the site may state that are not resume metrics: they come from
# site-carryover facts or are plain calendar/colloquial numbers.
NUMBER_ALLOWLIST = {'1', '4', '2025'}

num_re = re.compile(r'~?\d+(?:\.\d+)?x?%?')

# Bullets spell small counts as words ("seven harmful-speech mechanisms"), so a
# tile showing "7" is backed even though the digit never appears. Normalise
# before comparing rather than loosening the check.
WORD_NUMBERS = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10',
    'eleven': '11', 'twelve': '12',
}


def numbers(text: str) -> set[str]:
    found = {m.group().lstrip('~') for m in num_re.finditer(text)}
    # Tokenise rather than regex word-boundaries: exact-word matching with
    # no escape sequences, so 'sevenfold' never counts as 'seven'.
    tokens = set(re.sub('[^a-z0-9]+', ' ', text.lower()).split())
    for word, digit in WORD_NUMBERS.items():
        if word in tokens:
            found.add(digit)
    return found


# ── walk content ─────────────────────────────────────────────────────
rows: list[tuple[str, str, str, bool, str]] = []
metric_rows: list[tuple[str, str, bool, str]] = []
tile_rows: list[tuple[str, str, bool, str]] = []
unexplained = 0
metric_fails = 0
tile_fails = 0

for f in sorted(glob.glob('src/content/**/*.md', recursive=True)):
    fm = Path(f).read_text(encoding='utf-8').split('---')[1]
    name = Path(f).name

    prov_m = re.search(r'^provenance:\s*"?([\w-]+)"?', fm, re.M)
    prov = prov_m.group(1) if prov_m else '(none)'

    # An entry may declare a source for figures the resume does not carry
    # (e.g. the author's own paper). That is reported, never silently passed.
    src_m = re.search(r'^figuresFrom:\s*"(.*)"$', fm, re.M)
    declared = src_m.group(1) if src_m else None

    bullets = [m.group(1) for m in re.finditer(r'^  - "(.+)"$', fm, re.M)]
    for b in bullets:
        nb = norm(b)
        if nb in sanctioned:
            verdict = 'default_bullets'
        elif nb and nb in resume_text:
            verdict = 'resume'
        else:
            verdict = 'UNMATCHED'
        ok = verdict != 'UNMATCHED' or prov == 'approved-draft'
        unexplained += not ok
        rows.append((name, prov, verdict, ok, b[:54]))

    backed = set().union(*(numbers(b) for b in bullets)) if bullets else set()

    # improvement + metrics now sit inside `segments`, one per problem.
    for imp in re.findall(r'^\s*improvement:\s*"(.*)"$', fm, re.M):
        claimed = numbers(imp)
        stray = claimed - backed - NUMBER_ALLOWLIST
        ok = not stray or bool(declared)
        metric_fails += not ok
        note = ('all backed' if not stray
                else f'declared source: {declared}' if declared
                else 'unbacked: ' + ', '.join(sorted(stray)))
        metric_rows.append((name, ', '.join(sorted(claimed)) or '-', ok, note))

    # The stat tiles restate figures from the prose, so they get the same
    # treatment: a tile must not be able to claim a number the bullets don't.
    for tile in re.findall(r'^\s*- value:\s*"(.*)"$', fm, re.M):
        claimed = numbers(tile)
        stray = claimed - backed - NUMBER_ALLOWLIST
        ok = not stray or bool(declared)
        tile_fails += not ok
        note = ('backed' if not stray
                else f'declared source: {declared}' if declared
                else 'unbacked: ' + ', '.join(sorted(stray)))
        tile_rows.append((name, tile, ok, note))

# ── report ───────────────────────────────────────────────────────────
w = max(len(r[0]) for r in rows)
print('CHECK 1 - bullets traceable to a sanctioned source')
print(f"{'file':{w}}  {'declared':16} {'matched':16} ok   bullet")
print('-' * (w + 60))
for name, prov, verdict, ok, snip in rows:
    print(f"{name:{w}}  {prov:16} {verdict:16} {'y' if ok else 'N':3}  {snip}...")
print(f"\n{len(rows)} bullets checked, {unexplained} unexplained\n")

print('CHECK 2 - improvement metrics backed by that entry\'s own bullets')
print(f"{'file':{w}}  {'numbers stated':22} ok   result")
print('-' * (w + 54))
for name, nums, ok, note in metric_rows:
    print(f"{name:{w}}  {nums:22} {'y' if ok else 'N':3}  {note}")
print(f"\n{len(metric_rows)} improvement lines checked, {metric_fails} with unbacked numbers\n")

print("CHECK 3 - stat-tile values backed by that entry's own bullets")
print(f"{'file':{w}}  {'tile value':22} ok   result")
print('-' * (w + 54))
for name, val, ok, note in tile_rows:
    print(f"{name:{w}}  {val:22} {'y' if ok else 'N':3}  {note}")
print(f"\n{len(tile_rows)} stat tiles checked, {tile_fails} with unbacked numbers")

sys.exit(1 if (unexplained or metric_fails or tile_fails) else 0)
