# -*- coding: utf-8 -*-
"""30/10/2026 - Posizionamento "impresa edile" (real-estate-dati-9.py) e nuove lavorazioni (real-estate-dati-10.py).
   NESSUN PREZZO PUBBLICATO (confermato dal titolare il 30/10/2026).
   Aggiorna: lavorazioni di cartongesso ampliate, link a /impresa-edile/ dal pilastro, footer IT, indice guide e llms.txt.
   Sostituzioni esatte: si ferma se un testo non si trova. Idempotente."""
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

# ---- cartongesso (2): lavorazioni ampliate e cartongessisti
rep('real-estate-dati-2.py', [
 ('desc="Pareti in cartongesso, contropareti isolanti, controsoffitti con luci integrate e soluzioni acustiche per case, uffici, negozi e hotel in Veneto e Friuli. Sopralluogo gratuito.",',
  'desc="Cartongessisti per pareti, contropareti isolanti, controsoffitti, pareti attrezzate, librerie, velette e isolamento acustico in Veneto e Friuli. Sopralluogo gratuito.",'),
 ('''             ("Antincendio", "Pareti e controsoffitti certificati per compartimentazioni e protezione delle strutture.")]},
  {"id": "galleria", "tipo": "gal", "eyebrow": "Esempi", "h2": f"Dal cantiere {G}al risultato{_G}",''',
  '''             ("Antincendio", "Pareti e controsoffitti certificati per compartimentazioni e protezione delle strutture.")]},
  {"id": "tutte", "tipo": "cards", "eyebrow": "Tutte le lavorazioni", "h2": f"Le altre lavorazioni {G}dei nostri cartongessisti{_G}",
   "corpo": [("Pareti attrezzate e librerie", "Pareti TV, librerie e mensole in cartongesso con luci e nicchie integrate, su misura."),
             ("Nicchie e vani", "Nicchie nella doccia, vani per lavatrice o caldaia, cassonetti per tubi e tapparelle."),
             ("Controsoffitti ribassati", "Per abbassare stanze molto alte, nascondere travi o canalizzazioni dell’aria condizionata."),
             ("Bagno e cucina", "Lastre idrorepellenti per pareti bagnate, contropareti per sanitari sospesi e scarichi."),
             ("Mansarde e sottotetti", "Controsoffitti isolati sotto le falde, pareti basse e ripostigli."),
             ("Insonorizzazione", "Contropareti e controsoffitti acustici contro voci, TV e calpestio dei vicini."),
             ("Contropareti isolanti", "Isolamento termico dall’interno su muri freddi o con muffa, quando la facciata non si tocca."),
             ("Porte scorrevoli a scomparsa", "Controtelai inseriti nella parete in cartongesso, anche filo muro."),
             ("Stuccatura e finitura", "Superfici stuccate e rasate pronte da tinteggiare, anche con i nostri imbianchini.")]},
  {"id": "galleria", "tipo": "gal", "eyebrow": "Esempi", "h2": f"Dal cantiere {G}al risultato{_G}",'''),
 ('altri=[("Ristrutturazione negozi, uffici e ristoranti", "/ristrutturazione-negozi-uffici-ristoranti/"), ("Porte interne e blindate", "/porte-interne-e-blindate/"), ("Porte REI tagliafuoco", "/porte-rei-tagliafuoco/"),\n        ("Impianti elettrici e idraulici", "/impianti-elettrici-e-idraulici/"), ("Imbianchino e tinteggiature", "/imbianchino-e-tinteggiature/"), ("Danova Real Estate", "/real-estate/")],',
  'altri=[("Guida: cartongesso al mq", "/guide/prezzo-cartongesso-al-mq/"), ("Pareti divisorie", "/pareti-divisorie/"), ("Soppalchi", "/soppalchi/"),\n        ("Guida: cappotto termico interno", "/guide/cappotto-termico-interno/"), ("Imbianchino e tinteggiature", "/imbianchino-e-tinteggiature/"), ("Impresa edile: tutte le lavorazioni", "/impresa-edile/")],'),
])

