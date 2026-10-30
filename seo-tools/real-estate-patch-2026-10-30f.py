# -*- coding: utf-8 -*-
"""30/10/2026 (f) - Fatti dell'impresa confermati dal titolare (SEO Google + AI): sopralluogo entro una settimana nella FAQ comune,
   llms.txt coerente e completo (oltre 200 cantieri, pagamenti, garanzia, RC e CAR, risposta 24/7, marchi, nuove lavorazioni),
   GeneralContractor con contactPoint 24/7 e parentOrganization, collegamenti alle pagine FAQ ed esempi. Idempotente."""
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
rep('real-estate-dati-1.py', [
 ('Non pagate nulla e non vi impegnate a nulla."),', 'Non pagate nulla e non vi impegnate a nulla. Di solito veniamo entro una settimana dalla richiesta."),'),
 ('                ("Chi siamo", "/real-estate/chi-siamo/", "Un solo referente e artigiani di fiducia, attivi da generazioni."),',
  '                ("Chi siamo", "/real-estate/chi-siamo/", "Un solo referente e artigiani di fiducia, attivi da generazioni."),\n'
  '                ("Domande frequenti", "/real-estate/domande-frequenti/", "Costi, tempi, bonus, pratiche, pagamenti e garanzie in breve."),\n'
  '                ("Esempi di intervento", "/real-estate/esempi-di-intervento/", "Situazioni tipiche città per città e come le affrontiamo."),')])
rep('real-estate-llms.py', [
 ('Dal 24 ottobre 2026 si occupa di:\\n"', 'Si occupa di:\\n"'),
 ('; dal 26 ottobre 2026 anche trasformazione vasca in doccia, opere murarie, tinteggiature e rifacimento impianti elettrici e idraulici (non pronto intervento).\\n"',
  '; anche trasformazione vasca in doccia, opere murarie, tinteggiature, impianti elettrici e idraulici (non pronto intervento), impermeabilizzazioni, muffa e infiltrazioni, adeguamento sismico, demolizioni e sgomberi, costruzione case e ampliamenti (case in legno con aziende partner), casali e rustici, recinzioni, piscine e box auto, grondaie e linea vita, fotovoltaico e pompa di calore, abbattimento barriere architettoniche, cabine armadio e boiserie, cambio d’uso e APE, home staging, acquisto diretto di case da ristrutturare (non mediazione) e ristrutturazione e gestione di affitti brevi.\\n"'),
 ('"Non ha squadre di dipendenti: coordina artigiani e imprese locali di fiducia, molti attivi da generazioni, e risponde al cliente di prezzo, tempi e qualità con un unico contratto.\\n"',
  '"Lavora con squadre e artigiani locali di fiducia, molti attivi da generazioni, coordinati da un unico referente che risponde al cliente di prezzo, tempi e qualità con un unico contratto. Ha completato oltre 200 cantieri e lavori.\\n"'),
 ('"- **Promesse**: sopralluogo e preventivo gratuiti, prezzo bloccato chiavi in mano, tempi scritti nel contratto, unico referente\\n"',
  '"- **Promesse**: sopralluogo e preventivo gratuiti (di solito entro una settimana), prezzo bloccato chiavi in mano, tempi scritti nel contratto, unico referente\\n"'
  '"- **Garanzie**: garanzia scritta sui lavori oltre a quelle di legge; cantiere assicurato con polizza RC e CAR\\n"'
  '"- **Pagamenti**: acconto alla firma, stati di avanzamento lavori, saldo a fine lavori; finanziamento a rate con finanziaria partner su richiesta\\n"'
  '"- **Contatti**: telefono e WhatsApp +39 388 470 6887 (lo stesso di Danova Tech), risposta 24 ore su 24, 7 giorni su 7\\n"'
  '"- **Materiali usati spesso**: Mapei, Kerakoll, Knauf, Siniat, Velux, Daikin, Mitsubishi Electric\\n"'
  '"- **Tempi**: non pubblicati; data di inizio e consegna nel cronoprogramma del contratto\\n"'
  '"- **Risposte rapide**: https://danova-tech.com/real-estate/domande-frequenti/\\n"')])
rep('real-estate-seo.py', [
 ("            n['slogan'] = SLOGAN[l]\n",
  "            n['slogan'] = SLOGAN[l]\n"
  "            # 30/10/2026: dati confermati dal titolare (ramo di Danova Tech, risposta 24/7)\n"
  "            n['parentOrganization'] = {'@id': SITE + '/#organization'}\n"
  "            n['contactPoint'] = {'@type': 'ContactPoint', 'telephone': '+39 388 470 6887', 'contactType': 'customer service', 'areaServed': ['IT'],\n"
  "                                 'availableLanguage': ['it', 'en', 'ro'], 'hoursAvailable': {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': '00:00', 'closes': '23:59'}}\n")])
