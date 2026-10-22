# Genera le liste per il Keyword Planner (22 ottobre 2026), scartando le keyword gia misurate.
# Uso: python3 seo-tools/keywords/2026-10-22/genera.py
import csv, glob, io, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
KW = os.path.dirname(BASE)

def norm(s): return re.sub(r'\s+', ' ', s.strip().lower())

# --- keyword gia misurate o gia incollate nel planner ---
gia = set()
for f in glob.glob(os.path.join(KW, 'planner-2026-10', '**', '*.csv'), recursive=True):
    t = None
    for enc in ('utf-16', 'utf-8'):
        try: t = open(f, encoding=enc).read(); break
        except Exception: pass
    if not t: continue
    parts = t.split('\n', 2)
    if len(parts) < 3: continue
    for r in csv.DictReader(io.StringIO(parts[2]), delimiter='\t'):
        k = r.get('Keyword') or ''
        if k: gia.add(norm(k))
for f in glob.glob(os.path.join(KW, '*.txt')):
    for line in open(f, encoding='utf-8', errors='ignore'):
        if line.strip(): gia.add(norm(line))

# per le lingue straniere conta solo cio che e gia stato misurato fuori dall'Italia
gia_estero = set()
for f in ['planner-DE.txt','planner-EN.txt','planner-FR.txt','planner-ES.txt','planner-USA-volumi-EN.txt','planner-USA-volumi-ES.txt','planner-USA-scoperta.txt']:
    p = os.path.join(KW, f)
    if os.path.exists(p):
        for line in open(p, encoding='utf-8', errors='ignore'):
            if line.strip(): gia_estero.add(norm(line))

def L(s): return [x for x in s.split('\n')]

