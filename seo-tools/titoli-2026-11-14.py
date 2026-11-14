# -*- coding: utf-8 -*-
"""14/11/2026: titoli allineati ai CSV del Keyword Planner del 14/11 (fasce di volume mensile tra parentesi).
Cambia <title>, og:title/twitter:title e il "name" del WebPage. Idempotente.
Uso: python3 seo-tools/titoli-2026-11-14.py"""
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = {
 # IT
 'whatsapp-aziendale': "Chatbot WhatsApp e WhatsApp Business API | Danova Tech",            # whatsapp business api 5k, chatbot/bot whatsapp 500
 'aprire-un-negozio-online': "Vendere online: come aprire un negozio online | Danova Tech",     # vendere online 5k, negozio online 5k
 'video-pubblicitari': "Video e spot pubblicitari per aziende in 24 ore | Danova Tech",         # spot pubblicitario 5k, video pubblicitari 500
 'spot-pubblicitari-con-intelligenza-artificiale': "Spot e video con intelligenza artificiale | Danova Tech",  # video con IA 5k
 'video-pubblicitari-per-social-e-ads': "Video per Instagram, TikTok e Meta Ads in 24 ore | Danova Tech",  # video per instagram 500 (+900%)
 'lead-generation-b2b': "Lead generation per aziende e B2B: più contatti | Danova Tech",       # lead generation 5k, acquisizione clienti 500
 'seo-per-intelligenza-artificiale': "GEO e SEO per l'AI: comparire su ChatGPT | Danova Tech",   # geo generative engine optimization 500
 'gestionale-ristorante': "Gestionale ristorante, bar e pizzeria su misura | Danova Tech",       # gestionale bar 500, software ristorazione 500
 'software-contabilita-aziendale': "Software e programma di contabilità aziendale | Danova Tech",  # software/programma contabilita' 500
 'gestionale-cloud': "Gestionale cloud, online e web su misura | Danova Tech",                   # gestionale online/web/in cloud 500
 'portale-rivenditori-b2b': "Portale B2B per rivenditori: ordini e listini | Danova Tech",      # portale b2b 500
 'gestionali-su-misura-milano': "Software house a Milano: gestionali su misura | Danova Tech",  # software house milano 500
 'consulente-seo': "Consulente SEO esperto per aziende e PMI | Danova Tech",                    # esperto seo 500, consulente seo 5k
 'app-rapportini-di-lavoro': "App rapportini giornalieri di lavoro e cantiere | Danova Tech",  # rapportini giornalieri 500
 'app-magazzino-codici-a-barre': "App gestione magazzino con codici a barre | Danova Tech",      # app gestione magazzino 500
 'software-gestionale-aziendale': "Software gestionale aziendale su misura per PMI | Danova Tech",  # software gestionale 5k, gestionale aziendale 5k
 'servizi/siti-web-ecommerce': "Web agency: realizzazione siti web ed e-commerce | Danova Tech",  # web agency 5k, agenzia web 5k, realizzazione siti web 5k
 # DE
 'de/leistungen/software-automatisierung': "Softwareentwicklung, Automatisierung und KI | Danova Tech",  # softwareentwicklung 50k
 'de/leistungen/websites-ecommerce': "Website und Onlineshop erstellen lassen | Danova Tech",    # website erstellen lassen 5k, onlineshop erstellen 5k
 'de/leistungen/warenwirtschaft-crm': "Warenwirtschaftssystem und CRM nach Maß | Danova Tech",  # warenwirtschaftssystem 5k
 'de/leistungen/seo': "SEO-Agentur: SEO-Optimierung und Beratung | Danova Tech",                # seo optimierung 50k, seo agentur 5k, seo beratung 5k
 'de/werbevideos-erstellen-lassen': "Werbevideo und Imagefilm erstellen lassen, in 24 h | Danova Tech",  # imagefilm 5k
 # FR / ES
 'fr/services/logiciels-automatisation': "Développement logiciel sur mesure et IA | Danova Tech",  # developpement logiciel 5k
 'es/servicios/software-automatizacion': "Desarrollo de software a medida e IA | Danova Tech",    # desarrollo de software 5k
 'es/servicios/erp-crm': "ERP y CRM a medida para pymes | Danova Tech",                          # erp para pymes 500
}
if __name__ == '__main__':
    for rel, new in T.items():
        assert len(new) <= 65, (rel, len(new))
        p = os.path.join(ROOT, rel, 'index.html'); s = open(p, encoding='utf-8').read()
        old = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
        if old == new: print('gia ok', rel); continue
        e = html.escape(new, quote=True)
        s = re.sub(r'<title>.*?</title>', lambda _: f'<title>{e}</title>', s, 1, flags=re.S)
        for k in ('og:title', 'twitter:title'):
            s = re.sub(rf'(<meta (?:property|name)="{k}" content=")[^"]*"', lambda m: m.group(1) + e + '"', s)
        s = s.replace('"name": "%s"' % old.replace('"', '\\"'), '"name": "%s"' % new.replace('"', '\\"'))
        open(p, 'w', encoding='utf-8').write(s); print(rel, '|', old, '->', new, len(new))
