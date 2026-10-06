"""#8 - click every nav link and confirm it lands on the page it names."""
import json, time, urllib.request
import websocket

CDP='http://localhost:9333'
page=next(t for t in json.loads(urllib.request.urlopen(f'{CDP}/json/list').read())
          if t['type']=='page')
ws=websocket.create_connection(page['webSocketDebuggerUrl'],timeout=40,suppress_origin=True)
_id=0
def send(m,**p):
    global _id
    _id+=1
    ws.send(json.dumps({'id':_id,'method':m,'params':p}))
    while True:
        msg=json.loads(ws.recv())
        if msg.get('id')==_id:
            if 'error' in msg: raise RuntimeError(f"{m}: {msg['error']}")
            return msg.get('result',{})
def ev(e,aw=False):
    return send('Runtime.evaluate',expression=e,returnByValue=True,
                awaitPromise=aw).get('result',{}).get('value')

send('Page.enable'); send('Runtime.enable')
send('Emulation.setDeviceMetricsOverride',width=1440,height=900,
     deviceScaleFactor=1,mobile=False)

BASE='http://localhost:4321'
print(f"{'from':14} {'link text':12} {'href':16} {'lands on':22} ok")
print('-'*76)
ok_all=True

for start in ['/', '/projects/', '/blog/', '/resume/']:
    send('Page.navigate',url=BASE+start); time.sleep(1.2)
    n = ev("document.querySelectorAll('header nav[aria-label=\"Main\"] ul a').length")
    for i in range(n or 0):
        send('Page.navigate',url=BASE+start); time.sleep(0.9)
        sel = f"document.querySelectorAll('header nav[aria-label=\\\"Main\\\"] ul a')[{i}]"
        label = ev(f"{sel}.textContent.trim()")
        href  = ev(f"{sel}.getAttribute('href')")
        ev(f"{sel}.click()"); time.sleep(1.1)
        landed = ev("location.pathname")
        title  = ev("document.title")
        expected = href
        good = landed == expected and 'not exist' not in (title or '')
        ok_all &= good
        print(f"{start:14} {label:12} {href:16} {landed:22} {'y' if good else 'N'}")

# sidebar in-page anchors on home
send('Page.navigate',url=BASE+'/'); time.sleep(1.2)
print()
spy = ev("[...document.querySelectorAll('.spy-link')].map(a=>a.getAttribute('href'))")
missing = ev("""[...document.querySelectorAll('.spy-link')]
   .map(a=>a.getAttribute('href').slice(1))
   .filter(id=>!document.getElementById(id))""")
print('sidebar anchors    :', spy)
print('anchors with no target:', missing if missing else 'none')
ok_all &= not missing

print('\nALL NAV LINKS OK' if ok_all else '\nSOME NAV LINKS FAILED')
ws.close()
