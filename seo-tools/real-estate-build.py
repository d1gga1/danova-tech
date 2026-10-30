# -*- coding: utf-8 -*-
"""24/10/2026 - Sezione DANOVA REAL ESTATE in 7 lingue (it, en, de, ro, sq, hi, hr).
   Motore: pagine-build.py + pagine-build-2026-10-23.py, con in piu':
   - hero con immagine/video di sfondo (d['hero'] = nome immagine in assets/img/re/, d['herovid'] facoltativo)
   - sezioni 'ba' (prima/dopo con cursore), 'gal' (galleria 3D), 'split' (video/immagine + testo), 'promesse'
   - <meta name="dt-sezione" content="real-estate"> per il tema (seo-tools/real-estate-tema.py)
   - hreflang reciproci fra le 6 lingue (hr vale anche per bs e sr-Latn) e selettore di lingua
   - cornice del donatore inglese tradotta per ro / sq / hi / hr (real-estate-lingue.py)
   Dati: real-estate-dati-*.py (IT) e real-estate-tr-<lingua>-*.py (traduzioni, ogni pagina ha 'key' = URL italiano).
   Idempotente.  Uso: bash seo-tools/real-estate-tutto.sh   (build + catena post-build)"""
import os, re, json, html, importlib.util, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
P23 = load('p23', 'pagine-build-2026-10-23.py')
LG = load('relingue', 'real-estate-lingue.py')
pb = P23.pb
SITE = pb.SITE; e = pb.e
FILES = sorted(glob.glob(os.path.join(HERE, 'real-estate-dati-*.py'))) + sorted(glob.glob(os.path.join(HERE, 'real-estate-tr-*.py')))
DATI = [load('red%d' % i, os.path.basename(f)) for i, f in enumerate(FILES)]
pb.pd = DATI[0]
for l, c in LG.CFG.items():
    pb.DONOR[l] = c['donor']; pb.LOC[l] = c['loc']; pb.OGL[l] = c['og']; pb.HOME[l] = c['home']
IMG = '/assets/img/re/'; VID = '/assets/video/re/'
RE_DESC = {
 'it': 'Divisione edilizia di Danova Tech: ristrutturazioni chiavi in mano, general contractor, facciate e cappotto, tetti e sottotetti, pavimentazioni esterne, porte, cartongesso, pavimenti, arredo hotel e mobili su misura in tutto il Veneto e il Friuli Venezia Giulia.',
 'en': 'Construction division of Danova Tech: turnkey renovations, general contracting, facades and insulation, roofs and lofts, outdoor paving, doors, drywall, flooring, hotel furniture and custom joinery in Veneto and Friuli Venezia Giulia, Italy.',
 'de': 'Bausparte von Danova Tech: schlüsselfertige Renovierungen, Generalunternehmer, Fassaden und Dämmung, Dächer und Dachböden, Außenbeläge, Türen, Trockenbau, Böden, Hotel- und Maßmöbel in Venetien und Friaul-Julisch Venetien.',
 'ro': 'Divizia de construcții a Danova Tech: renovări la cheie, antreprenor general, fațade și izolații, acoperișuri și poduri, pavaje exterioare, uși, rigips, pardoseli, mobilier hotelier și mobilă la comandă în Veneto și Friuli Venezia Giulia, Italia.',
 'sq': 'Divizioni i ndërtimit i Danova Tech: rinovime çelës në dorë, kontraktor i përgjithshëm, fasada dhe termoizolim, çati dhe papafingo, shtrime të jashtme, dyer, gipskarton, dysheme, mobilim hotelesh dhe mobilje me porosi në Veneto dhe Friuli Venezia Giulia, Itali.',
 'hi': 'Danova Tech का कंस्ट्रक्शन डिवीज़न: इटली के Veneto और Friuli Venezia Giulia में टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर, फ़साड और इंसुलेशन, छतें और अटारी, बाहरी फ़्लोरिंग, दरवाज़े, ड्राईवॉल, फ़र्श, होटल फ़र्नीचर और कस्टम फ़र्नीचर।',
 'hr': 'Građevinski odjel tvrtke Danova Tech: renoviranje po sistemu ključ u ruke, generalni izvođač, fasade, vrata, gips, podovi i namještaj za hotele u Venetu i Furlaniji.'}