# ================= ITALIA =================
it_servizio = L("""
trasporto stand fieristici
trasporto stand fiera
trasporto materiale fiera
spedizione materiale fiera
spedizioni per fiere
spedizioni fiere estero
logistica fieristica
logistica fiere
logistica per fiere
corriere per fiere
consegna materiale in fiera
ritiro materiale fiera
deposito stand
deposito stand fieristici
stoccaggio stand
stoccaggio stand fieristici
custodia stand fieristici
magazzino per stand
riutilizzo stand
stand riutilizzabile
riallestimento stand
montaggio e smontaggio stand
montaggio smontaggio stand fieristici
smontaggio stand fieristici
smontaggio stand fiera
montatori fiera
montatori fieristici
montatore fieristico
squadra montaggio stand
personale montaggio fiere
ditta montaggio stand
montaggio stand estero
montatori stand estero
installazione stand fieristici
falegnameria stand
falegnameria stand fieristici
falegnameria allestimenti fieristici
falegnameria per allestimenti
falegnameria allestimenti
costruzione stand in legno
laboratorio stand fieristici
produzione stand in legno
fabbrica stand fieristici
azienda stand fieristici
aziende stand fieristici
ditta stand fieristici
ditte stand fieristici
società allestimenti fieristici
allestitori fieristici italiani
miglior allestitore fieristico
migliori allestitori fieristici
allestitori stand fieristici
allestitore fiere
allestitore fiere estero
allestimenti fieristici chiavi in mano
allestimento stand chiavi in mano
stand chiavi in mano prezzi
servizio completo fiera
gestione completa fiera
organizzazione partecipazione fiera
project manager fiera
servizi per espositori
servizi espositori fiera
assistenza espositori
pratiche fiera espositori
documenti fiera espositori
approvazione progetto stand
allacciamento elettrico fiera
allaccio elettrico stand
appendimenti fiera
americana per stand
americane per fiere
truss per stand
piattaforma aerea fiera
carnet ata fiere
carnet ata
dogana fiere estero
pavimento sopraelevato stand
pedana per stand
pedana stand fiera
moquette per stand
moquette fiera
controsoffitto stand
ripostiglio stand
cucina per stand
bar per stand fieristico
bancone bar stand
bancone per fiere
banco reception fiera
arredi su misura per stand
arredi stand fieristici
mobili per stand
noleggio mobili fiera
vetrine per stand
vetrine espositive fiera
monitor per stand
schermi per fiere
insegna luminosa stand
lettere luminose stand
logo luminoso stand
lightbox per fiere
tessuto retroilluminato
grafica tessile stand
stampa tessuto stand
stampa pannelli fiera
vetrofanie stand
rendering stand
render stand fieristico
progetto stand 3d
progettista stand
progettista stand fieristici
architetto stand fieristici
designer stand fieristici
exhibit designer
studio progettazione stand
concept stand fieristico
stand fieristici nord italia
stand fieristici nord est
stand fieristici triveneto
allestitori fieristici nord italia
allestitori fieristici nord est
allestitori fieristici triveneto
allestitori fieristici friuli
allestitori fieristici trentino
allestitori fieristici piemonte
allestitori fieristici toscana
allestitori fieristici lazio
allestitori fieristici campania
allestitori fieristici puglia
allestitori fieristici liguria
allestitori fieristici marche
allestitori fieristici umbria
allestitori fieristici sicilia
allestitori fieristici sardegna
allestimenti fieristici friuli
allestimenti fieristici trentino
allestimenti fieristici piemonte
allestimenti fieristici toscana
allestimenti fieristici lazio
allestimenti fieristici campania
allestimenti fieristici puglia
allestimenti fieristici marche
allestimenti fieristici modena
allestimenti fieristici reggio emilia
allestimenti fieristici ferrara
allestimenti fieristici cremona
allestimenti fieristici piacenza
allestimenti fieristici trento
allestimenti fieristici montichiari
allestimenti fieristici arezzo
allestimenti fieristici ancona
allestimenti fieristici pesaro
allestimenti fieristici lucca
allestimenti fieristici como
allestimenti fieristici varese
allestimenti fieristici monza
allestimenti fieristici novara
allestimenti fieristici cuneo
allestimenti fieristici mantova
allestimenti fieristici belluno
allestimenti fieristici rovigo
allestimenti fieristici trieste
allestimenti fieristici catania
allestimenti fieristici palermo
allestimenti fieristici cagliari
stand fieristici treviso
stand fieristici venezia
stand fieristici udine
stand fieristici pordenone
stand fieristici bergamo
stand fieristici genova
stand fieristici napoli
stand fieristici bari
stand fieristici parma
stand fieristici modena
stand fieristici trento
stand fieristici bolzano
""")

it_prezzi = L("""
quanto costa uno stand di 16 mq
quanto costa uno stand di 9 mq
quanto costa uno stand di 12 mq
quanto costa uno stand di 20 mq
quanto costa uno stand di 24 mq
quanto costa uno stand di 32 mq
quanto costa uno stand di 50 mq
quanto costa uno stand di 100 mq
quanto costa uno stand a isola
quanto costa uno stand su misura
quanto costa uno stand preallestito
quanto costa uno stand modulare
quanto costa uno stand in legno
quanto costa uno stand a due piani
quanto costa montare uno stand
quanto costa il montaggio di uno stand
quanto costa allestire uno stand
quanto costa uno stand all estero
quanto costa uno stand in germania
costo stand al metro quadro
prezzo stand al mq
prezzo stand fiera al mq
costo stand fiera al mq
prezzo allestimento stand al mq
costo allestimento stand al metro quadro
costo montaggio stand
prezzo montaggio stand
costo progettazione stand
costo render stand
costo trasporto stand
costo stand estero
costo stand germania
costo area espositiva fiera
costo spazio fiera
costo spazio espositivo fiera milano
preventivo stand
preventivo stand fiera
preventivo stand fieristico online
richiesta preventivo stand
preventivo stand su misura
preventivo allestimento fieristico
listino prezzi stand fieristici
stand fieristici prezzi
stand fiera prezzi
stand su misura prezzi
stand modulari prezzi
stand preallestiti prezzi
stand in legno prezzi
stand usati
stand usati per fiere
stand fieristico usato
stand usato
vendita stand usati
stand fieristici usati vendita
stand fieristici in vendita
comprare uno stand fieristico
acquisto stand fieristico
noleggiare o comprare uno stand
stand ricondizionati
stand trasportabili per fiere
stand smontabile
stand portatile
stand fiera economico
stand low cost
stand fieristici low cost
allestimento stand economico
leasing stand fieristico
stand fiera iva
iva stand fiera estero
stand fieristico deducibile
stand fiera ammortamento
""")

