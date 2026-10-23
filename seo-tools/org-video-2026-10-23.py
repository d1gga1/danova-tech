# -*- coding: utf-8 -*-
"""23/10/2026 - Nodo #organization di ogni pagina (IT/EN/DE/FR/ES): aggiunge video pubblicitari e sito in 24 ore
   a knowsAbout, hasOfferCatalog e descrizione. Serve a Google e agli assistenti AI per associare questi servizi a Danova Tech.
   Idempotente. Uso: python3 seo-tools/org-video-2026-10-23.py"""
import os, re, json, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); os.chdir(R)
OID = 'https://danova-tech.com/#organization'
RX = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
KA = ['Video pubblicitari', 'Motion design', 'Video con intelligenza artificiale', 'Promotional video production', 'Sito web in 24 ore']
TX = {
 'it': ('Video pubblicitari', 'Spot con intelligenza artificiale, motion design 3D e reel per Instagram e TikTok, pronti in 24 ore.', '/video-pubblicitari/',
        'Sito web in 24 ore', 'Sito vetrina fino a 5 pagine online in 24 ore, 7 giorni su 7, a 350 € IVA inclusa: testi e immagini inclusi.', '/sito-web-in-24-ore/',
        ' Realizza inoltre video pubblicitari con intelligenza artificiale e motion design, e siti web pronti in 24 ore.'),
 'en': ('Promotional videos', 'AI commercials, 3D motion design and Instagram/TikTok reels, ready in 24 hours.', '/en/promotional-video-production/',
        'Website in 24 hours', 'Brochure website of up to 5 pages live within 24 hours, 7 days a week, for €350 incl. VAT, copy and images included.', '/en/website-in-24-hours/',
        ' It also produces AI and motion-design promotional videos and websites ready in 24 hours.'),
 'de': ('Werbevideos', 'KI-Werbespots, 3D-Motion-Design und Reels für Instagram und TikTok, fertig in 24 Stunden.', '/de/werbevideos-erstellen-lassen/',
        'Website in 24 Stunden', 'Website mit bis zu 5 Seiten, online in 24 Stunden, 7 Tage die Woche, für 350 € inkl. MwSt., Texte und Bilder inklusive.', '/de/website-in-24-stunden/',
        ' Außerdem produziert sie Werbevideos mit KI und Motion Design sowie Websites in 24 Stunden.'),
 'fr': ('Vidéos publicitaires', 'Spots IA, motion design 3D et reels Instagram et TikTok, prêts en 24 heures.', '/fr/creation-video-publicitaire/',
        'Site internet en 24 heures', 'Site vitrine jusqu’à 5 pages en ligne en 24 heures, 7 jours sur 7, pour 350 € TTC, textes et images inclus.', '/fr/site-internet-en-24-heures/',
        ' Elle réalise aussi des vidéos publicitaires en IA et motion design, et des sites internet prêts en 24 heures.'),
 'es': ('Vídeos publicitarios', 'Spots con IA, motion design 3D y reels para Instagram y TikTok, listos en 24 horas.', '/es/videos-publicitarios/',
        'Página web en 24 horas', 'Web de hasta 5 páginas online en 24 horas, 7 días a la semana, por 350 € IVA incluido, textos e imágenes incluidos.', '/es/pagina-web-en-24-horas/',
        ' También produce vídeos publicitarios con IA y motion design, y páginas web listas en 24 horas.'),
}
def offer(nome, desc, url):
    return {"@type": "Offer", "itemOffered": {"@type": "Service", "name": nome, "description": desc, "url": "https://danova-tech.com" + url,
            "provider": {"@id": OID}, "areaServed": [{"@type": "Country", "name": "Italia"}, {"@type": "Place", "name": "Europa"}]}}
n = 0
for p in glob.glob('**/index.html', recursive=True):
    if p.startswith(('seo-tools', '_to_delete', 'social', 'assets')): continue
    top = p.split('/')[0] if '/' in p else ''
    if top in ('zh', 'zh-hant', 'ar', 'tr'): continue
    lang = top if top in TX else 'it'
    t = TX[lang]; h = open(p, encoding='utf-8').read(); h0 = h
    def fix(m):
        try: g = json.loads(m.group(2))
        except Exception: return m.group(0)
        ch = False
        for node in g.get('@graph', []) if isinstance(g, dict) else []:
            if node.get('@id') != OID: continue
            ka = node.setdefault('knowsAbout', [])
            for k in KA:
                if k not in ka: ka.append(k); ch = True
            oc = node.get('hasOfferCatalog')
            if oc and isinstance(oc.get('itemListElement'), list):
                names = [o.get('itemOffered', {}).get('name') for o in oc['itemListElement']]
                if t[0] not in names: oc['itemListElement'].append(offer(t[0], t[1], t[2])); ch = True
                if t[3] not in names: oc['itemListElement'].append(offer(t[3], t[4], t[5])); ch = True
            if node.get('description') and t[6].strip() not in node['description']:
                node['description'] = node['description'].rstrip() + t[6]; ch = True
        if not ch: return m.group(0)
        return m.group(1) + '\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n' + m.group(3)
    h = RX.sub(fix, h)
    if h != h0: open(p, 'w', encoding='utf-8').write(h); n += 1
print('pagine aggiornate:', n)
