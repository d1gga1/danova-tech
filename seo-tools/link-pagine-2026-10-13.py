# -*- coding: utf-8 -*-
"""Collega le pagine fiere del 13/10/2026 (galleria render, espositori, hub regionali) e aggiorna
   alcuni titoli in base alle ricerche del Keyword Planner. Idempotente.
   Uso: python3 seo-tools/link-pagine-2026-10-13.py   (dopo i build e dopo link-pagine-2026-10.py)"""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = 'https://danova-tech.com'
GAL = ("/progetti-stand-fieristici/", "Progetti di stand (render)")
ESP = ("/espositori-desk-totem-per-fiere/", "Espositori, desk e totem per fiere")
VEN = ("/allestimenti-fieristici-veneto/", "Allestimenti fieristici in Veneto")
LOM = ("/allestimenti-fieristici-lombardia/", "Allestimenti fieristici in Lombardia")
EMI = ("/allestimenti-fieristici-emilia-romagna/", "Allestimenti fieristici in Emilia-Romagna")
REGIONE = {"verona": VEN, "padova": VEN, "vicenza": VEN, "venezia": VEN, "treviso": VEN, "longarone": VEN,
           "milano": LOM, "bergamo": LOM, "brescia": LOM, "bologna": EMI, "rimini": EMI, "parma": EMI,
           "stand-vinitaly": VEN, "stand-marmomac": VEN, "stand-fieracavalli": VEN, "stand-vicenzaoro": VEN,
           "stand-salone-del-mobile": LOM, "stand-eicma": LOM, "stand-host": LOM, "stand-micam": LOM, "stand-mido": LOM,
           "stand-cosmoprof": EMI, "stand-cersaie": EMI, "stand-eima": EMI, "stand-sigep": EMI, "stand-ecomondo": EMI,
           "stand-macfrut": EMI, "stand-cibus": EMI}
ESP_SU = ["servizi/allestimenti-fieristici", "stand-preallestiti", "stand-fieristici-piccoli", "grafica-per-stand-fieristici",
          "ledwall-e-illuminazione-stand", "noleggio-stand-fieristici", "allestimenti-eventi-showroom-negozi", "stand-modulari",
          "quanto-costa-uno-stand-fieristico", "progetti-stand-fieristici", "idee-stand-fieristici", "guide/come-preparare-una-fiera"]

def pagine_fiere():
    out = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in ('seo-tools', 'assets', '.git', 'en', 'de', 'fr', 'es', 'zh', 'tr', 'ar')]
        if 'index.html' in fn:
            rel = os.path.relpath(dp, ROOT).replace('\\', '/')
            h = open(os.path.join(dp, 'index.html'), encoding='utf-8').read()
            if '/assets/img/stand/' in h or 'fiere.css' in h: out.append(rel)
    return sorted(out)

def aggiungi(rel, links):
    p = os.path.join(ROOT, rel, 'index.html'); h = open(p, encoding='utf-8').read()
    m = re.search(r'<div class="pg-altri"[^>]*>', h)
    if not m: return False
    add = ''.join(f'<a href="{u}">{t}</a>' for u, t in links if f'href="{u}"' not in h[m.start():m.start() + 6000] and rel != u.strip('/'))
    if not add: return False
    h = h[:m.end()] + add + h[m.end():]; open(p, 'w', encoding='utf-8').write(h); return True

n = 0
for rel in pagine_fiere():
    links = [GAL]
    if rel in ESP_SU: links.append(ESP)
    k = rel.replace('allestimenti-fieristici-', '')
    if k in REGIONE: links.append(REGIONE[k])
    if rel in ("servizi/allestimenti-fieristici", "calendario-fiere"): links += [VEN, LOM, EMI]
    n += aggiungi(rel, links)
print('box Approfondisci aggiornati:', n)

# footer colonna "Fiere": galleria ed espositori dopo il calendario
LI = ('\n        <li><a href="/progetti-stand-fieristici/">Progetti di stand</a></li>'
      '\n        <li><a href="/espositori-desk-totem-per-fiere/">Espositori, desk e totem</a></li>')
f = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('seo-tools', 'assets', '.git', 'en', 'de', 'fr', 'es', 'zh', 'tr', 'ar')]
    if 'index.html' not in fn: continue
    p = os.path.join(dp, 'index.html'); s = open(p, encoding='utf-8').read()
    m = re.search(r'<div><h5>Fiere</h5><ul>(.*?)</ul>', s, re.S)
    if not m or '/progetti-stand-fieristici/' in m.group(1): continue
    cal = '<li><a href="/calendario-fiere/">Calendario fiere 2026–2027</a></li>'
    i = s.find(cal, m.start(), m.end())
    k = (i + len(cal)) if i > 0 else m.start(1)
    s = s[:k] + LI + s[k:]; open(p, 'w', encoding='utf-8').write(s); f += 1
