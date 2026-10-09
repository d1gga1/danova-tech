#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera due file che servono ai motori di ricerca e ai motori di risposta AI:
  feed.xml       feed RSS delle guide e dei lavori (sottoscrivibile, e i lettori
                 di feed sono uno dei modi in cui i contenuti vengono ripresi)
  llms-full.txt  il testo integrale delle pagine italiane principali, in chiaro,
                 per ChatGPT / Perplexity / Claude / Gemini
Uso:  python3 seo-tools/genera-feed-e-llms.py   (dalla cartella danovatech/)
"""
import os,re,html,datetime,email.utils,time

SITE="https://danova-tech.com"
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def leggi(rel):
    return open(rel,encoding="utf-8").read()

def meta(h,name):
    m=re.search(r'<meta name="%s" content="(.*?)">'%name,h,re.S)
    return html.unescape(m.group(1)) if m else ""

def titolo(h):
    m=re.search(r'<title>(.*?)</title>',h,re.S)
    return html.unescape(m.group(1)).split(" | ")[0].strip() if m else ""

def data_pagina(h,rel):
    m=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"',h)
    if m: return m.group(1)
    return datetime.date.fromtimestamp(os.path.getmtime(rel)).isoformat()

def testo(h):
    """Testo leggibile della pagina: solo il contenuto dentro <main>."""
    m=re.search(r'<main\b[^>]*>(.*)</main>',h,flags=re.S|re.I)
    if m: h=m.group(1)
    h=re.sub(r'<head\b.*?</head>',' ',h,flags=re.S|re.I)
    h=re.sub(r'<script\b.*?</script>',' ',h,flags=re.S|re.I)
    h=re.sub(r'<style\b.*?</style>',' ',h,flags=re.S|re.I)
    h=re.sub(r'<header\b.*?</header>',' ',h,flags=re.S|re.I)
    h=re.sub(r'<footer\b.*?</footer>',' ',h,flags=re.S|re.I)
    h=re.sub(r'<(h[1-6])\b[^>]*>',r'\n\n## ',h,flags=re.I)
    h=re.sub(r'</(h[1-6])>','\n',h,flags=re.I)
    h=re.sub(r'</(p|li|div|section|tr)>','\n',h,flags=re.I)
    h=re.sub(r'<li\b[^>]*>','- ',h,flags=re.I)
    h=re.sub(r'<[^>]+>',' ',h)
    h=html.unescape(h)
    h=re.sub(r'[ \t\xa0]+',' ',h)
    h=re.sub(r'\n\s*\n\s*\n+','\n\n',h)
    return "\n".join(l.strip() for l in h.splitlines()).strip()

# ------------------------------------------------------------------ FEED RSS
voci=[]
for base in ("guide","lavori"):
    for d in sorted(os.listdir(base)):
        rel=os.path.join(base,d,"index.html")
        if not os.path.isfile(rel): continue
        h=leggi(rel)
        voci.append({
            "url":f"{SITE}/{base}/{d}/",
            "titolo":titolo(h),
            "desc":meta(h,"description"),
            "data":data_pagina(h,rel),
            "sez":"Guide" if base=="guide" else "Lavori",
        })
voci.sort(key=lambda v:v["data"],reverse=True)

def rfc822(d):
    t=time.mktime(datetime.datetime.strptime(d,"%Y-%m-%d").timetuple())
    return email.utils.formatdate(t,localtime=False)

rss=['<?xml version="1.0" encoding="UTF-8"?>',
     '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
     '  <channel>',
     '    <title>Danova Tech — guide e lavori</title>',
     f'    <link>{SITE}/</link>',
     '    <description>Guide pratiche su siti web, SEO e software gestionali, e i lavori consegnati da Danova Tech, software house italiana con sede a Mansuè (Treviso).</description>',
     '    <language>it-IT</language>',
     f'    <lastBuildDate>{rfc822(voci[0]["data"]) if voci else rfc822(datetime.date.today().isoformat())}</lastBuildDate>',
     f'    <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml"/>',
     f'    <image><url>{SITE}/assets/img/logo.png</url><title>Danova Tech</title><link>{SITE}/</link></image>']
for v in voci:
    rss+= ['    <item>',
           f'      <title>{html.escape(v["titolo"])}</title>',
           f'      <link>{v["url"]}</link>',
           f'      <guid isPermaLink="true">{v["url"]}</guid>',
           f'      <category>{v["sez"]}</category>',
           f'      <pubDate>{rfc822(v["data"])}</pubDate>',
           f'      <description>{html.escape(v["desc"])}</description>',
           '    </item>']
rss+=['  </channel>','</rss>']
open("feed.xml","w",encoding="utf-8").write("\n".join(rss)+"\n")
print(f"feed.xml: {len(voci)} voci")

# ------------------------------------------------------------- llms-full.txt
PRIORITA=["index.html","chi-siamo/index.html","servizi/index.html","contatti/index.html"]
italiane=[]
for dp,dn,fn in os.walk("."):
    dn[:]=[d for d in dn if d not in (".git","seo-tools","assets","en","de","fr","es","_archivio")]
    for f in fn:
        if f!="index.html": continue
        rel=os.path.relpath(os.path.join(dp,f),".").replace("\\","/")
        italiane.append(rel)
ordine={p:i for i,p in enumerate(PRIORITA)}
italiane.sort(key=lambda r:(ordine.get(r,99),r))
ESCLUDI=re.compile(r'^(privacy|cookie-policy|termini)/')
parti=[f"""# Danova Tech — testo integrale del sito
# Generato il {datetime.date.today().isoformat()} da {SITE}
# Questo file raccoglie il contenuto delle pagine italiane in testo semplice,
# per i motori di ricerca e i motori di risposta basati su AI.
# Indice sintetico: {SITE}/llms.txt — Sitemap: {SITE}/sitemap.xml
"""]
n=0
for rel in italiane:
    if ESCLUDI.match(rel): continue
    h=leggi(rel)
    if re.search(r'<meta name="robots"[^>]*noindex',h): continue
    url=SITE+"/"+(os.path.dirname(rel)+"/" if os.path.dirname(rel) else "")
    parti.append(f"\n\n{'='*72}\n# {titolo(h)}\nURL: {url}\nDescrizione: {meta(h,'description')}\n{'='*72}\n\n{testo(h)}")
    n+=1
open("llms-full.txt","w",encoding="utf-8").write("\n".join(parti)+"\n")
kb=os.path.getsize("llms-full.txt")/1024
print(f"llms-full.txt: {n} pagine, {kb:.0f} KB")
