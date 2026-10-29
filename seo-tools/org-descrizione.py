#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aggiunge la descrizione aziendale al nodo #organization di ogni pagina che
ne e' priva, nella lingua della pagina (presa dalla homepage di quella lingua).
Serve ai motori di risposta AI: ogni pagina dice chi e' Danova Tech e cosa fa.
Idempotente. Da rilanciare dopo ogni script che genera o rigenera pagine.
Uso:  python3 seo-tools/org-descrizione.py   (dalla cartella danovatech/)
Pagine zh, zh-hant, ar, tr: saltate (manca una descrizione nella loro lingua)."""
import os,re,json,glob,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
R=re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)',re.S)
OID='https://danova-tech.com/#organization'
def orgdesc(p):
    for b in R.findall(open(p,encoding='utf-8').read()):
        for n in json.loads(b[1]).get('@graph',[]):
            if n.get('@id')==OID and n.get('description'): return n['description']
D={'it':orgdesc('index.html')}
for l in ('en','de','fr','es'): D[l]=orgdesc(f'{l}/index.html')
stats=collections.Counter()
for p in glob.glob('**/index.html',recursive=True):
    if p.startswith('seo-tools'): continue
    top=p.split('/')[0] if '/' in p else ''
    if top in ('zh','zh-hant','ar','tr','hi'): continue
    lang=top if top in D else 'it'
    h=open(p,encoding='utf-8').read()
    def fix(m):
        b=m.group(2)
        if OID not in b: return m.group(0)
        d=json.loads(b); mod=False
        for n in d.get('@graph',[]):
            if n.get('@id')==OID and 'name' in n and not n.get('description'):
                new={}
                for k,v in n.items():
                    new[k]=v
                    if k=='name': new['description']=D[lang]
                n.clear(); n.update(new); mod=True
        if not mod: return m.group(0)
        lead=b[:len(b)-len(b.lstrip())]; trail=b[len(b.rstrip()):]
        return m.group(1)+lead+json.dumps(d,ensure_ascii=False,indent=2)+trail+m.group(3)
    nh=R.sub(fix,h)
    if nh!=h: open(p,'w',encoding='utf-8').write(nh); stats[lang]+=1
print('descrizione aggiunta:',dict(stats) or 'nessuna pagina da aggiornare')
