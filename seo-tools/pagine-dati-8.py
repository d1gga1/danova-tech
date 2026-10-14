# -*- coding: utf-8 -*-
"""Pagine nuove del 14 ottobre 2026 (ottavo giro): gestionale personalizzato e software su misura per ogni azienda,
   da ricerche Keyword Planner non ancora coperte (cartella keywords/planner-2026-10).
   Dati confermati dal titolare: prima versione in pochi giorni o poche settimane; integrazione con Excel e programmi
   esistenti; funziona da PC, tablet e telefono; canone mensile o pagamento unico a scelta del cliente.
   Uso:  python3 seo-tools/pagine-build-2.py pagine-dati-8.py  &&  python3 seo-tools/sumisura.py"""
OGGI = "2026-10-14"
IT = [{"@type":"Country","name":"Italia"}]
LG = ["Italian","English","German"]
PAGINE = []
G = '<span class="grad">'; _G = '</span>'
GEST = ("Gestionali e CRM", "/servizi/gestionali-crm/")
APP = ("App su misura", "/servizi/app-su-misura/")
WEB = ("Siti web ed e-commerce", "/servizi/siti-web-ecommerce/")
AUT = ("Software e automazioni", "/servizi/software-automazioni/")
CTA_GEST = {"h2": "Ci raccontate come lavorate oggi?", "p": "Mezz'ora per capire dove perdete ore ogni settimana e cosa servirebbe per recuperarle. Poi vi diciamo cosa costruiremmo e quanto costa, per iscritto.", "btn": "Prenota la chiamata"}
def svc(name, typ, desc, cat): return {"name": name, "type": typ, "desc": desc, "area": IT, "lingue": LG, "catalogo": cat}

# ============================================================ GESTIONALE PERSONALIZZATO
PAGINE.append({
 "lang":"it", "url":"/gestionale-personalizzato/",
 "title":"Gestionale personalizzato: solo vostro, su misura",
 "desc":"Gestionale personalizzato, costruito sui processi della vostra azienda e solo per voi: niente programma uguale per tutti. Prima versione in pochi giorni.",
 "ogtitle":"Gestionale personalizzato — Danova Tech",
 "ogdesc":"Il vostro gestionale, solo vostro: costruito su come lavorate, non su come lavora la media delle aziende.",
 "crumbs":[GEST, ("Gestionale personalizzato", None)],
 "eyebrow":"Gestionale su misura",
 "h1":f"Gestionale personalizzato: {G}il vostro, e di nessun altro.{_G}",
 "lead":"Un gestionale commerciale è scritto per andare bene a tutti, e quindi costringe tutti a lavorare allo stesso modo. Un gestionale personalizzato fa il contrario: nasce da come lavora la vostra azienda, con i vostri passaggi, i vostri nomi e i vostri documenti, ed esiste solo per voi.",
 "cta1":"Raccontateci come lavorate", "cta2":"Perché personalizzato",
 "sezioni":[
  {"id":"perche","tipo":"testo","eyebrow":"Il problema","h2":f"Perché i gestionali {G}uguali per tutti non bastano{_G}",
   "corpo":["Ogni azienda ha un modo suo di lavorare: come nasce un ordine, chi approva un preventivo, come si chiude una commessa, cosa deve vedere il magazziniere e cosa il titolare. I programmi commerciali offrono centinaia di funzioni pensate per la media delle aziende, e lasciano fuori proprio i passaggi che vi rendono diversi.",
    "Il risultato si vede in quasi tutte le aziende che visitiamo: il gestionale fa una parte del lavoro, e il resto vive in fogli Excel, gruppi WhatsApp e post-it. Ogni dato si copia due o tre volte, e nessuno ha il quadro completo.",
    "Un gestionale personalizzato rimette tutto in un unico posto, costruito attorno a voi. Non dovete adattarvi al software: è il software ad adattarsi a voi, e a cambiare quando cambia il vostro modo di lavorare."]},
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa può gestire","h2":f"Quello che serve a voi, {G}niente di più.{_G}",
   "corpo":[("Ordini, commesse e preventivi","Dal primo contatto alla fattura, con gli stati e le approvazioni che usate davvero."),
    ("Magazzino e acquisti","Giacenze, lotti, ubicazioni, riordini ai fornitori, codici a barre se servono."),
    ("Produzione e lavorazioni","Fasi, tempi, macchine, operatori, avanzamento in tempo reale."),
    ("Clienti e fornitori","Anagrafiche, storico, documenti, scadenze, promemoria."),
    ("Personale e attività","Presenze, rapportini, interventi, calendari, ruoli e permessi."),
    ("Report e cruscotti","I numeri che guardate ogni giorno, in una schermata, senza esportare in Excel.")]},
  {"id":"passi","tipo":"passi","eyebrow":"Come lavoriamo","h2":f"Dalla prima chiamata {G}al gestionale in uso{_G}",
   "corpo":[("Analisi","Veniamo a vedere come lavorate, o lo facciamo in videochiamata: dove si perde tempo, quali dati si copiano, cosa manca."),
    ("Prima versione","Partiamo dal pezzo che vi fa perdere più ore: una prima versione funzionante arriva in pochi giorni o in poche settimane."),
    ("I vostri dati","Importiamo Excel e archivi esistenti e colleghiamo il gestionale ai programmi che usate già, come fatturazione e contabilità."),
    ("Uso e formazione","Il gestionale si apre da PC, tablet e telefono. Formiamo chi lo usa, poi aggiungiamo un modulo alla volta.")]},
  {"id":"costi","tipo":"testo","eyebrow":"Costi","h2":f"Canone mensile {G}o pagamento unico{_G}",
   "corpo":["Potete scegliere fra un canone mensile con hosting, aggiornamenti e assistenza inclusi, oppure un pagamento unico. Un gestionale su misura parte da 1.500 € IVA inclusa per il primo modulo, come indicato nel nostro <a href=\"/prezzi/\">listino prezzi</a>; la cifra esatta la fissiamo per iscritto dopo l'analisi.",
    "In molti casi un gestionale personalizzato costa meno, nel tempo, di un programma commerciale con licenze per utente, moduli aggiuntivi e consulenze per adattarlo: pagate solo le funzioni che usate. Trovate un confronto completo nella guida <a href=\"/guide/gestionale-su-misura-o-standard/\">gestionale su misura o standard</a>."]}],
 "faqtitle":f"Le domande {G}sul gestionale personalizzato.{_G}",
 "faq":[("Che differenza c'è fra un gestionale personalizzato e uno commerciale?","Il gestionale commerciale è lo stesso programma per migliaia di aziende, con impostazioni da configurare. Quello personalizzato è costruito sui processi della vostra azienda ed esiste solo per voi: schermate, campi e passaggi sono i vostri."),
  ("Quanto tempo serve?","Una prima versione funzionante arriva in pochi giorni o in poche settimane, a seconda del primo modulo. Poi il gestionale cresce a fasi, senza fermare il lavoro."),
  ("Possiamo recuperare i dati che abbiamo in Excel?","Sì, importiamo fogli Excel e archivi esistenti, e colleghiamo il gestionale ai programmi che usate già."),
  ("Funziona anche da tablet e telefono?","Sì, si apre dal browser o come app, da PC, tablet e telefono, con utenti e permessi diversi."),
  ("C'è un canone mensile?","Scegliete voi: canone mensile con tutto incluso oppure pagamento unico. Le cifre sono nel listino prezzi."),
  ("È adatto anche a una piccola azienda?","Sì: si parte da un solo modulo, quello che fa risparmiare più tempo, e si aggiunge il resto solo quando serve.")],
 "ctabox":CTA_GEST, "altrititle":"Pagine collegate",
 "altri":[("Gestionale aziendale su misura","/software-gestionale-aziendale/"),("Gestionale su misura o standard","/guide/gestionale-su-misura-o-standard/"),("ERP per piccole aziende","/erp-per-piccole-aziende/"),("Dashboard aziendale","/dashboard-aziendale/"),("Sostituire Excel con un gestionale","/guide/sostituire-excel-con-un-gestionale/"),("Quanto costa un gestionale","/quanto-costa-un-gestionale/"),("Prezzi","/prezzi/")],
 "svc":svc("Gestionale personalizzato","Sviluppo di software gestionale su misura","Software gestionale personalizzato costruito sui processi della singola azienda: ordini, magazzino, produzione, clienti, personale e report, da PC, tablet e telefono.",["Analisi dei processi","Prima versione in pochi giorni o settimane","Importazione dati da Excel","Integrazione con programmi esistenti","Canone mensile o pagamento unico"])
})

