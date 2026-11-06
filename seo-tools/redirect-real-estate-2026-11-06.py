#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""06/11/2026 - Redirect delle vecchie pagine Danova Real Estate verso danovacostruzioni.it.

Perche': il commit 6b7ef90b ha cancellato 536 pagine (IT, EN, DE, RO, SQ, HI) senza
redirect. Search Console le mostra ancora con impressioni: ora danno 404, e il valore
accumulato (link, storico) va perso. danovacostruzioni.it usa gli stessi percorsi, quindi
il redirect e' 1:1. GitHub Pages non fa 301: si usa lo stesso schema delle pagine stand
(meta refresh 0 + canonical + location.replace), che Google tratta come redirect permanente.

Elenco: pagine cancellate in 6b7ef90b (git), salvo quelle che nel frattempo esistono di nuovo.
Idempotente. Uso:  python3 seo-tools/redirect-real-estate-2026-11-06.py
"""
import os, subprocess, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
NEW = "https://danovacostruzioni.it/"
MAP = {"real-estate": "", "real-estate/chi-siamo": "chi-siamo/",
       "real-estate/domande-frequenti": "domande-frequenti/",
       "real-estate/esempi-di-intervento": "esempi-di-intervento/"}
LANG = {"de": "de", "en": "en", "ro": "ro", "sq": "sq", "hi": "hi"}

out = subprocess.run(["git", "show", "--name-status", "--format=", "6b7ef90b"],
                     capture_output=True, text=True, check=True).stdout
paths = sorted({l.split("\t")[1][:-len("/index.html")] for l in out.splitlines()
                if l.startswith("D\t") and l.endswith("/index.html")})
fatti = saltati = 0
for p in paths:
    f = os.path.join(p, "index.html")
    if os.path.exists(f) and 'http-equiv="refresh"' not in open(f, encoding="utf-8").read(800):
        saltati += 1; continue            # pagina tornata vera: non toccarla
    dest = NEW + MAP.get(p, p + "/")
    lang = LANG.get(p.split("/")[0], "it")
    u = html.escape(dest, quote=True)
    os.makedirs(p, exist_ok=True)
    open(f, "w", encoding="utf-8").write(
        '<!DOCTYPE html>\n<html lang="%s"><head><meta charset="utf-8">\n'
        '<title>Danova Costruzioni</title>\n'
        '<link rel="canonical" href="%s">\n'
        '<meta http-equiv="refresh" content="0; url=%s">\n'
        '<script>location.replace("%s"+location.hash)</script>\n'
        '</head><body>\n<p>Questa pagina si è spostata su <a href="%s">%s</a></p>\n'
        '</body></html>\n' % (lang, u, u, dest, u, u))
    fatti += 1
print("redirect scritti:", fatti, "| saltati (pagina vera presente):", saltati)
