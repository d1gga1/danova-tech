#!/usr/bin/env python3
"""17/10/2026: aggiunge la pagina Facebook (sameAs + footer), dopo TikTok. Idempotente.
Da rilanciare dopo ogni build, insieme alle patch Instagram e TikTok."""
import os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
TT="https://www.tiktok.com/@danova.tech"; FB="https://www.facebook.com/profile.php?id=61594907955699"
LI_TT=f'<li><a href="{TT}" target="_blank" rel="noopener me">TikTok @danova.tech</a></li>'
LI_FB=f'<li><a href="{FB}" target="_blank" rel="noopener me">Facebook Danova Tech</a></li>'
n1=n2=0
for dp,dn,fn in os.walk("."):
    dn[:]=[d for d in dn if d not in (".git","seo-tools","social",".github","assets")]
    for f in fn:
        if not f.endswith(".html"): continue
        p=os.path.join(dp,f); h=open(p,encoding="utf-8").read(); o=h
        if FB not in h:
            h,k=re.subn(r'(\n([ \t]*)"'+re.escape(TT)+r'",?)',lambda m:m.group(1).rstrip(',')+',\n'+m.group(2)+f'"{FB}"'+(',' if m.group(1).endswith(',') else ''),h,count=1); n1+=k
            if LI_TT in h: h=h.replace(LI_TT,LI_TT+"\n        "+LI_FB,1); n2+=1
        if h!=o: open(p,"w",encoding="utf-8").write(h)
print("sameAs",n1,"footer",n2)
