# -*- coding: utf-8 -*-
"""14/11/2026 - Selettore lingua (desktop e menu mobile) sulle pagine nuove del 14/11 che hanno versioni in
altre lingue: i donatori de/fr/es/en non hanno lo <span class="lang-links">, quindi lingue() non trovava
dove scriverlo. Lo inserisce come nelle pagine /de/leistungen/. Idempotente; rilanciare dopo il build del 14/11."""
import os, re, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
s_ = importlib.util.spec_from_file_location('d1411', os.path.join(HERE, 'pagine-dati-2026-11-14.py'))
D = importlib.util.module_from_spec(s_); s_.loader.exec_module(D)
ORD = ('it', 'en', 'de', 'fr', 'es'); n = 0
for d in D.PAGINE:
    alt = d.get('alt')
    if not alt: continue
    f = os.path.join(ROOT, d['url'].strip('/'), 'index.html'); s = open(f, encoding='utf-8').read()
    if 'class="lang-links"' in s: continue
    def links(ind):
        return ''.join('%s<a href="%s" hreflang="%s"%s>%s</a>\n' % (ind, alt[l], l, ' aria-current="page"' if l == d['lang'] else '', l.upper())
                       for l in ORD if l in alt)
    s = s.replace('<div class="nav-r">\n', '<div class="nav-r">\n      <span class="lang-links">\n' + links('        ') + '      </span>\n', 1)
    m = re.search(r'(<nav id="mob"[^>]*>.*?)(</nav>)', s, re.S)
    if m and 'mob-lang-links' not in m.group(1):
        s = s[:m.end(1)] + '\n  <div class="mob-lang-links">\n' + links('    ') + '  </div>\n' + s[m.end(1):]
    open(f, 'w', encoding='utf-8').write(s); n += 1
print('selettore lingua aggiunto a', n, 'pagine')
