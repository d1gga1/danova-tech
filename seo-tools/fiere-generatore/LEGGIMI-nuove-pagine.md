# Pagine fiere aggiunte l'8 ottobre 2026

53 pagine nuove + collegamenti sulle esistenti. Tutto si rigenera con gli script qui sotto
(dalla cartella seo-tools/fiere-generatore), nell'ordine:

    python3 build_calendario.py     # /calendario-fiere/  (mappa + elenco + richiesta stand)
    python3 build_fiere.py          # /stand-<fiera>/     (20 pagine)
    python3 build_citta_nuove.py    # 15 nuove citta'
    python3 build_tipi.py           # 9 tipologie di stand
    python3 build_settori.py        # 6 settori
    python3 it_pages.py; python3 it_pillar.py; python3 it_citta.py   # pagine esistenti (ora collegate)
    python3 patch_link_nuove.py     # footer, home, llms.txt (idempotente)
    cd .. && python3 genera-sitemap.py && python3 genera-feed-e-llms.py

## Aggiornare le date delle fiere
Tutte le date stanno in `dati_calendario.py` (lista F). Per ogni fiera: inizio, fine, conf (1 = date
ufficiali, 0 = solo mese "da confermare"). Le fiere concluse spariscono da sole dal calendario
(anche lato browser), ma conviene aggiungere le nuove edizioni ogni 2-3 mesi e rilanciare gli script.
Il titolo delle pagine /stand-<fiera>/ contiene l'anno della prossima edizione: si aggiorna da solo
quando cambi le date.

## Esperienza dichiarata
Solo le 10 fiere con exp=True in `dati_pagine_fiere.py` dicono "abbiamo gia' allestito stand".
Se allestite stand in altre fiere, mettete exp=True anche li'.

## File di supporto
- assets/js/fiere-richiesta.js  modulo "Richiedi lo stand" -> WhatsApp (o email)
- assets/js/calendario-fiere.js filtri + mappa (Leaflet 1.9.4 da cdnjs, mappa CARTO dark, caricata solo quando visibile)
- assets/css/fiere.css          stili aggiunti in fondo
- lib.py: build() ha due parametri in piu' (wp_extra, scripts). Backup: *.bak-2026-10-08