# ============================================================ GUIDA SU MISURA O STANDARD
PAGINE.append({
 "lang":"it", "url":"/guide/gestionale-su-misura-o-standard/",
 "title":"Gestionale su misura o standard: quale scegliere",
 "desc":"Gestionale su misura o standard commerciale: differenze, costi nel tempo, licenze, adattabilità e quando conviene l'uno o l'altro. Guida pratica.",
 "ogtitle":"Gestionale su misura o standard? — Danova Tech",
 "ogdesc":"Un confronto onesto: quando basta un programma commerciale e quando conviene un gestionale costruito per voi.",
 "crumbs":[("Guide","/guide/"), ("Gestionale su misura o standard", None)],
 "eyebrow":"Guida",
 "h1":f"Gestionale su misura o standard: {G}quale scegliere, senza slogan.{_G}",
 "lead":"Un gestionale standard è un programma uguale per tutte le aziende che lo comprano; un gestionale su misura è costruito per una sola azienda. Nessuno dei due è sempre la scelta giusta: dipende da quanto il vostro modo di lavorare è particolare, da quante persone lo useranno e da quanto vi costa oggi adattarvi al software.",
 "cta1":"Chiedeteci un parere", "cta2":"Il confronto",
 "sezioni":[
  {"id":"confronto","tipo":"cards","eyebrow":"Il confronto","h2":f"Le differenze {G}che contano davvero{_G}",
   "corpo":[("Adattamento","Lo standard si configura entro i limiti previsti dal produttore. Il su misura fa esattamente quello che serve a voi."),
    ("Funzioni","Lo standard ha centinaia di funzioni, molte inutili per voi. Il su misura ha solo quelle che usate."),
    ("Tempi di partenza","Lo standard si installa subito, ma adattarlo richiede tempo. Il su misura parte con una prima versione in pochi giorni o settimane e cresce a fasi."),
    ("Costi nel tempo","Lo standard spesso ha licenze per utente e moduli a pagamento. Il su misura si paga con canone mensile o una volta sola, a vostra scelta."),
    ("Evoluzione","Lo standard cambia quando decide il produttore. Il su misura cambia quando cambiate voi."),
    ("Dipendenza","Con lo standard dipendete dalla roadmap di un produttore. Con il su misura avete un fornitore che conosce i vostri processi.")]},
  {"id":"quando-standard","tipo":"testo","eyebrow":"Quando basta lo standard","h2":f"Quando un programma commerciale {G}va benissimo{_G}",
   "corpo":["Se la vostra attività è simile a quella di migliaia di altre, avete pochi utenti e vi servono funzioni classiche (fatture, prima nota, un magazzino semplice), un programma commerciale spesso basta ed è la scelta più economica. Ve lo diciamo anche noi, quando è così.",
    "Lo standard conviene meno quando state già usando tre o quattro strumenti diversi per fare un lavoro solo, quando il programma vi obbliga a passaggi inutili o quando i dati veri vivono in fogli Excel paralleli."]},
  {"id":"quando-misura","tipo":"testo","eyebrow":"Quando conviene il su misura","h2":f"I segnali che {G}vi serve un gestionale vostro{_G}",
   "corpo":["Ogni settimana qualcuno copia gli stessi dati da un programma a un altro. Il titolare deve chiedere a tre persone per sapere a che punto è una commessa. Il magazzino vero è in un foglio Excel. Il programma che avete non gestisce un passaggio che per voi è fondamentale, e lo fate a mano.",
    "In questi casi un gestionale su misura recupera ore ogni settimana e riduce gli errori. Si può partire da un solo modulo, collegandolo ai programmi che già usate, e aggiungere il resto solo quando serve. Vedete come lavoriamo nella pagina sul <a href=\"/gestionale-personalizzato/\">gestionale personalizzato</a>."]}],
 "faqtitle":f"Le domande {G}più frequenti.{_G}",
 "faq":[("Un gestionale su misura costa più di uno standard?","All'inizio può costare di più, nel tempo spesso meno: niente licenze per utente né moduli che non usate. Potete scegliere fra canone mensile e pagamento unico."),
  ("Quanto tempo serve per un gestionale su misura?","Una prima versione funzionante arriva in pochi giorni o in poche settimane; poi il gestionale cresce a fasi."),
  ("Posso tenere il programma di fatturazione che uso già?","Sì, spesso conviene: colleghiamo il gestionale su misura ai programmi esistenti invece di sostituirli tutti."),
  ("E se l'azienda cresce?","Il gestionale su misura cresce con voi: nuovi moduli, utenti e collegamenti si aggiungono uno alla volta.")],
 "ctabox":CTA_GEST, "altrititle":"Pagine collegate",
 "altri":[("Gestionale personalizzato","/gestionale-personalizzato/"),("Come scegliere un gestionale","/guide/come-scegliere-un-gestionale/"),("Cos'è un gestionale","/guide/cos-e-un-gestionale/"),("Differenza fra gestionale, ERP e CRM","/guide/differenza-gestionale-erp-crm/"),("Quanto costa un gestionale","/quanto-costa-un-gestionale/")],
 "svc":svc("Consulenza sulla scelta del gestionale","Consulenza software gestionale","Confronto fra gestionale su misura e gestionale standard commerciale, con analisi dei processi aziendali.",["Analisi dei processi","Gestionale su misura","Integrazione con programmi esistenti"])
})