it_domande = L("""
come funziona una fiera per espositori
come organizzare uno stand fieristico
cosa serve per partecipare a una fiera
cosa portare in fiera espositore
cosa mettere in uno stand
come rendere attrattivo uno stand
come allestire uno stand piccolo
come allestire uno stand di vino
come allestire uno stand alimentare
come allestire uno stand di abbigliamento
come allestire uno stand di gioielli
posizione migliore stand fiera
quando prenotare lo stand in fiera
quanto tempo per montare uno stand
orari allestimento fiera
regolamento allestimento fiera milano
regolamento tecnico veronafiere
regolamento tecnico bolognafiere
regolamento tecnico rimini fiera
altezza massima stand fiera
progetto stand fiera milano approvazione
stand a due piani autorizzazione
classe 1 reazione al fuoco stand
pannelli ignifughi stand
moquette ignifuga
assicurazione stand fiera
assicurazione fiera espositori
sicurezza montaggio stand
pos fiera allestimento
duvri fiera
ritorno investimento fiera
come misurare il roi di una fiera
invito fiera clienti
budget fiera
budget stand fieristico
come risparmiare in fiera
partecipare a una fiera all estero
come partecipare a una fiera all estero
fiere all estero per aziende italiane
fiere internazionali per pmi
contributi fiere estere 2027
bando fiere internazionali 2027
simest fiere 2027
ice fiere
ice agenzia fiere
padiglione italia fiera estero
collettiva ice fiera
camera di commercio fiere contributi
voucher internazionalizzazione fiere
regione veneto contributi fiere
regione lombardia contributi fiere
regione emilia romagna contributi fiere
regione friuli contributi fiere
""")

it_fiere_nuove = ['made expo','transpotec','fieragricola','homi','sana bologna','ipack ima','xylexpo','plast milano','bit milano','ttg rimini','mce milano','mostra convegno expocomfort','myplant','venditalia','marca bologna','fiera del levante','salone nautico genova','motor bike expo','agrilevante','tecna','milano unica','simac tanning tech','bimu','sps italia','exposanita','rimini wellness','beer and food attraction','enolitech','artigiano in fiera','expo ferroviaria','a&t torino','saie bologna','cosmofarma','euroflora','sicurezza milano','intralogistica italia','print4all','viscom italia','mipel','milano home','klimahouse','arte fiera','oroarezzo','expodental','interpoma','hotel bolzano','agriumbria','ibe rimini','tecnargilla','samoter','progetto fuoco','automotive dealer day','eurocucina','euroluce','salone del bagno','sposaitalia','dolcitalia']
it_fiere_tpl = ['stand {}','allestimento stand {}','{} espositori','{} 2027','costo stand {}']

it_settori = ['medicale','farmaceutico','automotive','nautica','packaging','tecnologia','elettronica','edilizia','ceramica','gioielli','ottica','occhiali','vino','cantine','birra','gelateria','pasticceria','caffè','olio','salumi','formaggi','macchine agricole','macchinari','macchine utensili','energia','fotovoltaico','ambiente','turismo','sport','biciclette','moto','giocattoli','editoria','arte','pet','abbigliamento','tessile','calzature','pelletteria','arredamento','illuminazione','bagno','cucine','marmo','legno','plastica','chimica','sicurezza','logistica','ferroviario','aerospaziale','dentale','benessere','fitness','ristorazione','start up','aziende','pmi','artigiani']
it_settori_tpl = ['stand fieristici {}','stand per {}','allestimento stand {}']

