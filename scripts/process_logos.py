"""
Turn the downloaded raw logo files into trimmed, transparent-background PNGs.

Flood-fills the background inward from the border rather than keying out every
pixel of that colour, so white *inside* a mark (counters in letters, a white
glyph on a coloured disc) survives. Then trims to the ink and squares it up, so
every tile renders at the same optical size regardless of the source padding.
"""
from collections import deque
from pathlib import Path
import sys

from PIL import Image

HERE = Path(__file__).resolve().parent.parent / 'src/assets/logos'
TOLERANCE = 32      # per-channel distance from the border colour
OUT_SIZE = 256      # square canvas written to disk
PAD = 0.06          # breathing room inside the square, as a fraction


def has_real_alpha(im: Image.Image) -> bool:
    if im.mode not in ('RGBA', 'LA'):
        return False
    alpha = im.getchannel('A')
    lo, hi = alpha.getextrema()
    return lo < 250          # something is actually transparent


def flood_background(im: Image.Image, tol: int = TOLERANCE) -> Image.Image:
    """Make the border-connected background transparent."""
    im = im.convert('RGBA')
    w, h = im.size
    px = im.load()
    assert px is not None

    # Reference colour: the most common of the four corners.
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    ref = max(set(c[:3] for c in corners), key=[c[:3] for c in corners].count)

    def near(c) -> bool:
        return all(abs(c[i] - ref[i]) <= tol for i in range(3))

    seen = bytearray(w * h)
    q: deque[tuple[int, int]] = deque()

    for x in range(w):
        for y in (0, h - 1):
            if near(px[x, y]):
                q.append((x, y)); seen[y * w + x] = 1
    for y in range(h):
        for x in (0, w - 1):
            if near(px[x, y]) and not seen[y * w + x]:
                q.append((x, y)); seen[y * w + x] = 1

    while q:
        x, y = q.popleft()
        px[x, y] = (px[x, y][0], px[x, y][1], px[x, y][2], 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx]:
                if near(px[nx, ny]):
                    seen[ny * w + nx] = 1
                    q.append((nx, ny))

    return im


def square(im: Image.Image, size: int = OUT_SIZE) -> Image.Image:
    """Trim to the visible ink, then centre it on a transparent square."""
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    inner = int(size * (1 - 2 * PAD))
    # Scale to fit in BOTH directions: thumbnail() only ever shrinks, which
    # left small glyphs marooned in the middle of the canvas.
    scale = min(inner / im.width, inner / im.height)
    im = im.resize((max(1, round(im.width * scale)),
                    max(1, round(im.height * scale))), Image.LANCZOS)
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    canvas.paste(im, ((size - im.width) // 2, (size - im.height) // 2), im)
    return canvas


def main() -> int:
    raws = sorted(HERE.glob('_raw_*'))
    if not raws:
        print('no _raw_* files found', file=sys.stderr)
        return 1

    for raw in raws:
        slug = raw.name.removeprefix('_raw_')
        im = Image.open(raw)

        if has_real_alpha(im):
            out, how = im.convert('RGBA'), 'kept existing alpha'
        else:
            out, how = flood_background(im), 'flood-filled background'

        out = square(out)
        dest = HERE / f'{slug}.png'
        out.save(dest, 'PNG', optimize=True)

        opaque = sum(1 for p in out.getdata() if p[3] > 8)
        pct = 100 * opaque / (out.width * out.height)
        print(f'  {slug:20} {how:26} -> {dest.name:24} '
              f'{dest.stat().st_size // 1024:3} kB  {pct:4.1f}% ink')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
