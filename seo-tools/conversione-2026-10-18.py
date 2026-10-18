# -*- coding: utf-8 -*-
"""18/10/2026 — Conversione: livelli del sito, garanzie, offerta a tempo, hero e CTA.
   Applica i testi di seo-tools/livelli-dati.py a:
     - le 5 homepage (HTML statico letto da Google + JSON-LD)
     - i 5 dizionari assets/js/i18n-*.js (testi applicati dal browser)
     - le 5 pagine prezzi (interventi mirati: NON rigenera la pagina, cosi'
       restano le modifiche fatte dopo il build: mockup, modulo, immagini)
     - assets/css/site.css (stili nuovi per le pagine interne)
   Idempotente: si puo' rilanciare dopo ogni modifica a livelli-dati.py.
   Uso:  python3 seo-tools/conversione-2026-10-18.py"""
import os, re, json, html, subprocess, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
def load(name, file):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, file))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
LV = load('livelli', 'livelli-dati.py')
PD = load('dati', 'prezzi-dati.py')          # gia' con i livelli applicati (vedi fondo di prezzi-dati.py)
D, NUM, SITE, URLP, LOC = PD.D, PD.NUM, PD.SITE, PD.URLP, PD.LOC
LANGS = ('it', 'en', 'de', 'fr', 'es')
HOMEF = {'it':'index.html','en':'en/index.html','de':'de/index.html','fr':'fr/index.html','es':'es/index.html'}
PRICEF = {l: os.path.join(PD.OUT[l], 'index.html') for l in LANGS}
FROM_KEYS = {'app_una', 'gest_da'} | LV.FROM_NEW
ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
         '<path d="M5 12h14M13 6l6 6-6 6"></path></svg>')
CHECK = ('<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4"><path d="M20 6 9 17l-5-5"></path></svg>')
def esc(s): return html.escape(s, quote=False)
def strip(s): return re.sub(r'<[^>]+>', '', s)
def icon(k): return ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                     'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % LV.ICONS[k])

