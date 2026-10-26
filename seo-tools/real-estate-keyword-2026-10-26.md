# Danova Real Estate — ricerca keyword Google Ads (26/10/2026)

Fonte: Strumento di pianificazione delle parole chiave (account senza campagne attive: volumi in fasce).
Periodo ott 2025 – set 2026.

## 1. Idee per Veneto + Friuli Venezia Giulia (lingua italiana) — 3.535 idee
Seed: ristrutturazione casa/bagno, impresa edile, ristrutturazioni chiavi in mano, general contractor,
cappotto termico, rifacimento facciata, ristrutturazione hotel, arredo hotel, impresa ristrutturazioni.

Fasce: 1K–10K = 11 keyword · 100–1K = 80 · 10–100 = 2.896 · 0–10 = 377

1K–10K (solo VE+FVG): ristrutturazione bagno, ristrutturare un bagno, ristrutturare il bagno, bagno da ristrutturare,
bagno ristrutturazione, ristrutturazione del bagno, ricostruzione bagno, sistemazione bagno, sostituzione bagno,
ristrutturazione di un bagno, impresa edile.

100–1K principali: ristrutturazione casa, ristrutturazioni, ristrutturazioni chiavi in mano, general contractor,
cappotto termico (esterno / interno / casa), rifacimento bagno, rifare il bagno (costi / quanto costa),
ristrutturazione bagno tutto compreso, imprese edili, azienda edile, impresa di costruzioni, ristrutturazione edilizia,
ristrutturare casa costi, costi di ristrutturazione al mq, isolamento termico interno, insufflaggio / isolamento sottotetto,
rifacimento tetto (servizio non offerto).

Volume stimato per tema (somma dei punti medi delle fasce):
cappotto/isolamento 86k · bagno 81k · costi/preventivi 41k · impresa edile/ditta 32k · casa/appartamenti 25k ·
tetto 8k · cartongesso/pareti 5.7k · hotel/contract 5k · mobili/arredo 4.7k · facciate 4.6k · chiavi in mano 3.8k ·
pavimenti 3.1k · serramenti 1.6k · condomini 1.4k · bonus 1.2k · cucina 1.1k · pratiche 0.7k

## 2. Volumi città (Italia, 400 combinazioni servizio × 50 città)
Legenda: IE = impresa edile <città> (anche "imprese edili"), R = ristrutturazioni, B = ristrutturazione bagno,
C = ristrutturazione casa, CT = cappotto termico, GC = general contractor. * = fascia 100–1K, altrimenti 10–100.

- Padova: IE*, R*, B*, C, CT, GC
- Verona: IE*, R*, B*, C, CT, GC
- Trieste: IE*, R*, B, C, CT   ← mancava una pagina
- Treviso: IE*, R, B, C, CT, GC
- Vicenza: IE*, R, B, C, CT, GC
- Udine: IE*, R, B, C, CT, GC
- Venezia / Pordenone: IE, R, B, C, CT, GC
- Belluno: IE, R, B, CT   ← mancava · Rovigo: IE, R, CT ← mancava · Gorizia: IE, R ← mancava
- Mestre: IE, R, B · Montebelluna: IE, R · Conegliano: IE, B · Bassano del Grappa: IE, B, CT ← mancava
- Tutti gli altri comuni testati hanno solo "impresa edile <città>" (10–100): Castelfranco, Oderzo, San Donà, Portogruaro,
  Jesolo, Chioggia, Schio, Thiene, Feltre, Cittadella, Abano, Mirano, Villafranca, Legnago, Adria, Sacile, Monfalcone,
  Codroipo, Cividale, Spilimbergo, Vittorio Veneto, Mogliano, San Bonifacio, Arzignano, Valdagno, Piove di Sacco,
  Tolmezzo, Latisana, Maniago.
- "general contractor" con città: solo nei capoluoghi già coperti. Nessun volume per Trieste/Belluno/Rovigo/Gorizia.

Conclusione: la keyword locale che conta è **"impresa edile <città>"**, più di "ristrutturazioni <città>".

## 3. Lingue straniere (Italia + Germania + Austria + Svizzera + Regno Unito)
Con volume: hotel furniture manufacturer (100–1K); 10–100: house renovation italy, renovating a house in italy,
builders in italy, italian builder, property renovation italy, general contractor italy, hotel furniture italy,
contract furniture italy, bauunternehmen italien, handwerker italien, haus in italien renovieren,
renovare baie, renovare apartament, firma renovari, constructii italia, kompani ndertimi.
Zero o quasi: ricerche locali in inglese/tedesco (renovierung lignano, bauunternehmen gardasee, renovation venice...).

## 4. Cosa è stato fatto (vedi real-estate-dati-3.py e real-estate-tr-*-3.py)
- 14 nuove pagine città × 5 lingue: Trieste, Gorizia, Monfalcone, Belluno, Feltre, Rovigo, Bassano del Grappa, Schio,
  Cittadella, Chioggia, Jesolo, Vittorio Veneto, Codroipo, Cividale del Friuli.
