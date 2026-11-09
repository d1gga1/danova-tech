# -*- coding: utf-8 -*-
# 09/11/2026 - Search Console: "Duplicate, Google chose different canonical than user".
# Le pagine /video/<nome>/ avevano ~70 parole proprie e tutto il resto uguale tra loro
# (FAQ identiche, nota social ripetuta 2 volte, descrizione ripetuta 3 volte, descrizioni
# degli altri video nei "Video simili"). Google le raggruppava come copie.
# Questo script toglie i blocchi ripetuti. Da rilanciare dopo ogni build delle pagine video.
# Uso: python3 seo-tools/post-build-video-duplicati.py   (dalla cartella del sito)
import os, re, json, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
VD = os.path.join(ROOT, 'video')
NOTA = re.compile(r'\s*<p class="vd-nota"[^>]*>.*?</p>', re.S)
def sezione(s, sid):
    m = re.search(r'<section id="%s">.*?</section>' % sid, s, re.S)
    return m
def sostituisci(s, sid, fn):
    m = sezione(s, sid)
    if not m: return s
    return s[:m.start()] + fn(m.group(0)) + s[m.end():]
cambiate = 0
for d in sorted(os.listdir(VD)):
    p = os.path.join(VD, d, 'index.html')
    if not os.path.isfile(p): continue
    s = open(p, encoding='utf-8').read()
    if 'http-equiv="refresh"' in s: continue
    o = s
    # 1) video principale: via la descrizione nella didascalia (e' gia' il sottotitolo in apertura)
    s = sostituisci(s, 'video', lambda x: re.sub(r'(</b>)<span>[^<]*</span>(</figcaption>)', r'\1\2', x))
    # 2) nota social: una sola volta, sotto il video principale
    s = sostituisci(s, 'correlati', lambda x: NOTA.sub('', x))
    # 3) video simili: solo titolo, senza la descrizione (testo delle altre pagine)
    s = sostituisci(s, 'correlati', lambda x: re.sub(r'(</a></b>)<span>[^<]*</span>', r'\1', x))
    # 4) in breve: via il paragrafo che ripete la descrizione, resta la scheda dati
    s = sostituisci(s, 'in-breve', lambda x: re.sub(r'\s*<p>[^\n]*?Realizzato da <b>Danova Tech</b>[^\n]*?</p>', '', x, count=1))
    # 5) FAQ generiche uguali su tutte le pagine: via sezione e schema FAQPage
    m = re.search(r'\s*<section id="faq">.*?</section>', s, re.S)
    if m: s = s[:m.start()] + s[m.end():]
    def pulisci_ld(mm):
        try: data = json.loads(mm.group(2))
        except Exception: return mm.group(0)
        g = data.get('@graph') if isinstance(data, dict) else None
        if not g: return mm.group(0)
        n = [x for x in g if x.get('@type') != 'FAQPage']
        if len(n) == len(g): return mm.group(0)
        data['@graph'] = n
        return mm.group(1) + json.dumps(data, ensure_ascii=False, indent=2) + mm.group(3)
    s = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', pulisci_ld, s, flags=re.S)
    s = s.replace('href="#faq"', 'href="#contatti"') if 'id="faq"' not in s else s
    if s != o:
        open(p, 'w', encoding='utf-8').write(s); cambiate += 1
print('pagine video sistemate:', cambiate)