# ============================================================ GESTIONALE PER ASSOCIAZIONI
PAGINE.append({
 "lang":"it", "url":"/gestionale-per-associazioni/",
 "title":"Gestionale per associazioni e ASD su misura | Danova Tech",
 "desc":"Gestionale per associazioni, ASD e società sportive su misura: soci e tesserati, quote, certificati medici, corsi, presenze e comunicazioni, anche da app.",
 "ogtitle":"Gestionale per associazioni e ASD — Danova Tech",
 "ogdesc":"Soci, quote, certificati, corsi e comunicazioni in un unico programma, costruito su come funziona la vostra associazione.",
 "crumbs":[GEST, ("Associazioni e ASD", None)],
 "eyebrow":"Software per associazioni",
 "h1":f"Gestionale per associazioni e ASD: {G}soci, quote e corsi in un posto solo.{_G}",
 "lead":"Nelle associazioni e nelle società sportive il lavoro amministrativo lo fanno spesso volontari, la sera, su fogli Excel che passano di mano in mano. Un gestionale costruito sulla vostra associazione mette in ordine soci, quote, certificati e corsi, e libera tempo per le attività vere.",
 "cta1":"Parliamo della vostra associazione", "cta2":"Cosa fa",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa fa","h2":f"Il lavoro della segreteria, {G}senza fogli sparsi{_G}",
   "corpo":[("Soci e tesserati","Anagrafiche, tessere, rinnovi, storico, ruoli nel consiglio direttivo."),
    ("Quote e pagamenti","Quote annuali e mensili, corsi a pagamento, solleciti automatici e ricevute."),
    ("Certificati medici","Scadenze dei certificati per ogni atleta, con avvisi prima che scadano."),
    ("Corsi e presenze","Iscrizioni ai corsi, gruppi, istruttori, presenze dal telefono."),
    ("Comunicazioni","Email e messaggi ai soci, per gruppo o per corso, senza liste copiate a mano."),
    ("Area soci","Iscrizione online, pagamento, documenti e calendario per i soci, da telefono.")]},
  {"id":"perche","tipo":"testo","eyebrow":"Perché su misura","h2":f"Ogni associazione {G}funziona a modo suo{_G}",
   "corpo":["Una ASD con dieci corsi e trecento atleti non lavora come un'associazione culturale con cento soci o una polisportiva con cinque discipline. I programmi pronti per associazioni coprono i casi più comuni; quando i vostri passaggi sono diversi, si finisce di nuovo su Excel.",
    "Costruiamo il gestionale sulla vostra associazione: si parte dal modulo che fa perdere più tempo (spesso soci e quote), importando gli elenchi che avete già, e si aggiunge il resto un pezzo alla volta. Si usa da PC, tablet e telefono, anche dagli istruttori in palestra. Per gli aspetti fiscali e statutari vi coordinate con il vostro commercialista: il gestionale vi dà i dati in ordine."]},
  {"id":"passi","tipo":"passi","eyebrow":"Come lavoriamo","h2":f"Dagli elenchi in Excel {G}al gestionale in uso{_G}",
   "corpo":[("Un incontro con la segreteria","Capire come iscrivete, incassate, comunicate."),
    ("Prima versione","Soci e quote, con i vostri dati importati, in pochi giorni o poche settimane."),
    ("Area soci e app","Iscrizioni, pagamenti e comunicazioni anche dal telefono."),
    ("Gli altri moduli","Corsi, presenze, certificati, report per il consiglio.")]}],
 "faqtitle":f"Le domande {G}sul gestionale per associazioni.{_G}",
 "faq":[("Va bene anche per una ASD o una società sportiva?","Sì: tesserati, corsi, istruttori, certificati medici, quote e presenze sono proprio i casi in cui serve di più."),
  ("Possiamo importare i soci che abbiamo in Excel?","Sì, importiamo gli elenchi esistenti, così non si ricomincia da zero."),
  ("I soci possono iscriversi e pagare online?","Sì, con un'area soci dal telefono per iscrizione, pagamento e documenti."),
  ("Quanto costa?","Potete scegliere fra canone mensile e pagamento unico; trovate le cifre nel listino prezzi e vi diamo un preventivo scritto dopo l'incontro.")],
 "ctabox":CTA_GEST, "altrititle":"Pagine collegate",
 "altri":[("Gestionale personalizzato","/gestionale-personalizzato/"),("Gestionale per palestre","/gestionale-palestra/"),("App per prenotazioni","/app-prenotazioni/"),("App per personal trainer","/app-per-personal-trainer/"),("Prezzi","/prezzi/")],
 "svc":svc("Gestionale per associazioni e ASD","Software gestionale per associazioni","Gestionale su misura per associazioni, ASD e società sportive: soci e tesserati, quote, certificati medici, corsi, presenze, comunicazioni e area soci.",["Gestione soci e quote","Certificati medici","Corsi e presenze","Area soci online"])
})

