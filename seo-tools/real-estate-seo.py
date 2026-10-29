# -*- coding: utf-8 -*-
"""24/10/2026 - Rifiniture SEO della sezione Danova Real Estate (tutte le lingue). Idempotente.
   1) meta description entro ~158 caratteri (Google taglia oltre): si tolgono frasi o l'ultimo elemento di un elenco,
      chiudendo l'elenco con la congiunzione della lingua ("e", "and", "und", "și", "dhe"). og/twitter restano complete.
   2) blocco "Dove lavoriamo" (tra <!--re-zone--> e <!--/re-zone-->) con tutte le pagine di citta' e localita' nella lingua
      della pagina: pagina principale, pagine hub e pagine di zona. Nessuna pagina di zona resta senza link interni.
   3) titoli: pagina principale con il marchio in testa; pagine citta' italiane su "Impresa edile <citta'> | Ristrutturazioni chiavi in mano" (dal 26/10/2026).
   4) dati strutturati: le guide sono Article (non Service); GeneralContractor con mappa e profili social.
   Lanciare dopo real-estate-chrome.py e prima di genera-sitemap.py (gia' nella catena di real-estate-tutto.sh).
   Uso: python3 seo-tools/real-estate-seo.py"""
import os, re, glob, json, html, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(HERE)
SITE = 'https://danova-tech.com'
_s = importlib.util.spec_from_file_location('relg', os.path.join(HERE, 'real-estate-lingue.py')); LG = importlib.util.module_from_spec(_s); _s.loader.exec_module(LG)
L5 = ['it', 'en', 'de', 'ro', 'sq']
def T(*v): return dict(zip(L5, v))
INV = {}
for k in LG.S:
    for l in L5:
        INV[LG.url(k, l)] = (k, l)

# ---------------------------------------------------------------- 1) description
CONG = T('e', 'and', 'und', 'și', 'dhe')
MAXD = 158

def accorcia_elenco(frase, l):
    """'a, b, c e d.' -> 'a, b e c.' (toglie l'ultimo elemento e richiude l'elenco)"""
    corpo = frase.rstrip().rstrip('.').rstrip('।'); fine = '।' if l == 'hi' else '.'
    parti = corpo.split(', ')
    if len(parti) < 2:
        return None
    ultimo = parti[-1]
    m = re.match(r'^(.*?)\s+(?:e|ed|and|und|sowie|și|dhe|और)\s+\S.*$', ultimo)
    if m and len(m.group(1)) > 2:
        parti[-1] = m.group(1)
    else:
        parti = parti[:-1]
    if len(parti) == 1:
        return parti[0] + fine
    return ', '.join(parti[:-1]) + ' ' + CONG[l] + ' ' + parti[-1] + fine

def corta(d, l):
    if len(d) <= MAXD:
        return d
    frasi = re.split(r'(?<=[.!?।])\s+', d.strip())
    out = ''
    for f in frasi:
        c = (out + ' ' + f).strip()
        if len(c) <= MAXD:
            out = c
            continue
        g = f
        for _ in range(6):
            g = accorcia_elenco(g, l)
            if not g:
                break
            c = (out + ' ' + g).strip()
            if len(c) <= MAXD and len(g) > 30:
                out = c
                break
        break
    if len(out) >= 100:
        return out
    if len(d) > 160:  # 26/10: ultima risorsa, si taglia all'ultima frase o virgola entro il limite
        cut = d[:MAXD]
        for sep in ('. ', '। ', ': ', ', '):
            i = cut.rfind(sep)
            if i >= 90:
                return cut[:i].rstrip(',:') + ('।' if l == 'hi' else '.')
    return d