# =================================================================== CSS
CSS_HOME = """/* conv-1018 */
.hero-trust{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;margin-top:22px;font-size:14px;color:var(--muted)}
.hero-trust b{color:var(--text);font-weight:600}
.hero-trust i{font-style:normal;color:var(--muted-2)}
.hero-trust .ht-st{color:#f5b301;letter-spacing:2px;font-size:13px}
.price-card.feat{border-color:rgba(77,139,255,.55);background:linear-gradient(150deg,rgba(30,107,255,.16),rgba(10,60,180,.05));box-shadow:0 24px 70px -34px rgba(30,107,255,.65)}
.price-badge{position:absolute;top:22px;right:22px;font-family:'JetBrains Mono',ui-monospace,monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;padding:6px 10px;border-radius:999px;background:var(--blue);color:#fff}
.price-for{font-size:14.5px;line-height:1.5;color:var(--muted);margin:-12px 0 18px}
.price-vat{margin-top:18px;font-size:13.5px;color:var(--muted-2)}
.price-sub{font-family:'Sora',sans-serif;font-size:1.05rem;font-weight:600;margin:46px 0 16px}
.price-mini{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr))}
.pm-card{display:block;background:var(--panel);border:1px solid var(--line);border-radius:var(--r-md);padding:22px 24px;color:inherit;text-decoration:none;transition:border-color .3s,background .3s}
.pm-card:hover{border-color:var(--line-strong);background:var(--panel-2)}
.pm-card .price-kind{margin-bottom:8px}
.pm-amt{font-family:'Sora',sans-serif;font-size:1.35rem;font-weight:700;letter-spacing:-.02em}
.pm-amt small{font-family:'Inter',sans-serif;font-size:13.5px;font-weight:500;color:var(--muted);margin-left:6px;letter-spacing:0}
.pm-card p{font-size:14px;line-height:1.5;color:var(--muted);margin-top:6px}
.gar-grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin-top:8px}
.gar{background:var(--panel);border:1px solid var(--line);border-radius:var(--r-md);padding:30px 28px}
.gar-ic{width:46px;height:46px;border-radius:12px;display:grid;place-items:center;background:rgba(30,107,255,.14);color:var(--blue-2);margin-bottom:18px}
.gar h3{font-family:'Sora',sans-serif;font-size:1.12rem;font-weight:700;letter-spacing:-.01em;margin-bottom:10px}
.gar p{color:var(--muted);font-size:15px;line-height:1.6}
.gar-offer{margin-top:24px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:18px;padding:24px 28px;border-radius:var(--r-md);border:1px dashed rgba(77,139,255,.5);background:rgba(30,107,255,.07)}
.gar-offer p{font-size:16px;line-height:1.55;max-width:640px}
.gar-offer b{color:var(--blue-2)}
@media (min-width:900px){.price-grid.tiers{grid-template-columns:repeat(3,1fr)}}
@media (max-width:760px){.price-grid.tiers .price-card.feat{order:-1}}
@media (max-width:560px){.price-badge{position:static;display:inline-block;align-self:flex-start;margin-bottom:14px}.gar-offer{padding:20px}}
@media (max-width:560px){.hero-trust i{display:none}.hero-trust{gap:4px 14px}}
/* /conv-1018 */
"""
CSS_SITE = """/* conv-1018 */
.price-for{font-size:14.5px;line-height:1.5;color:var(--muted);margin:-12px 0 18px}
.price-card.feat{box-shadow:0 24px 70px -34px rgba(30,107,255,.65);border-color:rgba(77,139,255,.55)}
.price-card.wide{grid-column:1/-1}
@media (max-width:560px){.price-badge{align-self:flex-start}}
.price-card.wide .price-list{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.gar-grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin-top:8px}
.gar{background:var(--panel);border:1px solid var(--line);border-radius:var(--r-md);padding:30px 28px}
.gar-ic{width:46px;height:46px;border-radius:12px;display:grid;place-items:center;background:rgba(30,107,255,.14);color:var(--blue-2);margin-bottom:18px}
.gar h3{font-family:'Sora',sans-serif;font-size:1.12rem;font-weight:700;letter-spacing:-.01em;margin-bottom:10px}
.gar p{color:var(--muted);font-size:15px;line-height:1.6}
.gar-offer{margin-top:24px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:18px;padding:24px 28px;border-radius:var(--r-md);border:1px dashed rgba(77,139,255,.5);background:rgba(30,107,255,.07)}
.gar-offer p{font-size:16px;line-height:1.55;max-width:640px;margin:0}
.gar-offer b{color:var(--blue-2)}
@media (min-width:900px){.price-grid.tiers{grid-template-columns:repeat(3,1fr)}}
@media (max-width:760px){.price-grid.tiers .price-card.feat{order:-1}}
/* /conv-1018 */
"""
def put_css(s, css, before='</style>'):
    if '/* conv-1018 */' in s:
        return re.sub(r'/\* conv-1018 \*/.*?/\* /conv-1018 \*/\n?', lambda m: css, s, count=1, flags=re.S)
    i = s.index(before); return s[:i] + css + s[i:]

# =================================================================== JS: analisi letterali
def skip_ws(s, i):
    while i < len(s):
        if s[i] in ' \t\r\n,': i += 1
        elif s.startswith('//', i): i = s.index('\n', i)
        elif s.startswith('/*', i): i = s.index('*/', i) + 2
        else: break
    return i
def skip_str(s, i):
    q = s[i]; j = i + 1
    while s[j] != q:
        j += 2 if s[j] == '\\' else 1
    return j + 1
def skip_val(s, i):
    c = s[i]
    if c in '\'"`': return skip_str(s, i)
    if c in '[{':
        d = 0; j = i
        while True:
            ch = s[j]
            if ch in '\'"`': j = skip_str(s, j); continue
            if ch in '[{': d += 1
            elif ch in ']}':
                d -= 1
                if d == 0: return j + 1
            j += 1
    j = i
    while s[j] not in ',}]\n': j += 1
    return j
def keys(s, i):
    assert s[i] == '{'; out = {}; j = i + 1
    while True:
        j = skip_ws(s, j)
        if s[j] == '}': return out
        if s[j] in '\'"': e = skip_str(s, j); k = s[j+1:e-1]; j = e
        else:
            m = re.compile(r'[A-Za-z_$][\w$]*').match(s, j); k = m.group(0); j = m.end()
        j = skip_ws(s, j); assert s[j] == ':', (k, s[j:j+30]); j = skip_ws(s, j + 1)
        e = skip_val(s, j); out[k] = (j, e); j = e
