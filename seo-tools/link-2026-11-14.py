#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""14/11/2026 - Link interni verso le 32 pagine nuove del 14/11: primo elemento del box
"Approfondisci" (pg-altri) delle pagine correlate, e le due guide nuove nella griglia di /guide/.
Idempotente. Uso: python3 seo-tools/link-2026-11-14.py"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
L = [
 ('/centralino-ai/', 'Centralino AI e segretaria virtuale', ['chatbot-aziendale', 'whatsapp-aziendale', 'agenti-ai-per-aziende', 'intelligenza-artificiale-per-aziende', 'app-prenotazioni', 'servizi/software-automazioni', 'gestionale-studio-medico', 'gestionale-parrucchieri-centri-estetici']),
 ('/chatgpt-per-aziende/', 'ChatGPT per aziende', ['intelligenza-artificiale-per-aziende', 'consulenza-intelligenza-artificiale', 'chatbot-aziendale', 'ai-act-aziende', 'servizi/software-automazioni']),
 ('/intelligenza-artificiale-per-commercialisti/', 'Intelligenza artificiale per commercialisti', ['software-gestionale-studi-professionali', 'intelligenza-artificiale-per-avvocati', 'intelligenza-artificiale-per-aziende', 'software-contabilita-aziendale']),
 ('/intelligenza-artificiale-per-medici/', 'Intelligenza artificiale per medici', ['gestionale-studio-medico', 'gestionale-studio-dentistico', 'intelligenza-artificiale-per-aziende']),
 ('/sito-web-accessibile/', 'Sito web accessibile (WCAG ed EAA)', ['guide/accessibilita-sito-web', 'restyling-sito-web', 'realizzazione-ecommerce', 'servizi/siti-web-ecommerce', 'sito-web-aziendale']),
 ('/audit-seo/', 'Audit SEO e SEO tecnica', ['servizi/seo', 'consulente-seo', 'posizionamento-sito-google', 'seo-locale', 'seo-per-ecommerce', 'come-indicizzare-un-sito-su-google']),
 ('/guide/google-ai-mode/', 'Google AI Mode e AI Overview', ['seo-per-intelligenza-artificiale', 'guide/come-andare-in-prima-pagina-su-google', 'servizi/seo', 'posizionamento-sito-google']),
 ('/guide/llms-txt/', 'llms.txt: cos’è e come si crea', ['seo-per-intelligenza-artificiale', 'glossario']),
 ('/agenzia-shopify/', 'Agenzia Shopify e WooCommerce', ['realizzazione-ecommerce', 'quanto-costa-un-ecommerce', 'migrazione-ecommerce', 'ecommerce-collegato-al-gestionale', 'aprire-un-negozio-online', 'servizi/siti-web-ecommerce', 'seo-per-ecommerce']),
 ('/ecommerce-vino/', 'E-commerce per vino e cantine', ['software-gestionale-agroalimentare', 'realizzazione-ecommerce', 'aprire-un-negozio-online', 'video-prodotto-ecommerce-amazon']),
 ('/tiktok-ads/', 'Agenzia TikTok Ads', ['video-pubblicitari-per-social-e-ads', 'servizi/meta-ads', 'video-pubblicitari', 'marketing-per-pmi', 'servizi/google-ads']),
 ('/bandi-digitalizzazione-2026/', 'Bandi digitalizzazione 2026 in Italia', ['bandi-digitalizzazione-veneto-2026', 'iperammortamento-2026', 'digitalizzazione-aziendale', 'guide/transizione-5-0']),
 ('/gestionale-presenze-turni/', 'Gestionale presenze, turni e ferie', ['app-ore-di-lavoro-e-timbrature', 'servizi/gestionali-crm', 'gestionale-negozio', 'software-per-pmi', 'gestionale-personalizzato']),
 ('/software-haccp/', 'Software HACCP', ['gestionale-ristorante', 'software-gestionale-agroalimentare', 'gestionale-su-misura-per-ogni-settore']),
 ('/software-sicurezza-lavoro/', 'Software sicurezza sul lavoro', ['software-gestionale-edilizia', 'app-gestione-cantieri', 'software-gestionale-manutenzioni', 'software-gestionale-impiantisti']),
 ('/gestionale-case-vacanza/', 'Gestionale case vacanza e affitti brevi', ['gestionale-hotel', 'siti-web-per-hotel', 'app-prenotazioni', 'gestionale-agenzia-immobiliare']),
 ('/gestionale-fisioterapista/', 'Gestionale per fisioterapisti', ['gestionale-studio-medico', 'gestionale-palestra', 'app-prenotazioni', 'gestionale-studio-dentistico']),
 ('/gestionale-stabilimento-balneare/', 'Gestionale stabilimento balneare', ['gestionale-hotel', 'gestionale-ristorante', 'app-prenotazioni', 'gestionale-su-misura-per-ogni-settore']),
 ('/en/ai-receptionist/', 'AI receptionist', ['en/services/software-automation', 'en/business-process-automation', 'en/services', 'en/custom-crm-development']),
 ('/en/ai-agents-for-business/', 'AI agents for business', ['en/services/software-automation', 'en/business-process-automation', 'en/services', 'en/software-development-italy']),
 ('/en/whatsapp-chatbot/', 'WhatsApp chatbot for business', ['en/services/software-automation', 'en/custom-crm-development', 'en/api-integration-services']),
 ('/en/generative-engine-optimization/', 'Generative engine optimization (GEO)', ['en/services/seo', 'en/seo-company-usa', 'en/services']),
 ('/de/ki-telefonassistent/', 'KI-Telefonassistent', ['de/leistungen/software-automatisierung', 'de/leistungen', 'de/leistungen/warenwirtschaft-crm']),
 ('/de/ki-agentur/', 'KI-Agentur: KI-Agenten', ['de/leistungen/software-automatisierung', 'de/leistungen', 'de/individualsoftware-deutschland', 'de/individualsoftware-oesterreich']),
 ('/de/barrierefreie-website/', 'Barrierefreie Website (BFSG)', ['de/leistungen/websites-ecommerce', 'de/webagentur-deutschland', 'de/webagentur-oesterreich']),
 ('/de/shopify-agentur/', 'Shopify-Agentur', ['de/leistungen/websites-ecommerce', 'de/webagentur-deutschland', 'de/webagentur-schweiz', 'de/leistungen']),
 ('/de/generative-engine-optimization/', 'Generative Engine Optimization (GEO)', ['de/leistungen/seo', 'de/webagentur-suedtirol', 'de/leistungen']),
 ('/fr/standard-telephonique-ia/', 'Standard téléphonique IA', ['fr/services/logiciels-automatisation', 'fr/services']),
 ('/fr/agence-ia/', 'Agence IA : agents IA', ['fr/services/logiciels-automatisation', 'fr/services', 'fr/logiciel-sur-mesure-france']),
 ('/fr/agence-shopify/', 'Agence Shopify', ['fr/services/sites-web-ecommerce', 'fr/creation-site-internet-france', 'fr/services']),
 ('/es/agentes-de-ia/', 'Agentes de IA para empresas', ['es/servicios/software-automatizacion', 'es/servicios', 'es/software-a-medida-espana']),
 ('/es/agencia-shopify/', 'Agencia Shopify', ['es/servicios/webs-ecommerce', 'es/diseno-web-espana', 'es/servicios']),
]
n = 0
for url, testo, pagine in L:
    for p in pagine:
        f = os.path.join(p, 'index.html')
        if not os.path.exists(f): print('manca', p); continue
        s = open(f, encoding='utf-8').read()
        if 'href="%s"' % url in s: continue
        m = re.search(r'(<div class="pg-altri"[^>]*>\n?)(\s*)(<a |<!--)', s)
        if not m: print('nessun pg-altri', p); continue
        s = s[:m.end(1)] + m.group(2) + '<a href="%s">%s</a>' % (url, testo) + ('\n' if m.group(2) else '') + s[m.end(1):]
        open(f, 'w', encoding='utf-8').write(s); n += 1
print('link aggiunti:', n)

# le due guide nuove nella griglia di /guide/
ICON = ('<div class="ic"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>'
        '<path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>')
GO = ('<span class="go">Leggi la guida <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
      'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span>')
GUIDE = [('/guide/google-ai-mode/', 'Google AI Mode e AI Overview: come farsi citare',
          'Cosa sono, quando sono arrivati in Italia, come scelgono le fonti e le otto cose che aumentano le probabilità di comparire.'),
         ('/guide/llms-txt/', 'llms.txt: cos’è, a cosa serve e come si crea',
          'Il file per gli assistenti AI spiegato semplice: struttura, differenze con robots.txt e sitemap, e quando conviene.')]
f = 'guide/index.html'; s = open(f, encoding='utf-8').read(); s0 = s
for href, h4, p in GUIDE:
    if 'class="sect sect-zone" href="%s"' % href in s: continue
    card = '<a class="sect sect-zone" href="%s">%s<h4>%s</h4><p>%s</p>%s</a>' % (href, ICON, h4, p, GO)
    s = s.replace('<!--/re-guide-->', '<!--/re-guide-->' + card, 1)
if s != s0: open(f, 'w', encoding='utf-8').write(s); print('guide aggiunte a /guide/')
