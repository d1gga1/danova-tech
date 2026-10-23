# -*- coding: utf-8 -*-
# 23/10/2026 - 19 video in piu' da Desktop/video_marketing (reel01-09 e reel15-24), compressi in assets/video/.
# Eseguito dentro pagine-dati-2026-10-23.py (usa V, MD, AI, VIDEO). Link ai post verificati sui profili il 23/10/2026.
def _v(slug, data, dur, tipo, it, en, de, fr, es, kw, ig=None, tt=None):
    VIDEO[slug] = V(data, dur, tipo, {'it': it[0], 'en': en[0], 'de': de[0], 'fr': fr[0], 'es': es[0]},
                    {'it': it[1], 'en': en[1], 'de': de[1], 'fr': fr[1], 'es': es[1]}, kw)
    if ig: VIDEO[slug]['ig'] = 'https://www.instagram.com/reel/%s/' % ig
    if tt: VIDEO[slug]['tt'] = 'https://www.tiktok.com/@danova.tech/video/%s' % tt
SPOT = {'it': 'Spot · riprese e motion design', 'en': 'Spot · footage & motion design', 'de': 'Spot · Footage & Motion Design', 'fr': 'Spot · images réelles et motion design', 'es': 'Spot · imágenes reales y motion design'}

_v('spot-stand-chiavi-in-mano', '2026-10-22', 43.5, SPOT,
   ('Spot: stand fieristico chiavi in mano', 'Spot di 43 secondi su riprese vere di fiere e laboratori, con transizioni 3D continue: progetto, produzione, trasporto, montaggio e smontaggio dello stand.'),
   ('Spot: turnkey exhibition stand', '43-second spot on real trade-fair and workshop footage with continuous 3D transitions: design, production, transport, build and dismantling.'),
   ('Spot: Messestand schlüsselfertig', '43-Sekunden-Spot mit echten Messe- und Werkstattaufnahmen und durchgehenden 3D-Übergängen: Planung, Produktion, Transport, Auf- und Abbau.'),
   ('Spot : stand de salon clé en main', 'Spot de 43 secondes sur images réelles de salons et d’ateliers, transitions 3D continues : conception, fabrication, transport, montage et démontage.'),
   ('Spot: stand ferial llave en mano', 'Spot de 43 segundos con imágenes reales de ferias y talleres y transiciones 3D continuas: diseño, producción, transporte, montaje y desmontaje.'),
   'spot stand fieristico, video aziendale con riprese')
_v('reel-ufficio-ordini-0-dipendenti', '2026-10-18', 43.9, MD,
   ('Un intero ufficio ordini con 0 dipendenti', 'Esempio dimostrativo in motion design: l’ordine arriva da mail, WhatsApp o sito, l’AI lo inserisce nel gestionale, controlla il magazzino e manda conferma e fattura.'),
   ('A whole order desk with zero staff', 'Motion-design demo: orders from email, WhatsApp or website are read by AI, entered in the management software, checked against stock and confirmed with an invoice.'),
   ('Eine ganze Auftragsannahme ohne Personal', 'Motion-Design-Demo: Bestellungen per E-Mail, WhatsApp oder Website liest die KI, trägt sie ein, prüft das Lager und schickt Bestätigung und Rechnung.'),
   ('Un service commandes entier sans salarié', 'Démo en motion design : la commande arrive par e-mail, WhatsApp ou site, l’IA la saisit, vérifie le stock et envoie confirmation et facture.'),
   ('Un departamento de pedidos sin empleados', 'Demo en motion design: el pedido llega por email, WhatsApp o web, la IA lo registra, revisa el almacén y envía confirmación y factura.'),
   'video automazione gestionale, AI ordini', 'Deq7u0oxko9', '7698307506623319328')
