# Danova Tech — ottimizzazione SEO

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