- Titoli città IT: "Impresa edile <città> | Ristrutturazioni chiavi in mano"; H2 e FAQ "impresa edile a <città>".
- Bagno: titolo su "ristrutturazione bagno", FAQ su costi (senza cifre) e "tutto compreso".
- Cappotto: sezione e FAQ su cappotto interno / isolamento dall'interno.
- EN: pagina arredo hotel orientata a "hotel furniture manufacturer".
- 3 nuovi servizi × 5 lingue (confermati dal titolare il 26/10): /rifacimento-tetto/, /isolamento-sottotetto/ (con insufflaggio),
  /pavimentazioni-esterne/. Dati in real-estate-dati-5.py e real-estate-tr-<lingua>-5.py; menu, footer, pagina principale e llms.txt aggiornati.

## 5. Audit e ottimizzazione SEO completa (26/10/2026)
- Titoli: modelli per lingua e tipo di pagina entro ~62 caratteri, con la keyword locale in testa
  (IT "Impresa edile <città>", EN "Builders in <città>", DE "Bauunternehmen in <città>", RO "Firmă de construcții <città>",
  SQ "Kompani ndërtimi <città>"; general contractor e arredo hotel per zona). Da 111 titoli troppo lunghi a 0 oltre 65.
- Description: troncamento di sicurezza nelle description oltre 160 caratteri; corrette a mano quelle troppo lunghe.
- Dati strutturati GeneralContractor: 11 province servite, knowsAbout per lingua, orari, priceRange, slogan.
- Link interni: servizio "Tetto e sottotetto" e guida "come scegliere l'impresa" in tutte le pagine città;
  nuovi servizi e guide collegati dalle pagine servizio correlate.
- Guide: cappotto (svantaggi, mattoni a vista/cortina, isolanti, zone climatiche) e CILA/SCIA (procedura, casi) ampliate;
  2 nuove guide × 5 lingue: /guide/quanto-costa-ristrutturare-casa/ e /guide/come-rifare-il-bagno/ (senza prezzi).
- Immagini Higgsfield (26/10): re-tetto-cantiere, re-sottotetto-insufflaggio, re-terrazzo-esterno, con la scritta del piano
  gratuito ritagliata su richiesta del titolare; alt descrittivi in 5 lingue.

## 6. Seconda ricerca Google Ads (26/10/2026 pomeriggio) — mestieri, bagno, finiture, partner
Località Veneto + Friuli Venezia Giulia (partner: Italia). Fasce ott 2025 – set 2026.

- Mestieri: idraulico, elettricista, impiantista elettrico, falegname, termoidraulica (1K–10K, molto pronto intervento);
  muratore, imbianchino, cartongessista, piastrellista, posatore pavimenti, serramentista, lattoniere, imbianchini/muratore vicino a me (100–1K);
  cerco muratore / per piccoli lavori / per ristrutturazione / per lavori in casa, cerco imbianchino / per pitturare casa / economico (100–1K, Italia).
- Bagno: doccia walk in (1K–10K); trasformazione / sostituzione / trasformare vasca in doccia (+ "prezzi") — decine di varianti 100–1K;
  piatto doccia filo pavimento, doccia filo pavimento (100–1K).
- Finiture: impianto elettrico casa, impianti idraulici (100–1K); impermeabilizzazione terrazzo e varianti (100–1K);
  isolamento acustico, isolamento acustico pareti, insonorizzare una stanza (100–1K); cartongesso prezzo al mq (100–1K); massetto (100–1K, prodotto).
  Basse (10–100): ristrutturazione cucina, tinteggiatura appartamento, sostituzione finestre, ristrutturazione mansarda, rifacimento facciata, preventivo ristrutturazione.
- Partner (Italia): lavora con noi edilizia, subappalto edilizia, cercasi artigiani edili, cerco imprese edili per collaborazione, cerco lavori edili in subappalto (10–100).
  Le ricerche forti sono di chi cerca lavoro da dipendente (cerco lavoro muratore/imbianchino, imprese edili che cercano operai: 100–1K).

Fatto (real-estate-dati-8.py, solo IT): /trasformazione-vasca-in-doccia/, /imbianchino-e-tinteggiature/, /muratore-e-opere-murarie/,
/impianti-elettrici-e-idraulici/ (senza pronto intervento). Cartongesso: sezione "Insonorizzare una stanza" + FAQ prezzo al mq.
Pavimentazioni esterne: H2 e FAQ su impermeabilizzazione del terrazzo. Bagno: link alla pagina vasca/doccia.
Diventa partner: subappalto, artigiani edili, FAQ operai senza partita IVA. Link dalla home Real Estate e dal footer IT.
Da valutare: versioni EN/DE/RO/SQ delle nuove pagine; pagine mestiere + città solo se i volumi locali lo giustificano.