_v('reel-sito-con-ai-in-1-minuto', '2026-10-18', 38.7, MD,
   ('Un sito fatto con l’AI in 1 minuto: e i clienti?', 'Reel esplicativo: un sito per una trattoria creato dall’AI in pochi secondi, e le 4 cose che gli mancano per portare clienti (Google, modulo, tracciamento, privacy).'),
   ('A website built by AI in 1 minute: and the customers?', 'Explainer reel: a restaurant website made by AI in seconds, and the 4 things it lacks to bring in customers (Google, form, tracking, privacy).'),
   ('Website von der KI in 1 Minute: und die Kunden?', 'Erklär-Reel: eine Restaurant-Website von der KI in Sekunden, und die 4 Dinge, die für Kunden fehlen (Google, Formular, Tracking, Datenschutz).'),
   ('Un site fait par l’IA en 1 minute : et les clients ?', 'Reel explicatif : un site de restaurant créé par l’IA en quelques secondes, et les 4 choses qui manquent pour attirer des clients.'),
   ('Una web hecha con IA en 1 minuto: ¿y los clientes?', 'Reel explicativo: la web de un restaurante creada por IA en segundos y las 4 cosas que le faltan para traer clientes.'),
   'video sito web AI, reel educativo', 'DewHjtdRBeT', '7699054855847054625')
_v('reel-sfida-sito-dentista', '2026-10-18', 34.6, MD,
   ('Sfida: un sito per un dentista in 30 minuti', 'Sfida a tempo con l’AI: bozza di sito per uno studio dentistico in 1 minuto e 55 secondi, con prenotazione e versione mobile, e cosa serve dopo perché porti pazienti.'),
   ('Challenge: a dental clinic website in 30 minutes', 'Timed AI challenge: a dental website draft in 1 min 55 s with booking and mobile version, and what it still needs to bring in patients.'),
   ('Challenge: Zahnarzt-Website in 30 Minuten', 'KI-Challenge auf Zeit: Website-Entwurf für eine Zahnarztpraxis in 1:55 Minuten, mit Buchung und Mobilversion, und was danach noch fehlt.'),
   ('Défi : un site de dentiste en 30 minutes', 'Défi chronométré avec l’IA : maquette de site pour un cabinet dentaire en 1 min 55, avec réservation et version mobile.'),
   ('Reto: una web para un dentista en 30 minutos', 'Reto cronometrado con IA: borrador de web para una clínica dental en 1 min 55 s, con reservas y versión móvil.'),
   'reel sfida, sito per dentisti')
_v('reel-ferrari-pizzeria', '2026-10-18', 33.0, MD,
   ('E se Ferrari facesse il sito di una pizzeria?', 'Reel creativo: il sito di una pizzeria nel linguaggio di un brand automobilistico (rosso corsa, carbonio, menù a griglia di partenza), per mostrare che ogni marchio ha il suo stile.'),
   ('What if a supercar brand built a pizzeria website?', 'Creative reel: a pizzeria website in a racing-car brand’s language (racing red, carbon, starting-grid menu) to show every brand has its own style.'),
   ('Und wenn eine Sportwagenmarke eine Pizzeria-Website baut?', 'Kreatives Reel: Pizzeria-Website in der Sprache einer Rennmarke (Rennrot, Carbon, Startaufstellungs-Menü): jede Marke hat ihren Stil.'),
   ('Et si une marque de sportives faisait le site d’une pizzeria ?', 'Reel créatif : un site de pizzeria dans le langage d’une marque de course (rouge, carbone, menu en grille de départ).'),
   ('¿Y si una marca de deportivos hiciera la web de una pizzería?', 'Reel creativo: la web de una pizzería con el lenguaje de una marca de carreras (rojo, carbono, menú en parrilla de salida).'),
   'reel creativo, sito ristorante')