CUR = ['it']
UI = lambda k: LG.UI[CUR[0]][k]

PROM = {
 'it': [("Sopralluogo e preventivo gratuiti", "Veniamo a vedere, misuriamo e vi consegniamo un preventivo dettagliato voce per voce, senza impegno."),
        ("Prezzo bloccato, chiavi in mano", "Il prezzo concordato è quello che pagate: niente extra a sorpresa a lavori iniziati."),
        ("Tempi scritti nel contratto", "Data di inizio e di consegna messe nero su bianco, con il cronoprogramma dei lavori."),
        ("Un unico referente", "Una sola persona coordina squadre, fornitori, pratiche e vi aggiorna sull’avanzamento.")],
 'en': [("Free survey and quote", "We visit, measure and give you a detailed, itemised quote, with no obligation."),
        ("Fixed turnkey price", "The agreed price is the price you pay: no surprise extras once work has started."),
        ("Deadlines in the contract", "Start and completion dates in black and white, with a full work schedule."),
        ("One point of contact", "A single person coordinates crews, suppliers and permits and keeps you updated.")],
 'de': [("Kostenlose Besichtigung und Angebot", "Wir kommen vorbei, messen auf und erstellen ein detailliertes Angebot Position für Position, unverbindlich."),
        ("Schlüsselfertiger Festpreis", "Der vereinbarte Preis ist der Endpreis: keine Überraschungen nach Baubeginn."),
        ("Termine im Vertrag", "Beginn und Fertigstellung schwarz auf weiß, mit vollständigem Bauzeitenplan."),
        ("Ein Ansprechpartner", "Eine Person koordiniert Handwerker, Lieferanten und Genehmigungen und hält Sie auf dem Laufenden.")],
 'ro': [("Inspecție și ofertă gratuite", "Venim la fața locului, măsurăm și vă dăm o ofertă detaliată pe fiecare poziție, fără obligații."),
        ("Preț blocat, la cheie", "Prețul convenit este cel pe care îl plătiți: fără costuri surpriză după începerea lucrărilor."),
        ("Termene scrise în contract", "Data de început și de predare trecute negru pe alb, cu graficul lucrărilor."),
        ("Un singur responsabil", "O singură persoană coordonează echipele, furnizorii și actele și vă ține la curent.")],
 'sq': [("Inspektim dhe ofertë falas", "Vijmë në vend, masim dhe ju japim një ofertë të detajuar zë për zë, pa asnjë detyrim."),
        ("Çmim i bllokuar, çelës në dorë", "Çmimi i rënë dakord është ai që paguani: pa shpenzime të papritura pasi fillojnë punimet."),
        ("Afatet të shkruara në kontratë", "Data e fillimit dhe e dorëzimit të shkruara qartë, me grafikun e punimeve."),
        ("Një person i vetëm kontakti", "Një person i vetëm koordinon skuadrat, furnitorët dhe lejet dhe ju mban të informuar.")],
 'hi': [("मुफ़्त साइट सर्वे और कोटेशन", "हम आकर देखते हैं, नाप लेते हैं और हर काम का अलग विस्तृत कोटेशन देते हैं, बिना किसी बाध्यता के।"),
        ("फ़िक्स्ड टर्नकी प्राइस", "तय कीमत ही आप देते हैं: काम शुरू होने के बाद कोई अचानक अतिरिक्त ख़र्च नहीं।"),
        ("कॉन्ट्रैक्ट में समय-सीमा", "शुरू और हैंडओवर की तारीख़ें लिखित में, काम के पूरे शेड्यूल के साथ।"),
        ("एक ही ज़िम्मेदार व्यक्ति", "एक ही व्यक्ति टीमों, सप्लायरों और परमिट का समन्वय करता है और आपको अपडेट देता है।")],
 'hr': [("Besplatan obilazak i ponuda", "Dolazimo na lice mjesta, mjerimo i dajemo vam detaljnu ponudu stavku po stavku, bez obveze."),
        ("Fiksna cijena, ključ u ruke", "Dogovorena cijena je ona koju plaćate: bez iznenadnih troškova nakon početka radova."),
        ("Rokovi upisani u ugovor", "Datum početka i predaje crno na bijelo, s terminskim planom radova."),
        ("Jedna kontakt osoba", "Jedna osoba koordinira ekipe, dobavljače i dozvole i redovito vas obavještava.")],
}

