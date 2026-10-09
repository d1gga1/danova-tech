# -*- coding: utf-8 -*-
"""Genera /prezzi/ e le sue traduzioni partendo dal guscio (header, footer,
   script) di una pagina esistente, cosi' restano identiche al resto del sito.
   Uso:  python3 seo-tools/prezzi-build.py"""
import os, re, json, html, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('dati', os.path.join(HERE, 'prezzi-dati.py'))
dati = importlib.util.module_from_spec(spec); spec.loader.exec_module(dati)
D, SITE, URLP, OUT, DONOR, LOC, OGLOC, LBL, P, NUM = (
    dati.D, dati.SITE, dati.URLP, dati.OUT, dati.DONOR, dati.LOC, dati.OGLOC, dati.LBL, dati.P, dati.NUM)

HOME = {'it':'/','en':'/en/','de':'/de/','fr':'/fr/','es':'/es/'}
FROM_KEYS = {'app_una','gest_da'}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<path d="M5 12h14M13 6l6 6-6 6"></path></svg>')

def esc(s): return html.escape(s, quote=False)

# ------------------------------------------------------------------ CONTENUTO
def build_main(lang, d):
    u, home = URLP[lang], HOME[lang]
    o = []
    a = o.append
    # briciole
    crumbs = ['<a href="%s">Home</a>' % home]
    for name, href in d['crumbs']:
        crumbs.append('<em>/</em>' + (('<a href="%s">%s</a>' % (href, name)) if href else name))
    a('<div class="wrap pg-crumbs">\n  %s\n</div>\n' % ''.join(crumbs))
    # hero
    a('<section class="pg-hero">\n  <div class="wrap">\n'
      '    <div class="eyebrow mono" data-scramble>%s</div>\n'
      '    <h1 data-rv="up">%s</h1>\n'
      '    <p class="lead" data-rv="up">%s</p>\n'
      '    <div class="hero-cta" data-rv="up">\n'
      '      <a href="%s#contatti" class="btn btn-p" data-mag><span class="sheen"></span>'
      '<span class="lbl">%s</span>\n        %s</a>\n'
      '      <a href="#%s" class="btn btn-g" data-mag><span class="lbl">%s</span></a>\n'
      '    </div>\n  </div>\n</section>\n'
      % (esc(d['eyebrow']), d['h1'], esc(d['lead']), home, esc(d['cta1']), ARROW,
         d['cats'][0]['id'], esc(d['cta2'])))
    # tabella riassuntiva (20/09/2026): la forma che Google e i motori AI estraggono meglio
    if d.get('tab'):
        t = d['tab']
        a('<section id="sintesi">\n  <div class="wrap">\n    <div class="sec-head">\n'
          '      <div class="eyebrow mono" data-scramble>%s</div>\n'
          '      <h2 class="title" data-rv="up">%s</h2>\n    </div>\n'
          '    <div class="price-table-wrap" data-rv="up">\n    <table class="price-table">\n'
          '      <caption>%s</caption>\n      <thead><tr>%s</tr></thead>\n      <tbody>\n'
          % (esc(t['eyebrow']), t['h2'], esc(t['caption']),
             ''.join('<th scope="col">%s</th>' % esc(c) for c in t['cols'])))
        for name, desc, key, unit, dur in d['offers']:
            if unit == 'MON': f = t['f_mese_min'] if dur else t['f_mese']
            elif key in FROM_KEYS: f = t['f_da']
            else: f = t['f_una']
            c = [html.escape(x) for x in t['cols']]
            a('        <tr><th scope="row">%s</th><td data-label="%s">%s</td>'
              '<td class="pt-amt" data-label="%s">%s</td><td data-label="%s">%s</td></tr>\n'
              % (esc(name), c[1], esc(f), c[2], esc(t['prezzi'][key]), c[3], esc(desc)))
        a('      </tbody>\n    </table>\n    </div>\n'
          '    <p class="price-upd" data-rv="up">%s</p>\n  </div>\n</section>\n' % t['upd'])
    # categorie
    for cat in d['cats']:
        a('<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n'
          '      <div class="eyebrow mono" data-scramble>%s</div>\n'
          '      <h2 class="title" data-rv="up">%s</h2>\n'
          '      <p class="lead" data-rv="up">%s</p>\n    </div>\n'
          % (cat['id'], esc(cat['eyebrow']), cat['h2'], esc(cat['intro'])))
        a('    <div class="price-grid">\n')
        for c in cat['cards']:
            cls = 'price-card feat' if c.get('feat') else 'price-card'
            a('      <article class="%s" data-tilt data-rv="blur">\n' % cls)
            if c.get('badge'):
                a('        <span class="price-badge">%s</span>\n' % esc(c['badge']))
            a('        <span class="price-kind mono">%s</span>\n' % esc(c['kind']))
            a('        <h3>%s</h3>\n' % esc(c['name']))
            a('        <p class="price-amt"><b>%s</b><span>%s</span></p>\n'
              % (esc(c['amt']), esc(c['unit'])))
            if c.get('extra'):
                a('        <p class="price-extra">%s</p>\n' % esc(c['extra']))
            a('        <p class="price-note">%s</p>\n' % esc(c['note']))
            if c.get('tot'):
                a('        <p class="price-tot">%s</p>\n' % esc(c['tot']))
            a('        <ul class="price-list">%s</ul>\n'
              % ''.join('<li>%s</li>' % esc(x) for x in c['list']))
            a('        <a href="%s#contatti" class="btn btn-g" data-mag><span class="lbl">%s</span></a>\n'
              % (home, esc(c['cta'])))
            a('      </article>\n')
        a('    </div>\n  </div>\n</section>\n')
    # confronto
    for blocco in ('compare', 'incluso'):
        b = d[blocco]
        a('<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n'
          '      <div class="eyebrow mono" data-scramble>%s</div>\n'
          '      <h2 class="title" data-rv="up">%s</h2>\n    </div>\n'
          '    <div class="pg-testo" data-rv="up">\n%s    </div>\n  </div>\n</section>\n'
          % (blocco, esc(b['eyebrow']), b['h2'],
             ''.join('      <p>%s</p>\n' % x for x in b['paras'])))
    # faq
    a('<section id="faq">\n  <div class="wrap">\n    <div class="sec-head">\n'
      '      <h2 class="title" data-rv="up">%s</h2>\n    </div>\n    <div class="faq">\n' % esc(d.get('faq_h2', 'FAQ')))
    for q, r in d['faq']:
        a('      <details data-rv="up"><summary>%s<span class="pm"></span></summary>\n'
          '        <div class="ans"><p>%s</p></div></details>\n' % (esc(q), esc(r)))
    a('    </div>\n  </div>\n</section>\n')
    # cta
    cb = d['ctabox']
    a('<section class="pg-cta">\n  <div class="wrap">\n    <div class="box" data-rv="up">\n'
      '      <h2 class="title">%s</h2>\n      <p>%s</p>\n'
      '      <a href="%s#contatti" class="btn btn-p" data-mag><span class="sheen"></span>'
      '<span class="lbl">%s</span>\n        %s</a>\n    </div>\n  </div>\n</section>\n'
      % (esc(cb['h2']), esc(cb['p']), home, esc(cb['btn']), ARROW))
    # collegati
    a('<section id="altri">\n  <div class="wrap">\n    <div class="pg-altri" data-rv="up">\n')
    for label, href in d['altri']:
        a('      <a href="%s">%s</a>\n' % (href, label))
    a('    </div>\n  </div>\n</section>\n')
    return ''.join(o)

