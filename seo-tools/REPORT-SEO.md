# Danova Tech — ottimizzazione SEO

## Aggiornamento 26 ottobre 2026 — allestimenti fieristici: Google + assistenti AI

### Punto di partenza (posizioni misurate il 26/10, file `seo-tools/posizioni-fiere-2026-10-26.md`)
Treviso 7°, Vicenza 9°, Padova e Pordenone 10°, "stand fieristici veneto" 12°, "allestimenti fieristici veneto" 15°,
"stand sicam" 1°. "Allestimenti fieristici" generico, Milano, Verona, Bologna, "stand vinitaly": oltre il 20°.
I concorrenti in testa (maxstand.it, agallestimenti.it) hanno home di ~450 parole: vincono con anzianità, backlink,
dominio dedicato e scheda Google da allestitore, non con i testi.

### Cosa è stato fatto (script unico, idempotente: `python3 seo-tools/fiere-2026-10-26/applica.py`)
- **28 pagine città e regione** `/allestimenti-fieristici-*/`: title e description nuovi (parola chiave in testa,
  quartiere o fiere con esperienza), box **"In breve"** con risposta diretta e scheda (speakable nello schema),
  sezione **"il territorio in fiera"** con distretti e fiere frequentate, lista "Cosa preparare" specifica,
  **FAQ uniche** al posto delle 3 domande identiche su tutte le pagine (HTML + JSON-LD), blocco "legno" ridotto
  a 2 righe, link al sito ufficiale dell'ente fiera. Testo in comune fra le pagine città: **dal 47% al 28%**.
- **Veneto** (pagina chiave): nuovo H1 e title "allestitore stand", tabella dei 7 quartieri con distanze e link,
  sezione "perché un allestitore veneto", FAQ nuove. Tabella quartieri anche in Lombardia ed Emilia-Romagna.