W_IMG = [480, 800, 1200, 1600, 2000, 2688]
SIZES = {'hero': '(orientation: portrait) 150vh, 100vw',
         'ba': '(max-width: 900px) calc(100vw - 44px), 610px',
         'split': '(max-width: 900px) calc(100vw - 44px), 640px',
         'gal': '(max-width: 640px) calc(100vw - 44px), (max-width: 1000px) 50vw, 410px'}
def _ss(nome, ext): return ', '.join('%s%s-%d.%s %dw' % (IMG, nome, w, ext, w) for w in W_IMG)

def immagine(nome, alt, ctx='ba', lazy=True, cls=''):
    """<picture> AVIF + WebP, 6 larghezze, immagine intera 16:9 (nessun ritaglio)"""
    return ('<picture><source type="image/avif" srcset="%s" sizes="%s"><source type="image/webp" srcset="%s" sizes="%s">'
            '<img src="%s%s-1200.webp" width="1600" height="900" alt="%s"%s%s decoding="async"></picture>'
            % (_ss(nome, 'avif'), SIZES[ctx], _ss(nome, 'webp'), SIZES[ctx], IMG, nome, html.escape(alt),
               ' loading="lazy"' if lazy else ' fetchpriority="high"', (' class="%s"' % cls) if cls else ''))

def video(nome, poster, titolo, auto=True):
    """niente autoplay nell'HTML: il video si scarica e parte solo quando entra nello schermo (VJS)"""
    return ('<video %splaysinline muted loop preload="none" width="1276" height="720" poster="%s%s-poster.webp" aria-label="%s" data-re-vid>'
            '<source src="%s%s.av1.mp4" type=\'video/mp4; codecs="av01.0.05M.08"\'><source src="%s%s.mp4" type="video/mp4"></video>'
            % ('data-auto ' if auto else 'controls ', IMG, nome, html.escape(titolo), VID, nome, VID, nome))

VJS = ('<script>(function(){if(window.__reV)return;window.__reV=1;'
       'var vs=[].slice.call(document.querySelectorAll("video[data-re-vid]"));'
       'var rm=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;'
       '[].slice.call(document.querySelectorAll(".re-ba input")).forEach(function(i){i.addEventListener("input",function(){'
       'i.parentNode.style.setProperty("--p",i.value+"%");});});'
       'if(rm||!("IntersectionObserver" in window)){vs.forEach(function(v){v.controls=true;v.preload="metadata";});return;}'
       'var o=new IntersectionObserver(function(es){es.forEach(function(x){var v=x.target;'
       'if(x.isIntersecting){if(v.preload==="none"){v.preload="auto";}if(v.hasAttribute("data-auto")){var p=v.play();if(p&&p.catch)p.catch(function(){});}}'
       'else if(!v.paused)v.pause();});},{rootMargin:"300px 0px",threshold:0.01});vs.forEach(function(v){o.observe(v);});})();</script>\n')

def gal_span(n):
    if n == 1: return [6]
    if n in (2, 4): return [3] * n
    r = n % 3
    if r == 0: return [2] * n
    if r == 2: return [2] * (n - 2) + [3, 3]
    return [2] * (n - 4) + [3] * 4

def head_sec(sec):
    o = ['<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n' % sec['id']]
    if sec.get('eyebrow'): o.append('      <div class="eyebrow mono" data-scramble>%s</div>\n' % e(sec['eyebrow']))
    o.append('      <h2 class="title" data-rv="up">%s</h2>\n' % sec['h2'])
    if sec.get('lead'): o.append('      <p class="lead" data-rv="up">%s</p>\n' % e(sec['lead']))
    o.append('    </div>\n'); return o

