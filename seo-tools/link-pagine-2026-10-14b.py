# -*- coding: utf-8 -*-
# 14/10/2026: link interni verso i nuovi calendari (Verona, Firenze, 8 settori). Idempotente.
import os,re,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"fiere-generatore"))
import dati_calendario as DC
R=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
SET={"food-e-ristorazione":("food e ristorazione",["food","vino"]),"meccanica-e-industria":("meccanica e industria",["industria","pack"]),
 "moda":("moda, calzature e accessori",["moda","gioielli"]),"arredo-e-design":("arredo e design",["arredo"]),
 "elettronica-e-tecnologia":("elettronica e tecnologia",["tech"]),"edilizia-ed-energia":("edilizia ed energia",["edilizia","ambiente"]),
 "agricoltura":("agricoltura e zootecnia",["agri"]),"turismo":("turismo e ospitalità",["turismo"])}
L=lambda s:(f"Fiere {SET[s][0]}: calendario",f"/calendario-fiere-{s}/")
VR=("Calendario fiere Verona","/calendario-fiere-verona/"); FI=("Calendario fiere Firenze","/calendario-fiere-firenze/")
T={}
def add(p,*links): T.setdefault(p,[]).extend(links)
add("calendario-fiere",VR,FI,*[L(s) for s in SET])
for c in ("milano","bologna","rimini","parma"): add(f"calendario-fiere-{c}",VR,FI)
add("calendario-fiere-verona",*[L(s) for s in ("food-e-ristorazione","edilizia-ed-energia","agricoltura")])
add("calendario-fiere-firenze",L("moda"),L("food-e-ristorazione"))
add("allestimenti-fieristici-verona",VR); add("allestimenti-fieristici-firenze",FI)
add("servizi/allestimenti-fieristici",VR,FI,*[L(s) for s in SET])
add("allestimenti-fieristici-veneto",VR)
for p,s in (("stand-fieristici-food-e-vino","food-e-ristorazione"),("stand-fieristici-arredo-e-design","arredo-e-design"),("stand-fieristici-meccanica-e-industria","meccanica-e-industria"),
            ("stand-fieristici-moda-e-calzature","moda"),("stand-fieristici-agricoltura","agricoltura"),("stand-fieristici-cosmetica-e-beauty","moda")):
    add(p,L(s))
# ogni pagina /stand-<fiera>/ -> calendario del suo settore (+ citta')
for f in DC.F:
    for k in os.listdir(R):
        if k.startswith("stand-") and f[0].startswith(k[6:]) and os.path.exists(os.path.join(R,k,"index.html")) and not k.startswith("stand-fieristici"):
            for s,(n,cats) in SET.items():
                if f[3] in cats: add(k,L(s))
            if f[2]=="verona": add(k,VR)
            if f[2]=="firenze": add(k,FI)
TOT=("Totem pubblicitari personalizzati","/totem-pubblicitari/"); EXP=("Espositori pubblicitari per negozi","/espositori-pubblicitari/")
for p in ("espositori-desk-totem-per-fiere","allestimenti-eventi-showroom-negozi","ledwall-e-illuminazione-stand","grafica-per-stand-fieristici","stand-fieristici-su-misura","servizi/allestimenti-fieristici","noleggio-stand-fieristici"):
    add(p,TOT,EXP)
for p in ("stand-fieristici-moda-e-calzature","stand-fieristici-cosmetica-e-beauty","stand-fieristici-food-e-vino","stand-fieristici-arredo-e-design"): add(p,EXP)
n=0
for p,links in T.items():
    fp=os.path.join(R,p,"index.html")
    if not os.path.exists(fp): print("manca",p); continue
    s=open(fp,encoding="utf-8").read()
    m=re.search(r'(<section id="altri">.*?<div class="pg-altri"[^>]*>)(.*?)(</div>)',s,re.S)
    if not m: print("no altri",p); continue
    cur=m.group(2); new=""
    seen=set()
    for t,u in links:
        if u in seen or f'href="{u}"' in cur or u==f"/{p}/": continue
        seen.add(u); new+=f'\n      <a href="{u}">{t}</a>'
    if new:
        s=s[:m.end(2)]+new+"\n    "+s[m.end(2):]; open(fp,"w",encoding="utf-8").write(s); n+=1
print("pagine con nuovi link:",n)