_v('reel-micro-animazioni-sito', '2026-10-18', 25.3, MD,
   ('Il tuo sito è piatto? Le micro-animazioni', 'Reel in stile chiaro sulle tendenze del web 2026: micro-animazioni, pulsanti e schede che reagiscono, e perché rendono un sito più convincente.'),
   ('Is your website flat? Micro-animations', 'Light-style reel on 2026 web trends: micro-animations, reactive buttons and cards, and why they make a site more convincing.'),
   ('Ist Ihre Website flach? Micro-Animationen', 'Reel im hellen Stil zu Webtrends 2026: Micro-Animationen und reagierende Buttons, und warum sie überzeugen.'),
   ('Votre site est plat ? Les micro-animations', 'Reel au style clair sur les tendances web 2026 : micro-animations, boutons et cartes réactifs.'),
   ('¿Tu web es plana? Las microanimaciones', 'Reel de estilo claro sobre tendencias web 2026: microanimaciones, botones y tarjetas que reaccionan.'),
   'reel web design, micro-animazioni')
_v('reel-siti-web-11500-dollari', '2026-10-18', 36.5, MD,
   ('Da zero a 11.500 dollari in 60 giorni con i siti', 'Storia vera raccontata in reel: un designer riparte con un’identità nuova e in 60 giorni guadagna 11.500 dollari con template, clienti e affiliazioni.'),
   ('From zero to $11,500 in 60 days with websites', 'True story as a reel: a designer restarts with a new identity and earns $11,500 in 60 days from templates, clients and affiliates.'),
   ('Von null auf 11.500 Dollar in 60 Tagen mit Websites', 'Wahre Geschichte als Reel: ein Designer startet neu und verdient in 60 Tagen 11.500 Dollar mit Templates, Kunden und Affiliates.'),
   ('De zéro à 11 500 dollars en 60 jours avec des sites', 'Histoire vraie en reel : un designer repart de zéro et gagne 11 500 dollars en 60 jours.'),
   ('De cero a 11.500 dólares en 60 días con webs', 'Historia real en reel: un diseñador empieza de cero y gana 11.500 dólares en 60 días.'),
   'reel storytelling, notizia web design', 'DepPiNtxcCA', '7698058285278072096')
_v('reel-ai-clona-office', '2026-10-18', 36.8, MD,
   ('Ha clonato Word, Excel e PowerPoint con l’AI', 'Notizia tech in formato reel: uno sviluppatore ricrea la suite da ufficio con l’intelligenza artificiale e la regala, open source.'),
   ('He cloned Word, Excel and PowerPoint with AI', 'Tech news as a reel: a developer rebuilds the office suite with AI and gives it away as open source.'),
   ('Word, Excel und PowerPoint mit KI nachgebaut', 'Tech-News als Reel: ein Entwickler baut die Office-Suite mit KI nach und verschenkt sie als Open Source.'),
   ('Il a cloné Word, Excel et PowerPoint avec l’IA', 'Actu tech en reel : un développeur recrée la suite bureautique avec l’IA et l’offre en open source.'),
   ('Clonó Word, Excel y PowerPoint con IA', 'Noticia tech en reel: un desarrollador recrea la suite ofimática con IA y la regala en código abierto.'),
   'reel notizia AI', 'DeoThVWx_h6', '7697928779104062752')
_v('reel-ai-di-notte', '2026-10-18', 40.2, MD,
   ('Cosa ha fatto l’AI mentre dormivo?', 'Reel dimostrativo: il “report della notte” di un assistente AI aziendale, con contatti a cui ha risposto e appuntamenti messi in agenda.'),
   ('What did the AI do while I slept?', 'Demo reel: the overnight report of a business AI assistant, with leads answered and appointments booked.'),
   ('Was hat die KI gemacht, während ich schlief?', 'Demo-Reel: der Nachtbericht eines KI-Assistenten mit beantworteten Anfragen und gebuchten Terminen.'),
   ('Qu’a fait l’IA pendant que je dormais ?', 'Reel de démo : le rapport de nuit d’un assistant IA, avec prospects traités et rendez-vous pris.'),
   ('¿Qué hizo la IA mientras dormía?', 'Reel demo: el informe nocturno de un asistente IA, con contactos respondidos y citas agendadas.'),
   'reel automazione AI, assistente AI')
