# -*- coding: utf-8 -*-
"""Aggiunge la sezione Prezzi alle cinque home, la voce di menu, le chiavi dei
   dizionari, il link nel footer e i prezzi nei dati strutturati."""
import os, re, json, html, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('dati', os.path.join(HERE, 'prezzi-dati.py'))
dati = importlib.util.module_from_spec(spec); spec.loader.exec_module(dati)
D, SITE, URLP, NUM, LBL = dati.D, dati.SITE, dati.URLP, dati.NUM, dati.LBL
HOMEF = {'it':'index.html','en':'en/index.html','de':'de/index.html','fr':'fr/index.html','es':'es/index.html'}
FROM_KEYS = {'app_una','gest_da'}
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<path d="M5 12h14M13 6l6 6-6 6"></path></svg>')

# ------------------------------------------------- testi della sezione in home
H = {
'it':{'eyebrow':'Prezzi','title':'Quanto costa,<br><span class="grad">detto subito.</span>',
 'lead':'Le cifre stanno scritte, non si scoprono in fondo a una call. Tutti i prezzi sono IVA inclusa.',
 'more':'Vedi il listino completo',
 'c':[('Sito web','Sito in abbonamento o sito vostro','24,80 €','al mese','oppure 350 € una tantum + 150 € di SEO su Google e Bing',
       'IVA inclusa · durata minima 24 mesi',['Dominio e hosting inclusi','Manutenzione e modifiche comprese','Nessun costo di avvio'],'Dettagli'),
      ('Applicazione web','Web app in canone o pronta da subito','50 €','al mese','oppure da 750 € una tantum, operativa subito',
       'IVA inclusa · attivazione senza costi',['Hosting e aggiornamenti inclusi','Utenti, ruoli e permessi','Assistenza compresa'],'Dettagli'),
      ('Gestionale aziendale','Gestionale su misura','da 1.500 €','a progetto','cifra definita dopo l\'analisi gratuita',
       'IVA inclusa · prezzo fisso, non cambia in corsa',['Analisi dei vostri processi','Migrazione dei dati','Formazione inclusa'],'Dettagli')]},
'en':{'eyebrow':'Pricing','title':'What it costs,<br><span class="grad">said upfront.</span>',
 'lead':'The figures are written down, not revealed at the end of a call. All prices include VAT.',
 'more':'See the full price list',
 'c':[('Website','Monthly plan or website you own','€24.80','per month','or €350 one-off + €150 SEO on Google and Bing',
       'VAT included · 24-month minimum term',['Domain and hosting included','Maintenance and changes included','No setup fee'],'Details'),
      ('Web app','Monthly plan or ready to use','€50','per month','or from €750 one-off, running from day one',
       'VAT included · no activation fee',['Hosting and updates included','Users, roles and permissions','Support included'],'Details'),
      ('Business ERP','Custom management system','from €1,500','per project','figure set after the free analysis',
       'VAT included · fixed price, no mid-project changes',['We map your processes','Data migration','Training included'],'Details')]},
'de':{'eyebrow':'Preise','title':'Was es kostet,<br><span class="grad">vorher gesagt.</span>',
 'lead':'Die Zahlen stehen hier, nicht erst am Ende eines Gesprächs. Alle Preise inklusive MwSt.',
 'more':'Zur vollständigen Preisliste',
 'c':[('Website','Website im Abo oder als Eigentum','24,80 €','pro Monat','oder 350 € einmalig + 150 € SEO bei Google und Bing',
       'inkl. MwSt. · Mindestlaufzeit 24 Monate',['Domain und Hosting inklusive','Wartung und Änderungen enthalten','Keine Einrichtungsgebühr'],'Details'),
      ('Web-App','Web-App im Abo oder sofort fertig','50 €','pro Monat','oder ab 750 € einmalig, sofort einsatzbereit',
       'inkl. MwSt. · keine Aktivierungsgebühr',['Hosting und Updates inklusive','Benutzer, Rollen, Rechte','Support enthalten'],'Details'),
      ('ERP-System','ERP nach Maß','ab 1.500 €','pro Projekt','Betrag nach der kostenlosen Analyse',
       'inkl. MwSt. · Festpreis, keine Nachträge',['Aufnahme Ihrer Prozesse','Datenübernahme','Schulung inklusive'],'Details')]},
'fr':{'eyebrow':'Tarifs','title':'Ce que ça coûte,<br><span class="grad">dit tout de suite.</span>',
 'lead':'Les montants sont écrits, pas révélés au bout d\'un rendez-vous. Tous les prix sont TVA incluse.',
 'more':'Voir la grille complète',
 'c':[('Site internet','Site en abonnement ou site à vous','24,80 €','par mois','ou 350 € en une fois + 150 € de SEO Google et Bing',
       'TVA incluse · durée minimale 24 mois',['Domaine et hébergement inclus','Maintenance et modifications comprises','Sans frais de mise en service'],'Détails'),
      ('Application web','En abonnement ou prête à l\'emploi','50 €','par mois','ou à partir de 750 € en une fois, opérationnelle tout de suite',
       'TVA incluse · sans frais d\'activation',['Hébergement et mises à jour inclus','Utilisateurs, rôles, permissions','Assistance comprise'],'Détails'),
      ('Logiciel de gestion','Logiciel de gestion sur mesure','dès 1 500 €','par projet','montant fixé après l\'analyse gratuite',
       'TVA incluse · prix ferme, sans dérive',['Analyse de vos processus','Reprise des données','Formation incluse'],'Détails')]},
'es':{'eyebrow':'Precios','title':'Cuánto cuesta,<br><span class="grad">dicho ya.</span>',
 'lead':'Las cifras están escritas, no se descubren al final de una llamada. Todos los precios con IVA incluido.',
 'more':'Ver las tarifas completas',
 'c':[('Página web','Web con cuota o web en propiedad','24,80 €','al mes','o 350 € en un pago + 150 € de SEO en Google y Bing',
       'IVA incluido · permanencia mínima 24 meses',['Dominio y alojamiento incluidos','Mantenimiento y cambios incluidos','Sin coste de alta'],'Detalles'),
      ('Aplicación web','Con cuota o lista desde el primer día','50 €','al mes','o desde 750 € en un pago, operativa enseguida',
       'IVA incluido · sin coste de activación',['Alojamiento y actualizaciones incluidos','Usuarios, roles y permisos','Soporte incluido'],'Detalles'),
      ('Software de gestión','Software de gestión a medida','desde 1.500 €','por proyecto','cifra definida tras el análisis gratuito',
       'IVA incluido · precio cerrado, sin sorpresas',['Análisis de vuestros procesos','Migración de datos','Formación incluida'],'Detalles')]},
}

