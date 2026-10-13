# -*- coding: utf-8 -*-
"""Generatore di pagine nuove: prende il guscio (testa, header, footer, script)
   da una pagina esistente della stessa lingua e profondita', e ci monta dentro
   il contenuto definito in pagine-dati.py.
   Uso:  python3 seo-tools/pagine-build.py"""
import os, re, json, html, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('pd', os.path.join(HERE,'pagine-dati.py'))
pd = importlib.util.module_from_spec(spec); spec.loader.exec_module(pd)
SITE = 'https://danova-tech.com'
DONOR = {'it':'quanto-costa-un-sito-web/index.html','de':'de/webagentur-muenchen/index.html',
         'fr':'fr/agence-web-lyon/index.html','es':'es/diseno-web-madrid/index.html',
         'en':'en/web-design-agency-uk/index.html'}
LOC  = {'it':'it-IT','en':'en-GB','de':'de-DE','fr':'fr-FR','es':'es-ES'}
OGL  = {'it':'it_IT','en':'en_GB','de':'de_DE','fr':'fr_FR','es':'es_ES'}
HOME = {'it':'/','en':'/en/','de':'/de/','fr':'/fr/','es':'/es/'}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<path d="M5 12h14M13 6l6 6-6 6"></path></svg>')
def e(s): return html.escape(s, quote=False)

def sezione(sec):
    o = ['<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n' % sec['id']]
    if sec.get('eyebrow'):
        o.append('      <div class="eyebrow mono" data-scramble>%s</div>\n' % e(sec['eyebrow']))
    o.append('      <h2 class="title" data-rv="up">%s</h2>\n' % sec['h2'])
    if sec.get('lead'):
        o.append('      <p class="lead" data-rv="up">%s</p>\n' % e(sec['lead']))
    o.append('    </div>\n')
    t = sec.get('tipo','testo')
    if t == 'testo':
        o.append('    <div class="pg-testo" data-rv="up">\n%s    </div>\n'
                 % ''.join('      <p>%s</p>\n' % p for p in sec['corpo']))
    elif t == 'cards':
        o.append('    <div class="pg-cards">\n')
        for i,(h3,p) in enumerate(sec['corpo'], start=1):
            o.append('      <article class="pg-card" data-tilt data-rv="blur">\n'
                     '        <span class="n">%02d</span>\n        <h3>%s</h3>\n        <p>%s</p>\n'
                     '      </article>\n' % (i, e(h3), e(p)))
        o.append('    </div>\n')
    elif t == 'passi':
        o.append('    <ol class="pg-passi" data-rv="up">\n%s    </ol>\n'
                 % ''.join('      <li><b>%s</b><span>%s</span></li>\n' % (e(a), e(b)) for a,b in sec['corpo']))
    o.append('  </div>\n</section>\n')
    return ''.join(o)

def main_html(d):
    lang = d['lang']; home = HOME[lang]; o = []
    crumbs = ['<a href="%s">Home</a>' % home]
    for nome, href in d['crumbs']:
        crumbs.append('<em>/</em>' + (('<a href="%s">%s</a>' % (href, nome)) if href else nome))
    o.append('<div class="wrap pg-crumbs">\n  %s\n</div>\n\n' % ''.join(crumbs))
    o.append('<section class="pg-hero">\n  <div class="wrap">\n'
             '    <div class="eyebrow mono" data-scramble>%s</div>\n'
             '    <h1 data-rv="up">%s</h1>\n    <p class="lead" data-rv="up">%s</p>\n'
             '    <div class="hero-cta" data-rv="up">\n'
             '      <a href="%s#contatti" class="btn btn-p" data-mag><span class="sheen"></span>'
             '<span class="lbl">%s</span>\n        %s</a>\n'
             '      <a href="#%s" class="btn btn-g" data-mag><span class="lbl">%s</span></a>\n'
             '    </div>\n  </div>\n</section>\n\n'
             % (e(d['eyebrow']), d['h1'], e(d['lead']), home, e(d['cta1']), ARROW,
                d['sezioni'][0]['id'], e(d['cta2'])))
    for sec in d['sezioni']: o.append(sezione(sec) + '\n')
    o.append('<section id="faq">\n  <div class="wrap">\n    <div class="sec-head">\n'
             '      <div class="eyebrow mono" data-scramble>FAQ</div>\n'
             '      <h2 class="title" data-rv="up">%s</h2>\n    </div>\n    <div class="faq">\n'
             % d['faqtitle'])
    for q,r in d['faq']:
        o.append('      <details data-rv="up"><summary>%s<span class="pm"></span></summary>\n'
                 '        <div class="ans"><p>%s</p></div></details>\n' % (e(q), e(r)))
    o.append('    </div>\n  </div>\n</section>\n\n')
    cb = d['ctabox']
    o.append('<section class="pg-cta">\n  <div class="wrap">\n    <div class="box" data-rv="up">\n'
             '      <h2 class="title">%s</h2>\n      <p>%s</p>\n'
             '      <a href="%s#contatti" class="btn btn-p" data-mag><span class="sheen"></span>'
             '<span class="lbl">%s</span>\n        %s</a>\n    </div>\n  </div>\n</section>\n\n'
             % (e(cb['h2']), e(cb['p']), home, e(cb['btn']), ARROW))
    o.append('<section id="altri">\n  <div class="wrap">\n    <div class="sec-head">'
             '<h2 class="title" data-rv="up">%s</h2></div>\n    <div class="pg-altri" data-rv="up">\n' % d['altrititle'])
    for t,h in d['altri']: o.append('      <a href="%s">%s</a>\n' % (h,t))
    o.append('    </div>\n  </div>\n</section>\n')
    return ''.join(o)

