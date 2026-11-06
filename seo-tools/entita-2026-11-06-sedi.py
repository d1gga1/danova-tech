#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""06/11/2026 - Sedi di Danova Tech senza i magazzini.

I magazzini di Fontanelle (TV) e Trumello (PV) servivano agli allestimenti fieristici, ora
su danovastand.com. Su danova-tech.com (siti, software, AI, marketing) confondevano l'entita'
per Google e per gli assistenti AI. Restano: sede a Mansue' (TV), uffici a Trumello (PV) e
Vermezzo con Zelo (MI). NON tocca il caso cliente Pan.door.a (produttore di porte a Fontanelle).

Cambia: nodo schema Place "Magazzino di Fontanelle" (tolto), "Magazzino e uffici di Trumello"
(-> "Uffici di Trumello"), riga sedi del footer in IT/EN/DE/FR/ES, descrizioni e llms-intro.md.
Idempotente: rilanciare dopo ogni build. Poi rigenerare sitemap/feed/llms."""
import os, re, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
SUB = [
 (re.compile(r'\{\s*"@type": "Place",\s*"name": "Danova Tech — Magazzino di Fontanelle",\s*"address": \{[^{}]*\}\s*\},\s*'), ''),
 (re.compile(r'"Danova Tech — Magazzino e uffici di Trumello"'), '"Danova Tech — Uffici di Trumello"'),
 (re.compile(r'<li>Magazzini: Fontanelle \(TV\) · Trumello \(PV\)<br>'), '<li>'),
 (re.compile(r'<li>Warehouses: Fontanelle \(TV\) · Trumello \(PV\)<br>'), '<li>'),
 (re.compile(r'<li>Lager: Fontanelle \(TV\) · Trumello \(PV\)<br>'), '<li>'),
 (re.compile(r'<li>Almacenes: Fontanelle \(TV\) · Trumello \(PV\)<br>'), '<li>'),
 (re.compile(r'<li>Entrepôts: Fontanelle \(TV\) · Trumello \(PV\)<br>'), '<li>'),
 (re.compile(r'Magazzini: Fontanelle \(TV\) · Trumello \(PV\)\s*(<br>|·)?\s*'), ''),
 (re.compile(r', con magazzini a Fontanelle \(TV\) e Trumello \(PV\)'), ''),
 (re.compile(r'Sedi a Mansuè e Fontanelle \(TV\), Trumello'), 'Sedi a Mansuè (TV), Trumello'),
 (re.compile(r'<b>Produzione:</b> Fontanelle \(TV\) e Trumello \(PV\)<br>'), ''),
 (re.compile(r'<th scope="row">Produzione e uffici</th><td>Produzione a Fontanelle \(TV\) e Trumello \(PV\), uffici a '), '<th scope="row">Uffici</th><td>'),
 (re.compile(r'La produzione è a Fontanelle \(TV\) e a Trumello \(PV\), dove abbiamo anche degli uffici; in Lombardia siamo presenti anche con gli uffici di Vermezzo con Zelo \(MI\)'),
  'Gli uffici sono a Trumello (PV) e a Vermezzo con Zelo (MI)'),
 (re.compile(r'Il nostro magazzino di Fontanelle \(TV\) è a circa due ore da Verona'), 'La nostra sede di Mansuè (TV) è a circa due ore da Verona'),
]
tot = {}; files = 0
for f in glob.glob('**/index.html', recursive=True) + ['404.html']:
    if f.startswith(('_', 'seo-tools', 'social')): continue
    s0 = s = open(f, encoding='utf-8').read()
    for i, (rx, rep) in enumerate(SUB):
        s, n = rx.subn(rep, s); tot[i] = tot.get(i, 0) + n
    if s != s0: open(f, 'w', encoding='utf-8').write(s); files += 1
print('file cambiati:', files, '| sostituzioni per regola:', tot)
# testo d'apertura di llms.txt
p = 'seo-tools/llms-intro.md'; s0 = s = open(p, encoding='utf-8').read()
s = s.replace('> magazzini a Fontanelle (TV) e Trumello (PV), uffici a Trumello (PV) e Vermezzo con Zelo (MI).',
              '> uffici a Trumello (PV) e Vermezzo con Zelo (MI).')
s = s.replace('- **Magazzini**: Fontanelle (TV), Trumello (PV)\n', '')
s = s.replace('magazzini a Fontanelle (TV) e Trumello (PV), uffici a', 'uffici a')
if s != s0: open(p, 'w', encoding='utf-8').write(s); print('llms-intro.md aggiornato')
