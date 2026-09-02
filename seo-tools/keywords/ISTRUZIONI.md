# Liste keyword per Google Ads — Keyword Planner

**2.069 keyword uniche**, divise per lingua e mercato. Servono per capire quali
parole hanno volume vero prima di scrivere le pagine estere.

| File | Keyword | Mercati coperti |
|---|---|---|
| `planner-IT.txt` | 391 | Italia (Veneto, Friuli, Nord Est) |
| `planner-DE.txt` | 707 | Austria, Germania, Svizzera, Alto Adige |
| `planner-FR.txt` | 420 | Francia, Belgio, Svizzera romanda |
| `planner-ES.txt` | 433 | Spagna, America Latina |
| `planner-EN.txt` | 118 | UK, Irlanda, Europa, nearshoring |
| `keywords-completo.csv` | 2.069 | tutte, con mercato / lingua / categoria / intento |

Il CSV si apre in Excel con doppio clic (separatore `;`, già impostato).

---

## Come estrarre i volumi — 5 minuti per lingua

1. Vai su **ads.google.com** → menu **Strumenti** → **Strumento di pianificazione
   delle parole chiave**.
2. Scegli **"Visualizza il volume di ricerca e le previsioni"**
   *(non "Individua nuove parole chiave": quello serve per scoprire, noi
   abbiamo già la lista).*
3. Apri il file `.txt` della lingua, **seleziona tutto e incolla** nel riquadro.
   Il limite è 1.000 keyword per volta: tutti i file ci stanno tranne il tedesco,
   che va incollato in due volte (prima metà e seconda metà).
4. **Prima di guardare i numeri, imposta il targeting** — è il passaggio che
   quasi tutti saltano e che rende i dati inutili:
   - in alto a sinistra, **Località** → togli "Italia" e metti il paese giusto
     (Austria per il tedesco, Francia per il francese, Spagna per lo spagnolo…)
   - accanto, **Lingua** → la lingua corrispondente
5. In alto a destra: **Scarica idee per le parole chiave** → **CSV**.
6. Mandami i CSV.

> ⚠️ **Un file per paese, non per lingua.** Il tedesco va estratto due volte,
> una con località Austria e una con località Germania: i volumi sono molto
> diversi e la concorrenza pure. Stessa cosa per il francese se ti interessa
> anche il Belgio. Se hai poco tempo, parti dai paesi che ti interessano di più.

---

## Cosa guardo io quando me li mandi

- **Volume medio mensile** — sotto le 50 ricerche/mese una pagina dedicata
  raramente si ripaga, meglio accorpare.
- **Concorrenza (organica, non quella per gli annunci)** — la colonna
  "concorrenza" del Planner riguarda le aste pubblicitarie, non il
  posizionamento naturale. La uso come indizio del valore commerciale della
  keyword: alta concorrenza = qualcuno ci sta guadagnando.
- **Offerta consigliata in cima alla pagina** — è il segnale migliore di tutti.
  Una keyword dove le agenzie pagano 8 € a clic vale più di dieci keyword da
  0,20 €, anche se ha meno volume.
- **Stagionalità** — per il B2B industriale c'è un crollo ad agosto e a
  dicembre. Serve a non spaventarsi dei cali.

Con quei dati decido su quali parole costruire le pagine paese e come scrivere
titoli e H1, invece di andare a intuito.

---

## Come è fatta la lista

Ogni riga del CSV ha quattro colonne oltre alla keyword:

- **Mercato** — Italia, Austria, Germania, Svizzera, Francia, Belgio, Spagna,
  America Latina, Internazionale.
- **Lingua** — it, de, en, fr, es.
- **Categoria** — Siti web, E-commerce, Gestionali ERP CRM, App, SEO e Ads,
  Automazioni e AI, Nearshoring, Informazionali.
- **Intento** — *commerciale* (cerca un fornitore, adesso) oppure *informativa*
  (si sta informando, es. "quanto costa un sito web"). Le commerciali portano
  richieste, le informative portano traffico e citazioni nelle risposte AI.
  Servono entrambe, ma per motivi diversi.

La categoria **Nearshoring** merita un occhio: sono le ricerche di aziende
tedesche, francesi e inglesi che cercano *apposta* uno sviluppatore in Europa
del Sud perché costa meno di uno locale. È il modo più realistico di vendere
all'estero senza avere una sede lì.
