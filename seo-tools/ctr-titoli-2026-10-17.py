#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Titoli e description riscritti sulle query reali di Search Console
(ago-ott 2026) per le pagine gia' fra posizione 4 e 20. Idempotente."""
import os,re,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
M={
 "calendario-fiere-rimini":(
  "Fiere Rimini 2026–2027: calendario e date (Ecomondo, Sigep, Macfrut)",
  "Prossime fiere a Rimini Expo Centre: Ecomondo 3–6 novembre 2026, Sigep World 23–27 gennaio 2027, KEY, Macfrut e RiminiWellness. Date ufficiali, settori e stand chiavi in mano."),
 "stand-eicma":(
  "Stand EICMA 2026, 3–8 novembre: allestimento chiavi in mano | Danova Tech",
  "Stand per EICMA 2026 a Fiera Milano Rho (3–8 novembre): progetto 3D, grafica, impianti e montaggio in fiera. Valutiamo anche richieste urgenti. Risposta in 24 ore."),
 "agenzia-seo-milano":(
  "Agenzia SEO Milano: posizionamento su Google per aziende | Danova Tech",
  "Agenzia SEO per aziende di Milano e provincia, con uffici a Vermezzo con Zelo (MI): audit tecnico, contenuti, SEO locale e report mensili leggibili. Prezzo dichiarato, nessun vincolo."),
 "gestionale-palestra":(
  "Gestionale palestra con app per soci e prenotazione corsi | Danova Tech",None),
 "app-fidelizzazione-clienti":(
  "Software e app fidelizzazione clienti, fidelity card digitale | Danova Tech",None),
 "allestimenti-fieristici-vicenza":(
  "Stand fieristici Vicenza: progettazione e allestimento chiavi in mano",None),
 "allestimenti-fieristici-padova":(
  "Stand fieristici Padova: progettazione e allestimento chiavi in mano",None),
 "de/webagentur-suedtirol":(
  "Webagentur & SEO-Agentur Südtirol: zweisprachige Websites | Danova Tech",None),
}
def esc(s): return html.escape(s,quote=True)
for d,(t,ds) in M.items():
    p=d+"/index.html"; h=open(p,encoding="utf-8").read(); o=h
    old_t=html.unescape(re.search(r'<title>(.*?)</title>',h,re.S).group(1))
    if old_t!=t:
        for variant in {old_t,esc(old_t),html.escape(old_t,quote=False)}:
            h=h.replace(f"<title>{variant}</title>",f"<title>{esc(t)}</title>")
            h=h.replace(f'content="{variant}"',f'content="{esc(t)}"')
            h=re.sub(r'("(?:name|headline)":\s*)"'+re.escape(variant)+'"',lambda m:m.group(1)+'"'+t.replace('"','\\"')+'"',h)
    if ds:
        old_d=html.unescape(re.search(r'<meta name="description" content="([^"]*)"',h).group(1))
        for variant in {esc(old_d),html.escape(old_d,quote=False),old_d}:
            h=h.replace(f'content="{variant}"',f'content="{esc(ds)}"')
            h=re.sub(r'("description":\s*)"'+re.escape(variant)+'"',lambda m:m.group(1)+'"'+ds.replace('"','\\"')+'"',h)
    if h!=o: open(p,"w",encoding="utf-8").write(h); print("ok ",d)
    else: print("-- ",d)