def esc(s): return html.escape(s, quote=False)

CSS = """
/* ---------- PREZZI ---------- */
.price-grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));align-items:stretch;margin-top:8px}
.price-card{position:relative;display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--line);
  border-radius:var(--r-md);padding:32px 30px;overflow:hidden;transition:border-color .35s,background .35s,transform .35s var(--ease)}
.price-card::before{content:"";position:absolute;inset:0;opacity:0;transition:opacity .35s;pointer-events:none;
  background:radial-gradient(360px circle at var(--mx,50%) var(--my,50%),rgba(30,107,255,.14),transparent 70%)}
.price-card:hover::before{opacity:1}
.price-card:hover{border-color:var(--line-strong);background:var(--panel-2)}
.price-kind{display:block;color:var(--blue-2);margin-bottom:13px}
.price-card h3{font-family:'Sora',sans-serif;font-size:1.2rem;font-weight:700;letter-spacing:-.02em;margin-bottom:20px}
.price-amt{font-family:'Sora',sans-serif;display:flex;align-items:baseline;flex-wrap:wrap;gap:8px;letter-spacing:-.03em;margin-bottom:9px}
.price-amt b{font-size:clamp(1.95rem,4.2vw,2.6rem);font-weight:700;line-height:1.05;
  background:linear-gradient(100deg,#fff 10%,var(--blue-2) 60%,#fff 95%);-webkit-background-clip:text;background-clip:text;color:transparent}
.price-amt span{font-family:'Inter',sans-serif;font-size:15px;font-weight:500;color:var(--muted)}
.price-extra{font-size:14.5px;color:var(--text);margin-bottom:9px}
.price-note{font-size:13px;line-height:1.55;color:var(--muted-2);margin-bottom:20px}
.price-list{list-style:none;display:grid;gap:11px;margin-bottom:28px}
.price-list li{position:relative;padding-left:27px;color:var(--muted);font-size:15px;line-height:1.55}
.price-list li::before{content:"";position:absolute;left:1px;top:.5em;width:11px;height:6px;
  border-left:1.9px solid var(--blue-2);border-bottom:1.9px solid var(--blue-2);transform:rotate(-45deg)}
.price-card .btn{margin-top:auto;align-self:flex-start}
.price-foot{margin-top:34px}
@media (max-width:1180px){nav.links a[data-nav-opt]{display:none}}
@media (max-width:560px){.price-card{padding:27px 23px}}
"""