_prev = pb.sezione
def sezione(sec):
    t = sec.get('tipo', 'testo')
    if t not in ('ba', 'gal', 'split', 'promesse', 'html'): return _prev(sec)
    o = head_sec(sec)
    if t == 'html':                      # 26/10/2026: HTML libero (es. modulo candidatura partner)
        o.append(sec['html'])
    elif t == 'ba':
        figs = []
        for it in sec['items']:
            figs.append(['ba', '<figure class="re-ba-fig@@W@@" data-rv="up">\n        <div class="re-ba">%s%s'
                     '<span class="re-linea"></span><span class="re-et p">%s</span><span class="re-et d">%s</span>'
                     '<input type="range" min="0" max="100" value="50" aria-label="%s: %s"></div>\n'
                     '        <figcaption><b>%s</b> <span>%s</span></figcaption>\n      </figure>\n'
                     % (immagine(it['prima'], UI('prima') + ': ' + it['titolo']), immagine(it['dopo'], UI('dopo') + ': ' + it['titolo'], cls='re-dopo'),
                        UI('prima'), UI('dopo'), html.escape(UI('cmp')), html.escape(it['titolo']), e(it['titolo']), e(it['testo']))])
        for nome, poster, tit in sec.get('video', []):
            figs.append(['vid', '<figure class="re-video@@W@@" data-rv="up">%s<figcaption>%s</figcaption></figure>\n' % (video(nome, poster, tit), e(tit))])
        if len(figs) % 2 == 1 and len(figs) > 1:      # numero dispari: l'ultimo occupa tutta la riga (immagine + testo affiancati)
            ib = [i for i, x in enumerate(figs) if x[0] == 'ba']
            k = ib[-1] if ib else len(figs) - 1
            figs.append(figs.pop(k)); figs[-1][1] = figs[-1][1].replace('@@W@@', ' re-wide' if figs[-1][0] == 'ba' else ' re-solo')
        elif len(figs) == 1:
            figs[0][1] = figs[0][1].replace('@@W@@', ' re-wide' if figs[0][0] == 'ba' else ' re-solo')
        o.append('    <div class="re-ba-grid">\n')
        for x in figs: o.append('      ' + x[1].replace('@@W@@', ''))
        o.append('    </div>\n')
        o.append('    <p class="re-nota-img">%s</p>\n' % UI('nota'))
    elif t == 'gal':
        sp = gal_span(len(sec['items']))
        o.append('    <div class="re-gal">\n')
        for it, k in zip(sec['items'], sp):
            media = video(it['video'], it['img'], it['titolo']) if it.get('video') else immagine(it['img'], it.get('alt', it['titolo']), ctx='gal')
            o.append('      <figure class="s%d" data-rv="up"><div class="re-m">%s</div><figcaption><b>%s</b><span>%s</span></figcaption></figure>\n' % (k, media, e(it['titolo']), e(it['testo'])))
        o.append('    </div>\n    <p class="re-nota-img">%s</p>\n' % UI('nota'))
    elif t == 'split':
        media = (video(sec['video'], sec['img'], sec['didascalia']) if sec.get('video') else immagine(sec['img'], sec['didascalia'], ctx='split'))
        o.append('    <div class="re-split">\n      <figure class="re-video" data-rv="up">%s<figcaption>%s</figcaption></figure>\n      <div class="pg-testo" data-rv="up">\n%s      </div>\n    </div>\n'
                 % (media, e(sec['didascalia']), ''.join('        <p>%s</p>\n' % p for p in sec['corpo'])))
    elif t == 'promesse':
        o.append('    <div class="re-promesse" data-rv="up">\n%s    </div>\n'
                 % ''.join('      <div><b>%s</b><span>%s</span></div>\n' % (e(a), e(b)) for a, b in sec.get('corpo', PROM[CUR[0]])))
    o.append('  </div>\n</section>\n')
    return ''.join(o)
P23._prev_hook = None
pb.sezione = lambda sec: sezione(sec) if sec.get('tipo') in ('ba', 'gal', 'split', 'promesse', 'html') else P23.sezione(sec, CUR[0])