# ============================================================ SOFTWARE TICKETING
PAGINE.append({
 "lang":"it", "url":"/software-ticketing/",
 "title":"Software ticketing su misura per assistenza clienti",
 "desc":"Software di ticketing su misura per assistenza clienti: richieste da email, form e WhatsApp, priorità, SLA, assegnazioni, storico e report.",
 "ogtitle":"Software ticketing su misura — Danova Tech",
 "ogdesc":"Le richieste dei clienti in un solo posto, con priorità, responsabili e tempi di risposta sotto controllo.",
 "crumbs":[AUT, ("Software ticketing", None)],
 "eyebrow":"Help desk e assistenza",
 "h1":f"Software ticketing: {G}nessuna richiesta persa, nessun cliente dimenticato.{_G}",
 "lead":"Quando le richieste di assistenza arrivano da email, telefono, WhatsApp e moduli del sito, prima o poi qualcuna si perde. Un sistema di ticketing le raccoglie tutte, assegna un responsabile e una priorità, e vi fa vedere a che punto è ogni richiesta.",
 "cta1":"Parliamo del vostro servizio clienti", "cta2":"Cosa fa",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa fa","h2":f"Dall'arrivo della richiesta {G}alla chiusura{_G}",
   "corpo":[("Tutti i canali in uno","Email, modulo del sito, WhatsApp e telefonate registrate diventano ticket nello stesso elenco."),
    ("Priorità e SLA","Tempi di risposta per tipo di cliente o di problema, con avvisi prima della scadenza."),
    ("Assegnazioni","Ogni ticket ha un responsabile; si passa a un collega senza perdere la storia."),
    ("Storico per cliente","Tutte le richieste di un cliente, i prodotti, gli interventi e i documenti."),
    ("Area clienti","Il cliente apre e segue le sue richieste da un portale, senza telefonare per sapere a che punto è."),
    ("Report","Tempi medi, ticket per tipo, carico per operatore, problemi ricorrenti.")]},
  {"id":"perche","tipo":"testo","eyebrow":"Perché su misura","h2":f"Il vostro servizio clienti {G}non è quello degli altri{_G}",
   "corpo":["I software di ticketing commerciali sono nati per i call center e i reparti IT. Se la vostra assistenza è tecnica, sul campo, legata a macchine, garanzie o contratti di manutenzione, servono campi, passaggi e collegamenti che un prodotto standard non ha.",
    "Costruiamo il ticketing sul vostro modo di lavorare e lo colleghiamo a quello che c'è già: anagrafica clienti, gestionale, rapportini d'intervento, fatturazione. Prima versione in pochi giorni o poche settimane, da PC, tablet e telefono."]}],
 "faqtitle":f"Le domande {G}sul software ticketing.{_G}",
 "faq":[("Cos'è un software di ticketing?","Un programma che trasforma ogni richiesta di assistenza in un ticket con responsabile, priorità e stato, così nessuna richiesta si perde e si vede sempre a che punto è."),
  ("Si collega a email e WhatsApp?","Sì, le richieste da email, modulo del sito e WhatsApp possono diventare ticket automaticamente."),
  ("Si può collegare ai rapportini dei tecnici?","Sì, un ticket può generare un intervento e il rapportino del tecnico chiude il ticket. Vedi l'<a href=\"/app-rapportini-di-lavoro/\">app rapportini</a>."),
  ("Quanto costa?","Potete scegliere fra canone mensile e pagamento unico; le cifre di partenza sono nel listino prezzi.")],
 "ctabox":CTA_GEST, "altrititle":"Pagine collegate",
 "altri":[("Software gestione interventi tecnici","/software-gestione-interventi-tecnici/"),("App rapportini di lavoro","/app-rapportini-di-lavoro/"),("CRM aziendale","/crm-aziendale/"),("WhatsApp aziendale","/whatsapp-aziendale/"),("Chatbot aziendale","/chatbot-aziendale/")],
 "svc":svc("Software ticketing su misura","Sviluppo software help desk e ticketing","Sistema di ticketing su misura per assistenza clienti: raccolta richieste da più canali, priorità, SLA, assegnazioni, area clienti e report.",["Ticketing multicanale","SLA e priorità","Area clienti","Integrazione con gestionale e rapportini"])
})

