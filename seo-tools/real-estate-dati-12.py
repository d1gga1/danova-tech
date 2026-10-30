# -*- coding: utf-8 -*-
"""30/10/2026 - Danova Real Estate (IT, solo_it): pagine per SEO Google e motori AI (ChatGPT, Claude, Perplexity, AI Overviews).
   Dati confermati dal titolare il 30/10/2026: ramo di Danova Tech (stessa P.IVA); oltre 200 cantieri; artigiani da generazioni;
   sopralluogo gratuito entro una settimana; pagamenti: acconto, SAL, saldo, finanziamento a rate con finanziaria partner su richiesta;
   garanzia scritta (senza anni) + RC e CAR; telefono/WhatsApp Danova Tech, risposta 24/7; marchi: Mapei, Kerakoll, Knauf, Siniat, Velux,
   Daikin, Mitsubishi Electric. NESSUN PREZZO e NESSUN TEMPO pubblicato. Gli esempi sono DICHIARATI come scenari tipo, non lavori reali."""
import importlib.util, os
_s = importlib.util.spec_from_file_location('re1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real-estate-dati-1.py'))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
G, _G, RE, svc, FAQ_BASE = _m.G, _m._G, _m.RE, _m.svc, _m.FAQ_BASE
PAGINE = []
def P(**k): PAGINE.append(dict(lang="it", solo_it=True, faqtitle=f"Domande {G}frequenti.{_G}", altrititle="Pagine collegate", **k))
TEL = "+39 388 470 6887"
MARCHI = "Mapei, Kerakoll, Knauf, Siniat, Velux, Daikin e Mitsubishi Electric"