def lingue(d, s):
    if d.get('solo_it'):   # 26/10/2026: pagina solo italiana (es. /diventa-partner/): hreflang solo IT, il selettore porta alle home Real Estate
        alt = {l: LG.url('/real-estate/', l) for l in LG.LINGUE}; alt['it'] = d['key']; hl = ['it']
    else:
        alt = LG.alt(d['key']); hl = LG.LINGUE
    links = ''.join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (h, SITE, alt[l]) for l in hl for h in LG.CFG[l]['hl'])
    links += '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (SITE, alt['it'])
    s = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n?', '', s)
    s = re.sub(r'(<link rel="canonical" href="[^"]*">\n?)', lambda m: m.group(1) + links, s, count=1)
    def sw(c):
        return ''.join(c + '<a href="%s" hreflang="%s"%s>%s</a>' % (alt[l], LG.CFG[l]['hl'][0], ' aria-current="page"' if l == d['lang'] else '', LG.CFG[l]['lab'])
                       for l in LG.LINGUE)
    if '<span class="lang-links">' in s:
        s = re.sub(r'(<span class="lang-links">)(.*?)(</span>)', lambda m: m.group(1) + sw('\n        ') + '\n      ' + m.group(3), s, count=1, flags=re.S)
    else:
        s = s.replace('<div class="nav-r">', '<div class="nav-r">\n      <span class="lang-links">%s\n      </span>' % sw('\n        '), 1)
    if '<div class="mob-lang-links">' in s:
        s = re.sub(r'(<div class="mob-lang-links">)(.*?)(</div>)', lambda m: m.group(1) + sw('\n    ') + '\n  ' + m.group(3), s, count=1, flags=re.S)
    else:
        s = re.sub(r'(<nav id="mob"[^>]*>.*?)(</nav>)', lambda m: m.group(1) + '\n  <div class="mob-lang-links">%s\n  </div>\n' % sw('\n    ') + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'<meta name="robots" content="[^"]*">',
               '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">', s, count=1)
    if 'id="pg2310"' not in s: s = s.replace('</head><body>', P23.CSS + '</head><body>', 1)
    return s