def jsonld(d, org):
    lang = d['lang']; u = SITE + d['url']
    svc = {"@type":"Service","@id":u+"#service","name":d['svc']['name'],
           "serviceType":d['svc']['type'],"description":d['svc']['desc'],
           "provider":{"@id":SITE+"/#organization"},
           "areaServed":d['svc']['area'],"availableLanguage":d['svc']['lingue']}
    if d['svc'].get('catalogo'):
        svc["hasOfferCatalog"]={"@type":"OfferCatalog","name":d['svc']['name'],
            "itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":x}}
                               for x in d['svc']['catalogo']]}
    wp = {"@type":"WebPage","@id":u+"#webpage","url":u,"name":d['title'],
          "description":d['desc'],"inLanguage":LOC[lang],
          "isPartOf":{"@id":SITE+"/#website"},"about":{"@id":u+"#service"},
          "publisher":{"@id":SITE+"/#organization"},
          "primaryImageOfPage":{"@id":SITE+"/#logo"},
          "breadcrumb":{"@id":u+"#breadcrumb"},
          "datePublished":pd.OGGI,"dateModified":pd.OGGI}
    items=[{"@type":"ListItem","position":1,"name":"Home","item":SITE+HOME[lang]}]
    for i,(n,h) in enumerate(d['crumbs'], start=2):
        items.append({"@type":"ListItem","position":i,"name":n,"item":SITE+(h or d['url'])})
    bc={"@type":"BreadcrumbList","@id":u+"#breadcrumb","itemListElement":items}
    faq={"@type":"FAQPage","@id":u+"#faq","inLanguage":LOC[lang],
         "mainEntity":[{"@type":"Question","name":q,
                        "acceptedAnswer":{"@type":"Answer","text":r}} for q,r in d['faq']]}
    return json.dumps({"@context":"https://schema.org","@graph":[org,svc,wp,bc,faq]},
                      ensure_ascii=False, indent=2)

def build(d):
    lang = d['lang']; u = SITE + d['url']
    src = open(os.path.join(ROOT, DONOR[lang]), encoding='utf-8').read()
    head, body = src.split('</head><body>', 1)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', head, re.S)
    org = json.loads(m.group(1))['@graph'][0]
    head = head[:m.start()] + '<script type="application/ld+json">\n' + jsonld(d, org) + '\n</script>' + head[m.end():]
    head = re.sub(r'<title>.*?</title>', lambda _: '<title>%s</title>' % e(d['title']), head, count=1, flags=re.S)
    for pat, rep in [
        (r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % html.escape(d['desc'])),
        (r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % u),
        (r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % u),
        (r'<meta property="og:locale" content="[^"]*">', '<meta property="og:locale" content="%s">' % OGL[lang]),
        (r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % html.escape(d['ogtitle'])),
        (r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % html.escape(d['ogdesc'])),
        (r'<meta name="twitter:title" content="[^"]*">', '<meta name="twitter:title" content="%s">' % html.escape(d['ogtitle'])),
        (r'<meta name="twitter:description" content="[^"]*">', '<meta name="twitter:description" content="%s">' % html.escape(d['ogdesc'])),
    ]:
        head = re.sub(pat, lambda _m, r=rep: r, head, count=1)
    alt = ('<link rel="alternate" hreflang="%s" href="%s">\n'
           '<link rel="alternate" hreflang="x-default" href="%s">' % (lang, u, u))
    head = re.sub(r'<link rel="alternate" hreflang="[a-z]{2}".*?hreflang="x-default" href="[^"]*">',
                  lambda _: alt, head, count=1, flags=re.S)
    body = re.sub(r'(<main id="main">)(.*?)(</main>)',
                  lambda mm: mm.group(1)+'\n\n'+main_html(d)+'\n'+mm.group(3), body, count=1, flags=re.S)
    # selettore lingua: la pagina esiste solo in questa lingua
    for pat, cls in ((r'(<span class="lang-links">)(.*?)(</span>)','\n        '),
                     (r'(<div class="mob-lang-links">)(.*?)(</div>)','\n    ')):
        body = re.sub(pat, lambda mm, c=cls: mm.group(1)+c+
            '<a href="%s" hreflang="%s" aria-current="page">%s</a>' % (d['url'], lang, lang.upper())+
            c+mm.group(3), body, count=1, flags=re.S)
    out = os.path.join(ROOT, d['url'].strip('/'))
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out,'index.html'),'w',encoding='utf-8').write(head+'</head><body>'+body)
    return os.path.join(d['url'].strip('/'),'index.html')

if __name__ == '__main__':
    for d in pd.PAGINE:
        p = build(d)
        n = len(open(os.path.join(ROOT,p),encoding='utf-8').read())
        print('%-3s  %-40s  %6d byte' % (d['lang'], d['url'], n))
