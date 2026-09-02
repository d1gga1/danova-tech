# Danova Tech — ottimizzazione SEO

Data intervento: 2 settembre 2026 · Sito: https://danova-tech.com

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

### Pagine prezzi — le più forti per il traffico e per le risposte AI

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

> ⚠️ **Da controllare: i prezzi.** Nelle due pagine prezzi ho usato fasce
> realistiche per il mercato italiano (sito vetrina 1.500-3.000 €, sito
> aziendale 3.000-8.000 €, e-commerce da 5.000 €, primo modulo gestionale da
> 5.000-8.000 €, gestionale multi-area 15.000-40.000 €). **Rileggile e
> allineale ai tuoi prezzi veri prima di pubblicare**: sono le uniche cifre
> del sito che non potevo verificare.

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

1. **Google Business Profile.** Se non l'hai, aprila oggi:
   nome esatto "Danova Tech", indirizzo Via Rigole 48, Mansuè (TV), categoria
   "Servizio di sviluppo software" o "Agenzia web", foto vere, orari, sito.
   È il singolo intervento che sposta di più le ricerche locali *e* che
   àncora l'entità "Danova Tech" all'Italia.
2. **Profili social.** Bastano LinkedIn aziendale e Instagram, curati e con
   link al sito. Servono per il campo `sameAs` nei dati strutturati, che è il
   modo con cui Google conferma "questa azienda è questa e non l'altra".
   👉 **Quando li hai, mandameli e li aggiungo allo schema in due minuti.**
   Finché il campo `sameAs` è vuoto, la disambiguazione dalle omonime resta
   a metà.
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
7. **Controlla i prezzi** nelle due pagine nuove (vedi avviso al punto 2).
8. **Verifica i redirect** lato host: `www` deve reindirizzare a `non-www`,
   `http` a `https`, con 301. Su Cloudflare si fa con una Redirect Rule,
   sull'hosting Apache lo fa già il `.htaccess` incluso.

### 🟢 Nei prossimi mesi — è qui che si vince davvero

9. **Backlink.** È l'unica leva che ti manca per competere sulle query più
   grosse, e non si simula: fornitori e clienti che ti linkano, associazioni
   di categoria, sponsorizzazioni locali, un caso studio ospitato sul sito di
   un cliente. Dieci link veri da siti veneti valgono più di mille link
   comprati.
10. **Nuove landing con lo stesso schema.** Il modello ora c'è ed è replicabile:
    Padova, Vicenza, Verona, Udine per i siti web; e-commerce per settore;
    gestionale per l'edilizia, per l'agroalimentare, per gli studi
    professionali. Ogni pagina è una porta d'ingresso in più.
11. **Un blog, ma solo se lo alimenti.** Due articoli utili al mese battono
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
