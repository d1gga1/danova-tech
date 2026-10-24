# -*- coding: utf-8 -*-
"""24/10/2026 - Sezione DANOVA REAL ESTATE in 6 lingue (it, en, de, ro, sq, hr).
   Motore: pagine-build.py + pagine-build-2026-10-23.py, con in piu':
   - hero con immagine/video di sfondo (d['hero'] = nome immagine in assets/img/re/, d['herovid'] facoltativo)
   - sezioni 'ba' (prima/dopo con cursore), 'gal' (galleria 3D), 'split' (video/immagine + testo), 'promesse'
   - <meta name="dt-sezione" content="real-estate"> per il tema (seo-tools/real-estate-tema.py)
   - hreflang reciproci fra le 6 lingue (hr vale anche per bs e sr-Latn) e selettore di lingua
   - cornice del donatore inglese tradotta per ro / sq / hr (real-estate-lingue.py)
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
 'hr': [("Besplatan obilazak i ponuda", "Dolazimo na lice mjesta, mjerimo i dajemo vam detaljnu ponudu stavku po stavku, bez obveze."),
        ("Fiksna cijena, ključ u ruke", "Dogovorena cijena je ona koju plaćate: bez iznenadnih troškova nakon početka radova."),
        ("Rokovi upisani u ugovor", "Datum početka i predaje crno na bijelo, s terminskim planom radova."),
        ("Jedna kontakt osoba", "Jedna osoba koordinira ekipe, dobavljače i dozvole i redovito vas obavještava.")],
}

def immagine(nome, alt, w=1600, h=900, lazy=True, cls=''):
    return ('<img src="%s%s.webp" srcset="%s%s-800.webp 800w, %s%s.webp 1600w" sizes="(max-width: 900px) 100vw, 50vw" '
            'width="%d" height="%d" alt="%s"%s%s decoding="async">'
            % (IMG, nome, IMG, nome, IMG, nome, w, h, html.escape(alt),
               ' loading="lazy"' if lazy else ' fetchpriority="high"', (' class="%s"' % cls) if cls else ''))

def video(nome, poster, titolo, auto=True):
    return ('<video %splaysinline preload="none" width="1280" height="720" poster="%s%s.webp" title="%s" data-re-vid>'
            '<source src="%s%s.mp4" type="video/mp4"></video>'
            % ('muted loop autoplay ' if auto else 'controls ', IMG, poster, html.escape(titolo), VID, nome))

VJS = ('<script>(function(){if(window.__reV)return;window.__reV=1;'
       'var vs=[].slice.call(document.querySelectorAll("video[data-re-vid]"));'
       'var rm=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;'
       'if(!("IntersectionObserver" in window)||rm)return;'
       'var o=new IntersectionObserver(function(es){es.forEach(function(x){var v=x.target;'
       'if(x.isIntersecting){if(v.preload==="none")v.preload="auto";if(v.autoplay){var p=v.play();if(p&&p.catch)p.catch(function(){});}}'
       'else if(v.autoplay)v.pause();});},{rootMargin:"200px"});vs.forEach(function(v){o.observe(v);});'
       '[].slice.call(document.querySelectorAll(".re-ba input")).forEach(function(i){i.addEventListener("input",function(){'
       'i.parentNode.style.setProperty("--p",i.value+"%");});});})();</script>\n')

def head_sec(sec):
    o = ['<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n' % sec['id']]
    if sec.get('eyebrow'): o.append('      <div class="eyebrow mono" data-scramble>%s</div>\n' % e(sec['eyebrow']))
    o.append('      <h2 class="title" data-rv="up">%s</h2>\n' % sec['h2'])
    if sec.get('lead'): o.append('      <p class="lead" data-rv="up">%s</p>\n' % e(sec['lead']))
    o.append('    </div>\n'); return o

_prev = pb.sezione
def sezione(sec):
    t = sec.get('tipo', 'testo')
    if t not in ('ba', 'gal', 'split', 'promesse'): return _prev(sec)
    o = head_sec(sec)
    if t == 'ba':
        o.append('    <div class="re-ba-grid">\n')
        for it in sec['items']:
            o.append('      <figure class="re-ba-fig" data-rv="up">\n        <div class="re-ba">%s%s'
                     '<span class="re-linea"></span><span class="re-et p">%s</span><span class="re-et d">%s</span>'
                     '<input type="range" min="0" max="100" value="50" aria-label="%s: %s"></div>\n'
                     '        <figcaption><b>%s</b> · %s</figcaption>\n      </figure>\n'
                     % (immagine(it['prima'], UI('prima') + ': ' + it['titolo']), immagine(it['dopo'], UI('dopo') + ': ' + it['titolo'], cls='re-dopo'),
                        UI('prima'), UI('dopo'), html.escape(UI('cmp')), html.escape(it['titolo']), e(it['titolo']), e(it['testo'])))
        o.append('    </div>\n')
        if sec.get('video'):
            o.append('    <div class="re-ba-grid" style="margin-top:26px">\n')
            for nome, poster, tit in sec['video']:
                o.append('      <figure class="re-video" data-rv="up">%s<figcaption>%s</figcaption></figure>\n' % (video(nome, poster, tit), e(tit)))
            o.append('    </div>\n')
        o.append('    <p class="re-nota-img">%s</p>\n' % UI('nota'))
    elif t == 'gal':
        o.append('    <div class="re-gal">\n')
        for it in sec['items']:
            media = video(it['video'], it['img'], it['titolo']) if it.get('video') else immagine(it['img'], it.get('alt', it['titolo']))
            o.append('      <figure data-rv="up">%s<figcaption><b>%s</b><span>%s</span></figcaption></figure>\n' % (media, e(it['titolo']), e(it['testo'])))
        o.append('    </div>\n    <p class="re-nota-img">%s</p>\n' % UI('nota'))
    elif t == 'split':
        media = (video(sec['video'], sec['img'], sec['didascalia']) if sec.get('video') else immagine(sec['img'], sec['didascalia']))
        o.append('    <div class="re-split">\n      <figure class="re-video" data-rv="up">%s<figcaption>%s</figcaption></figure>\n      <div class="pg-testo" data-rv="up">\n%s      </div>\n    </div>\n'
                 % (media, e(sec['didascalia']), ''.join('        <p>%s</p>\n' % p for p in sec['corpo'])))
    elif t == 'promesse':
        o.append('    <div class="re-promesse" data-rv="up">\n%s    </div>\n'
                 % ''.join('      <div><b>%s</b><span>%s</span></div>\n' % (e(a), e(b)) for a, b in sec.get('corpo', PROM[CUR[0]])))
    o.append('  </div>\n</section>\n')
    return ''.join(o)
P23._prev_hook = None
pb.sezione = lambda sec: sezione(sec) if sec.get('tipo') in ('ba', 'gal', 'split', 'promesse') else P23.sezione(sec, CUR[0])

def lingue(d, s):
    alt = LG.alt(d['key'])
    links = ''.join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (h, SITE, alt[l]) for l in LG.LINGUE for h in LG.CFG[l]['hl'])
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
    if lang in ('ro', 'sq', 'hr'):   # shell EN: i link relativi '../' puntano a /en/, non a /xx/
        s = re.sub(r'href="\.\./(?!\.\./)', 'href="/en/', s)
    if lang not in ('it', 'en'):
        s = s.replace('<a href="%s">Home</a>' % pb.HOME[lang], '<a href="%s">%s</a>' % (pb.HOME[lang], UI('home')), 1)
    bg = video(d['herovid'], d['hero'], d['ogtitle']) if d.get('herovid') else immagine(d['hero'], d.get('heroalt', d['ogtitle']), lazy=False)
    bg = bg.replace('preload="none"', 'preload="metadata"')
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
    s = s[:m.start(1)] + '\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n' + s[m.end(1):]
    return s

if __name__ == '__main__':
    import sys
    solo = sys.argv[1:]   # facoltativo: lingue da generare (es. en de)
    tutte = [d for D in DATI for d in getattr(D, 'PAGINE', [])]
    for d in tutte: d.setdefault('key', d['url'])
    n = 0
    for d in tutte:
        if solo and d['lang'] not in solo: continue
        CUR[0] = d['lang']; P23._cur_lang[0] = d['lang']; P23._cur_url[0] = d['url']
        p = P23.build(d)
        f = os.path.join(ROOT, p)
        s = post(d, lingue(d, open(f, encoding='utf-8').read()))
        open(f, 'w', encoding='utf-8').write(s); n += 1
    from collections import Counter
    print('pagine Real Estate generate:', n, dict(Counter(d['lang'] for d in tutte if not solo or d['lang'] in solo)))
