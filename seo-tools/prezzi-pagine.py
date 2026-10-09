# -*- coding: utf-8 -*-
"""Inserisce il blocco prezzi (schede + dati strutturati) nelle pagine
   'quanto costa' e nelle pagine di servizio, e aggiunge il link Prezzi
   nel menu e nel footer di tutte le pagine interne."""
import os, re, json, html, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('dati', os.path.join(HERE, 'prezzi-dati.py'))
dati = importlib.util.module_from_spec(spec); spec.loader.exec_module(dati)
D, SITE, URLP, NUM, LBL = dati.D, dati.SITE, dati.URLP, dati.NUM, dati.LBL
HOME = {'it':'/','en':'/en/','de':'/de/','fr':'/fr/','es':'/es/'}
FROM_KEYS = {'app_una','gest_da'}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<path d="M5 12h14M13 6l6 6-6 6"></path></svg>')

T = {'it':('Il nostro prezzo','Quanto costa <span class="grad">da noi</span>','Vedi tutti i prezzi'),
     'en':('Our price','What it costs <span class="grad">with us</span>','See all prices'),
     'de':('Unser Preis','Was es <span class="grad">bei uns kostet</span>','Alle Preise ansehen'),
     'fr':('Notre prix','Combien ça coûte <span class="grad">chez nous</span>','Voir tous les tarifs'),
     'es':('Nuestro precio','Cuánto cuesta <span class="grad">con nosotros</span>','Ver todos los precios')}

# pagina -> indice della categoria (0 sito, 1 web app, 2 gestionale)
PAGES = {
 'it':[('quanto-costa-un-sito-web',0),('quanto-costa-una-app',1),('quanto-costa-un-gestionale',2),
       ('servizi/siti-web-ecommerce',0),('servizi/app-su-misura',1),('servizi/gestionali-crm',2)],
 'en':[('en/how-much-does-a-website-cost',0),('en/services/websites-ecommerce',0),
       ('en/services/custom-apps',1),('en/services/erp-crm',2)],
 'de':[('de/was-kostet-eine-website',0),('de/leistungen/websites-ecommerce',0),
       ('de/leistungen/individuelle-apps',1),('de/leistungen/warenwirtschaft-crm',2)],
 'fr':[('fr/prix-creation-site-internet',0),('fr/services/sites-web-ecommerce',0),
       ('fr/services/applications-sur-mesure',1),('fr/services/erp-crm',2)],
 'es':[('es/cuanto-cuesta-una-pagina-web',0),('es/servicios/webs-ecommerce',0),
       ('es/servicios/apps-a-medida',1),('es/servicios/erp-crm',2)],
}
# offerte per categoria
CAT_OFFERS = {0:[0,1,2], 1:[3,4], 2:[5]}

def esc(s): return html.escape(s, quote=False)

def offer_json(lang, i, url):
    name, desc, key, unit, dur = D[lang]['offers'][i]
    val = float(NUM[key])
    if unit == 'MON':
        ps = {"@type":"UnitPriceSpecification","price":val,"priceCurrency":"EUR",
              "valueAddedTaxIncluded":True,"unitCode":"MON"}
        if dur: ps["billingDuration"]=dur; ps["billingIncrement"]=1
    elif key in FROM_KEYS:
        ps = {"@type":"PriceSpecification","minPrice":val,"priceCurrency":"EUR","valueAddedTaxIncluded":True}
    else:
        ps = {"@type":"PriceSpecification","price":val,"priceCurrency":"EUR","valueAddedTaxIncluded":True}
    return {"@type":"Offer","name":name,"description":desc,"price":val,"priceCurrency":"EUR",
            "availability":"https://schema.org/InStock","url":url,"priceSpecification":ps,
            "seller":{"@id":SITE+"/#organization"},
            "itemOffered":{"@type":"Service","name":name}}