# ---------------------------------------------------------------- 2) dove lavoriamo
NOMI = {'treviso': 'Treviso', 'oderzo': 'Oderzo', 'conegliano': 'Conegliano', 'motta-di-livenza': 'Motta di Livenza', 'castelfranco-veneto': 'Castelfranco Veneto',
        'montebelluna': 'Montebelluna', 'venezia': 'Venezia', 'mestre': 'Mestre', 'san-dona-di-piave': 'San Donà di Piave', 'portogruaro': 'Portogruaro',
        'padova': 'Padova', 'vicenza': 'Vicenza', 'verona': 'Verona', 'pordenone': 'Pordenone', 'udine': 'Udine', 'sacile': 'Sacile',
        'jesolo': 'Jesolo', 'caorle': 'Caorle', 'bibione': 'Bibione', 'cavallino-treporti': 'Cavallino-Treporti', 'sottomarina': 'Sottomarina e Chioggia',
        'lignano': 'Lignano Sabbiadoro', 'grado': 'Grado', 'cortina': 'Cortina d’Ampezzo', 'dolomiti': 'Dolomiti bellunesi', 'lago-di-garda': 'Lago di Garda'}
# 26/10/2026: nuove citta (real-estate-citta-nuove.py)
NOMI.update({c[1]: c[0] for c in LG._CN.NUOVE_IT})
GRUPPI = [('/ristrutturazioni-%s/', LG.CITTA, T('Ristrutturazioni', 'Renovation', 'Renovierung', 'Renovări', 'Rinovime')),
          ('/general-contractor-%s/', LG.GC, T('General contractor', 'General contractor', 'Generalunternehmer', 'Antreprenor general', 'Kontraktor i përgjithshëm')),
          ('/arredo-hotel-%s/', LG.ZONE, T('Arredo hotel', 'Hotel furniture', 'Hotelmöbel', 'Mobilier hotelier', 'Mobilim hotelesh'))]
TIT = T('Dove lavoriamo', 'Where we work', 'Wo wir arbeiten', 'Unde lucrăm', 'Ku punojmë')
H2 = T('Veneto e Friuli Venezia Giulia, <span class="grad">città per città</span>', 'Veneto and Friuli Venezia Giulia, <span class="grad">town by town</span>',
       'Venetien und Friaul, <span class="grad">Ort für Ort</span>', 'Veneto și Friuli Venezia Giulia, <span class="grad">oraș cu oraș</span>',
       'Veneto dhe Friuli Venezia Giulia, <span class="grad">qytet pas qyteti</span>')
LEAD = T('Sopralluogo gratuito in tutte le province del Veneto e del Friuli Venezia Giulia. Ecco le zone in cui lavoriamo più spesso.',
         'Free site survey in every province of Veneto and Friuli Venezia Giulia, north-east Italy. These are the areas where we work most often.',
         'Kostenlose Besichtigung in allen Provinzen Venetiens und Friaul-Julisch Venetiens. Hier arbeiten wir am häufigsten.',
         'Inspecție gratuită în toate provinciile din Veneto și Friuli Venezia Giulia. Acestea sunt zonele în care lucrăm cel mai des.',
         'Inspektim falas në të gjitha provincat e Venetos dhe të Friuli Venezia Giulias. Këto janë zonat ku punojmë më shpesh.')
HUB = ['/real-estate/', '/ristrutturazioni-chiavi-in-mano/', '/general-contractor/', '/arredo-hotel-contract/', '/ristrutturazione-hotel/',
       '/hotel-chiavi-in-mano/', '/ristrutturazione-appartamenti-e-case/']
CSS = ('<style id="re-zone-css">.re-zone h3{font-family:Sora,sans-serif;font-size:1.02rem;margin:26px 0 12px;color:var(--text)}'
       '.re-zone h3:first-of-type{margin-top:6px}body .re-zone .pg-altri{gap:10px}body .re-zone .pg-altri>*{flex:0 0 auto}.re-zone .pg-altri a[aria-current]{border-color:var(--sage);color:var(--sage)}</style>')