# ------------------------------------------------------------------ JSON-LD
def build_jsonld(lang, d, org):
    u = SITE + URLP[lang]
    offers = []
    for name, desc, key, unit, dur in d['offers']:
        val = float(NUM[key])
        if unit == 'MON':
            ps = {"@type": "UnitPriceSpecification", "price": val, "priceCurrency": "EUR",
                  "valueAddedTaxIncluded": True, "unitCode": "MON",
                  "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"}}
            if dur:
                ps["billingDuration"] = dur
                ps["billingIncrement"] = 1
        elif key in FROM_KEYS:
            ps = {"@type": "PriceSpecification", "minPrice": val, "priceCurrency": "EUR",
                  "valueAddedTaxIncluded": True}
        else:
            ps = {"@type": "PriceSpecification", "price": val, "priceCurrency": "EUR",
                  "valueAddedTaxIncluded": True}
        offers.append({
            "@type": "Offer", "name": name, "description": desc,
            "price": val, "priceCurrency": "EUR",
            "availability": "https://schema.org/InStock",
            "url": u, "priceSpecification": ps,
            "seller": {"@id": SITE + "/#organization"},
            "itemOffered": {"@type": "Service", "name": name, "description": desc,
                            "provider": {"@id": SITE + "/#organization"}}})
    service = {
        "@type": "Service", "@id": u + "#service",
        "name": d['svc']['name'], "serviceType": d['svc']['type'],
        "description": d['svc']['desc'],
        "provider": {"@id": SITE + "/#organization"},
        "areaServed": [{"@type": "Country", "name": "Italia"}, {"@type": "Place", "name": "Europa"}],
        "offers": offers,
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": d['svc']['name'],
            "itemListElement": [{"@type": "OfferCatalog", "name": re.sub(r'<[^>]+>', '', c['h2']),
                                 "url": u + '#' + c['id']} for c in d['cats']]}}
    webpage = {
        "@type": "WebPage", "@id": u + "#webpage", "url": u,
        "name": d['title'], "description": d['desc'], "inLanguage": LOC[lang],
        "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": u + "#service"},
        "publisher": {"@id": SITE + "/#organization"},
        "primaryImageOfPage": {"@id": SITE + "/#logo"},
        "breadcrumb": {"@id": u + "#breadcrumb"},
        "datePublished": getattr(dati, 'PUBBLICATO', None) or "2026-09-19",
        "dateModified": getattr(dati, 'AGGIORNATO', None) or "2026-09-19"}
    if d.get('ogimg'):
        webpage["image"] = {"@type": "ImageObject", "url": SITE + d['ogimg'], "width": 1200, "height": 630}
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + HOME[lang]}]
    for i, (name, href) in enumerate(d['crumbs'], start=2):
        items.append({"@type": "ListItem", "position": i, "name": name,
                      "item": SITE + (href if href else URLP[lang])})
    crumb = {"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement": items}
    faq = {"@type": "FAQPage", "@id": u + "#faq", "inLanguage": LOC[lang],
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in d['faq']]}
    graph = {"@context": "https://schema.org", "@graph": [org, service, webpage, crumb, faq]}
    return json.dumps(graph, ensure_ascii=False, indent=2)

