"""
Ottimizzazioni dalla lista "Le 100 discipline della visibilita' online" (8/11/2026).
Idempotente: si puo' rilanciare dopo ogni build.

1. AEO / VSO / GEO (punti 3, 16, 33, 81): "speakable" su ogni pagina reale
   (titolo + paragrafo di apertura o box "In breve"). Le pagine senza nodo
   WebPage ricevono un WebPage completo con dateModified (dalla data git).
2. Semantic / Entity SEO (32, 49, 63): knowsAbout dell'organizzazione con le
   entita' collegate a Wikipedia, invece di 5 parole generiche.
3. E-E-A-T e content refresh (7, 83): data di aggiornamento visibile e
   responsabile del contenuto in testa a guide e articoli.
4. Accessibilita' / AI Agent Optimization (13, 75): nome accessibile al pulsante
   del modale legali (vuoto nell'HTML statico).
5. SEO on-page (9): meta description troppo lunghe accorciate.
"""
import os, re, json, subprocess, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SKIP = {'.git', '_to_delete', '_archivio', 'seo-tools', 'assets', 'social', 'node_modules'}
BASE = 'https://danova-tech.com'

WP = 'https://en.wikipedia.org/wiki/'
KNOWS = [
    ('Web design', 'Web_design'), ('Web development', 'Web_development'),
    ('E-commerce', 'E-commerce'), ('Search engine optimization', 'Search_engine_optimization'),
    ('Local search engine optimisation', 'Local_search_engine_optimisation'),
    ('Generative engine optimization', 'Generative_engine_optimization'),
    ('Search engine marketing', 'Search_engine_marketing'), ('Google Ads', 'Google_Ads'),
    ('Social media marketing', 'Social_media_marketing'), ('Digital marketing', 'Digital_marketing'),
    ('Custom software', 'Custom_software'), ('Enterprise resource planning', 'Enterprise_resource_planning'),
    ('Customer relationship management', 'Customer_relationship_management'),
    ('Mobile app development', 'Mobile_app_development'), ('Web application', 'Web_application'),
    ('Artificial intelligence', 'Artificial_intelligence'), ('Intelligent agent', 'Intelligent_agent'),
    ('Chatbot', 'Chatbot'), ('Robotic process automation', 'Robotic_process_automation'),
    ('Business process automation', 'Business_process_automation'),
    ('Web accessibility', 'Web_accessibility'), ('Video production', 'Video_production'),
]
KNOWS_LD = [{'@type': 'Thing', 'name': n, 'sameAs': WP + s} for n, s in KNOWS]

DESC = {  # meta description > 170 caratteri reali
    'agenzia-seo-milano/index.html': "Agenzia SEO per aziende di Milano e provincia, con ufficio a Vermezzo con Zelo (MI): audit tecnico, contenuti, SEO locale e report mensili chiari. Nessun vincolo.",
    'tr/index.html': "Danova Tech, Treviso merkezli İtalyan yazılım ve web ajansı: İtalyanca web siteleri, e-ticaret, özel yazılım, yapay zekâ ve İtalya pazarı için SEO. 24 saatte teklif.",
    'de/individuelle-app-entwicklung/index.html': "Individuelle Apps für jedes Unternehmen: Buchungen, Bestellungen, Kundenbindung, Baustellen, Lager. iOS, Android und Web, funktionierende Demo in 48–72 Stunden.",
    'fr/application-sur-mesure/index.html': "Applications sur mesure pour toute activité : réservations, commandes, fidélité, chantiers, stock, commerciaux. iOS, Android et web, démo en 48 à 72 heures.",
    'realizzazione-landing-page/index.html': "Landing page per Google Ads e Meta Ads: una pagina, un'offerta, un'azione. Veloci, misurate e collegate al CRM. Prezzo fisso dopo la prima call.",
}
MESI = {
 'it': 'gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre',
 'en': 'January February March April May June July August September October November December',
 'de': 'Januar Februar März April Mai Juni Juli August September Oktober November Dezember',
 'fr': 'janvier février mars avril mai juin juillet août septembre octobre novembre décembre',
 'es': 'enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre',
}
UPD = {  # testo, link "chi siamo"
 'it': ('Aggiornata il {d} · a cura del team Danova Tech', '/chi-siamo/', 'Chi siamo'),
 'en': ('Updated {d} · written by the Danova Tech team', '/en/about/', 'About us'),
 'de': ('Aktualisiert am {d} · vom Team von Danova Tech', '/de/ueber-uns/', 'Über uns'),
 'fr': ('Mis à jour le {d} · par l’équipe Danova Tech', '/fr/a-propos/', 'À propos'),
 'es': ('Actualizado el {d} · por el equipo de Danova Tech', '/es/sobre-nosotros/', 'Quiénes somos'),
}
DONE = {'it': 'Ho capito', 'en': 'Got it', 'de': 'Verstanden', 'fr': 'Compris', 'es': 'Entendido',
        'zh': 'Got it', 'ar': 'Got it', 'tr': 'Got it'}

def fdate(iso, lang):
    y, m, d = iso[:10].split('-')
    mm = MESI[lang].split()[int(m) - 1]
    if lang == 'en': return f'{mm} {int(d)}, {y}'
    if lang == 'de': return f'{int(d)}. {mm} {y}'
    return f'{int(d)} {mm} {y}'

