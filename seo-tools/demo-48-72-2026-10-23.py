# -*- coding: utf-8 -*-
"""23/10/2026 - Il titolare conferma: demo funzionante di APP e GESTIONALI in 48-72 ore (non piu' 'meno di 24 ore').
   Restano invariate le promesse sui SITI (bozza del sito in 24 ore, sito Essenziale online in 24 ore).
   Applica sostituzioni precise a pagine HTML, file dati del generatore (seo-tools/*.py) e testi per le AI.
   Idempotente. Uso: python3 seo-tools/demo-48-72-2026-10-23.py"""
import os, re, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SUB = [
 ('una demo funzionante arriva in meno di 24 ore', 'una demo funzionante arriva in 48-72 ore'),
 ('Una demo funzionante arriva in meno di 24 ore', 'Una demo funzionante arriva in 48-72 ore'),
 ('in meno di 24 ore vi mostriamo una demo funzionante', 'in 48-72 ore vi mostriamo una demo funzionante'),
 ('e entro 24 ore vi mostriamo una demo funzionante', 'e in 48-72 ore vi mostriamo una demo funzionante'),
 ('Entro 24 ore vi mostriamo una demo funzionante', 'In 48-72 ore vi mostriamo una demo funzionante'),
 ('in meno di 24 ore vi mostriamo un prototipo', 'in 48-72 ore vi mostriamo un prototipo'),
 ('costruiamo un prototipo in meno di 24 ore', 'costruiamo un prototipo in 48-72 ore'),
 ('con una demo in meno di 24 ore', 'con una demo in 48-72 ore'),
 ('Demo in 24 ore, prima versione in 1-2 settimane', 'Demo in 48-72 ore, prima versione in 1-2 settimane'),
 ('Una demo funzionante sul vostro caso, entro il giorno dopo', 'Una demo funzionante sul vostro caso, in 48-72 ore'),
 ('Tempi: demo funzionante in meno di 24 ore e consegna in 1-2 settimane per siti, gestionali e app',
  'Tempi: bozza del sito in 24 ore (sito Essenziale online in 24 ore), demo funzionante di gestionali e app in 48-72 ore, consegna in 1-2 settimane per siti, gestionali e app'),
]
# titolo del passo "Demo in 24 ore" quando il testo che segue parla di demo funzionante (software, non siti)
RX = re.compile(r'Demo in 24 ore((?:</b><span>|",\s*"|\s+)(?:Una demo funzionante|In 48-72 ore vi mostriamo))')
SKIP = {'pagine-dati-2026-10-23.py', 'pagine-dati-2026-10-23-lingue.py', 'pagine-build-2026-10-23.py', 'demo-48-72-2026-10-23.py'}
files = [f for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True) if '/_to_delete/' not in f]
files += [f for f in glob.glob(os.path.join(R, 'seo-tools', '*.py')) if os.path.basename(f) not in SKIP]
files += [os.path.join(R, 'seo-tools', 'llms-intro.md')] + glob.glob(os.path.join(R, 'seo-tools', 'fiere-generatore', '*.py'))
n = 0; tot = 0
for f in files:
    s = open(f, encoding='utf-8').read(); s0 = s
    for a, b in SUB:
        tot += s.count(a); s = s.replace(a, b)
    s, k = RX.subn(r'Demo in 48-72 ore\1', s); tot += k
    if s != s0:
        open(f, 'w', encoding='utf-8').write(s); n += 1
print('file aggiornati: %d | sostituzioni: %d' % (n, tot))
