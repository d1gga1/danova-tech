# -*- coding: utf-8 -*-
"""Genera tutte le pagine USA con il motore di pagine-build.py:
     pagine-dati-usa.py     (hub, servizi nazionali, 30 citta', software NY/LA/Chicago)
     pagine-dati-usa-2.py   (settori e guide)
     pagine-dati-usa-es.py  (spagnolo per il mercato ispanico)
   Lingua en-US / es-US: <html lang>, og:locale, inLanguage, hreflang.
   Le guide ricevono uno schema Article al posto di Service.
   Le coppie spagnolo/inglese ricevono hreflang reciproci.
   Uso:  python3 seo-tools/pagine-build-usa.py
   Poi:  python3 seo-tools/patch-footer-usa.py
         python3 seo-tools/genera-sitemap.py && python3 seo-tools/genera-feed-e-llms.py"""
import os, re, json, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://danova-tech.com'
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
pb = load('pb', 'pagine-build.py')
pb.LOC.update({'en': 'en-US', 'es': 'es-US'})
pb.OGL.update({'en': 'en_US', 'es': 'es_US'})
FILES = ['pagine-dati-usa.py', 'pagine-dati-usa-2.py', 'pagine-dati-usa-es.py']
mods = [load('usa%d' % i, f) for i, f in enumerate(FILES)]
es = mods[2]

def path_of(url): return os.path.join(pb.ROOT, url.strip('/'), 'index.html')

def articolo(h, d):
    """Sostituisce il nodo Service con un Article nelle guide."""
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    g = json.loads(m.group(1)); u = SITE + d['url']
    nodes = []
    for n in g['@graph']:
        if n.get('@type') == 'Service': continue
        if n.get('@type') == 'WebPage': n['about'] = {'@id': u + '#article'}
        nodes.append(n)
    nodes.insert(1, {"@type": "Article", "@id": u + "#article", "headline": d['title'],
                     "description": d['desc'], "inLanguage": "en-US",
                     "datePublished": pb.pd.OGGI, "dateModified": pb.pd.OGGI,
                     "author": {"@id": SITE + "/#organization"}, "publisher": {"@id": SITE + "/#organization"},
                     "mainEntityOfPage": {"@id": u + "#webpage"}, "image": {"@id": SITE + "/#logo"}})
    g['@graph'] = nodes
    return h[:m.start()] + '<script type="application/ld+json">\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n</script>' + h[m.end():]

for mod in mods:
    pb.pd = mod
    for d in mod.PAGINE:
        p = pb.build(d); f = os.path.join(pb.ROOT, p)
        h = open(f, encoding='utf-8').read()
        loc = pb.LOC[d['lang']]
        h = re.sub(r'<html lang="[a-zA-Z-]+"', '<html lang="%s"' % loc, h, count=1)
        h = h.replace('<link rel="alternate" hreflang="%s" href=' % d['lang'], '<link rel="alternate" hreflang="%s" href=' % loc, 1)
        h = re.sub(r'(<a href="[^"]*" hreflang=")%s(" aria-current="page">)' % d['lang'], r'\g<1>%s\2' % loc, h)
        if d.get('guida'): h = articolo(h, d)
        open(f, 'w', encoding='utf-8').write(h)
        print('%-5s  %-52s  %6d byte' % (loc, d['url'], len(h)))

# hreflang reciproci spagnolo <-> inglese (x-default = inglese)
for url_es, url_en in es.COPPIE.items():
    fe, fn = path_of(url_es), path_of(url_en)
    blocco = ('<link rel="alternate" hreflang="en-US" href="%s%s">\n'
              '<link rel="alternate" hreflang="es-US" href="%s%s">\n'
              '<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, url_en, SITE, url_es, SITE, url_en))
    for f in (fe, fn):
        h = open(f, encoding='utf-8').read()
        h = re.sub(r'<link rel="alternate" hreflang="[a-zA-Z-]+" href="[^"]*">\n(?:<link rel="alternate" hreflang="[a-zA-Z-]+" href="[^"]*">\n?)*',
                   lambda _: blocco + '\n', h, count=1)
        sel = ('<a href="%s" hreflang="en-US"%s>EN</a>\n        <a href="%s" hreflang="es-US"%s>ES</a>'
               % (url_en, ' aria-current="page"' if f == fn else '', url_es, ' aria-current="page"' if f == fe else ''))
        h = re.sub(r'(<span class="lang-links">)(.*?)(</span>)', lambda m: m.group(1) + '\n        ' + sel + '\n        ' + m.group(3), h, count=1, flags=re.S)
        h = re.sub(r'(<div class="mob-lang-links">)(.*?)(</div>)', lambda m: m.group(1) + '\n    ' + sel.replace('\n        ', '\n    ') + '\n    ' + m.group(3), h, count=1, flags=re.S)
        open(f, 'w', encoding='utf-8').write(h)
print('hreflang reciproci:', len(es.COPPIE), 'coppie')
