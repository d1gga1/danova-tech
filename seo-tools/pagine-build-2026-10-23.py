# -*- coding: utf-8 -*-
"""23/10/2026 - Pagine nuove: sito web in 24 ore, video pubblicitari (hub + 5 pagine),
   app per ogni attivita', gestionale per ogni settore, in IT/EN/DE/FR/ES.
   Usa il motore di pagine-build.py e aggiunge:
   - sezione 'breve'  : box "In breve" (risposta diretta, pensata per Google e assistenti AI)
   - sezione 'video'  : galleria dei reel (assets/video/) con link a Instagram e TikTok + VideoObject
   - sezione 'link'   : griglia di pagine collegate con descrizione (hub per settore)
   - offerta con prezzo nel JSON-LD del servizio (svc['offer'])
   - hreflang tra le versioni linguistiche (d['alt']) e selettore lingua coerente
   Idempotente. Uso:  python3 seo-tools/pagine-build-2026-10-23.py"""
import os, re, json, html, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
pb = load('pb', 'pagine-build.py')
D = load('d2310', 'pagine-dati-2026-10-23.py')
pb.pd = D
SITE = pb.SITE; e = pb.e
VID = D.VIDEO

CSS = ('<style id="pg2310">'
 '.pg-breve{border:1px solid rgba(77,139,255,.35);background:rgba(30,107,255,.07);border-radius:18px;padding:24px 26px;margin-top:8px}'
 '.pg-breve p{margin:0 0 14px;font-size:1.06rem;line-height:1.6}'
 '.pg-breve dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px 22px;margin:0}'
 '.pg-breve dt{font-family:"JetBrains Mono",monospace;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;opacity:.7}'
 '.pg-breve dd{margin:3px 0 0;font-weight:600}'
 '.vd-grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));margin-top:8px}'
 '.vd-card{margin:0;border:1px solid rgba(255,255,255,.09);border-radius:18px;overflow:hidden;background:rgba(255,255,255,.03);display:flex;flex-direction:column}'
 '.vd-card video{display:block;width:100%;height:auto;aspect-ratio:9/16;background:#04060c;object-fit:cover}'
 '.vd-card figcaption{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;font-size:.9rem;line-height:1.45}'
 '.vd-card figcaption b{font-size:.98rem}'
 '.vd-card .vd-tag{font-family:"JetBrains Mono",monospace;font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;opacity:.7}'
 '.vd-social{display:flex;gap:8px;flex-wrap:wrap;margin-top:4px}'
 '.vd-social a{font-size:.78rem;padding:5px 10px;border-radius:99px;border:1px solid rgba(77,139,255,.45);text-decoration:none}'
 '.vd-social a:hover{background:rgba(30,107,255,.18)}'
 '.vd-nota{margin-top:18px;opacity:.85}'
 '.pg-link{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));margin-top:8px}'
 '.pg-link a{display:block;padding:16px 18px;border:1px solid rgba(255,255,255,.09);border-radius:14px;text-decoration:none;background:rgba(255,255,255,.03)}'
 '.pg-link a:hover{border-color:rgba(77,139,255,.6)}'
 '.pg-link b{display:block;margin-bottom:4px}.pg-link span{font-size:.88rem;opacity:.8;line-height:1.45}'
 '.vd-grid.uno{grid-template-columns:minmax(0,400px)}.vd-card figcaption b a{color:inherit;text-decoration:none}.vd-card figcaption b a:hover{text-decoration:underline}'
 '.pg-link-g{margin-top:26px}.pg-link-g h3{margin:0 0 10px;font-size:1.05rem}'
 '@media(max-width:640px){.vd-grid{grid-template-columns:1fr 1fr;gap:12px}.vd-card figcaption{padding:10px 11px 12px;font-size:.8rem}'
 '.vd-grid.uno{grid-template-columns:1fr}.vd-card figcaption>span:not(.vd-tag):not(.vd-social){display:none}.vd-card figcaption b{font-size:.86rem}.vd-social a{font-size:.7rem;padding:4px 8px}'
 '.pg-breve{padding:18px}}'
 '</style>')