def block(lang, cat_i):
    cat = D[lang]['cats'][cat_i]; eyebrow, h2, more = T[lang]; home = HOME[lang]
    o = ['\n<section id="prezzo">\n  <div class="wrap">\n    <div class="sec-head">\n'
         '      <div class="eyebrow mono" data-scramble>%s</div>\n'
         '      <h2 class="title" data-rv="up">%s</h2>\n'
         '      <p class="lead" data-rv="up">%s</p>\n    </div>\n    <div class="price-grid">\n'
         % (esc(eyebrow), h2, esc(cat['intro']))]
    for c in cat['cards']:
        cls = 'price-card feat' if c.get('feat') else 'price-card'
        o.append('      <article class="%s" data-tilt data-rv="blur">\n' % cls)
        if c.get('badge'): o.append('        <span class="price-badge">%s</span>\n' % esc(c['badge']))
        o.append('        <span class="price-kind mono">%s</span>\n        <h3>%s</h3>\n'
                 '        <p class="price-amt"><b>%s</b><span>%s</span></p>\n'
                 % (esc(c['kind']), esc(c['name']), esc(c['amt']), esc(c['unit'])))
        if c.get('extra'): o.append('        <p class="price-extra">%s</p>\n' % esc(c['extra']))
        o.append('        <p class="price-note">%s</p>\n' % esc(c['note']))
        if c.get('tot'): o.append('        <p class="price-tot">%s</p>\n' % esc(c['tot']))
        o.append('        <ul class="price-list">%s</ul>\n'
                 % ''.join('<li>%s</li>' % esc(x) for x in c['list']))
        o.append('        <a href="%s#contatti" class="btn btn-g" data-mag><span class="lbl">%s</span></a>\n'
                 '      </article>\n' % (home, esc(c['cta'])))
    o.append('    </div>\n    <p class="price-foot" data-rv="up">'
             '<a href="%s" class="btn btn-p" data-mag><span class="sheen"></span>'
             '<span class="lbl">%s</span> %s</a></p>\n  </div>\n</section>\n' % (URLP[lang], esc(more), ARROW))
    return ''.join(o)

def patch_block(lang, rel, cat_i):
    path = os.path.join(ROOT, rel, 'index.html')
    if not os.path.exists(path): return 'MANCA'
    s = open(path, encoding='utf-8').read()
    if 'id="prezzo"' in s: return 'gia fatto'
    anchor = '<section id="faq">' if '<section id="faq">' in s else '<section class="pg-cta">'
    i = s.index(anchor)
    s = s[:i] + block(lang, cat_i) + '\n' + s[i:]
    # offerte nel nodo Service dei dati strutturati
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    if m:
        g = json.loads(m.group(1)); url = SITE + '/' + rel + '/'
        for n in g.get('@graph', []):
            if n.get('@type') == 'Service' and 'offers' not in n:
                n['offers'] = [offer_json(lang, k, url) for k in CAT_OFFERS[cat_i]]
                break
        s = s[:m.start()] + '<script type="application/ld+json">\n' + \
            json.dumps(g, ensure_ascii=False, indent=2) + '\n</script>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)
    return 'ok'

# ------------------------------------------------ menu e footer su tutte le pagine
def lang_of(rel):
    for l in ('en','de','fr','es'):
        if rel.startswith(l + '/'): return l
    return 'it'

def patch_nav(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
    if rel in ('index.html','en/index.html','de/index.html','fr/index.html','es/index.html'): return None
    lang = lang_of(rel); s = open(path, encoding='utf-8').read()
    if '>%s</a>' % LBL[lang] in s and URLP[lang] in s and 'nav-prezzi' in s: return None
    self_page = rel.startswith(os.path.relpath(os.path.join(ROOT, dati.OUT[lang]), ROOT).replace(os.sep,'/'))
    cur = ' aria-current="page"' if self_page else ''
    link = '<a href="%s" class="nav-prezzi"%s>%s</a>' % (URLP[lang], cur, LBL[lang])
    n = [0]
    def rep(m):
        n[0] += 1
        return '%s\n%s%s' % (link, m.group(1), m.group(0))
    # prima del link "Contatti" nei due menu
    s2 = re.sub(r'(?m)^(\s*)(<a href="[^"]*#contatti"[^>]*>[^<]*</a>)$',
                lambda m: '%s%s\n%s%s' % (m.group(1), link, m.group(1), m.group(2)), s)
    changed = (s2 != s)
    # voce nel footer, colonna Agenzia
    s3 = re.sub(r'(<h5>(?:Agenzia|Agency|Agentur|Agence|Agencia)</h5><ul>)',
                r'\1\n        <li><a href="%s">%s</a></li>' % (URLP[lang], LBL[lang]), s2, count=1)
    if s3 != s: open(path, 'w', encoding='utf-8').write(s3)
    return 'ok' if s3 != s else None

if __name__ == '__main__':
    for lang, items in PAGES.items():
        for rel, cat in items:
            print('%-3s  %-42s  %s' % (lang, rel, patch_block(lang, rel, cat)))
    n = 0
    for dp, _, fn in os.walk(ROOT):
        if 'seo-tools' in dp or '_archivio' in dp: continue
        if 'index.html' in fn:
            if patch_nav(os.path.join(dp, 'index.html')): n += 1
    print('\nmenu + footer aggiornati su %d pagine interne' % n)
