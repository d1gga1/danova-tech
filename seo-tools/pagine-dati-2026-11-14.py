# -*- coding: utf-8 -*-
"""14/11/2026 - Dati delle 32 pagine nuove scelte sui CSV del Keyword Planner del 14/11
   (Downloads/PAROLE_DANOVA_TECH, 42 file, 42.048 righe). Build: seo-tools/pagine-build-2026-11-14.py.
   Raccoglie i file pagine-dati-2026-11-14-{it-ai,it-web,it-gest,estero-1,estero-2}.py e accorcia
   le meta description sotto i 160 caratteri."""
import os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(fn):
    s = importlib.util.spec_from_file_location(fn.replace('-', '_'), os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
OGGI = "2026-11-14"
PAGINE = []
for fn in ('pagine-dati-2026-11-14-it-ai.py', 'pagine-dati-2026-11-14-it-web.py', 'pagine-dati-2026-11-14-it-gest.py',
           'pagine-dati-2026-11-14-estero-1.py', 'pagine-dati-2026-11-14-estero-2.py'):
    PAGINE += _load(fn).PAGINE

DESC = {
 '/centralino-ai/': "Centralino AI che risponde al telefono anche di notte: prende appuntamenti, smista le chiamate e scrive tutto nel CRM. Segretaria virtuale AI su misura.",
 '/chatgpt-per-aziende/': "ChatGPT aziendale fatto bene: piano giusto, regole d’uso, assistente sui vostri documenti e integrazione nel gestionale. Per PMI italiane.",
 '/intelligenza-artificiale-per-commercialisti/': "AI per lo studio del commercialista: raccolta documenti, lettura di fatture, risposte dalle circolari e bozze di lettere, nel rispetto della legge 132/2025.",
 '/intelligenza-artificiale-per-medici/': "AI per lo studio medico contro la burocrazia: centralino che prenota, promemoria, moduli online, riepilogo delle note. Nessuna diagnosi, dati protetti.",
 '/sito-web-accessibile/': "Rendiamo il sito accessibile secondo WCAG 2.1 AA ed European Accessibility Act: verifica, correzioni nel codice e dichiarazione di accessibilità.",
 '/audit-seo/': "Audit SEO completo: SEO tecnica, contenuti, link, SEO locale e visibilità su Google AI Mode e ChatGPT. Problemi in ordine di impatto, prezzo fisso.",
 '/guide/google-ai-mode/': "Cosa sono Google AI Mode e AI Overview, quando sono arrivati in Italia, come scelgono le fonti e cosa fare perché il vostro sito venga citato.",
 '/ecommerce-vino/': "E-commerce per cantine e produttori alimentari: verifica dell’età, spedizioni, accise per l’estero, listini Horeca e collegamento al gestionale.",
 '/tiktok-ads/': "Campagne TikTok Ads con video pensati per TikTok: pixel ed eventi configurati, Spark Ads, test delle creatività e costo per contatto misurato.",
 '/bandi-digitalizzazione-2026/': "Bandi e voucher digitalizzazione 2026 per PMI: Voucher Doppia Transizione delle Camere di Commercio, bandi regionali, iperammortamento.",
 '/gestionale-presenze-turni/': "Gestionale presenze su misura: timbrature da app, turni in pochi clic, ferie e permessi online, export per il consulente del lavoro. Da 1.500 €.",
 '/software-haccp/': "Software HACCP su misura: temperature, pulizie e controlli da tablet, sensori collegati, avvisi sulle anomalie e tracciabilità dei lotti.",
 '/software-sicurezza-lavoro/': "Software sicurezza sul lavoro su misura: scadenze di corsi e visite mediche, DPI, attrezzature e documenti con avvisi automatici. D.Lgs. 81/2008.",
 '/gestionale-case-vacanza/': "Gestionale case vacanza e affittacamere: calendario unico con Booking e Airbnb o channel manager, check-in online, Alloggiati Web, pulizie.",
 '/gestionale-fisioterapista/': "Gestionale per fisioterapisti: agenda e cicli di sedute, prenotazioni online, scheda paziente, fatture sanitarie e invio al Sistema Tessera Sanitaria.",
 '/gestionale-stabilimento-balneare/': "Gestionale per stabilimenti balneari: mappa della spiaggia, prenotazione online di ombrelloni, abbonamenti stagionali, cassa e bar collegati.",
 '/en/ai-receptionist/': "A custom AI receptionist that answers your business phone 24/7, books appointments, routes calls and logs every call in your CRM. EU data.",
 '/en/whatsapp-chatbot/': "WhatsApp chatbot on the official WhatsApp Business Platform: answers, bookings, order status and leads, linked to your CRM, with human handover.",
 '/en/generative-engine-optimization/': "GEO services to get your company cited by ChatGPT, Google AI Mode, Perplexity and Copilot: content, structured data and monthly AI visibility checks.",
 '/de/ki-telefonassistent/': "KI-Telefonassistent, der Anrufe rund um die Uhr annimmt, Termine vergibt, weiterleitet und jedes Gespräch im CRM festhält. Individuell, Daten in der EU.",
 '/de/ki-agentur/': "KI-Agentur und Softwarehaus: KI-Agenten für KMU, die E-Mails lesen, Warenwirtschaft und CRM pflegen und vor wichtigen Schritten um Freigabe bitten.",
 '/de/barrierefreie-website/': "Website und Onlineshop barrierefrei nach WCAG 2.1 AA, BFSG und BaFG: Prüfung, Korrekturen im Code, Erklärung zur Barrierefreiheit.",
 '/de/generative-engine-optimization/': "Generative Engine Optimization: damit ChatGPT, Google AI Mode, Perplexity und Copilot Ihr Unternehmen verstehen und zitieren.",
 '/fr/standard-telephonique-ia/': "Standard téléphonique IA sur mesure : répond 24 h/24, prend les rendez-vous, oriente les appels et note chaque appel dans votre CRM.",
 '/fr/agence-ia/': "Agence IA : agents IA pour PME qui lisent e-mails et documents, mettent à jour ERP et CRM et demandent validation avant d’agir.",
 '/fr/agence-shopify/': "Agence Shopify : boutiques rapides, thèmes sur mesure, migration sans perte SEO et connexion à l’ERP et au stock. Dès 2 990 €.",
 '/es/agentes-de-ia/': "Agentes de IA a medida para pymes: leen correos y documentos, actualizan ERP y CRM, preparan presupuestos y piden aprobación antes de actuar.",
}
for d in PAGINE:
    if d['url'] in DESC:
        if d['ogdesc'] == d['desc']: d['ogdesc'] = DESC[d['url']]
        d['desc'] = DESC[d['url']]
if __name__ == '__main__':
    for d in PAGINE:
        print('%3d %3d %-3s %s' % (len(d['title']), len(d['desc']), d['lang'], d['url']))
    print(len(PAGINE), 'pagine')
