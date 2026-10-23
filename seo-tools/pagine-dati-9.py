# -*- coding: utf-8 -*-
"""14/10/2026 (nono giro): pagine Milano e Pavia per gestionali e siti web, legate alle sedi reali
   (uffici a Vermezzo con Zelo MI; produzione e uffici a Trumello PV).
   Dati confermati dal titolare: demo funzionante in meno di 24 ore, consegna in 1-2 settimane
   (siti, gestionali, app); assistenza e manutenzione con contratto.
   Uso: python3 seo-tools/pagine-build-2.py pagine-dati-9.py && python3 seo-tools/prezzi-pagine-2.py"""
OGGI = "2026-10-14"
G = '<span class="grad">'; _G = '</span>'
LG = ["Italian","English","German"]
GEST = ("Gestionali e CRM", "/servizi/gestionali-crm/")
WEB = ("Siti web ed e-commerce", "/servizi/siti-web-ecommerce/")
def area(c): return [{"@type":"City","name":c},{"@type":"AdministrativeArea","name":"Lombardia"},{"@type":"Country","name":"Italia"}]
def svc(name, typ, desc, cat, c): return {"name": name, "type": typ, "desc": desc, "area": area(c), "lingue": LG, "catalogo": cat}
CTA_G = {"h2": "Ci raccontate come lavorate oggi?", "p": "Mezz'ora, in videochiamata o di persona nei nostri uffici in Lombardia: capiamo dove perdete ore e in 48-72 ore vi mostriamo una demo funzionante.", "btn": "Prenota la chiamata"}
CTA_W = {"h2": "Vediamo il vostro sito?", "p": "Raccontateci cosa vendete e a chi: entro 24 ore vi mandiamo una demo della home page, poi il sito è online in 1-2 settimane.", "btn": "Chiedi la demo"}
PAGINE = []
STD_FAQ_G = [("Quanto tempo serve?","Una demo funzionante arriva in 48-72 ore e la prima versione in 1-2 settimane. Poi il gestionale cresce a fasi, un modulo alla volta, senza fermare il lavoro."),
 ("Possiamo recuperare i dati che abbiamo in Excel?","Sì: importiamo fogli Excel e archivi esistenti e colleghiamo il gestionale ai programmi che usate già, come fatturazione e contabilità."),
 ("Dopo la consegna chi ci segue?","Noi, con un contratto di assistenza e manutenzione: aggiornamenti, backup, correzioni e nuove funzioni quando servono, con un referente che conosce il vostro gestionale.")]
STD_FAQ_W = [("In quanto tempo è online il sito?","Entro 24 ore vi mandiamo una demo della home page; il sito completo è online in 1-2 settimane, con testi, immagini e SEO di base."),
 ("Il sito resta nostro?","Sì: dominio, hosting e contenuti sono vostri. Se scegliete l'abbonamento, dominio e hosting li gestiamo noi per voi."),
 ("Fate anche la manutenzione?","Sì, con un contratto di assistenza: aggiornamenti di sicurezza, backup, modifiche a testi e immagini e supporto via email e telefono.")]

