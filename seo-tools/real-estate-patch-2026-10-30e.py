# -*- coding: utf-8 -*-
"""30/10/2026 (e) - Titoli <= 62 e description <= 160 caratteri sulle pagine IT Real Estate che sforavano. Idempotente."""
import os, glob, sys
H = os.path.dirname(os.path.abspath(__file__))
R = [
 ("Quanto costa rifare il bagno: demolizione, impianti, impermeabilizzazione, piastrelle, sanitari e doccia, le voci che pesano di più sul preventivo e come risparmiare.",
  "Quanto costa rifare il bagno: demolizione, impianti, impermeabilizzazione, piastrelle, sanitari e doccia. Le voci che pesano sul preventivo e come risparmiare."),
 ("Quanto costa rifare il tetto: differenza tra sostituzione delle tegole, tetto isolato, tetto ventilato e interventi strutturali, ponteggi, eternit, pratiche e bonus.",
  "Quanto costa rifare il tetto: tegole, tetto isolato o ventilato, interventi strutturali, ponteggi, eternit, pratiche e bonus. Le voci del preventivo."),
 ("Rimozione amianto ed eternit in Veneto e Friuli | Bonifica e nuovo tetto", "Rimozione amianto ed eternit | Bonifica e nuovo tetto"),
 ("Danova Real Estate coordina ristrutturazioni e lavori edili in Veneto e Friuli con artigiani locali di fiducia, attivi da generazioni: un contratto, un referente.",
  "Danova Real Estate coordina ristrutturazioni e lavori edili in Veneto e Friuli con artigiani locali di fiducia: un contratto, un solo referente."),
 ("Soppalchi in legno, acciaio o laterocemento per case, mansarde, negozi e magazzini in Veneto e Friuli: progetto strutturale, pratiche edilizie, scale e parapetti.",
  "Soppalchi in legno, acciaio o laterocemento per case, mansarde, negozi e magazzini in Veneto e Friuli: progetto strutturale, pratiche, scale e parapetti."),
 ("Umidità di risalita: diagnosi e risanamento muri in Veneto e Friuli", "Umidità di risalita: diagnosi e risanamento | Veneto e Friuli"),
 ("Umidità di risalita e muri umidi: diagnosi delle cause, barriera chimica, intonaci deumidificanti, vespaio aerato e drenaggi per case e cantine in Veneto e Friuli.",
  "Umidità di risalita e muri umidi: diagnosi, barriera chimica, intonaci deumidificanti, vespaio aerato e drenaggi per case e cantine in Veneto e Friuli."),
 ("Aprire o allargare un vano in un muro portante: cerchiatura in acciaio o cemento armato, calcolo strutturale, pratica sismica ed edilizia, opere murarie e finiture.",
  "Aprire o allargare un vano nel muro portante: cerchiatura in acciaio o cemento armato, calcolo strutturale, pratiche sismiche ed edilizie, finiture."),
 ("Stucco veneziano e decorazioni in Veneto e Friuli | Marmorino e calce", "Stucco veneziano e decorazioni | Marmorino e calce"),
 ("Impresa edile in Veneto e Friuli: ristrutturazioni, muratura, cartongesso, imbiancature, bagni, impianti, tetti, cappotto, microcemento, resine, pergole e pratiche. Sopralluogo gratuito.",
  "Impresa edile in Veneto e Friuli: ristrutturazioni, muratura, cartongesso, bagni, tetti, cappotto, impermeabilizzazioni e pratiche. Sopralluogo gratuito."),
 ("Pavimenti in resina per case, negozi, uffici, garage e laboratori in Veneto e Friuli: autolivellante, epossidica o poliuretanica, anche sopra il pavimento esistente.",
  "Pavimenti in resina per case, negozi, uffici, garage e laboratori in Veneto e Friuli: epossidica o poliuretanica, anche sopra il pavimento esistente."),
 ("Microcemento per pavimenti, pareti, bagni, docce, cucine e scale in Veneto e Friuli: superfici continue senza fughe, anche sopra le piastrelle esistenti. Sopralluogo gratuito.",
  "Microcemento per pavimenti, pareti, bagni, docce, cucine e scale in Veneto e Friuli: superfici senza fughe, anche sopra le piastrelle esistenti."),
 ("Porte blindate certificate in classe antieffrazione, con isolamento termico e acustico, rivestimenti su misura e sostituzione del vecchio portoncino in Veneto e Friuli.",
  "Porte blindate certificate antieffrazione, con isolamento termico e acustico, rivestimenti su misura e sostituzione del portoncino in Veneto e Friuli."),
 ("Pergole e tettoie in Veneto e Friuli | Legno, alluminio, bioclimatiche", "Pergole e tettoie | Legno, alluminio, bioclimatiche"),
 ("Pergole in legno e alluminio, pergole bioclimatiche, pergotende e tettoie per case, ristoranti e hotel in Veneto e Friuli, con pratiche edilizie comprese. Sopralluogo gratuito.",
  "Pergole in legno e alluminio, bioclimatiche, pergotende e tettoie per case, ristoranti e hotel in Veneto e Friuli, con pratiche edilizie comprese."),
 ("Sanatoria edilizia per difformità e piccoli abusi: verifica della conformità, CILA tardiva, accertamento di conformità e regole del Salva Casa, prima di vendere o ristrutturare.",
  "Sanatoria edilizia per difformità e piccoli abusi: verifica, CILA tardiva, accertamento di conformità e Salva Casa, prima di vendere o ristrutturare."),
 ("Scale interne su misura in legno, acciaio, vetro o muratura, a giorno, a chiocciola o a sbalzo, anche con apertura del solaio e pratiche strutturali, in Veneto e Friuli.",
  "Scale interne su misura in legno, acciaio, vetro o muratura, a giorno, a chiocciola o a sbalzo, anche con apertura del solaio, in Veneto e Friuli."),
]
files = [f for f in glob.glob(os.path.join(H, 'real-estate-*.py')) if 'patch' not in f]
for a, b in R:
    hit = [f for f in files if a in open(f, encoding='utf-8').read()]
    if not hit:
        if not any(b in open(f, encoding='utf-8').read() for f in files): print('NON TROVATO:', a[:70])
        continue
    for f in hit:
        s = open(f, encoding='utf-8').read().replace(a, b); open(f, 'w', encoding='utf-8').write(s); print('aggiornato', os.path.basename(f), '|', b[:50])
