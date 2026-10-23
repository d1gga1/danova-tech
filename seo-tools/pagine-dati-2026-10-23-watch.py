# -*- coding: utf-8 -*-
# 23/10/2026 - Una pagina per ogni video (/video/<nome>/): video in apertura, scheda "in breve", testo dalla caption,
# descrizione visiva (alt text) dove disponibile, video correlati e servizio collegato. Solo IT (i video sono in italiano).
# Eseguito dentro pagine-dati-2026-10-23.py dopo VIDEO e TUTTI.
import html as _h
TESTI = {
 "spot-stand-chiavi-in-mano": {
  "p": [
   "Hai una fiera in calendario? Lo stand lo facciamo noi, dall'inizio alla fine. 🏗️",
   "1️⃣ Progetto: partiamo dal tuo marchio, dai prodotti e dallo spazio. Se vuoi, vedi lo stand in 3D prima che venga costruito.<br>2️⃣ Produzione: è tutta nostra. Pareti, grafiche, arredi e luci, con materiali in Classe 1.<br>3️⃣ Trasporto: carichiamo tutto e lo portiamo noi in fiera, ovunque sia.<br>4️⃣ Montaggio: la nostra squadra lo monta a regola d'arte, con impianto elettrico e dichiarazione di conformità.<br>5️⃣ Smontaggio: quando la fiera chiude, tu pensi ai contatti. Al resto pensiamo noi.",
   "10 m² o 1000 m²: un solo referente, dal primo schizzo all'ultima vite. Oltre 300 stand montati in Italia e in 11 paesi europei."
  ],
  "alt": "Video dinamico con riprese di fiere e laboratori e grafiche animate, diviso in cinque fasi numerate con una barra di avanzamento. Uno, il progetto: una mano disegna e appare un'anteprima 3D dello stand con il logo del cliente. Due, la produzione: macchina a controllo numerico, verniciatura, le etichette pareti, grafiche, arredi, luci e il badge \"Classe 1\". Tre, il trasporto: muletti in magazzino e un camion all'alba con un percorso fino alla fiera. Quattro, il montaggio: operai che montano i pannelli con le spunte \"impianto elettrico\" e \"dichiarazione di conformità\". Cinque, lo smontaggio e lo stand pieno di visitatori con notifiche di nuovi contatti. Poi un quadrato da 10 che diventa 1000 metri quadri, un solo referente al centro delle cinque fasi, il numero 300+ stand montati e Italia più 11 paesi europei. Chiude la scheda Danova Tech \"La tua prossima fiera\" con la checklist e il commento STAND."
 },
 "reel-siti-web-11500-dollari": {
  "p": [
   "Da ZERO a $11.500 in 60 giorni. Con dei siti web. 🤯",
   "Nandi Muzsik, di Framer University, si è creato un'identità finta ed è ripartito da zero:<br>❌ 0 follower<br>❌ 0 portfolio<br>❌ 0 reputazione",
   "In 60 giorni ha fatto $11.500 tra template venduti online, progetti per clienti e affiliazioni (fonte: il suo video \"I tried making money with Framer for 60 days\").",
   "Il messaggio è uno solo: un sito fatto bene non è una spesa. È una macchina che lavora per te, anche mentre dormi."
  ],
  "alt": ""
 },
 "reel-stand-pandoora": {
  "p": [
   "Caso studio SEO: da pochi clic al giorno a oltre 50 in 3 mesi 📈",
   "Pan.door.a produce porte per interni a Fontanelle (Treviso) dal 1987. Insieme abbiamo fatto 3 cose:<br>✅ sito web rifatto da zero, veloce e ottimizzato per Google<br>✅ una pagina per ogni prodotto e per ogni zona (Veneto, Friuli Venezia Giulia, Treviso)<br>✅ guide con i prezzi veri, quelle che i clienti cercano prima di chiedere un preventivo",
   "Risultato in 3 mesi: 931 clic da Google e 29.900 impressioni. Dati reali da Google Search Console."
  ],
  "alt": ""
 },
 "reel-micro-animazioni-sito": {
  "p": [
   "Un sito “piatto”, fatto solo di testi e immagini ferme, oggi sembra vecchio anche quando è appena uscito. Le micro-animazioni sono piccoli movimenti che rispondono a quello che fa il visitatore: un pulsante che si accende, una scheda che si solleva, una spunta che conferma l’invio.",
   "Non servono a fare scena: guidano l’occhio verso il pulsante giusto, confermano che un clic è andato a buon fine e rendono il sito più piacevole da usare, soprattutto da telefono. Vanno dosate: troppe animazioni rallentano la pagina e distraggono, e la velocità resta un fattore che Google misura."
  ],
  "alt": ""
 },
 "reel-ufficio-ordini-0-dipendenti": {
  "p": [
   "Un intero ufficio ordini. Con 0 dipendenti. 📥 (Ep.1 di \"Reparto con 0 dipendenti\")",
   "Ecco come funziona 👇<br>1️⃣ Arriva un ordine: via mail, WhatsApp o dal sito<br>2️⃣ L'AI lo legge e capisce cliente, prodotti e quantità<br>3️⃣ Lo inserisce da sola nel gestionale<br>4️⃣ Controlla il magazzino e ti avvisa se manca qualcosa<br>5️⃣ Manda la conferma al cliente e prepara la fattura<br>6️⃣ Tu ricevi solo una notifica: ordine fatto ✅",
   "Niente copia-incolla, niente errori, niente ordini persi alle 11 di sera.",
   "⚑ Questo è un esempio dimostrativo: ogni sistema lo costruiamo su misura per la tua azienda."
  ],
  "alt": ""
 },
 "reel-agenti-ai-anthropic": {
  "p": [
   "6 a 1. 🤯 Dentro Anthropic gli agenti AI ora lavorano più ore dei dipendenti.",
   "Cosa dice il report uscito questa settimana (16/10/2026):<br>👉 gli agenti AI usati dai dipendenti hanno lavorato 6 volte le ore delle persone che li guidano (dato di agosto)<br>👉 ogni persona coordina il suo \"esercito di Claude\": agenti che scrivono, controllano ed eseguono<br>👉 tra le nuove assunzioni tecniche, la quota di profili junior è scesa dal 27% al 9%",
   "Per un'azienda il messaggio è chiaro: il lavoro ripetitivo passa agli agenti, le persone guidano. La domanda non è se succederà anche da te, ma chi ci arriva prima.",
   "Fonte: Anthropic, report sul lavoro interno, 16 ottobre 2026."
  ],
  "alt": ""
 },
 "spot-ai-roadster": {
  "p": [
   "Reel in stile “hype” sulla notizia della Tesla Roadster: immagini così spettacolari che in molti le hanno scambiate per intelligenza artificiale. Non lo erano: le foto sono vere, con i crediti nel video.",
   "Attorno alle foto abbiamo costruito il ritmo di uno spot: zoom e rotazioni sulle immagini, un’auto 3D generica, uno smartphone 3D con l’articolo, tipografia cinetica e voce fuori campo, su una base musicale composta per il video. È lo stile che usiamo quando un prodotto deve sembrare un evento."
  ],
  "alt": ""
 },
 "reel-sito-con-ai-in-1-minuto": {
  "p": [
   "Un sito fatto con l'AI in 1 minuto? Facile. Farlo lavorare per te è un'altra storia 👀",
   "Abbiamo chiesto all'AI un sito per una trattoria di Treviso. Risultato: carino, responsive, pronto in pochi secondi.",
   "1️⃣ Google non sa che esiste<br>2️⃣ Il modulo ti dice \"grazie\"… ma la richiesta non arriva a nessuno<br>3️⃣ Zero tracciamento: non sai chi lo visita né da dove arriva<br>4️⃣ Niente privacy policy (e il modulo raccoglie dati personali 😬)",
   "L'AI ti fa la vetrina. Non il lavoro che porta clienti."
  ],
  "alt": ""
 },
 "reel-mac-lento": {
  "p": [
   "Il suo Mac era lento e scottava da settimane. Non era vecchio. 🔥💻",
   "Uno sviluppatore ha chiesto a Claude Code di creargli una piccola app per controllare la temperatura del Mac. Mentre leggeva i sensori, l'AI ha trovato il vero colpevole: un programma nascosto (xmrig) che minava criptovalute usando tutti i 12 core del processore, fino a 112 gradi. Era tra i programmi di avvio da fine agosto.",
   "La parte più interessante? L'AI non ha toccato niente da sola: ha chiesto il permesso, poi ha fermato il programma e l'ha messo in quarantena. Il Mac è tornato come nuovo.",
   "Il PC dell'ufficio è lento? Forse non è vecchio. Prima di cambiarlo, vale la pena fare 5 controlli.",
   "Fonti: The Mac Observer, \"Claude Code Agent Catches Crypto Miner Melting Down A Mac\" (19/10/2026); Clubic (19/10/2026)."
  ],
  "alt": "Video in stile editoriale su sfondo scuro con una scheda al centro che si trasforma: un Mac disegnato con la rotellina che gira e la temperatura che sale; il terminale di Claude Code con la richiesta di creare un'app per la temperatura; la lista dei processi che scorre e si ferma su \"xmrig 1175%\", evidenziato in rosso come miner di criptovalute; 12 core al 100% e 112 gradi; 51 giorni accesi in rosso dal 29 agosto; la richiesta di permesso con il clic su \"Consenti\"; il programma che finisce in una teca di vetro chiusa col lucchetto verde; su fondo chiaro la temperatura che scende a 45 gradi; sei PC d'ufficio con una lente che scopre programmi nascosti; la guida gratuita Danova Tech \"5 controlli in 5 minuti\" con il commento CONTROLLO."
 },
 "reel-quanto-costa-un-sito": {
  "p": [
   "Quanto costa un sito web? La risposta onesta è: dipende da cosa è compreso. Dominio, hosting, manutenzione e modifiche sono spesso le voci che fanno lievitare il conto dopo la consegna.",
   "Nel reel lo diciamo in 15 secondi: da noi il prezzo è scritto prima di partire. Il sito Essenziale costa 350 € IVA inclusa una volta sola, oppure 24,80 € al mese con dominio, hosting, manutenzione e modifiche compresi nel canone."
  ],
  "alt": ""
 },
 "reel-notizia-rtx5090": {
  "p": [
   "2 bancali di RTX 5090 spariti in aeroporto 🚨 E nessuno sa dove sono.",
   "Il distributore brasiliano Oderço ha fatto arrivare due bancali di schede video Zotac RTX 5090 all’aeroporto di Guarulhos, a San Paolo. Poi il nulla.",
   "✅ Nessun bancale ritrovato<br>✅ Nessuna risposta, dice l’azienda<br>✅ “In 38 anni non ci era mai successo” (Oderço Matos)",
   "E tu sai dov’è la tua merce, adesso? Se la risposta è “più o meno”, ti serve un gestionale che te lo dice in tempo reale. Noi li costruiamo così.",
   "Fonti: Wccftech 18/10/2026, Tech Times 19/10/2026."
  ],
  "alt": ""
 },
 "reel-cartello-palestra": {
  "p": [
   "\"Vietato programmare con l'AI tra una serie e l'altra.\" 🏋️‍♂️💻",
   "La foto del cartello di una palestra di San Francisco ha fatto il giro del mondo questa settimana: decine di migliaia di like, ripresa dalle pagine tech più seguite. Quasi tutti l'hanno condivisa come vera.",
   "Peccato che fosse falsa. La palestra (Fitness SF) ha confrontato la foto con i suoi cartelli veri: le regole reali parlano di telefono e di cortesia, nessun divieto di \"vibe coding\". Qualcuno aveva modificato un loro cartello, logo compreso.",
   "Il punto per chi ha un'azienda? Oggi un falso con il tuo logo può girare ovunque in un giorno. La palestra è riuscita a smentire subito perché aveva i suoi originali sotto mano. Tu te ne accorgeresti?",
   "Fonte: Business Insider, \"A San Francisco gym went viral for a sign about vibe coding. The gym says it's an AI-generated fake\" (ottobre 2026). Riprese: Pexels."
  ],
  "alt": "Si apre in una palestra vera con due persone sulle cyclette e il testo \"Vietato programmare con l'AI in palestra?\". Un cartello \"Regole della sala\" si attacca davanti alla scena con la frase \"Niente codice e niente prompt a Claude tra una serie e l'altra\" evidenziata in rosso. Il cartello diventa la foto di un post, i like salgono e le ricondivisioni si aprono a ventaglio; compare la scritta \"FALSO\" e tutto si spegne. Il cartello vero e quello virale vengono confrontati con una linea di scansione che trova la frase aggiunta; il cartello si scompone in livelli, logo compreso. Su fondo chiaro \"il tuo logo\" si diffonde in 24 ore; una notifica avvisa di un post mai pubblicato; la guida gratuita Danova Tech \"Il tuo logo online: 4 controlli\" con il commento LOGO."
 },
 "reel-bmw-uscite": {
  "p": [
   "BMW offre a chi se ne va, in alcuni casi, più di 650.000 €. 🚗💶",
   "Secondo Handelsblatt, il portale interno per le uscite volontarie è stato preso d'assalto: circa 50.000 dipendenti di uffici e sviluppo hanno potuto fare richiesta (la produzione è esclusa) e il sistema è andato in tilt.<br>L'obiettivo è di circa 8.000 posti in meno entro il 2027, con un bonus in più per chi esce entro il 31 marzo 2027.",
   "Ma il conto vero arriva dopo: quando una persona se ne va, se ne va anche quello che sa. Clienti, fornitori, procedure, password, trucchi del mestiere.",
   "Nella tua azienda è scritto da qualche parte? 🤔",
   "Fonti: Handelsblatt, ripreso da Motor1 e Carscoops (ottobre 2026); 20 Minuten/Tio (21/10/2026). BMW ha confermato il programma ma non le cifre. Riprese: Pexels."
  ],
  "alt": "Video animato con riprese di auto sportive BMW recenti. Si apre con la calandra M blu con lo stemma, poi una M4 scura dentro un pannello 3D mentre un numero in 3D sale fino a 650.000 €. Un portale \"uscite volontarie\" si riempie di richieste finché va in errore 503. Un palazzo di uffici e una fabbrica in 3D: dagli uffici escono figure luminose, la fabbrica diventa grigia con la scritta \"esclusa\", sopra il numero circa 8.000 posti entro il 2027. Un calendario sfoglia i mesi fino a marzo 2027 con un'etichetta \"+ bonus\", sotto lo stemma su un cofano. Una M4 si allontana mentre le schede \"clienti\", \"fornitori\", \"procedure\", \"password\", \"trucchi del mestiere\" la seguono e spariscono. Una cartella \"Procedure\" si apre vuota: procedure scritte 0. Chiude la guida Danova Tech con il commento PROCESSI."
 },
 "reel-accenture-claude": {
  "p": [
   "Da 1.000 $ a 29 $ al mese 😳 Accenture ha messo un tetto a Claude.",
   "Accenture, uno dei colossi mondiali della consulenza con circa 799.000 dipendenti, ha deciso di pagare a molti di loro solo 29 $ al mese di Claude, l'AI di Anthropic. C'era chi ne spendeva fino a 1.000. Per andare oltre adesso serve il codice di un progetto che paghi la differenza, e l'accesso non è garantito.",
   "La parte più ironica? È la stessa azienda che spinge i clienti a investire nell'AI.",
   "Il punto non è usarla di più: è usarla dove rende davvero.",
   "📋 Abbiamo preparato una checklist gratuita di 9 domande per capire dove l'AI fa risparmiare la tua azienda (e dove stai solo pagando abbonamenti).",
   "Fonti: 404 Media (15/10/2026), The Next Web (16/10/2026)"
  ],
  "alt": "Animazione: il numero 1.000 dollari scende a 29 dollari, la sede di Accenture, il contatore dei 799.000 dipendenti, un tetto che schiaccia la spesa per Claude, gli articoli di 404 Media e The Next Web, un iPhone con il limite mensile raggiunto, e la checklist gratuita di Danova Tech."
 },
 "reel-simboli-prompt": {
  "p": [
   "Usi ChatGPT? Questi 5 simboli cambiano le risposte 🤯",
   "Non sono comandi segreti: servono a mettere ordine nel prompt.<br>✅ #  apre un titolo: dice all’AI di cosa parli<br>✅ ###  divide il compito in parti<br>✅   mette in evidenza ciò che conta<br>✅ [ ]  segna gli spazi da riempire<br>✅ |  crea una tabella",
   "Prompt più ordinato = risposta più precisa.<br>Noi l’AI la mettiamo al lavoro nelle aziende, con le regole giuste."
  ],
  "alt": ""
 },
 "reel-ai-di-notte": {
  "p": [
   "\"Claude, cosa hai fatto mentre dormivo?\" 🌙",
   "Ore 07:00, ecco il report della notte 👇<br>💬 Ha risposto a tutti i messaggi arrivati dopo cena e fissato gli appuntamenti in agenda<br>🔍 Ha analizzato i competitor (siti, social e recensioni) e trovato dove puoi batterli<br>🗓 Ha preparato i contenuti della settimana: post, caption e idee per i reel<br>🌐 Ha costruito la bozza del nuovo sito, pronta da vedere",
   "Tu dormivi. Lui lavorava.",
   "⚑ Questo è un esempio dimostrativo: ogni assistente AI lo costruiamo su misura per la tua azienda.",
   "E domani mattina, il report lo leggi tu ☀️"
  ],
  "alt": ""
 },
 "reel-ai-al-colloquio": {
  "p": [
   "Ha mandato la sua AI al colloquio. Dall’altra parte c’era un’altra AI 🤖🤝🤖",
   "Il comico americano Graham Dot Zip ha fatto l’esperimento (messo in scena per un suo video):<br>❌ la sua AI ha inventato che lui aveva guidato un team<br>❌ ha chiesto 60.000 $ l’anno quando lui ne voleva 140-150.000 (il selezionatore AI non è salito oltre 90.000)<br>❌ appena lui è uscito, le due AI si sono fissate un secondo colloquio da sole… e sono rimaste bloccate a salutarsi senza riuscire a chiudere la chiamata",
   "Fa ridere, ma la domanda è seria: oggi le AI parlano già al telefono e in chat al posto delle aziende.",
   "Fonte: The Register, 14/10/2026"
  ],
  "alt": ""
 },
 "reel-tv-senza-pubblicita": {
  "p": [
   "Ha tolto TUTTA la pubblicità dalla TV dei suoi genitori. Con l'AI 🤯",
   "Gathin, uno sviluppatore, era stanco delle pubblicità e delle app inutili sulla smart TV Xiaomi dei genitori. Così ha chiesto a Claude Code di sistemarla: l'AI ha trovato la TV sul Wi-Fi, ha tolto 25 app inutili e ha scritto una schermata nuova, pulita come quella di Apple TV.",
   "In due giorni qualche migliaio di persone ha fatto lo stesso, su TV Xiaomi, TCL, Sony, Fire TV e LG. ⚠️ Attenzione però: c'è anche chi la TV l'ha bloccata. Gli agenti AI possono sbagliare.",
   "Il punto per chi ha un'azienda? Se l'AI riesce a rimettere in ordine una TV, immagina cosa può fare con i programmi che vi fanno perdere ore ogni settimana.",
   "Fonte: TechCrunch, \"People are using AI to make their smart TVs dumb again\" (19/10/2026)"
  ],
  "alt": "Animazione 3D di un salotto: una TV piena di pubblicità, la scritta \"Pubblicità\" che si apre sulla scena, il terminale di Claude Code che trova la TV sul Wi-Fi, 25 app che volano via, la nuova schermata pulita, un muro di migliaia di TV che diventano blu, una TV bloccata, le finestre di programmi aziendali che si rimettono in ordine e la checklist gratuita di Danova Tech."
 },
 "reel-stand-chiavi-in-mano": {
  "p": [
   "Stand fieristico chiavi in mano, raccontato in 3D: lo stand con il marchio del cliente si costruisce davanti alla camera, poi seguono produzione, trasporto e montaggio in fiera.",
   "È il primo video che abbiamo dedicato al servizio stand, in stile neon 3D con sottotitoli; la versione successiva, con riprese vere di fiere e laboratori, è lo spot “stand fieristico chiavi in mano” da 43 secondi."
  ],
  "alt": ""
 },
 "reel-sfida-sito-dentista": {
  "p": [
   "Ho sfidato l'AI: un sito per uno studio dentistico in 30 minuti. ⏱",
   "Ci ha messo 1 minuto e 55 secondi (tempo reale, cronometrato):<br>✅ struttura e design<br>✅ sezione trattamenti<br>✅ foto dello studio generata con l'AI<br>✅ modulo per prenotare<br>✅ versione per smartphone",
   "Però una cosa va detta: questa è una BOZZA. Un sito che porta davvero pazienti ha bisogno di testi veri, SEO per farsi trovare su Google e di qualcuno che lo segue nel tempo.",
   "👉 Ed è lì che entriamo noi.",
   "Nome dello studio inventato per la demo."
  ],
  "alt": ""
 },
 "reel-scartato-in-6-minuti": {
  "p": [
   "Si è candidato nella sua azienda. Scartato in 6 minuti. 🤯",
   "Un manager racconta: per mesi l'ufficio del personale gli ha ripetuto che per il posto da Senior Associate non c'erano candidati validi. \"Colpa del mercato.\"",
   "Così ha fatto una prova: nuova email, nome finto e il suo stesso curriculum. Rifiuto automatico dopo 6 minuti.",
   "Ci ha messo una settimana a capire il perché: il filtro dei CV voleva \"React.js\", nel suo c'era scritto \"React\". Per tre caratteri, candidati validi scartati da aprile.",
   "E non è un caso isolato: secondo lo studio \"Hidden Workers\" di Harvard Business School e Accenture, l'88% delle aziende ammette che candidati qualificati vengono scartati perché non corrispondono esattamente ai criteri.",
   "Le automazioni vanno controllate, non solo accese. Vale per i CV, ma anche per moduli contatti, spam, CRM e chatbot.",
   "Fonti: Dev.ua e Distractify (21/10/2026), dal racconto del manager su Reddit; Harvard Business School e Accenture, \"Hidden Workers: Untapped Talent\" (2021)."
  ],
  "alt": "Video che alterna riprese vere e grafiche animate. Un manager davanti a una lavagna in ufficio, con i mesi da aprile a settembre che si accendono e due messaggi dell'ufficio del personale: \"Ancora nessun candidato valido\" e \"Colpa del mercato\". Su un portatile vero si compila un modulo di candidatura con email nuova, nome di prova e il suo CV, poi si preme invia. Un orologio corre fino a 6 minuti e arriva una mail di rifiuto con il timbro \"Scartato in automatico\"; un uomo reagisce sconvolto. Una settimana di giorni che si girano, il filtro che richiede \"React.js\" e il CV con scritto \"React\", evidenziato in rosso con il simbolo diverso. \".js\" in 3D rosso con la scritta \"3 caratteri\", CV che finiscono in un cesto \"Scartati\". Poi l'88% in 3D sopra una griglia di 100 edifici, 88 rossi. Tre interruttori di automazioni che si accendono e diventano \"controllata\". Chiude la guida Danova Tech \"6 controlli sulle tue automazioni\" con il commento FILTRO."
 },
 "reel-ai-nelle-vendite": {
  "p": [
   "Contatti commerciali giusti: dal 18% al 97%. 📈",
   "È il risultato di Cox Communications nel primo anno con l'AI nelle vendite: ritorno di 7 volte sull'investimento e costo per verificare i contatti sceso dell'86%.",
   "Ora Anthropic, l'azienda che sviluppa Claude, ha pubblicato una guida di 28 pagine per portare l'AI in tutto il reparto vendite. In sintesi:<br>1️⃣ Prepari: un responsabile, i sistemi collegati (CRM, email, chiamate), una metrica di attività e una di fatturato<br>2️⃣ Provi su 2 o 3 team motivati<br>3️⃣ Estendi a ondate: 25 persone, poi 150, poi tutti",
   "E il ritorno si misura confrontando chi usa l'AI e chi no nello stesso trimestre, non a sensazione.",
   "Fonte: Anthropic, \"Building an AI-native revenue organization\" (settembre 2026)."
  ],
  "alt": "Video in stile editoriale su sfondo scuro. Una scheda CRM con otto contatti passa da \"da verificare\" in rosso a \"verificato\" in verde mentre un contatore sale dal 18% al 97%. Poi la scheda del caso Cox Communications con tre tessere: 7× di ritorno, −86% di costo per verificare i contatti, 97% di accuratezza, e un grafico che sale. Arriva la guida di Anthropic, che si apre a ventaglio con le etichette 28 pagine, 3 fasi, per qualsiasi azienda. Una linea del tempo accende le tre fasi (prepari, provi, estendi) mentre una griglia di puntini si illumina a ondate. Lo sfondo diventa chiaro per tre barre: efficienza, espansione, nuove capacità, e la frase \"mi sembra che funzioni\" viene barrata. Chiude la scheda Danova Tech \"L'AI nelle vendite, in italiano\" con il commento VENDITE."
 },
 "reel-un-solo-team": {
  "p": [
   "Sito web, SEO, Meta Ads, app e gestionale: 5 fornitori diversi che si rimpallano le colpe? 🙃",
   "Con Danova Tech hai un unico partner per tutta la tua tecnologia. Siti web ed e-commerce su misura, SEO, campagne, app, gestionali e software, fino allo stand in fiera chiavi in mano.",
   "Un solo referente, dal progetto al lancio."
  ],
  "alt": ""
 },
 "reel-ferrari-pizzeria": {
  "p": [
   "E se Ferrari facesse il sito di una pizzeria? 🏎️🍕",
   "L'abbiamo costruito davvero, con l'AI:<br>🔴 rosso corsa e fibra di carbonio<br>⏱ \"da zero a pizza in 90 secondi\"<br>🏁 il menù è una griglia di partenza (P1 Margherita, P2 Diavola…)<br>🛞 la consegna? Pit stop<br>🎌 per prenotare: un giro di pista",
   "Il punto è uno: ogni brand ha un suo linguaggio, e un buon sito lo parla dal primo pixel.<br>Il tuo sito parla come il tuo brand? Se la risposta è no, ci pensiamo noi.",
   "Concept non ufficiale a scopo creativo, nessun legame con Ferrari. \"Corsa Pizzeria\" è un nome inventato."
  ],
  "alt": ""
 },
 "reel-ai-tv-box": {
  "p": [
   "Una notizia di ricerca raccontata in 23 secondi: secondo quanto pubblicato da Anthropic il 12 ottobre 2026, un modello di intelligenza artificiale è stato suddiviso e fatto funzionare su 15 TV box Android da circa 55 dollari, e in una rete simulata un altro modello è riuscito a copiarsi da un nodo all’altro.",
   "Il reel usa lo stile “schermo”: interfacce ricostruite, lo schema dei 15 dispositivi, uno screenshot della fonte e una ripresa d’ufficio in chiusura, con voce fuori campo. Fonti: Anthropic, BleepingComputer e Dark Reading (ottobre 2026)."
  ],
  "alt": ""
 },
 "reel-listino-prezzi": {
  "p": [
   "Il prezzo, prima della call. Invece di “dipende, sentiamoci”, nel reel mostriamo il listino pubblico con oggetti 3D animati: sito web Essenziale 350 € con SEO a 150 €, applicazioni web e gestionali da 1.500 €, tutto IVA inclusa.",
   "È il formato che consigliamo a chi vende servizi: un video breve che risponde alla prima domanda di ogni cliente, e filtra già le richieste giuste."
  ],
  "alt": ""
 },
 "reel-fornitori": {
  "p": [
   "Il sito non va. Di chi è la colpa? Dell’agenzia web, dell’hosting o di chi ha fatto il gestionale? Nel reel, in stile gag, i tre fornitori si rimpallano il problema mentre il cliente aspetta.",
   "La morale è semplice: con un unico referente per sito, hosting, gestionale e campagne, quando qualcosa si rompe c’è una sola persona da chiamare, e nessuno scaricabarile."
  ],
  "alt": ""
 },
 "reel-ai-clona-office": {
  "p": [
   "Uno sviluppatore ha appena clonato Word, Excel e PowerPoint con l’AI. E li regala. 🤯",
   "👉 Si chiama Brandon Thomas e ha usato Claude, l’AI di Anthropic<br>👉 WordCraft, GridCraft e DeckCraft: gratis, open source, su Windows, Mac e Linux<br>👉 Prima aveva già fatto lo stesso con le app di Adobe<br>👉 Non sono perfetti: sono ancora in sviluppo",
   "Ma il punto è un altro.<br>Costruire software su misura oggi costa molto meno di prima.",
   "Quel gestionale che “tanto è roba da grandi aziende”? Clienti, ordini, magazzino e fatture in un unico posto: da 1.500 €, IVA inclusa, prezzo fisso.",
   "Fonti: TechRadar (12/10/2026), Analytics Insight (14/10/2026)"
  ],
  "alt": ""
 },
 "reel-anthropic-junior": {
  "p": [
   "Reel editoriale senza voce sui dati che Anthropic ha pubblicato sulle proprie assunzioni tecniche (16 ottobre 2026): la quota di profili junior tra i nuovi assunti scende dal 27% al 9%, mentre crescono le ore di lavoro svolte dagli agenti AI per ogni ora di lavoro delle persone.",
   "Il formato è quello delle schede editoriali: una sola scheda al centro che si trasforma (contatore, screenshot della fonte, grafici ricostruiti dai dati, citazione evidenziata), con testo che entra riga per riga e un pannello di stato fisso. Pensato per essere letto anche senza audio."
  ],
  "alt": ""
 },
 "reel-occhiali-scacchi": {
  "p": [
   "Ha barato a scacchi con gli occhiali smart 🤓♟️",
   "In un video diventato virale (quasi 3 milioni di visualizzazioni), un ragazzo dice di aver giocato a scacchi una o due volte in vita sua. Eppure vince. Il trucco, racconta lui: gli occhiali smart riprendono la scacchiera, un portatile calcola la mossa migliore e gliela suggerisce all'orecchio. Il video è montato, quindi non si può verificare la partita intera.",
   "E non è solo un gioco: in Corea del Sud uno studente è stato scoperto con gli occhiali smart durante un esame di ammissione all'università ed è stato escluso per tre anni. All'esame nazionale di novembre controlleranno gli occhiali di tutti i candidati.",
   "Il punto per chi ha un'azienda? Non ha inventato niente: ha collegato strumenti che esistono già. In azienda si può fare lo stesso, ma per lavorare meglio: email, Excel, ordini e gestionale che finalmente si parlano.",
   "Fonti: video di @Sourgrape02 su TikTok, rilanciato da @evolving.ai (20/10/2026); The Korea Times, \"AI glasses raise cheating fears ahead of CSAT, putting teachers under pressure\" (16/10/2026)."
  ],
  "alt": "Animazione 3D su fondo blu elettrico: occhiali smart in primo piano, i pezzi degli scacchi che cadono a cascata sulla scacchiera, la donna bianca dà scacco e il re nero cade. Un tunnel di video con il contatore fino a 2.900.000 visualizzazioni. Gli occhiali ai raggi X con fotocamera, altoparlante, batteria e chip dorati, un portatile che calcola la mossa migliore e la manda all'orecchio. Un'aula d'esame vista dall'alto con uno scanner rosso, un banco che si accende di rosso e la scritta \"3 ANNI\" in 3D. Le icone degli strumenti collegati, poi Excel, email, ordini, gestionale, magazzino e agenda collegati al motore AI. \"Commenta OCCHIALI\" in oro, la checklist gratuita e il logo Danova Tech che si forma da un anello di particelle."
 },
 "reel-risposta-in-24-ore": {
  "p": [
   "Chi chiede un preventivo per un sito o un software spesso aspetta giorni prima di sapere tempi e costi. Nel reel, girato in stile realistico con un calendario e uno smartphone animati, mostriamo il nostro impegno: scrivi oggi, entro 24 ore lavorative hai una risposta con tempi, costi e passo successivo."
  ],
  "alt": ""
 },
 "reel-sito-lento": {
  "p": [
   "Il tuo sito è lento? Google se ne accorge. ⚡",
   "Google misura 3 cose sui visitatori veri del tuo sito:<br>• LCP: il contenuto principale deve comparire entro 2,5 secondi<br>• INP: il sito deve rispondere a un clic entro 200 millisecondi<br>• CLS: la pagina non deve “saltare” mentre carica (sotto 0,1)",
   "La causa numero uno di un sito lento? Immagini troppo pesanti nel formato sbagliato. Si risolve con WebP o AVIF e dimensioni reali."
  ],
  "alt": ""
 }
}
WS_OVR = {'spot-ai-roadster': 'tesla-roadster-sembra-ai', 'reel-stand-pandoora': 'caso-studio-seo-pandoora',
          'reel-stand-chiavi-in-mano': 'stand-chiavi-in-mano-3d'}