def section(lang):
    h = H[lang]; u = URLP[lang]
    o = ['<!-- ===== PREZZI ===== -->\n<section id="prezzi">\n  <div class="wrap">\n'
         '    <div class="sec-head">\n'
         '      <div class="eyebrow mono" data-scramble="" data-i18n="prezzi.eyebrow">%s</div>\n'
         '      <h2 class="title" data-rv="up" data-i18n-html="prezzi.title">%s</h2>\n'
         '      <p class="lead" data-rv="up" data-i18n="prezzi.lead">%s</p>\n    </div>\n'
         '    <div class="price-grid">\n' % (esc(h['eyebrow']), h['title'], esc(h['lead']))]
    for i, (k, t, a, un, ex, n, li, b) in enumerate(h['c'], start=1):
        o.append('      <article class="price-card" data-tilt="" data-rv="blur" style="transition-delay: %dms;">\n'
                 '        <span class="price-kind mono" data-i18n="prezzi.c%d.k">%s</span>\n'
                 '        <h3 data-i18n="prezzi.c%d.t">%s</h3>\n'
                 '        <p class="price-amt"><b data-i18n="prezzi.c%d.a">%s</b><span data-i18n="prezzi.c%d.u">%s</span></p>\n'
                 '        <p class="price-extra" data-i18n="prezzi.c%d.e">%s</p>\n'
                 '        <p class="price-note" data-i18n="prezzi.c%d.n">%s</p>\n'
                 '        <ul class="price-list" data-i18n-html="prezzi.c%d.l">%s</ul>\n'
                 '        <a href="%s" data-pricing class="btn btn-g" data-mag><span class="lbl" data-i18n="prezzi.c%d.b">%s</span></a>\n'
                 '      </article>\n'
                 % ((i-1)*90, i, esc(k), i, esc(t), i, esc(a), i, esc(un), i, esc(ex), i, esc(n),
                    i, ''.join('<li>%s</li>' % esc(x) for x in li), u, i, esc(b)))
    o.append('    </div>\n    <p class="price-foot" data-rv="up">'
             '<a href="%s" data-pricing class="btn btn-p" data-mag><span class="sheen"></span>'
             '<span class="lbl" data-i18n="prezzi.more">%s</span> %s</a></p>\n'
             '  </div>\n</section>\n\n<div class="wrap"><div class="divider"></div></div>\n\n'
             % (u, esc(h['more']), ARROW))
    return ''.join(o)

def dict_block(lang):
    h = H[lang]
    def q(s): return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"
    rows = ["  prezzi:{eyebrow:%s,title:%s,lead:%s,more:%s," % (q(h['eyebrow']), q(h['title']), q(h['lead']), q(h['more']))]
    for i, (k, t, a, un, ex, n, li, b) in enumerate(h['c'], start=1):
        rows.append("    c%d:{k:%s,t:%s,a:%s,u:%s,e:%s,n:%s,l:%s,b:%s},"
                    % (i, q(k), q(t), q(a), q(un), q(ex), q(n),
                       q(''.join('<li>%s</li>' % esc(x) for x in li)), q(b)))
    rows[-1] = rows[-1].rstrip(',')
    rows.append("  },")
    return '\n'.join(rows) + '\n'