def span(s, root, path):
    i = root
    for n, k in enumerate(path):
        ks = keys(s, i)
        if k not in ks: return None
        a, b = ks[k]
        if n == len(path) - 1: return (a, b)
        i = a
def js(v, ind=''):
    if isinstance(v, str):
        return "'" + v.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n') + "'"
    if isinstance(v, (list, tuple)): return '[' + ','.join(js(x) for x in v) + ']'
    if isinstance(v, dict): return '{' + ','.join('%s:%s' % (k, js(x)) for k, x in v.items()) + '}'
    return json.dumps(v)
def node_eval(path, lang):
    code = ("global.window={};require(%s);process.stdout.write(JSON.stringify(window.I18N[%s]))"
            % (json.dumps(path), json.dumps(lang)))
    return json.loads(subprocess.run(['node', '-e', code], capture_output=True, text=True, check=True).stdout)

# =================================================================== testi comuni
def li(lst): return ''.join('<li>%s</li>' % esc(x) for x in lst)
def faq_list(old, first, add):
    qs = {q for q, _ in add}
    rest = [it for it in old if it[0] not in qs]
    rest[0] = list(first)
    return rest[:1] + [list(x) for x in add] + rest[1:]

def dict_prezzi(h):
    p = h['prezzi']; rows = []
    head = {k: p[k] for k in ('eyebrow', 'title', 'lead', 'more', 'note', 'oh')}
    rows.append('{' + js(head)[1:-1] + ',')
    for i, t in enumerate(p['tiers'], 1):
        o = {'k':t['k'], 'n':t['n'], 'w':t['w'], 'a':t['a'], 'u':t['u'], 'e':t['e'], 'l':li(t['l']), 'b':t['b']}
        if t.get('badge'): o['badge'] = t['badge']
        rows.append('    t%d:%s,' % (i, js(o)))
    for i, o in enumerate(p['others'], 1):
        rows.append('    o%d:%s,' % (i, js({k: o[k] for k in ('k', 'a', 'u', 'e')})))
    rows[-1] = rows[-1].rstrip(',')
    return '\n'.join(rows) + '\n  }'
def dict_garanzie(h):
    g = h['garanzie']
    o = {'eyebrow':g['eyebrow'], 'title':g['title'], 'lead':g['lead']}
    for i, (_, t, p) in enumerate(g['items'], 1): o['g%d' % i] = {'t':t, 'p':p}
    o['offer'] = g['offer']; o['btn'] = g['btn']
    return js(o)

# =================================================================== DIZIONARI
def patch_dict(lang):
    h = LV.HOME[lang]
    path = os.path.join(ROOT, 'assets/js/i18n-%s.js' % lang)
    s = open(path, encoding='utf-8').read()
    old = node_eval(path, lang)
    root = s.index('{', s.index('window.I18N.%s=' % lang))
    ops = []
    def rep(p, val):
        sp = span(s, root, p); assert sp, p; ops.append((sp[0], sp[1], val))
    hero = h['hero']
    for k in ('l1', 'l2', 'rot', 'sub', 'cta1', 'cta2'): rep(['hero', k], js(hero[k]))
    sp = span(s, root, ['hero', 'trust'])
    if sp: ops.append((sp[0], sp[1], js(hero['trust'])))
    else:
        a, b = span(s, root, ['hero', 'cta2']); ops.append((b, b, ', trust:' + js(hero['trust'])))
    rep(['prezzi'], dict_prezzi(h))
    sp = span(s, root, ['garanzie'])
    if sp: ops.append((sp[0], sp[1], dict_garanzie(h)))
    else:
        a, b = span(s, root, ['prezzi']); ops.append((b, b, ',\n  garanzie:' + dict_garanzie(h)))
    rep(['settori', 'lead'], js(h['settori_lead']))
    rep(['lavori', 'lead'], js(h['lavori_lead']))
    faq = faq_list(old['faq']['items'], h['faq_first'], h['faq_add'])
    rep(['faq', 'items'], '[\n' + ',\n'.join('      ' + js(x) for x in faq) + '\n    ]')
    rep(['cta', 'lead'], js(h['cta']['lead']))
    rep(['cta', 'list'], js(h['cta']['list']))
    rep(['cta', 'f', 'send'], js(h['cta']['send']))
    rep(['meta', 'desc'], js(h['meta_desc']))
    for a, b, v in sorted(ops, key=lambda x: x[0], reverse=True):
        s = s[:a] + v + s[b:]
    open(path, 'w', encoding='utf-8').write(s)
    return node_eval(path, lang)        # verifica: il file deve restare JavaScript valido