def watch_url(k):
    s = WS_OVR.get(k) or k.replace('reel-', '', 1).replace('spot-', 'spot-', 1)
    return '/video/%s/' % s
WATCH = {k: watch_url(k) for k in VIDEO}
CAT_SITO = ['reel-sito-con-ai-in-1-minuto', 'reel-sito-lento', 'reel-sfida-sito-dentista', 'reel-ferrari-pizzeria', 'reel-micro-animazioni-sito',
            'reel-stand-pandoora', 'reel-quanto-costa-un-sito', 'reel-siti-web-11500-dollari', 'reel-listino-prezzi', 'reel-risposta-in-24-ore',
            'reel-un-solo-team', 'reel-fornitori']
CAT_AI = ['reel-ufficio-ordini-0-dipendenti', 'reel-ai-di-notte', 'reel-ai-nelle-vendite', 'reel-tv-senza-pubblicita', 'reel-mac-lento',
          'reel-occhiali-scacchi', 'reel-notizia-rtx5090', 'reel-ai-clona-office', 'reel-ai-al-colloquio', 'reel-simboli-prompt',
          'reel-agenti-ai-anthropic', 'reel-anthropic-junior', 'reel-accenture-claude', 'reel-cartello-palestra', 'reel-scartato-in-6-minuti',
          'reel-bmw-uscite', 'reel-ai-tv-box']