# ------------------------------------------------------------------ DOMANDE FREQUENTI
FAQ = [
 ("Chi è Danova Real Estate?", "Danova Real Estate è la divisione edilizia di Danova Tech, con sede a Mansuè (Treviso). Facciamo ristrutturazioni chiavi in mano e singoli lavori edili in Veneto e Friuli Venezia Giulia, con artigiani di fiducia attivi da generazioni e un unico referente. Abbiamo completato oltre 200 cantieri e lavori."),
 ("In quali zone lavorate?", "In tutto il Veneto e il Friuli Venezia Giulia: province di Treviso, Venezia, Padova, Vicenza, Verona, Rovigo, Belluno, Pordenone, Udine, Gorizia e Trieste. Non lavoriamo fuori da queste due regioni."),
 ("Quanto costa una ristrutturazione?", "Non pubblichiamo listini perché il prezzo dipende da superficie, stato di impianti e strutture, materiali scelti, pratiche e accessibilità del cantiere. Dopo il sopralluogo gratuito ricevete un preventivo scritto voce per voce a prezzo bloccato: il prezzo del contratto è quello finale per i lavori descritti."),
 ("Quanto tempo serve per ristrutturare?", "Dipende dal tipo di lavoro, dalle pratiche e dai materiali. Non diamo tempi a voce: data di inizio, fasi e data di consegna sono scritte nel cronoprogramma allegato al contratto."),
 ("Il sopralluogo è gratuito? Quando venite?", "Sì, il sopralluogo e il preventivo sono gratuiti e senza impegno. Di solito veniamo entro una settimana dalla richiesta."),
 ("Posso restare in casa durante i lavori?", "Spesso sì, organizzando il cantiere per fasi: per esempio lasciando sempre un bagno utilizzabile, chiudendo con teli le zone di lavoro e concordando gli orari rumorosi. Per ristrutturazioni complete con impianti rifatti in tutta la casa conviene in genere trasferirsi per il periodo dei lavori principali. Ve lo diciamo al sopralluogo."),
 ("Quali bonus spettano nel 2026?", "Per la ristrutturazione dell’abitazione principale la detrazione è del 50%, per gli altri immobili del 36%. Il sismabonus segue le stesse aliquote; la detrazione al 75% per le barriere architettoniche è scaduta il 31 dicembre 2025. Prepariamo fatture e documenti; la verifica finale spetta al vostro commercialista o CAF."),
 ("Vi occupate voi di pratiche e permessi?", "Sì. I nostri tecnici verificano la situazione urbanistica e catastale e presentano la pratica corretta: edilizia libera, CILA, SCIA o permesso di costruire, deposito strutturale quando serve, sanatorie e cambi di destinazione d’uso. In Friuli Venezia Giulia seguiamo il Codice regionale dell’edilizia (legge regionale 19/2009)."),
 ("Come si paga?", "Con un acconto alla firma del contratto, pagamenti a stati di avanzamento durante il cantiere e il saldo a fine lavori. Su richiesta è possibile un finanziamento a rate con una finanziaria partner."),
 ("Che garanzie date?", "Prezzo bloccato e tempi scritti nel contratto, garanzia scritta sui lavori oltre alle garanzie previste dalla legge, cantiere assicurato con polizza di responsabilità civile e CAR (tutti i rischi del cantiere)."),
 ("Chi esegue i lavori?", "Squadre e artigiani locali di fiducia, molti attivi da generazioni, per muratura, cartongesso, posa, impianti, tetti e finiture, coordinati da un unico referente di Danova Real Estate che risponde di prezzo, tempi e qualità."),
 ("Che materiali usate?", "Scegliamo i materiali con voi in base al progetto. Lavoriamo spesso con prodotti di aziende come " + MARCHI + "."),
 ("Fate anche piccoli lavori?", "Sì: oltre alle ristrutturazioni complete facciamo singoli lavori come bagno, imbiancatura, cartongesso, porte, impermeabilizzazioni, grondaie e riparazioni."),
 ("Comprate case da ristrutturare?", "Sì, acquistiamo direttamente case, appartamenti e rustici da ristrutturare in Veneto e Friuli, con valutazione gratuita e proposta scritta. Non siamo un’agenzia immobiliare e non facciamo intermediazione."),
 ("Come vi contatto?", "Al telefono o su WhatsApp al " + TEL + ", oppure dal modulo del sito. Rispondiamo 24 ore su 24, 7 giorni su 7. Parliamo italiano, inglese e rumeno."),
]
P(url="/real-estate/domande-frequenti/", hero="re-direttore-lavori", heroalt="Responsabile di cantiere che spiega i lavori a un cliente",
 title="Domande frequenti su ristrutturazioni | Danova Real Estate",
 desc="Risposte dirette su costi, tempi, bonus 2026, pratiche, pagamenti, garanzie e zone di lavoro di Danova Real Estate, impresa edile in Veneto e Friuli.",
 ogtitle="Domande frequenti — Danova Real Estate", ogdesc="Costi, tempi, bonus, pratiche, pagamenti e garanzie: le risposte in breve.",
 crumbs=[RE, ("Domande frequenti", None)], eyebrow="Domande frequenti · Danova Real Estate",
 h1=f"Domande frequenti: {G}le risposte in breve.{_G}",
 lead="Le domande che ci fate più spesso prima di iniziare una ristrutturazione in Veneto o in Friuli, con risposte brevi e precise.",
 cta1="Richiedi il sopralluogo gratuito", cta2="Leggi le risposte",
 badges=["Oltre 200 cantieri", "Sopralluogo entro una settimana", "Prezzo bloccato", "Risposta 24/7"],
 sezioni=[
  {"id": "in-breve", "tipo": "breve", "eyebrow": "In breve", "h2": f"Danova Real Estate {G}in sei righe{_G}",
   "testo": "<b>Danova Real Estate</b> è la divisione edilizia di <b>Danova Tech</b> (stessa società), con sede a <b>Mansuè (Treviso)</b>. Ristrutturazioni chiavi in mano e lavori edili in <b>Veneto e Friuli Venezia Giulia</b>, con artigiani di fiducia attivi da generazioni e <b>oltre 200 cantieri</b> completati. Sopralluogo <b>gratuito entro una settimana</b>, preventivo a <b>prezzo bloccato</b>, tempi nel contratto, un unico referente.",
   "fatti": [("Sede", "Mansuè (TV)"), ("Zone", "Veneto e Friuli Venezia Giulia"), ("Esperienza", "Oltre 200 cantieri"),
             ("Sopralluogo", "Gratuito, entro una settimana"), ("Pagamenti", "Acconto, stati di avanzamento, saldo; rate su richiesta"), ("Contatti", TEL + " · 24/7")]}],
 faq=FAQ,
 ctabox={"h2": "Non trovate la vostra domanda?", "p": "Scriveteci su WhatsApp o chiamate: rispondiamo 24 ore su 24.", "btn": "Richiedi il sopralluogo gratuito"},
 altri=[("Danova Real Estate", "/real-estate/"), ("Chi siamo", "/real-estate/chi-siamo/"), ("Esempi di intervento", "/real-estate/esempi-di-intervento/"),
        ("Impresa edile: tutte le lavorazioni", "/impresa-edile/"), ("Bonus ristrutturazione 2026", "/bonus-ristrutturazione-2026/"), ("Guida: quanto costa ristrutturare casa", "/guide/quanto-costa-ristrutturare-casa/")],
 svc=svc("Ristrutturazioni e lavori edili", "Impresa edile", "Ristrutturazioni chiavi in mano e lavori edili in Veneto e Friuli Venezia Giulia, con sopralluogo gratuito entro una settimana e prezzo bloccato.",
         ["Ristrutturazioni chiavi in mano", "Lavori edili", "Pratiche edilizie", "Bonus fiscali"]))