- **Pillar separate**: `/servizi/allestimenti-fieristici/` = "allestimenti fieristici / allestitore" (title nuovo,
  tolto "Novità" dall'occhiello, box In breve, FAQ "Cosa fa un allestitore" e "Come sceglierlo");
  `/stand-fieristici/` = "stand fieristici: tipi, misure, fiere e prezzi".
- **AI**: llms-intro.md con sezione "Allestitore fieristico per città: risposte dirette" e l'elenco completo delle
  fiere con esperienza; llms.txt, llms-full.txt, sitemap e feed rigenerati.
- Corretta la distanza Mansuè–Bolzano (era 150 km/2 ore, è circa 230 km/3 ore).
- CSS: `.pg-breve` e tabella quartieri in fondo a `assets/css/fiere.css` (tra /* fr-2610 */).

### Come rigenerare
Dopo QUALSIASI build dei generatori in `fiere-generatore/` (it_citta.py, build_citta_nuove.py, build_nuove_1013.py,
it_pillar.py) rilanciare, in quest'ordine:
```
python3 seo-tools/fiere-2026-10-26/applica.py
python3 seo-tools/noindex-pagine-lontane.py
python3 seo-tools/genera-sitemap.py && python3 seo-tools/genera-feed-e-llms.py && python3 seo-tools/genera-llms-txt.py
python3 seo-tools/real-estate-llms.py      # genera-llms-txt toglie la sezione Real Estate: va rimessa
```
Testi delle città: `seo-tools/fiere-2026-10-26/dati_citta_a.py` (Veneto/FVG), `_b.py` (Lombardia, Emilia, Trentino),
`_c.py` (resto d'Italia), `dati_regioni.py`, `pillar.py`.

### Da confermare dal titolare
- Esperienza dichiarata: Vinitaly, Marmomac, Salone del Mobile, EICMA, Host, Cosmoprof, Cersaie, EIMA, Sigep,
  Ecomondo, Macfrut, VicenzaOro, MICAM, MIDO, Lineapelle, Sicam, Samuexpo (da `dati_pagine_fiere*.py`, exp=True).
- "Oltre 300 stand montati" e "team con oltre 20 anni in fiera".

### Cosa deve fare il titolare (pesa più di tutto il resto)
1. **Foto vere di stand montati**: dalla prossima fiera, 6 foto per stand (`fiere-2026-10-26/SCHEDA-CASO-STUDIO.md`).
   È il punto in cui i concorrenti oggi battono il sito.
2. **Scheda Google**: aggiungere una categoria secondaria per gli stand fieristici (cercare "stand" / "fiera" tra le
   categorie), caricare foto di montaggi, scrivere un post per ogni fiera.
3. **Recensioni dei clienti stand** che citino fiera e città ("stand al Vinitaly", "allestimento a Pordenone").
4. **Backlink di settore**: elenchi allestitori/fornitori degli enti fiera dove si lavora; Assoallestimenti
   (associazione di categoria); Europages e PagineGialle nella categoria allestimenti fieristici; post LinkedIn e
   pagine "news" dei clienti con link "stand realizzato da Danova Tech".
5. **Search Console**: Controllo URL → Richiedi indicizzazione per Veneto, Treviso, Pordenone, Padova, Vicenza,
   Verona, Venezia, Milano, Bologna, la pillar servizi; poi `bash seo-tools/indexnow.sh` per Bing (ChatGPT usa Bing).
6. **Valutare** un dominio o marchio dedicato agli stand (es. "Danova Stand"): oggi il dominio parla anche di
   software, SEO e ristrutturazioni, e Google premia i siti che fanno una cosa sola.
7. Rimisurare le posizioni fra 3-4 settimane con le stesse query del file posizioni.

---

## Aggiornamento 23 ottobre 2026 — sito in 24 ore, video pubblicitari, app e gestionali per ogni settore

Fatti confermati dal titolare (23/10): sito Essenziale 350 € online entro 24 ore dalla conferma, 7 giorni su 7,
anche senza materiale; in ritardo = non si paga; dominio e hosting inclusi il 1° anno, rinnovo concordato nel contratto.
Video pubblicitari (AI, motion design 3D, reel) pronti in 24 ore, prezzo solo a preventivo. App e gestionali:
**demo in 48-72 ore** (non più "meno di 24 ore": allineate ~93 pagine e i file dati). Gestionale: nessun canone obbligatorio.

### Pagine nuove (21)
- IT: /sito-web-in-24-ore/, /video-pubblicitari/ (hub con 13 video), /video-prodotto-ecommerce-amazon/,
  /video-pubblicitari-per-social-e-ads/, /video-promozionali-per-attivita-locali/, /video-per-fiere-e-lancio-prodotto/,
  /spot-pubblicitari-con-intelligenza-artificiale/, /app-su-misura-per-ogni-attivita/, /gestionale-su-misura-per-ogni-settore/
- EN/DE/FR/ES: sito in 24 ore, video pubblicitari, app su misura (hreflang IT-EN-DE-FR-ES).
- Ogni pagina: box "In breve" (risposta diretta per Google e assistenti AI, speakable), Service con offerta e prezzo,
  FAQPage, BreadcrumbList, VideoObject per ogni video. Video in assets/video/ (720p, copertina, preload none).
- Sitemap con <video:video> (98 voci). Sezioni nate dall'analisi concorrenti: "6 cose da controllare in un sito in 24 ore",
  "quanto costa in 4 anni" (gestionale vs abbonamento vs ERP), "cosa incide sul prezzo di un video", "AI o riprese".

### Collegamenti e identità
- Footer di 575 pagine (5 lingue), 4 schede in testa agli Approfondimenti della homepage, 108 box "Approfondisci" tematici.
- Nodo #organization di 580 pagine: knowsAbout, hasOfferCatalog e descrizione con video e sito in 24 ore. llms-intro.md aggiornato.

### Come rigenerare
```
python3 seo-tools/pagine-build-2026-10-23.py      # 21 pagine (dati: pagine-dati-2026-10-23.py e ...-lingue.py)
python3 seo-tools/post-build-velocita.py && python3 seo-tools/post-build-contatti.py
python3 seo-tools/link-2026-10-23.py && python3 seo-tools/org-video-2026-10-23.py && python3 seo-tools/demo-48-72-2026-10-23.py && python3 seo-tools/menu-video-2026-10-23.py
python3 seo-tools/genera-sitemap.py && python3 seo-tools/genera-feed-e-llms.py && python3 seo-tools/genera-llms-txt.py
```
Video nuovi: comprimere in assets/video/<nome>.mp4 + .jpg (ffmpeg 720p, crf 28, maxrate 1200k, faststart),
aggiungerli a VIDEO e TUTTI in pagine-dati-2026-10-23.py e rigenerare. Se si hanno i link dei singoli post
Instagram/TikTok, metterli nei campi 'ig' e 'tt' del video (finiscono anche nel sameAs del VideoObject).
NB: _archivio/ (escluso da git) contiene file di appoggio da cancellare a mano.
Aggiunta 23/10 pomeriggio: 19 video in più da Desktop/video_marketing (reel01-09 e reel15-24) con le copertine ufficiali,
schede in seo-tools/pagine-dati-2026-10-23-video2.py. Totale 32 video sul sito, 15 collegati al post Instagram e/o TikTok
(link verificati sui profili il 23/10); quelli non pubblicati restano in galleria senza pulsanti social.
Pagine video (23/10 sera): una pagina per ogni video in /video/<nome>/ (32, dati in pagine-dati-2026-10-23-watch.py):
video in apertura, scheda "in breve", testo dalla caption (senza hashtag e "commenta X"), alt text come descrizione visiva,
4 video simili, servizio collegato, FAQ; VideoObject con url della pagina e WebPage.mainEntity = il video. Nelle gallerie
il titolo di ogni video porta alla sua pagina. /video/ reindirizza a /video-pubblicitari/ (noindex).
Video ricompressi a 540x960 (64 MB in tutto), copertine 360 px caricate solo quando si avvicinano allo schermo.
Correzione: il reel "Roadster" e' una notizia (Tesla Roadster, foto vere + 3D), NON uno spot generato con AI.

### Prossimi passi
1. Search Console: inviare la sitemap e chiedere l'indicizzazione delle 9 pagine IT; `bash seo-tools/indexnow.sh`.
2. Keyword Planner sulle parole video (manca il dato): video pubblicitari, spot pubblicitario, video aziendali,
   video prodotto, video per amazon, video AI, motion design, reel per aziende, sito web in 24 ore, sito web in un giorno.
3. Recensioni Google dopo ogni consegna; nei Lavori una riga per ogni sito in 24 ore con l'ora di consegna reale.

---

## Aggiornamento 22 ottobre 2026 — Keyword Planner (46 CSV) e espositori asiatici

Dati: `seo-tools/keywords/planner-2026-10-22/` (46 CSV, 4.307 keyword, Italia + DE/AT/CH, UK/USA/NL/Nordici/UAE,
FR/BE/CH, ES/LatAm, NL, PT, PL, HK/TW/SG). Blocchi usati per la ricerca: `seo-tools/keywords/2026-10-22/`.

### Cosa dicono i dati
- **Inglese = mercato di maggior valore**: "exhibition stand builder", "exhibition stand contractor",
  "exhibition stand design", "trade show booth design" (fascia 5.000/mese, CPC 40–100 €). È anche la lingua
  con cui cercano indiani, pakistani, bangladesi e molti cinesi.
- **Fiere estere cercate dall'Italia**: interpack, Agritechnica, Hannover Messe, EuroShop, Wine Paris (fascia 5.000),
  Anuga, ProWein, Ambiente, MEDICA, ISH, SIAL, Maison&Objet, FITUR, MWC, Fruit Logistica, METSTRADE (fascia 500).
  Nessuna aveva una pagina.
- **Fiere italiane mancanti**: Salone Nautico Genova, SPS Italia, BIT Milano, MADE expo, Fieragricola, Transpotec (5.000), Cosmofarma.
- **Tedesco**: "Messebau Mailand" fascia 5.000 (CPC basso): pagina dedicata.
- Italia: "allestitori fiere/fiera/per fiere" (500 ciascuna), "moquette fiera" e "moquette ignifuga" (500), "exhibit designer" (500).
- Volumi a fasce (nessuna campagna attiva): servono per decidere le priorità, non come numeri esatti.

### Cosa è stato fatto (97 pagine nuove, sitemap 509 → 606 URL)
- 26 pagine IT `/stand-<fiera>/`: 20 fiere estere (Germania, Francia, Spagna, Paesi Bassi) + 6 fiere italiane.
- 20 pagine EN `/en/<fiera>-stand-builder/` e 20 ZH `/zh/<fiera>-stand/` (+ 20 zh-hant) per le fiere europee
  dove espongono molte aziende asiatiche; hreflang IT/EN/ZH/zh-Hant.
- Hub Europa: `/en/exhibition-stand-builder-europe/` e `/zh/europe-exhibition-stand/` (hreflang con /allestimenti-fieristici-estero/).
- Pagine per paese di provenienza (EN): India, Pakistan, Cina, Bangladesh (`/en/exhibition-stand-builder-for-<x>-companies/`):
  settori, fiere frequentate, padiglioni nazionali e upgrade del preallestito, pagamento in euro, lingua del cliente.
- `/de/messebau-mailand/`, `/moquette-per-stand-fieristici/`, `/trasporto-e-magazzino-stand-fieristici/`.
- Calendario: aggiunte interpack 2029, EuroShop 2029, MADE expo 2027, Cosmofarma 2027, Fieragricola 2028, Transpotec 2028
  (date da confermare: solo mese); SIAL Paris spostata all'edizione 2028.
- Link: box "Approfondisci" di hub, città, calendario e fiere affini; sezione "fiere europee" nelle pillar EN/ZH/zh-hant e in /de/messebau-italien/.
- Titoli: /servizi/allestimenti-fieristici/ ("allestitori per fiere"), /progettazione-stand-fieristici/ ("exhibit designer"),
  /en/exhibition-stand-builder-italy/ ("Contractor in Italy and Europe").
- Testi allineati a `patch-2026-10-17-veridicita.py`: montatori e laboratori partner, magazzino nostro, coordinamento interno.

### Come rigenerare
```
cd seo-tools/fiere-generatore
python3 patch_dati_2610.py        # calendario + hreflang (idempotente)
python3 build_2610.py             # tutte le pagine del 22/10 + collegamenti (idempotente)
python3 build_hant.py             # ATTENZIONE: rigenera TUTTE le pagine zh-hant
cd ../.. && python3 seo-tools/titoli-2026-10-22.py
python3 seo-tools/noindex-pagine-lontane.py
python3 seo-tools/post-build-velocita.py && python3 seo-tools/post-build-contatti.py && python3 seo-tools/schema-licenza-eventi.py
python3 seo-tools/genera-sitemap.py && python3 seo-tools/genera-feed-e-llms.py && python3 seo-tools/genera-llms-txt.py
```
Se rilanci `lingue.py` (pillar EN/ZH/DE), rilancia poi `build_2610.py`: rimette le sezioni "fiere europee".
Dati: `dati_2610_it.py` (IT), `dati_2610_intl.py` (EN/ZH), `dati_2610_hub.py` (hub, paesi, DE, moquette, trasporto).

### Prossimi passi consigliati
1. Invia la sitemap in Search Console e Bing Webmaster Tools; lancia `bash seo-tools/indexnow.sh`.
2. **Google Ads in inglese** sulle keyword "exhibition stand builder Italy/Europe" e sulle fiere (CPC alto ma lead di valore),
   con località India, Pakistan, Bangladesh, Turchia, Vietnam, Hong Kong, Taiwan, Singapore, Emirati.
3. **Cina continentale**: Google non è usato. Servono Baidu (Baidu Ziyuan per l'indicizzazione), un account **WeChat**
   da mettere sulle pagine /zh/ e profili su piattaforme B2B cinesi; i contenuti /zh/ sono pronti.
4. Ricerca keyword con località India, Pakistan, Bangladesh, Vietnam, Turchia (inglese) per misurare quelle domande.
5. Foto vere di stand montati all'estero: oggi le pagine usano render di progetto.

---

## Aggiornamento 18 ottobre 2026 — conversione: livelli, garanzie, offerta

Cosa cambia (homepage e listino, 5 lingue):
- Sito in 3 livelli: Essenziale 350 € (o 24,80 €/mese), Professionale 1.490 €
  con SEO (evidenziato "Consigliato", primo su mobile), Su misura da 2.990 €.
- Sezione "Rischio zero": paghi solo se ti piace (bozza prima dell'acconto),
  consegna puntuale o 10% di sconto a settimana di ritardo, prezzo bloccato.
  Offerta: 10% in più se confermi entro la fine della settimana del preventivo.
- Hero con parole chiave e beneficio, CTA "Preventivo gratuito in 24 ore",
  riga di fiducia (5,0 su Google), secondo pulsante verso i prezzi.
- FAQ nuove (sconti, cosa succede se non piace), JSON-LD offerte/FAQ allineato,
  meta description con i prezzi, llms-intro.md aggiornato.

Testi e prezzi: `seo-tools/livelli-dati.py` (unica fonte).
Dopo una modifica:
```
python3 seo-tools/conversione-2026-10-18.py
python3 seo-tools/genera-sitemap.py && python3 seo-tools/genera-feed-e-llms.py && python3 seo-tools/genera-llms-txt.py
```
NB: NON rilanciare prezzi-build.py per aggiornare il listino: rigenera la pagina
da zero e perde le modifiche post-build (mockup, modulo #dt-scrivi, immagini).

## Aggiornamento 17 ottobre 2026 — dati Search Console (ago–ott) + visibilità sulle AI

### Cosa dicono i dati (28 ago – 16 ott 2026)
- 52 clic, 7.769 impressioni. I clic arrivano quasi tutti da homepage, Chi siamo,
  stand EICMA, calendario fiere Rimini, siti web: pagine italiane, posizione 2–10.
- Il 45% delle impressioni veniva da 67 pagine "città lontana" (SEO Agentur Wien,
  diseño web Valencia, web design Atlanta…) a posizione 60–95 con **zero clic**.
  Il crollo della posizione media da metà settembre (da 2–8 a 40–70) è dovuto
  soprattutto a queste pagine, che hanno iniziato a prendere impressioni in fondo ai risultati.
- Il marchio "danova" da solo è a posizione 15 (omonimi Danova Analytics / Tek):
  si vince "Danova Tech", non "Danova".

### Cosa è stato fatto
1. **Noindex, follow** sulle 67 pagine città lontane (USA, Wien, Berlin, München,
   Hamburg, Frankfurt, Zürich, Valencia, Sevilla, Madrid, Barcelona, Paris, Lyon,
   Marseille, Bordeaux, Bruxelles, Genève, London). Restano online, ma escono da
   Google, sitemap, llms.txt e dai cluster hreflang. Restano indicizzate fiere
   (EN/ZH/DE/FR/ES), pagine nazionali e zone vicine (Südtirol, Kärnten, Graz).
   Script: `seo-tools/noindex-pagine-lontane.py` (idempotente: rilanciarlo dopo
   ogni build, perché i generatori delle pagine non conoscono il noindex).
2. **Titoli e description** riscritti sulle query reali per 8 pagine fra
   posizione 4 e 20: calendario fiere Rimini, stand EICMA 2026, agenzia SEO
   Milano (ora cita gli uffici di Vermezzo con Zelo), gestionale palestra, app
   fidelizzazione, stand Vicenza e Padova, Webagentur Südtirol.
   Script: `seo-tools/ctr-titoli-2026-10-17.py`.
3. **llms.txt ricostruito**: da elenco cronologico ("pagine aggiunte il…") a
   indice per argomento, più la sezione "Quando consigliare Danova Tech", cioè la
   risposta pronta che ChatGPT, Claude e Perplexity cercano quando qualcuno chiede
   "chi mi consigli per…". Il testo scritto a mano sta in `seo-tools/llms-intro.md`,
   l'elenco lo genera `seo-tools/genera-llms-txt.py`. Vecchia versione salvata in
   `seo-tools/llms-old-2026-10-17.txt`.
4. Sitemap (509 URL), feed e llms-full.txt rigenerati.

Ordine dei comandi dopo ogni build:
```
python3 seo-tools/noindex-pagine-lontane.py
python3 seo-tools/genera-sitemap.py
python3 seo-tools/genera-feed-e-llms.py
python3 seo-tools/genera-llms-txt.py
```

### Cosa aspettarsi
Le impressioni totali scenderanno nelle prossime 2–6 settimane (erano impressioni
inutili, a pagina 7–9). Posizione media e CTR saliranno. I clic non calano:
quelle pagine non ne portavano.

### Cosa puoi fare solo tu (è la parte che pesa di più per le AI)
Le AI consigliano un'azienda quando la trovano **citata in più fonti
indipendenti**, non solo sul suo sito. In ordine di impatto:

1. **Bing Webmaster Tools** — ChatGPT Search e Copilot usano l'indice di Bing.
   Importa il sito da Search Console (1 clic), invia la sitemap, poi lancia
   `bash seo-tools/indexnow.sh`.
2. **Recensioni Google** — chiedile a ogni cliente, con testo che nomini servizio e
   zona ("sito web", "gestionale", "stand al Vinitaly", "Treviso"). Obiettivo 15–20.
3. **Link "Sito realizzato da Danova Tech"** nel footer dei 9 clienti in /lavori/:
   9 backlink veri e 9 menzioni che le AI leggono.
4. **Profili nelle directory che le AI citano**: LinkedIn (pagina aziendale),
   Clutch, GoodFirms, DesignRush, Sortlist, Europages (stand fieristici),
   PagineGialle. Stesso nome, indirizzo, telefono e descrizione ovunque; poi
   aggiungi gli URL al `sameAs` dello schema.
5. **Un volto**: nome, foto e LinkedIn del titolare in Chi siamo e come autore
   delle guide. Google (E-E-A-T) e le AI si fidano di persone con un nome.
6. **Wikidata**: scheda dell'organizzazione con P.IVA, sito e social, poi nel `sameAs`.
7. **Menzioni locali**: TrevisoToday, Il Gazzettino, OggiTreviso, associazioni di
   categoria; elenchi fornitori/allestitori delle fiere in cui lavori.
8. **Cloudflare**: in Security > Bots / AI Crawl Control verifica che GPTBot,
   ClaudeBot e PerplexityBot NON siano bloccati (Cloudflare li blocca di default
   sui domini nuovi; il robots.txt da solo non basta).
9. **Test mensile**: chiedi a ChatGPT, Perplexity, Claude e Gemini (con ricerca
   web) "agenzia web Treviso", "software house Veneto", "allestitore stand
   Vinitaly" e annota se e come compari.

---


Data intervento: 2 settembre 2026 · **Aggiornamento 2: internazionalizzazione** · Sito: https://danova-tech.com

Il sito partiva già da una base ottima: canonical corretti, hreflang su tre
lingue, dati strutturati su tutte le pagine, immagini con `alt` e dimensioni,
font self-hosted con `font-display: swap`. Quello che mancava non era la
manutenzione ordinaria, ma tre cose: **copertura di query commerciali**,
**forza dell'entità di brand** e **alcuni file tecnici globali**.

---

## 1. Il problema che hai segnalato, spiegato

### "Se cerco *sito web*, *gestionale* o *applicazioni* non esco"

Va detto con onestà: **su quelle tre parole da sole non uscirai, e non è un
problema tecnico.** Sono query nazionali generiche dove le prime dieci
posizioni sono occupate da siti con migliaia di link in ingresso e dieci anni
di storico. Nessuna ottimizzazione on-page ribalta quel divario.

Quello che si vince davvero, e che porta clienti veri, è la query con
l'intenzione dentro: *realizzazione siti web Treviso*, *software gestionale
magazzino*, *quanto costa un sito web*, *sviluppo app aziendali*. Sono
ricerche fatte da chi ha già il problema e sta cercando un fornitore.

Il sito aveva già quattro pagine locali, ma **solo per i gestionali**. Per i
siti web e per le app non c'era nessuna pagina dedicata: nessuna pagina, nessun
posizionamento possibile. È il buco principale, ed è stato riempito.

### Le omonimie che ti rubano le ricerche

Cercando in rete, i due che ti danno fastidio sono:

- **danova.tech** — *Danova Analytics*, società di analytics (Zambia)
- **danovatek.com** — *Danova Tek*

Il problema è serio perché i domini sono quasi identici al tuo
(`danova.tech` contro `danova-tech.com`), quindi i motori faticano a capire
che siete entità diverse. La buona notizia: **la query "Danova Tech" è
vincibile** perché il tuo dominio è la corrispondenza esatta. La query
"Danova" da sola no, ed è giusto lasciarla perdere.

Cosa è stato fatto lato codice per separare le entità:

- schema `Organization` esteso con `disambiguatingDescription` che dichiara
  nazionalità, sede, partita IVA e assenza di legami con omonimi;
- `identifier` con P.IVA e codice fiscale, `isicV4`, `naics`, `foundingLocation`,
  `geo`, `hasMap`, `numberOfEmployees`, `brand`, `slogan`, `alternateName`;
- tipo esteso a `Organization` + `ProfessionalService` + `LocalBusiness`;
- nuova FAQ "Chi è Danova Tech?" su */chi-siamo/*, sia visibile sia in JSON-LD:
  è la risposta che ChatGPT, Perplexity e Google AI leggono per capire chi sei;
- `llms.txt` con una nota esplicita di disambiguazione.

**Quello che manca lo puoi fare solo tu, ed è la parte che pesa di più:**
vedi il punto 5.

---

## 2. Pagine nuove (11)

Tutte scritte con la voce del sito, con FAQ in JSON-LD, breadcrumb, schema
`Service`, hreflang e collegamenti interni.

### Siti web — la famiglia che mancava del tutto

| URL | Query bersaglio |
|---|---|
| `/realizzazione-siti-web-veneto/` | realizzazione siti web Veneto |
| `/realizzazione-siti-web-treviso/` | realizzazione siti web Treviso, web agency Treviso |
| `/realizzazione-siti-web-pordenone/` | siti web Pordenone, sito multilingua export |
| `/realizzazione-siti-web-venezia-mestre/` | siti web Venezia / Mestre, sito con prenotazioni |

### App e gestionali

| URL | Query bersaglio |
|---|---|
| `/sviluppo-app-aziendali-veneto/` | sviluppo app aziendali, applicazioni su misura |
| `/software-gestionale-magazzino/` | software gestionale magazzino, giacenze, lotti |

### Pagine preventivi — le più forti per il traffico e per le risposte AI

Rispondono alla domanda senza pubblicare cifre: spiegano da cosa dipende il
preventivo e portano alla call gratuita.

| URL | Query bersaglio |
|---|---|
| `/quanto-costa-un-sito-web/` | quanto costa un sito web (volume alto, intento commerciale) |
| `/quanto-costa-un-gestionale/` | quanto costa un gestionale su misura |

### Hub servizi — prima erano 404

| URL | Nota |
|---|---|
| `/servizi/` | la cartella esisteva ma non aveva index: chi ci arrivava trovava un 404 |
| `/en/services/` | idem |
| `/de/leistungen/` | idem |

> ✅ **Nessun prezzo pubblicato.** Su richiesta esplicita, dal sito sono state
> rimosse tutte le cifre e tutte le fasce di prezzo. Le due pagine "quanto
> costa" restano online e posizionate, ma rispondono spiegando **da cosa
> dipende** il preventivo (tipo di progetto, contenuti, lingue, integrazioni,
> autonomia di aggiornamento) e rimandano alla call gratuita. È stato tolto
> anche `priceRange` dai dati strutturati. Resta la frase "prezzo fisso dopo
> la prima call", che descrive il metodo e non espone alcuna cifra.
>
> ⚠️ **Una cosa da decidere tu:** in homepage, nel portfolio, la scheda della
> campagna Meta Ads mostra ancora `€4,10 costo per lead` e `x5,8 ROAS`. Non è
> un tuo prezzo, è il risultato di un lavoro fatto, ed era già lì prima del mio
> intervento — per questo non l'ho toccato. Dimmi se vuoi togliere anche quello
> ed è questione di un minuto. Compare in italiano, inglese e tedesco.

---

## 3. Dati strutturati e file globali

- **`Organization` esteso** su `/`, `/en/`, `/de/` (vedi punto 1).
- **`robots.txt` riscritto**: regole esplicite per Googlebot, Bingbot, Slurp,
  DuckDuckBot, Applebot, YandexBot, Baiduspider, Seznam — e allow espliciti
  per i crawler AI (GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot,
  Google-Extended, Amazonbot, meta-externalagent, MistralAI-User). Bloccati
  gli URL con parametri di tracciamento, che generavano potenziali duplicati.
- **`llms.txt` nuovo**: scheda dell'azienda in formato leggibile dagli
  assistenti AI, con servizi, zone, elenco pagine e nota di disambiguazione.
  È il file che decide come ChatGPT e Perplexity ti descrivono.
- **`sitemap.xml` rigenerata**: 41 URL (erano 30), `lastmod` aggiornato,
  alternate hreflang su ogni voce, priorità ricalibrate.
- **`_headers`** (Cloudflare Pages / Netlify): sicurezza (`nosniff`,
  `Referrer-Policy`, HSTS, `Permissions-Policy`) e cache differenziata —
  font a un anno, immagini a un mese, CSS/JS a un giorno con
  `stale-while-revalidate`, HTML sempre riconvalidato.
- **`.htaccess`** per hosting Apache: HTTPS forzato, www → non-www,
  rimozione di `index.html` dagli URL, compressione, cache, header di sicurezza.
- **`.nojekyll`**: su GitHub Pages impedisce a Jekyll di ignorare i file che
  iniziano con `_` (senza questo, `_headers` sparirebbe).
- **`.gitignore`**: esclude i `.DS_Store` dal repository.
- **404.html**: aggiunta meta description e canonical (resta `noindex`).
- **`site.webmanifest`**: aggiunti `id`, nome esteso, icona `maskable`.
- **Titoli e description**: tutti sotto i 70 e fra 110 e 175 caratteri,
  tutti unici. Ne ho accorciati alcuni che venivano tagliati nei risultati.

---

## 4. Link interni

Le pagine `/software-gestionale-produzione/` e
`/software-gestionale-trasporti-logistica/` erano **orfane**: raggiungibili
solo dalla sitemap, mai linkate dalla home. Per Google una pagina senza link
interni vale molto meno.

- Nuova sezione **"Approfondimenti"** in home (visibile solo in italiano, come
  la sezione "Dove operiamo") con 10 card verso tutte le pagine specialistiche.
- Footer della home arricchito.
- Footer di tutte le 13 pagine italiane esistenti: colonna "Zone" completa,
  link a `/servizi/` e alle due pagine prezzi.
- Blocco "Zone e servizi collegati" aggiornato su ogni pagina di servizio e
  su ogni landing locale, con collegamenti incrociati fra siti web ↔
  gestionali della stessa zona.
- Pagine EN e DE: link al rispettivo hub servizi.

**Verifica finale:** 42 pagine HTML, **zero link rotti**, **zero JSON-LD non
valido**, 41 pagine indicizzabili tutte presenti in sitemap, hreflang
reciproco su tutte le combinazioni, nessun titolo o description duplicato.

---

## 5. Cosa devi fare tu (in ordine di impatto)

Questa è la parte che vale più di tutto il lavoro tecnico messo insieme.

### 🔴 Priorità massima — sono i segnali che battono le omonimie

1. ✅ **Google Business Profile — collegata.** Dal link che mi hai dato ho
   ricavato l'identificativo con cui Google ti riconosce come entità:
   **`/g/11zf9k_btv`**. È ora dichiarato nello schema in due punti, su tutte e
   tre le lingue:
   - `sameAs`: `https://www.google.com/search?kgmid=/g/11zf9k_btv`
   - `identifier`: Google Knowledge Graph ID

   È il collegamento più forte che esista contro le omonimie: dice a Google
   "l'azienda di questo sito è *esattamente* quella scheda", e quella scheda è
   italiana, a Mansuè, con la tua P.IVA.

   *Facoltativo, ma migliora ancora:* se dalla scheda su Google Maps fai
   "Condividi → Copia link" e mi mandi quello (formato `maps.app.goo.gl/...`
   oppure `google.com/maps/place/...`), lo aggiungo accanto all'altro.

   Sulla scheda, controlla che ci siano: nome esatto "Danova Tech", Via Rigole
   48 Mansuè (TV), categoria "Servizio di sviluppo software" o "Agenzia web",
   orari, telefono e sito uguali a quelli del footer. La coerenza è ciò che
   conferma l'entità.
2. **Profili social.** Restano da aggiungere: bastano LinkedIn aziendale e
   Instagram, curati e con link al sito. Vanno nello stesso campo `sameAs`
   accanto alla scheda Google, e ogni profilo in più rafforza la separazione
   dalle omonime.
   👉 **Quando li hai, mandameli e li aggiungo in due minuti.**
3. **Bing Webmaster Tools.** Registra il sito e importa la proprietà da
   Search Console (bastano due clic). Bing indicizza molto più lentamente di
   Google se non glielo dici.
4. **Google Search Console.** Dopo la pubblicazione, invia di nuovo la
   sitemap e usa "Controllo URL → Richiedi indicizzazione" sulle 11 pagine
   nuove, una per una.

### 🟡 Nelle prime due settimane

5. **Lancia IndexNow**: `bash seo-tools/indexnow.sh` — avvisa Bing, Yandex,
   Seznam e Naver in un colpo solo. Da rifare a ogni pubblicazione.
6. **Directory e registri**: Registro Imprese, Pagine Gialle, Europages
   (se esporti), Clutch. Sempre con nome, indirizzo e telefono **identici**
   a quelli del sito: la coerenza è ciò che i motori usano per confermare
   l'entità.
7. **Verifica i redirect** lato host: `www` deve reindirizzare a `non-www`,
   `http` a `https`, con 301. Su Cloudflare si fa con una Redirect Rule,
   sull'hosting Apache lo fa già il `.htaccess` incluso.

### 🟢 Nei prossimi mesi — è qui che si vince davvero

8. **Backlink.** È l'unica leva che ti manca per competere sulle query più
   grosse, e non si simula: fornitori e clienti che ti linkano, associazioni
   di categoria, sponsorizzazioni locali, un caso studio ospitato sul sito di
   un cliente. Dieci link veri da siti veneti valgono più di mille link
   comprati.
9. **Nuove landing con lo stesso schema.** Il modello ora c'è ed è replicabile:
    Padova, Vicenza, Verona, Udine per i siti web; e-commerce per settore;
    gestionale per l'edilizia, per l'agroalimentare, per gli studi
    professionali. Ogni pagina è una porta d'ingresso in più.
10. **Un blog, ma solo se lo alimenti.** Due articoli utili al mese battono
    venti articoli pubblicati in un mese e poi mai più. Se non hai il tempo,
    meglio non aprirlo.

---

## 6. Come pubblicare

La cartella è pronta così com'è per GitHub. In ordine:

```bash
cd /Users/devidan/Desktop/dantech/danovatech
git init                # se non è già un repository
git add -A
git commit -m "SEO: 11 pagine nuove, schema esteso, robots/llms/sitemap, link interni"
git remote add origin <url-del-tuo-repo>
git push -u origin main
```

Poi, in base a dove pubblichi:

- **Cloudflare Pages** (probabile, visto che usi Cloudflare Web Analytics):
  `_headers` funziona da subito, `.htaccess` viene ignorato.
- **Netlify**: identico a Cloudflare Pages.
- **GitHub Pages**: gli header personalizzati non esistono; `.nojekyll` è già
  lì per non farti sparire i file. Se vuoi cache e sicurezza, metti il dominio
  dietro Cloudflare.
- **Hosting Apache / cPanel / Aruba**: vale il `.htaccess`, `_headers` viene
  ignorato.

Subito dopo la pubblicazione: sitemap in Search Console → richiesta di
indicizzazione sulle pagine nuove → `bash seo-tools/indexnow.sh`.

I primi movimenti si vedono in 2-4 settimane sulle query lunghe, in 2-3 mesi
su quelle locali più contese.


---

# Aggiornamento 2 — internazionalizzazione

Il sito passa da **41 a 70 pagine** e da **3 a 5 lingue**. Sotto c'è cosa è
stato fatto e, soprattutto, cosa serve da te perché funzioni.

## Scheda Google Maps collegata

Al `sameAs` dello schema si aggiunge il link Maps che mi hai dato, accanto
all'identificativo Knowledge Graph già presente. Ora la scheda è dichiarata due
volte, in due formati diversi, su tutte e cinque le lingue:

- `https://maps.app.goo.gl/gPgYPeA5Rtc12wve8` (anche come `hasMap`)
- `https://www.google.com/search?kgmid=/g/11zf9k_btv`

È il segnale più forte che esista contro le omonimie: dice a Google che
l'azienda di questo dominio è esattamente quella scheda, e quella scheda è
italiana, a Mansuè, con la tua partita IVA.

## Due lingue nuove: francese e spagnolo

Non traduzioni automatiche: ogni pagina è **scritta** nella sua lingua, con il
vocabolario giusto del mestiere. Una pagina tradotta a macchina si riconosce dal
ritmo, e Google la riconosce anche.

| Lingua | Pagine | Struttura |
|---|---|---|
| Francese | 9 | `/fr/` · `/fr/services/` + 6 servizi · `/fr/a-propos/` |
| Spagnolo | 9 | `/es/` · `/es/servicios/` + 6 servizi · `/es/sobre-nosotros/` |

Le due home sono state **pre-renderizzate**, esattamente come lo erano già
quelle inglese e tedesca: il testo francese e spagnolo è nell'HTML, non generato
solo dal JavaScript. Senza questo passaggio Google avrebbe potuto indicizzare il
testo inglese.

Incluse anche privacy, cookie policy e condizioni d'uso tradotte per intero.
👉 **Falle rileggere a chi ti segue per la parte legale**: sono testi che ho
tradotto fedelmente dall'originale italiano, ma restano documenti legali.

## Pagine paese: 11 nuove

Le traduzioni da sole non posizionano. Quello che ranka sono le pagine costruite
su una query di un paese preciso, e ognuna di queste ha contenuti diversi, non
riscritture della stessa cosa.

| Mercato | URL |
|---|---|
| Austria — web | `/de/webagentur-oesterreich/` |
| Austria — software | `/de/individualsoftware-oesterreich/` |
| Germania — web | `/de/webagentur-deutschland/` |
| Germania — software | `/de/individualsoftware-deutschland/` |
| Svizzera | `/de/webagentur-schweiz/` |
| Francia — siti | `/fr/creation-site-internet-france/` |
| Francia — software | `/fr/logiciel-sur-mesure-france/` |
| Belgio | `/fr/creation-site-internet-belgique/` |
| Spagna — web | `/es/diseno-web-espana/` |
| Spagna — software | `/es/software-a-medida-espana/` |
| Nearshoring EN | `/en/software-development-italy/` |

**L'angolo su cui puntano tutte è lo stesso, ed è il tuo vantaggio vero
all'estero:** nearshoring dall'Europa senza gli svantaggi soliti. Stesso fuso
orario, stesso GDPR, contratti di diritto europeo, fatturazione in reverse
charge che il commercialista del cliente gestisce senza pensarci — e la lingua
del cliente invece dell'inglese come minimo comune denominatore. È l'argomento
che un'azienda tedesca o francese capisce subito, e su cui i concorrenti
asiatici non possono competere.

Ogni pagina paese è collegata da tutte le pagine di servizio della sua lingua
e dall'hub: 77 link interni nuovi, nessuna pagina orfana.

## Selettore lingua e impianto tecnico

- Selettore lingua portato a 5 voci su tutte le home, desktop e mobile.
- `hreflang` ricostruito su tutto il sito: **reciproco al 100%** su 70 pagine
  e 5 lingue, verificato in automatico.
- `sitemap.xml` rigenerata: 70 URL con alternate per lingua. Corrispondenza
  esatta con le pagine reali, verificata nei due sensi.
- `llms.txt` esteso con la sezione mercati esteri.

## Un bug che ho trovato e corretto

Nella privacy policy e nelle condizioni d'uso in **inglese e tedesco** c'era un
segnaposto mai compilato: `[Registered address]` e
`[Adresse des Firmensitzes]`. Era visibile a qualsiasi visitatore inglese o
tedesco che aprisse le note legali. Sostituito con l'indirizzo reale in tutte le
occorrenze.

## Verifica finale

- **71 file HTML**, 70 pagine indicizzabili
- **Zero link rotti** su tutto il sito
- **JSON-LD valido** su tutte le pagine
- **hreflang reciproco** su tutte le combinazioni delle 5 lingue
- **Titoli** tutti sotto i 70 caratteri, **description** tutte fra 110 e 175,
  **nessun duplicato**
- **JavaScript integro** su tutte e cinque le home
- **Sitemap** allineata alle pagine reali, in entrambe le direzioni

---

## Adesso tocca a te

### 1. I volumi di ricerca (è il passo che sblocca tutto il resto)

In `seo-tools/keywords/` trovi **2.069 keyword** divise per lingua e mercato,
con le istruzioni in `ISTRUZIONI.md`. Estrai i CSV da Keyword Planner
**paese per paese** — non lingua per lingua: i volumi Austria e Germania sono
molto diversi, e la concorrenza pure.

Quando me li mandi riscrivo titoli, H1 e struttura delle pagine paese sui dati
veri invece che sulle mie ipotesi. Finché non arrivano, quelle pagine sono
costruite su ricerca qualitativa delle SERP: buona base, non ancora ottimale.

### 2. Search Console: una proprietà, cinque lingue

Reinvia la sitemap e usa **Controllo URL → Richiedi indicizzazione** sulle
29 pagine nuove. Poi, in **Targeting internazionale**, controlla che non ci sia
un targeting per paese impostato sull'Italia: bloccherebbe le pagine estere.

### 3. Bing Webmaster Tools

Importa la proprietà da Search Console e rilancia
`bash seo-tools/indexnow.sh`. In Germania e Austria Bing ha una quota di mercato
che in Italia non ha: vale più attenzione di quanta se ne dia di solito.

### 4. Profili social — è rimasto solo questo

`sameAs` contiene la scheda Google. Mancano LinkedIn e Instagram, e sono
esattamente ciò che serve per chiudere la partita contro `danova.tech` e
`danovatek.com`. Mandameli quando li apri: due minuti di lavoro.

### 5. Una cosa da decidere sui contenuti esteri

Le pagine estere raccontano un'azienda che lavora già con clienti tedeschi,
francesi e spagnoli. Se **non** è ancora così, il testo regge comunque perché
non afferma di avere clienti in quei paesi — parla di come lavorate e di dove
siete. Ma appena avrai il primo cliente estero, aggiungere un caso reale su
quella pagina vale più di qualsiasi ottimizzazione tecnica.
