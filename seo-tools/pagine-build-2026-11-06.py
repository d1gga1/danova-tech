# -*- coding: utf-8 -*-
"""06/11/2026 - Pagine nuove: /agenti-ai-per-aziende/ (IT) e pagine base /zh/, /ar/, /tr/.
   Dati: seo-tools/pagine-dati-2026-11-06.py. Usa il motore di pagine-build.py + le sezioni
   'breve' e la pulizia (robots, CSS, speakable) di pagine-build-2026-10-23.py.
   Per ZH/AR/TR il guscio e' la pagina inglese (menu e footer in inglese), con i percorsi
   resi assoluti; il testo e' nella lingua della pagina, <main dir="rtl"> per l'arabo.
   Aggiunge anche zh/ar/tr agli hreflang delle 5 home (reciprocita').
   Idempotente. Uso:  python3 seo-tools/pagine-build-2026-11-06.py
   Poi: python3 seo-tools/genera-sitemap.py && python3 seo-tools/genera-feed-e-llms.py && python3 seo-tools/genera-llms-txt.py"""
import os, re, html, importlib.util, tempfile
from urllib.parse import urljoin
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
M = load('b2310', 'pagine-build-2026-10-23.py')     # motore + sezione 'breve' + lingue()
D = load('d2611', 'pagine-dati-2026-11-06.py')
pb = M.pb; pb.pd = D; SITE = pb.SITE

HL = {'it': 'it', 'en': 'en', 'de': 'de', 'fr': 'fr', 'es': 'es', 'zh': 'zh-Hans', 'ar': 'ar', 'tr': 'tr'}
ORD = ['it', 'en', 'de', 'fr', 'es', 'zh', 'ar', 'tr']
NOMI = {'it': 'IT', 'en': 'EN', 'de': 'DE', 'fr': 'FR', 'es': 'ES', 'zh': '中文', 'ar': 'عربي', 'tr': 'TR'}
NUOVE = ('zh', 'ar', 'tr')

# guscio inglese con percorsi assoluti, valido a qualsiasi profondita'
donor_rel = pb.DONOR['en']
base = SITE + '/' + donor_rel.rsplit('/', 1)[0] + '/'
src = open(os.path.join(ROOT, donor_rel), encoding='utf-8').read()
def absol(m):
    u = urljoin(base, m.group(2))
    return m.group(1) + (u[len(SITE):] if u.startswith(SITE) else u) + m.group(3)
src = re.sub(r'((?:href|src)=")(\.\./[^"]*|\./[^"]*)(")', absol, src)
src = re.sub(r'(url\()(\.\./[^)]*)(\))', absol, src)
tmp = os.path.join(tempfile.gettempdir(), 'donor-en-assoluto.html')
open(tmp, 'w', encoding='utf-8').write(src)
for l, loc, ogl in (('zh', 'zh-CN', 'zh_CN'), ('ar', 'ar', 'ar_AR'), ('tr', 'tr-TR', 'tr_TR')):
    pb.DONOR[l] = tmp; pb.LOC[l] = loc; pb.OGL[l] = ogl; pb.HOME[l] = '/%s/' % l

def hreflang_home(s, alt):
    links = ''.join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (HL[l], SITE, alt[l]) for l in ORD if l in alt)
    links += '<link rel="alternate" hreflang="x-default" href="%s/">' % SITE
    return re.sub(r'<link rel="alternate" hreflang="[a-zA-Z-]+".*?hreflang="x-default" href="[^"]*">',
                  lambda _: links, s, count=1, flags=re.S)

def selettore(s, cur, alt):
    def sw(c):
        return ''.join(c + '<a href="%s" hreflang="%s"%s>%s</a>' % (alt[l], HL[l], ' aria-current="page"' if l == cur else '', NOMI[l])
                       for l in ORD if l in alt)
    s = re.sub(r'(<span class="lang-links">)(.*?)(</span>)', lambda m: m.group(1) + sw('\n        ') + '\n      ' + m.group(3), s, count=1, flags=re.S)
    s = re.sub(r'(<div class="mob-lang-links">)(.*?)(</div>)', lambda m: m.group(1) + sw('\n    ') + '\n  ' + m.group(3), s, count=1, flags=re.S)
    return s

for d in D.PAGINE:
    M._cur_lang[0] = d['lang']; M._cur_url[0] = d['url']
    p = M.build(d); f = os.path.join(ROOT, p)
    s = open(f, encoding='utf-8').read()
    if d['lang'] in NUOVE:
        alt = d['alt']
        s = M.lingue(dict(d, alt={'en': '/en/'}), s)       # robots index, CSS 'breve'
        s = hreflang_home(s, alt)
        s = selettore(s, d['lang'], alt)
        s = re.sub(r'<html lang="[^"]*"', '<html lang="%s"' % HL[d['lang']], s, count=1)
        if d['lang'] == 'ar':
            s = s.replace('<main id="main">', '<main id="main" dir="rtl">', 1)
    else:
        s = M.lingue(d, M.hreflang_mancanti(d, s))
    open(f, 'w', encoding='utf-8').write(s)
    print('%-3s  %-28s  %6d byte' % (d['lang'], d['url'], len(s)))

# reciprocita': le 5 home dichiarano anche zh / ar / tr
for l in ('it', 'en', 'de', 'fr', 'es'):
    f = os.path.join(ROOT, D.ALT_HOME[l].strip('/'), 'index.html')
    s0 = s = open(f, encoding='utf-8').read()
    s = hreflang_home(s, D.ALT_HOME)
    if s != s0: open(f, 'w', encoding='utf-8').write(s); print('hreflang zh/ar/tr aggiunti a', D.ALT_HOME[l])
