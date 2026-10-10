# -*- coding: utf-8 -*-
"""Legge i CSV del Keyword Planner (USA) e produce un riepilogo.
   Uso: python3 seo-tools/analizza-planner-usa.py"""
import os, csv, io, json, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keywords', 'planner-2026-10', 'usa')
def leggi(f):
    b = open(os.path.join(D, f), 'rb').read()
    t = b.decode('utf-16' if b[:2] in (b'\xff\xfe', b'\xfe\xff') else 'utf-8')
    righe = t.splitlines()[2:]
    r = csv.DictReader(io.StringIO('\n'.join(righe)), delimiter='\t')
    out = []
    for x in r:
        k = (x.get('Keyword') or '').strip()
        if not k: continue
        def num(c):
            try: return float((x.get(c) or '').replace(',', ''))
            except: return None
        out.append({'kw': k, 'vol': num('Avg. monthly searches') or 0, 'comp': x.get('Competition') or '',
                    'lo': num('Top of page bid (low range)'), 'hi': num('Top of page bid (high range)'),
                    'yoy': x.get('YoY change') or '', 'src': f})
    return out
ALL = {}
for f in sorted(os.listdir(D)):
    if not f.endswith('.csv'): continue
    for x in leggi(f):
        k = x['kw'].lower()
        if k not in ALL or x['vol'] > ALL[k]['vol']: ALL[k] = x
json.dump(ALL, open(os.path.join(D, 'tutte.json'), 'w'), ensure_ascii=False)
print('keyword uniche:', len(ALL))
