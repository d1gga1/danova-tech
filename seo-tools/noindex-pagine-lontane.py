#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Noindex alle pagine "citta' lontana" (doorway pages).

Perche': Search Console (ago-ott 2026) mostra che queste pagine prendono
impressioni a posizione 60-95 con zero clic. Per Google sono a rischio
"doorway pages / scaled content abuse" e pesano sulla qualita' di tutto il
sito; per ChatGPT/Claude/Perplexity rendono confusa l'entita' (un'agenzia
di Treviso che dice di servire Atlanta, Wien e Sevilla).

Cosa fa (idempotente, si puo' rilanciare dopo ogni build):
 1. mette <meta name="robots" content="noindex, follow"> sulle pagine in LISTA;
 2. toglie i loro <link rel="alternate" hreflang> e li toglie dalle altre pagine;
 3. sitemap.xml, llms-full.txt e feed le escludono gia' da soli (saltano noindex).
Poi:  python3 seo-tools/genera-sitemap.py && python3 seo-tools/genera-feed-e-llms.py

Restano indicizzate: fiere (EN/ZH/DE/FR/ES), pagine nazionali (Deutschland,
Oesterreich, Schweiz, Espana, France, Belgique, USA, UK), zone vicine
(Suedtirol, Kaernten, Graz) e tutte le pagine italiane.
Per reindicizzare una pagina: toglila da LISTA e rimetti a mano il meta robots.
"""
import os,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE="https://danova-tech.com"

LISTA_RE=[
 r'^en/web-design-(?!agency-usa|agency-uk|for-law-firms)[a-z-]+$',   # citta' USA + London
 r'^en/software-development-(?!company-usa|company-uk|italy)[a-z-]+$',
 r'^es/diseno-web-(?!espana)[a-z-]+$',                              # Valencia, Sevilla, Madrid, Barcelona, citta' USA
 r'^es/agencia-seo-valencia$',
 r'^de/seo-agentur-(wien|berlin|muenchen)$',
 r'^de/webagentur-(wien|berlin|muenchen|hamburg|frankfurt|zuerich)$',
 r'^fr/agence-web-(paris|lyon|marseille|bruxelles|geneve)$',
 r'^fr/agence-seo-bordeaux$',
]
def in_lista(d): return any(re.match(p,d) for p in LISTA_RE)

pagine=[]
for dp,dn,fn in os.walk("."):
    dn[:]=[x for x in dn if x not in (".git",".github","seo-tools","assets","social")]
    if "index.html" in fn: pagine.append(os.path.relpath(dp,".").replace("\\","/"))
lontane=sorted(d for d in pagine if in_lista(d))
url_lontani={f"{SITE}/{d}/" for d in lontane}
if "--prova" in sys.argv:
    print(len(lontane)); print("\n".join(lontane)); sys.exit()

ROBOTS='<meta name="robots" content="noindex, follow">'
mod=0
for d in pagine:
    rel=("" if d=="." else d+"/")+"index.html"
    h=open(rel,encoding="utf-8").read(); o=h
    if d in lontane:
        h=re.sub(r'\n?<link rel="alternate" hreflang="[^"]+" href="[^"]+">','',h)
        if re.search(r'<meta name="robots"[^>]*>',h):
            h=re.sub(r'<meta name="robots"[^>]*>',ROBOTS,h,count=1)
        else:
            h=h.replace('<link rel="canonical"',ROBOTS+'\n<link rel="canonical"',1)
    else:
        h=re.sub(r'\n?<link rel="alternate" hreflang="[^"]+" href="([^"]+)">',
                 lambda m:'' if m.group(1) in url_lontani else m.group(0),h)
        # se e' rimasto un solo hreflang (cluster di 1) non ha senso: lo lascio, e' innocuo
    if h!=o:
        open(rel,"w",encoding="utf-8").write(h); mod+=1
print(f"pagine noindex: {len(lontane)} — file modificati: {mod}")
for d in lontane: print("  /"+d+"/")