# ---- pilastro Real Estate (1): link alla pagina impresa edile
rep('real-estate-dati-1.py', [(
 '              ("General contractor", [\n                ("General contractor", "/general-contractor/", "Un unico contratto per progetto, imprese, forniture e direzione del cantiere."),',
 '              ("General contractor", [\n                ("Impresa edile: tutte le lavorazioni", "/impresa-edile/", "Muratura, cartongesso, imbiancature, bagni, impianti, tetti, resine, pergole e pratiche, con un solo referente."),\n                ("General contractor", "/general-contractor/", "Un unico contratto per progetto, imprese, forniture e direzione del cantiere."),')])

# ---- footer IT
rep('real-estate-chrome.py', [(
 "c2 += ''.join(li(u, t, cur) for u, t in [('/trasformazione-vasca-in-doccia/', 'Trasformazione vasca in doccia'),",
 "c2 += ''.join(li(u, t, cur) for u, t in [('/impresa-edile/', 'Impresa edile: tutte le lavorazioni'), ('/microcemento/', 'Microcemento'), ('/pavimenti-in-resina/', 'Pavimenti in resina'), ('/porte-blindate/', 'Porte blindate'), ('/pergole-e-tettoie/', 'Pergole e tettoie'), ('/trasformazione-vasca-in-doccia/', 'Trasformazione vasca in doccia'),")])

# ---- indice guide
rep('real-estate-guide.py', [(
 'G = [("/guide/quanto-costa-ristrutturare-casa/",',
 'G = [("/guide/quanto-costa-rifare-il-bagno/", "Quanto costa rifare il bagno: le voci che fanno il prezzo", "Demolizione, impianti, piastrelle, sanitari e doccia: cosa pesa di più sul preventivo."),\n'
 '     ("/guide/quanto-costa-trasformare-vasca-in-doccia/", "Trasformare la vasca in doccia: costi, soluzioni e tempi", "Sostituzione semplice, walk-in o filo pavimento: cosa decide il costo."),\n'
 '     ("/guide/prezzo-cartongesso-al-mq/", "Cartongesso al mq: cosa fa il prezzo", "Pareti, contropareti, controsoffitti, REI e pareti attrezzate a confronto."),\n'
 '     ("/guide/quanto-costa-imbiancare-casa/", "Quanto costa imbiancare casa: come si calcola", "Come si contano i metri da dipingere e cosa fa salire il conto."),\n'
 '     ("/guide/quanto-costa-rifare-il-tetto/", "Quanto costa rifare il tetto: interventi e voci", "Dalla sostituzione delle tegole al tetto ventilato con nuova struttura."),\n'
 '     ("/guide/cappotto-termico-interno/", "Cappotto termico interno: quando conviene", "Materiali, spessori, condensa e ponti termici dell’isolamento dall’interno."),\n'
 '     ("/guide/quanto-costa-ristrutturare-casa/",')])

# ---- llms.txt
rep('real-estate-llms.py', [(
 'P = [("Danova Real Estate (pagina principale)", "/real-estate/"),',
 'P = [("Danova Real Estate (pagina principale)", "/real-estate/"), ("Impresa edile: tutte le lavorazioni", "/impresa-edile/"),\n'
 '     ("Microcemento", "/microcemento/"), ("Pavimenti in resina", "/pavimenti-in-resina/"), ("Pergole e tettoie", "/pergole-e-tettoie/"), ("Porte blindate", "/porte-blindate/"),\n'
 '     ("Soppalchi", "/soppalchi/"), ("Scale interne", "/scale-interne/"), ("Cerchiatura e apertura muro portante", "/cerchiatura-muro-portante/"),\n'
 '     ("Umidità di risalita", "/umidita-di-risalita/"), ("Rimozione amianto ed eternit", "/rimozione-amianto-eternit/"), ("Sanatoria edilizia", "/sanatoria-edilizia/"),\n'
 '     ("Stucco veneziano e decorazioni", "/stucco-veneziano-e-decorazioni/"),\n'
 '     ("Guida: quanto costa rifare il bagno", "/guide/quanto-costa-rifare-il-bagno/"), ("Guida: trasformare la vasca in doccia", "/guide/quanto-costa-trasformare-vasca-in-doccia/"),\n'
 '     ("Guida: cartongesso al mq", "/guide/prezzo-cartongesso-al-mq/"), ("Guida: quanto costa imbiancare casa", "/guide/quanto-costa-imbiancare-casa/"),\n'
 '     ("Guida: quanto costa rifare il tetto", "/guide/quanto-costa-rifare-il-tetto/"), ("Guida: cappotto termico interno", "/guide/cappotto-termico-interno/"),')])
