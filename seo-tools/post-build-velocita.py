# -*- coding: utf-8 -*-
"""Velocita' (Core Web Vitals) - 15 ottobre 2026. Idempotente: rilanciare dopo ogni build.
1) Inserisce fonts.css direttamente nella pagina (una richiesta bloccante in meno al primo caricamento).
2) Contrasto del grigio secondario (--muted-2) portato sopra 4.5:1 (accessibilita' / Lighthouse).
Uso: python3 seo-tools/post-build-velocita.py"""
import os, re, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
css = open(os.path.join(R, 'assets/css/fonts.css'), encoding='utf-8').read()
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
css = re.sub(r'\s+', ' ', css); css = re.sub(r'\s*([{};:,])\s*', r'\1', css).replace(';}', '}').strip()
LINK = re.compile(r'<link rel="stylesheet" href="([^"]*?)assets/css/fonts\.css">')
n = c = 0
for f in glob.glob(os.path.join(R, '**', '*.html'), recursive=True):
    if '/seo-tools/' in f.replace('\\', '/'): continue
    s = open(f, encoding='utf-8').read(); s0 = s
    s = LINK.sub(lambda m: '<style id="fonts-inline">' + css.replace('url(../fonts/', 'url(' + m.group(1) + 'assets/fonts/') + '</style>', s)
    s = s.replace('--muted-2:#5f6880', '--muted-2:#747d96')
    if s != s0:
        open(f, 'w', encoding='utf-8').write(s); n += 1
p = os.path.join(R, 'assets/css/site.css'); s = open(p, encoding='utf-8').read()
if '--muted-2:#5f6880' in s: open(p, 'w', encoding='utf-8').write(s.replace('--muted-2:#5f6880', '--muted-2:#747d96')); c = 1
print(f'Pagine aggiornate: {n} | site.css aggiornato: {bool(c)}')