_orig_sezione = pb.sezione
def sezione(sec, lang='it'):
    t = sec.get('tipo', 'testo')
    if t not in ('breve', 'video', 'link'):
        return _orig_sezione(sec)
    o = ['<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n' % sec['id']]
    if sec.get('eyebrow'):
        o.append('      <div class="eyebrow mono" data-scramble>%s</div>\n' % e(sec['eyebrow']))
    o.append('      <h2 class="title" data-rv="up">%s</h2>\n' % sec['h2'])
    if sec.get('lead'):
        o.append('      <p class="lead" data-rv="up">%s</p>\n' % e(sec['lead']))
    o.append('    </div>\n')
    if t == 'breve':
        o.append('    <div class="pg-breve" data-rv="up">\n      <p>%s</p>\n      <dl>\n' % sec['testo'])
        for k, v in sec['fatti']:
            o.append('        <div><dt>%s</dt><dd>%s</dd></div>\n' % (e(k), e(v)))
        o.append('      </dl>\n    </div>\n')
    elif t == 'video':
        L = D.VTX[lang]
        o.append('    <div class="vd-grid%s">\n' % (' uno' if sec.get('uno') else ''))
        for k in sec['video']:
            v = VID[k]
            soc = ''.join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (v[k2], L[k2]) for k2 in ('ig', 'tt') if v.get(k2))
            o.append('      <figure class="vd-card" data-rv="up">\n'
                     '        <video controls preload="none" playsinline width="540" height="960" data-poster="/assets/video/%s.jpg" title="%s">'
                     '<source src="/assets/video/%s.mp4" type="video/mp4"></video>\n'
                     '        <figcaption><span class="vd-tag">%s · %ss</span><b>%s</b><span>%s</span>%s</figcaption>\n      </figure>\n'
                     % (k, html.escape(v['nome'][lang]), k, e(v['tipo'][lang]), v['durata'],
                        ('<a href="%s">%s</a>' % (D.WATCH[k], e(v['nome'][lang]))) if (lang == 'it' and D.WATCH.get(k) and D.WATCH[k] != _cur_url[0]) else e(v['nome'][lang]),
                        e(v['desc'][lang]), ('\n          <span class="vd-social">%s</span>' % soc) if soc else ''))
        o.append('    </div>\n    <p class="vd-nota" data-rv="up">%s</p>\n' % L['nota'])
        o.append('    <script>(function(){var v=[].slice.call(document.querySelectorAll("video[data-poster]"));'
                 'function s(x){var p=x.getAttribute("data-poster");if(p){x.poster=p;x.removeAttribute("data-poster");}}'
                 'if(!("IntersectionObserver" in window)){v.forEach(s);return;}'
                 'var o=new IntersectionObserver(function(e){e.forEach(function(i){if(i.isIntersecting){s(i.target);o.unobserve(i.target);}});},{rootMargin:"600px"});'
                 'v.forEach(function(x){if(!x.__dp){x.__dp=1;o.observe(x);}});})();</script>\n')
    elif t == 'link':
        for gruppo, voci in sec['gruppi']:
            o.append('    <div class="pg-link-g" data-rv="up">\n')
            if gruppo: o.append('      <h3>%s</h3>\n' % e(gruppo))
            o.append('      <div class="pg-link">\n')
            for tit, href, desc in voci:
                o.append('        <a href="%s"><b>%s</b><span>%s</span></a>\n' % (href, e(tit), e(desc)))
            o.append('      </div>\n    </div>\n')
    o.append('  </div>\n</section>\n')
    return ''.join(o)

_cur_lang = ['it']; _cur_url = ['']
pb.sezione = lambda sec: sezione(sec, _cur_lang[0])