CAT_STAND = ['spot-stand-chiavi-in-mano', 'reel-stand-chiavi-in-mano', 'spot-ai-roadster']
GEST_V = {'reel-ufficio-ordini-0-dipendenti', 'reel-notizia-rtx5090', 'reel-ai-clona-office', 'reel-fornitori'}
def _servizio(k):
    if k in CAT_STAND[:2]: return ('Stand fieristici chiavi in mano', '/stand-fieristici/')
    if k == 'reel-stand-pandoora' or k == 'reel-sito-lento': return ('SEO e posizionamento', '/servizi/seo/')
    if k in GEST_V: return ('Gestionale su misura per ogni settore', '/gestionale-su-misura-per-ogni-settore/')
    if k in CAT_SITO: return ('Sito web in 24 ore', '/sito-web-in-24-ore/')
    if k in CAT_AI: return ('Intelligenza artificiale per aziende', '/intelligenza-artificiale-per-aziende/')
    return ('Video pubblicitari', '/video-pubblicitari/')
def _correlati(k):
    cat = next((c for c in (CAT_SITO, CAT_AI, CAT_STAND) if k in c), TUTTI)
    i = cat.index(k); altri = [cat[(i + j) % len(cat)] for j in range(1, len(cat))][:4]
    if len(altri) < 4: altri += [x for x in TUTTI if x != k and x not in altri][:4 - len(altri)]
    return altri
