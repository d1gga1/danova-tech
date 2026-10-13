# -*- coding: utf-8 -*-
"""Mockup illustrativi (siti, app, gestionali, SEO, campagne, guide) sotto l'hero di ogni pagina.
   Dati: seo-tools/immagini-sito.json  {path: {file, alt, cap, lang}}   Immagini: assets/img/mockup/
   Uso: python3 seo-tools/immagini-sito.py   (idempotente: rilanciarlo dopo qualsiasi rigenerazione di pagine)"""
import os, re, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://danova-tech.com'; DIR = '/assets/img/mockup/'; W, HH = 1600, 1063
A, B = '<!--mk-foto-->', '<!--/mk-foto-->'
E = lambda s: H.escape(s, quote=True)
CREDIT = {'it': 'Mockup illustrativo Danova Tech', 'en': 'Danova Tech illustrative mockup', 'de': 'Illustratives Mockup von Danova Tech', 'fr': 'Maquette illustrative Danova Tech', 'es': 'Maqueta ilustrativa de Danova Tech'}
MAP = json.load(open(os.path.join(ROOT, 'seo-tools', 'immagini-sito.json'), encoding='utf-8'))

def url(f, kind=''):
    return f'{SITE}{DIR}og/{f}.jpg' if kind == 'og' else f'{SITE}{DIR}{f}{kind}.webp'

def figure(f, alt, cap):
    return (f'{A}<section class="fr-foto-sec"><div class="wrap"><figure class="fr-foto mk" data-rv="up">'
            f'<img src="{DIR}{f}.webp" srcset="{DIR}{f}-800.webp 800w, {DIR}{f}.webp 1600w" '
            f'sizes="(max-width: 1240px) calc(100vw - 44px), 1196px" width="{W}" height="{HH}" alt="{E(alt)}" decoding="async">'
            f'<figcaption>{E(cap)}</figcaption></figure></div></section>{B}\n')

def inject(s, path):
    d = MAP.get(path)
    if not d: return s
    f, alt, cap, lang = d['file'], d['alt'], d['cap'], d['lang'][:2]
    s = re.sub(re.escape(A) + r'.*?' + re.escape(B) + r'\n?', '', s, flags=re.S)
    if '/assets/img/stand/' in s: return s          # pagine fiere: hanno gia' il render dello stand
    m = re.search(r'<section class="pg-hero">.*?</section>\n?', s, re.S)
    if not m: return s
    s = s[:m.end()] + figure(f, alt, cap) + s[m.end():]
    og = url(f, 'og')
    s = re.sub(r'(<meta property="og:image" content=")[^"]*(">)', lambda x: x.group(1) + og + x.group(2), s)
    s = re.sub(r'(<meta name="twitter:image" content=")[^"]*(">)', lambda x: x.group(1) + og + x.group(2), s)
    s = re.sub(r'<meta property="og:image:alt" content="[^"]*">\n', '', s)
    if '<meta property="og:image:height"' in s:
        s = re.sub(r'(<meta property="og:image:height" content="[^"]*">\n)', lambda x: x.group(1) + f'<meta property="og:image:alt" content="{E(alt)}">\n', s, 1)
    s = re.sub(r'(<meta property="og:image:width" content=")[^"]*(">)', r'\g<1>1200\2', s)
    s = re.sub(r'(<meta property="og:image:height" content=")[^"]*(">)', r'\g<1>630\2', s)
    io = {"@type": "ImageObject", "@id": url(f) + "#img", "url": url(f), "contentUrl": url(f), "width": W, "height": HH, "caption": cap, "description": alt,
          "inLanguage": d['lang'], "creditText": CREDIT.get(lang, CREDIT['en']), "copyrightNotice": "© Danova Tech", "creator": {"@id": SITE + "/#organization"}, "thumbnailUrl": url(f, '-800')}
    def fix(m):
        try: g = json.loads(m.group(2))
        except ValueError: return m.group(0)
        nodes = g.get('@graph') if isinstance(g, dict) and '@graph' in g else None
        if nodes is None: return m.group(0)
        nodes = [n for n in nodes if not (n.get('@type') == 'ImageObject' and str(n.get('@id', '')).startswith(SITE + DIR))]
        for n in nodes:
            t = n.get('@type'); tt = t if isinstance(t, list) else [t]
            if any(x in ('WebPage', 'CollectionPage', 'AboutPage', 'ContactPage', 'FAQPage') for x in tt) and 'WebPage' in tt or any(x in ('CollectionPage', 'AboutPage', 'ContactPage') for x in tt):
                n['primaryImageOfPage'] = {"@id": io['@id']}; n['image'] = {"@id": io['@id']}
            if any(x in ('Service', 'Article', 'BlogPosting', 'HowTo', 'TechArticle') for x in tt):
                n['image'] = {"@id": io['@id']}
        nodes.append(io); g['@graph'] = nodes
        return m.group(1) + '\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n' + m.group(3)
    s = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', fix, s, count=1, flags=re.S)
    return s

if __name__ == '__main__':
    ok = 0; miss = []
    for p in sorted(MAP):
        fn = os.path.join(ROOT, p.strip('/'), 'index.html')
        if not os.path.exists(fn): miss.append(p); continue
        a = open(fn, encoding='utf-8').read(); b = inject(a, p)
        if b != a: open(fn, 'w', encoding='utf-8').write(b); ok += 1
    print('pagine aggiornate:', ok, 'di', len(MAP), '· mancanti:', miss)