# =================================================================== HOMEPAGE
def match_div(s, i):
    """indice di fine del <div ...> che inizia in i"""
    d = 0; j = i
    for m in re.compile(r'<div\b|</div>').finditer(s, i):
        d += 1 if m.group(0) == '<div' else -1
        if d == 0: return m.end()
    raise ValueError('div non chiuso')

def home_prezzi(lang, h):
    p = h['prezzi']; u = URLP[lang]; o = []
    o.append('<section id="prezzi">\n  <div class="wrap">\n    <div class="sec-head">\n'
             '      <div class="eyebrow mono" data-scramble="" data-i18n="prezzi.eyebrow">%s</div>\n'
             '      <h2 class="title" data-rv="up" data-i18n-html="prezzi.title">%s</h2>\n'
             '      <p class="lead" data-rv="up" data-i18n="prezzi.lead">%s</p>\n    </div>\n'
             '    <div class="price-grid tiers">\n' % (esc(p['eyebrow']), p['title'], esc(p['lead'])))
    for i, t in enumerate(p['tiers'], 1):
        feat = bool(t.get('badge'))
        o.append('      <article class="price-card%s" data-tilt="" data-rv="blur" style="transition-delay: %dms;">\n'
                 % (' feat' if feat else '', (i - 1) * 90))
        if feat:
            o.append('        <span class="price-badge" data-i18n="prezzi.t%d.badge">%s</span>\n' % (i, esc(t['badge'])))
        o.append('        <span class="price-kind mono" data-i18n="prezzi.t{0}.k">{1}</span>\n'
                 '        <h3 data-i18n="prezzi.t{0}.n">{2}</h3>\n'
                 '        <p class="price-for" data-i18n="prezzi.t{0}.w">{3}</p>\n'
                 '        <p class="price-amt"><b data-i18n="prezzi.t{0}.a">{4}</b><span data-i18n="prezzi.t{0}.u">{5}</span></p>\n'
                 '        <p class="price-extra" data-i18n="prezzi.t{0}.e">{6}</p>\n'
                 '        <ul class="price-list" data-i18n-html="prezzi.t{0}.l">{7}</ul>\n'
                 .format(i, esc(t['k']), esc(t['n']), esc(t['w']), esc(t['a']), esc(t['u']), esc(t['e']), li(t['l'])))
        if feat:
            o.append('        <a href="#contatti" class="btn btn-p" data-mag=""><span class="sheen"></span>'
                     '<span class="lbl" data-i18n="prezzi.t%d.b">%s</span></a>\n' % (i, esc(t['b'])))
        else:
            o.append('        <a href="#contatti" class="btn btn-g" data-mag=""><span class="lbl" data-i18n="prezzi.t%d.b">%s</span></a>\n'
                     % (i, esc(t['b'])))
        o.append('      </article>\n')
    o.append('    </div>\n    <p class="price-vat" data-rv="up" data-i18n="prezzi.note">%s</p>\n'
             '    <h3 class="price-sub" data-rv="up" data-i18n="prezzi.oh">%s</h3>\n    <div class="price-mini">\n'
             % (esc(p['note']), esc(p['oh'])))
    for i, x in enumerate(p['others'], 1):
        href = ('href="%s" data-pricing' % u) if x['href'] == 'pricing' else 'href="%s"' % x['href']
        o.append('      <a class="pm-card" %s data-rv="up">\n'
                 '        <span class="price-kind mono" data-i18n="prezzi.o{0}.k">{1}</span>\n'
                 '        <div class="pm-amt"><span data-i18n="prezzi.o{0}.a">{2}</span><small data-i18n="prezzi.o{0}.u">{3}</small></div>\n'
                 '        <p data-i18n="prezzi.o{0}.e">{4}</p>\n      </a>\n'
                 .replace('%s', href, 1).format(i, esc(x['k']), esc(x['a']), esc(x['u']), esc(x['e'])))
    o.append('    </div>\n    <p class="price-foot" data-rv="up"><a href="%s" data-pricing class="btn btn-p" data-mag>'
             '<span class="sheen"></span><span class="lbl" data-i18n="prezzi.more">%s</span> %s</a></p>\n'
             '  </div>\n</section>' % (u, esc(p['more']), ARROW))
    return ''.join(o)

