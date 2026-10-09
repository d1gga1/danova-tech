#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rigenera sitemap.xml leggendo direttamente i file del sito.
Uso:  python3 seo-tools/genera-sitemap.py
Da lanciare dalla cartella danovatech/. Non serve configurare nulla:
gli hreflang li legge dai <link rel="alternate"> di ogni pagina,
le immagini dai tag <img> e dagli sfondi CSS della pagina.
"""
import os,re,html,datetime,sys

SITE="https://danova-tech.com"
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def url_of(rel):
    d=os.path.dirname(rel)
    return SITE+"/"+(d+"/" if d else "")

def priorita(rel):
    p=rel.replace("\\","/")
    if p=="index.html": return "1.0","weekly"
    if re.match(r'^(en|de|fr|es)/index\.html$',p): return "0.9","weekly"
    if re.search(r'(privacy|cookie|termini|terms|datenschutz|cookie-richtlinie|agb|confidentialite|cookies|conditions|privacidad|condiciones)/index\.html$',p):
        return "0.2","yearly"
    if re.search(r'(contatti|contact|kontakt|contacto)/index\.html$',p): return "0.6","monthly"
    if p.startswith("guide/"): return "0.7","monthly"
    if p.startswith("lavori/"): return "0.7","monthly"
    if re.match(r'^(prezzi|en/pricing|de/preise|fr/tarifs|es/precios)/index\.html$',p): return "0.9","monthly"
    if p in ("servizi/index.html",): return "0.9","monthly"
    return "0.8","monthly"

pages=[]
for dp,dn,fn in os.walk("."):
    dn[:]=[d for d in dn if d not in (".git","seo-tools","assets","_archivio")]
    for f in fn:
        if f!="index.html": continue
        pages.append(os.path.relpath(os.path.join(dp,f),".").replace("\\","/"))
pages.sort()

out=['<?xml version="1.0" encoding="UTF-8"?>',
     '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
     '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
     '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
nimg=0
for rel in pages:
    h=open(rel,encoding="utf-8").read()
    if re.search(r'<meta name="robots"[^>]*noindex',h): continue
    loc=url_of(rel)
    can=re.search(r'<link rel="canonical" href="([^"]+)"',h)
    if can: loc=can.group(1)
    pr,cf=priorita(rel)
    lastmod=datetime.date.fromtimestamp(os.path.getmtime(rel)).isoformat()
    out.append("  <url>")
    out.append(f"    <loc>{html.escape(loc)}</loc>")
    for m in re.finditer(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"',h):
        out.append(f'    <xhtml:link rel="alternate" hreflang="{m.group(1)}" href="{html.escape(m.group(2))}"/>')
    # immagini della pagina: <img src> + sfondi css url(...)
    imgs=[]
    for m in re.finditer(r'<img\b[^>]*\bsrc="([^"]+)"',h):
        imgs.append(m.group(1))
    for m in re.finditer(r'url\(&quot;([^&]+\.(?:webp|jpg|png))&quot;\)',h):
        imgs.append(m.group(1))
    seen=set()
    for src in imgs:
        if src.startswith("data:"): continue
        u=re.sub(r'^(\.\./)+','/',src)
        if not u.startswith("/"): u="/"+u
        if "logo.png" in u: continue          # il logo non e' contenuto
        full=SITE+u
        if full in seen: continue
        seen.add(full)
        out.append("    <image:image>")
        out.append(f"      <image:loc>{html.escape(full)}</image:loc>")
        out.append("    </image:image>")
        nimg+=1
    out.append(f"    <lastmod>{lastmod}</lastmod>")
    out.append(f"    <changefreq>{cf}</changefreq>")
    out.append(f"    <priority>{pr}</priority>")
    out.append("  </url>")
out.append("</urlset>")
open("sitemap.xml","w",encoding="utf-8").write("\n".join(out)+"\n")
print(f"sitemap.xml: {len(pages)} pagine, {nimg} immagini dichiarate")