def zona_blocco(l, cur):
    o = ['<!--re-zone-->\n<section id="dove-lavoriamo" class="re-zone">\n  <div class="wrap">\n    <div class="sec-head">\n'
         '      <div class="eyebrow mono">%s</div>\n      <h2 class="title" data-rv="up">%s</h2>\n      <p class="lead" data-rv="up">%s</p>\n    </div>\n' % (TIT[l], H2[l], LEAD[l])]
    for pat, slugs, tit in GRUPPI:
        o.append('    <h3>%s</h3>\n    <div class="pg-altri">\n' % tit[l])
        for c in slugs:
            u = LG.url(pat % c, l)
            o.append('      <a href="%s"%s>%s</a>\n' % (u, ' aria-current="page"' if u == cur else '', html.escape(LG.nome(NOMI[c], l))))
        o.append('    </div>\n')
    o.append('  </div>\n</section>\n<!--/re-zone-->\n')
    return ''.join(o)

def con_zona(key):
    if key in HUB:
        return True
    return any(re.fullmatch(p.replace('%s', '[a-z-]+'), key) for p, _, _ in GRUPPI)

# ---------------------------------------------------------------- 3) titoli
PILASTRO = T('Danova Real Estate: ristrutturazioni in Veneto e Friuli', 'Danova Real Estate: renovation contractor in Veneto, Italy',
             'Danova Real Estate: Renovierung in Venetien, Italien', 'Danova Real Estate: renovări și construcții în Veneto, Italia',
             'Danova Real Estate: rinovime dhe ndërtim në Veneto, Itali')

# 26/10/2026: titoli entro ~62 caratteri (Google taglia oltre) e con la keyword locale in testa
TT = {  # (modello lungo, modello corto se il lungo supera MAXT)
 'citta': {'it': ('Impresa edile %s | Ristrutturazioni chiavi in mano', 'Impresa edile %s | Ristrutturazioni'),
           'en': ('Builders in %s, Italy | Turnkey renovation', 'Builders in %s | Renovation'),
           'de': ('Bauunternehmen in %s | Renovierung schlüsselfertig', 'Bauunternehmen %s | Renovierung'),
           'ro': ('Firmă de construcții %s | Renovări la cheie', 'Firmă construcții %s | Renovări'),
           'sq': ('Kompani ndërtimi %s | Rinovime çelës në dorë', 'Kompani ndërtimi %s | Rinovime')},
 'gc':    {'it': ('General contractor %s | Unico contratto, prezzo bloccato', 'General contractor %s | Prezzo bloccato'),
           'en': ('General contractor in %s, Italy | Fixed price', 'General contractor %s | Fixed price'),
           'de': ('Generalunternehmer %s | Ein Vertrag, Festpreis', 'Generalunternehmer %s | Festpreis'),
           'ro': ('Antreprenor general %s | Un contract, preț blocat', 'Antreprenor general %s | Preț blocat'),
           'sq': ('Kontraktor i përgjithshëm %s | Çmim i bllokuar', 'Kontraktor %s | Çmim i bllokuar')},
 'hotel': {'it': ('Arredo hotel %s | Camere e spazi su misura', 'Arredo hotel %s | Su misura'),
           'en': ('Hotel furniture %s | Custom contract furniture', 'Hotel furniture %s | Made to measure'),
           'de': ('Hotelmöbel %s | Objekteinrichtung nach Maß', 'Hotelmöbel %s | Nach Maß'),
           'ro': ('Mobilier hotelier %s | Mobilier la comandă', 'Mobilier hotelier %s | La comandă'),
           'sq': ('Mobilim hoteli %s | Mobilje me porosi', 'Mobilim hoteli %s | Me porosi')}}
MAXT = 62
NOMI_GC = {c: NOMI.get(c, c.title()) for c in LG.GC}
def _tm(tipo, l, nome):
    lungo, corto = TT[tipo][l]
    t = lungo % nome
    return t if len(t) <= MAXT else corto % nome
