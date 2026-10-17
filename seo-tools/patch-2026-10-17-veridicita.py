#!/usr/bin/env python3
"""17/10/2026 - Allinea i testi a come lavora davvero Danova Tech negli stand:
progetto e coordinamento interni; produzione con laboratori partner; montatori e
trasportatori partner; Fontanelle e Trumello sono magazzini; oltre 300 stand montati;
team con oltre 20 anni di esperienza. Uso: python3 seo-tools/patch-2026-10-17-veridicita.py [--scrivi]"""
import os,sys,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
R=[
# ---------- IT ----------
("li progettiamo, li produciamo nei nostri laboratori di Fontanelle (TV) e Trumello (PV) e li montiamo noi. Non li compriamo da altri fornitori per poi rivenderli, ed è per questo che i nostri preventivi sono molto competitivi, soprattutto rispetto a chi non ha una capacità produttiva propria.",
 "li progettiamo noi sul tuo marchio, li facciamo produrre da laboratori partner selezionati, con cui lavoriamo da anni, e coordiniamo noi il montaggio in fiera. Un solo referente segue progetto, produzione, trasporto e montaggio: tu non devi rincorrere fornitori diversi."),
("realizziamo oltre 100 stand all'anno e la produzione di Fontanelle (TV) è a circa due ore da Veronafiere","abbiamo già montato oltre 300 stand, e il nostro magazzino di Fontanelle (TV) è a circa due ore da Veronafiere"),
("realizziamo oltre 100 stand all'anno","abbiamo già montato oltre 300 stand"),
("La nostra produzione di Fontanelle (TV) è a circa due ore da Verona","Il nostro magazzino di Fontanelle (TV) è a circa due ore da Verona"),
("produzione degli elementi in legno nei nostri laboratori di Fontanelle (TV) e Trumello (PV)","produzione degli elementi in legno con i nostri laboratori partner"),
("li produciamo nei nostri laboratori di Fontanelle (TV) e Trumello (PV) e li consegniamo pronti","li facciamo produrre dai nostri laboratori partner e li consegniamo pronti"),
("li produciamo nei nostri laboratori:","li facciamo produrre dai nostri laboratori partner:"),
("prodotti nei nostri laboratori.","realizzati su misura con i nostri laboratori partner."),
("Produzione propria.</b> Laboratori a Fontanelle (TV) e Trumello (PV): nessun ricarico di terzi.","Laboratori partner.</b> Produzione su misura con laboratori di fiducia, coordinata da noi."),
(">Produzione propria<",">Partner collaudati<"),
("Strutture, pareti e arredi in legno li costruiamo noi, dalla A alla Z, e tutto lo stand si prova prima di partire.","Strutture, pareti e arredi in legno li realizzano i nostri laboratori partner sul nostro progetto, e noi coordiniamo ogni fase fino al montaggio."),
("trasporto con mezzi propri","trasporto con trasportatori di fiducia"),
("Trasporto stand con mezzi propri","Trasporto e logistica dello stand"),
("viaggiamo con i nostri camion, montiamo con le nostre squadre e un partner locale a Colonia","organizziamo il trasporto e coordiniamo il montaggio con squadre partner, compreso un partner locale a Colonia"),
("e le nostre squadre di montatori costruiscono lo stand direttamente in fiera","e squadre di montatori partner, coordinate da noi, costruiscono lo stand direttamente in fiera"),
("montate in fiera dalle nostre squadre.","montate in fiera da squadre coordinate da noi."),
("montate dalle nostre squadre direttamente in fiera","montate direttamente in fiera da squadre coordinate da noi"),
("Squadre di montaggio nostre, magazzino e produzione interna.","Montatori partner coordinati da noi, magazzino e laboratori di fiducia."),
("con squadre di montaggio nostre, magazzino e produzione interna di strutture e arredi in legno","con montatori partner coordinati da noi, magazzino e laboratori di fiducia per strutture e arredi in legno"),
("con squadre di montaggio nostre e produzione interna di strutture e arredi","con montatori partner coordinati da noi e laboratori di fiducia per strutture e arredi"),
("con squadre di montaggio nostre e produzione interna.","con montatori partner coordinati da noi e laboratori di fiducia."),
("Squadre di montaggio nostre, coordinate da un capocantiere","Squadre di montaggio coordinate da un unico capocantiere"),
("Oltre 25 anni di esperienza nel settore fieristico","Un team con oltre 20 anni di esperienza nel settore fieristico"),
("Oltre 25 anni di esperienza.","Un team con oltre 20 anni di esperienza."),
("Oltre 25 anni di fiere ci hanno insegnato","I nostri oltre 20 anni di fiere ci hanno insegnato"),
("Oltre 25 anni di fiere,","Oltre 20 anni di fiere,"),
("Oltre 25 anni in fiera.","Oltre 20 anni in fiera."),
("Produzione: Fontanelle (TV) · Trumello (PV)","Magazzini: Fontanelle (TV) · Trumello (PV)"),
("Danova Tech — Produzione di Fontanelle","Danova Tech — Magazzino di Fontanelle"),
("Danova Tech — Produzione e uffici di Trumello","Danova Tech — Magazzino e uffici di Trumello"),
("progetta e allestisce stand fieristici, con produzione a Fontanelle (TV) e Trumello (PV)","progetta e allestisce stand fieristici, con magazzini a Fontanelle (TV) e Trumello (PV)"),
("progettiamo, produciamo e montiamo stand","progettiamo, realizziamo e montiamo stand"),
# ---------- EN ----------
("we design them, build them in our own workshops in Fontanelle (Treviso) and Trumello (Pavia) and install them ourselves. We do not buy them from other suppliers and resell them, which is why our quotes are highly competitive, especially compared with stand builders without their own production capacity.",
 "we design them around your brand, have them built by selected partner workshops we have worked with for years, and coordinate the installation at the fair. One contact person runs design, production, transport and installation, so you never have to chase separate suppliers."),
("build more than 100 stands a year","have already built more than 300 stands"),
(">Our own production<",">Proven partners<"),
("Our own crews, warehouse and production.","Coordinated crews, warehouse and production."),
("Installation crews, warehouse and in-house production of all wood-based structures and furniture: fewer subcontractors, more control over quality and deadlines.","Partner installation crews, our warehouse and trusted workshops for all wood-based structures and furniture, coordinated by one team: one point of control over quality and deadlines."),
("Our own crews and partners build the stand","Partner crews coordinated by us build the stand"),
("with our own installation crews and in-house production of structures and furniture.","with partner installation crews coordinated by us and trusted workshops for structures and furniture."),
("and our installation crews build your stand right at the fair","and partner installation crews, coordinated by us, build your stand right at the fair"),
("Our crews build the stand on site","Partner crews coordinated by us build the stand on site"),
("Coordination between our crews and your tilers","Coordination between the installation crews and your tilers"),
("Over 25 years of experience","A team with over 20 years of experience"),
("Production: Fontanelle (TV) · Trumello (PV)","Warehouses: Fontanelle (TV) · Trumello (PV)"),
# ---------- DE ----------
("Wir planen sie, fertigen sie in unseren eigenen Werkstätten in Fontanelle (Treviso) und Trumello (Pavia) und montieren sie selbst. Wir kaufen sie nicht bei anderen Lieferanten ein, um sie weiterzuverkaufen. Deshalb sind unsere Angebote sehr wettbewerbsfähig, vor allem im Vergleich zu Messebauern ohne eigene Fertigung.",
 "Wir planen sie passend zu Ihrer Marke, lassen sie von ausgewählten Partnerwerkstätten fertigen, mit denen wir seit Jahren zusammenarbeiten, und koordinieren die Montage auf der Messe. Ein Ansprechpartner steuert Planung, Fertigung, Transport und Montage, Sie müssen keine einzelnen Lieferanten koordinieren."),
("bauen über 100 Messestände pro Jahr","haben bereits über 300 Messestände gebaut"),
(">Eigene Fertigung<",">Bewährte Partner<"),
("und unsere Montageteams bauen Ihren Stand","und von uns koordinierte Montageteams unserer Partner bauen Ihren Stand"),
("Über 25 Jahre Erfahrung","Ein Team mit über 20 Jahren Erfahrung"),
("Produktion: Fontanelle (TV) · Trumello (PV)","Lager: Fontanelle (TV) · Trumello (PV)"),
# ---------- FR ----------
("nous les concevons, les fabriquons dans nos ateliers de Fontanelle (Trévise) et Trumello (Pavie) et les montons nous-mêmes. Nous ne les achetons pas à d'autres fournisseurs pour les revendre : c'est pourquoi nos devis sont très compétitifs, surtout face aux standistes sans capacité de production.",
 "nous les concevons autour de votre marque, les faisons fabriquer par des ateliers partenaires sélectionnés avec lesquels nous travaillons depuis des années, et coordonnons le montage sur le salon. Un seul interlocuteur pilote conception, fabrication, transport et montage : vous n'avez pas à gérer plusieurs fournisseurs."),
("réalisons plus de 100 stands par an","avons déjà monté plus de 300 stands"),
(">Production propre<",">Partenaires éprouvés<"),
("et nos équipes de monteurs construisent votre stand","et des équipes de monteurs partenaires, coordonnées par nous, construisent votre stand"),
("Plus de 25 ans d'expérience","Une équipe avec plus de 20 ans d'expérience"),
("Nos équipes montent le stand sur place","Des équipes partenaires coordonnées par nous montent le stand sur place"),
("Avec nos équipes et nos partenaires,","Avec nos équipes partenaires,"),
("Nos équipes et des équipes partenaires montent","Des équipes partenaires coordonnées par nous montent"),
("Production : Fontanelle (TV) · Trumello (PV)","Entrepôts : Fontanelle (TV) · Trumello (PV)"),
# ---------- ES ----------
("los diseñamos, los fabricamos en nuestros talleres de Fontanelle (Treviso) y Trumello (Pavía) y los montamos nosotros. No los compramos a otros proveedores para revenderlos, por eso nuestros presupuestos son muy competitivos, sobre todo frente a montadores sin capacidad de producción propia.",
 "los diseñamos según tu marca, los fabrican talleres asociados seleccionados con los que trabajamos desde hace años y coordinamos el montaje en la feria. Un único interlocutor gestiona diseño, fabricación, transporte y montaje: no tienes que coordinar proveedores distintos."),
("realizamos más de 100 stands al año","ya hemos montado más de 300 stands"),
(">Producción propia<",">Socios de confianza<"),
("y nuestros equipos de montadores construyen tu stand","y equipos de montadores asociados, coordinados por nosotros, construyen tu stand"),
("Más de 25 años de experiencia","Un equipo con más de 20 años de experiencia"),
("Nuestros equipos montan el stand en la feria","Equipos asociados coordinados por nosotros montan el stand en la feria"),
("Producción: Fontanelle (TV) · Trumello (PV)","Almacenes: Fontanelle (TV) · Trumello (PV)"),
# ---------- ZH semplificato ----------
("设计、在我们位于丰塔内莱（特雷维索）和特鲁梅洛（帕维亚）的工厂生产以及现场安装，全部由我们自己完成。我们不从其他供应商采购再转卖，所以我们的报价非常有竞争力，尤其是与没有自己生产能力的搭建商相比。",
 "由我们根据您的品牌进行设计，交由合作多年的精选合作工坊生产，并由我们统筹展会现场搭建。从设计、生产、运输到搭建，全程由一位联系人负责，您无需对接多个供应商。"),
("每年搭建超过 100 个展台","已累计搭建超过 300 个展台"),
(">自主生产<",">可靠的合作伙伴<"),
("没有生产能力的搭建商要向别人采购墙板和家具，再加上自己的利润。我们不需要：同样的展台，价格更低。","我们与固定的合作工坊和搭建团队长期合作：流程熟悉、沟通顺畅，质量和工期更可控。"),
("自有搭建团队、仓库，以及所有木制结构和家具的自主生产：外包环节更少，质量和工期更可控。","由我们统筹的合作搭建团队、自有仓库，以及长期合作的木制结构和家具工坊：一个团队负责到底，质量和工期更可控。"),
("由我们的搭建团队直接在展会现场完成施工。25年以上的展会经验","由我们统筹的合作搭建团队直接在展会现场完成施工。团队拥有20年以上的展会经验"),
# ---------- ZH tradizionale ----------
("設計、生產和現場安裝全部由我們自己完成。我們不從其他供應商採購再轉賣，所以我們的報價非常有競爭力，尤其是與沒有自己生產能力的搭建商相比。",
 "由我們根據您的品牌進行設計，交由合作多年的精選合作工坊生產，並由我們統籌展會現場搭建。從設計、生產、運輸到搭建，全程由一位聯繫人負責，您無需對接多個供應商。"),
("每年搭建超過 100 個展臺","已累計搭建超過 300 個展臺"),
(">自主生產<",">可靠的合作夥伴<"),
("沒有生產能力的搭建商要向別人採購牆板和傢俱，再加上自己的利潤。我們不需要：同樣的展臺，價格更低。","我們與固定的合作工坊和搭建團隊長期合作：流程熟悉、溝通順暢，質量和工期更可控。"),
("自有搭建團隊、倉庫，以及所有木製結構和傢俱的自主生產：外包環節更少，質量和工期更可控。","由我們統籌的合作搭建團隊、自有倉庫，以及長期合作的木製結構和傢俱工坊：一個團隊負責到底，質量和工期更可控。"),
("由我們的搭建團隊直接在展會現場完成施工。25年以上的展會經驗","由我們統籌的合作搭建團隊直接在展會現場完成施工。團隊擁有20年以上的展會經驗"),
# ---------- AR / TR ----------
("فرقنا تبني الجناح في الموقع","فرق شريكة بتنسيق منا تبني الجناح في الموقع"),
("Ekiplerimiz standı fuar alanında kurar","Koordine ettiğimiz partner ekipler standı fuar alanında kurar"),
]

