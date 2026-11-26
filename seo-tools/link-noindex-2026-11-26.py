#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Toglie i link interni verso le pagine in noindex (citta' lontane, vedi noindex-pagine-lontane.py).
Perche': 144 pagine indicizzabili avevano 1.793 link verso 67 pagine noindex (footer "Markets",
sezione "Across the US" con 30 citta', griglie "altri"). Per Google e' l'impronta delle doorway
pages che il noindex doveva eliminare, e il PageRank finisce in pagine che non si posizionano.
Cosa fa (idempotente, da rilanciare dopo ogni build e dopo noindex-pagine-lontane.py):
 1. footer: toglie le <li> il cui link porta a una pagina noindex;
 2. sezione id="cities" delle pagine servizio EN: l'elenco di citta' diventa un link a /en/united-states/;
 3. altrove: il link a una pagina noindex diventa testo semplice (griglie di soli link: rimosso).
Uso:  python3 seo-tools/link-noindex-2026-11-26.py
"""
import os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
SKIP=('.git','.github','seo-tools','assets','_archivio','_to_delete','social')
files={}
for dp,dn,fn in os.walk('.'):
    dn[:]=[d for d in dn if d not in SKIP]
    if 'index.html' in fn:
        d=os.path.relpath(dp); files['/' if d=='.' else '/'+d+'/']=os.path.join(dp,'index.html')
H={u:open(p,encoding='utf-8').read() for u,p in files.items()}
red={u for u,h in H.items() if 'http-equiv="refresh"' in h[:2000]}
NI={u for u,h in H.items() if u not in red and re.search(r'<meta name="robots"[^>]*noindex',h)}
href_ni=r'(?:%s)'%'|'.join(re.escape(x) for x in sorted(NI,key=len,reverse=True))
A_NI=re.compile(r'<a href="(?:https://danova-tech\.com)?'+href_ni+r'"[^>]*>(.*?)</a>',re.S)
LI_NI=re.compile(r'[ \t]*<li><a href="(?:https://danova-tech\.com)?'+href_ni+r'"[^>]*>.*?</a></li>\n?',re.S)
CITY_INTRO={
 'Local market notes, city by city:':'The process is the same in every state: see <a href="/en/united-states/">how we work with US businesses</a>.',
 'For the metros we hear from most, there is a page on the local market, industries and search landscape:':'The approach is the same in every metro: see <a href="/en/united-states/">how we work with US businesses</a>.',
}
tot=0;pag=0
for u,h in H.items():
    if u in red or u in NI: continue
    if not A_NI.search(h): continue
    o=h
    h=LI_NI.sub('',h)
    # sezione citta' (pagine servizio EN): via il paragrafo-elenco, intro che rimanda all'hub USA
    def citta(m):
        s=m.group(0)
        ps=re.findall(r'<p>.*?</p>',s,re.S)
        lista=[p for p in ps if len(A_NI.findall(p))>=5]
        if not lista or u=='/en/united-states/': return s
        for p in lista: s=s.replace(p,'',1)
        for k,v in CITY_INTRO.items():
            if k in s: s=s.replace(k,v,1); break
        s=re.sub(r'\n\s*\n(\s*</div>)',r'\n\1',s)
        return s
    h=re.sub(r'<section id="cities">.*?</section>',citta,h,flags=re.S)
    # griglie di soli link ("pg-altri"): rimuovi il link
    def griglia(m): return A_NI.sub('',m.group(0))
    h=re.sub(r'<div class="pg-altri"[^>]*>.*?</div>',griglia,h,flags=re.S)
    # resto: link -> testo
    h=A_NI.sub(lambda m:m.group(1),h)
    if h!=o:
        n=len(A_NI.findall(o))-len(A_NI.findall(h)); tot+=n; pag+=1
        open(files[u],'w',encoding='utf-8').write(h)
print(f'pagine noindex: {len(NI)} | pagine modificate: {pag} | link tolti: {tot}')