estere = ['anuga','prowein','ambiente francoforte','ish francoforte','bau monaco','bauma','euroshop','interpack','medica dusseldorf','agritechnica','eurotier','hannover messe','drupa','k dusseldorf','fruit logistica','itb berlino','imm cologne','light building','automechanika','intersolar','iaa mobility','boot dusseldorf','spoga gafa','interzum','ligna','biofach','spielwarenmesse','iwa norimberga','embedded world','emo hannover','electronica monaco','productronica','inhorgenta','ispo','fibo','caravan salon','gamescom','ifa berlino','achema','formnext','blechexpo','motek','heimtextil','techtextil','domotex','ifat','transport logistic','analytica','a+a dusseldorf','wire dusseldorf','glasstec','eurobike','internorga','intermot','christmasworld','fakuma','stone tec','holz handwerk','fensterbau frontale','chillventa','brau beviale',
 'sial paris','maison et objet','wine paris','vinexpo paris','batimat','equip auto','premiere vision','whos next','global industrie','eurosatory','sima parigi','sirha lione','pollutec','salon de l agriculture','jec world','vivatech','equiphotel','europain','salon du chocolat',
 'fitur','mwc barcellona','ise barcellona','alimentaria barcellona','hostelco','seafood expo barcellona','cevisama','fruit attraction','smart city expo','barcelona wine week','construmat','intergift','hispack','habitat valencia','salon gourmets',
 'metstrade','horecava','greentech amsterdam','ibc amsterdam','intertraffic','plma amsterdam','batibouw','ife londra','london book fair','dsei','farnborough','swissbau','art basel','watches and wonders','ebace','stockholm furniture fair',
 'gulfood','big 5 dubai','arab health','gitex','index dubai','adipec','saudi food show','ces las vegas','conexpo','nab show','summer fancy food show','nra show','imts','pack expo','icff','coverings','kbis','sema show','jck las vegas','canton fair','chinaplas','hong kong jewellery show','sial shanghai','prowine asia','foodex japan']
it_estere_tpl = ['stand {}','allestimento stand {}','{} 2027','{} espositori italiani','partecipare a {}']

paesi_citta = ['germania','francoforte','dusseldorf','colonia','monaco di baviera','norimberga','hannover','berlino','stoccarda','amburgo','essen','lipsia','friedrichshafen','francia','parigi','lione','spagna','madrid','barcellona','valencia','olanda','amsterdam','belgio','bruxelles','svizzera','basilea','ginevra','zurigo','austria','vienna','salisburgo','wels','inghilterra','londra','birmingham','polonia','varsavia','poznan','praga','brno','svezia','stoccolma','danimarca','portogallo','lisbona','grecia','croazia','slovenia','romania','turchia','istanbul','dubai','emirati arabi','arabia saudita','riyadh','stati uniti','usa','las vegas','new york','chicago','cina','shanghai','hong kong','giappone','europa','estero']
it_paesi_tpl = ['allestimento stand {}','stand fieristici {}','allestitori fieristici {}','fiere {} 2027','stand fiera {}','montaggio stand {}','trasporto stand {}']

