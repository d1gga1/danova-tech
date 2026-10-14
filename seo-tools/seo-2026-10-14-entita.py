# Patch SEO 14/10/2026: entita' aziendale coerente, stand fieristici in homepage, Article sulle guide.
import os,re,json,subprocess,sys
DRY='--dry' in sys.argv
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
LD=re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)',re.S)
ORG='https://danova-tech.com/#organization'
AREA=[{"@type":"City","name":n} for n in ["Treviso","Oderzo","Pordenone","Venezia","Milano","Pavia"]]+\
     [{"@type":"AdministrativeArea","name":n} for n in ["Veneto","Friuli-Venezia Giulia","Lombardia"]]+\
     [{"@type":"Country","name":"Italia"},{"@type":"Place","name":"Europa"},{"@type":"Country","name":"United States"}]

HOME={
 'index.html':dict(
  title="Siti web, software su misura e stand fieristici | Danova Tech",
  desc="Agenzia italiana: siti web ed e-commerce, SEO e Meta Ads, gestionali e software su misura, progettazione e allestimento di stand fieristici. Risposta in 24 ore.",
  org="Agenzia tech italiana che progetta e sviluppa siti web, e-commerce, strategie SEO, campagne Meta Ads, applicazioni, gestionali e software su misura, e che progetta e allestisce stand fieristici in Italia e all'estero.",
  dis=("e cura SEO e campagne Meta Ads.","cura SEO e campagne Meta Ads e progetta e allestisce stand fieristici, con produzione a Fontanelle (TV) e Trumello (PV)."),
  hero=("Siti web, SEO, campagne Meta Ads, applicazioni, gestionali e software su misura.","Siti web, SEO, campagne Meta Ads, app, gestionali, software su misura e stand fieristici.")),
 'en/index.html':dict(
  title="Websites, custom software & exhibition stands | Danova Tech",
  desc="Italian tech agency: websites, e-commerce, apps, ERP and custom software, plus exhibition stand design and build in Italy. Fixed price, reply in 24h.",
  org="Italian tech agency that designs and builds websites, e-commerce, SEO strategies, Meta Ads campaigns, apps, ERP systems and custom software, and designs and builds exhibition stands in Italy and abroad.",
  dis=("and runs SEO and Meta Ads campaigns.","runs SEO and Meta Ads campaigns, and designs and builds trade fair exhibition stands."),
  hero=("Websites, SEO, Meta Ads campaigns, applications, management systems and custom software.","Websites, SEO, Meta Ads campaigns, apps, management systems, custom software and exhibition stands.")),
 'de/index.html':dict(
  title="Websites, Individualsoftware und Messestände | Danova Tech",
  desc="Italienische Tech-Agentur: Websites und Onlineshops, SEO, Meta Ads, Apps, Warenwirtschaft, Individualsoftware und Messestandbau in Italien. Angebot in 24 Stunden.",
  org="Italienische Tech-Agentur, die Websites, Onlineshops, SEO-Strategien, Meta-Ads-Kampagnen, Anwendungen, Warenwirtschaft und Individualsoftware entwickelt sowie Messestände in Italien und im Ausland plant und baut.",
  dis=("und betreut SEO und Meta-Ads-Kampagnen.","betreut SEO und Meta-Ads-Kampagnen und plant und baut Messestände."),
  hero=("Websites, SEO, Meta-Ads-Kampagnen, Anwendungen, Warenwirtschaft und maßgeschneiderte Software.","Websites, SEO, Meta-Ads-Kampagnen, Anwendungen, Warenwirtschaft, maßgeschneiderte Software und Messestände.")),
 'fr/index.html':dict(
  title="Sites web, logiciels sur mesure et stands | Danova Tech",
  desc="Agence tech italienne : sites web et e-commerce, référencement, Meta Ads, applications, ERP, logiciels sur mesure et stands d'exposition. Devis gratuit sous 24 h.",
  org="Agence tech italienne qui conçoit et développe des sites web, des boutiques en ligne, des stratégies SEO, des campagnes Meta Ads, des applications, des ERP et des logiciels sur mesure, et qui conçoit et construit des stands d'exposition en Italie et à l'étranger.",
  dis=("et gère le référencement et les campagnes Meta Ads.","gère le référencement et les campagnes Meta Ads, et conçoit et construit des stands d'exposition pour les salons."),
  hero=("Sites web, référencement, campagnes Meta Ads, applications, ERP et logiciels sur mesure.","Sites web, référencement, campagnes Meta Ads, applications, ERP, logiciels sur mesure et stands d'exposition.")),
 'es/index.html':dict(
  title="Diseño web, software a medida y stands feriales | Danova Tech",
  desc="Agencia tecnológica italiana: webs y e-commerce, SEO, Meta Ads, apps, ERP, software a medida y stands para ferias. Presupuesto gratuito, respuesta en 24 h.",
  org="Agencia tecnológica italiana que diseña y desarrolla webs, tiendas online, estrategias SEO, campañas de Meta Ads, aplicaciones, ERP y software a medida, y diseña y construye stands feriales en Italia y en el extranjero.",
  dis=("y gestiona SEO y campañas de Meta Ads.","gestiona SEO y campañas de Meta Ads, y diseña y construye stands feriales."),
  hero=("Webs, SEO, campañas de Meta Ads, aplicaciones, ERP y software a medida.","Webs, SEO, campañas de Meta Ads, aplicaciones, ERP, software a medida y stands feriales.")),
}
SHORT={
 'allestimenti-fieristici-emilia-romagna/index.html':("Allestimenti fieristici in Emilia-Romagna: stand chiavi in mano nei quartieri fieristici della regione.",
   "Allestimenti fieristici in Emilia-Romagna: stand chiavi in mano a Bologna, Rimini e Parma, dal progetto 3D al montaggio in fiera."),
 'stand-32-mq/index.html':("Stand fieristico di 32 mq (8×4 m): esposizione, sala incontri, magazzino e grafica, ad angolo o a penisola.",
   "Stand fieristico di 32 mq (8×4 m): esposizione, sala incontri, magazzino e grafica, ad angolo o a penisola. Progetto e montaggio chiavi in mano."),
 'stand-16-mq/index.html':("Stand fieristico di 16 mq (4×4 m): layout, zona incontri, ripostiglio, grafica e luci, ad angolo o in linea.",
   "Stand fieristico di 16 mq (4×4 m): layout, zona incontri, ripostiglio, grafica e luci, ad angolo o in linea. Progetto e montaggio chiavi in mano."),
}
GUIDES=["come-andare-in-prima-pagina-su-google","come-inserire-attivita-su-google-maps","cos-e-la-rpa","cos-e-un-crm",
        "cos-e-un-gestionale","gestionale-su-misura-o-standard","gestione-magazzino-con-excel"]

