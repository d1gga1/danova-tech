#!/usr/bin/env python3
"""17/10/2026: genera /stand-fieristici/ (hub di tutte le pagine stand) e /sicurezza-stand-fieristici/.
Riusa header, footer, modulo richiesta e stili di /stand-fieristici-per-metratura/. Rilanciabile."""
import os,re,json,html
from bs4 import BeautifulSoup
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
D="https://danova-tech.com"; OGGI="2026-10-17"
T=open("stand-fieristici-per-metratura/index.html",encoding="utf-8").read()
def esc(s): return html.escape(s,quote=True)
def titolo(slug):
    if not os.path.isfile(slug.strip("/")+"/index.html"): return "Sicurezza e materiali Classe 1"
    h=open(slug.strip("/")+"/index.html",encoding="utf-8").read()
    t=re.search(r"<title>([^<]*)",h).group(1)
    t=html.unescape(t).split(" | ")[0].split(" — ")[0]
    return t
def link(slug,label=None):
    return f'<a href="{slug}">{esc(label or titolo(slug))}</a>'
def dirs(prefix):
    return sorted(d for d in os.listdir(".") if d.startswith(prefix) and os.path.isfile(d+"/index.html"))

def pagina(slug,title,desc,ogt,ogd,crumb,eyebrow,h1,h1b,lead,cta2,main,faq,ld_extra):
    url=D+slug
    h=T
    head_end=h.index('<script type="application/ld+json">')
    head=h[:head_end]
    rep=[(r"<title>[^<]*</title>",f"<title>{esc(title)}</title>"),
         (r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{esc(desc)}">'),
         (r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="{url}">'),
         (r'<link rel="alternate" hreflang="it" href="[^"]*">',f'<link rel="alternate" hreflang="it" href="{url}">'),
         (r'<link rel="alternate" hreflang="x-default" href="[^"]*">',f'<link rel="alternate" hreflang="x-default" href="{url}">'),
         (r'<meta property="og:url" content="[^"]*">',f'<meta property="og:url" content="{url}">'),
         (r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{esc(ogt)}">'),
         (r'<meta name="twitter:title" content="[^"]*">',f'<meta name="twitter:title" content="{esc(ogt)}">'),
         (r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{esc(ogd)}">'),
         (r'<meta name="twitter:description" content="[^"]*">',f'<meta name="twitter:description" content="{esc(ogd)}">')]
    for a,b in rep: head=re.sub(a,lambda m:b,head,count=1)
    # nodo Organization completo, preso dalla pagina modello
    ld=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',h,re.S).group(1))
    org=[n for n in ld["@graph"] if n.get("@id")==D+"/#organization"][0]
    graph=[org,
      {"@type":"WebSite","@id":D+"/#website","url":D+"/","name":"Danova Tech","inLanguage":"it"},
      {"@type":ld_extra.pop("_type","WebPage"),"@id":url+"#webpage","url":url,"name":title,"description":desc,
       "isPartOf":{"@id":D+"/#website"},"inLanguage":"it","datePublished":OGGI,"dateModified":OGGI,
       "breadcrumb":{"@id":url+"#breadcrumb"},"publisher":{"@id":D+"/#organization"},
       "primaryImageOfPage":{"@type":"ImageObject","url":re.search(r'<meta property="og:image" content="([^"]+)"',h).group(1)}},
      {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":D+"/"}]+
        ([{"@type":"ListItem","position":2,"name":"Stand fieristici","item":D+"/stand-fieristici/"}] if slug!="/stand-fieristici/" else [])+
        [{"@type":"ListItem","position":2 if slug=="/stand-fieristici/" else 3,"name":crumb,"item":url}]},
      {"@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub("<[^>]+>","",a)}} for q,a in faq]}]
    for k,v in ld_extra.items(): graph.append(v)
    ldtxt='<script type="application/ld+json">\n'+json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False,indent=2)+'\n</script>\n'
    # header/nav dal modello, main nuovo, footer dal modello
    after_ld=h[h.index('</script>',head_end)+len('</script>'):h.index('<main id="main">')]
    after_ld=after_ld.replace('href="/stand-fieristici-per-metratura/" hreflang="it"',f'href="{slug}" hreflang="it"')
    richiesta=h[h.index('<section id="richiesta"'):h.index('<section id="faq">')]
    tail=h[h.index('</main>'):]
    crumbs=f'<a href="/">Home</a><em>/</em>'+('' if slug=="/stand-fieristici/" else '<a href="/stand-fieristici/">Stand fieristici</a><em>/</em>')+esc(crumb)
    faqhtml="\n".join(f'      <details data-rv="up"><summary>{esc(q)}<span class="pm"></span></summary>\n        <div class="ans"><p>{a}</p></div></details>' for q,a in faq)
    body=f'''<main id="main">

<div class="wrap pg-crumbs">
  {crumbs}
</div>

<section class="pg-hero">
  <div class="wrap">
    <div class="eyebrow mono" data-scramble>{esc(eyebrow)}</div>
    <h1 data-rv="up">{esc(h1)} <span class="grad">{esc(h1b)}</span></h1>
    <p class="lead" data-rv="up">{lead}</p>
    <div class="hero-cta" data-rv="up">
      <a href="#richiesta" class="btn btn-p" data-mag><span class="sheen"></span><span class="lbl">Richiedi un preventivo</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></a>
      {cta2}
    </div>
  </div>
</section>
{main}
{richiesta}<section id="faq">
  <div class="wrap">
    <div class="sec-head">
      <div class="eyebrow mono" data-scramble>Domande frequenti</div>
      <h2 class="title" data-rv="up">Le risposte che <span class="grad">servono davvero.</span></h2>
    </div>
    <div class="faq">
{faqhtml}
    </div>
  </div>
</section>

'''
    out=head+ldtxt+after_ld+body+tail
    os.makedirs(slug.strip("/"),exist_ok=True)
    open(slug.strip("/")+"/index.html","w",encoding="utf-8").write(out)
    print("scritta",slug,len(out))

def sezione(id_,h2,h2b,lead,blocco):
    return f'''<section id="{id_}">
  <div class="wrap">
    <div class="sec-head">
      <h2 class="title" data-rv="up">{esc(h2)} <span class="grad">{esc(h2b)}</span></h2>
      {f'<p class="lead" data-rv="up">{lead}</p>' if lead else ''}
    </div>
    {blocco}
  </div>
</section>'''
def altri(slugs,labels=None):
    labels=labels or {}
    return '<div class="pg-altri" data-rv="up">'+"\n      ".join(link(s,labels.get(s)) for s in slugs)+'</div>'

# ------------------------------------------------------------------ HUB
servizi=["/servizi/allestimenti-fieristici/","/stand-fieristici-su-misura/","/stand-modulari/","/stand-preallestiti/","/noleggio-stand-fieristici/",
 "/progettazione-stand-fieristici/","/montaggio-stand-fieristici/","/grafica-per-stand-fieristici/","/ledwall-e-illuminazione-stand/",
 "/espositori-desk-totem-per-fiere/","/totem-pubblicitari/","/espositori-pubblicitari/","/stand-fieristici-ecosostenibili/","/allestimenti-eventi-showroom-negozi/"]
tipi=["/stand-a-isola/","/stand-ad-angolo/","/stand-a-due-piani/","/stand-fieristici-piccoli/","/stand-fieristici-per-metratura/"]+["/"+d+"/" for d in ["stand-9-mq","stand-12-mq","stand-16-mq","stand-24-mq","stand-32-mq","stand-48-mq","stand-100-mq"]]
settori=["/"+d+"/" for d in dirs("stand-fieristici-") if d not in ("stand-fieristici-su-misura","stand-fieristici-per-metratura","stand-fieristici-piccoli","stand-fieristici-ecosostenibili")]
esclusi=set(s.strip("/") for s in servizi+tipi+settori)|{"stand-modulari","stand-preallestiti"}
fiere=["/"+d+"/" for d in dirs("stand-") if d not in esclusi and not d.startswith("stand-fieristici")]
citta=["/"+d+"/" for d in dirs("allestimenti-fieristici-")]
regioni=[c for c in citta if any(x in c for x in ("lombardia","veneto","emilia-romagna","estero","germania"))]
citta=[c for c in citta if c not in regioni]
cal=["/calendario-fiere/"]+["/"+d+"/" for d in dirs("calendario-fiere-")]
prezzi=["/quanto-costa-uno-stand-fieristico/","/contributi-fiere-2026/","/idee-stand-fieristici/","/progetti-stand-fieristici/","/sicurezza-stand-fieristici/"]
guide=["/guide/"+g+"/" for g in ["come-preparare-una-fiera","quanto-costa-partecipare-a-una-fiera","come-scegliere-un-allestitore-fieristico","regolamento-tecnico-fiera","materiali-ignifughi-stand","dichiarazione-di-conformita-stand","come-attirare-visitatori-allo-stand","come-raccogliere-contatti-in-fiera"] if os.path.isfile("guide/"+g+"/index.html")]
def lab_citta(s): return titolo(s).split(":")[0].replace("Allestimenti fieristici ","").strip().capitalize() if False else titolo(s).split(":")[0]
def lab_corto(s):
    t=titolo(s); return t.split(":")[0].strip()
numeri='''<dl class="fr-scheda" data-rv="up">
      <div><dt>Stand montati</dt><dd>Oltre 300, in Italia e all'estero</dd></div>
      <div><dt>Esperienza</dt><dd>Team con oltre 20 anni in fiera</dd></div>
      <div><dt>Quartieri</dt><dd>Veronafiere, Fiera Milano, Bologna, Rimini, Parma</dd></div>
      <div><dt>Estero</dt><dd>Stand montati in 11 paesi europei</dd></div>
      <div><dt>Materiali</dt><dd>Certificati in Classe 1 di reazione al fuoco</dd></div>
      <div><dt>Referente</dt><dd>Uno solo, dal progetto allo smontaggio</dd></div>
    </dl>'''
come='''<div class="pg-testo" data-rv="up">
      <p>Progettiamo noi ogni stand, sul tuo marchio e sul regolamento tecnico della fiera. Strutture, pareti e arredi in legno li realizzano laboratori partner con cui lavoriamo da anni; trasporto e montaggio li gestiamo noi, con trasportatori e squadre partner di fiducia e un unico capocantiere. Tra una fiera e l'altra lo stand resta nei nostri magazzini di Fontanelle (TV) e Trumello (PV).</p>
      <p>Per te cambia una cosa sola: hai un solo referente e un solo preventivo, voce per voce, invece di cinque fornitori da coordinare. Grafica, impianto elettrico con dichiarazione di conformità, luci, moquette, ledwall e pratiche con l'ente fiera sono dentro lo stesso progetto.</p>
    </div>
    <ul class="pg-lista" data-rv="up">
      <li><b>Prima fiera.</b> Uno stand preallestito personalizzato o modulare da 9–16 mq, ad angolo se possibile: la soluzione con il rapporto più sano fra costo e visibilità.</li>
      <li><b>Fiere ripetute.</b> Uno stand modulare di proprietà, riconfigurato per ogni metratura e conservato nel nostro magazzino.</li>
      <li><b>Lancio o fiera chiave.</b> Uno stand su misura in legno, anche a isola o a due piani, con sala riunioni e ledwall.</li>
    </ul>'''
main_hub="\n".join([
 sezione("numeri","Danova Tech in fiera,","in numeri.","Dati reali del nostro lavoro: niente stime gonfiate.",numeri),
 sezione("come","Come lavoriamo","e quale stand scegliere.",None,come),
 sezione("servizi","Servizi per","lo stand.",None,altri(servizi,{s:lab_corto(s) for s in servizi})),
 sezione("tipi","Per tipo","e metratura.","Le misure sono indicative: lo spazio reale dipende dal padiglione e dal regolamento della fiera.",altri(tipi,{s:lab_corto(s) for s in tipi})),
 sezione("fiere","Stand per","le fiere principali.","Una pagina per ogni fiera: date, quartiere, regole di allestimento e cosa serve davvero allo stand.",altri(fiere,{s:lab_corto(s) for s in fiere})),
 sezione("citta","Allestimenti","per città e quartiere fieristico.",None,altri(citta,{s:lab_corto(s) for s in citta})+'\n    <div class="pg-altri" data-rv="up" style="margin-top:14px">'+"\n      ".join(link(s,lab_corto(s)) for s in regioni)+'</div>'),
 sezione("settori","Per settore","merceologico.",None,altri(settori,{s:lab_corto(s) for s in settori})),
 sezione("calendari","Calendari","fiere 2026–2027.",None,altri(cal,{s:lab_corto(s) for s in cal})),
 sezione("prezzi","Prezzi, idee","e sicurezza.",None,altri(prezzi,{s:lab_corto(s) for s in prezzi if os.path.isfile(s.strip('/')+'/index.html') or s=='/sicurezza-stand-fieristici/'} | {"/sicurezza-stand-fieristici/":"Sicurezza e materiali Classe 1"})),
 sezione("guide","Guide","per preparare la fiera.",None,altri(guide,{s:lab_corto(s) for s in guide})),
])
faq_hub=[
 ("Quanto costa uno stand fieristico?","Dipende da metratura, tipo di struttura, finiture, impianti e servizi. La maggior parte dei nostri clienti investe fra 10.000 e 30.000 euro per uno stand completo; per una cifra precisa ti mandiamo un preventivo gratuito voce per voce. Trovi esempi e voci di costo nella pagina <a href=\"/quanto-costa-uno-stand-fieristico/\">quanto costa uno stand fieristico</a>."),
 ("Quanti stand avete realizzato?","Oltre 300, in Italia e all'estero, soprattutto a Veronafiere, Fiera Milano e nei quartieri di Bologna, Rimini e Parma, oltre che in 11 paesi europei. Il team lavora in fiera da più di 20 anni."),
 ("Producete voi gli stand?","Il progetto e il coordinamento sono nostri. Strutture e arredi in legno li realizzano laboratori partner con cui lavoriamo da anni, il montaggio squadre partner coordinate da un unico capocantiere. Tu hai un solo referente e un solo preventivo."),
 ("Con quanto anticipo devo chiedere lo stand?","Per uno stand su misura l'ideale è partire 3–4 mesi prima della fiera; per un preallestito o un modulare bastano spesso poche settimane. Valutiamo anche richieste urgenti."),
 ("I materiali sono a norma per la fiera?","Sì: usiamo materiali certificati in Classe 1 di reazione al fuoco e l'impianto elettrico è realizzato da un elettricista abilitato, con dichiarazione di conformità. Dettagli nella pagina <a href=\"/sicurezza-stand-fieristici/\">sicurezza e materiali</a>."),
]
itemlist={"@type":"ItemList","@id":D+"/stand-fieristici/#elenco","name":"Pagine sugli stand fieristici","itemListElement":[{"@type":"ListItem","position":i+1,"url":D+s,"name":lab_corto(s) if s!="/sicurezza-stand-fieristici/" else "Sicurezza e materiali Classe 1"} for i,s in enumerate(servizi+tipi+fiere+citta+regioni+settori+cal+prezzi+guide)]}
pagina("/stand-fieristici/",
 "Stand fieristici: progetto e allestimento chiavi in mano",
 "Stand fieristici su misura, modulari e preallestiti: oltre 300 stand montati, team con 20+ anni in fiera. Fiere, città, metrature, prezzi e guide in un'unica pagina.",
 "Stand fieristici — Danova Tech","Oltre 300 stand montati: tipi, fiere, città, prezzi e guide per il tuo prossimo stand.",
 "Stand fieristici","Stand fieristici","Stand fieristici chiavi in mano:","dal progetto allo smontaggio.",
 "Oltre 300 stand montati in Italia e in 11 paesi europei, con un team che lavora in fiera da più di 20 anni. Qui trovi tutto quello che facciamo: tipi di stand, fiere, città, metrature, settori, prezzi e guide.",
 '<a href="#fiere" class="btn btn-g" data-mag><span class="lbl">Trova la tua fiera</span></a>',
 main_hub,faq_hub,{"_type":"CollectionPage","elenco":itemlist})

# ------------------------------------------------------------------ SICUREZZA
sic_main="\n".join([
 sezione("materiali","Materiali certificati","in Classe 1.",None,'''<div class="pg-testo" data-rv="up">
      <p>Ogni quartiere fieristico chiede che pareti, pedane, tessuti, moquette e arredi abbiano una reazione al fuoco certificata: in Italia la classe di riferimento è la Classe 1 (DM 26 giugno 1984), oppure la corrispondente Euroclasse della norma EN 13501-1. Noi usiamo materiali certificati in Classe 1 di reazione al fuoco e conserviamo i certificati di ogni materiale, pronti da consegnare all'ente fiera quando li chiede.</p>
      <p>Un materiale senza certificato non è un dettaglio: in fase di controllo l'ente fiera può chiederne la rimozione o bloccare l'allestimento, e a quel punto si perdono ore che durante il montaggio non ci sono. Per questo la scelta dei materiali si fa in fase di progetto, non in padiglione.</p>
    </div>'''),
 sezione("elettrico","Impianto elettrico","con dichiarazione di conformità.",None,'''<div class="pg-testo" data-rv="up">
      <p>L'impianto elettrico dello stand lo realizza un elettricista abilitato, che rilascia la dichiarazione di conformità prevista dal DM 37/2008. È il documento che l'ente fiera chiede per allacciare lo stand alla rete del quartiere: senza, lo stand resta al buio.</p>
    </div>'''),
 sezione("regolamento","Progetto sul regolamento","tecnico della fiera.",None,'''<ul class="pg-lista" data-rv="up">
      <li><b>Altezze e distanze.</b> Il progetto parte dalle altezze massime, dagli arretramenti dai confini e dalle regole sui lati aperti della tua fiera.</li>
      <li><b>Pratiche con l'ente fiera.</b> Progetto da approvare, servizi da prenotare, orari di carico e scarico: li seguiamo noi.</li>
      <li><b>Montaggio coordinato.</b> Squadre partner coordinate da un unico capocantiere, nei tempi di allestimento e smontaggio fissati dal quartiere.</li>
      <li><b>Un solo referente.</b> Sai sempre a chi chiedere un documento, dal progetto allo smontaggio.</li>
    </ul>'''),
 sezione("approfondisci","Per approfondire","",None,altri(["/guide/materiali-ignifughi-stand/","/guide/dichiarazione-di-conformita-stand/","/guide/regolamento-tecnico-fiera/","/stand-fieristici/","/quanto-costa-uno-stand-fieristico/"],{"/stand-fieristici/":"Tutte le pagine sugli stand"})),
])
faq_sic=[
 ("Cosa vuol dire Classe 1 di reazione al fuoco?","È la classificazione italiana (DM 26 giugno 1984) dei materiali che partecipano poco alla combustione. È quella che i regolamenti tecnici delle fiere italiane chiedono di solito per pareti, pedane, tessuti e arredi; in alternativa si usano le Euroclassi della norma EN 13501-1."),
 ("Mi date i certificati dei materiali per l'ente fiera?","Sì: per i materiali che usiamo nello stand conserviamo i certificati di reazione al fuoco e te li consegniamo, o li mandiamo direttamente all'ente fiera, quando servono."),
 ("Chi firma la dichiarazione di conformità dell'impianto elettrico?","Un elettricista abilitato, che realizza l'impianto dello stand e rilascia la dichiarazione prevista dal DM 37/2008."),
 ("Cosa succede se un materiale non è certificato?","L'ente fiera può chiederne la rimozione o fermare l'allestimento finché il problema non è risolto. Per evitarlo scegliamo i materiali già in fase di progetto."),
]
pagina("/sicurezza-stand-fieristici/",
 "Sicurezza stand fieristici: materiali Classe 1 e documenti",
 "Stand a norma: materiali certificati in Classe 1 di reazione al fuoco, impianto elettrico con dichiarazione di conformità, progetto sul regolamento della fiera.",
 "Sicurezza dello stand — Danova Tech","Materiali in Classe 1, impianto elettrico con dichiarazione di conformità, progetto sul regolamento della fiera.",
 "Sicurezza e materiali","Sicurezza dello stand","Sicurezza dello stand:","materiali in Classe 1 e documenti in regola.",
 "Uno stand bello che non passa i controlli dell'ente fiera non apre. Ecco cosa garantiamo su materiali, impianto elettrico e progetto, e quali documenti ricevi.",
 '<a href="#materiali" class="btn btn-g" data-mag><span class="lbl">Cosa garantiamo</span></a>',
 sic_main,faq_sic,{})