def titolo(key, l, t):
    if key == '/real-estate/':
        return PILASTRO[l]
    for tipo, rx in (('citta', r'/ristrutturazioni-([a-z-]+)/'), ('gc', r'/general-contractor-([a-z-]+)/'), ('hotel', r'/arredo-hotel-([a-z-]+)/')):
        m = re.fullmatch(rx, key)
        if m and m.group(1) in NOMI:
            return _tm(tipo, l, LG.nome(NOMI[m.group(1)], l))
    # altre pagine: se troppo lungo, si toglie l'ultimo segmento dopo " | " (se resta un titolo di almeno 35 caratteri)
    if len(t) > 65 and ' | ' in t:
        testa = t.rsplit(' | ', 1)[0]
        if len(testa) >= 35:
            return testa
    return t

# ---------------------------------------------------------------- 4) schema
PROVINCE = [(p, 'Veneto') for p in ('Treviso', 'Venezia', 'Padova', 'Vicenza', 'Verona', 'Rovigo', 'Belluno')] + \
           [(p, 'Friuli-Venezia Giulia') for p in ('Pordenone', 'Udine', 'Gorizia', 'Trieste')]
KNOWS = T(['Ristrutturazioni chiavi in mano', 'Ristrutturazione bagno', 'Impresa edile', 'General contractor', 'Cappotto termico', 'Isolamento sottotetto e insufflaggio',
           'Rifacimento tetto', 'Facciate ventilate', 'Pavimentazioni esterne', 'Cartongesso e controsoffitti', 'Porte REI tagliafuoco', 'Pavimenti e serramenti',
           'Arredo hotel e contract', 'Mobili su misura', 'Pratiche edilizie CILA e SCIA', 'Bonus ristrutturazione'],
          ['Turnkey renovation', 'Bathroom renovation', 'Building contractor', 'General contracting', 'External wall insulation', 'Loft insulation', 'Roof replacement',
           'Ventilated facades', 'Outdoor paving', 'Drywall and suspended ceilings', 'Fire-rated doors', 'Flooring and windows', 'Hotel contract furniture',
           'Custom-made furniture', 'Italian building permits (CILA, SCIA)', 'Italian renovation tax bonus'],
          ['Schlüsselfertige Renovierung', 'Badsanierung', 'Bauunternehmen', 'Generalunternehmer', 'Wärmedämmung', 'Dachbodendämmung', 'Dachsanierung', 'Fassadensanierung',
           'Terrassen und Außenbeläge', 'Trockenbau', 'Brandschutztüren', 'Böden und Fenster', 'Hotelmöbel', 'Maßmöbel', 'Baugenehmigungen in Italien', 'Renovierungsbonus Italien'],
          ['Renovări la cheie', 'Renovare baie', 'Firmă de construcții', 'Antreprenor general', 'Izolație termică exterioară', 'Izolare pod', 'Refacere acoperiș', 'Renovare fațade',
           'Pavaje exterioare', 'Rigips și tavane false', 'Uși rezistente la foc', 'Pardoseli și tâmplărie', 'Mobilier hotelier', 'Mobilă la comandă', 'Autorizații de construcție în Italia', 'Bonus renovare Italia'],
          ['Rinovime çelës në dorë', 'Rinovim banjoje', 'Kompani ndërtimi', 'Kontraktor i përgjithshëm', 'Termoizolim i jashtëm', 'Izolim papafingo', 'Rinovim çatie', 'Rinovim fasadash',
           'Shtrime të jashtme', 'Gipskarton dhe tavane të varura', 'Dyer kundër zjarrit', 'Dysheme dhe dritare', 'Mobilim hotelesh', 'Mobilje me porosi', 'Leje ndërtimi në Itali', 'Bonusi i rinovimit në Itali'])
SLOGAN = T('Sopralluogo gratuito, prezzo bloccato, tempi nel contratto, un unico referente.', 'Free survey, fixed price, deadlines in the contract, one point of contact.',
           'Kostenlose Besichtigung, Festpreis, Termine im Vertrag, ein Ansprechpartner.', 'Inspecție gratuită, preț blocat, termene în contract, un singur responsabil.',
           'Inspektim falas, çmim i bllokuar, afate në kontratë, një person kontakti.')