# ===================================================== GESTIONALI MILANO
PAGINE.append({
 "lang":"it","url":"/gestionali-su-misura-milano/",
 "title":"Gestionali su misura a Milano: software aziendale",
 "desc":"Software gestionale su misura per aziende di Milano e hinterland: magazzino, commesse, CRM. Uffici a Vermezzo con Zelo, demo in 24 ore.",
 "ogtitle":"Gestionali su misura a Milano — Danova Tech",
 "ogdesc":"Gestionali, CRM e software di magazzino su misura per le aziende milanesi, dai nostri uffici di Vermezzo con Zelo.",
 "crumbs":[GEST,("Gestionali su misura a Milano",None)],
 "eyebrow":"Milano e hinterland",
 "h1":f"Gestionali su misura a Milano: {G}dai nostri uffici di Vermezzo.{_G}",
 "lead":"Software gestionale, di magazzino e CRM costruiti sulle aziende di Milano e dell'hinterland. I nostri uffici sono a Vermezzo con Zelo, a sud-ovest della città: veniamo a vedere come lavorate, e in 48-72 ore vi mostriamo una demo funzionante.",
 "cta1":"Raccontateci come lavorate","cta2":"Cosa costruiamo",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa costruiamo","h2":f"I gestionali che chiedono {G}le aziende milanesi{_G}",
   "corpo":[("Magazzino e logistica","Giacenze, ubicazioni, lotti, codici a barre e spedizioni: per chi gestisce merce fra Milano, i poli logistici dell'hinterland e i clienti."),
    ("Commesse e preventivi","Dal preventivo alla fattura, con stati, approvazioni e margini per commessa, per aziende di servizi, impianti e produzione."),
    ("CRM e rete vendita","Clienti, trattative, agenti e promemoria in un posto solo, consultabili dal telefono anche fuori ufficio."),
    ("Portali per clienti e rivenditori","Ordini online B2B, listini riservati, stato degli ordini e documenti scaricabili, collegati al gestionale."),
    ("Studi e società di servizi","Pratiche, scadenze, ore lavorate e fatturazione per studi professionali e società di consulenza."),
    ("Cruscotti per la direzione","I numeri che il titolare guarda ogni mattina, in una schermata, senza esportare in Excel.")]},
  {"id":"vicini","tipo":"testo","eyebrow":"Dove siamo","h2":f"Uffici a Vermezzo con Zelo, {G}a mezz'ora dal centro{_G}",
   "corpo":["I nostri uffici lombardi sono a Vermezzo con Zelo, fra Abbiategrasso e la tangenziale ovest. Da qui raggiungiamo in poco tempo Milano città, Corsico, Assago, Rozzano, Magenta, Abbiategrasso, Rho e Legnano: il primo incontro lo facciamo volentieri in azienda, perché un gestionale si capisce guardando come si lavora davvero.",
    "Abbiamo anche una sede a Trumello, in provincia di Pavia, e la sede principale a Mansuè, in provincia di Treviso. Il gruppo di sviluppo è uno solo: chi vi segue a Milano lavora con le stesse persone che hanno costruito gestionali per aziende venete, friulane e lombarde.",
    "Il resto del lavoro lo seguiamo in videochiamata e con un ambiente di prova sempre aggiornato: vedete il gestionale crescere giorno per giorno, non solo alla consegna."]},
  {"id":"milano","tipo":"testo","eyebrow":"Il contesto","h2":f"A Milano il problema è {G}la velocità, non le funzioni{_G}",
   "corpo":["Le aziende milanesi non hanno bisogno di un programma con mille funzioni: hanno bisogno di rispondere in fretta a clienti che si aspettano preventivi in giornata, consegne puntuali e informazioni sempre disponibili. Quando i dati vivono in tre programmi e cinque fogli Excel, quella velocità si perde.",
    "Un gestionale su misura mette ordine partendo dal punto che vi rallenta di più: il magazzino che non torna, le commesse di cui non si conosce il margine, i commerciali che non aggiornano il CRM. Partiamo da lì, con una prima versione in 1-2 settimane, e aggiungiamo il resto solo quando serve."]},
  {"id":"passi","tipo":"passi","eyebrow":"Come lavoriamo","h2":f"Dalla prima chiamata {G}al gestionale in uso{_G}",
   "corpo":[("Incontro","In azienda o in videochiamata: dove si perde tempo, quali dati si copiano, cosa manca."),
    ("Demo in 48-72 ore","In 48-72 ore vi mostriamo una demo funzionante sul vostro caso, non una presentazione."),
    ("Prima versione in 1-2 settimane","Il primo modulo va in uso con i vostri dati, importati da Excel e dai programmi esistenti."),
    ("Assistenza con contratto","Aggiornamenti, backup e nuove funzioni con un referente che conosce il vostro gestionale.")]}],
 "faqtitle":f"Le domande {G}delle aziende milanesi.{_G}",
 "faq":[("Venite in azienda a Milano?","Sì. I nostri uffici sono a Vermezzo con Zelo, a circa mezz'ora dal centro di Milano: il primo incontro e la formazione li facciamo volentieri da voi.")]+STD_FAQ_G+
  [("Lavorate anche nell'hinterland?","Sì: Corsico, Assago, Rozzano, Abbiategrasso, Magenta, Rho, Legnano e tutta la provincia, oltre a Pavia e Lodi.")],
 "ctabox":CTA_G,"altrititle":"Pagine collegate",
 "altri":[("Siti web a Milano","/realizzazione-siti-web-milano/"),("Gestionali su misura a Pavia","/gestionali-su-misura-pavia/"),("Gestionale personalizzato","/gestionale-personalizzato/"),("Software gestionale magazzino","/software-gestionale-magazzino/"),("CRM aziendale","/crm-aziendale/"),("Portale rivenditori B2B","/portale-rivenditori-b2b/"),("Allestimenti fieristici a Milano","/allestimenti-fieristici-milano/")],
 "svc":svc("Gestionali su misura a Milano","Sviluppo di software gestionale su misura","Software gestionale, di magazzino e CRM su misura per aziende di Milano e provincia, con uffici a Vermezzo con Zelo (MI).",
   ["Gestionale di magazzino","Gestionale commesse","CRM aziendale","Portale B2B","Cruscotti aziendali"],"Milano")})