_v('reel-agenti-ai-anthropic', '2026-10-18', 27.4, MD,
   ('Gli agenti AI lavorano 6 volte le ore delle persone', 'Notizia dal report di Anthropic sul lavoro interno (16 ottobre 2026), raccontata con grafici animati in 27 secondi.'),
   ('AI agents work 6× the hours of people', 'News from Anthropic’s internal work report (16 Oct 2026), told with animated charts in 27 seconds.'),
   ('KI-Agenten arbeiten 6-mal so viele Stunden', 'News aus Anthropics Bericht (16.10.2026), mit animierten Diagrammen in 27 Sekunden.'),
   ('Les agents IA travaillent 6 fois plus d’heures', 'Actu du rapport d’Anthropic (16/10/2026), en graphiques animés en 27 secondes.'),
   ('Los agentes IA trabajan 6 veces más horas', 'Noticia del informe de Anthropic (16/10/2026), con gráficos animados en 27 segundos.'),
   'reel notizia AI, grafici animati')
_v('reel-anthropic-junior', '2026-10-20', 25.6, MD,
   ('Dal 27% al 9%: meno junior nelle assunzioni', 'Reel editoriale senza voce, con schede e grafici animati sui dati pubblicati da Anthropic sulle nuove assunzioni tecniche.'),
   ('From 27% to 9%: fewer junior hires', 'Editorial reel without voice-over, with animated cards and charts on Anthropic’s published hiring data.'),
   ('Von 27 % auf 9 %: weniger Junior-Einstellungen', 'Redaktionelles Reel ohne Sprecher mit animierten Karten und Diagrammen zu Anthropics Daten.'),
   ('De 27 % à 9 % : moins de juniors recrutés', 'Reel éditorial sans voix, cartes et graphiques animés sur les données publiées par Anthropic.'),
   ('Del 27 % al 9 %: menos juniors contratados', 'Reel editorial sin voz, con tarjetas y gráficos animados sobre los datos de Anthropic.'),
   'reel editoriale, infografica animata')
_v('reel-accenture-claude', '2026-10-21', 28.0, MD,
   ('Da 1.000 a 29 dollari: il tetto di Accenture all’AI', 'Notizia in motion design 3D con iPhone ricostruito e tunnel di 5.000 badge: un colosso della consulenza limita la spesa in AI per dipendente.'),
   ('From $1,000 to $29: Accenture caps its AI', 'News in 3D motion design with a rebuilt iPhone and a tunnel of 5,000 badges: a consulting giant caps AI spend per employee.'),
   ('Von 1.000 auf 29 Dollar: Accentures KI-Deckel', 'News in 3D-Motion-Design: ein Beratungsriese begrenzt die KI-Ausgaben pro Mitarbeiter.'),
   ('De 1 000 à 29 dollars : le plafond IA d’Accenture', 'Actu en motion design 3D : un géant du conseil plafonne la dépense IA par salarié.'),
   ('De 1.000 a 29 dólares: el tope de Accenture a la IA', 'Noticia en motion design 3D: un gigante de la consultoría limita el gasto en IA por empleado.'),
   'reel notizia, motion design 3D')
_v('reel-tv-senza-pubblicita', '2026-10-21', 31.5, MD,
   ('Ha tolto la pubblicità dalla TV con l’AI', 'Piano sequenza 3D in un salotto realistico: uno sviluppatore usa un assistente AI per ripulire la smart TV dei genitori da pubblicità e app inutili.'),
   ('He removed the ads from his parents’ TV with AI', 'One-take 3D in a realistic living room: a developer uses an AI assistant to clean ads and junk apps off a smart TV.'),
   ('Mit KI die Werbung vom Fernseher entfernt', 'Plansequenz in 3D im realistischen Wohnzimmer: ein Entwickler befreit den Smart-TV mit KI von Werbung.'),
   ('Il a supprimé la pub de la TV avec l’IA', 'Plan-séquence 3D dans un salon réaliste : un développeur nettoie la smart TV de ses parents avec l’IA.'),
   ('Quitó la publicidad de la tele con IA', 'Plano secuencia 3D en un salón realista: un desarrollador limpia la smart TV de sus padres con IA.'),
   'reel piano sequenza 3D, animazione 3D', 'Dew3q0zxIkS', '7699164743017205024')