SOCIAL = ['https://www.instagram.com/danova_techh/', 'https://www.facebook.com/profile.php?id=61594907955699', 'https://www.tiktok.com/@danova.tech']
# 29/10/2026: hindi (hi)
L5.append('hi')
CONG['hi'] = 'और'
for (_p, _sl, _t), _h in zip(GRUPPI, ['रेनोवेशन', 'जनरल कॉन्ट्रैक्टर', 'होटल फ़र्नीचर']): _t['hi'] = _h
TIT['hi'] = 'हम कहाँ काम करते हैं'
H2['hi'] = 'Veneto और Friuli Venezia Giulia, <span class="grad">शहर-दर-शहर</span>'
LEAD['hi'] = 'उत्तर-पूर्वी इटली के Veneto और Friuli Venezia Giulia के हर प्रांत में मुफ़्त साइट सर्वे। ये वे इलाक़े हैं जहाँ हम सबसे ज़्यादा काम करते हैं।'
PILASTRO['hi'] = 'Danova Real Estate: इटली के Veneto में रेनोवेशन कंपनी'
TT['citta']['hi'] = ('%s, इटली में बिल्डर | टर्नकी रेनोवेशन', '%s में बिल्डर | रेनोवेशन')
TT['gc']['hi'] = ('%s, इटली में जनरल कॉन्ट्रैक्टर | फ़िक्स्ड प्राइस', '%s में जनरल कॉन्ट्रैक्टर')
TT['hotel']['hi'] = ('%s में होटल फ़र्नीचर | कस्टम कॉन्ट्रैक्ट फ़र्नीचर', '%s में होटल फ़र्नीचर | कस्टम')
KNOWS['hi'] = ['टर्नकी रेनोवेशन', 'बाथरूम रेनोवेशन', 'कंस्ट्रक्शन कंपनी', 'जनरल कॉन्ट्रैक्टर', 'बाहरी थर्मल इंसुलेशन', 'अटारी इंसुलेशन', 'छत की मरम्मत',
               'वेंटिलेटेड फ़साड', 'बाहरी फ़्लोरिंग', 'ड्राईवॉल और फ़ॉल्स सीलिंग', 'फ़ायर-रेटेड दरवाज़े', 'फ़र्श और खिड़कियाँ', 'होटल फ़र्नीचर', 'कस्टम फ़र्नीचर',
               'इटली में बिल्डिंग परमिट (CILA, SCIA)', 'इटली रेनोवेशन टैक्स बोनस']
SLOGAN['hi'] = 'मुफ़्त साइट सर्वे, फ़िक्स्ड प्राइस, कॉन्ट्रैक्ट में समय-सीमा, एक ही ज़िम्मेदार व्यक्ति।'
for _k in LG.S:
    INV[LG.url(_k, 'hi')] = (_k, 'hi')