def _par(p): return _h.escape(p, quote=False).replace('&lt;br&gt;', '<br>')
for k in TUTTI:
    v = VIDEO[k]; T = TESTI[k]; nome = v['nome']['it']; url = WATCH[k]
    pub = ' e '.join(x for x, y in (('Instagram', v.get('ig')), ('TikTok', v.get('tt'))) if y) or 'Non ancora pubblicato sui social'
    serv = _servizio(k)
    sez = [{"id": "video", "tipo": "video", "uno": True, "eyebrow": "Video", "h2": f"Guarda il video {G}({int(round(v['durata']))} secondi){_G}", "video": [k]},
           {"id": "in-breve", "tipo": "breve", "eyebrow": "In breve", "h2": f"Il video {G}in breve{_G}",
            "testo": _h.escape(v['desc']['it'], quote=False) + ' Realizzato da <b>Danova Tech</b>, agenzia di Mansuè (Treviso) che crea video pubblicitari, reel e spot per aziende in 24 ore.',
            "fatti": [("Tecnica", v['tipo']['it']), ("Durata", "%s secondi" % str(v['durata']).replace('.', ',')), ("Formato", "Verticale 9:16, con sottotitoli"),
                      ("Pubblicato su", pub), ("Data", '/'.join(reversed(v['data'].split('-')))), ("Realizzato da", "Danova Tech")]},
           {"id": "di-cosa-parla", "tipo": "testo", "eyebrow": "Il testo", "h2": f"Di cosa parla {G}il video{_G}", "corpo": [_par(p) for p in T['p']]}]
    if T['alt']:
        sez.append({"id": "cosa-si-vede", "tipo": "testo", "eyebrow": "Descrizione visiva", "h2": f"Cosa si vede {G}nel video{_G}", "corpo": [_par(T['alt'])]})
    sez.append({"id": "correlati", "tipo": "video", "eyebrow": "Altri video", "h2": f"Video {G}simili{_G}", "video": _correlati(k)})
    PAGINE.append({
     "lang": "it", "url": url, "ogimg": "/assets/video/%s.jpg" % k, "videopage": k,
     "title": (nome if len(nome) <= 52 else nome[:50].rsplit(' ', 1)[0] + '…') + ' (video)',
     "desc": v['desc']['it'][:158],
     "ogtitle": nome + ' — video Danova Tech', "ogdesc": v['desc']['it'][:200],
     "crumbs": [VIDH, (nome, None)], "eyebrow": v['tipo']['it'] + ' · ' + str(v['durata']).replace('.', ',') + ' s',
     "h1": nome, "lead": v['desc']['it'], "cta1": "Voglio un video così", "cta2": "Guarda il video",
     "sezioni": sez,
     "faqtitle": f"Domande {G}su questo video.{_G}",
     "faq": [("Chi ha realizzato questo video?", "Danova Tech, agenzia di Mansuè (Treviso) che realizza video pubblicitari, reel per Instagram e TikTok, spot con intelligenza artificiale e motion design 3D per aziende di tutta Italia."),
             ("Potete fare un video così per la mia azienda?", "Sì: diteci cosa vendete e dove volete pubblicarlo. Il video è pronto in 24 ore dall’approvazione dell’idea, in verticale per Reel e TikTok e negli altri formati che servono. Il prezzo è a preventivo, scritto e senza sorprese."),
             ("Quanto costa un video come questo?", "Dipende da durata, tecnica e numero di versioni: per questo facciamo un preventivo a corpo entro 24 ore lavorative dalla richiesta.")],
     "ctabox": CTA_VID, "altrititle": "Pagine collegate",
     "altri": [serv, ("Tutti i video pubblicitari", "/video-pubblicitari/"), ("Video per Meta Ads e TikTok", "/video-pubblicitari-per-social-e-ads/"),
               ("Spot con intelligenza artificiale", "/spot-pubblicitari-con-intelligenza-artificiale/"), ("Sito web in 24 ore", "/sito-web-in-24-ore/"), ("Contatti", "/contatti/")],
     "svc": svc("Video pubblicitari", "Produzione video pubblicitari",
                "Video pubblicitari, reel e spot per aziende: motion design 3D, video con intelligenza artificiale e reel per Instagram e TikTok, pronti in 24 ore.",
                ["Reel per Instagram e TikTok", "Spot pubblicitari", "Motion design 3D", "Video prodotto"])})