def home_garanzie(h):
    g = h['garanzie']; o = []
    o.append('<section id="garanzie">\n  <div class="wrap">\n    <div class="sec-head">\n'
             '      <div class="eyebrow mono" data-scramble="" data-i18n="garanzie.eyebrow">%s</div>\n'
             '      <h2 class="title" data-rv="up" data-i18n-html="garanzie.title">%s</h2>\n'
             '      <p class="lead" data-rv="up" data-i18n="garanzie.lead">%s</p>\n    </div>\n'
             '    <div class="gar-grid">\n' % (esc(g['eyebrow']), g['title'], esc(g['lead'])))
    for i, (ic, t, p) in enumerate(g['items'], 1):
        o.append('      <div class="gar" data-rv="up" style="transition-delay: %dms;"><div class="gar-ic">%s</div>'
                 '<h3 data-i18n="garanzie.g%d.t">%s</h3><p data-i18n="garanzie.g%d.p">%s</p></div>\n'
                 % ((i - 1) * 90, icon(ic), i, esc(t), i, esc(p)))
    o.append('    </div>\n    <div class="gar-offer" data-rv="up"><p data-i18n-html="garanzie.offer">%s</p>'
             '<a href="#contatti" class="btn btn-p" data-mag=""><span class="sheen"></span>'
             '<span class="lbl" data-i18n="garanzie.btn">%s</span> %s</a></div>\n  </div>\n</section>'
             % (g['offer'], esc(g['btn']), ARROW))
    return ''.join(o)