def gitdates(p):
    out=subprocess.run(['git','log','--format=%ad','--date=short','--',p],capture_output=True,text=True).stdout.split()
    return (out[-1],out[0]) if out else ('2026-10-14','2026-10-14')

def esc(s): return s.replace('&','&amp;').replace('"','&quot;')

stats={}
def bump(k): stats[k]=stats.get(k,0)+1

pages=[]
for d,ds,fs in os.walk('.'):
    ds[:]=[x for x in ds if x not in('.git','seo-tools','assets')]
    if 'index.html' in fs: pages.append(os.path.join(d,'index.html')[2:])

for p in sorted(pages):
    h0=h=open(p,encoding='utf-8').read()
    H=HOME.get(p)
    oldmeta=re.search(r'<meta name="description" content="([^"]*)"',h).group(1)
    guide=p.startswith('guide/') and p.split('/')[1] in GUIDES
    def fix(m):
        o=json.loads(m.group(2))
        graph=o.get('@graph',[])
        for n in graph:
            if n.get('@id')==ORG:
                if 'Danova Tech srl' in (n.get('alternateName') or []):
                    n['alternateName']=[a for a in n['alternateName'] if a!='Danova Tech srl']; bump('srl rimosso')
                if isinstance(n.get('areaServed'),list) and n['areaServed']!=AREA:
                    n['areaServed']=AREA; bump('areaServed')
                if H:
                    n['description']=H['org']; bump('org desc')
                    dd=n.get('disambiguatingDescription','')
                    if H['dis'][0] in dd: n['disambiguatingDescription']=dd.replace(H['dis'][0],H['dis'][1]); bump('disamb')
            if H and n.get('description')==oldmeta.replace('&amp;','&').replace('&quot;','"'):
                n['description']=H['desc']; bump('json desc=meta')
        if guide and graph and not any('Article' in str(n.get('@type')) for n in graph):
            wp=next((n for n in graph if n.get('@type')=='WebPage'),None)
            img=next((n for n in graph if n.get('@type')=='ImageObject'),None)
            u='https://danova-tech.com/'+p[:-len('index.html')]
            h1=re.sub(r'<[^>]+>','',re.search(r'<h1[^>]*>(.*?)</h1>',h,re.S).group(1))
            h1=re.sub(r'\s+',' ',h1).strip()
            pub,mod=gitdates(p)
            art={"@type":["Article","BlogPosting"],"@id":u+"#article","headline":h1[:110],
                 "description":__import__("html").unescape(oldmeta),
                 "inLanguage":"it","datePublished":pub,"dateModified":mod,"url":u,
                 "mainEntityOfPage":{"@id":(wp or {}).get('@id',u+'#webpage')},
                 "author":{"@id":ORG},"publisher":{"@id":ORG},"articleSection":"Guide"}
            if img: art["image"]={"@id":img['@id']}
            if wp:
                wp.setdefault('datePublished',pub); wp['dateModified']=mod
            graph.append(art); bump('Article aggiunto')
        return m.group(1)+'\n'+json.dumps(o,indent=2,ensure_ascii=False)+'\n'+m.group(3) if m.group(2).startswith('\n') else m.group(1)+json.dumps(o,indent=2,ensure_ascii=False)+m.group(3)
    # preserva gli spazi originali attorno al JSON
    def fix2(m):
        b=m.group(2); lead=b[:len(b)-len(b.lstrip())]; trail=b[len(b.rstrip()):]
        new=fix(type('M',(),{'group':lambda s,i:(m.group(1),b.strip(),m.group(3))[i-1]})())
        inner=new[len(m.group(1)):-len(m.group(3))]
        if json.loads(inner)==json.loads(b) : return m.group(0)
        return m.group(1)+lead+inner+trail+m.group(3)
    h=LD.sub(fix2,h)
    if H:
        h=re.sub(r'<title>[^<]*</title>','<title>'+H['title']+'</title>',h,1)
        h=h.replace('content="'+oldmeta+'"','content="'+esc(H['desc'])+'"')
        h=re.sub(r'(<meta (?:property="og:description"|name="twitter:description") content=")[^"]*"',lambda m:m.group(1)+esc(H['desc'])+'"',h)
        if H['hero'][0] in h: h=h.replace(H['hero'][0],H['hero'][1]); bump('hero')
        else: print('HERO NON TROVATO',p)
        bump('homepage')
    if p in SHORT:
        a,b=SHORT[p]; n=h.count(a); h=h.replace(a,b); bump('desc corta x%d'%n)
    if h!=h0:
        bump('file modificati')
        if not DRY: open(p,'w',encoding='utf-8').write(h)
print(stats)