# ================= TEDESCO =================
de_generico = L("""
messebau
messebauer
messebaufirma
messebau firma
messebau unternehmen
messebau agentur
messebau full service
messebau komplettservice
messestand
messestände
messestand bauen lassen
messestand kaufen
messestand mieten
messestand leihen
messestand kosten
was kostet ein messestand
messestand preis
messestand preise
messestand kosten pro qm
messestand kosten pro quadratmeter
messebau kosten
messebau preise
messestand holz
messestand aus holz
individueller messestand
messestand individuell
messestand nach maß
systemmessestand
systemstand
modularer messestand
messestand modular
messestand design
messestanddesign
messestand gestaltung
messestand planung
messeplanung
messestand 3d
messestand entwurf
messestand aufbau
messestand abbau
messestand auf und abbau
messe aufbau service
messemontage
messemonteur
messebau montage
messebau monteure
messebau logistik
messelogistik
messestand transport
messestand einlagerung
messestand lagerung
messestand schlüsselfertig
messebau günstig
günstiger messestand
messestand günstig
messestand nachhaltig
nachhaltiger messebau
messestand wiederverwendbar
inselstand
inselstand messe
kopfstand messe
eckstand messe
reihenstand messe
doppelstöckiger messestand
zweigeschossiger messestand
messestand 20 qm
messestand 30 qm
messestand 50 qm
messestand 100 qm
messestand 9 qm
messestand 12 qm
messestand 16 qm
kleiner messestand
messestand ideen
messestand beispiele
kreative messestände
messestand grafik
messegrafik
messestand beleuchtung
led wand messe mieten
messemöbel mieten
messetheke
messe counter
messebau italien
italienischer messebauer
messebauer italien
messebau europa
messebau international
messebau ausland
messe im ausland
messeauftritt ausland
auslandsmesse
messebau österreich
messebau schweiz
messebau südtirol
messebau deutschland
messebau in der nähe
messen in italien
messen italien 2027
messekalender italien
messekalender italien 2027
ausstellen in italien
messeauftritt italien
""")
de_citta_it = ['mailand','milano','verona','bologna','rimini','florenz','parma','vicenza','padua','pordenone','riva del garda','rom','turin','genua','bozen','neapel','bari','carrara','italien','norditalien']
de_citta_dach = ['frankfurt','düsseldorf','köln','münchen','nürnberg','hannover','berlin','stuttgart','hamburg','essen','leipzig','friedrichshafen','karlsruhe','dortmund','augsburg','bremen','freiburg','wien','salzburg','wels','graz','innsbruck','dornbirn','linz','klagenfurt','basel','zürich','bern','genf','luzern','st. gallen','lausanne']
de_tpl_citta = ['messebau {}','messestand {}','messebauer {}','messebau firma {}']
fiere_italia_int = ['salone del mobile','vinitaly','eicma','cosmoprof','host milano','marmomac','cersaie','mido','micam','pitti uomo','sigep','tuttofood','cibus','macfrut','ecomondo','key energy','eima','mecspe','lamiera','lineapelle','vicenzaoro','expo riva schuh','emo milano','zoomark','sicam','samuexpo','fieracavalli','made expo','homi','milano unica','transpotec','fieragricola','interpoma','klimahouse','sps italia','ipack ima','xylexpo','plast','tecna','euroluce','eurocucina']
de_tpl_fiere = ['messestand {}','messebau {}','{} aussteller','{} 2027']
fiere_de = ['anuga','prowein','ambiente','ish','bau','bauma','euroshop','interpack','medica','agritechnica','eurotier','hannover messe','drupa','k messe','fruit logistica','itb','imm cologne','light building','automechanika','intersolar','iaa','boot','spoga gafa','interzum','ligna','biofach','spielwarenmesse','iwa','embedded world','electronica','productronica','inhorgenta','ispo','fibo','caravan salon','gamescom','ifa','achema','formnext','blechexpo','motek','amb','heimtextil','techtextil','domotex','didacta','ifat','transport logistic','analytica','a+a','wire','glasstec','eurobike','internorga','intermot','christmasworld','chillventa','fensterbau frontale','holz handwerk','stone tec','brau beviale','fakuma','dmea','swissbau','art basel','bauen energie']
de_tpl_fiere_de = ['messestand {}','messebau {}']

