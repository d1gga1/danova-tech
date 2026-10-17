#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rigenera llms.txt: testo scritto a mano (seo-tools/llms-intro.md) + elenco
delle pagine indicizzabili raggruppato per ARGOMENTO (non per data).
Le pagine con noindex sono escluse. Rilanciare dopo ogni build:
    python3 seo-tools/genera-llms-txt.py
"""
import os,re,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE="https://danova-tech.com"
SKIP_DIRS={".git",".github","seo-tools","assets","social","_archivio"}
LEGALE=re.compile(r'(^|/)(privacy|cookie-policy|termini|terms|agb|datenschutz|cookie-richtlinie|confidentialite|cookies|conditions|privacidad|condiciones)$')

def info(d):
    h=open(("" if d=="." else d+"/")+"index.html",encoding="utf-8").read()
    if re.search(r'<meta name="robots"[^>]*noindex',h): return None
    t=re.search(r'<title>(.*?)</title>',h,re.S)
    t=html.unescape(re.sub(r'\s+',' ',t.group(1))).strip() if t else d
    t=re.sub(r'\s*[|—–-]\s*Danova Tech\s*$','',t)
    return t

pagine={}
for dp,dn,fn in os.walk("."):
    dn[:]=[x for x in dn if x not in SKIP_DIRS]
    if "index.html" not in fn: continue
    d=os.path.relpath(dp,".").replace("\\","/")
    if d=="." or LEGALE.search(d): continue
    t=info(d)
    if t: pagine[d]=t

ESTERE=("en","de","fr","es","zh","zh-hant","ar","tr")
CITTA=r'(treviso|padova|verona|vicenza|venezia|udine|pordenone|milano|pavia|veneto|conegliano|oderzo)'
REGOLE=[
 ("Servizi principali", r'^(servizi(/|$)|chi-siamo$|contatti$|prezzi$)'),
 ("Guide e approfondimenti", r'^(guide(/|$)|glossario$)'),
 ("Lavori realizzati (casi cliente)", r'^lavori(/|$)'),
 ("Prezzi e costi", r'^quanto-costa'),
 ("Calendari delle fiere", r'^calendario-fiere'),
 ("Stand e allestimenti fieristici", r'(stand|allestiment|fier|espositori|totem|ledwall)'),
 ("Pagine locali (Veneto, Friuli, Lombardia)", CITTA),
 ("Intelligenza artificiale e automazioni", r'(intelligenza-artificiale|ai-act|chatbot|automazion|n8n|whatsapp)'),
 ("App su misura", r'^(app-|sviluppo-web-app|sviluppo-app)'),
 ("Gestionali e software su misura", r'(gestionale|gestionali|software|erp|crm|dashboard|wms|integrazione|digitalizzazione|portale|documentale|iperammortamento|bandi)'),
 ("SEO, Google Ads e marketing", r'(seo|posizionamento|indicizzare|link-building|lead-generation|marketing|google-ads|recensioni)'),
 ("Siti web ed e-commerce", r'(siti|sito|realizzazione|restyling|ecommerce|negozio-online|landing)'),
]
gruppi={k:[] for k,_ in REGOLE}; gruppi["Altre pagine"]=[]
estere={}
for d,t in sorted(pagine.items()):
    top=d.split("/")[0]
    if top in ESTERE:
        estere.setdefault(top,[]).append((d,t)); continue
    for k,rx in REGOLE:
        if re.search(rx,d): gruppi[k].append((d,t)); break
    else: gruppi["Altre pagine"].append((d,t))

NOMI={"en":"English","de":"Deutsch","fr":"Français","es":"Español","zh":"中文 (简体)","zh-hant":"中文 (繁體)","ar":"العربية","tr":"Türkçe"}
out=[open("seo-tools/llms-intro.md",encoding="utf-8").read().rstrip()]
out.append("\n## Indice delle pagine per argomento\n\nTutte le pagine indicizzabili del sito in italiano, raggruppate per argomento.")
for k,_ in REGOLE+[("Altre pagine","")]:
    if not gruppi[k]: continue
    out.append(f"\n### {k}\n")
    out += [f"- {t}: {SITE}/{d}/" for d,t in gruppi[k]]
out.append("\n## Pagine in altre lingue\n\nDanova Tech lavora anche per clienti esteri in remoto e allestisce stand per espositori stranieri nelle fiere italiane.")
for lang in ESTERE:
    if lang not in estere: continue
    out.append(f"\n### {NOMI[lang]}\n")
    if lang=="zh-hant":   # stesse pagine del cinese semplificato: basta il rimando
        out.append(f"- Versione in cinese tradizionale delle {len(estere[lang])} pagine sulle fiere italiane: {SITE}/zh-hant/italy-exhibition-stand/")
        continue
    out += [f"- {t}: {SITE}/{d}/" for d,t in estere[lang]]
out.append("""
## Contatti e informazioni legali

- Contatti: https://danova-tech.com/contatti/ — info@danova-tech.com — +39 388 470 6887 (anche WhatsApp)
- Privacy Policy: https://danova-tech.com/privacy/
- Cookie Policy: https://danova-tech.com/cookie-policy/
- Termini e condizioni d'uso: https://danova-tech.com/termini/
""")
open("llms.txt","w",encoding="utf-8").write("\n".join(out))
n=sum(len(v) for v in gruppi.values())+sum(len(v) for v in estere.values())
print(f"llms.txt: {n} pagine, {os.path.getsize('llms.txt')//1024} KB")
for k,v in gruppi.items(): print(f"  {k}: {len(v)}")
for k,v in estere.items(): print(f"  [{k}]: {len(v)}")