# ===================================================== SITI MILANO
PAGINE.append({
 "lang":"it","url":"/realizzazione-siti-web-milano/",
 "title":"Realizzazione siti web a Milano: web agency",
 "desc":"Realizzazione siti web ed e-commerce a Milano e hinterland: veloci, ottimizzati per Google, prezzo chiaro. Demo in 24 ore, online in 1-2 settimane.",
 "ogtitle":"Realizzazione siti web a Milano — Danova Tech",
 "ogdesc":"Siti web ed e-commerce per aziende milanesi, demo in 24 ore e online in 1-2 settimane.",
 "crumbs":[WEB,("Siti web a Milano",None)],
 "eyebrow":"Web agency · Milano",
 "h1":f"Realizzazione siti web a Milano: {G}demo in 24 ore, online in 1-2 settimane.{_G}",
 "lead":"Siti aziendali, landing page ed e-commerce per le aziende di Milano e dell'hinterland, scritti in codice su misura: veloci, ottimizzati per Google e facili da aggiornare. Lavoriamo dai nostri uffici di Vermezzo con Zelo, a sud-ovest della città.",
 "cta1":"Chiedi la demo","cta2":"Cosa realizziamo",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa realizziamo","h2":f"Siti fatti per {G}portare contatti{_G}",
   "corpo":[("Siti aziendali","Chi siete, cosa fate, perché scegliere voi: poche pagine chiare, scritte per i clienti e per Google."),
    ("E-commerce","Negozi online collegati al magazzino e al gestionale, con pagamenti, spedizioni e fatturazione."),
    ("Landing page","Pagine per campagne Google Ads e Meta, pensate per trasformare i clic in richieste."),
    ("Siti multilingua","Italiano, inglese, tedesco, francese e spagnolo, con la SEO impostata per ogni lingua."),
    ("Restyling","Rifacciamo il vostro sito senza perdere le posizioni su Google, con i redirect fatti bene."),
    ("SEO locale","Pagine e scheda Google pensate per chi cerca un'azienda come la vostra a Milano e dintorni.")]},
  {"id":"codice","tipo":"testo","eyebrow":"Perché codice su misura","h2":f"Niente temi pesanti, {G}siti che si caricano subito{_G}",
   "corpo":["A Milano la concorrenza online è altissima, e Google premia i siti veloci e chiari. Per questo scriviamo i siti in codice su misura invece di usare temi carichi di funzioni inutili: pagine leggere, che si aprono in un attimo anche dal telefono, con i dati strutturati che aiutano Google a capire chi siete.",
    "Il sito resta vostro, ed è pensato per crescere: nuove pagine di servizio, una sezione di guide, una versione in inglese per i clienti esteri. Lo aggiorniamo noi con un contratto di assistenza, oppure vi mostriamo come fare da soli."]},
  {"id":"zona","tipo":"testo","eyebrow":"Dove lavoriamo","h2":f"Milano città {G}e tutto l'hinterland{_G}",
   "corpo":["Dagli uffici di Vermezzo con Zelo seguiamo aziende a Milano, Corsico, Buccinasco, Assago, Rozzano, Abbiategrasso, Magenta, Rho, Legnano e nel resto della provincia. Il primo incontro lo facciamo volentieri di persona; il resto in videochiamata, che per un progetto di sito è il modo più rapido di lavorare.",
    "Siamo anche a Trumello, in provincia di Pavia, e la nostra sede principale è a Mansuè, in provincia di Treviso. Oltre ai siti progettiamo gestionali, app e stand fieristici: se esponete a Fiera Milano Rho, sito e stand possono raccontare la stessa storia."]},
  {"id":"passi","tipo":"passi","eyebrow":"Come lavoriamo","h2":f"Dalla prima chiamata {G}al sito online{_G}",
   "corpo":[("Chiamata","Cosa vendete, a chi, cosa non funziona nel sito attuale."),("Demo in 24 ore","Vi mandiamo la home page in bozza sul vostro caso."),
    ("Online in 1-2 settimane","Testi, immagini, SEO di base, scheda Google e analisi delle visite."),("Assistenza","Aggiornamenti, backup e modifiche con un contratto chiaro.")]}],
 "faqtitle":f"Le domande {G}delle aziende milanesi.{_G}",
 "faq":[("Siete una web agency di Milano?","Abbiamo uffici a Vermezzo con Zelo, in provincia di Milano, a circa mezz'ora dal centro: seguiamo aziende di Milano e dell'hinterland di persona e in videochiamata.")]+STD_FAQ_W+
  [("Fate anche e-commerce?","Sì, collegati al magazzino e al gestionale, con pagamenti, spedizioni e fatture automatiche.")],
 "ctabox":CTA_W,"altrititle":"Pagine collegate",
 "altri":[("Gestionali su misura a Milano","/gestionali-su-misura-milano/"),("Siti web a Pavia","/realizzazione-siti-web-pavia/"),("Realizzazione siti internet","/realizzazione-siti-internet/"),("Realizzazione e-commerce","/realizzazione-ecommerce/"),("Restyling sito web","/restyling-sito-web/"),("SEO locale","/seo-locale/"),("Allestimenti fieristici a Milano","/allestimenti-fieristici-milano/")],
 "svc":svc("Realizzazione siti web a Milano","Realizzazione di siti web ed e-commerce","Siti web aziendali, landing page ed e-commerce in codice su misura per aziende di Milano e provincia, con uffici a Vermezzo con Zelo (MI).",
   ["Sito web aziendale","E-commerce","Landing page","Sito multilingua","Restyling sito web"],"Milano")})

