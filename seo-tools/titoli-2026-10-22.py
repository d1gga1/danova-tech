# -*- coding: utf-8 -*-
"""22/10/2026: titoli allineati alle ricerche del Keyword Planner (allestitori fiere, exhibit designer,
exhibition stand contractor). Cambia <title>, og:title/twitter:title e il "name" del WebPage. Idempotente.
Uso: python3 seo-tools/titoli-2026-10-22.py"""
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = {
 'servizi/allestimenti-fieristici': "Allestimenti fieristici e allestitori per fiere chiavi in mano",
 'progettazione-stand-fieristici': "Progettazione stand fieristici e render 3D: exhibit designer",
 'en/exhibition-stand-builder-italy': "Exhibition Stand Builder & Contractor in Italy and Europe",
}
for rel, new in T.items():
    p = os.path.join(ROOT, rel, 'index.html'); s = open(p, encoding='utf-8').read()
    old = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
    if old == new: print('gia ok', rel); continue
    e = html.escape(new, quote=True)
    s = re.sub(r'<title>.*?</title>', f'<title>{e}</title>', s, 1, flags=re.S)
    for k in ('og:title', 'twitter:title'):
        s = re.sub(rf'(<meta (?:property|name)="{k}" content=")[^"]*"', lambda m: m.group(1) + e + '"', s)
    s = s.replace(f'"name": {old!r}'.replace("'", '"'), f'"name": "{new}"')
    open(p, 'w', encoding='utf-8').write(s); print(rel, '->', new, len(new))
