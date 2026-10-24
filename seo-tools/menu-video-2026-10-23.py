# -*- coding: utf-8 -*-
"""23/10/2026 - Voce "Video" nel menu principale (desktop e mobile) di tutte le pagine IT/EN/DE/FR/ES,
   come seconda voce. Idempotente. Rilanciare dopo pagine-build-2026-10-23.py.
   Uso: python3 seo-tools/menu-video-2026-10-23.py"""
import os, re, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
V = {'it': ('Video', '/video-pubblicitari/'), 'en': ('Videos', '/en/promotional-video-production/'),
     'de': ('Videos', '/de/werbevideos-erstellen-lassen/'), 'fr': ('Vidéos', '/fr/creation-video-publicitaire/'),
     'es': ('Vídeos', '/es/videos-publicitarios/')}
NAV = re.compile(r'(<nav (?:class="links"|id="mob")[^>]*>\s*(?:<div class="mob-links">\s*)?<a\b[^>]*>.*?</a>)(\s*)', re.S)
n = 0
for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
    rel = os.path.relpath(f, R).replace('\\', '/')
    if rel.startswith(('_archivio/', 'seo-tools/', 'social/', 'assets/')): continue
    top = rel.split('/')[0]
    lang = top if top in ('en', 'de', 'fr', 'es') else ('it' if top not in ('zh', 'zh-hant', 'ar', 'tr', 'ro', 'sq', 'hr') else None)
    if not lang: continue
    t, href = V[lang]
    s = open(f, encoding='utf-8').read(); s0 = s
    if 'name="dt-sezione" content="real-estate"' in s: continue   # 24/10/2026: le pagine Real Estate hanno un menu proprio
    def add(m):
        cur = ' aria-current="page"' if rel == href.strip('/') + '/index.html' else ''
        return m.group(1) + m.group(2) + '<a href="%s" data-nav-video%s>%s</a>' % (href, cur, t) + m.group(2)
    if 'data-nav-video' not in s:
        s = NAV.sub(add, s)
    if s != s0:
        open(f, 'w', encoding='utf-8').write(s); n += 1
print('pagine con la voce Video nel menu:', n)