# ============================================================ SITO VETRINA
PAGINE.append({
 "lang":"it", "url":"/sito-vetrina/",
 "title":"Sito vetrina per aziende: cos'è e quanto costa | Danova Tech",
 "desc":"Sito vetrina per aziende e professionisti: cosa deve contenere, come farlo trovare su Google e quanto costa, in abbonamento o con pagamento unico.",
 "ogtitle":"Sito vetrina — Danova Tech",
 "ogdesc":"Un sito vetrina che si fa trovare e porta contatti, con prezzi scritti: abbonamento o pagamento unico.",
 "crumbs":[WEB, ("Sito vetrina", None)],
 "eyebrow":"Siti web",
 "h1":f"Sito vetrina: {G}poche pagine, fatte bene, che portano contatti.{_G}",
 "lead":"Un sito vetrina presenta l'azienda, i servizi e i contatti, senza vendita online. Sembra la cosa più semplice, ed è proprio per questo che molti siti vetrina non servono a niente: belli da vedere, invisibili su Google e senza un motivo per scrivervi.",
 "cta1":"Chiedi un preventivo", "cta2":"Cosa deve avere",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa deve avere","h2":f"Le pagine che {G}servono davvero{_G}",
   "corpo":[("Home chiara","Chi siete, cosa fate, per chi e dove, nelle prime righe."),
    ("Una pagina per servizio","Ogni servizio con la sua pagina: è così che Google vi trova per le ricerche giuste."),
    ("Lavori e prove","Foto, casi, recensioni: le prove che convincono un cliente nuovo."),
    ("Contatti facili","Telefono, WhatsApp, modulo e mappa, raggiungibili da ogni pagina."),
    ("Veloce sul telefono","La maggior parte delle visite arriva da smartphone: deve aprirsi subito."),
    ("SEO di base","Titoli, descrizioni, dati strutturati, sitemap e scheda Google Business.")]},
  {"id":"costi","tipo":"testo","eyebrow":"Quanto costa","h2":f"Abbonamento {G}o pagamento unico{_G}",
   "corpo":["Pubblichiamo i prezzi, cosa rara fra le agenzie: un sito vetrina costa 24,80 € al mese in abbonamento (minimo 24 mesi, con dominio, hosting, manutenzione e modifiche inclusi) oppure 350 € con pagamento unico, più 150 € per l'ottimizzazione SEO iniziale. Tutti i prezzi sono IVA inclusa e li trovate nel <a href=\"/prezzi/\">listino</a>.",
    "Cosa cambia fra le due formule è solo il modo di pagare: nell'abbonamento pensiamo noi a tutto per tutta la durata; con il pagamento unico il sito è vostro dal giorno della consegna e la manutenzione è facoltativa. Per siti con molte pagine, più lingue o funzioni particolari, vedete <a href=\"/quanto-costa-un-sito-web/\">quanto costa un sito web</a>."]},
  {"id":"passi","tipo":"passi","eyebrow":"Come lavoriamo","h2":f"Dal primo contatto {G}al sito online{_G}",
   "corpo":[("Chiamata","Cosa fate, per chi, dove: i contenuti nascono da qui."),
    ("Struttura e testi","Le pagine, le parole che i clienti cercano su Google, i testi."),
    ("Grafica e sviluppo","Il sito sul vostro marchio, veloce e leggibile da telefono."),
    ("Online e Google","Pubblicazione, indicizzazione, scheda Google Business collegata.")]}],
 "faqtitle":f"Le domande {G}sul sito vetrina.{_G}",
 "faq":[("Cos'è un sito vetrina?","Un sito che presenta azienda, servizi e contatti, senza vendita online. Serve a farsi trovare e a ricevere richieste."),
  ("Quanto costa un sito vetrina?","24,80 € al mese in abbonamento per almeno 24 mesi, oppure 350 € una tantum più 150 € di SEO iniziale, IVA inclusa."),
  ("Quante pagine deve avere?","Almeno una pagina per ogni servizio importante, più home, chi siamo e contatti. Meglio poche pagine curate che molte vuote."),
  ("Il sito è mio?","Con il pagamento unico il sito è vostro dal giorno della consegna, con dominio e hosting intestati a voi.")],
 "ctabox":{"h2":"Vi serve un sito che porti contatti?","p":"Diteci cosa fate e dove: vi rispondiamo con le pagine che servono e il prezzo, già scritto nel listino.","btn":"Chiedi un preventivo"},
 "altrititle":"Pagine collegate",
 "altri":[("Quanto costa un sito web","/quanto-costa-un-sito-web/"),("Sito web aziendale","/sito-web-aziendale/"),("Realizzazione siti internet","/realizzazione-siti-internet/"),("SEO locale","/seo-locale/"),("Prezzi","/prezzi/")],
 "svc":svc("Sito vetrina","Realizzazione siti web","Realizzazione di siti vetrina per aziende e professionisti, ottimizzati per Google e per smartphone, in abbonamento o con pagamento unico.",["Sito vetrina in abbonamento","Sito vetrina a costo chiuso","Ottimizzazione SEO iniziale"])
})

