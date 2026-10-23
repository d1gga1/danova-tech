# -*- coding: utf-8 -*-
"""23/10/2026 - Collegamenti interni verso le pagine nuove (sito in 24 ore, video pubblicitari,
   app per ogni attivita', gestionale per ogni settore). Idempotente.
   1) footer di tutte le pagine IT/EN/DE/FR/ES (colonna Servizi)
   2) homepage IT: 4 schede in testa a "Approfondimenti"
   3) box "Approfondisci"/"Pagine collegate" (.pg-altri) delle pagine IT affini per argomento
   Uso: python3 seo-tools/link-2026-10-23.py"""
import os, re, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FOOT = {
 'it': [('Sito web in 24 ore', '/sito-web-in-24-ore/'), ('Video pubblicitari', '/video-pubblicitari/'),
        ('App per ogni attività', '/app-su-misura-per-ogni-attivita/'), ('Gestionale per ogni settore', '/gestionale-su-misura-per-ogni-settore/')],
 'en': [('Website in 24 hours', '/en/website-in-24-hours/'), ('Promotional videos', '/en/promotional-video-production/'), ('Apps for every business', '/en/custom-apps-for-every-business/')],
 'de': [('Website in 24 Stunden', '/de/website-in-24-stunden/'), ('Werbevideos', '/de/werbevideos-erstellen-lassen/'), ('Individuelle App-Entwicklung', '/de/individuelle-app-entwicklung/')],
 'fr': [('Site internet en 24 heures', '/fr/site-internet-en-24-heures/'), ('Vidéos publicitaires', '/fr/creation-video-publicitaire/'), ('Application sur mesure', '/fr/application-sur-mesure/')],
 'es': [('Web en 24 horas', '/es/pagina-web-en-24-horas/'), ('Vídeos publicitarios', '/es/videos-publicitarios/'), ('Aplicaciones a medida', '/es/aplicaciones-a-medida/')],
}
H5 = {'it': 'Servizi', 'en': 'Services', 'de': 'Leistungen', 'fr': 'Services', 'es': 'Servicios'}
ARGOMENTI = [  # (regex sul percorso, testo, href)
 (r'^(realizzazione-siti|sito-|siti-web-|quanto-costa-un-sito|realizzazione-landing|restyling|prezzi|servizi/siti-web|web-agency|aprire-un-negozio)', 'Sito web in 24 ore', '/sito-web-in-24-ore/'),
 (r'^(app-|sviluppo-web-app|sviluppo-app|servizi/app-su-misura|quanto-costa-una-app|whatsapp-aziendale|chatbot-aziendale)', 'App su misura per ogni attività', '/app-su-misura-per-ogni-attivita/'),
 (r'^(gestionale|software-|gestionali-su-misura|servizi/gestionali|quanto-costa-un-gestionale|crm-aziendale|erp-|dashboard-aziendale|ecommerce-collegato|software-house|sviluppo-software)', 'Gestionale su misura per ogni settore', '/gestionale-su-misura-per-ogni-settore/'),
 (r'^(servizi/meta-ads|servizi/google-ads|marketing-per-pmi|lead-generation|ledwall|realizzazione-ecommerce|seo-per-ecommerce|quanto-costa-google-ads|grafica-per-stand|stand-fieristici/|intelligenza-artificiale-per-aziende|consulenza-intelligenza)', 'Video pubblicitari', '/video-pubblicitari/'),
]
NUOVE = {'sito-web-in-24-ore', 'video-pubblicitari', 'app-su-misura-per-ogni-attivita', 'gestionale-su-misura-per-ogni-settore'}
ICON = '<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
GO = '<span class="go">Vedi la pagina <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span>'
HOME = [('/sito-web-in-24-ore/', 'Sito web in 24 ore', 'Online domani a 350 €, anche nel weekend e senza materiale. In ritardo? Non paghi.', '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path>'),
        ('/video-pubblicitari/', 'Video pubblicitari', 'Spot con AI, motion design 3D e reel per Instagram e TikTok, pronti in 24 ore.', '<rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="M10 9l5 3-5 3z"></path>'),
        ('/app-su-misura-per-ogni-attivita/', 'App per ogni attività', 'Prenotazioni, ordini, cantieri, magazzino: la vostra app, con demo in 48-72 ore.', '<rect x="7" y="2" width="10" height="20" rx="2"></rect><path d="M11 18h2"></path>'),
        ('/gestionale-su-misura-per-ogni-settore/', 'Gestionale per ogni settore', 'Il gestionale costruito sul vostro lavoro, da 1.500 € e senza canone obbligatorio.', '<path d="M3 3h18v4H3zM3 10h18v4H3zM3 17h18v4H3z"></path>')]