def offers_ld(lang, seller=False, url=None):
    out = []
    for name, desc, key, unit, dur in D[lang]['offers']:
        val = float(NUM[key])
        if unit == 'MON':
            ps = {"@type": "UnitPriceSpecification", "price": val, "priceCurrency": "EUR",
                  "valueAddedTaxIncluded": True, "unitCode": "MON"}
            if seller: ps["referenceQuantity"] = {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"}
            if dur: ps["billingDuration"] = dur; ps["billingIncrement"] = 1
        elif key in FROM_KEYS:
            ps = {"@type": "PriceSpecification", "minPrice": val, "priceCurrency": "EUR", "valueAddedTaxIncluded": True}
        else:
            ps = {"@type": "PriceSpecification", "price": val, "priceCurrency": "EUR", "valueAddedTaxIncluded": True}
        o = {"@type": "Offer", "name": name, "description": desc, "price": val, "priceCurrency": "EUR",
             "availability": "https://schema.org/InStock", "url": url or SITE + URLP[lang], "priceSpecification": ps}
        if seller:
            o["seller"] = {"@id": SITE + "/#organization"}
            o["itemOffered"] = {"@type": "Service", "name": name, "description": desc,
                                "provider": {"@id": SITE + "/#organization"}}
        else:
            o["itemOffered"] = {"@type": "Service", "name": name}
        out.append(o)
    return out

def set_meta(s, desc):
    for pat in (r'<meta name="description" content="[^"]*">', r'<meta property="og:description" content="[^"]*">',
                r'<meta name="twitter:description" content="[^"]*">'):
        tag = pat.split(' content')[0].replace('\\', '')
        s = re.sub(pat, lambda m: '%s content="%s">' % (tag, html.escape(desc)), s, count=1)
    return s

def patch_home(lang, t):
    h = LV.HOME[lang]; hero = h['hero']
    path = os.path.join(ROOT, HOMEF[lang]); s = open(path, encoding='utf-8').read()
    old_desc = re.search(r'<meta name="description" content="([^"]*)">', s).group(1)
    s = put_css(s, CSS_HOME)
    # --- hero
    s = re.sub(r'(<span class="ln" id="hl1">)[^<]*(</span>)', lambda m: m.group(1) + esc(hero['l1']) + m.group(2), s, count=1)
    s = re.sub(r'(<span class="ln" id="hl2">)[^<]*(</span>)', lambda m: m.group(1) + esc(hero['l2']) + m.group(2), s, count=1)
    s = re.sub(r'(<i class="spacer">)[^<]*(</i>)', lambda m: m.group(1) + esc(hero['rot'][0]) + m.group(2), s, count=1)
    s = re.sub(r'(<p class="hero-sub" id="heroSub">).*?(</p>)', lambda m: m.group(1) + hero['sub'] + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'(<span class="lbl" id="hcta1">)[^<]*(</span>)', lambda m: m.group(1) + esc(hero['cta1']) + m.group(2), s, count=1)
    s = re.sub(r'<a href="#[a-z]+"( class="btn btn-g"[^>]*><span class="lbl" id="hcta2">)[^<]*(</span>)',
               lambda m: '<a href="#prezzi"' + m.group(1) + esc(hero['cta2']) + m.group(2), s, count=1)
    trust = '<p class="hero-trust" id="heroTrust" data-i18n-html="hero.trust">%s</p>' % hero['trust']
    if 'id="heroTrust"' in s:
        s = re.sub(r'<p class="hero-trust" id="heroTrust".*?</p>', lambda m: trust, s, count=1, flags=re.S)
    else:
        i = s.index('<div class="hero-cta">'); j = match_div(s, i)
        s = s[:j] + '\n    ' + trust + s[j:]
    # --- prezzi + garanzie
    s = re.sub(r'<section id="prezzi">.*?</section>', lambda m: home_prezzi(lang, h), s, count=1, flags=re.S)
    gar = home_garanzie(h)
    if '<section id="garanzie">' in s:
        s = re.sub(r'<section id="garanzie">.*?</section>', lambda m: gar, s, count=1, flags=re.S)
    else:
        i = s.index('<!-- ===== SETTORI ===== -->')
        s = s[:i] + ('<!-- ===== GARANZIE ===== -->\n%s\n\n<div class="wrap"><div class="divider"></div></div>\n\n' % gar) + s[i:]
    # --- testi singoli
    for key, val in (('settori.lead', h['settori_lead']), ('lavori.lead', h['lavori_lead']), ('cta.lead', h['cta']['lead'])):
        s = re.sub(r'(<p [^>]*data-i18n="%s"[^>]*>).*?(</p>)' % re.escape(key),
                   lambda m: m.group(1) + esc(val) + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'(<span class="lbl" data-i18n="cta.f.send">)[^<]*(</span>)', lambda m: m.group(1) + esc(h['cta']['send']) + m.group(2), s, count=1)
    # --- FAQ e lista contatti: stesso markup che genera home.js
    i = s.index('<div class="faq" id="faqBox">'); j = match_div(s, i)
    faq = ''.join('\n    <details data-rv="up"><summary>%s<span class="pm"></span></summary>\n'
                  '      <div class="ans"><p>%s</p></div></details>' % (q, a) for q, a in t['faq']['items'])
    s = s[:i] + '<div class="faq" id="faqBox">' + faq + '</div>' + s[j:]
    i = s.index('<div class="cta-list" id="ctaList">'); j = match_div(s, i)
    s = s[:i] + '<div class="cta-list" id="ctaList">' + ''.join('<div>%s%s</div>' % (CHECK, x) for x in t['cta']['list']) + '</div>' + s[j:]
    # --- meta
    s = set_meta(s, h['meta_desc'])
    # --- versioni dei file JS: il browser deve scaricare i dizionari nuovi
    s = re.sub(r'(/assets/js/(?:i18n-[a-z]+|home)\.js)\?v=[A-Za-z0-9]+', lambda m: m.group(1) + '?v=' + VER, s)
    # --- dati strutturati: offerte e FAQ allineate al testo visibile
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    g = json.loads(m.group(1))
    for node in g['@graph']:
        if 'makesOffer' in node: node['makesOffer'] = offers_ld(lang)
        if node.get('@type') == 'FAQPage':
            node['mainEntity'] = [{"@type": "Question", "name": strip(q),
                                   "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in t['faq']['items']]
        if node.get('@type') == 'WebPage':
            if node.get('description') == html.unescape(old_desc): node['description'] = h['meta_desc']
            node['dateModified'] = '2026-10-18'
    s = s[:m.start()] + '<script type="application/ld+json">\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n</script>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)

# =================================================================== PAGINE PREZZI
def card_html(c, cta):
    cls = 'price-card' + (' feat' if c.get('feat') else '') + (' wide' if c.get('wide') else '')
    o = ['      <article class="%s" data-tilt data-rv="blur">\n' % cls]
    if c.get('badge'): o.append('        <span class="price-badge">%s</span>\n' % esc(c['badge']))
    o.append('        <span class="price-kind mono">%s</span>\n        <h3>%s</h3>\n' % (esc(c['kind']), esc(c['name'])))
    if c.get('for'): o.append('        <p class="price-for">%s</p>\n' % esc(c['for']))
    o.append('        <p class="price-amt"><b>%s</b><span>%s</span></p>\n' % (esc(c['amt']), esc(c['unit'])))
    if c.get('extra'): o.append('        <p class="price-extra">%s</p>\n' % esc(c['extra']))
    o.append('        <p class="price-note">%s</p>\n' % esc(c['note']))
    if c.get('tot'): o.append('        <p class="price-tot">%s</p>\n' % esc(c['tot']))
    o.append('        <ul class="price-list">%s</ul>\n' % li(c['list']))
    if c.get('feat'):
        o.append('        <a href="%s" class="btn btn-p" data-mag><span class="sheen"></span><span class="lbl">%s</span></a>\n' % (cta, esc(c['cta'])))
    else:
        o.append('        <a href="%s" class="btn btn-g" data-mag><span class="lbl">%s</span></a>\n' % (cta, esc(c['cta'])))
    o.append('      </article>\n')
    return ''.join(o)

def page_cat(cat, cta):
    return ('<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n'
            '      <div class="eyebrow mono" data-scramble>%s</div>\n'
            '      <h2 class="title" data-rv="up">%s</h2>\n'
            '      <p class="lead" data-rv="up">%s</p>\n    </div>\n'
            '    <div class="price-grid tiers">\n%s    </div>\n  </div>\n</section>'
            % (cat['id'], esc(cat['eyebrow']), cat['h2'], esc(cat['intro']),
               ''.join(card_html(c, cta) for c in cat['cards'])))

def page_gar(g, cta):
    ics = ['ok', 'time', 'lock']
    items = ''.join('      <div class="gar" data-rv="up"><div class="gar-ic">%s</div><h3>%s</h3><p>%s</p></div>\n'
                    % (icon(ics[i]), esc(t), esc(p)) for i, (t, p) in enumerate(g['items']))
    return ('<section id="garanzie">\n  <div class="wrap">\n    <div class="sec-head">\n'
            '      <div class="eyebrow mono" data-scramble>%s</div>\n'
            '      <h2 class="title" data-rv="up">%s</h2>\n'
            '      <p class="lead" data-rv="up">%s</p>\n    </div>\n'
            '    <div class="gar-grid">\n%s    </div>\n'
            '    <div class="gar-offer" data-rv="up"><p>%s</p><a href="%s" class="btn btn-p" data-mag>'
            '<span class="sheen"></span><span class="lbl">%s</span> %s</a></div>\n  </div>\n</section>'
            % (esc(g['eyebrow']), g['h2'], esc(g['lead']), items, g['offer'], cta, esc(g['btn']), ARROW))

def patch_price(lang):
    d = D[lang]; path = os.path.join(ROOT, PRICEF[lang]); s = open(path, encoding='utf-8').read()
    cat = d['cats'][0]
    sec = re.search(r'<section id="%s">.*?</section>' % re.escape(cat['id']), s, re.S)
    cta = re.search(r'<a href="([^"]+)" class="btn btn-[gp]" data-mag>', sec.group(0)).group(1)
    s = s[:sec.start()] + page_cat(cat, cta) + s[sec.end():]
    gar = page_gar(d['garanzie'], cta)
    if '<section id="garanzie">' in s:
        s = re.sub(r'<section id="garanzie">.*?</section>', lambda m: gar, s, count=1, flags=re.S)
    else:
        i = s.index('</section>', s.index('<section id="%s">' % cat['id'])) + len('</section>')
        s = s[:i] + '\n' + gar + s[i:]
    # tabella riassuntiva
    tb = d['tab']; c = [html.escape(x) for x in tb['cols']]; rows = []
    for name, desc, key, unit, dur in d['offers']:
        if unit == 'MON': f = tb['f_mese_min'] if dur else tb['f_mese']
        elif key in FROM_KEYS: f = tb['f_da']
        else: f = tb['f_una']
        rows.append('        <tr><th scope="row">%s</th><td data-label="%s">%s</td>'
                    '<td class="pt-amt" data-label="%s">%s</td><td data-label="%s">%s</td></tr>\n'
                    % (esc(name), c[1], esc(f), c[2], esc(tb['prezzi'][key]), c[3], esc(desc)))
    s = re.sub(r'(<table class="price-table">.*?<tbody>\n).*?(\s*</tbody>)', lambda m: m.group(1) + ''.join(rows).rstrip('\n') + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'(<p class="price-upd"[^>]*>).*?(</p>)', lambda m: m.group(1) + tb['upd'] + m.group(2), s, count=1, flags=re.S)
    # FAQ
    fs = s.index('<section id="faq">'); i = s.index('<div class="faq">', fs); j = match_div(s, i)
    faq = ''.join('\n      <details data-rv="up"><summary>%s<span class="pm"></span></summary>\n'
                  '        <div class="ans"><p>%s</p></div></details>' % (esc(q), esc(r)) for q, r in d['faq'])
    s = s[:i] + '<div class="faq">' + faq + '\n    </div>' + s[j:]
    # box finale
    cs = s.index('<section class="pg-cta">')
    s = s[:cs] + re.sub(r'(<p>).*?(</p>)', lambda m: m.group(1) + esc(d['ctabox']['p']) + m.group(2), s[cs:], count=1, flags=re.S)
    # testa
    s = re.sub(r'<meta name="description" content="[^"]*">', lambda m: '<meta name="description" content="%s">' % html.escape(d['desc']), s, count=1)
    for tag in ('<meta property="og:description"', '<meta name="twitter:description"'):
        s = re.sub(re.escape(tag) + r' content="[^"]*">', lambda m: '%s content="%s">' % (tag, html.escape(d['ogdesc'])), s, count=1)
    # JSON-LD
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    g = json.loads(m.group(1))
    for node in g['@graph']:
        tp = node.get('@type')
        if tp == 'Service' and 'offers' in node:
            node['offers'] = offers_ld(lang, seller=True, url=SITE + URLP[lang]); node['description'] = d['svc']['desc']
        elif tp == 'WebPage':
            node['description'] = d['desc']; node['dateModified'] = LV.AGGIORNATO
        elif tp == 'FAQPage':
            node['mainEntity'] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in d['faq']]
    s = s[:m.start()] + '<script type="application/ld+json">\n' + json.dumps(g, ensure_ascii=False, indent=2) + '\n</script>' + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)

VER = '20261018'

if __name__ == '__main__':
    # dizionari delle altre lingue caricati al cambio lingua: stessa versione
    p = os.path.join(ROOT, 'assets/js/home.js'); s = open(p, encoding='utf-8').read()
    s2 = re.sub(r"s\.src='/assets/js/i18n-'\+l\+'\.js(?:\?v=[A-Za-z0-9]+)?';", "s.src='/assets/js/i18n-'+l+'.js?v=%s';" % VER, s)
    if s2 != s: open(p, 'w', encoding='utf-8').write(s2)
    p = os.path.join(ROOT, 'assets/css/site.css'); s = open(p, encoding='utf-8').read()
    if '/* conv-1018 */' in s: s = put_css(s, CSS_SITE)
    else: s = s.rstrip('\n') + '\n' + CSS_SITE
    open(p, 'w', encoding='utf-8').write(s)
    for lang in LANGS:
        t = patch_dict(lang)
        patch_home(lang, t)
        patch_price(lang)
        print('%-3s  dizionario, home e listino aggiornati (FAQ home: %d, FAQ listino: %d)'
              % (lang, len(t['faq']['items']), len(D[lang]['faq'])))
