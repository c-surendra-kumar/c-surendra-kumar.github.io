"""
Build the favicon: a rocket mark in the site's palette.

Drawn as vector paths rather than an emoji or an SVG <text> glyph. A favicon
renders in a sandbox that loads no webfonts, and emoji rasterise differently on
every platform, so a path is the only way the mark looks the same everywhere.

The silhouette is deliberately heavy and the details few: at 16px, thin fins and
small windows turn to mush. The window is a cut-out rather than a second fill,
so it stays crisp at any size.

Writes:
  public/favicon.svg          vector, used by modern browsers
  public/favicon-32.png       raster fallback
  public/apple-touch-icon.png home-screen icon (square, opaque - iOS masks it)
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public'

ACCENT = '#c2410c'   # terracotta, the site's accent
CREAM = '#f7f4ee'    # the site's canvas
BOX = 32
RADIUS = 7

# Rocket, drawn on a 32x32 grid. Body and fins are one cream group; the window
# is punched out of the body with fill-rule evenodd so it reads as a hole.
BODY = (
    'M16 3.4'
    'c3.1 2.9 4.9 6.9 4.9 11.1'
    'v6.2'
    'c0 1.5-1.2 2.7-2.7 2.7'
    'h-4.4'
    'c-1.5 0-2.7-1.2-2.7-2.7'
    'v-6.2'
    'c0-4.2 1.8-8.2 4.9-11.1'
    'Z'
)
WINDOW = 'M16 9.6a2.7 2.7 0 1 0 0 5.4 2.7 2.7 0 1 0 0-5.4Z'
FIN_L = 'M10.3 16.1 6.6 21.9c-.5.8.1 1.8 1 1.6l2.7-.6Z'
FIN_R = 'M21.7 16.1l3.7 5.8c.5.8-.1 1.8-1 1.6l-2.7-.6Z'
FLAME = 'M13.9 25.6c0 2.3 1 3.9 2.1 5 1.1-1.1 2.1-2.7 2.1-5Z'


def build_svg(radius: int = RADIUS) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BOX} {BOX}">
  <title>Surendra Kumar</title>
  <rect width="{BOX}" height="{BOX}" rx="{radius}" fill="{ACCENT}"/>
  <g fill="{CREAM}">
    <path fill-rule="evenodd" d="{BODY}{WINDOW}"/>
    <path d="{FIN_L}"/>
    <path d="{FIN_R}"/>
    <path d="{FLAME}" opacity="0.85"/>
  </g>
</svg>
'''


def main() -> int:
    svg = build_svg()
    (OUT / 'favicon.svg').write_text(svg, encoding='utf-8', newline='\n')
    print(f'  favicon.svg          {len(svg)} bytes')

    # Rasterised from the same SVG by headless Chrome so they cannot drift.
    chrome = Path(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    # iOS composites a transparent icon onto black and applies its own mask,
    # so the touch icon is square and fully opaque; the browser favicon keeps
    # its rounded corners and transparent surround.
    variants = (
        ('favicon-32.png', 32, build_svg(RADIUS)),
        ('apple-touch-icon.png', 180, build_svg(0)),
    )
    for name, size, art in variants:
        html = OUT / '_icon.html'
        html.write_text(
            '<body style="margin:0">'
            + art.replace('<svg ', f'<svg width="{size}" height="{size}" '),
            encoding='utf-8')
        subprocess.run(
            [str(chrome), '--headless=new', '--disable-gpu', '--hide-scrollbars',
             f'--user-data-dir={Path.home()}/AppData/Local/Temp/favicon-profile',
             f'--window-size={size},{size}', '--default-background-color=00000000',
             f'--screenshot={OUT / name}', str(html)],
            capture_output=True, timeout=120)
        html.unlink(missing_ok=True)
        print(f'  {name:20} {(OUT / name).stat().st_size} bytes  {size}x{size}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
