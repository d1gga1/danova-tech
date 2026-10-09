# -*- coding: utf-8 -*-
"""Rinforza i collegamenti interni: nuova colonna di footer per i mercati
   esteri e per i settori italiani, piu' le pagine che mancavano."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def li(items): return ''.join('\n        <li><a href="%s">%s</a></li>' % (h, t) for t, h in items)

COL = {
 'it': ('Settori', [
    ('Edilizia e cantieri','/software-gestionale-edilizia/'),
    ('Impianti e manutenzioni','/software-gestionale-impiantisti/'),
    ('Metalmeccanica','/software-gestionale-metalmeccanica/'),
    ('Agroalimentare','/software-gestionale-agroalimentare/'),
    ('Noleggio','/software-gestionale-noleggio/'),
    ('Studi professionali','/software-gestionale-studi-professionali/'),
    ('Gestione commesse','/software-gestionale-commesse/'),
    ('Officine meccaniche','/gestionale-officina-meccanica/'),
    ('Controllo di gestione','/software-controllo-di-gestione/')]),
 'de': ('Märkte', [
    ('Webagentur Deutschland','/de/webagentur-deutschland/'),
    ('Webagentur Österreich','/de/webagentur-oesterreich/'),
    ('Webagentur Schweiz','/de/webagentur-schweiz/'),
    ('Webagentur Berlin','/de/webagentur-berlin/'),
    ('Webagentur München','/de/webagentur-muenchen/'),
    ('Webagentur Hamburg','/de/webagentur-hamburg/'),
    ('Webagentur Frankfurt','/de/webagentur-frankfurt/'),
    ('Webagentur Wien','/de/webagentur-wien/'),
    ('Webagentur Graz','/de/webagentur-graz/'),
    ('Webagentur Zürich','/de/webagentur-zuerich/'),
    ('Webagentur Kärnten','/de/webagentur-kaernten/'),
    ('Webagentur Südtirol','/de/webagentur-suedtirol/'),
    ('Individualsoftware Deutschland','/de/individualsoftware-deutschland/'),
    ('Individualsoftware Österreich','/de/individualsoftware-oesterreich/'),
    ('Softwareentwicklung Schweiz','/de/softwareentwicklung-schweiz/'),
    ('Was kostet eine Website','/de/was-kostet-eine-website/')]),
 'en': ('Markets', [
    ('Software development company UK','/en/software-development-company-uk/'),
    ('Web design agency UK','/en/web-design-agency-uk/'),
    ('Mobile app development UK','/en/mobile-app-development-company-uk/'),
    ('Software development in Italy','/en/software-development-italy/'),
    ('How much does a website cost','/en/how-much-does-a-website-cost/')]),
 'fr': ('Marchés', [
    ('Création de site en France','/fr/creation-site-internet-france/'),
    ('Création de site en Belgique','/fr/creation-site-internet-belgique/'),
    ('Agence web Paris','/fr/agence-web-paris/'),
    ('Agence web Lyon','/fr/agence-web-lyon/'),
    ('Agence web Bruxelles','/fr/agence-web-bruxelles/'),
    ('Agence web Genève','/fr/agence-web-geneve/'),
    ('Agence SEO France','/fr/agence-seo-france/'),
    ('Logiciel sur mesure France','/fr/logiciel-sur-mesure-france/'),
    ('Prix d’un site internet','/fr/prix-creation-site-internet/')]),
 'es': ('Mercados', [
    ('Diseño web España','/es/diseno-web-espana/'),
    ('Diseño web Madrid','/es/diseno-web-madrid/'),
    ('Diseño web Barcelona','/es/diseno-web-barcelona/'),
    ('Diseño web Valencia','/es/diseno-web-valencia/'),
    ('Agencia SEO España','/es/agencia-seo-espana/'),
    ('Software a medida España','/es/software-a-medida-espana/'),
    ('Cuánto cuesta una página web','/es/cuanto-cuesta-una-pagina-web/')]),
}
AGENZIA = {'it':'Agenzia','de':'Agentur','en':'Agency','fr':'Agence','es':'Agencia'}
# pagine che mancavano, da infilare nelle colonne gia' presenti (solo italiano)
EXTRA_IT = {
 'Software': [('App magazzino e codici a barre','/app-magazzino-codici-a-barre/'),
              ('App per agenti di commercio','/app-per-agenti-di-commercio/'),
              ('App rapportini di lavoro','/app-rapportini-di-lavoro/'),
              ('Sviluppo web app','/sviluppo-web-app/'),
              ('App aziendali in Veneto','/sviluppo-app-aziendali-veneto/')],
 'Web':      [('Migrazione e-commerce','/migrazione-ecommerce/'),
              ('Restyling sito web','/restyling-sito-web/'),
              ('Aprire un negozio online','/aprire-un-negozio-online/'),
              ('Quanto costa un e-commerce','/quanto-costa-un-ecommerce/'),
              ("Quanto costa un'app",'/quanto-costa-una-app/')],
}

def lang_of(rel):
    for l in ('en','de','fr','es'):
        if rel.startswith(l+'/'): return l
    return 'it'

n = collections_n = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('seo-tools','assets','.git')]
    if 'index.html' not in fn: continue
    path = os.path.join(dp,'index.html')
    rel = os.path.relpath(path, ROOT).replace(os.sep,'/')
    if rel in ('index.html','en/index.html','de/index.html','fr/index.html','es/index.html'): continue
    L = lang_of(rel); s = open(path, encoding='utf-8').read(); orig = s
    titolo, voci = COL[L]
    if '<h5>%s</h5>' % titolo not in s:
        blocco = '<div><h5>%s</h5><ul>%s\n      </ul></div>\n      ' % (titolo, li(voci))
        s = s.replace('<div><h5>%s</h5><ul>' % AGENZIA[L], blocco + '<div><h5>%s</h5><ul>' % AGENZIA[L], 1)
    if L == 'it':
        for col, items in EXTRA_IT.items():
            m = re.search(r'(<h5>%s</h5><ul>)(.*?)(</ul>)' % col, s, re.S)
            if not m: continue
            nuovi = [x for x in items if 'href="%s"' % x[1] not in m.group(2)]
            if nuovi:
                s = s[:m.end(2)] + li(nuovi) + '\n      ' + s[m.end(2):]
    if s != orig:
        open(path,'w',encoding='utf-8').write(s); n += 1
print('footer rinforzati su %d pagine' % n)