def post(d, s):
    lang = d['lang']
    if 'name="dt-sezione"' not in s:
        s = s.replace('<meta name="description"', '<meta name="dt-sezione" content="real-estate">\n<meta name="description"', 1)
    s = re.sub(r'<html lang="[^"]*"', '<html lang="%s"' % LG.CFG[lang]['hl'][0], s, count=1)
    for a, b in LG.CHROME.get(lang, []): s = s.replace(a, b)
    if lang == 'hi': s = s.replace(' data-scramble', '')   # 29/10/2026: l'effetto con lettere latine casuali stona sul devanagari
    if lang in ('ro', 'sq', 'hr', 'hi'):   # shell EN: i link relativi '../' puntano a /en/, non a /xx/
        s = re.sub(r'href="\.\./(?!\.\./)', 'href="/en/', s)
    if lang not in ('it', 'en'):
        s = s.replace('<a href="%s">Home</a>' % pb.HOME[lang], '<a href="%s">%s</a>' % (pb.HOME[lang], UI('home')), 1)
    # hero: sempre immagine ad alta risoluzione (un video 720p a tutto schermo risulta sfocato)
    bg = immagine(d['hero'], d.get('heroalt', d['ogtitle']), ctx='hero', lazy=False)
    if 'rel="preload" as="image"' not in s:
        s = s.replace('<link rel="canonical"', '<link rel="preload" as="image" type="image/avif" imagesrcset="%s" imagesizes="(orientation: portrait) 150vh, 100vw" fetchpriority="high">\n<link rel="canonical"' % _ss(d['hero'], 'avif'), 1)
    s = s.replace('<section class="pg-hero">\n  <div class="wrap">',
                  '<section class="pg-hero re-hero">\n  <div class="re-bg">%s</div>\n  <div class="wrap">' % bg, 1)
    badges = d.get('badges', UI('badges'))
    s = re.sub(r'(<section class="pg-hero re-hero">.*?<div class="hero-cta" data-rv="up">.*?</a>\s*<a [^>]*>.*?</a>\s*</div>)',
               lambda m: m.group(1) + '\n    <div class="re-badges" data-rv="up">%s</div>' % ''.join('<span>%s</span>' % e(b) for b in badges),
               s, count=1, flags=re.S)
    if '__reV' not in s: s = s.replace('</main>', VJS + '</main>', 1)
    og = SITE + IMG + d['hero'] + '.jpg'
    s = re.sub(r'(<meta property="og:image" content=")[^"]*(")', lambda m: m.group(1) + og + m.group(2), s, count=1)
    s = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', lambda m: m.group(1) + og + m.group(2), s, count=1)
    s = re.sub(r'<meta property="og:image:alt" content="[^"]*">', '<meta property="og:image:alt" content="%s">' % html.escape(d['ogtitle']), s, count=1)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    g = json.loads(m.group(1))
    imgobj = {"@type": "ImageObject", "@id": SITE + d['url'] + "#primaryimage", "url": og, "width": 1200, "height": 630, "caption": d['ogtitle']}
    for n in g['@graph']:
        if n.get('@type') == 'Service':
            n['image'] = og
        if n.get('@type') == 'WebPage':
            n['primaryImageOfPage'] = {"@id": imgobj['@id']}
        if n.get('@type') == 'BreadcrumbList' and lang not in ('it', 'en'):
            n['itemListElement'][0]['name'] = UI('home')
    if not any(n.get('@id') == imgobj['@id'] for n in g['@graph']): g['@graph'].append(imgobj)
    # entita' Danova Real Estate (GeneralContractor, divisione di Danova Tech) + VideoObject dei video in pagina
    org = next((n for n in g['@graph'] if n.get('@id') == SITE + '/#organization'), {})
    reid = SITE + '/real-estate/#danova-real-estate'
    rorg = {"@type": "GeneralContractor", "@id": reid, "name": "Danova Real Estate", "alternateName": "Danova Real Estate by Danova Tech",
            "description": RE_DESC[lang], "url": SITE + LG.url('/real-estate/', lang), "logo": SITE + "/assets/img/logo.png",
            "image": SITE + IMG + 're-soggiorno-nuovo.jpg', "telephone": org.get('telephone', '+39 388 470 6887'), "email": org.get('email', 'info@danova-tech.com'),
            "address": org.get('address'), "geo": org.get('geo'),
            "areaServed": [{"@type": "AdministrativeArea", "name": "Veneto"}, {"@type": "AdministrativeArea", "name": "Friuli-Venezia Giulia"}],
            "knowsLanguage": ["it", "en", "ro"], "parentOrganization": {"@id": SITE + "/#organization"},
            "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "telephone": "+39 388 470 6887", "email": "info@danova-tech.com", "availableLanguage": ["Italian", "English", "Romanian"], "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}}}
    rorg = {k: v for k, v in rorg.items() if v}
    g['@graph'] = [n for n in g['@graph'] if n.get('@id') != reid and n.get('@type') != 'VideoObject']
    g['@graph'].append(rorg)
    for n in g['@graph']:
        if n.get('@type') == 'Service': n['provider'] = {"@id": reid}
    dm = re.search(r'<meta name="description" content="([^"]*)"', s)
    pdesc = html.unescape(dm.group(1)) if dm else ''
    vis = set()
    for vm in re.finditer(r'<video\b[^>]*poster="([^"]+)"[^>]*aria-label="([^"]+)"[^>]*data-re-vid>(.*?)</video>', s, re.S):
        pos, tit, srcs = vm.groups()
        mp4 = [x for x in re.findall(r'<source src="([^"]+)"', srcs) if not x.endswith('.av1.mp4')][0]
        if mp4 in vis: continue
        vis.add(mp4); tit = html.unescape(tit)
        g['@graph'].append({"@type": "VideoObject", "@id": SITE + d['url'] + '#video-' + os.path.basename(mp4)[:-4], "name": tit,
                            "description": (tit + ' — ' + pdesc)[:500], "thumbnailUrl": [SITE + pos], "contentUrl": SITE + mp4,
                            "uploadDate": "2026-10-24T09:00:00+02:00", "duration": "PT5S", "inLanguage": LG.CFG[lang]['hl'][0],
                            "isFamilyFriendly": True, "publisher": {"@id": SITE + "/#organization"}})
    s = s[:m.start(1)] + '\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n' + s[m.end(1):]
    return s

# 24/10/2026: "Hotel" (lavori) e "Arredo hotel" (arredi) non ripetono le stesse immagini
_CANT = {'it': ('Cantiere in bassa stagione', 'Cartongesso, impianti e finiture a hotel chiuso.'),
         'en': ('Works in the low season', 'Drywall, services and finishes while the hotel is closed.'),
         'de': ('Baustelle in der Nebensaison', 'Trockenbau, Haustechnik und Ausbau bei geschlossenem Hotel.'),
         'ro': ('Șantier în extrasezon', 'Rigips, instalații și finisaje cu hotelul închis.'),
         'sq': ('Kantier jashtë sezonit', 'Gipskarton, impiante dhe përfundime me hotelin të mbyllur.'),
         'hi': ('ऑफ़-सीज़न में साइट', 'होटल बंद रहते हुए ड्राईवॉल, सिस्टम और फ़िनिशिंग।'),
         'hr': ('Gradilište izvan sezone', 'Gips, instalacije i završni radovi dok je hotel zatvoren.')}