# ------------------------------------------------------------------ MONTAGGIO
def lang_links(lang, mobile=False):
    rows = []
    for L in ('it', 'en', 'de', 'fr', 'es'):
        cur = ' aria-current="page"' if L == lang else ''
        rows.append('<a href="%s" hreflang="%s"%s>%s</a>' % (URLP[L], L, cur, L.upper()))
    sep = '\n        ' if not mobile else '\n    '
    return sep.join(rows)

def build(lang):
    d = D[lang]
    src = open(os.path.join(ROOT, DONOR[lang]), encoding='utf-8').read()
    head, body = src.split('</head><body>', 1)
    u = SITE + URLP[lang]

    # --- JSON-LD: riuso il nodo Organization del donatore
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
    org = json.loads(m.group(1))['@graph'][0]
    head = head[:m.start()] + '<script type="application/ld+json">\n' + \
        build_jsonld(lang, d, org) + '\n</script>' + head[m.end():]

    # --- testa
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(d['title']), head, count=1, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">',
                  '<meta name="description" content="%s">' % html.escape(d['desc']), head, count=1)
    head = re.sub(r'<link rel="canonical" href="[^"]*">',
                  '<link rel="canonical" href="%s">' % u, head, count=1)
    alt = '\n'.join('<link rel="alternate" hreflang="%s" href="%s%s">' % (L, SITE, URLP[L])
                    for L in ('it', 'en', 'de', 'fr', 'es'))
    alt += '\n<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, URLP['it'])
    head = re.sub(r'<link rel="alternate" hreflang="it".*?hreflang="x-default" href="[^"]*">',
                  alt, head, count=1, flags=re.S)
    head = re.sub(r'<meta property="og:url" content="[^"]*">',
                  '<meta property="og:url" content="%s">' % u, head, count=1)
    head = re.sub(r'<meta property="og:locale" content="[^"]*">',
                  '<meta property="og:locale" content="%s">' % OGLOC[lang], head, count=1)
    head = re.sub(r'<meta property="og:title" content="[^"]*">',
                  '<meta property="og:title" content="%s">' % html.escape(d['ogtitle']), head, count=1)
    head = re.sub(r'<meta property="og:description" content="[^"]*">',
                  '<meta property="og:description" content="%s">' % html.escape(d['ogdesc']), head, count=1)
    head = re.sub(r'<meta name="twitter:title" content="[^"]*">',
                  '<meta name="twitter:title" content="%s">' % html.escape(d['ogtitle']), head, count=1)
    head = re.sub(r'<meta name="twitter:description" content="[^"]*">',
                  '<meta name="twitter:description" content="%s">' % html.escape(d['ogdesc']), head, count=1)

    if d.get('ogimg'):
        head = re.sub(r'<meta property="og:image" content="[^"]*">',
                      '<meta property="og:image" content="%s%s">' % (SITE, d['ogimg']), head, count=1)
        head = re.sub(r'<meta name="twitter:image" content="[^"]*">',
                      '<meta name="twitter:image" content="%s%s">' % (SITE, d['ogimg']), head, count=1)
        head = head.replace('<meta property="og:image:height" content="630">',
                            '<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="%s">'
                            % html.escape(d['ogtitle']), 1)
    body = body.replace('class="nav-prezzi">', 'class="nav-prezzi" aria-current="page">')
    # --- corpo: selettore lingua e contenuto
    body = re.sub(r'(<span class="lang-links">)(.*?)(</span>)',
                  lambda m: m.group(1) + '\n        ' + lang_links(lang) + '\n      ' + m.group(3),
                  body, count=1, flags=re.S)
    body = re.sub(r'(<div class="mob-lang-links">)(.*?)(</div>)',
                  lambda m: m.group(1) + '\n    ' + lang_links(lang, True) + '\n  ' + m.group(3),
                  body, count=1, flags=re.S)
    body = re.sub(r'(<main id="main">)(.*?)(</main>)',
                  lambda m: m.group(1) + '\n\n' + build_main(lang, d) + '\n' + m.group(3),
                  body, count=1, flags=re.S)

    out_dir = os.path.join(ROOT, OUT[lang])
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, 'index.html')
    open(path, 'w', encoding='utf-8').write(head + '</head><body>' + body)
    return path, len(head + body)

if __name__ == '__main__':
    for lang in ('it', 'en', 'de', 'fr', 'es'):
        p, n = build(lang)
        print('%-3s  %-28s  %6d byte' % (lang, os.path.relpath(p, ROOT), n))