# ================= INGLESE =================
en_generico = L("""
exhibition stand builder
exhibition stand builders
exhibition stand contractor
exhibition stand contractors
exhibition stand company
exhibition stand companies
exhibition stand design
exhibition stand designers
exhibition stand design and build
custom exhibition stands
bespoke exhibition stands
modular exhibition stands
wooden exhibition stand
timber exhibition stand
sustainable exhibition stands
reusable exhibition stand
eco friendly exhibition stand
double decker exhibition stand
two storey exhibition stand
island exhibition stand
island stand
corner stand exhibition
peninsula stand
space only stand
shell scheme upgrade
exhibition stand cost
how much does an exhibition stand cost
exhibition stand price
exhibition stand prices
exhibition stand cost per square metre
exhibition stand hire
exhibition stand rental
exhibition stand installation
exhibition stand build and dismantle
stand build and dismantle
exhibition stand storage
exhibition logistics
exhibition logistics europe
trade show logistics europe
exhibition stand transport
turnkey exhibition stand
full service exhibition stand
exhibition stand graphics
exhibition stand lighting
exhibition stand furniture hire
exhibition stand ideas
exhibition stand examples
small exhibition stand
small exhibition stand ideas
3x3 exhibition stand
6x3 exhibition stand
trade show booth builder
trade show booth builders
trade show booth design
custom trade show booth
custom trade show booths
trade show booth europe
european trade show booth builder
trade show booth builder europe
trade show booth rental europe
trade show booth cost europe
exhibiting in europe
exhibiting in italy
exhibiting at a trade show in italy
exhibiting at trade fairs in germany
trade shows in italy
trade shows in italy 2027
trade fairs in italy
trade fairs in italy 2027
italy trade fair calendar
trade fairs in europe 2027
european trade show calendar 2027
trade shows in germany 2027
stand builder europe
exhibition stand builder europe
european exhibition stand builder
italian exhibition stand builder
italian stand builder
stand builder italy
stand builders italy
exhibition stand contractor italy
exhibition company italy
booth builder italy
trade show booth italy
""")
en_citta = ['italy','milan','verona','bologna','rimini','florence','parma','vicenza','padua','rome','turin','genoa','riva del garda','pordenone','germany','frankfurt','dusseldorf','cologne','munich','nuremberg','hannover','berlin','essen','stuttgart','hamburg','paris','lyon','france','barcelona','madrid','valencia','spain','amsterdam','netherlands','brussels','vienna','austria','basel','geneva','zurich','switzerland','lisbon','warsaw','prague','dubai','europe']
en_tpl_citta = ['exhibition stand builder {}','exhibition stand {}','stand builder {}','exhibition stand contractor {}','trade show booth {}','booth builder {}']
en_tpl_fiere = ['{} stand builder','{} exhibition stand','{} booth','{} stand','{} exhibitors','{} 2027']
fiere_en_estere = ['anuga','prowein','ambiente frankfurt','ish frankfurt','bau munich','bauma','euroshop','interpack','medica','agritechnica','hannover messe','drupa','fruit logistica','itb berlin','imm cologne','light building','automechanika frankfurt','intersolar','iaa','boot dusseldorf','interzum','ligna','biofach','spielwarenmesse','embedded world','electronica munich','ispo','achema','formnext','heimtextil','sial paris','maison et objet','wine paris','batimat','equip auto','eurosatory','sima paris','sirha','fitur','mwc barcelona','ise barcelona','alimentaria','hostelco','seafood expo global','cevisama','fruit attraction','metstrade','horecava','greentech amsterdam','ibc amsterdam','intertraffic','plma amsterdam','gulfood','arab health','big 5','gitex']