_v('reel-occhiali-scacchi', '2026-10-22', 27.0, MD,
   ('Ha barato a scacchi con gli occhiali smart', 'Storia virale raccontata in 3D: scacchiera, occhiali ai raggi X e motore di scacchi, con il collegamento a come l’AI lavora nei processi aziendali.'),
   ('He cheated at chess with smart glasses', 'Viral story told in 3D: chessboard, X-ray glasses and chess engine, linked to how AI works in business processes.'),
   ('Mit Smart-Brille beim Schach geschummelt', 'Virale Geschichte in 3D: Schachbrett, Röntgen-Brille und Schach-Engine, mit Bezug zu KI in Unternehmen.'),
   ('Il a triché aux échecs avec des lunettes connectées', 'Histoire virale en 3D : échiquier, lunettes aux rayons X et moteur d’échecs.'),
   ('Hizo trampa al ajedrez con gafas inteligentes', 'Historia viral en 3D: tablero, gafas de rayos X y motor de ajedrez.'),
   'reel 3D, storia virale', 'Deywd9CROnP', '7699436097264176417')
_v('reel-mac-lento', '2026-10-22', 25.0, MD,
   ('Il Mac era lento. Non era vecchio.', 'Reel editoriale dinamico: un assistente AI scopre un programma nascosto che consumava il computer. Con guida gratuita ai 5 controlli da fare.'),
   ('The Mac was slow. It wasn’t old.', 'Dynamic editorial reel: an AI assistant finds a hidden program draining the computer. With a free 5-check guide.'),
   ('Der Mac war langsam. Er war nicht alt.', 'Dynamisches Reel: ein KI-Assistent findet ein verstecktes Programm, das den Rechner auslastete.'),
   ('Le Mac était lent. Il n’était pas vieux.', 'Reel éditorial dynamique : un assistant IA découvre un programme caché qui épuisait l’ordinateur.'),
   ('El Mac iba lento. No era viejo.', 'Reel editorial dinámico: un asistente IA descubre un programa oculto que agotaba el ordenador.'),
   'reel editoriale, sicurezza informatica', 'DezcFhBxFIk', '7699534695909903649')
_v('reel-cartello-palestra', '2026-10-22', 23.0, MD,
   ('Il cartello della palestra era falso', 'Apertura con riprese vere e grafica animata: il cartello virale “vietato programmare con l’AI” in una palestra, verificato e smontato.'),
   ('The gym sign was fake', 'Opens with real footage and animated graphics: the viral “no coding with AI” gym sign, fact-checked.'),
   ('Das Fitnessstudio-Schild war gefälscht', 'Echte Aufnahmen und Animation: das virale Schild „Kein Programmieren mit KI“ im Faktencheck.'),
   ('La pancarte de la salle de sport était fausse', 'Images réelles et graphisme animé : la pancarte virale « interdit de coder avec l’IA » vérifiée.'),
   ('El cartel del gimnasio era falso', 'Imágenes reales y gráficos animados: el cartel viral de “prohibido programar con IA”, verificado.'),
   'reel fact checking, riprese e motion design')