# ---------- secondo giro (trasporto, montatori, estero) ----------
R+=[
("Progettiamo e costruiamo lo stand in Italia, lo portiamo con i nostri mezzi ","Progettiamo lo stand, lo facciamo costruire in Italia dai nostri laboratori partner, lo spediamo con trasportatori di fiducia "),
("e lo montiamo con squadre nostre e partner locali","e coordiniamo il montaggio con squadre partner, anche locali"),
("Oltre 1.000 fiere all'estero in più di 25 anni.","Oltre 300 stand montati, da un team in fiera da più di 20 anni."),
("Oltre 1.000 fiere all'estero: progetto,","Stand per fiere all'estero: progetto,"),
("In più di 25 anni abbiamo lavorato a oltre 1.000 fiere all'estero.","Il nostro team lavora in fiera da oltre 20 anni e abbiamo già montato oltre 300 stand."),
("<dt>Fiere all'estero</dt><dd>Oltre 1.000</dd>","<dt>Stand montati</dt><dd>Oltre 300</dd>"),
("<dt>Esperienza</dt><dd>Più di 25 anni</dd>","<dt>Esperienza</dt><dd>Team con oltre 20 anni</dd>"),
("<dt>Trasporto</dt><dd>Con i nostri mezzi</dd>","<dt>Trasporto</dt><dd>Trasportatori di fiducia</dd>"),
("<dt>Montaggio</dt><dd>Squadre nostre e partner locali</dd>","<dt>Montaggio</dt><dd>Montatori partner coordinati da noi</dd>"),
("Lo progettiamo, lo costruiamo e lo proviamo in Italia, poi lo portiamo in fiera con i nostri mezzi.","Lo progettiamo noi, lo costruiscono in Italia i nostri laboratori partner e lo spediamo in fiera con trasportatori di fiducia."),
("<h3>Trasporto con i nostri mezzi</h3>\n        <p>Lo stand viaggia sui nostri camion, con i nostri imballi e gli orari di scarico prenotati. Nessun passaggio di mano tra spedizionieri.</p>",
 "<h3>Trasporto organizzato da noi</h3>\n        <p>Lo stand viaggia con trasportatori di fiducia, imballi curati e orari di scarico prenotati da noi. Un solo referente segue la spedizione dall'Italia al padiglione.</p>"),
("lo riportiamo in fiera con i nostri mezzi","lo rispediamo in fiera"),
("Squadre nostre dall'Italia, affiancate da partner locali di fiducia quando lo stand è grande o i tempi di allestimento sono stretti.","Montatori partner dall'Italia, affiancati da partner locali di fiducia quando lo stand è grande o i tempi di allestimento sono stretti. Il coordinamento resta nostro."),
("Con squadre nostre che partono dall'Italia,","Con squadre di montatori partner che partono dall'Italia,"),
("Squadre nostre che partono dall'Italia,","Squadre di montatori partner che partono dall'Italia,"),
("Squadre nostre e partner che montano lo stand","Montatori partner, coordinati da noi, che montano lo stand"),
("lavoriamo con squadre nostre e squadre esterne e valutiamo","lavoriamo con una rete di montatori partner e valutiamo"),
("cosa è possibile fare con squadre nostre e partner.","cosa è possibile fare con i nostri montatori partner."),
("Ce ne occupiamo noi, con squadre nostre e partner,","Ce ne occupiamo noi, con i nostri montatori partner,"),
("con squadre nostre e squadre esterne riusciamo","con la nostra rete di montatori partner riusciamo"),
("Lavorando con squadre nostre e squadre esterne riusciamo","Lavorando con una rete di montatori partner riusciamo"),
("<li><b>Squadre nostre e partner.</b> Possiamo coprire","<li><b>Rete di montatori partner.</b> Possiamo coprire"),
("magazzino, con squadre nostre e partner.</p>","magazzino, con trasportatori e montatori partner coordinati da noi.</p>"),
("In più di 25 anni di lavoro nel settore fieristico","In oltre 20 anni di lavoro nel settore fieristico"),
('Gli elementi in legno <span class="grad">li facciamo noi, dalla A alla Z.</span>','Gli elementi in legno <span class="grad">su misura, con laboratori partner.</span>'),
("<li><b>Produzione interna.</b> Tutti gli elementi in legno, dalla A alla Z.</li>","<li><b>Laboratori partner collaudati.</b> Tutti gli elementi in legno su misura, su nostro progetto.</li>"),
("<li><b>Squadre nostre.</b> Con partner per i picchi di lavoro, coordinati da noi.</li>","<li><b>Montaggio coordinato da noi.</b> Una rete di squadre partner, un unico referente.</li>"),
("<b>3. Le squadre di montaggio sono vostre?</b> Squadre proprie, coordinate da un capocantiere, rispondono meglio agli imprevisti dell'allestimento.","<b>3. Chi coordina le squadre di montaggio?</b> Che siano interne o partner, conta che ci sia un capocantiere unico che le coordina e risponde degli imprevisti dell'allestimento."),
("<dd>Interna: strutture e arredi in legno, dalla A alla Z</dd>","<dd>Laboratori partner: strutture e arredi in legno su nostro progetto</dd>"),
("<dd>Squadre nostre con capocantiere, partner per i picchi di lavoro</dd>","<dd>Montatori partner coordinati da un unico capocantiere</dd>"),
("Dalla produzione di Fontanelle (TV)","Dal magazzino di Fontanelle (TV)"),
("Dalla produzione e dagli uffici di Trumello (PV)","Dal magazzino e dagli uffici di Trumello (PV)"),
("tra la sede di Mansuè e la produzione di Fontanelle","tra la sede di Mansuè e il magazzino di Fontanelle"),
("Organizziamo il trasporto con i nostri mezzi o con corriere dedicato,","Organizziamo il trasporto con trasportatori di fiducia o corriere dedicato,"),
("materiali portati con i nostri mezzi,","materiali consegnati dai nostri trasportatori di fiducia,"),
("portare i materiali con i nostri mezzi","far arrivare i materiali in poche ore"),
("consegne con i nostri mezzi","consegne rapide"),
("Con i nostri mezzi o corriere, montaggio compreso se serve.","Con trasportatori di fiducia o corriere, montaggio compreso se serve."),
("Sì, con i nostri mezzi o con corriere dedicato.","Sì, con trasportatori di fiducia o con corriere dedicato."),
("<b>自有施工团队、仓库和生产。</b>","<b>统筹施工、自有仓库、合作生产。</b>"),
("<b>自有施工團隊、倉庫和生產。</b>","<b>統籌施工、自有倉庫、合作生產。</b>"),
]

