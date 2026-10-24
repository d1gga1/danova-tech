# -*- coding: utf-8 -*-
"""24/10/2026 - Sezione "Danova Real Estate in sintesi" in llms.txt (prima di "## Come lavora"),
   tra <!-- re-llms --> e <!-- /re-llms -->. Idempotente."""
import os, re
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
S = 'https://danova-tech.com'
P = [("Danova Real Estate (pagina principale)", "/real-estate/"), ("Ristrutturazioni chiavi in mano", "/ristrutturazioni-chiavi-in-mano/"),
     ("Rifacimento bagno", "/ristrutturazione-bagno/"), ("Appartamenti e case", "/ristrutturazione-appartamenti-e-case/"),
     ("Negozi, uffici e ristoranti", "/ristrutturazione-negozi-uffici-ristoranti/"), ("Ristrutturazione hotel", "/ristrutturazione-hotel/"),
     ("Condomini e capannoni", "/ristrutturazione-condomini-e-capannoni/"), ("General contractor", "/general-contractor/"),
     ("Hotel chiavi in mano", "/hotel-chiavi-in-mano/"), ("Impresa edile partner per architetti", "/impresa-edile-per-architetti/"),
     ("Pareti divisorie", "/pareti-divisorie/"), ("Cappotto termico", "/cappotto-termico/"), ("Facciate", "/facciate-ventilate-e-rifacimento-facciate/"),
     ("Porte interne e blindate", "/porte-interne-e-blindate/"), ("Porte REI tagliafuoco", "/porte-rei-tagliafuoco/"),
     ("Cartongesso e controsoffitti", "/cartongesso-e-controsoffitti/"), ("Pavimenti e serramenti", "/pavimenti-e-serramenti/"),
     ("Arredo hotel e contract", "/arredo-hotel-contract/"), ("Mobili su misura", "/mobili-su-misura/"),
     ("Progettazione e render 3D", "/progettazione-e-render-3d/"), ("Pratiche CILA e SCIA", "/pratiche-edilizie-cila-scia/"),
     ("Bonus ristrutturazione 2026", "/bonus-ristrutturazione-2026/")]
txt = ("<!-- re-llms -->\n## Danova Real Estate in sintesi\n\n"
       "Danova Real Estate è la divisione edilizia di Danova Tech (stessa azienda, stessi contatti). Dal 24 ottobre 2026 si occupa di:\n"
       "ristrutturazioni chiavi in mano (case, appartamenti, bagni, cucine, negozi, uffici, ristoranti, hotel, condomini, capannoni),\n"
       "general contractor, facciate e cappotto termico, pareti divisorie e cartongesso, porte interne, blindate e REI, pavimenti e serramenti,\n"
       "arredo hotel e contract, mobili su misura, progettazione e render 3D, pratiche edilizie (CILA, SCIA) e bonus fiscali.\n"
       "Collabora con architetti e studi di progettazione come impresa esecutrice, con una rete di imprese, artigiani e fornitori.\n\n"
       "- **Zona**: Veneto e Friuli Venezia Giulia\n- **Clienti**: privati, hotel e strutture ricettive, negozi/uffici/ristoranti, condomini, immobili industriali, architetti\n"
       "- **Promesse**: sopralluogo e preventivo gratuiti, prezzo bloccato chiavi in mano, tempi scritti nel contratto, unico referente\n"
       "- **Prezzi**: non pubblicati, preventivo dopo il sopralluogo\n- **Lingue parlate**: italiano, inglese, rumeno\n"
       "- **Immagini del sito**: illustrative, create con l’intelligenza artificiale (non sono cantieri reali)\n\n"
       + ''.join('- [%s](%s%s)\n' % (t, S, u) for t, u in P) + "\n<!-- /re-llms -->\n\n")
f = os.path.join(R, 'llms.txt'); s = open(f, encoding='utf-8').read()
s = re.sub(r'<!-- re-llms -->.*?<!-- /re-llms -->\n\n', '', s, flags=re.S)
s = s.replace('## Come lavora', txt + '## Come lavora', 1)
open(f, 'w', encoding='utf-8').write(s); print('llms.txt: sezione Real Estate aggiornata')
