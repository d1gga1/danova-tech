# -*- coding: utf-8 -*-
"""Search Console, 15 ottobre 2026 - correzioni dati strutturati (idempotente, si puo' rilanciare dopo ogni build).
1) Metadati immagine: aggiunge 'license' e 'acquireLicensePage' a ogni ImageObject.
2) Eventi: aggiunge 'description' ai BusinessEvent che ne sono privi (pagine en / zh / zh-hant).
Uso: python3 seo-tools/schema-licenza-eventi.py"""
import os, re, json, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SITE = 'https://danova-tech.com'
LIC = {'it': (SITE + '/termini/#proprieta-intellettuale', SITE + '/contatti/'),
       'en': (SITE + '/en/terms/#intellectual-property', SITE + '/en/contact/')}
LANGS = ('en', 'de', 'fr', 'es', 'zh', 'zh-hant', 'ar', 'tr')
MESI_EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
CITY_ZH = {'Milan': '米兰', 'Bologna': '博洛尼亚', 'Verona': '维罗纳', 'Vicenza': '维琴察', 'Rimini': '里米尼', 'Parma': '帕尔马',
           'Florence': '佛罗伦萨', 'Riva del Garda': '加尔达湖里瓦', 'Pordenone': '波代诺内'}
CITY_HANT = {'Milan': '米蘭', 'Bologna': '博洛尼亞', 'Verona': '維羅納', 'Vicenza': '維琴察', 'Rimini': '里米尼', 'Parma': '帕爾馬',
             'Florence': '佛羅倫薩', 'Riva del Garda': '加爾達湖里瓦', 'Pordenone': '波代諾內'}

def lic(lang):
    return LIC['it'] if lang == 'it' else LIC['en']

def event_desc(ev, lang):
    n = ev.get('name', ''); loc = ev.get('location') or {}
    venue = loc.get('name', ''); city = (loc.get('address') or {}).get('addressLocality', '')
    s, e = ev.get('startDate', '')[:10], ev.get('endDate', '')[:10]
    y1, m1, d1 = (int(x) for x in s.split('-')); y2, m2, d2 = (int(x) for x in (e or s).split('-'))
    if lang in ('zh', 'zh-hant'):
        c = (CITY_HANT if lang == 'zh-hant' else CITY_ZH).get(city, city)
        end = f"{y2}年{m2}月{d2}日" if y2 != y1 else (f"{m2}月{d2}日" if m2 != m1 else f"{d2}日")
        if lang == 'zh-hant':
            return f"{n}將於{y1}年{m1}月{d1}日至{end}在義大利{c}的{venue}舉辦，是該行業的重要國際專業展會。"
        return f"{n}将于{y1}年{m1}月{d1}日至{end}在意大利{c}的{venue}举办，是该行业的重要国际专业展会。"
    if (y1, m1) == (y2, m2): dates = f"{d1}–{d2} {MESI_EN[m1-1]} {y1}" if d1 != d2 else f"{d1} {MESI_EN[m1-1]} {y1}"
    elif y1 == y2: dates = f"{d1} {MESI_EN[m1-1]} – {d2} {MESI_EN[m2-1]} {y1}"
    else: dates = f"{d1} {MESI_EN[m1-1]} {y1} – {d2} {MESI_EN[m2-1]} {y2}"
    return f"{n}: international trade fair held at {venue}, {city} (Italy), {dates}."

def walk(o, lang, cnt):
    if isinstance(o, dict):
        t = o.get('@type')
        if t == 'ImageObject':
            l, a = lic(o.get('inLanguage', lang) if o.get('inLanguage') in ('it',) else lang)
            if 'license' not in o: o['license'] = l; cnt['img'] += 1
            if 'acquireLicensePage' not in o: o['acquireLicensePage'] = a
            o.setdefault('creditText', 'Danova Tech'); o.setdefault('copyrightNotice', '© Danova Tech')
            o.setdefault('creator', {"@type": "Organization", "name": "Danova Tech", "url": SITE + "/"})
        if isinstance(t, str) and t.endswith('Event') and not o.get('description'):
            o['description'] = event_desc(o, lang); cnt['ev'] += 1
        for v in o.values(): walk(v, lang, cnt)
    elif isinstance(o, list):
        for v in o: walk(v, lang, cnt)

tot = {'img': 0, 'ev': 0, 'files': 0}
for f in glob.glob(os.path.join(R, '**', '*.html'), recursive=True):
    rel = os.path.relpath(f, R).replace('\\', '/')
    if rel.startswith('seo-tools/'): continue
    first = rel.split('/')[0]; lang = first if first in LANGS else 'it'
    s = open(f, encoding='utf-8').read(); cnt = {'img': 0, 'ev': 0}
    def fix(m):
        try: d = json.loads(m.group(2))
        except ValueError: return m.group(0)
        before = json.dumps(d, ensure_ascii=False, sort_keys=True)
        walk(d, lang, cnt)
        if json.dumps(d, ensure_ascii=False, sort_keys=True) == before: return m.group(0)
        raw = m.group(2); lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
        return m.group(1) + lead + json.dumps(d, ensure_ascii=False, indent=2) + trail + m.group(3)
    s2 = re.sub(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', fix, s, flags=re.S)
    if s2 != s:
        open(f, 'w', encoding='utf-8').write(s2); tot['files'] += 1; tot['img'] += cnt['img']; tot['ev'] += cnt['ev']
print(f"File aggiornati: {tot['files']} | ImageObject con licenza aggiunta: {tot['img']} | Eventi con descrizione aggiunta: {tot['ev']}")