def offers_ld(lang):
    out = []
    for name, desc, key, unit, dur in D[lang]['offers']:
        val = float(NUM[key])
        if unit == 'MON':
            ps = {"@type": "UnitPriceSpecification", "price": val, "priceCurrency": "EUR",
                  "valueAddedTaxIncluded": True, "unitCode": "MON"}
            if dur: ps["billingDuration"] = dur; ps["billingIncrement"] = 1
        elif key in FROM_KEYS:
            ps = {"@type": "PriceSpecification", "minPrice": val, "priceCurrency": "EUR", "valueAddedTaxIncluded": True}
        else:
            ps = {"@type": "PriceSpecification", "price": val, "priceCurrency": "EUR", "valueAddedTaxIncluded": True}
        out.append({"@type": "Offer", "name": name, "description": desc, "price": val,
                    "priceCurrency": "EUR", "availability": "https://schema.org/InStock",
                    "url": SITE + URLP[lang], "priceSpecification": ps,
                    "itemOffered": {"@type": "Service", "name": name}})
    return out

def patch(lang):
    path = os.path.join(ROOT, HOMEF[lang]); s = open(path, encoding='utf-8').read()
    done = []
    # 1. css inline
    if '.price-card' not in s:
        i = s.index('</style>'); s = s[:i] + CSS + s[i:]; done.append('css')
    # 2. sezione
    if '<section id="prezzi">' not in s:
        i = s.index('<!-- ===== SETTORI ===== -->'); s = s[:i] + section(lang) + s[i:]; done.append('sezione')
    # 3. voce di menu (desktop + mobile) e marcatura del link meno importante
    if 'data-i18n="nav.prezzi"' not in s:
        s = s.replace('<a href="#clienti">Clienti</a>', '<a href="#clienti" data-nav-opt>Clienti</a>')
        s = re.sub(r'(<a href="#servizi" data-i18n="nav\.servizi">[^<]*</a>)',
                   r'\1\n      <a href="#prezzi" data-i18n="nav.prezzi">' + LBL[lang] + '</a>', s)
        done.append('menu')
    # 4. link Prezzi nella colonna footer statica
    if 'id="fc2"' in s and URLP[lang] not in s.split('id="fc2"')[1][:600]:
        s = re.sub(r'(<ul id="fc2">)', r'\1<li><a href="%s">%s</a></li>' % (URLP[lang], LBL[lang]), s, count=1)
        done.append('footer')
    # 5. prezzi nei dati strutturati della home
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    g = json.loads(m.group(1))
    org = g['@graph'][0]
    if 'makesOffer' not in org:
        org['makesOffer'] = offers_ld(lang)
        s = s[:m.start()] + '<script type="application/ld+json">\n' + \
            json.dumps(g, ensure_ascii=False, indent=2) + '\n</script>' + s[m.end():]
        done.append('json-ld')
    open(path, 'w', encoding='utf-8').write(s)
    # 6. dizionario
    dpath = os.path.join(ROOT, 'assets/js/i18n-%s.js' % lang); t = open(dpath, encoding='utf-8').read()
    if 'prezzi:{' not in t:
        t = re.sub(r'(\n  mq:\[)', '\n' + dict_block(lang) + r'\1', t, count=1)
        open(dpath, 'w', encoding='utf-8').write(t); done.append('dizionario')
    # nav.prezzi nel dizionario
    if "nav:{" in t and "prezzi:'" not in t.split('nav:{')[1][:300]:
        t = re.sub(r"(nav:\{servizi:'[^']*',)", r"\1prezzi:'%s'," % LBL[lang], t, count=1)
        open(dpath, 'w', encoding='utf-8').write(t); done.append('nav-dict')
    return done

if __name__ == '__main__':
    for lang in ('it', 'en', 'de', 'fr', 'es'):
        print('%-3s  %s' % (lang, ', '.join(patch(lang)) or 'nessuna modifica'))