# ===================================================== GESTIONALI PAVIA
PAGINE.append({
 "lang":"it","url":"/gestionali-su-misura-pavia/",
 "title":"Gestionali su misura a Pavia e in Lomellina",
 "desc":"Software gestionale su misura per aziende di Pavia, Vigevano, Lomellina e Oltrepò: magazzino, produzione, commesse. Sede a Trumello, demo in 24 ore.",
 "ogtitle":"Gestionali su misura a Pavia — Danova Tech",
 "ogdesc":"Gestionali, software di produzione e magazzino su misura per le aziende pavesi, dalla nostra sede di Trumello.",
 "crumbs":[GEST,("Gestionali su misura a Pavia",None)],
 "eyebrow":"Pavia · Lomellina · Oltrepò",
 "h1":f"Gestionali su misura a Pavia: {G}dalla nostra sede di Trumello.{_G}",
 "lead":"Software gestionale, di produzione e di magazzino per le aziende della provincia di Pavia, dalla Lomellina all'Oltrepò. Abbiamo produzione e uffici a Trumello, fra Garlasco e Mortara: siamo vicini, e in 48-72 ore vi mostriamo una demo funzionante.",
 "cta1":"Raccontateci come lavorate","cta2":"Cosa costruiamo",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa costruiamo","h2":f"I gestionali per {G}le aziende pavesi{_G}",
   "corpo":[("Produzione e officina","Fasi di lavoro, tempi, macchine e avanzamento delle commesse per le aziende meccaniche e manifatturiere della provincia."),
    ("Magazzino e lotti","Giacenze, lotti, scadenze e tracciabilità per l'agroalimentare: riso, vino, conserve e prodotti tipici."),
    ("Commesse e preventivi","Dal preventivo alla fattura, con i margini reali di ogni lavoro, per impiantisti, edilizia e servizi."),
    ("Vendite e agenti","Ordini, listini e clienti consultabili dal telefono, per chi vende in Italia e all'estero."),
    ("Cantine e aziende agricole","Vendemmia, lotti, imbottigliamento e vendite per le cantine dell'Oltrepò Pavese."),
    ("Cruscotti per il titolare","Ordini, fatturato, scorte e margini in una schermata, aggiornati in tempo reale.")]},
  {"id":"vicini","tipo":"testo","eyebrow":"Dove siamo","h2":f"Trumello, {G}nel cuore della Lomellina{_G}",
   "corpo":["La nostra sede pavese è a Trumello, fra Garlasco, Mortara e Vigevano, a circa mezz'ora da Pavia. Ci lavorano la produzione degli allestimenti e gli uffici: per le aziende della zona significa un fornitore che può essere in azienda in giornata, per l'analisi iniziale, la formazione o un intervento.",
    "In Lombardia abbiamo anche gli uffici di Vermezzo con Zelo (MI) e la sede principale è a Mansuè (TV). Il gruppo di sviluppo è uno solo, e ogni progetto ha un referente unico dall'analisi all'assistenza."]},
  {"id":"pavia","tipo":"testo","eyebrow":"Il territorio","h2":f"Calzature, meccanica, riso e vino: {G}aziende diverse, problemi simili{_G}",
   "corpo":["La provincia di Pavia ha un tessuto produttivo vario: la meccanica e il calzaturiero del Vigevanese, il riso della Lomellina, il vino dell'Oltrepò, servizi e studi professionali a Pavia città. Settori diversi, ma lo stesso problema ricorre in quasi tutte le aziende che visitiamo: i dati sono sparsi fra un gestionale vecchio, fogli Excel e messaggi, e nessuno ha il quadro completo.",
    "Un gestionale su misura parte dal punto che fa perdere più tempo, che sia la tracciabilità dei lotti, l'avanzamento della produzione o le commesse, e lo mette in uso in 1-2 settimane. Poi cresce un modulo alla volta, senza fermare il lavoro."]},
  {"id":"passi","tipo":"passi","eyebrow":"Come lavoriamo","h2":f"Dalla prima chiamata {G}al gestionale in uso{_G}",
   "corpo":[("Incontro in azienda","Da Trumello veniamo da voi: come lavorate, dove si perde tempo, cosa manca."),
    ("Demo in 48-72 ore","Una demo funzionante sul vostro caso, in 48-72 ore."),
    ("Prima versione in 1-2 settimane","Il primo modulo in uso con i vostri dati, importati da Excel e dai programmi esistenti."),
    ("Assistenza con contratto","Aggiornamenti, backup e nuove funzioni, con un referente vicino.")]}],
 "faqtitle":f"Le domande {G}delle aziende pavesi.{_G}",
 "faq":[("Dove siete in provincia di Pavia?","A Trumello, fra Garlasco e Mortara: seguiamo di persona aziende a Pavia, Vigevano, Mortara, Voghera, Stradella e in tutta la provincia.")]+STD_FAQ_G+
  [("Fate gestionali per cantine e aziende agricole?","Sì: lotti, vendemmia, imbottigliamento, magazzino e vendite, con la tracciabilità richiesta dalla normativa.")],
 "ctabox":CTA_G,"altrititle":"Pagine collegate",
 "altri":[("Siti web a Pavia","/realizzazione-siti-web-pavia/"),("Gestionali su misura a Milano","/gestionali-su-misura-milano/"),("Software gestionale produzione","/software-gestionale-produzione/"),("Gestionale agroalimentare","/software-gestionale-agroalimentare/"),("Software MES","/software-mes-produzione/"),("Gestionale metalmeccanica","/software-gestionale-metalmeccanica/"),("Allestimenti fieristici in Lombardia","/allestimenti-fieristici-lombardia/")],
 "svc":svc("Gestionali su misura a Pavia","Sviluppo di software gestionale su misura","Software gestionale, di produzione e di magazzino su misura per aziende della provincia di Pavia, con sede a Trumello (PV).",
   ["Gestionale di produzione","Gestionale di magazzino e lotti","Gestionale per cantine","Gestionale commesse","Cruscotti aziendali"],"Pavia")})

