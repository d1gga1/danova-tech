# -*- coding: utf-8 -*-
"""30/10/2026 (c) - Collegamenti alle 15 nuove pagine di real-estate-dati-11.py: pagina principale Real Estate, /impresa-edile/,
   footer IT, llms.txt e pagine esistenti correlate. NESSUN PREZZO PUBBLICATO. Sostituzioni esatte, idempotente."""
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

G1 = ('              ("Strutture, impermeabilizzazioni ed esterni", [\n'
      '                ("Impermeabilizzazioni", "/impermeabilizzazioni/", "Docce, terrazzi, balconi e frontalini, tetti piani, fondazioni e cantine."),\n'
      '                ("Muffa e infiltrazioni", "/muffa-e-infiltrazioni/", "Troviamo da dove arriva l’umidità, la eliminiamo e ripristiniamo."),\n'
      '                ("Adeguamento sismico e consolidamento", "/adeguamento-sismico-e-consolidamento/", "Solai, murature, cordoli, fondazioni e vespai, con sismabonus."),\n'
      '                ("Demolizioni e sgomberi", "/demolizioni-e-sgomberi/", "Demolizioni interne e di fabbricati, sgomberi, smaltimento a norma."),\n'
      '                ("Costruzione case e ampliamenti", "/costruzione-case-e-ampliamenti/", "Case nuove in muratura o in legno, ampliamenti e sopraelevazioni."),\n'
      '                ("Ristrutturazione casali e rustici", "/ristrutturazione-casali-e-rustici/", "Case di campagna e case vecchie recuperate, materiali originali salvati."),\n'
      '                ("Recinzioni, piscine e box auto", "/recinzioni-piscine-e-box-auto/", "Recinzioni, cancelli, piscine interrate, garage, vialetti e drenaggi."),\n'
      '                ("Grondaie, lattoneria e linea vita", "/grondaie-lattoneria-e-linea-vita/", "Grondaie, scossaline, linea vita e lucernari.")]),\n'
      '              ("Accessibilità, impianti e su misura", [\n'
      '                ("Abbattimento barriere architettoniche", "/abbattimento-barriere-architettoniche/", "Bagni per disabili e anziani, montascale, ascensori, rampe."),\n'
      '                ("Fotovoltaico e pompa di calore", "/fotovoltaico-e-pompa-di-calore/", "Fotovoltaico con accumulo, pompa di calore, pavimento radiante, VMC."),\n'
      '                ("Cabine armadio, pareti attrezzate e boiserie", "/cabine-armadio-pareti-attrezzate-e-boiserie/", "Spazi su misura in cartongesso o legno, porte filo muro."),\n'
      '                ("Cambio destinazione d’uso e APE", "/cambio-destinazione-d-uso-e-ape/", "Cambio d’uso, frazionamento, APE, diagnosi energetica, agibilità.")]),\n')
G2 = ('              ("Vendere, comprare, affittare", [\n'
      '                ("Compriamo case da ristrutturare", "/compriamo-case-da-ristrutturare/", "Acquisto diretto di case e rustici da ristrutturare, con proposta scritta."),\n'
      '                ("Home staging", "/home-staging/", "Lavori mirati e allestimento per vendere o affittare prima e meglio."),\n'
      '                ("Ristrutturazione e gestione affitti brevi", "/ristrutturazione-e-gestione-affitti-brevi/", "Appartamenti pronti per Airbnb e gestiti, CIN compreso.")]),\n')

# ---- pagina principale /real-estate/: due gruppi prima di "Arredo"
rep('real-estate-dati-1.py', [('              ("Arredo", [', G1 + G2 + '              ("Arredo", [')])
# ---- /impresa-edile/: gruppi prima di "Progetto, pratiche e coordinamento"
rep('real-estate-dati-9.py', [('              ("Progetto, pratiche e coordinamento", [', G1 + '              ("Progetto, pratiche e coordinamento", [')])

# ---- footer IT
rep('real-estate-chrome.py', [(
 "('/stucco-veneziano-e-decorazioni/', 'Stucco veneziano'), ",
 "('/stucco-veneziano-e-decorazioni/', 'Stucco veneziano'), ('/abbattimento-barriere-architettoniche/', 'Barriere architettoniche'), ('/impermeabilizzazioni/', 'Impermeabilizzazioni'), ('/muffa-e-infiltrazioni/', 'Muffa e infiltrazioni'), ('/adeguamento-sismico-e-consolidamento/', 'Adeguamento sismico'), ('/demolizioni-e-sgomberi/', 'Demolizioni e sgomberi'), ('/costruzione-case-e-ampliamenti/', 'Costruzione case'), ('/ristrutturazione-casali-e-rustici/', 'Casali e rustici'), ('/recinzioni-piscine-e-box-auto/', 'Recinzioni e piscine'), ('/grondaie-lattoneria-e-linea-vita/', 'Grondaie e linea vita'), ('/fotovoltaico-e-pompa-di-calore/', 'Fotovoltaico e pompa di calore'), ('/cabine-armadio-pareti-attrezzate-e-boiserie/', 'Cabine armadio e boiserie'), ('/cambio-destinazione-d-uso-e-ape/', 'Cambio d’uso e APE'), ('/home-staging/', 'Home staging'), ('/compriamo-case-da-ristrutturare/', 'Compriamo case da ristrutturare'), ('/ristrutturazione-e-gestione-affitti-brevi/', 'Affitti brevi'), ")])