# ============================================================ DASHBOARD AZIENDALE
PAGINE.append({
 "lang":"it", "url":"/dashboard-aziendale/",
 "title":"Dashboard aziendale su misura: i numeri in tempo reale",
 "desc":"Dashboard aziendale su misura: vendite, margini, magazzino, produzione e incassi in tempo reale, presi dai programmi che usate già. Da PC, tablet e telefono.",
 "ogtitle":"Dashboard aziendale su misura — Danova Tech",
 "ogdesc":"I numeri che guardate ogni giorno, in una schermata, senza esportare in Excel.",
 "crumbs":[GEST, ("Dashboard aziendale", None)],
 "eyebrow":"Cruscotto aziendale",
 "h1":f"Dashboard aziendale: {G}i numeri che contano, ogni mattina.{_G}",
 "lead":"In molte aziende i numeri esistono già, ma sono sparsi fra gestionale, fatturazione, e-commerce e fogli Excel. Per avere il quadro qualcuno deve esportare, copiare e incollare, e quando il report è pronto è già vecchio. Una dashboard su misura li raccoglie da soli e ve li mostra aggiornati.",
 "cta1":"Parliamo dei vostri numeri", "cta2":"Cosa mostra",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"Cosa mostra","h2":f"Solo gli indicatori {G}che usate per decidere{_G}",
   "corpo":[("Vendite e margini","Per cliente, prodotto, agente, periodo, confrontati con l'anno prima."),
    ("Incassi e scadenze","Cosa deve entrare, cosa è scaduto, cosa dobbiamo pagare."),
    ("Magazzino","Giacenze, prodotti fermi, sottoscorta, valore."),
    ("Produzione e commesse","Avanzamento, ritardi, ore previste e consumate."),
    ("Marketing e sito","Contatti, campagne, costo per contatto, vendite online."),
    ("Avvisi","Una notifica quando un numero esce dai limiti che decidete voi.")]},
  {"id":"come","tipo":"testo","eyebrow":"Come funziona","h2":f"Dai vostri programmi, {G}senza ricopiare niente{_G}",
   "corpo":["Colleghiamo la dashboard ai programmi che usate già: gestionale, fatturazione, e-commerce, CRM, fogli Excel condivisi. I dati si aggiornano da soli; voi aprite la dashboard da PC, tablet o telefono e vedete la situazione di oggi.",
    "Ogni azienda guarda numeri diversi: per questo la dashboard è costruita su di voi, con i vostri indicatori e i vostri nomi. Una prima versione arriva in pochi giorni o poche settimane; poi si aggiungono indicatori quando servono. Canone mensile o pagamento unico, a vostra scelta."]}],
 "faqtitle":f"Le domande {G}sulla dashboard aziendale.{_G}",
 "faq":[("Cos'è una dashboard aziendale?","Una schermata che mostra in tempo reale i numeri principali dell'azienda, presi automaticamente dai programmi che usate."),
  ("Da quali programmi prende i dati?","Da gestionale, fatturazione, e-commerce, CRM ed Excel: verifichiamo i vostri programmi prima di iniziare."),
  ("Si vede dal telefono?","Sì, da PC, tablet e telefono, con utenti che vedono solo i numeri di loro competenza."),
  ("Quanto tempo serve?","Una prima versione in pochi giorni o poche settimane, a seconda di quanti programmi collegare.")],
 "ctabox":CTA_GEST, "altrititle":"Pagine collegate",
 "altri":[("Software controllo di gestione","/software-controllo-di-gestione/"),("Gestionale personalizzato","/gestionale-personalizzato/"),("Integrazione software aziendali","/integrazione-software-aziendali/"),("ERP per piccole aziende","/erp-per-piccole-aziende/")],
 "svc":svc("Dashboard aziendale su misura","Sviluppo dashboard e business intelligence","Dashboard aziendali su misura collegate ai programmi esistenti: vendite, margini, incassi, magazzino, produzione e marketing in tempo reale.",["Collegamento ai programmi esistenti","Indicatori su misura","Avvisi automatici","Accesso da PC, tablet e telefono"])
})