def iso_dur(s):
    s = int(round(float(s))); return 'PT%dM%dS' % (s // 60, s % 60) if s >= 60 else 'PT%dS' % s

_orig_jsonld = pb.jsonld
def jsonld(d, org):
    g = json.loads(_orig_jsonld(d, org))
    u = SITE + d['url']; lang = d['lang']
    for n in g['@graph']:
        if n.get('@type') == 'Service':
            if d['svc'].get('offer'):
                of = d['svc']['offer']
                n['offers'] = {"@type": "Offer", "price": of['price'], "priceCurrency": "EUR",
                               "availability": "https://schema.org/InStock", "url": u,
                               "description": of['desc'], "seller": {"@id": SITE + "/#organization"}}
        if n.get('@type') == 'WebPage':
            n['speakable'] = {"@type": "SpeakableSpecification", "cssSelector": [".pg-hero h1", ".pg-breve p"]}
    vids = []
    for sec in d['sezioni']:
        if sec.get('tipo') == 'video':
            for k in sec['video']:
                v = VID[k]
                vids.append({"@type": "VideoObject", "@id": SITE + "/assets/video/%s.mp4#video" % k,
                    "name": v['nome'][lang], "description": v['desc'][lang],
                    "thumbnailUrl": [SITE + "/assets/video/%s.jpg" % k],
                    "contentUrl": SITE + "/assets/video/%s.mp4" % k,
                    "uploadDate": v['data'] + "T12:00:00+02:00", "duration": iso_dur(v['durata']),
                    "inLanguage": "it-IT", "width": 720, "height": 1280,
                    "creator": {"@id": SITE + "/#organization"}, "publisher": {"@id": SITE + "/#organization"},
                    "isFamilyFriendly": True, "url": SITE + D.WATCH.get(k, d['url']),
                    "keywords": v.get('kw', ''),
                    "sameAs": [x for x in (v.get('ig'), v.get('tt')) if x] or None})
    for x in vids:
        if x['sameAs'] is None: del x['sameAs']
    if vids:
        for n in g['@graph']:
            if n.get('@type') == 'WebPage':
                n['video'] = [{"@id": x['@id']} for x in vids]
                if d.get('videopage'): n['mainEntity'] = {"@id": SITE + "/assets/video/%s.mp4#video" % d['videopage']}
        g['@graph'].extend(vids)
    return json.dumps(g, ensure_ascii=False, indent=2)
pb.jsonld = jsonld

def lingue(d, s):
    alt = d.get('alt') or {d['lang']: d['url']}
    order = [l for l in ('it', 'en', 'de', 'fr', 'es') if l in alt]
    xdef = alt.get('it') or alt.get('en') or d['url']
    links = ''.join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (l, SITE, alt[l]) for l in order)
    links += '<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, xdef)
    s = re.sub(r'<link rel="alternate" hreflang="[a-z]{2}".*?hreflang="x-default" href="[^"]*">',
               lambda _: links, s, count=1, flags=re.S)
    def sw(c):
        return ''.join(c + '<a href="%s" hreflang="%s"%s>%s</a>' % (alt[l], l, ' aria-current="page"' if l == d['lang'] else '', l.upper())
                       for l in order)
    s = re.sub(r'(<span class="lang-links">)(.*?)(</span>)', lambda m: m.group(1) + sw('\n        ') + '\n      ' + m.group(3), s, count=1, flags=re.S)
    s = re.sub(r'(<div class="mob-lang-links">)(.*?)(</div>)', lambda m: m.group(1) + sw('\n    ') + '\n  ' + m.group(3), s, count=1, flags=re.S)
    # i donatori de/fr/es sono pagine citta' con noindex (17/10): le pagine nuove vanno indicizzate
    s = re.sub(r'<meta name="robots" content="[^"]*">',
               '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">', s, count=1)
    if 'id="pg2310"' not in s:
        s = s.replace('</head><body>', CSS + '</head><body>', 1)
    if d.get('ogimg'):
        s = re.sub(r'(<meta property="og:image" content=")[^"]*(")', lambda m: m.group(1) + SITE + d['ogimg'] + m.group(2), s, count=1)
        s = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', lambda m: m.group(1) + SITE + d['ogimg'] + m.group(2), s, count=1)
    return s

def build(d):
    """Come pb.build, ma corregge i percorsi relativi solo per la differenza di profondita'
       fra pagina e donatore (pb.build assume il donatore a 1 livello: errato per en/de/fr/es)."""
    lv_page = d['url'].strip('/').count('/') + 1
    lv_donor = pb.DONOR[d['lang']].count('/')          # 'en/x/index.html' -> 2
    if not (lv_page == 2 and lv_donor == 2):
        return pb.build(d)
    # stessa profondita' del donatore: disattiva la correzione dei percorsi di pb.build
    class _Re:
        def __getattr__(self, k): return getattr(re, k)
        def sub(self, pat, rep, s, *a, **k):
            if isinstance(pat, str) and '(?!\\.\\./)' in pat: return s
            return re.sub(pat, rep, s, *a, **k)
    pb.re = _Re()
    try:
        return pb.build(d)
    finally:
        pb.re = re

def hreflang_mancanti(d, s):
    if re.search(r'<link rel="alternate" hreflang=', s): return s
    alt = d.get('alt') or {d['lang']: d['url']}
    order = [l for l in ('it', 'en', 'de', 'fr', 'es') if l in alt]
    xdef = alt.get('it') or alt.get('en') or d['url']
    links = ''.join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (l, SITE, alt[l]) for l in order)
    links += '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (SITE, xdef)
    return re.sub(r'(<link rel="canonical" href="[^"]*">\n?)', lambda m: m.group(1) + links, s, count=1)

if __name__ == '__main__':
    for d in D.PAGINE:
        _cur_lang[0] = d['lang']; _cur_url[0] = d['url']
        p = build(d)
        f = os.path.join(pb.ROOT, p)
        s = lingue(d, hreflang_mancanti(d, open(f, encoding='utf-8').read()))
        open(f, 'w', encoding='utf-8').write(s)
        print('%-3s  %-50s  %6d byte' % (d['lang'], d['url'], len(s)))