# ---------- terzo giro ----------
R+=[
("<p>从图纸到成品不依赖任何外部厂家：即使是最后一刻的修改，也由我们自己完成。</p>","<p>从图纸到成品由我们统筹固定的合作工坊：即使是最后一刻的修改，也由同一个团队快速落实。</p>"),
("<p>從圖紙到成品不依賴任何外部廠家：即使是最後一刻的修改，也由我們自己完成。</p>","<p>從圖紙到成品由我們統籌固定的合作工坊：即使是最後一刻的修改，也由同一個團隊快速落實。</p>"),
('We make every wooden element <span class="grad">ourselves, from A to Z.</span>','Every wooden element, <span class="grad">made to measure by proven partners.</span>'),
('Alle Holzelemente <span class="grad">fertigen wir selbst, von A bis Z.</span>','Alle Holzelemente <span class="grad">nach Maß, von bewährten Partnern.</span>'),
('Tous les éléments en bois, <span class="grad">nous les fabriquons nous-mêmes, de A à Z.</span>','Tous les éléments en bois, <span class="grad">sur mesure, par des partenaires éprouvés.</span>'),
('Todos los elementos de madera <span class="grad">los fabricamos nosotros, de la A a la Z.</span>','Todos los elementos de madera, <span class="grad">a medida, con socios de confianza.</span>'),
("Lo stand parte dall'Italia sui nostri camion.","Lo stand parte dall'Italia con trasportatori di fiducia."),
("stand e arredi in legno prodotti da noi dalla A alla Z, progetto 3D","stand e arredi in legno su nostro progetto 3D, laboratori partner"),
("Stand fieristici su misura in legno, prodotti da noi dalla A alla Z: progetto 3D, costruzione,","Stand fieristici su misura in legno, progettati da noi e costruiti da laboratori partner: progetto 3D,"),
("Con equipos propios y colaboradores a menudo organizamos","Con nuestra red de montadores asociados a menudo organizamos"),
("With our own crews and partner crews we can often organise","With our network of partner crews we can often organise"),
("Our own crews and trusted partner crews build the stand","Trusted partner crews coordinated by us build the stand"),
("We can coordinate your tilers with our crews or organise the installation ourselves.","We can coordinate your tilers with the installation crews or organise the whole installation for you."),
("Sì, con squadre di montaggio nostre, produzione interna e partner per i picchi di lavoro, coordinati da un unico referente.","Sì, con montatori e laboratori partner coordinati da un unico referente."),
]

scrivi="--scrivi" in sys.argv
cnt=collections.Counter(); files=0
targets=[]
for dp,dn,fn in os.walk("."):
    dn[:]=[d for d in dn if d not in (".git","social",".github","assets","render-stand","__pycache__","keywords")]
    for f in fn:
        if f.endswith((".html",".txt",".py",".json")) and ".bak" not in f and "patch-2026-10-17" not in f:
            targets.append(os.path.join(dp,f))
for p in targets:
    try: h=open(p,encoding="utf-8").read()
    except: continue
    o=h
    for i,(a,b) in enumerate(R):
        # anche le varianti con apostrofo HTML-escaped
        for aa,bb in ((a,b),(a.replace("'","&#x27;"),b.replace("'","&#x27;")),(a.replace("'","&#39;"),b.replace("'","&#39;"))):
            n=h.count(aa)
            if n: cnt[i]+=n; h=h.replace(aa,bb)
    if h!=o:
        files+=1
        if scrivi: open(p,"w",encoding="utf-8").write(h)
for i,(a,b) in enumerate(R): print(f"{cnt[i]:4d}  {a[:70]}")
print("file toccati:",files,"(scritti)" if scrivi else "(prova)")