# ============================================================ ERP PER PICCOLE AZIENDE
PAGINE.append({
 "lang":"it", "url":"/erp-per-piccole-aziende/",
 "title":"ERP per piccole aziende: su misura, senza complicazioni",
 "desc":"ERP per piccole aziende su misura: ordini, acquisti, magazzino, produzione e amministrazione collegati, partendo da un modulo. Canone o pagamento unico.",
 "ogtitle":"ERP per piccole aziende — Danova Tech",
 "ogdesc":"Un ERP della taglia giusta: solo i moduli che servono, costruiti sui vostri processi.",
 "crumbs":[GEST, ("ERP per piccole aziende", None)],
 "eyebrow":"ERP su misura",
 "h1":f"ERP per piccole aziende: {G}della vostra taglia, non di quella di una multinazionale.{_G}",
 "lead":"Gli ERP più noti sono nati per le grandi aziende: potenti, ma pesanti da configurare e costosi da mantenere. Una piccola azienda ha bisogno della stessa cosa in piccolo: ordini, acquisti, magazzino, produzione e amministrazione che si parlano, senza mesi di consulenza.",
 "cta1":"Parliamo della vostra azienda", "cta2":"Cosa comprende",
 "sezioni":[
  {"id":"cosa","tipo":"cards","eyebrow":"I moduli","h2":f"Un modulo alla volta, {G}tutti collegati{_G}",
   "corpo":[("Vendite e ordini","Preventivi, ordini, conferme, consegne, fatture."),
    ("Acquisti","Richieste, ordini ai fornitori, arrivi, controllo prezzi."),
    ("Magazzino","Giacenze, lotti, movimenti, inventario, codici a barre."),
    ("Produzione","Distinte base, fasi, ordini di lavoro, avanzamento."),
    ("Amministrazione","Scadenze, incassi, collegamento alla contabilità del commercialista."),
    ("Report","Margini, costi, tempi: i numeri per decidere.")]},
  {"id":"perche","tipo":"testo","eyebrow":"Perché su misura","h2":f"Un ERP che {G}vi somiglia{_G}",
   "corpo":["Un ERP su misura per una piccola azienda parte dal modulo che serve di più, di solito ordini e magazzino, e collega gli altri quando servono. Importiamo i dati da Excel e dai programmi esistenti, e colleghiamo l'ERP a quello che volete tenere, come la fatturazione elettronica o la contabilità.",
    "Prima versione in pochi giorni o poche settimane, uso da PC, tablet e telefono, e la scelta fra canone mensile e pagamento unico. Se volete capire la differenza fra ERP, gestionale e CRM, c'è una <a href=\"/guide/differenza-gestionale-erp-crm/\">guida apposta</a>."]}],
 "faqtitle":f"Le domande {G}sull'ERP per piccole aziende.{_G}",
 "faq":[("Che differenza c'è fra ERP e gestionale?","Nelle piccole aziende i termini si sovrappongono: l'ERP è un gestionale che collega tutte le aree dell'azienda (vendite, acquisti, magazzino, produzione, amministrazione) in un unico sistema."),
  ("Una piccola azienda ha bisogno di un ERP?","Ha bisogno che le informazioni non si copino tre volte. Si può partire da un solo modulo e collegare gli altri quando servono."),
  ("Quanto tempo serve?","Una prima versione funzionante in pochi giorni o poche settimane; poi l'ERP cresce a fasi."),
  ("Quanto costa?","Potete scegliere fra canone mensile e pagamento unico; un gestionale su misura parte da 1.500 € IVA inclusa per il primo modulo, come indicato nel listino.")],
 "ctabox":CTA_GEST, "altrititle":"Pagine collegate",
 "altri":[("Gestionale personalizzato","/gestionale-personalizzato/"),("Differenza fra gestionale, ERP e CRM","/guide/differenza-gestionale-erp-crm/"),("Software MES per la produzione","/software-mes-produzione/"),("Gestionale magazzino","/software-gestionale-magazzino/"),("Dashboard aziendale","/dashboard-aziendale/")],
 "svc":svc("ERP per piccole aziende","Sviluppo ERP su misura","ERP su misura per piccole e medie imprese: vendite, acquisti, magazzino, produzione, amministrazione e report collegati, un modulo alla volta.",["Vendite e ordini","Acquisti","Magazzino","Produzione","Collegamento alla contabilità"])
})

# ============================================================ APP PERSONALIZZATA
PAGINE.append({
 "lang":"it", "url":"/app-personalizzata/",
 "title":"App personalizzata per la tua azienda: come crearla",
 "desc":"Creare un'app personalizzata per la propria azienda, per clienti o uso interno: da telefono, tablet e PC, collegata ai vostri programmi.",
 "ogtitle":"App personalizzata per aziende — Danova Tech",
 "ogdesc":"Un'app costruita sul vostro lavoro e solo per voi, non una piattaforma uguale per tutti.",
 "crumbs":[APP, ("App personalizzata", None)],
 "eyebrow":"App su misura",
 "h1":f"App personalizzata per la tua azienda: {G}costruita sul vostro lavoro.{_G}",
 "lead":"Un'app personalizzata serve quando un'attività che oggi fate su carta, al telefono o con tre programmi diversi può diventare un'unica schermata sul telefono: un ordine dell'agente, un rapportino del tecnico, una prenotazione del cliente, un controllo in magazzino.",
 "cta1":"Raccontaci la tua idea", "cta2":"Che app si possono fare",
 "sezioni":[
  {"id":"tipi","tipo":"cards","eyebrow":"Esempi","h2":f"App che {G}le aziende usano davvero{_G}",
   "corpo":[("Per agenti e venditori","Catalogo, listini, ordini e clienti, anche senza connessione."),
    ("Per tecnici e cantieri","Rapportini, foto, firme, ore e materiali, che arrivano subito in ufficio."),
    ("Per il magazzino","Lettura dei codici a barre, carichi, scarichi, inventario."),
    ("Per i clienti","Prenotazioni, ordini, fidelizzazione, area riservata."),
    ("Per il personale","Presenze, turni, ferie, comunicazioni interne."),
    ("Per i fornitori","Ordini, conferme, documenti di consegna.")]},
  {"id":"come","tipo":"testo","eyebrow":"Come la creiamo","h2":f"Dall'idea {G}all'app in uso{_G}",
   "corpo":["Partiamo da un'ora di lavoro vero: seguiamo chi userà l'app e capiamo dove perde tempo. La prima versione funzionante arriva in pochi giorni o poche settimane; la provano le persone che la useranno, e la miglioriamo a fasi.",
    "L'app si usa da telefono, tablet e PC, e si collega ai programmi che avete già, dal gestionale alla fatturazione, importando i dati che oggi stanno in Excel. Potete scegliere fra canone mensile e pagamento unico: le cifre sono nel <a href=\"/prezzi/\">listino prezzi</a> e in <a href=\"/quanto-costa-una-app/\">quanto costa un'app</a>."]}],
 "faqtitle":f"Le domande {G}sulle app personalizzate.{_G}",
 "faq":[("Quanto costa creare un'app personalizzata?","Dipende da cosa deve fare. Potete scegliere fra canone mensile e pagamento unico; le cifre di partenza sono nel listino prezzi e vi diamo un preventivo scritto."),
  ("Quanto tempo serve?","Una prima versione funzionante in pochi giorni o poche settimane, poi si migliora a fasi."),
  ("Funziona su iPhone e Android?","Sì, e anche da PC tramite browser."),
  ("Si collega al nostro gestionale?","Sì, colleghiamo l'app ai programmi che usate già e importiamo i dati esistenti.")],
 "ctabox":{"h2":"Hai in mente un'app per la tua azienda?","p":"Raccontaci cosa deve fare e chi la userà: ti diciamo come la costruiremmo e quanto costa, per iscritto.","btn":"Parliamone"},
 "altrititle":"Pagine collegate",
 "altri":[("Sviluppo app su misura","/servizi/app-su-misura/"),("Quanto costa un'app","/quanto-costa-una-app/"),("App per agenti di commercio","/app-per-agenti-di-commercio/"),("App rapportini di lavoro","/app-rapportini-di-lavoro/"),("App magazzino con codici a barre","/app-magazzino-codici-a-barre/"),("Web app","/sviluppo-web-app/")],
 "svc":svc("App personalizzata per aziende","Sviluppo app su misura","Sviluppo di app personalizzate per aziende, per clienti o uso interno, su telefono, tablet e PC, collegate ai programmi esistenti.",["App per agenti","App per tecnici","App per magazzino","App per clienti","Integrazione con gestionale"])
})

