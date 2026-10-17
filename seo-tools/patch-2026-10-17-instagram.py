#!/usr/bin/env python3
"""17/10/2026: aggiunge il profilo Instagram (sameAs + footer) e piccoli fix tecnici.
Idempotente: si puo' rilanciare senza duplicare nulla. Uso: python3 seo-tools/patch-2026-10-17-instagram.py"""
import os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
IG="https://www.instagram.com/danova_techh/"
LI=f'<li><a href="{IG}" target="_blank" rel="noopener me">Instagram @danova_techh</a></li>'
st={'sameas':0,'footer':0,'relfix':0,'nofooter':[]}
for dp,dn,fn in os.walk("."):
    dn[:]=[d for d in dn if d not in (".git","seo-tools","social",".github","assets")]
    for f in fn:
        if not f.endswith(".html"): continue
        p=os.path.join(dp,f); h=open(p,encoding="utf-8").read(); o=h
        if IG not in h.split('<footer')[0]:
            h,n=re.subn(r'("sameAs":\s*\[\s*\n?)(\s*)("https://www\.google\.com/search\?kgmid=[^"]+")',
                        lambda m:f'{m.group(1)}{m.group(2)}{m.group(3)},\n{m.group(2)}"{IG}"' if IG not in m.group(0) else m.group(0),h,count=1)
            st['sameas']+=n
        i=h.find('<footer')
        if i>=0 and IG not in h[i:]:
            m=re.compile(r'<li><a href="mailto:info@danova-tech\.com">[^<]*</a></li>').search(h,i)
            if m: h=h[:m.end()]+"\n        "+LI+h[m.end():]; st['footer']+=1
            else: st['nofooter'].append(p)
        # link relativi senza / iniziale nel footer (rompono se la pagina non e' in radice)
        h,n=re.subn(r'href="((?:realizzazione-siti-web|gestionali-su-misura)-[a-z-]+/)"',r'href="/\1"',h); st['relfix']+=n
        if h!=o: open(p,"w",encoding="utf-8").write(h)
print(st)