print('footer aggiornati:', f)

# home: link nella sezione fiere
p = os.path.join(ROOT, 'index.html'); s = open(p, encoding='utf-8').read()
if '/progetti-stand-fieristici/' not in s:
    s = s.replace('<div class="fr-links fr-links2"><a href="/calendario-fiere/">Calendario fiere 2026–2027</a>',
                  '<div class="fr-links fr-links2"><a href="/calendario-fiere/">Calendario fiere 2026–2027</a><a href="/progetti-stand-fieristici/">Progetti di stand</a><a href="/espositori-desk-totem-per-fiere/">Espositori e totem</a>', 1)
    s = s.replace('<a href="/allestimenti-fieristici-estero/">Estero</a></div>',
                  '<a href="/allestimenti-fieristici-veneto/">Veneto</a><a href="/allestimenti-fieristici-lombardia/">Lombardia</a><a href="/allestimenti-fieristici-emilia-romagna/">Emilia-Romagna</a><a href="/allestimenti-fieristici-estero/">Estero</a></div>', 1)
    open(p, 'w', encoding='utf-8').write(s); print('home ok')

# llms.txt
p = os.path.join(ROOT, 'llms.txt'); s = open(p, encoding='utf-8').read()
if '/progetti-stand-fieristici/' not in s:
    add = (f"- Progetti di stand fieristici (60 render per tipo, settore e fiera): {S}/progetti-stand-fieristici/\n"
           f"- Espositori per fiere: desk, banchi, totem, roll-up, vetrine: {S}/espositori-desk-totem-per-fiere/\n"
           f"- Allestimenti fieristici in Veneto: {S}/allestimenti-fieristici-veneto/\n"
           f"- Allestimenti fieristici in Lombardia: {S}/allestimenti-fieristici-lombardia/\n"
           f"- Allestimenti fieristici in Emilia-Romagna: {S}/allestimenti-fieristici-emilia-romagna/\n")
    s = s.replace(f"- Parma: {S}/allestimenti-fieristici-parma/\n", f"- Parma: {S}/allestimenti-fieristici-parma/\n" + add, 1)
    open(p, 'w', encoding='utf-8').write(s); print('llms.txt ok')

# ---- titoli (Keyword Planner 9/10/2026): "allestimento stand <citta>", "allestitori <citta>",
# "stand fieristici innovativi", "affitto stand fieristici"
NUOVE = ["Firenze", "Torino", "Roma", "Napoli", "Bari", "Genova", "Bergamo", "Brescia", "Venezia", "Treviso", "Udine",
         "Bolzano", "Riva del Garda", "Carrara", "Longarone"]
def slug(c): return c.lower().replace(' ', '-')
T = {}
for c in NUOVE:
    t = f"Allestimenti fieristici a {c}: allestimento stand | Danova Tech"
    if len(t) > 62: t = f"Allestimenti fieristici a {c}: allestimento stand"
    T[f"allestimenti-fieristici-{slug(c)}"] = (f"Allestimenti fieristici e stand a {c} | Danova Tech", t)
T["idee-stand-fieristici"] = ("Idee per stand fieristici che attirano visitatori | Danova Tech", "Stand fieristici innovativi: idee che attirano visitatori")
T["noleggio-stand-fieristici"] = ("Noleggio stand fieristici e arredi per fiere | Danova Tech", "Noleggio stand fieristici: affitto stand e arredi | Danova Tech")
t = 0
for rel, (old, new) in T.items():
    p = os.path.join(ROOT, rel, 'index.html')
    if not os.path.exists(p): continue
    s = open(p, encoding='utf-8').read()
    oe = old.replace('&', '&amp;')
    if f'<title>{oe}</title>' not in s: continue
    s = s.replace(f'<title>{oe}</title>', f'<title>{new}</title>', 1)
    s = s.replace(json.dumps(old, ensure_ascii=False)[1:-1].join(['"name": "', '"']), '"name": "' + json.dumps(new, ensure_ascii=False)[1:-1] + '"')
    open(p, 'w', encoding='utf-8').write(s); t += 1
print('titoli aggiornati:', t)
