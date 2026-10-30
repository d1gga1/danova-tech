# -*- coding: utf-8 -*-
"""30/10/2026 (b) - Le 11 nuove lavorazioni nella pagina principale Real Estate, nel footer IT e dalla pagina porte.
   NESSUN PREZZO PUBBLICATO. Sostituzioni esatte, idempotente."""
import os, sys
H = os.path.dirname(os.path.abspath(__file__))
def rep(fn, pairs):
    p = os.path.join(H, fn); s = open(p, encoding='utf-8').read(); s0 = s
    for a, b in pairs:
        if b in s: continue
        if s.count(a) != 1: sys.exit('%s: testo non trovato o ripetuto (%d): %s' % (fn, s.count(a), a[:80]))
        s = s.replace(a, b)
    if s != s0: open(p, 'w', encoding='utf-8').write(s); print('aggiornato', fn)
    else: print('invariato', fn)

# ---- pagina principale: nuovo gruppo con le 11 lavorazioni
rep('real-estate-dati-1.py', [(
 '                ("Pavimenti e serramenti", "/pavimenti-e-serramenti/", "Parquet, gres, resine, finestre e portefinestre.")]),\n              ("Arredo", [',
 '                ("Pavimenti e serramenti", "/pavimenti-e-serramenti/", "Parquet, gres, resine, finestre e portefinestre.")]),\n'
 '              ("Superfici, strutture e risanamento", [\n'
 '                ("Microcemento", "/microcemento/", "Pavimenti, bagni e pareti continui, senza fughe, anche sopra le vecchie piastrelle."),\n'
 '                ("Pavimenti in resina", "/pavimenti-in-resina/", "Resine per case, negozi, garage e capannoni: lisce, resistenti, facili da pulire."),\n'
 '                ("Stucco veneziano e decorazioni", "/stucco-veneziano-e-decorazioni/", "Marmorino, grassello e finiture a calce per pareti di pregio."),\n'
 '                ("Pergole e tettoie", "/pergole-e-tettoie/", "In legno, alluminio o bioclimatiche, con pratiche e permessi."),\n'
 '                ("Porte blindate", "/porte-blindate/", "Fornitura e posa certificata, anche sul telaio esistente."),\n'
 '                ("Soppalchi", "/soppalchi/", "Metri in più in legno, acciaio o laterocemento, con calcoli strutturali."),\n'
 '                ("Scale interne", "/scale-interne/", "Scale a giorno, a chiocciola o in muratura, su misura."),\n'
 '                ("Cerchiatura muro portante", "/cerchiatura-muro-portante/", "Aprire o allargare un passaggio in sicurezza, con progetto e deposito."),\n'
 '                ("Umidità di risalita", "/umidita-di-risalita/", "Diagnosi e risanamento di muri umidi, salnitro e intonaci che si staccano."),\n'
 '                ("Rimozione amianto ed eternit", "/rimozione-amianto-eternit/", "Bonifica con ditta autorizzata e nuovo tetto, pratiche ASL comprese."),\n'
 '                ("Sanatoria edilizia", "/sanatoria-edilizia/", "Difformità, Salva Casa e regolarizzazioni prima di vendere o ristrutturare.")]),\n'
 '              ("Arredo", [')])

# ---- footer IT: le 7 lavorazioni che mancavano
rep('real-estate-chrome.py', [(
 "('/pergole-e-tettoie/', 'Pergole e tettoie'), ('/trasformazione-vasca-in-doccia/',",
 "('/pergole-e-tettoie/', 'Pergole e tettoie'), ('/soppalchi/', 'Soppalchi'), ('/scale-interne/', 'Scale interne'), ('/cerchiatura-muro-portante/', 'Cerchiatura muro portante'), ('/umidita-di-risalita/', 'Umidità di risalita'), ('/rimozione-amianto-eternit/', 'Rimozione amianto ed eternit'), ('/sanatoria-edilizia/', 'Sanatoria edilizia'), ('/stucco-veneziano-e-decorazioni/', 'Stucco veneziano'), ('/trasformazione-vasca-in-doccia/',")])

# ---- pagina porte: rimando alla pagina dedicata alle porte blindate
rep('real-estate-dati-2.py', [(
 ' altri=[("Porte REI tagliafuoco", "/porte-rei-tagliafuoco/"), ("Cartongesso e controsoffitti", "/cartongesso-e-controsoffitti/"),',
 ' altri=[("Porte blindate: la pagina dedicata", "/porte-blindate/"), ("Porte REI tagliafuoco", "/porte-rei-tagliafuoco/"), ("Cartongesso e controsoffitti", "/cartongesso-e-controsoffitti/"),')])
