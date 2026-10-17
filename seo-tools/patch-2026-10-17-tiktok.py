#!/usr/bin/env python3
"""17/10/2026: aggiunge il profilo TikTok (sameAs + footer), dopo Instagram. Idempotente."""
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
IG="https://www.instagram.com/danova_techh/"; TT="https://www.tiktok.com/@danova.tech"
LI_IG=f'<li><a href="{IG}" target="_blank" rel="noopener me">Instagram @danova_techh</a></li>'
LI_TT=f'<li><a href="{TT}" target="_blank" rel="noopener me">TikTok @danova.tech</a></li>'
n1=n2=0
for dp,dn,fn in os.walk("."):
    dn[:]=[d for d in dn if d not in (".git","seo-tools","social",".github","assets")]
    for f in fn:
        if not f.endswith(".html"): continue
        p=os.path.join(dp,f); h=open(p,encoding="utf-8").read(); o=h
        if TT not in h:
            i=h.find(f'"{IG}"')
            if i>=0 and i<h.find('<footer') if '<footer' in h else i>=0:
                ls=h.rfind("\n",0,i); ind=h[ls+1:i]
                h=h[:i]+f'"{IG}",\n{ind}"{TT}"'+h[i+len(IG)+2:]; n1+=1
            if LI_IG in h: h=h.replace(LI_IG,LI_IG+"\n        "+LI_TT,1); n2+=1
        if h!=o: open(p,"w",encoding="utf-8").write(h)
print("sameAs",n1,"footer",n2)