def schema(s, key, l, title, desc, url):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    if not m:
        return s
    g = json.loads(m.group(1))
    org = next((n for n in g['@graph'] if n.get('@id') == SITE + '/#organization'), {})
    for n in g['@graph']:
        if n.get('@type') == 'GeneralContractor':
            n['hasMap'] = org.get('hasMap', 'https://maps.app.goo.gl/gPgYPeA5Rtc12wve8')
            n['sameAs'] = SOCIAL
            # 26/10/2026: tutte le 11 province servite, servizi, orari e fascia di prezzo (per Google e per gli assistenti AI)
            n['areaServed'] = [{"@type": "AdministrativeArea", "name": "Veneto"}, {"@type": "AdministrativeArea", "name": "Friuli-Venezia Giulia"}] + \
                [{"@type": "AdministrativeArea", "name": "Provincia di %s" % p_, "containedInPlace": {"@type": "AdministrativeArea", "name": r_}} for p_, r_ in PROVINCE]
            n['knowsAbout'] = KNOWS[l]
            if org.get('openingHoursSpecification'):
                n['openingHoursSpecification'] = org['openingHoursSpecification']
            n['priceRange'] = '€€'
            n['slogan'] = SLOGAN[l]
        if n.get('@type') == 'WebPage':
            n['name'] = title
            n['description'] = desc
    if key.startswith('/guide/'):
        art_id = SITE + url + '#article'
        img = next((n.get('url') for n in g['@graph'] if n.get('@type') == 'ImageObject'), None)
        wp = next((n for n in g['@graph'] if n.get('@type') == 'WebPage'), {})
        g['@graph'] = [n for n in g['@graph'] if n.get('@type') != 'Service' and n.get('@id') != art_id]
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        g['@graph'].append({"@type": "Article", "@id": art_id, "headline": html.unescape(re.sub(r'<[^>]+>', '', h1.group(1))).strip()[:110] if h1 else title,
                            "description": desc, "inLanguage": LG.CFG[l]['hl'][0], "mainEntityOfPage": {"@id": SITE + url + '#webpage'},
                            "image": img, "datePublished": wp.get('datePublished', '2026-10-24'), "dateModified": wp.get('dateModified', '2026-10-24'),
                            "author": {"@id": SITE + '/real-estate/#danova-real-estate'}, "publisher": {"@id": SITE + '/#organization'},
                            "about": {"@id": SITE + '/real-estate/#danova-real-estate'}})
    return s[:m.start(1)] + '\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n' + s[m.end(1):]


def main():
    n = 0; nd = 0; nz = 0
    for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
        rel = os.path.relpath(f, R).replace('\\', '/')
        if rel.startswith(('seo-tools/', '_archivio/', 'social/')):
            continue
        s = open(f, encoding='utf-8').read()
        if 'name="dt-sezione" content="real-estate"' not in s:
            continue
        url = '/' + rel[:-len('index.html')]
        if url not in INV:
            continue
        key, l = INV[url]
        s0 = s
        # titolo
        t0 = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
        t1 = titolo(key, l, t0)
        if t1 != t0:
            s = re.sub(r'<title>.*?</title>', lambda m: '<title>%s</title>' % html.escape(t1, quote=False), s, count=1, flags=re.S)
            for p in ('og:title', 'og:image:alt'):
                s = re.sub(r'<meta property="%s" content="[^"]*">' % p, lambda m: '<meta property="%s" content="%s">' % (p, html.escape(t1)), s, count=1)
            s = re.sub(r'<meta name="twitter:title" content="[^"]*">', lambda m: '<meta name="twitter:title" content="%s">' % html.escape(t1), s, count=1)
        # description
        dm = re.search(r'<meta name="description" content="([^"]*)">', s)
        d0 = html.unescape(dm.group(1)); d1 = corta(d0, l)
        if d1 != d0:
            s = s[:dm.start(1)] + html.escape(d1) + s[dm.end(1):]; nd += 1
        # dove lavoriamo
        s = re.sub(r'<!--re-zone-->.*?<!--/re-zone-->\n?', '', s, flags=re.S)
        s = s.replace(CSS, '')
        if con_zona(key):
            blocco = zona_blocco(l, url)
            if '<section id="altri">' in s:
                s = s.replace('<section id="altri">', blocco + '<section id="altri">', 1)
            else:
                s = s.replace('</main>', blocco + '</main>', 1)
            s = s.replace('</head>', CSS + '</head>', 1); nz += 1
        s = schema(s, key, l, t1, d1, url)
        if s != s0:
            open(f, 'w', encoding='utf-8').write(s); n += 1
    print('SEO Real Estate: pagine aggiornate %d | description accorciate %d | blocchi "dove lavoriamo" %d' % (n, nd, nz))


if __name__ == '__main__':
    main()
