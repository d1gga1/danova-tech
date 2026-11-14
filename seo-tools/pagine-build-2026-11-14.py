# -*- coding: utf-8 -*-
"""14/11/2026 - 32 pagine nuove scelte sui CSV del Keyword Planner del 14/11 (18 IT, 4 EN, 5 DE, 3 FR, 2 ES).
   Dati: seo-tools/pagine-dati-2026-11-14.py (+ i file -comune, -it-ai, -it-web, -it-gest, -estero-1, -estero-2).
   Usa il motore di pagine-build.py con le sezioni 'breve' e la pulizia (robots, CSS, hreflang) di
   pagine-build-2026-10-23.py, come il build del 06/11.
   Aggiorna anche gli hreflang delle pagine IT esistenti che ora hanno una versione estera
   (/agenti-ai-per-aziende/, /whatsapp-aziendale/, /seo-per-intelligenza-artificiale/).
   Idempotente. Uso:  python3 seo-tools/pagine-build-2026-11-14.py
   Poi la sequenza "Come rigenerare" del REPORT-SEO.md (14/11)."""
import os, re, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
M = load('b2310', 'pagine-build-2026-10-23.py')
D = load('d1411', 'pagine-dati-2026-11-14.py')
pb = M.pb; pb.pd = D

for d in D.PAGINE:
    M._cur_lang[0] = d['lang']; M._cur_url[0] = d['url']
    p = M.build(d); f = os.path.join(ROOT, p)
    s = open(f, encoding='utf-8').read()
    s = M.lingue(d, M.hreflang_mancanti(d, s))
    open(f, 'w', encoding='utf-8').write(s)
    print('%-3s  %-48s  %6d byte' % (d['lang'], d['url'], len(s)))

# reciprocita' hreflang sulle pagine IT gia' esistenti
ESISTENTI = {
 '/agenti-ai-per-aziende/': {'it': '/agenti-ai-per-aziende/', 'en': '/en/ai-agents-for-business/', 'de': '/de/ki-agentur/', 'fr': '/fr/agence-ia/', 'es': '/es/agentes-de-ia/'},
 '/whatsapp-aziendale/': {'it': '/whatsapp-aziendale/', 'en': '/en/whatsapp-chatbot/'},
 '/seo-per-intelligenza-artificiale/': {'it': '/seo-per-intelligenza-artificiale/', 'en': '/en/generative-engine-optimization/', 'de': '/de/generative-engine-optimization/'},
}
for url, alt in ESISTENTI.items():
    f = os.path.join(ROOT, url.strip('/'), 'index.html')
    s0 = open(f, encoding='utf-8').read()
    s = M.lingue({'lang': 'it', 'url': url, 'alt': alt}, s0)
    if s != s0:
        open(f, 'w', encoding='utf-8').write(s); print('hreflang aggiornati', url)
    else: print('gia ok', url)

# immagine di anteprima (og/twitter): la piu' vicina tra i mockup esistenti, con il suo alt vero
# (il donatore lasciava la sua, per esempio "Schreinerei in Muenchen" sulle pagine tedesche)
import json, html as H
OGIMG = {
 '/centralino-ai/': 'chatbot-aziendale', '/chatgpt-per-aziende/': 'intelligenza-artificiale-per-aziende',
 '/intelligenza-artificiale-per-commercialisti/': 'software-gestionale-studi-professionali',
 '/intelligenza-artificiale-per-medici/': 'app-prenotazioni', '/sito-web-accessibile/': 'guide-accessibilita-sito-web',
 '/audit-seo/': 'servizi-seo', '/guide/google-ai-mode/': 'seo-per-intelligenza-artificiale',
 '/guide/llms-txt/': 'seo-per-intelligenza-artificiale', '/agenzia-shopify/': 'realizzazione-ecommerce',
 '/ecommerce-vino/': 'aprire-un-negozio-online', '/tiktok-ads/': 'servizi-meta-ads',
 '/bandi-digitalizzazione-2026/': 'bandi-digitalizzazione-veneto-2026', '/gestionale-presenze-turni/': 'app-ore-di-lavoro-e-timbrature',
 '/software-haccp/': 'gestionale-ristorante', '/software-sicurezza-lavoro/': 'software-gestionale-edilizia',
 '/gestionale-case-vacanza/': 'gestionale-hotel', '/gestionale-fisioterapista/': 'gestionale-studio-dentistico',
 '/gestionale-stabilimento-balneare/': 'app-prenotazioni', '/agenti-ai-per-aziende/': 'intelligenza-artificiale-per-aziende',
 '/en/ai-receptionist/': 'en-business-process-automation', '/en/ai-agents-for-business/': 'en-services-software-automation',
 '/en/whatsapp-chatbot/': 'en-custom-crm-development', '/en/generative-engine-optimization/': 'en-services-seo',
 '/de/ki-telefonassistent/': 'de-leistungen-software-automatisierung', '/de/ki-agentur/': 'de-leistungen-software-automatisierung',
 '/de/barrierefreie-website/': 'de-leistungen-websites-ecommerce', '/de/shopify-agentur/': 'de-leistungen-websites-ecommerce',
 '/de/generative-engine-optimization/': 'de-leistungen-seo', '/fr/standard-telephonique-ia/': 'fr-services-logiciels-automatisation',
 '/fr/agence-ia/': 'fr-services-logiciels-automatisation', '/fr/agence-shopify/': 'fr-services-sites-web-ecommerce',
 '/es/agentes-de-ia/': 'es-servicios-software-automatizacion', '/es/agencia-shopify/': 'es-servicios-webs-ecommerce',
}
MK = json.load(open(os.path.join(HERE, 'immagini-sito.json'), encoding='utf-8'))
ALT_DI = {}
for p, v in MK.items():
    ALT_DI.setdefault(p.strip('/').replace('/', '-') or 'home', v['alt'])
for url, img in OGIMG.items():
    f = os.path.join(ROOT, url.strip('/'), 'index.html'); s0 = s = open(f, encoding='utf-8').read()
    og = 'https://danova-tech.com/assets/img/mockup/og/%s.jpg' % img
    s = re.sub(r'(<meta property="og:image" content=")[^"]*(">)', lambda m: m.group(1) + og + m.group(2), s, 1)
    s = re.sub(r'(<meta name="twitter:image" content=")[^"]*(">)', lambda m: m.group(1) + og + m.group(2), s, 1)
    alt = ALT_DI.get(img)
    if alt:
        s = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(">)', lambda m: m.group(1) + H.escape(alt, quote=True) + m.group(2), s, 1)
    if s != s0: open(f, 'w', encoding='utf-8').write(s)
    if not alt: print('alt non trovato per', img)
print('immagini di anteprima impostate:', len(OGIMG))
