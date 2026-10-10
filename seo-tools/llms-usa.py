# -*- coding: utf-8 -*-
"""Rigenera la sezione USA di llms.txt dai file dati. Idempotente.
   Uso: python3 seo-tools/llms-usa.py"""
import os, re, importlib.util as u
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def L(f):
    s = u.spec_from_file_location(f, os.path.join(ROOT, 'seo-tools', f)); m = u.module_from_spec(s); s.loader.exec_module(m); return m
a, b, c = L('pagine-dati-usa.py'), L('pagine-dati-usa-2.py'), L('pagine-dati-usa-es.py')
p = os.path.join(ROOT, 'llms.txt'); h = open(p, encoding='utf-8').read()
h = re.sub(r'\n### English \(United States\).*?<!-- /usa -->\n', '\n', h, flags=re.S)
t = lambda d: d['title'].replace(' | Danova Tech', '')
riga = lambda d: '- %s: https://danova-tech.com%s' % (t(d), d['url'])
naz = lambda d: d['url'] == '/en/united-states/' or d['url'].endswith('-usa/')
extra = set(x[1] for x in a.EXTRA)
R = ['', '### English (United States) — websites, apps and custom software',
     "Danova Tech works remotely, in English and Spanish, with US companies. Fixed prices in writing, sites built to WCAG 2.1 AA, code and domain in the client's name. Italy is 6 hours ahead of US Eastern time, 9 of Pacific.",
     '', 'Hub and national services:'] + [riga(d) for d in a.PAGINE if naz(d)]
R += ['', 'Website design by city:'] + [riga(d) for d in a.PAGINE if d['url'].startswith('/en/web-design-') and not naz(d)]
R += ['', 'App and software development by city:'] + [riga(d) for d in a.PAGINE if d['url'].startswith('/en/software-development-') and not naz(d)]
R += ['', 'Specific services:'] + [riga(d) for d in b.PAGINE if d['url'] in extra]
R += ['', 'Industries:'] + [riga(d) for d in b.PAGINE if not d.get('guida') and d['url'] not in extra]
R += ['', 'Guides (cost and US compliance):'] + [riga(d) for d in b.PAGINE if d.get('guida')]
R += ['', 'Español (Estados Unidos, mercado hispano):'] + [riga(d) for d in c.PAGINE]
R.append('<!-- /usa -->')
h = h.replace('- All services: https://danova-tech.com/en/services/\n', '- All services: https://danova-tech.com/en/services/\n' + '\n'.join(R) + '\n', 1)
open(p, 'w', encoding='utf-8').write(h)
print('llms.txt: sezione USA con', sum(1 for r in R if r.startswith('- ')), 'pagine')
