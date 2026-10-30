# -*- coding: utf-8 -*-
"""30/10/2026 (d) - Pagine /ristrutturazioni-<citta>/ (IT) rese davvero locali con real-estate-citta-locali.py:
   sezione "Cosa ristrutturiamo a <citta>" (tipi di case), "Dove lavoriamo" (quartieri/frazioni e km da Mansue'), 2 FAQ locali in testa,
   meno FAQ generiche ripetute. Motivo: Search Console 30/10 - pagine citta' 'scansionate ma non indicizzate', testi uguali al 63-74%.
   Sostituzioni esatte, idempotente."""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(H, 'real-estate-dati-3.py'); s = open(p, encoding='utf-8').read(); s0 = s
PAIRS = [
 ('for nome, slug, area, hero, p1, p2, zone in CITTA:\n    P(url="/ristrutturazioni-%s/" % slug,',
  '_spL = _iuN.spec_from_file_location(\'reloc\', os.path.join(os.path.dirname(os.path.abspath(__file__)), \'real-estate-citta-locali.py\'))\n'
  '_LM = _iuN.module_from_spec(_spL); _spL.loader.exec_module(_LM); LOC = _LM.LOC  # 30/10/2026: contenuti locali\n'
  'for nome, slug, area, hero, p1, p2, zone in CITTA:\n    P(url="/ristrutturazioni-%s/" % slug,'),
 ('        "corpo": [p1, p2, "Zone in cui lavoriamo spesso: %s e gli altri comuni della zona (%s)." % (", ".join(zone), area)]},\n',
  '        "corpo": [p1, p2, "Zone in cui lavoriamo spesso: %s e gli altri comuni della zona (%s)." % (", ".join(zone), area)]},\n'
  '       *([{"id": "case", "tipo": "cards", "eyebrow": "Le case di %s" % nome, "h2": f"Cosa ristrutturiamo {G}a {nome}{_G}", "corpo": LOC[slug]["case"]},\n'
  '          {"id": "quartieri", "tipo": "testo", "eyebrow": "Quartieri e frazioni", "h2": f"Dove lavoriamo {G}a {nome}{_G}",\n'
  '           "corpo": [LOC[slug]["qtesto"], "Quartieri e frazioni: %s. La sede di Danova Real Estate è a Mansuè (Treviso), a circa %d km da %s." % (", ".join(LOC[slug]["quartieri"]), LOC[slug]["km"], nome)]}] if slug in LOC else []),\n'),
 ('      faq=[("Siete un’impresa edile di %s?" % nome,', '      faq=(LOC[slug]["faq"] if slug in LOC else []) + [("Siete un’impresa edile di %s?" % nome,'),
 ('] + FAQ_BASE[:3],\n      ctabox={"h2": "Un immobile da ristrutturare a %s?" % nome,', '] + FAQ_BASE[:1],\n      ctabox={"h2": "Un immobile da ristrutturare a %s?" % nome,'),
]
for a, b in PAIRS:
    if b in s: continue
    if s.count(a) != 1: sys.exit('testo non trovato o ripetuto (%d): %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
if s != s0: open(p, 'w', encoding='utf-8').write(s); print('aggiornato real-estate-dati-3.py')
else: print('invariato real-estate-dati-3.py')