# ===================================================== SITI PAVIA
PAGINE.append({
 "lang":"it","url":"/realizzazione-siti-web-pavia/",
 "title":"Realizzazione siti web a Pavia e Vigevano",
 "desc":"Realizzazione siti web ed e-commerce a Pavia, Vigevano, Lomellina e Oltrepò: veloci e ottimizzati per Google. Sede a Trumello, demo in 24 ore.",
 "ogtitle":"Realizzazione siti web a Pavia — Danova Tech",
 "ogdesc":"Siti web ed e-commerce per aziende pavesi, dalla nostra sede di Trumello: demo in 24 ore, online in 1-2 settimane.",
 "crumbs":[WEB,("Siti web a Pavia",None)],
 "eyebrow":"Web agency · Pavia",
 "h1":f"Realizzazione siti web a Pavia: {G}demo in 24 ore, online in 1-2 settimane.{_G}",
 "lead":"Siti aziendali, e-commerce e siti per cantine, aziende agricole e attività della provincia di Pavia. Siamo a Trumello, in Lomellina: scriviamo siti veloci e ottimizzati per Google, e vi seguiamo anche dopo la consegna.",
 "cta1":"Chiedi la demo","cta2":"Cosa realizziamo",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa realizziamo","h2":f"Siti per {G}le aziende pavesi{_G}",
   "corpo":[("Siti aziendali","Per aziende manifatturiere, meccaniche e di servizi: chi siete, cosa fate, come contattarvi."),
    ("Siti per cantine","Per le cantine dell'Oltrepò: vini, visite, degustazioni e vendita online, anche in inglese e tedesco."),
    ("E-commerce","Negozi online per prodotti tipici, riso, vino e articoli artigianali, collegati al magazzino."),
    ("Siti per attività locali","Ristoranti, agriturismi, studi e negozi: orari, prenotazioni, scheda Google curata."),
    ("Restyling","Rifacciamo il sito senza perdere posizioni su Google."),
    ("SEO locale","Per farvi trovare da chi cerca un'azienda come la vostra a Pavia, Vigevano, Voghera e dintorni.")]},
  {"id":"vicini","tipo":"testo","eyebrow":"Dove siamo","h2":f"Una sede in Lomellina, {G}a mezz'ora da Pavia{_G}",
   "corpo":["Siamo a Trumello, fra Garlasco e Mortara: seguiamo di persona aziende e attività a Pavia, Vigevano, Mortara, Voghera, Stradella e nel resto della provincia. Il primo incontro lo facciamo volentieri da voi, il resto in videochiamata.",
    "Scriviamo i siti in codice su misura, senza temi pesanti: pagine che si aprono subito anche dal telefono, con i dati strutturati che aiutano Google. Il sito resta vostro, e lo seguiamo con un contratto di assistenza se lo desiderate."]},
  {"id":"passi","tipo":"passi","eyebrow":"Come lavoriamo","h2":f"Dalla prima chiamata {G}al sito online{_G}",
   "corpo":[("Chiamata o incontro","Cosa fate, a chi vi rivolgete, cosa non va nel sito attuale."),("Demo in 24 ore","La home page in bozza sul vostro caso, entro il giorno dopo."),
    ("Online in 1-2 settimane","Testi, immagini, SEO di base, scheda Google e analisi delle visite."),("Assistenza","Aggiornamenti, backup e modifiche con un contratto chiaro.")]}],
 "faqtitle":f"Le domande {G}delle aziende pavesi.{_G}",
 "faq":[("Avete una sede in provincia di Pavia?","Sì, a Trumello, in Lomellina, fra Garlasco e Mortara. In Lombardia abbiamo anche gli uffici di Vermezzo con Zelo (MI).")]+STD_FAQ_W+
  [("Fate siti per cantine e agriturismi?","Sì, con schede dei vini o delle camere, prenotazioni, vendita online e versioni in lingua per i visitatori stranieri.")],
 "ctabox":CTA_W,"altrititle":"Pagine collegate",
 "altri":[("Gestionali su misura a Pavia","/gestionali-su-misura-pavia/"),("Siti web a Milano","/realizzazione-siti-web-milano/"),("Siti web per hotel","/siti-web-per-hotel/"),("Siti web per ristoranti","/siti-web-per-ristoranti/"),("Realizzazione e-commerce","/realizzazione-ecommerce/"),("SEO locale","/seo-locale/")],
 "svc":svc("Realizzazione siti web a Pavia","Realizzazione di siti web ed e-commerce","Siti web aziendali, e-commerce e siti per cantine e attività locali in provincia di Pavia, con sede a Trumello (PV).",
   ["Sito web aziendale","Sito per cantine","E-commerce","Sito per attività locali","Restyling sito web"],"Pavia")})
