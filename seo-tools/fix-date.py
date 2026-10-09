# -*- coding: utf-8 -*-
"""Aggiunge datePublished e dateModified ai dati strutturati di ogni pagina,
   prendendo le date vere dalla storia di git (prima e ultima modifica)."""
import os, re, json, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.join(os.path.dirname(ROOT), '_repo')
PAGINA = ('WebPage','CollectionPage','AboutPage','ContactPage','Article','BlogPosting','ItemList')

def date_git(rel):
    def run(args):
        try:
            return subprocess.run(['git','-C',REPO]+args, capture_output=True, text=True, timeout=20).stdout.strip()
        except Exception: return ''
    first = run(['log','--diff-filter=A','--format=%ad','--date=short','--','%s'%rel]).splitlines()
    last  = run(['log','-1','--format=%ad','--date=short','--','%s'%rel])
    return (first[-1] if first else None), (last or None)

def tipo(n):
    t = n.get('@type')
    ts = t if isinstance(t, list) else [t]
    return any(x in PAGINA for x in ts)

n_pub = n_mod = n_pag = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('seo-tools','assets','.git')]
    if 'index.html' not in fn: continue
    path = os.path.join(dp,'index.html')
    rel = os.path.relpath(path, ROOT).replace(os.sep,'/')
    s = open(path, encoding='utf-8').read()
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    if not m: continue
    g = json.loads(m.group(1))
    nodes = g.get('@graph') or [g]
    pub, mod = date_git(rel)
    if not mod: continue
    cambiato = False
    for nd in nodes:
        if not isinstance(nd, dict) or not tipo(nd): continue
        if 'datePublished' not in nd and pub:
            nd['datePublished'] = pub; n_pub += 1; cambiato = True
        if 'dateModified' not in nd:
            nd['dateModified'] = mod; n_mod += 1; cambiato = True
    if cambiato:
        s = s[:m.start()] + '<script type="application/ld+json">\n' + \
            json.dumps(g, ensure_ascii=False, indent=2) + '\n</script>' + s[m.end():]
        open(path,'w',encoding='utf-8').write(s); n_pag += 1
print('pagine aggiornate: %d | datePublished aggiunti: %d | dateModified aggiunti: %d' % (n_pag, n_pub, n_mod))
