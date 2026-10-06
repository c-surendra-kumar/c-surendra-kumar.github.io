"""Functional checks: mobile nav disclosure, theme toggle, console, network."""
import json, base64, time, urllib.request, sys
from pathlib import Path
import websocket

CDP='http://localhost:9333'
page=next(t for t in json.loads(urllib.request.urlopen(f'{CDP}/json/list').read())
          if t['type']=='page')
ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=40,suppress_origin=True)
_id=0
console, failed = [], []
def send(method,**params):
    global _id
    _id+=1
    ws.send(json.dumps({'id':_id,'method':method,'params':params}))
    while True:
        m=json.loads(ws.recv())
        if m.get('method')=='Runtime.consoleAPICalled':
            console.append((m['params']['type'],
                            ' '.join(str(a.get('value','')) for a in m['params']['args'])))
        elif m.get('method')=='Runtime.exceptionThrown':
            console.append(('exception', str(m['params']['exceptionDetails'].get('text'))))
        elif m.get('method')=='Network.loadingFailed':
            failed.append(m['params'])
        elif m.get('method')=='Network.responseReceived':
            r=m['params']['response']
            if r['status']>=400: failed.append({'url':r['url'],'status':r['status']})
        if m.get('id')==_id:
            if 'error' in m: raise RuntimeError(f"{method}: {m['error']}")
            return m.get('result',{})

def ev(expr, await_p=False):
    r=send('Runtime.evaluate',expression=expr,returnByValue=True,awaitPromise=await_p)
    return r.get('result',{}).get('value')

def shot(name):
    d=base64.b64decode(send('Page.captureScreenshot',format='png',
                            captureBeyondViewport=True)['data'])
    Path(f'.shots/{name}.png').write_bytes(d)

send('Page.enable'); send('Runtime.enable'); send('Network.enable')
send('Emulation.setDeviceMetricsOverride',width=390,height=800,
     deviceScaleFactor=2,mobile=True)
send('Emulation.setEmulatedMedia',
     features=[{'name':'prefers-color-scheme','value':'light'}])
send('Page.navigate',url='http://localhost:4321/')
time.sleep(2.0)

print('=== mobile nav disclosure ===')
print('  panel hidden initially      :', ev("document.getElementById('mobile-nav').classList.contains('hidden')"))
print('  aria-expanded initially     :', ev("document.getElementById('nav-toggle').getAttribute('aria-expanded')"))
ev("document.getElementById('nav-toggle').click()")
time.sleep(0.4)
open_hidden = ev("document.getElementById('mobile-nav').classList.contains('hidden')")
print('  panel hidden after click    :', open_hidden)
print('  aria-expanded after click   :', ev("document.getElementById('nav-toggle').getAttribute('aria-expanded')"))
print('  links reachable in panel    :', ev("document.querySelectorAll('#mobile-nav a').length"))
shot('mobile-nav-open')
ev("document.getElementById('nav-toggle').click()")
time.sleep(0.3)
print('  closes again                :', ev("document.getElementById('mobile-nav').classList.contains('hidden')"))

print('\n=== theme toggle ===')
print('  initial data-theme          :', ev("document.documentElement.dataset.theme"))
ev("document.getElementById('theme-toggle').click()")
time.sleep(0.3)
print('  after click                 :', ev("document.documentElement.dataset.theme"))
print('  localStorage persisted      :', ev("localStorage.getItem('theme')"))
print('  toggle aria-label updated   :', ev("document.getElementById('theme-toggle').getAttribute('aria-label')"))
ev("document.getElementById('theme-toggle').click()")
print('  back to                     :', ev("document.documentElement.dataset.theme"))

print('\n=== console ===')
errs=[c for c in console if c[0] in ('error','exception','warning')]
print(f'  messages captured: {len(console)}, errors/warnings: {len(errs)}')
for t,m in errs[:10]: print(f'   [{t}] {m[:140]}')

print('\n=== network failures (>=400 or blocked) ===')
if not failed: print('  none')
for f in failed[:15]:
    print('  ', f.get('status','FAILED'), f.get('url','')[:100], f.get('errorText',''))

print('\n=== external hosts requested ===')
hosts=ev("""[...new Set(performance.getEntriesByType('resource')
   .map(r=>new URL(r.name).host))].filter(h=>!h.startsWith('localhost'))""")
print('  ', hosts if hosts else 'none (all assets same-origin)')
ws.close()