def gitdate(p):
    try:
        out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', p], capture_output=True, text=True).stdout.strip()
        return out or datetime.date.today().isoformat()
    except Exception:
        return datetime.date.today().isoformat()

def types(n):
    t = n.get('@type', [])
    return t if isinstance(t, list) else [t]

PAGE_T = {'WebPage', 'AboutPage', 'ContactPage', 'CollectionPage', 'FAQPage_x', 'ItemPage'}
stats = dict(pagine=0, speak=0, webpage_nuovo=0, knows=0, data_visibile=0, bottone=0, desc=0)
about_exists = {l: os.path.exists(v[1].strip('/') + '/index.html') for l, v in UPD.items()}

for d, ds, fs in os.walk('.'):
    ds[:] = [x for x in ds if x not in SKIP]
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.normpath(os.path.join(d, f))
        h = open(p, encoding='utf-8').read()
        if re.search(r'http-equiv=["\']refresh', h[:4000], re.I) or '<h1' not in h: continue
        if p == '404.html': continue
        orig = h; stats['pagine'] += 1
        lang = (re.search(r'<html[^>]*lang="([a-zA-Z]+)', h) or [None, 'it'])[1].lower()[:2]
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', h)
        url = canon.group(1) if canon else BASE + '/' + p.replace('index.html', '')
        title = re.search(r'<title>(.*?)</title>', h, re.S).group(1).strip()
        # selettori speakable
        if 'class="pg-breve' in h: sel = ['h1', '.pg-breve p']
        elif 'class="lead' in h: sel = ['h1', '.pg-hero .lead']
        elif 'class="hero-sub' in h: sel = ['h1', '.hero-sub']
        else: sel = ['h1']
        speak = {'@type': 'SpeakableSpecification', 'cssSelector': sel}

        def fix_ld(m):
            raw = m.group(2)
            try: j = json.loads(raw)
            except Exception: return m.group(0)
            graph = j['@graph'] if isinstance(j, dict) and '@graph' in j else None
            nodes = graph if graph is not None else [j]
            ch = False
            for n in nodes:
                if not isinstance(n, dict): continue
                if n.get('@id') == BASE + '/#organization':
                    ka = n.get('knowsAbout') or []
                    if isinstance(ka, str): ka = [ka]
                    if not any(isinstance(x, dict) and str(x.get('sameAs', '')).startswith(WP) for x in ka):
                        n['knowsAbout'] = KNOWS_LD + ka; ch = True; stats['knows'] += 1
                if set(types(n)) & PAGE_T:
                    if 'speakable' not in n:
                        n['speakable'] = speak; ch = True; stats['speak'] += 1
            has_page = any(isinstance(n, dict) and set(types(n)) & PAGE_T for n in nodes)
            if graph is not None and not has_page and '"#webpage"' not in raw and url + '#webpage' not in raw:
                graph.append({
                    '@type': 'WebPage', '@id': url + '#webpage', 'url': url,
                    'name': re.sub(r'&amp;', '&', title), 'inLanguage': lang,
                    'isPartOf': {'@id': BASE + '/#website'}, 'about': {'@id': BASE + '/#organization'},
                    'publisher': {'@id': BASE + '/#organization'},
                    'dateModified': gitdate(p), 'speakable': speak})
                ch = True; stats['webpage_nuovo'] += 1; stats['speak'] += 1
            if not ch: return m.group(0)
            return m.group(1) + '\n' + json.dumps(j, ensure_ascii=False, indent=2).replace('</', '<\\/') + '\n' + m.group(3)
        h = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', fix_ld, h, flags=re.S)

        # data di aggiornamento visibile su guide e articoli
        if '"BlogPosting"' in h or re.search(r'"@type":\s*\[?\s*"Article"', h):
            if 'class="pg-upd' not in h and lang in UPD:
                dm = re.search(r'"dateModified":\s*"([0-9-]{10})', h)
                if dm:
                    txt, ab, abn = UPD[lang]
                    link = f' · <a href="{ab}" style="color:inherit;text-decoration:underline">{abn}</a>' if about_exists[lang] else ''
                    tag = (f'<p class="pg-upd mono" style="margin-top:16px;font-size:12.5px;letter-spacing:.03em;color:var(--muted-2)">'
                           f'<time datetime="{dm.group(1)}">{txt.format(d=fdate(dm.group(1), lang))}</time>{link}</p>')
                    h2 = re.sub(r'(<section class="pg-hero">.*?<p class="lead"[^>]*>.*?</p>)', lambda m: m.group(1) + '\n' + tag, h, count=1, flags=re.S)
                    if h2 != h: h = h2; stats['data_visibile'] += 1

        # pulsante modale legali senza nome
        if '<button class="lgl-done" id="lglDone"></button>' in h:
            h = h.replace('<button class="lgl-done" id="lglDone"></button>',
                          f'<button class="lgl-done" id="lglDone" type="button">{DONE.get(lang, "OK")}</button>')
            stats['bottone'] += 1

        # meta description
        key = p.replace(os.sep, '/')
        if key in DESC:
            new = DESC[key].replace("'", '&#x27;')
            h2 = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + new + m.group(2), h, count=1)
            h2 = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + new + m.group(2), h2, count=1)
            h2 = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', lambda m: m.group(1) + new + m.group(2), h2, count=1)
            if h2 != h: h = h2; stats['desc'] += 1

        if h != orig:
            open(p, 'w', encoding='utf-8').write(h)
print(stats)
