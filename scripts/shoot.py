"""Full-page screenshots over CDP against one headless Chrome instance."""
import json, base64, time, sys, urllib.request
from pathlib import Path
import websocket

CDP = 'http://localhost:9333'
OUT = Path('.shots'); OUT.mkdir(exist_ok=True)

targets = json.loads(urllib.request.urlopen(f'{CDP}/json/list').read())
page = next(t for t in targets if t['type'] == 'page')
ws = websocket.create_connection(page['webSocketDebuggerUrl'], timeout=40,
                                suppress_origin=True)

_id = 0
def send(method, **params):
    global _id
    _id += 1
    ws.send(json.dumps({'id': _id, 'method': method, 'params': params}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get('id') == _id:
            if 'error' in msg:
                raise RuntimeError(f"{method}: {msg['error']}")
            return msg.get('result', {})

send('Page.enable'); send('Runtime.enable')

def shoot(name, url, width, dark=False, height=900, scale=1):
    send('Emulation.setDeviceMetricsOverride',
         width=width, height=height, deviceScaleFactor=scale, mobile=width < 500)
    send('Emulation.setEmulatedMedia',
         features=[{'name': 'prefers-color-scheme',
                    'value': 'dark' if dark else 'light'}])
    send('Page.navigate', url=url)
    # A stored theme would override the emulated media query, so clear it and
    # reload: these shots must show what a first-time visitor sees.
    time.sleep(0.25)
    send('Runtime.evaluate', expression="localStorage.removeItem('theme')")
    send('Page.reload')
    # wait for the document to finish and fonts to settle
    for _ in range(60):
        time.sleep(0.12)
        r = send('Runtime.evaluate',
                 expression='document.readyState', returnByValue=True)
        if r.get('result', {}).get('value') == 'complete':
            break
    send('Runtime.evaluate', expression='document.fonts.ready', awaitPromise=True)
    # captureBeyondViewport renders the whole page but does NOT trigger
    # loading="lazy" images below the fold, so flip them to eager and wait for
    # every image to decode. Without this, below-fold logos shoot as blank.
    send('Runtime.evaluate', expression='''(async () => {
      document.querySelectorAll('img[loading="lazy"]')
        .forEach(i => { i.loading = 'eager'; });
      await Promise.all([...document.images].map(i => i.decode().catch(() => {})));
      return document.images.length;
    })()''', awaitPromise=True, returnByValue=True)
    time.sleep(0.4)
    res = send('Page.captureScreenshot', format='png',
               captureBeyondViewport=True, optimizeForSpeed=False)
    data = base64.b64decode(res['data'])
    (OUT / f'{name}.png').write_bytes(data)
    theme = send('Runtime.evaluate',
                 expression="document.documentElement.dataset.theme",
                 returnByValue=True)['result'].get('value')
    print(f'  {name:26} {len(data)//1024:4}kB  data-theme={theme}')

B = 'http://localhost:4321'
SHOTS = [
    ('home-1440-light',     f'{B}/',                1440, False),
    ('home-1440-dark',      f'{B}/',                1440, True),
    ('projects-1440-light', f'{B}/projects/',       1440, False),
    ('projects-1440-dark',  f'{B}/projects/',       1440, True),
    ('blog-1440-light',     f'{B}/blog/',           1440, False),
    ('post-1440-light',     f'{B}/blog/rag-lessons/', 1440, False),
    ('resume-1440-light',   f'{B}/resume/',         1440, False),
    ('err404-1440-light',   f'{B}/404.html',        1440, False),
    ('home-390-light',      f'{B}/',                390,  False),
    ('home-390-dark',       f'{B}/',                390,  True),
    ('projects-390-light',  f'{B}/projects/',       390,  False),
    ('resume-390-light',    f'{B}/resume/',         390,  False),
]
for name, url, w, dark in SHOTS:
    shoot(name, url, w, dark)
ws.close()
print(f'\n{len(SHOTS)} screenshots written to .shots/')