def lang_of(rel):
    p = rel.split('/')[0]
    return p if p in ('en', 'de', 'fr', 'es') else ('it' if p not in ('zh', 'zh-hant', 'ar', 'tr') else None)

nf = nh = na = 0
for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
    rel = os.path.relpath(f, R).replace('\\', '/')
    if rel.startswith(('_to_delete/', 'seo-tools/', 'social/', 'assets/')): continue
    lang = lang_of(rel)
    if not lang: continue
    s = open(f, encoding='utf-8').read(); s0 = s
    # 1) footer
    m = re.search(r'(<footer.*?<h5>%s</h5><ul>)(.*?)(</ul>)' % re.escape(H5[lang]), s, re.S)
    if m and FOOT[lang][0][1] not in m.group(2):
        add = ''.join('\n          <li><a href="%s">%s</a></li>' % (h, t) for t, h in FOOT[lang])
        s = s[:m.end(1)] + add + m.group(2) + s[m.end(2):]
        nf += 1
    # 2) homepage
    if rel == 'index.html' and 'href="/sito-web-in-24-ore/" data-rv' not in s:
        cards = ''.join('\n        <a class="sect sect-zone" href="%s" data-rv="up" data-tilt><div class="ic">%s</div> <h4>%s</h4><p>%s</p> %s </a>'
                        % (h, ICON % ic, t, p, GO) for h, t, p, ic in HOME)
        s, k = re.subn(r'(<section id="approf">.*?<div class="sect-grid">)', lambda mm: mm.group(1) + cards, s, count=1, flags=re.S)
        nh += k
    # 3) box Approfondisci delle pagine IT affini
    if lang == 'it':
        d = rel[:-len('index.html')]
        if d.strip('/') not in NUOVE:
            for rx, t, h in ARGOMENTI:
                box = re.search(r'<div class="pg-altri"[^>]*>(.*?)</div>', s, re.S)
                if re.match(rx, d) and box and ('href="%s"' % h) not in box.group(1):
                    s, k = re.subn(r'(<div class="pg-altri"[^>]*>)', lambda mm: mm.group(1) + '<a href="%s">%s</a>\n      ' % (h, t), s, count=1)
                    na += k
    if s != s0:
        open(f, 'w', encoding='utf-8').write(s)
# 4) link "Domande frequenti" nel footer IT, dopo "Gestionale per ogni settore"
FAQ_LI = '\n          <li><a href="/domande-frequenti/">Domande frequenti</a></li>'
nq = 0
for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
    rel = os.path.relpath(f, R).replace('\\', '/')
    if rel.startswith(('_archivio/', 'seo-tools/', 'social/', 'assets/')) or lang_of(rel) != 'it': continue
    s2 = open(f, encoding='utf-8').read()
    a = '<li><a href="/gestionale-su-misura-per-ogni-settore/">Gestionale per ogni settore</a></li>'
    if a in s2 and 'href="/domande-frequenti/">Domande frequenti</a></li>' not in s2:
        open(f, 'w', encoding='utf-8').write(s2.replace(a, a + FAQ_LI, 1)); nq += 1
print('footer FAQ: %d' % nq)
print('footer: %d | homepage: %d | box approfondisci: %d' % (nf, nh, na))