# ================= FRANCESE =================
fr_generico = L("""
standiste
standistes
standiste salon
standiste salon professionnel
standiste italie
standiste italien
standiste europe
standiste international
standiste allemagne
standiste espagne
standiste etranger
conception stand
conception de stand
conception stand salon
conception et réalisation de stand
création stand salon
stand sur mesure
stand salon sur mesure
stand sur mesure prix
stand modulable
stand modulaire
stand modulaire salon
stand bois
stand en bois salon
stand éco conçu
stand écoresponsable
stand réutilisable
prix stand salon
prix d un stand
combien coûte un stand
combien coûte un stand de salon
prix stand au m2
prix stand salon m2
coût stand salon
budget stand salon
location stand salon
location de stand
montage stand
montage stand salon
monteur stand
monteur de stand
installateur stand
démontage stand
montage démontage stand
stand clé en main
stand salon clé en main
stand à étage
stand 2 étages
stand îlot
stand en îlot
stand angle
aménagement stand
agencement stand
agencement de stand salon
mobilier stand location
graphisme stand
éclairage stand
transport stand salon
stockage stand
logistique salon
exposer à l étranger
exposer en italie
exposer à un salon en italie
salons en italie
salons professionnels italie
salons professionnels italie 2027
calendrier salons italie
salons allemagne 2027
""")
fr_citta = ['milan','vérone','bologne','rimini','florence','parme','vicence','padoue','italie','francfort','düsseldorf','cologne','munich','nuremberg','hanovre','berlin','barcelone','madrid','amsterdam','bruxelles','genève','bâle','vienne','dubaï','paris','lyon']
fr_tpl_citta = ['standiste {}','stand salon {}','montage stand {}']
fiere_fr = ['salone del mobile','salon du meuble de milan','vinitaly','eicma','cosmoprof','host milano','marmomac','cersaie','mido','micam','pitti uomo','sigep','tuttofood','cibus','macfrut','ecomondo','anuga','prowein','ambiente','bauma','medica','interpack','fitur','alimentaria','mwc','sial','maison et objet','wine paris','batimat','equip auto','sima','sirha','gulfood']
fr_tpl_fiere = ['stand {}','standiste {}','exposer au {}','{} 2027']

# ================= SPAGNOLO =================
es_generico = L("""
empresa de stands
empresas de stands
montaje de stands
montaje stands
montaje de stands feriales
montaje stands feriales
montadores de stands
diseño de stands
diseño de stands feriales
diseño stand feria
stands a medida
stand a medida
stands feriales a medida
stands modulares
stand modular
stands de madera
stand de madera
stands sostenibles
stand reutilizable
cuanto cuesta un stand
cuanto cuesta un stand en una feria
precio stand feria
precio de un stand
precio stand por m2
precio stand por metro cuadrado
coste stand feria
presupuesto stand feria
alquiler de stands
alquiler stand feria
construcción de stands
fabricación de stands
fabricante de stands
stand llave en mano
stands llave en mano
stand de dos pisos
stand dos plantas
stand isla
stand esquina
stand pequeño
stand 3x3
transporte stand feria
almacenaje stand
logística ferias
exponer en italia
exponer en una feria en italia
exponer en ferias internacionales
ferias en italia
ferias en italia 2027
ferias internacionales 2027
ferias en alemania 2027
calendario ferias italia
calendario ferias europa 2027
""")
es_citta = ['italia','milán','milan','verona','bolonia','rímini','florencia','parma','vicenza','padua','alemania','fráncfort','frankfurt','düsseldorf','colonia','múnich','núremberg','hannover','berlín','parís','francia','europa','ámsterdam','dubái']
es_tpl_citta = ['montaje stands {}','stand feria {}','empresa de stands {}','stands feriales {}']
fiere_es = ['salone del mobile','vinitaly','eicma','cosmoprof','host milano','marmomac','cersaie','mido','micam','pitti uomo','sigep','tuttofood','cibus','macfrut','ecomondo','anuga','prowein','ambiente','bauma','medica','interpack','fruit logistica','sial paris','maison et objet','wine paris','gulfood']
es_tpl_fiere = ['stand {}','stand en {}','{} 2027','exponer en {}']

