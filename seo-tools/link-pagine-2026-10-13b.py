# -*- coding: utf-8 -*-
"""Collega le 15 pagine del 13/10/2026 (pagine-dati-7.py): box 'Pagine collegate', footer (Settori, Web),
   indice /guide/ e llms.txt. Idempotente.  Uso: python3 seo-tools/link-pagine-2026-10-13b.py"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = 'https://danova-tech.com'
N = {'rist': ('/gestionale-ristorante/', 'Gestionale per ristoranti'), 'hotel': ('/gestionale-hotel/', 'Gestionale per hotel'), 'neg': ('/gestionale-negozio/', 'Gestionale per negozi'),
     'salone': ('/gestionale-parrucchieri-centri-estetici/', 'Gestionale per parrucchieri e centri estetici'), 'dent': ('/gestionale-studio-dentistico/', 'Gestionale per studi dentistici'),
     'imm': ('/gestionale-agenzia-immobiliare/', 'Gestionale per agenzie immobiliari'), 'auto': ('/gestionale-autonoleggio/', 'Gestionale per autonoleggio'),
     'seol': ('/seo-locale/', 'SEO locale e Google Maps'), 'wa': ('/whatsapp-aziendale/', 'WhatsApp aziendale'), 'mkt': ('/marketing-per-pmi/', 'Web marketing per PMI'),
     'crm': ('/guide/cos-e-un-crm/', 'Cos&#8217;è un CRM'), 'gest': ('/guide/cos-e-un-gestionale/', 'Cos&#8217;è un gestionale'), 'xls': ('/guide/gestione-magazzino-con-excel/', 'Gestione magazzino con Excel'),
     'maps': ('/guide/come-inserire-attivita-su-google-maps/', 'Come inserire l&#8217;attività su Google Maps'), 'prima': ('/guide/come-andare-in-prima-pagina-su-google/', 'Come andare in prima pagina su Google')}
MAP = {'siti-web-per-ristoranti': ['rist', 'seol'], 'app-prenotazioni': ['rist', 'salone', 'hotel'], 'software-gestionale-magazzino': ['xls', 'neg', 'rist'], 'servizi/gestionali-crm': ['rist', 'hotel', 'neg', 'crm', 'gest'],
       'software-gestionale-aziendale': ['gest', 'rist', 'hotel', 'neg'], 'siti-web-per-hotel': ['hotel', 'seol'], 'ecommerce-collegato-al-gestionale': ['neg'], 'realizzazione-ecommerce': ['neg'],
       'app-fidelizzazione-clienti': ['neg', 'salone'], 'web-agency-oderzo-motta-di-livenza': ['salone', 'seol'], 'software-gestionale-studi-professionali': ['dent'], 'realizzazione-landing-page': ['dent', 'mkt'],
       'siti-web-per-agenzie-immobiliari': ['imm', 'seol'], 'crm-aziendale': ['crm', 'imm', 'wa'], 'software-gestione-flotte': ['auto'], 'software-gestionale-noleggio': ['auto'],
       'servizi/seo': ['seol', 'prima', 'maps'], 'consulente-seo-treviso': ['seol', 'maps'], 'guide/google-business-profile-guida': ['maps', 'seol'], 'come-ottenere-recensioni-google': ['seol', 'maps'],
       'posizionamento-sito-google': ['prima', 'seol'], 'consulente-seo': ['prima', 'seol'], 'come-indicizzare-un-sito-su-google': ['prima', 'maps'], 'automazioni-n8n': ['wa'], 'chatbot-aziendale': ['wa'],
       'servizi/software-automazioni': ['wa'], 'servizi/google-ads': ['mkt'], 'servizi/meta-ads': ['mkt'], 'lead-generation-b2b': ['mkt', 'wa'], 'quanto-costa-google-ads': ['mkt'],
       'guide/differenza-gestionale-erp-crm': ['crm', 'gest'], 'guide/come-scegliere-un-gestionale': ['gest', 'xls'], 'quanto-costa-un-gestionale': ['gest', 'rist', 'hotel'], 'software-per-pmi': ['gest', 'mkt'],
       'app-magazzino-codici-a-barre': ['xls'], 'guide/sostituire-excel-con-un-gestionale': ['xls', 'gest'], 'software-wms': ['xls'], 'gestionale-officina-meccanica': ['auto'], 'gestionale-palestra': ['salone']}
n = 0
for page, keys in MAP.items():
    p = os.path.join(ROOT, page, 'index.html')
    if not os.path.exists(p): print('manca', page); continue
    h = open(p, encoding='utf-8').read(); m = re.search(r'<div class="pg-altri"[^>]*>', h)
    if not m: print('senza box', page); continue
    add = ''.join('<a href="%s">%s</a>' % N[k] for k in keys if 'href="%s"' % N[k][0] not in h)
    if add: h = h[:m.end()] + add + h[m.end():]; open(p, 'w', encoding='utf-8').write(h); n += 1
print('box aggiornati:', n)

# footer: colonna Settori (gestionali per settore) e colonna Web (SEO locale, marketing PMI)
FT = {'Settori': ['rist', 'hotel', 'neg', 'salone', 'dent', 'imm', 'auto'], 'Web': ['seol', 'mkt', 'wa']}
f = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('seo-tools', 'assets', '.git', 'en', 'de', 'fr', 'es', 'zh', 'tr', 'ar')]
    if 'index.html' not in fn: continue
    p = os.path.join(dp, 'index.html'); s = open(p, encoding='utf-8').read(); ch = False
    for col, keys in FT.items():
        m = re.search(r'<div><h5>%s</h5><ul>(.*?)</ul>' % col, s, re.S)
        if not m: continue
        add = ''.join('\n        <li><a href="%s">%s</a></li>' % N[k] for k in keys if 'href="%s"' % N[k][0] not in m.group(1))
        if add: s = s[:m.end(1)] + add + s[m.end(1):]; ch = True
    if ch: open(p, 'w', encoding='utf-8').write(s); f += 1
print('footer aggiornati:', f)

# indice /guide/: schede delle 5 guide nuove
G = [('crm', 'Cos’è un CRM e a cosa serve, spiegato semplice', 'Le cinque cose che fa un CRM, quando serve a una PMI, la differenza con il gestionale e come scegliere quello giusto.'),
     ('gest', 'Cos’è un gestionale aziendale e come funziona', 'I moduli di un gestionale, il principio del dato inserito una volta e i segnali che vi serve davvero.'),
     ('xls', 'Gestione magazzino con Excel: quando basta e quando no', 'Come impostare il foglio articoli e movimenti, i limiti che arrivano presto e il passo successivo.'),
     ('maps', 'Come inserire un’attività su Google Maps', 'Creare e verificare la scheda Google Business Profile, scegliere la categoria e gli errori da evitare.'),
     ('prima', 'Come andare in prima pagina su Google', 'I quattro pilastri del posizionamento, tempi realistici e cinque cose da fare questa settimana.')]
p = os.path.join(ROOT, 'guide', 'index.html'); s = open(p, encoding='utf-8').read()
m = re.search(r'<div class="sect-grid">', s)
card0 = re.search(r'<a class="sect sect-zone" href="[^"]+">(<div class="ic">.*?</div>)<h4>', s, re.S)
if m and card0:
    ic = card0.group(1); add = ''
    for k, t, d in G:
        u = N[k][0]
        if 'href="%s"' % u in s: continue
        add += ('<a class="sect sect-zone" href="%s">%s<h4>%s</h4><p>%s</p><span class="go">Leggi la guida <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span></a>' % (u, ic, t, d))
    if add: s = s[:m.end()] + add + s[m.end():]; open(p, 'w', encoding='utf-8').write(s); print('indice guide: +', add.count('class="sect sect-zone"'))

# llms.txt
p = os.path.join(ROOT, 'llms.txt'); s = open(p, encoding='utf-8').read()
if '/gestionale-ristorante/' not in s:
    s = s.rstrip('\n') + '\n\n## Pagine aggiunte il 13 ottobre 2026\n' + ''.join('- %s: %s%s\n' % (t.replace('&#8217;', '’'), S, u) for u, t in N.values())
    open(p, 'w', encoding='utf-8').write(s); print('llms.txt ok')
