# -*- coding: utf-8 -*-
"""Aggiunge i link alle pagine USA nella colonna "Markets" del footer di tutte
   le pagine inglesi (/en/...). Idempotente: si puo' rilanciare.
   Uso:  python3 seo-tools/patch-footer-usa.py"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINKS = [("/en/united-states/", "Web &amp; software for US businesses"),
         ("/en/web-design-new-york/", "Web design New York"),
         ("/en/web-design-los-angeles/", "Web design Los Angeles"),
         ("/en/web-design-chicago/", "Web design Chicago"),
         ("/en/software-development-company-usa/", "Software development USA"),
         ("/en/mobile-app-development-company-usa/", "App development USA")]
MARK = '<!-- usa -->'
blocco = MARK + ''.join('\n        <li><a href="%s">%s</a></li>' % l for l in LINKS) + '\n        <!-- /usa -->'
n = 0
for dp, dn, fn in os.walk(os.path.join(ROOT, 'en')):
    for f in fn:
        if f != 'index.html': continue
        p = os.path.join(dp, f); h = open(p, encoding='utf-8').read()
        h2 = re.sub(r'\s*<!-- usa -->.*?<!-- /usa -->', '', h, flags=re.S)
        h2 = re.sub(r'(<h5>Markets</h5><ul>)', lambda m: m.group(1) + '\n        ' + blocco, h2, count=1)
        if h2 != h:
            open(p, 'w', encoding='utf-8').write(h2); n += 1
print('footer aggiornato in', n, 'pagine')

# La home inglese non ha la colonna "Markets": la aggiungiamo dopo "Services".
p = os.path.join(ROOT, 'en', 'index.html'); h = open(p, encoding='utf-8').read()
if '<h5>Markets</h5>' not in h:
    col = ('\n      <div><h5>Markets</h5><ul>\n        ' + blocco +
           '\n        <li><a href="/en/web-design-agency-uk/">Web design agency UK</a></li>'
           '\n        <li><a href="/en/software-development-company-uk/">Software development company UK</a></li>'
           '\n        <li><a href="/en/web-design-agency-london/">Web design agency London</a></li>'
           '\n      </ul></div>')
    h = re.sub(r'(<div><h5 data-i18n="footer.h1">Services</h5>.*?</ul></div>)', lambda m: m.group(1) + col, h, count=1, flags=re.S)
    open(p, 'w', encoding='utf-8').write(h); print('colonna Markets aggiunta alla home inglese')