# ================= ALTRE LINGUE =================
altre = {
'NL — Paesi Bassi e Belgio, lingua olandese': L("""
standbouw
standbouwer
standbouw italië
standbouwer italië
standbouw milaan
standbouw verona
standbouw bologna
standbouw duitsland
standbouwer duitsland
standbouw europa
beursstand
beursstand italië
beursstand milaan
beursstand laten maken
beursstand op maat
beursstand kosten
wat kost een beursstand
beursstand huren
beursstand hout
duurzame beursstand
standbouw salone del mobile
beursstand vinitaly
beursstand eicma
beursstand marmomac
beursstand anuga
beursstand prowein
beurzen italië 2027
"""),
'PT — Brasile e Portogallo, lingua portoghese': L("""
montagem de stands
montadora de stands
empresa de stands
stand para feira
stand feira itália
stand feira milão
montagem de stands itália
montadora de stands itália
montadora de stands europa
stand marmomac
stand vinitaly
stand micam
stand salone del mobile
stand cersaie
stand eicma
stand anuga
stand prowein
stand sial paris
stand fruit logistica
quanto custa um stand
preço stand feira
stand sob medida
stand de madeira
feiras na itália 2027
feiras internacionais 2027
expor em feira na itália
"""),
'PL — Polonia, lingua polacca': L("""
zabudowa targowa
zabudowa stoisk targowych
zabudowa targowa włochy
stoisko targowe
stoisko targowe włochy
stoisko targowe mediolan
stoisko targowe niemcy
zabudowa targowa niemcy
zabudowa targowa europa
stoisko marmomac
stoisko salone del mobile
stoisko vinitaly
stoisko eicma
stoisko anuga
ile kosztuje stoisko targowe
stoisko targowe cena
targi we włoszech 2027
"""),
'ZH-HANT — Hong Kong, Taiwan, Singapore, cinese tradizionale': L("""
意大利展台搭建
米蘭展台搭建
意大利展會
意大利展覽 2027
米蘭家具展 展台
米蘭展會 展台設計
維羅納展會 展台
博洛尼亞展會 展台
歐洲展台搭建
德國展台搭建
展台設計 搭建
特裝展台
展台搭建公司
"""),
}

def espandi(lista, tpl): return [t.format(x) for x in lista for t in tpl]

def pulisci(lista, base=None):
    base = gia if base is None else base
    out, seen = [], set()
    for k in lista:
        k = norm(k)
        if not k or k in seen or k in base: continue
        seen.add(k); out.append(k)
    return out

it_italia = pulisci(it_servizio + it_prezzi + it_domande + espandi(it_fiere_nuove, it_fiere_tpl) + espandi(it_settori, it_settori_tpl))
it_estero = pulisci(espandi(estere, it_estere_tpl) + espandi(paesi_citta, it_paesi_tpl))
de = pulisci(de_generico + espandi(de_citta_it, de_tpl_citta) + espandi(fiere_italia_int, de_tpl_fiere) + espandi(de_citta_dach, de_tpl_citta[:2]) + espandi(fiere_de, de_tpl_fiere_de), gia_estero)
en = pulisci(en_generico + espandi(en_citta, en_tpl_citta) + espandi(fiere_italia_int, en_tpl_fiere) + espandi(fiere_en_estere, en_tpl_fiere[:4]), gia_estero)
fr = pulisci(fr_generico + espandi(fr_citta, fr_tpl_citta) + espandi(fiere_fr, fr_tpl_fiere), gia_estero)
es = pulisci(es_generico + espandi(es_citta, es_tpl_citta) + espandi(fiere_es, es_tpl_fiere), gia_estero)

def scrivi(nome, lista, n=1000):
    files = []
    parti = (len(lista) + n - 1) // n
    for i in range(parti):
        suf = '' if parti == 1 else f'-parte{i+1}'
        p = os.path.join(BASE, nome + suf + '.txt')
        chunk = lista[i*n:(i+1)*n]
        open(p, 'w', encoding='utf-8').write('\n'.join(chunk) + '\n')
        files.append((os.path.basename(p), len(chunk)))
    return files

riepilogo = []
riepilogo += scrivi('B1-volumi-IT-italia', it_italia)
riepilogo += scrivi('B2-volumi-IT-fiere-estero', it_estero)
riepilogo += scrivi('B3-volumi-DE-tedesco', de)
riepilogo += scrivi('B4-volumi-EN-inglese', en)
riepilogo += scrivi('B5-volumi-FR-francese', fr)
riepilogo += scrivi('B6-volumi-ES-spagnolo', es)
for i, (lab, lst) in enumerate(altre.items(), start=1):
    nome = 'B7-volumi-' + lab.split(' ')[0]
    riepilogo += scrivi(nome, pulisci(lst, gia_estero))
print('keyword gia misurate escluse dal confronto:', len(gia))
for f, n in riepilogo: print(f, n)
