# -*- coding: utf-8 -*-
"""Collega le pagine software del 14/10/2026 (pagine-dati-8.py): box 'Pagine collegate', footer (Software, Web),
   indice /guide/ e llms.txt. Idempotente.  Uso: python3 seo-tools/link-pagine-2026-10-14.py"""
import os, re, json, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('pd', os.path.join(ROOT, 'seo-tools', 'pagine-dati-8.py'))
pd = importlib.util.module_from_spec(spec); spec.loader.exec_module(pd)
N = {'pers': ('/gestionale-personalizzato/', 'Gestionale personalizzato'), 'vs': ('/guide/gestionale-su-misura-o-standard/', 'Gestionale su misura o standard'),
     'ass': ('/gestionale-per-associazioni/', 'Gestionale per associazioni e ASD'), 'tick': ('/software-ticketing/', 'Software ticketing'),
     'vetr': ('/sito-vetrina/', 'Sito vetrina'), 'dash': ('/dashboard-aziendale/', 'Dashboard aziendale'), 'erp': ('/erp-per-piccole-aziende/', 'ERP per piccole aziende'),
     'app': ('/app-personalizzata/', 'App personalizzata'), 'rpa': ('/guide/cos-e-la-rpa/', 'Cos&#8217;è la RPA')}
MAP = {'servizi/gestionali-crm': ['pers', 'vs', 'erp', 'dash'], 'software-gestionale-aziendale': ['pers', 'vs', 'erp'], 'sviluppo-software-su-misura': ['pers', 'app', 'vs'],
       'quanto-costa-un-gestionale': ['pers', 'vs', 'erp'], 'guide/come-scegliere-un-gestionale': ['vs', 'pers'], 'guide/cos-e-un-gestionale': ['vs', 'pers', 'erp'],
       'guide/differenza-gestionale-erp-crm': ['erp', 'vs'], 'guide/sostituire-excel-con-un-gestionale': ['pers', 'dash'], 'software-controllo-di-gestione': ['dash', 'erp'],
       'software-gestione-interventi-tecnici': ['tick'], 'crm-aziendale': ['tick', 'dash'], 'chatbot-aziendale': ['tick'], 'whatsapp-aziendale': ['tick'],
       'gestionale-palestra': ['ass'], 'app-prenotazioni': ['ass', 'app'], 'app-per-personal-trainer': ['ass'],
       'quanto-costa-un-sito-web': ['vetr'], 'realizzazione-siti-internet': ['vetr'], 'sito-web-aziendale': ['vetr'], 'servizi/siti-web-ecommerce': ['vetr'], 'prezzi': ['vetr', 'pers', 'app'],
       'servizi/app-su-misura': ['app'], 'quanto-costa-una-app': ['app'], 'sviluppo-app-aziendali-veneto': ['app'], 'sviluppo-web-app': ['app'],
       'automazione-processi-aziendali': ['rpa'], 'automazioni-n8n': ['rpa'], 'integrazione-software-aziendali': ['rpa', 'dash'], 'servizi/software-automazioni': ['rpa', 'tick'],
       'intelligenza-artificiale-per-aziende': ['rpa'], 'software-gestionale-magazzino': ['erp'], 'software-mes-produzione': ['erp', 'dash'], 'software-house': ['pers', 'app'],
       'gestionali-su-misura-veneto': ['pers', 'vs'], 'software-per-pmi': ['pers', 'erp', 'dash']}
n = 0
for page, keys in MAP.items():
    f = os.path.join(ROOT, page, 'index.html')
    if not os.path.exists(f): print('manca', page); continue
    s = open(f, encoding='utf-8').read(); o = s
    m = re.search(r'<div class="pg-altri"[^>]*>', s)
    if not m: print('niente box', page); continue
    box = s[m.end():s.find('</div>', m.end())]
    add = ''.join(f'\n      <a href="{N[k][0]}">{N[k][1]}</a>' for k in keys if f'href="{N[k][0]}"' not in box)
    s = s[:m.end()] + add + s[m.end():]
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
print('box aggiornati:', n)

# footer: colonna Software e Web su tutte le pagine italiane
F = {'Software': [N['pers'], N['erp'], N['dash'], N['app']], 'Web': [N['vetr']]}
nf = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('seo-tools', 'assets', '.git', 'en', 'de', 'fr', 'es', 'zh', 'zh-hant', 'tr', 'ar')]
    if 'index.html' not in fn: continue
    p = os.path.join(dp, 'index.html'); s = open(p, encoding='utf-8').read(); o = s
    for col, links in F.items():
        m = re.search(rf'(<h5>{col}</h5><ul>)(.*?)(</ul>)', s, re.S)
        if not m: continue
        add = ''.join(f'\n        <li><a href="{u}">{t}</a></li>' for u, t in links if f'href="{u}"' not in m.group(2))
        if add: s = s[:m.end(1)] + add + s[m.end(1):]
    if s != o: open(p, 'w', encoding='utf-8').write(s); nf += 1
print('footer aggiornati:', nf)

# indice guide
f = os.path.join(ROOT, 'guide', 'index.html'); s = open(f, encoding='utf-8').read(); o = s
m = re.search(r'<a class="sect sect-zone" href="/guide/come-scegliere-un-gestionale/">.*?</a>(?=<a class="sect)', s, re.S)
if m:
    ins = ''
    for d in pd.PAGINE:
        if not d['url'].startswith('/guide/') or f'href="{d["url"]}"' in s: continue
        c = m.group(0).replace('/guide/come-scegliere-un-gestionale/', d['url'])
        c = re.sub(r'<h4>.*?</h4>', '<h4>' + re.sub(r'<[^>]+>', '', d['h1']).rstrip('.') + '</h4>', c, 1, flags=re.S)
        c = re.sub(r'<p>.*?</p>', f"<p>{d['desc']}</p>", c, 1, flags=re.S)
        ins += c
    s = s[:m.end()] + ins + s[m.end():]
    j = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', s, re.S)
    g = json.loads(j.group(2))
    for node in g.get('@graph', []):
        if node.get('@type') == 'ItemList':
            have = {x.get('url') for x in node['itemListElement']}
            for d in pd.PAGINE:
                u = 'https://danova-tech.com' + d['url']
                if d['url'].startswith('/guide/') and u not in have:
                    node['itemListElement'].append({"@type": "ListItem", "position": len(node['itemListElement']) + 1, "url": u, "name": re.sub(r'<[^>]+>', '', d['h1'])})
    s = s[:j.start(2)] + '\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n' + s[j.end(2):]
if s != o: open(f, 'w', encoding='utf-8').write(s); print('indice guide aggiornato')
else: print('indice guide: niente da fare' if m else 'indice guide: carta modello non trovata')

# llms.txt
f = os.path.join(ROOT, 'llms.txt'); s = open(f, encoding='utf-8').read()
if '/gestionale-personalizzato/' not in s:
    L = ["", "## Software su misura: pagine del 14 ottobre 2026",
         "Posizionamento: ogni gestionale o app è costruito per una sola azienda, sui suoi processi; non un programma commerciale uguale per tutti. Prima versione in pochi giorni o poche settimane; importazione da Excel e integrazione con i programmi esistenti; uso da PC, tablet e telefono; il cliente sceglie fra canone mensile e pagamento unico."]
    L += [f"- {re.sub(r'<[^>]+>', '', d['h1'])}: https://danova-tech.com{d['url']}" for d in pd.PAGINE]
    s = s.replace('\n## Contatti e informazioni legali', '\n'.join(L) + '\n\n## Contatti e informazioni legali', 1)
    open(f, 'w', encoding='utf-8').write(s); print('llms aggiornato')