_v('reel-ai-nelle-vendite', '2026-10-23', 21.0, MD,
   ('L’AI nelle vendite: contatti giusti dal 18% al 97%', 'Reel con schede animate in 3D sul caso di un’azienda che con l’AI ha migliorato la qualità dei contatti commerciali, e sulla guida pubblicata da Anthropic.'),
   ('AI in sales: qualified leads from 18% to 97%', 'Reel with 3D animated cards on a company that improved lead quality with AI, and Anthropic’s published guide.'),
   ('KI im Vertrieb: passende Kontakte von 18 % auf 97 %', 'Reel mit 3D-Karten zu einem Unternehmen, das mit KI die Lead-Qualität verbessert hat.'),
   ('L’IA dans la vente : bons contacts de 18 % à 97 %', 'Reel aux cartes animées 3D sur une entreprise qui a amélioré la qualité des contacts avec l’IA.'),
   ('IA en ventas: contactos buenos del 18 % al 97 %', 'Reel con tarjetas 3D sobre una empresa que mejoró la calidad de los contactos con IA.'),
   'reel AI vendite, CRM', 'De1D87dxm9r', '7699767343899086113')
_v('reel-scartato-in-6-minuti', '2026-10-23', 34.0, MD,
   ('Si è candidato nella sua azienda: scartato in 6 minuti', 'Storia raccontata in reel: un manager mette alla prova il filtro automatico delle candidature della sua azienda, e lo scopre troppo severo.'),
   ('He applied to his own company: rejected in 6 minutes', 'Story reel: a manager tests his company’s automated applicant filter and finds it far too strict.'),
   ('Bei der eigenen Firma beworben: in 6 Minuten abgelehnt', 'Story-Reel: ein Manager testet den automatischen Bewerberfilter seiner Firma.'),
   ('Candidat dans sa propre entreprise : rejeté en 6 minutes', 'Reel narratif : un manager teste le filtre automatique de candidatures de son entreprise.'),
   ('Se postuló en su empresa: descartado en 6 minutos', 'Reel narrativo: un directivo pone a prueba el filtro automático de candidaturas.'),
   'reel storytelling, automazioni')
_v('reel-bmw-uscite', '2026-10-23', 25.0, MD,
   ('Una casa auto paga chi se ne va', 'Notizia economica in reel con grafica animata: il programma di uscite volontarie di un grande costruttore tedesco e cosa significa per le aziende.'),
   ('A carmaker pays staff to leave', 'Business news as a reel with animated graphics: a German carmaker’s voluntary exit programme.'),
   ('Ein Autobauer zahlt fürs Gehen', 'Wirtschaftsnews als Reel: das Freiwilligenprogramm eines deutschen Autobauers.'),
   ('Un constructeur auto paie ceux qui partent', 'Actu économique en reel : le programme de départs volontaires d’un constructeur allemand.'),
   ('Un fabricante de coches paga a quien se va', 'Noticia económica en reel: el programa de bajas voluntarias de un fabricante alemán.'),
   'reel notizia economia, grafica animata')

TUTTI = ['spot-ai-roadster', 'spot-stand-chiavi-in-mano', 'reel-ufficio-ordini-0-dipendenti', 'reel-sito-con-ai-in-1-minuto',
         'reel-sito-lento', 'reel-ferrari-pizzeria', 'reel-sfida-sito-dentista', 'reel-micro-animazioni-sito', 'reel-stand-pandoora',
         'reel-ai-di-notte', 'reel-tv-senza-pubblicita', 'reel-mac-lento', 'reel-occhiali-scacchi', 'reel-ai-nelle-vendite',
         'reel-fornitori', 'reel-un-solo-team', 'reel-quanto-costa-un-sito', 'reel-listino-prezzi', 'reel-risposta-in-24-ore',
         'reel-stand-chiavi-in-mano', 'reel-ai-clona-office', 'reel-siti-web-11500-dollari', 'reel-notizia-rtx5090',
         'reel-ai-al-colloquio', 'reel-simboli-prompt', 'reel-agenti-ai-anthropic', 'reel-anthropic-junior', 'reel-accenture-claude',
         'reel-cartello-palestra', 'reel-scartato-in-6-minuti', 'reel-bmw-uscite', 'reel-ai-tv-box']
assert len(TUTTI) == len(VIDEO) == len(set(TUTTI)), (len(TUTTI), len(VIDEO))