_R3D = {'it': ('Progetto e render 3D', 'Ogni arredo approvato in 3D prima della produzione.'),
        'en': ('Design and 3D rendering', 'Every piece approved in 3D before production.'),
        'de': ('Planung und 3D-Rendering', 'Jedes Möbel wird vor der Produktion in 3D freigegeben.'),
        'ro': ('Proiect și randare 3D', 'Fiecare piesă aprobată în 3D înainte de producție.'),
        'sq': ('Projekt dhe render 3D', 'Çdo mobilje miratohet në 3D para prodhimit.'),
        'hi': ('डिज़ाइन और 3D रेंडर', 'हर फ़र्नीचर निर्माण से पहले 3D में मंज़ूर।'),
        'hr': ('Projekt i 3D vizualizacija', 'Svaki komad odobren u 3D-u prije proizvodnje.')}
def distingui_hotel(d):
    l = d['lang']
    if d['key'] == '/ristrutturazione-hotel/':
        for sec in d['sezioni']:
            if sec.get('tipo') == 'gal':
                its = [x for x in sec['items'] if x.get('img') not in ('re-camera-hotel-mare', 're-lobby-hotel-dolomiti')]
                t, x = _CANT.get(l, _CANT['en'])
                sec['items'] = [{'img': 're-cantiere-cartongesso', 'titolo': t, 'testo': x}] + its
    else:
        d['sezioni'] = [sec for sec in d['sezioni'] if sec.get('tipo') != 'ba']
        d.pop('herovid', None)
        for sec in d['sezioni']:
            if sec.get('tipo') == 'gal':
                t, x = _R3D.get(l, _R3D['en'])
                sec['items'] = [it if it.get('img') != 're-ristorante' else {'img': 're-render-3d', 'titolo': t, 'testo': x} for it in sec['items']]
                sec['items'] = [it for it in sec['items'] if it.get('img') != 're-camera-hotel-mare']

if __name__ == '__main__':
    import sys
    solo = sys.argv[1:]   # facoltativo: lingue da generare (es. en de)
    tutte = [d for D in DATI for d in getattr(D, 'PAGINE', [])]
    for d in tutte: d.setdefault('key', d['url'])
    # 24/10/2026: copertine diverse per "Hotel" (ristrutturazione) e "Arredo hotel" e per le pagine hotel vicine
    HERO = {'/ristrutturazione-hotel/': 're-hotel-dolomiti-esterno', '/guide/ristrutturare-un-hotel/': 're-hotel-garda-terrazza',
            '/arredo-hotel-cortina/': 're-lobby-hotel-dolomiti'}
    HERO['/arredo-hotel-contract/'] = 're-ristorante'
    for d in tutte:
        if d['key'] in HERO: d['hero'] = HERO[d['key']]
        if d['key'] in ('/ristrutturazione-hotel/', '/arredo-hotel-contract/'): distingui_hotel(d)
    n = 0
    for d in tutte:
        if solo and d['lang'] not in solo: continue
        CUR[0] = d['lang']; P23._cur_lang[0] = d['lang']; P23._cur_url[0] = d['url']
        p = P23.build(d)
        f = os.path.join(ROOT, p)
        s = post(d, lingue(d, open(f, encoding='utf-8').read()))
        if d.get('cta_href'):   # 26/10/2026: i pulsanti della pagina portano al suo modulo (es. #candidatura)
            s = s.replace('href="%s#contatti" class="btn btn-p" data-mag><span class="sheen">' % pb.HOME[d['lang']], 'href="%s" class="btn btn-p" data-mag><span class="sheen">' % d['cta_href'])
        open(f, 'w', encoding='utf-8').write(s); n += 1
    from collections import Counter
    print('pagine Real Estate generate:', n, dict(Counter(d['lang'] for d in tutte if not solo or d['lang'] in solo)))