# ------------------------------------------------------------------ ESEMPI DI INTERVENTO (scenari dichiarati)
AVV = "<b>Attenzione:</b> questi sono <b>esempi di intervento tipo</b>, scritti per mostrare come lavoriamo in situazioni frequenti nelle varie zone. Non descrivono un cantiere o un cliente specifico, e non indicano prezzi né tempi: quelli li trovate nel preventivo e nel cronoprogramma dopo il sopralluogo."
ES = [
 ("Treviso: appartamento anni ’70 in condominio", "Situazione tipica: impianti originali, bagno cieco, cucina chiusa, serramenti in legno che non tengono.", "Cosa si fa: demolizioni interne, impianti elettrico e idraulico nuovi a norma, cucina aperta sul soggiorno con trave di sostegno se il muro è portante, bagno con doccia a filo pavimento, serramenti nuovi, pratica CILA e documenti per il bonus.", "/ristrutturazioni-treviso/"),
 ("Pordenone: villetta da rendere efficiente", "Situazione tipica: casa singola degli anni ’80, caldaia a gas vecchia, tetto non isolato, bollette alte.", "Cosa si fa: isolamento del sottotetto o del tetto, cappotto, serramenti, pompa di calore con fotovoltaico e accumulo, verifica delle detrazioni nel 2026. Pratiche secondo le regole del Friuli Venezia Giulia.", "/ristrutturazioni-pordenone/"),
 ("Venezia: piano terra con acqua alta", "Situazione tipica: muri umidi con salnitro, impianti bassi danneggiati dall’acqua salata, edificio vincolato.", "Cosa si fa: intonaci risananti, impianti sollevati, pavimenti e materiali che resistono all’acqua, trasporti in barca organizzati da noi e verifica delle autorizzazioni necessarie per l’edificio.", "/ristrutturazioni-venezia/"),
 ("Padova: appartamento da affittare a studenti", "Situazione tipica: appartamento grande con un solo bagno, vicino all’Università.", "Cosa si fa: verifica comunale, pareti divisorie in cartongesso insonorizzato per ricavare camere, un secondo bagno, impianti adatti a più inquilini, arredo resistente.", "/ristrutturazioni-padova/"),
 ("Udine: casa friulana con corte", "Situazione tipica: casa in sasso e mattoni con solai in legno, umidità al piano terra, tetto da rifare.", "Cosa si fa: progetto strutturale, consolidamento dei solai e collegamenti antisismici, vespaio aerato, tetto nuovo isolato, impianti e finiture che lasciano la pietra a vista. Valutazione del sismabonus.", "/ristrutturazioni-udine/"),
 ("Jesolo: seconda casa da affittare", "Situazione tipica: appartamento al Lido degli anni ’70, proprietario che vive lontano.", "Cosa si fa: lavori programmati fuori stagione, bagno e cucina nuovi, climatizzazione, arredo resistente, aggiornamenti con foto ogni settimana e, se richiesto, gestione degli affitti brevi.", "/ristrutturazioni-jesolo/"),
]
P(url="/real-estate/esempi-di-intervento/", hero="re-soggiorno-dopo", heroalt="Soggiorno rinnovato con luci a incasso (immagine illustrativa)",
 title="Esempi di intervento in Veneto e Friuli | Danova Real Estate",
 desc="Esempi di intervento tipo in Veneto e Friuli: appartamenti, villette, piani terra a Venezia, case friulane e seconde case al mare. Cosa si fa, caso per caso.",
 ogtitle="Esempi di intervento", ogdesc="Situazioni tipiche e come le affrontiamo, città per città.",
 crumbs=[RE, ("Esempi di intervento", None)], eyebrow="Esempi di intervento · Veneto e Friuli",
 h1=f"Esempi di intervento: {G}situazioni tipiche, città per città.{_G}",
 lead="Sei situazioni che incontriamo spesso tra Veneto e Friuli e il modo in cui le affrontiamo. Sono esempi tipo, non cantieri specifici.",
 cta1="Richiedi il sopralluogo gratuito", cta2="Vedi gli esempi",
 badges=["Esempi tipo", "Veneto", "Friuli Venezia Giulia", "Nessun prezzo inventato"],
 sezioni=[
  {"id": "nota", "tipo": "testo", "eyebrow": "Prima di leggere", "h2": f"Esempi tipo, {G}non casi reali{_G}", "corpo": [AVV]}] +
  [{"id": "es-%d" % i, "tipo": "testo", "eyebrow": "Esempio di intervento tipo", "h2": t, "corpo": [a, b, "Vedete anche la pagina <a href=\"%s\">%s</a>." % (u, t.split(':')[0] if ':' in t else t)]}
   for i, (t, a, b, u) in enumerate(ES, 1)],
 faq=[("Questi esempi sono lavori reali?", "No, sono scenari tipo scritti per spiegare come lavoriamo in situazioni frequenti. Non riguardano un cliente o un cantiere specifico."),
      ("Perché non indicate prezzi e tempi?", "Perché cambiano molto da casa a casa. Dopo il sopralluogo gratuito ricevete preventivo a prezzo bloccato e cronoprogramma scritto.")] + FAQ_BASE[:1],
 ctabox={"h2": "La vostra situazione somiglia a uno di questi esempi?", "p": "Raccontatecela: veniamo a vedere entro una settimana.", "btn": "Richiedi il sopralluogo gratuito"},
 altri=[("Domande frequenti", "/real-estate/domande-frequenti/"), ("Chi siamo", "/real-estate/chi-siamo/"), ("Impresa edile: tutte le lavorazioni", "/impresa-edile/"),
        ("Ristrutturazioni chiavi in mano", "/ristrutturazioni-chiavi-in-mano/"), ("Danova Real Estate", "/real-estate/")],
 svc=svc("Ristrutturazioni in Veneto e Friuli", "Ristrutturazione edilizia", "Esempi di intervento tipo per appartamenti, villette, case storiche e seconde case in Veneto e Friuli Venezia Giulia.",
         ["Ristrutturazione appartamenti", "Efficientamento energetico", "Recupero case storiche", "Ristrutturazione per affitti"]))