# ============================================================ GUIDA RPA
PAGINE.append({
 "lang":"it", "url":"/guide/cos-e-la-rpa/",
 "title":"Cos'è la RPA: automazione dei processi con i software robot",
 "desc":"Cos'è la RPA (Robotic Process Automation), come funziona, esempi in azienda, differenze con le integrazioni e quando conviene un'automazione su misura.",
 "ogtitle":"Cos'è la RPA — Danova Tech",
 "ogdesc":"I software robot che ripetono i clic al posto vostro: quando servono e quando c'è una strada migliore.",
 "crumbs":[("Guide","/guide/"), ("Cos'è la RPA", None)],
 "eyebrow":"Guida",
 "h1":f"Cos'è la RPA: {G}i software robot che lavorano al posto dei clic.{_G}",
 "lead":"RPA sta per Robotic Process Automation: un software che ripete al posto di una persona i passaggi fatti a mano sullo schermo, come copiare dati da una mail a un gestionale o scaricare documenti da un portale. È utile, ma non è sempre la soluzione migliore.",
 "cta1":"Parliamo delle vostre attività ripetitive", "cta2":"Come funziona",
 "sezioni":[
  {"id":"come","tipo":"testo","eyebrow":"Come funziona","h2":f"Un robot {G}che usa i programmi come una persona{_G}",
   "corpo":["Un robot RPA apre i programmi, legge lo schermo, clicca, copia e incolla seguendo istruzioni precise. Non serve modificare i programmi esistenti: il robot li usa dall'esterno, come farebbe un impiegato.",
    "Questo è il suo pregio e il suo limite. Il robot funziona finché le schermate restano uguali: se un portale cambia aspetto, il robot si ferma. Per questo, quando i programmi permettono di scambiare dati direttamente, un'integrazione diretta è più solida."]},
  {"id":"esempi","tipo":"cards","eyebrow":"Esempi","h2":f"Attività che {G}si possono automatizzare{_G}",
   "corpo":[("Ordini da email","Leggere gli ordini arrivati per email e inserirli nel gestionale."),
    ("Documenti dai portali","Scaricare fatture, DDT o estratti conto dai portali dei fornitori e delle banche."),
    ("Riconciliazioni","Confrontare incassi e fatture e segnalare le differenze."),
    ("Aggiornamento listini","Caricare prezzi e disponibilità da file dei fornitori."),
    ("Report periodici","Raccogliere numeri da più programmi e preparare il report del lunedì."),
    ("Inserimenti ripetitivi","Qualsiasi copia-incolla fra due programmi che fate ogni giorno.")]},
  {"id":"quando","tipo":"testo","eyebrow":"Quando conviene","h2":f"RPA, integrazione {G}o software su misura?{_G}",
   "corpo":["La RPA conviene quando i programmi non hanno collegamenti e non si possono cambiare. Se invece i programmi permettono uno scambio diretto di dati, conviene un'<a href=\"/integrazione-software-aziendali/\">integrazione</a>; se il problema è che il lavoro è sparso fra troppi strumenti, conviene un <a href=\"/gestionale-personalizzato/\">gestionale su misura</a> che li sostituisca.",
    "Noi partiamo dal problema, non dalla tecnologia: guardiamo le attività ripetitive, stimiamo le ore che fanno perdere e proponiamo la strada più semplice. Vedete anche le <a href=\"/automazione-processi-aziendali/\">automazioni dei processi aziendali</a> e le <a href=\"/automazioni-n8n/\">automazioni con n8n</a>."]}],
 "faqtitle":f"Le domande {G}sulla RPA.{_G}",
 "faq":[("Cosa significa RPA?","Robotic Process Automation: software che automatizzano attività ripetitive ripetendo i passaggi che una persona fa sullo schermo."),
  ("La RPA è intelligenza artificiale?","No, di base esegue regole precise. Si può affiancare all'intelligenza artificiale per leggere documenti o email non strutturati."),
  ("Che differenza c'è fra RPA e integrazione?","La RPA usa i programmi dall'esterno come una persona; l'integrazione li collega direttamente. L'integrazione è più solida quando è possibile."),
  ("Una piccola azienda può usarla?","Sì, per singole attività ripetitive. Spesso però un'automazione più semplice o un piccolo software su misura risolvono meglio lo stesso problema.")],
 "ctabox":CTA_GEST, "altrititle":"Pagine collegate",
 "altri":[("Automazione processi aziendali","/automazione-processi-aziendali/"),("Automazioni con n8n","/automazioni-n8n/"),("Integrazione software aziendali","/integrazione-software-aziendali/"),("Intelligenza artificiale per aziende","/intelligenza-artificiale-per-aziende/"),("Gestionale personalizzato","/gestionale-personalizzato/")],
 "svc":svc("Automazione RPA e integrazioni","Automazione dei processi aziendali","Analisi delle attività ripetitive e automazione con RPA, integrazioni dirette o software su misura.",["Analisi delle attività ripetitive","RPA","Integrazioni","Software su misura"])
})
