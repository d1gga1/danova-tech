# -*- coding: utf-8 -*-
"""06/11/2026: titoli allineati al Keyword Planner del 06/11 (gestionale b&b, negozio abbigliamento,
gestionale dipendenti, programma preventivi; chatbot vs agenti AI). Cambia <title>, og:title/twitter:title e il "name" del WebPage. Idempotente.
Uso: python3 seo-tools/titoli-2026-11-06.py"""
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = {
 'software-preventivi-configuratore': "Software e programma per preventivi su misura | Danova Tech",
 'gestionale-hotel': "Gestionale hotel e B&B su misura: camere e prenotazioni | Danova Tech",
 'gestionale-negozio': "Gestionale negozio: cassa, magazzino, taglie e colori | Danova Tech",
 'app-ore-di-lavoro-e-timbrature': "App timbratura e gestionale dipendenti su misura | Danova Tech",
 'chatbot-aziendale': "Chatbot aziendale su misura sui vostri documenti | Danova Tech",
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