# ---- llms.txt
rep('real-estate-llms.py', [(
 '     ("Stucco veneziano e decorazioni", "/stucco-veneziano-e-decorazioni/"),\n',
 '     ("Stucco veneziano e decorazioni", "/stucco-veneziano-e-decorazioni/"),\n'
 '     ("Abbattimento barriere architettoniche", "/abbattimento-barriere-architettoniche/"), ("Impermeabilizzazioni", "/impermeabilizzazioni/"), ("Muffa e infiltrazioni", "/muffa-e-infiltrazioni/"),\n'
 '     ("Adeguamento sismico e consolidamento", "/adeguamento-sismico-e-consolidamento/"), ("Demolizioni e sgomberi", "/demolizioni-e-sgomberi/"), ("Costruzione case e ampliamenti", "/costruzione-case-e-ampliamenti/"),\n'
 '     ("Ristrutturazione casali e rustici", "/ristrutturazione-casali-e-rustici/"), ("Recinzioni, piscine e box auto", "/recinzioni-piscine-e-box-auto/"), ("Grondaie, lattoneria e linea vita", "/grondaie-lattoneria-e-linea-vita/"),\n'
 '     ("Fotovoltaico e pompa di calore", "/fotovoltaico-e-pompa-di-calore/"), ("Cabine armadio, pareti attrezzate e boiserie", "/cabine-armadio-pareti-attrezzate-e-boiserie/"), ("Cambio destinazione d’uso e APE", "/cambio-destinazione-d-uso-e-ape/"),\n'
 '     ("Home staging", "/home-staging/"), ("Compriamo case da ristrutturare (acquisto diretto, non mediazione)", "/compriamo-case-da-ristrutturare/"), ("Ristrutturazione e gestione affitti brevi", "/ristrutturazione-e-gestione-affitti-brevi/"),\n')])

# ---- pagine esistenti correlate: un link in testa a "Pagine collegate"
def al(fn, first, new): rep(fn, [(' altri=[' + first, ' altri=[' + new + ', ' + first)])
al('real-estate-dati-3.py', '("Trasformazione vasca in doccia", "/trasformazione-vasca-in-doccia/"), ("Guida: rifare il bagno"', '("Bagno per disabili e anziani", "/abbattimento-barriere-architettoniche/")')
al('real-estate-dati-8.py', '("Ristrutturazione bagno", "/ristrutturazione-bagno/"), ("Guida: rifare il bagno"', '("Bagno per anziani e disabili", "/abbattimento-barriere-architettoniche/")')
al('real-estate-dati-5.py', '("Pavimenti e serramenti", "/pavimenti-e-serramenti/"), ("Facciate ventilate e rifacimento"', '("Impermeabilizzazioni", "/impermeabilizzazioni/")')
al('real-estate-dati-5.py', '("Isolamento sottotetto", "/isolamento-sottotetto/"), ("Cappotto termico", "/cappotto-termico/"), ("Condomini', '("Grondaie, lattoneria e linea vita", "/grondaie-lattoneria-e-linea-vita/")')
al('real-estate-dati-10.py', '("Muratore e opere murarie", "/muratore-e-opere-murarie/"), ("Imbianchino e tinteggiature", "/imbianchino-e-tinteggiature/"), ("Guida: cappotto', '("Muffa e infiltrazioni", "/muffa-e-infiltrazioni/")')
al('real-estate-dati-10.py', '("Pratiche edilizie CILA e SCIA", "/pratiche-edilizie-cila-scia/"), ("Guida: CILA o SCIA"', '("Cambio destinazione d’uso e APE", "/cambio-destinazione-d-uso-e-ape/")')
al('real-estate-dati-2.py', '("Guida: cartongesso al mq", "/guide/prezzo-cartongesso-al-mq/"), ("Pareti divisorie"', '("Cabine armadio e pareti attrezzate", "/cabine-armadio-pareti-attrezzate-e-boiserie/")')
al('real-estate-dati-8.py', '("Ristrutturazioni chiavi in mano", "/ristrutturazioni-chiavi-in-mano/"), ("Pareti divisorie", "/pareti-divisorie/"), ("Pratiche CILA', '("Demolizioni e sgomberi", "/demolizioni-e-sgomberi/")')
al('real-estate-dati-8.py', '("Ristrutturazioni chiavi in mano", "/ristrutturazioni-chiavi-in-mano/"), ("Ristrutturazione bagno", "/ristrutturazione-bagno/"), ("Cartongesso', '("Fotovoltaico e pompa di calore", "/fotovoltaico-e-pompa-di-calore/")')
