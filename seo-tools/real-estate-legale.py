# -*- coding: utf-8 -*-
"""24/10/2026 - Pagine legali in rumeno e albanese per la sezione Danova Real Estate:
   /ro/confidentialitate/  /ro/politica-cookie/  /ro/termeni-de-utilizare/
   /sq/privatesia/          /sq/politika-e-cookie-ve/  /sq/kushtet-e-perdorimit/
   Costruite sulla cornice della pagina /xx/real-estate/ (stesso tema), con hreflang reciproci verso le versioni IT/EN/DE.
   I testi descrivono il funzionamento reale del sito al 24/10/2026: modulo inviato tramite FormSubmit (con ripiego sull'app di posta),
   font ospitati sul dominio, statistiche Cloudflare Web Analytics senza cookie, immagini illustrative create con l'IA.
   Lanciare dopo real-estate-build.py e prima di real-estate-tema.py / real-estate-chrome.py. Idempotente.
   Uso: python3 seo-tools/real-estate-legale.py"""
import os, re, json, html
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(HERE)
SITE = 'https://danova-tech.com'
MAIL = '<a href="mailto:info@danova-tech.com">info@danova-tech.com</a>'
ALT = {  # pagina -> equivalenti nelle altre lingue
 'privacy': {'it': '/privacy/', 'en': '/en/privacy/', 'de': '/de/datenschutz/', 'ro': '/ro/confidentialitate/', 'sq': '/sq/privatesia/', 'hi': '/hi/privacy/'},
 'cookie': {'it': '/cookie-policy/', 'en': '/en/cookie-policy/', 'de': '/de/cookie-richtlinie/', 'ro': '/ro/politica-cookie/', 'sq': '/sq/politika-e-cookie-ve/', 'hi': '/hi/cookie-policy/'},
 'termini': {'it': '/termini/', 'en': '/en/terms/', 'de': '/de/agb/', 'ro': '/ro/termeni-de-utilizare/', 'sq': '/sq/kushtet-e-perdorimit/', 'hi': '/hi/terms/'},
}
def ul(*x): return '<ul>' + ''.join('<li>%s</li>' % i for i in x) + '</ul>'
def p(*x): return ''.join('<p>%s</p>' % i for i in x)

T = {'ro': {}, 'sq': {}}
# ------------------------------------------------------------------ RUMENO
T['ro']['privacy'] = dict(
 title='Politica de confidențialitate — Danova Real Estate', h1='Politica de confidențialitate',
 desc='Cum prelucrează Danova Tech și divizia Danova Real Estate datele personale colectate prin site: operator, scopuri, temeiuri juridice, păstrare și drepturile dvs. conform GDPR.',
 lead='Cum prelucrează Danova Tech, inclusiv divizia Danova Real Estate, datele personale colectate prin acest site: operator, scopuri, temeiuri juridice, perioade de păstrare, destinatari și cum vă puteți exercita drepturile prevăzute de GDPR.',
 sec=[
 ('Operatorul de date', p('<b>Danova Tech</b> — P.IVA (cod fiscal italian) 05369890263 — sediul în Via Rigole 48, 31040 Rigole di Mansuè (TV), Italia. E-mail: ' + MAIL,
   'Danova Real Estate este divizia de construcții și renovări a Danova Tech: operatorul datelor este același. Danova Tech este operatorul datelor personale colectate prin acest site, în conformitate cu Regulamentul (UE) 2016/679 (GDPR) și cu legislația italiană (Decretul legislativ 196/2003, modificat prin Decretul legislativ 101/2018). Nu a fost numit un responsabil cu protecția datelor (DPO), deoarece nu sunt îndeplinite condițiile legale care l-ar impune.')),
 ('Ce date prelucrăm', p('Prelucrăm doar datele pe care ni le furnizați în mod voluntar și datele tehnice necesare funcționării site-ului.') + ul(
   '<b>Date de contact</b> introduse în formular: nume și firmă, e-mail, telefon (opțional), textul mesajului și, dacă o indicați, perioada în care doriți să începeți lucrările.',
   '<b>Date de navigare</b> înregistrate automat de serverul de găzduire: adresa IP, browserul și sistemul de operare, data și ora solicitării, paginile vizitate. Sunt folosite în formă agregată pentru securitate, diagnosticare și statistici de trafic.')
   + p('Site-ul <b>nu folosește cookie-uri de profilare</b> și nu creează profiluri comerciale ale vizitatorilor.')),
 ('Cum funcționează formularul de contact', p('Când trimiteți formularul, datele sunt transmise prin serviciul <b>FormSubmit</b> (formsubmit.co), care ni le livrează ca e-mail în căsuța ' + MAIL + '; acolo sunt păstrate ca simplă corespondență comercială. Dacă trimiterea nu reușește, site-ul deschide aplicația de e-mail de pe dispozitivul dvs. cu mesajul deja completat, pe care îl trimiteți chiar dvs.',
   'Ne puteți contacta și direct prin telefon sau WhatsApp, fără a folosi formularul.')),
 ('Scopuri și temeiuri juridice', ul(
   'Răspunsul la cererile de informații, inspecție și ofertă și demersurile precontractuale — art. 6 alin. (1) lit. b) GDPR.',
   'Gestionarea relației contractuale și a lucrărilor comandate — art. 6 alin. (1) lit. b) GDPR.',
   'Îndeplinirea obligațiilor fiscale, contabile și a altor obligații legale — art. 6 alin. (1) lit. c) GDPR.',
   'Securitatea site-ului și prevenirea abuzurilor sau a tentativelor de intruziune — interes legitim, art. 6 alin. (1) lit. f) GDPR.',
   'Comunicări promoționale despre serviciile noastre, numai cu consimțământul dvs. liber exprimat, pe care îl puteți retrage oricând — art. 6 alin. (1) lit. a) GDPR.')),
 ('Este obligatorie furnizarea datelor?', p('Furnizarea datelor marcate ca obligatorii în formular este necesară pentru a vă putea răspunde: fără ele nu putem da curs cererii. Furnizarea celorlalte date este facultativă și nu influențează răspunsul nostru.')),
 ('Cui comunicăm datele', p('Datele pot fi prelucrate de personalul autorizat și comunicate furnizorilor de servicii la care apelăm, desemnați, după caz, persoane împuternicite conform art. 28 GDPR: furnizorul de găzduire a site-ului, furnizorii serviciilor de e-mail și de formular, consultanții contabili, fiscali și juridici, precum și autoritățile publice, atunci când legea o impune.',
   'Pentru executarea lucrărilor, datele strict necesare (de exemplu adresa imobilului și un număr de telefon) pot fi comunicate firmelor și meșterilor care lucrează pe șantierul dvs.',
   'Datele <b>nu sunt niciodată făcute publice, comercializate sau vândute</b> unor terți în scopuri comerciale.')),
 ('Transferuri în afara Uniunii Europene', p('Serviciul de formular FormSubmit și serviciul de statistici Cloudflare Web Analytics pot prelucra date pe servere situate în afara Spațiului Economic European, inclusiv în Statele Unite. Pentru aceste transferuri ne bazăm pe garanțiile prevăzute în capitolul V din GDPR.',
   'Fonturile site-ului, imaginile și videoclipurile sunt găzduite pe acest domeniu: browserul dvs. nu contactează servere Google sau YouTube pentru a le încărca.')),
 ('Cât timp păstrăm datele', ul(
   'Cereri de contact care nu sunt urmate de un contract: <b>24 de luni</b> de la ultimul schimb de mesaje.',
   'Date privind contractele, facturile și evidențele contabile: <b>10 ani</b>, conform legislației civile și fiscale italiene.',
   'Jurnale tehnice ale serverului: cel mult <b>12 luni</b>, cu excepția cazului în care sunt necesare pentru investigarea unor fapte ilegale.',
   'Date prelucrate pe baza consimțământului: până la retragerea acestuia.')),
 ('Drepturile dvs.', p('Vă puteți exercita oricând drepturile prevăzute la articolele 15–22 din GDPR: accesul la date, rectificarea, ștergerea, restricționarea prelucrării, portabilitatea, opoziția la prelucrare și retragerea consimțământului acordat.',
   'Este suficient să ne scrieți la ' + MAIL + ': răspundem în cel mult 30 de zile de la primirea cererii. Aveți, de asemenea, dreptul de a depune o plângere la autoritatea italiană pentru protecția datelor (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">garanteprivacy.it</a>) sau la autoritatea de supraveghere din țara în care locuiți — în România, ANSPDCP (<a href="https://www.dataprotection.ro" target="_blank" rel="noopener">dataprotection.ro</a>).')),
 ('Securitatea datelor', p('Aplicăm măsuri tehnice și organizatorice adecvate pentru a proteja datele împotriva accesului neautorizat, pierderii sau divulgării: conexiuni criptate HTTPS, căsuțe de e-mail protejate cu parole puternice și autentificare în doi pași, acces limitat la personalul strict necesar și copii de siguranță periodice.')),
 ('Minori', p('Serviciile noastre se adresează adulților, firmelor și organizațiilor. Nu colectăm în mod intenționat date personale de la minori sub 16 ani. Dacă credeți că un minor ne-a transmis date, scrieți-ne și le vom șterge fără întârziere.')),
 ('Modificări ale acestei informări', p('Această informare poate fi actualizată pentru a reflecta modificări ale legislației sau ale serviciilor noastre. Versiunea în vigoare este întotdeauna cea publicată pe această pagină, cu data ultimei actualizări.')),
 ])
T['ro']['cookie'] = dict(
 title='Politica privind cookie-urile — Danova Real Estate', h1='Politica privind cookie-urile',
 desc='Ce cookie-uri folosește site-ul Danova Tech și Danova Real Estate: fără cookie-uri de profilare sau publicitate, statistici agregate fără cookie-uri.',
 lead='Ce cookie-uri folosește site-ul Danova Tech și Danova Real Estate, la ce servesc și cum le gestionați din browser. Fără cookie-uri de profilare, fără urmărire publicitară.',
 sec=[
 ('Ce sunt cookie-urile', p('Cookie-urile sunt fișiere text de mici dimensiuni pe care site-urile le salvează pe dispozitivul vizitatorului pentru a păstra informații: preferințe, sesiuni de autentificare sau, în cazul cookie-urilor de profilare, comportamentul de navigare folosit în scopuri publicitare. Tehnologii similare sunt pixelii de urmărire, stocarea locală (local storage) și amprenta browserului (fingerprinting).')),
 ('Cookie-urile folosite de acest site', p('Acest site <b>nu instalează cookie-uri de profilare, de analiză sau de marketing</b> și nu folosește instrumente care urmăresc comportamentul vizitatorilor. Nu există Google Analytics, Meta Pixel sau tehnologii echivalente.',
   'Vizitele sunt numărate cu <b>Cloudflare Web Analytics</b>, un instrument de statistici agregate care nu setează cookie-uri, nu salvează nimic pe dispozitivul dvs. și nu creează profiluri.',
   'Site-ul nu salvează pe dispozitivul dvs. nici cookie-uri tehnice proprii. Din acest motiv nu este necesar un banner de consimțământ prealabil.')),
 ('Servicii terțe', p('Fonturile folosite pe site (Sora, Inter, JetBrains Mono), imaginile și videoclipurile sunt <b>găzduite pe acest domeniu</b>: browserul dvs. nu contactează servere externe pentru a le descărca.',
   'Statisticile de vizitare sunt colectate cu <b>Cloudflare Web Analytics</b> (Cloudflare, Inc.): sunt înregistrate, în formă agregată, pagina vizitată, sursa traficului, tipul de dispozitiv și țara. Ca la orice solicitare către un server extern, adresa IP este comunicată Cloudflare pentru a livra răspunsul. Informarea Cloudflare: <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">cloudflare.com/privacypolicy</a>. Dacă blocați scriptul cu o extensie a browserului, site-ul funcționează la fel.',
   'Când trimiteți formularul de contact, datele sunt transmise serviciului <b>FormSubmit</b> (formsubmit.co), care ni le livrează prin e-mail.')),
 ('Linkuri și conținut extern', p('Site-ul conține linkuri către platforme terțe (de exemplu WhatsApp, Instagram, Facebook și TikTok). Urmând aceste linkuri ajungeți pe site-uri care au propriile politici privind cookie-urile, asupra cărora nu avem control; vă recomandăm să le citiți.')),
 ('Gestionarea cookie-urilor din browser', p('Vă puteți configura oricând browserul pentru a bloca sau șterge cookie-urile oricărui site. Instrucțiunile se găsesc în setările browserului:') + ul(
   '<b>Chrome</b> — Setări › Confidențialitate și securitate › Cookie-uri.', '<b>Safari</b> — Setări › Confidențialitate › Gestionați datele site-urilor.',
   '<b>Firefox</b> — Setări › Confidențialitate și securitate › Cookie-uri și date ale site-urilor.', '<b>Edge</b> — Setări › Cookie-uri și permisiuni pentru site.')
   + p('Blocarea cookie-urilor nu vă împiedică să navigați pe acest site.')),
 ('Actualizări', p('Dacă vom introduce în viitor instrumente de măsurare sau de marketing, vom activa un banner de consimțământ prealabil conform ghidurilor autorității italiene pentru protecția datelor și vom actualiza această pagină înainte ca aceste instrumente să fie active.')),
 ])
T['ro']['termini'] = dict(
 title='Termeni de utilizare — Danova Real Estate', h1='Termeni de utilizare',
 desc='Termenii de utilizare ai site-ului Danova Tech și Danova Real Estate: proprietate intelectuală, oferte, imagini ilustrative, răspundere, lege aplicabilă.',
 lead='Termenii de utilizare ai site-ului Danova Tech și ai diviziei Danova Real Estate: proprietatea conținutului, utilizarea permisă, ofertele, limitarea răspunderii, legea aplicabilă și instanța competentă.',
 sec=[
 ('Obiect și proprietarul site-ului', p('Acest site este administrat de <b>Danova Tech</b> — P.IVA 05369890263 — cu sediul în Via Rigole 48, 31040 Rigole di Mansuè (TV), Italia, e-mail ' + MAIL + '. Danova Real Estate este divizia de construcții și renovări a Danova Tech. Acești termeni reglementează accesul la site și utilizarea conținutului său.')),
 ('Acceptare', p('Navigând pe site, acceptați integral acești termeni. Dacă nu sunteți de acord cu ei, vă rugăm să nu folosiți site-ul.')),
 ('Utilizare permisă', p('Puteți consulta și folosi site-ul în scop informativ și pentru a ne contacta. Este interzis: să folosiți site-ul în scopuri ilegale sau contrare bunei-credințe, să încercați accesul neautorizat la sisteme sau zone rezervate, să extrageți conținut în mod automat și în masă, să introduceți cod malițios sau să faceți orice acțiune care compromite funcționarea ori securitatea site-ului.')),
 ('Proprietate intelectuală', p('Codul, grafica, textele, machetele, imaginile prelucrate, precum și numele și logourile <b>Danova Tech</b> și <b>Danova Real Estate</b> aparțin Danova Tech sau licențiatorilor săi și sunt protejate de legislația privind dreptul de autor și mărcile. Reproducerea, modificarea, distribuirea sau reutilizarea, integrală ori parțială, fără acord scris sunt interzise.',
   'Mărcile, denumirile și logourile terților menționate aparțin proprietarilor lor și sunt folosite exclusiv în scop descriptiv.')),
 ('Imagini, exemple și cifre', p('Imaginile și videoclipurile din secțiunea Danova Real Estate sunt <b>ilustrative, create cu inteligența artificială</b> pentru a arăta tipul de lucrări: nu reprezintă șantiere, imobile sau clienți reali. Exemplele, termenele și cifrele prezentate se referă la situații tipice și nu constituie o promisiune de rezultat pentru alte proiecte.')),
 ('Conținut și disponibilitate', p('Conținutul are caracter informativ și promoțional și poate fi modificat sau eliminat oricând, fără preaviz. Deși avem grijă să fie corect, nu garantăm că informațiile sunt complete sau mereu actualizate.',
   'Ne străduim să menținem site-ul accesibil, dar nu garantăm funcționarea neîntreruptă: accesul poate fi suspendat pentru întreținere, actualizări sau din motive independente de voința noastră.')),
 ('Cereri de ofertă și încheierea contractului', p('Informațiile despre servicii, termene și metode publicate pe site sunt orientative și <b>nu constituie o ofertă publică</b> în sensul art. 1336 din Codul civil italian. Trimiterea unei cereri prin formular sau prin e-mail nu obligă niciuna dintre părți.',
   'Relația contractuală se naște doar prin acceptarea în scris a unei oferte specifice, care stabilește obiectul, termenele, prețul și condițiile lucrărilor și prevalează asupra celor afirmate pe site.')),
 ('Limitarea răspunderii', p('În limitele permise de lege, Danova Tech nu răspunde pentru daunele indirecte sau consecutive care decurg din utilizarea sau imposibilitatea utilizării site-ului, din întreruperi ale serviciului ori din conținutul site-urilor terțe la care trimit linkurile. Nicio prevedere a acestor termeni nu limitează răspunderea pentru dol, culpă gravă sau în cazurile în care legea nu permite excluderi.')),
 ('Linkuri către site-uri terțe', p('Site-ul poate conține linkuri către resurse externe, oferite pentru comoditatea dvs. Nu controlăm aceste site-uri și nu răspundem pentru conținutul, politicile sau serviciile lor.')),
 ('Protecția datelor personale', p('Prelucrarea datelor personale colectate prin site este descrisă în <a href="/ro/confidentialitate/">Politica de confidențialitate</a> și în <a href="/ro/politica-cookie/">Politica privind cookie-urile</a>, care fac parte integrantă din acești termeni.')),
 ('Legea aplicabilă și instanța competentă', p('Acești termeni sunt guvernați de legea italiană. Pentru litigiile cu utilizatorii care au calitatea de consumatori este competentă instanța de la domiciliul sau reședința consumatorului. În toate celelalte cazuri este competentă instanța de la sediul proprietarului site-ului.')),
 ('Modificări ale acestor termeni', p('Acești termeni pot fi actualizați oricând. Versiunea aplicabilă este cea publicată pe această pagină în momentul accesării, cu data ultimei actualizări.')),
 ])
# ------------------------------------------------------------------ ALBANESE
T['sq']['privacy'] = dict(
 title='Politika e privatësisë — Danova Real Estate', h1='Politika e privatësisë',
 desc='Si i përpunojnë Danova Tech dhe divizioni Danova Real Estate të dhënat personale të mbledhura nga faqja: kontrolluesi, qëllimet, bazat ligjore, ruajtja dhe të drejtat tuaja sipas GDPR.',
 lead='Si i përpunon Danova Tech, përfshirë divizionin Danova Real Estate, të dhënat personale të mbledhura përmes kësaj faqeje: kontrolluesi, qëllimet, bazat ligjore, afatet e ruajtjes, marrësit dhe si t’i ushtroni të drejtat tuaja sipas GDPR.',
 sec=[
 ('Kontrolluesi i të dhënave', p('<b>Danova Tech</b> — P.IVA (numri tatimor italian) 05369890263 — me seli në Via Rigole 48, 31040 Rigole di Mansuè (TV), Itali. Email: ' + MAIL,
   'Danova Real Estate është divizioni i ndërtimit dhe i rinovimeve i Danova Tech: kontrolluesi i të dhënave është i njëjti. Danova Tech është kontrolluesi i të dhënave personale të mbledhura përmes kësaj faqeje, në përputhje me Rregulloren (BE) 2016/679 (GDPR) dhe me legjislacionin italian (Dekreti Legjislativ 196/2003, i ndryshuar me Dekretin Legjislativ 101/2018). Nuk është caktuar një zyrtar për mbrojtjen e të dhënave (DPO), sepse nuk plotësohen kushtet ligjore që e bëjnë të detyrueshëm.')),
 ('Cilat të dhëna përpunojmë', p('Përpunojmë vetëm të dhënat që na i jepni vullnetarisht dhe të dhënat teknike të nevojshme për funksionimin e faqes.') + ul(
   '<b>Të dhënat e kontaktit</b> të plotësuara në formular: emri dhe kompania, email-i, telefoni (opsional), teksti i mesazhit dhe, nëse e tregoni, koha kur dëshironi të nisin punimet.',
   '<b>Të dhënat e shfletimit</b> të regjistruara automatikisht nga serveri i hostimit: adresa IP, shfletuesi dhe sistemi operativ, data dhe ora e kërkesës, faqet e vizituara. Përdoren në formë të përmbledhur për siguri, diagnostikim dhe statistika trafiku.')
   + p('Faqja <b>nuk përdor cookie profilizimi</b> dhe nuk krijon profile tregtare të vizitorëve.')),
 ('Si funksionon formulari i kontaktit', p('Kur e dërgoni formularin, të dhënat transmetohen përmes shërbimit <b>FormSubmit</b> (formsubmit.co), i cili na i dorëzon si email në kutinë ' + MAIL + ', ku ruhen si korrespondencë e zakonshme tregtare. Nëse dërgimi nuk arrihet, faqja hap aplikacionin e email-it në pajisjen tuaj me mesazhin të gatshëm, të cilin e dërgoni vetë.',
   'Mund të na kontaktoni edhe drejtpërdrejt me telefon ose në WhatsApp, pa përdorur formularin.')),
 ('Qëllimet dhe bazat ligjore', ul(
   'Përgjigjja ndaj kërkesave për informacion, inspektim dhe ofertë, si dhe hapat parakontraktorë — neni 6(1)(b) i GDPR.',
   'Menaxhimi i marrëdhënies kontraktore dhe i punimeve të porositura — neni 6(1)(b) i GDPR.',
   'Përmbushja e detyrimeve tatimore, kontabël dhe ligjore të tjera — neni 6(1)(c) i GDPR.',
   'Siguria e faqes dhe parandalimi i abuzimeve ose i përpjekjeve për ndërhyrje — interes legjitim, neni 6(1)(f) i GDPR.',
   'Komunikime promovuese për shërbimet tona, vetëm me pëlqimin tuaj të lirë, të cilin mund ta tërhiqni në çdo kohë — neni 6(1)(a) i GDPR.')),
 ('A është e detyrueshme dhënia e të dhënave?', p('Dhënia e të dhënave të shënuara si të detyrueshme në formular është e nevojshme që t’ju përgjigjemi: pa to nuk mund ta trajtojmë kërkesën tuaj. Dhënia e të dhënave të tjera është fakultative dhe nuk ndikon në përgjigjen tonë.')),
 ('Me kë i ndajmë të dhënat', p('Të dhënat mund të përpunohen nga personeli i autorizuar dhe t’u komunikohen ofruesve të shërbimeve që përdorim, të caktuar, kur është e nevojshme, si përpunues sipas nenit 28 të GDPR: ofruesi i hostimit të faqes, ofruesit e shërbimeve të email-it dhe të formularit, këshilltarët kontabël, tatimorë dhe ligjorë, si dhe autoritetet publike kur e kërkon ligji.',
   'Për kryerjen e punimeve, të dhënat rreptësisht të nevojshme (për shembull adresa e pronës dhe një numër telefoni) mund t’u komunikohen kompanive dhe mjeshtrave që punojnë në kantierin tuaj.',
   'Të dhënat <b>nuk publikohen, nuk tregtohen dhe nuk u shiten kurrë</b> palëve të treta për qëllime tregtare.')),
 ('Transferimet jashtë Bashkimit Evropian', p('Shërbimi i formularit FormSubmit dhe shërbimi i statistikave Cloudflare Web Analytics mund të përpunojnë të dhëna në serverë jashtë Zonës Ekonomike Evropiane, përfshirë Shtetet e Bashkuara. Për këto transferime mbështetemi te garancitë e parashikuara në Kapitullin V të GDPR.',
   'Fontet, imazhet dhe videot e faqes janë të hostuara në këtë domen: shfletuesi juaj nuk kontakton serverët e Google ose të YouTube për t’i ngarkuar.')),
 ('Sa kohë i ruajmë të dhënat', ul(
   'Kërkesat për kontakt që nuk pasohen nga një kontratë: <b>24 muaj</b> nga komunikimi i fundit.',
   'Të dhënat që lidhen me kontratat, faturat dhe regjistrat kontabël: <b>10 vjet</b>, siç e kërkon ligji civil dhe tatimor italian.',
   'Regjistrat teknikë të serverit: jo më shumë se <b>12 muaj</b>, përveçse kur nevojiten për të hetuar veprime të paligjshme.',
   'Të dhënat e përpunuara në bazë të pëlqimit: deri në tërheqjen e tij.')),
 ('Të drejtat tuaja', p('Në çdo kohë mund të ushtroni të drejtat e parashikuara nga nenet 15–22 të GDPR: qasjen në të dhënat tuaja, korrigjimin, fshirjen, kufizimin e përpunimit, transferueshmërinë, kundërshtimin e përpunimit dhe tërheqjen e çdo pëlqimi të dhënë.',
   'Mjafton të na shkruani në ' + MAIL + ': përgjigjemi brenda 30 ditëve nga marrja e kërkesës. Keni gjithashtu të drejtë të paraqisni ankesë pranë Autoritetit italian për mbrojtjen e të dhënave (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">garanteprivacy.it</a>) ose pranë autoritetit mbikëqyrës të vendit ku banoni.')),
 ('Siguria e të dhënave', p('Zbatojmë masa teknike dhe organizative të përshtatshme për t’i mbrojtur të dhënat nga qasja e paautorizuar, humbja ose zbulimi: lidhje të enkriptuara HTTPS, kuti email-i të mbrojtura me fjalëkalime të forta dhe vërtetim me dy hapa, qasje e kufizuar vetëm te personeli i domosdoshëm dhe kopje rezervë të rregullta.')),
 ('Të miturit', p('Shërbimet tona u drejtohen të rriturve, kompanive dhe organizatave. Nuk mbledhim me vetëdije të dhëna personale nga fëmijë nën 16 vjeç. Nëse mendoni se një i mitur na ka dhënë të dhëna, na shkruani dhe do t’i fshijmë pa vonesë.')),
 ('Ndryshimet e këtij njoftimi', p('Ky njoftim mund të përditësohet për të pasqyruar ndryshime në ligj ose në shërbimet tona. Versioni në fuqi është gjithmonë ai i publikuar në këtë faqe, me datën e përditësimit të fundit.')),
 ])
T['sq']['cookie'] = dict(
 title='Politika e cookie-ve — Danova Real Estate', h1='Politika e cookie-ve',
 desc='Cilat cookie përdor faqja e Danova Tech dhe Danova Real Estate: pa cookie profilizimi apo reklamash, statistika të përmbledhura pa cookie.',
 lead='Cilat cookie përdor faqja e Danova Tech dhe e Danova Real Estate, për çfarë shërbejnë dhe si t’i menaxhoni nga shfletuesi. Pa cookie profilizimi, pa gjurmim reklamash.',
 sec=[
 ('Çfarë janë cookie-t', p('Cookie-t janë skedarë të vegjël teksti që faqet e internetit ruajnë në pajisjen e vizitorit për të mbajtur informacione: preferenca, seanca hyrjeje ose, në rastin e cookie-ve të profilizimit, sjelljen e shfletimit që përdoret për reklama. Teknologji të ngjashme janë pikselët e gjurmimit, ruajtja lokale (local storage) dhe gjurma e shfletuesit (fingerprinting).')),
 ('Cookie-t që përdor kjo faqe', p('Kjo faqe <b>nuk instalon cookie profilizimi, analitike apo marketingu</b> dhe nuk përdor mjete që gjurmojnë sjelljen e vizitorëve. Nuk ka Google Analytics, Meta Pixel apo teknologji të ngjashme.',
   'Vizitat numërohen me <b>Cloudflare Web Analytics</b>, një mjet statistikash të përmbledhura që nuk vendos cookie, nuk ruan asgjë në pajisjen tuaj dhe nuk krijon profile.',
   'Faqja nuk ruan në pajisjen tuaj as cookie teknike të veta. Për këtë arsye nuk nevojitet një banner për pëlqim paraprak.')),
 ('Shërbimet e palëve të treta', p('Fontet e përdorura në faqe (Sora, Inter, JetBrains Mono), imazhet dhe videot janë <b>të hostuara në këtë domen</b>: shfletuesi juaj nuk kontakton serverë të jashtëm për t’i shkarkuar.',
   'Statistikat e vizitave mblidhen me <b>Cloudflare Web Analytics</b> (Cloudflare, Inc.): regjistrohen, në formë të përmbledhur, faqja e vizituar, burimi i trafikut, lloji i pajisjes dhe vendi. Si në çdo kërkesë drejt një serveri të jashtëm, adresa IP i komunikohet Cloudflare për të dhënë përgjigjen. Njoftimi i Cloudflare: <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">cloudflare.com/privacypolicy</a>. Nëse e bllokoni skriptin me një shtesë të shfletuesit, faqja funksionon njësoj.',
   'Kur dërgoni formularin e kontaktit, të dhënat i kalojnë shërbimit <b>FormSubmit</b> (formsubmit.co), i cili na i dorëzon me email.')),
 ('Lidhjet dhe përmbajtja e jashtme', p('Faqja përmban lidhje drejt platformave të palëve të treta (për shembull WhatsApp, Instagram, Facebook dhe TikTok). Duke ndjekur këto lidhje kaloni në faqe që kanë politikat e tyre të cookie-ve, mbi të cilat nuk kemi kontroll; ju këshillojmë t’i lexoni.')),
 ('Menaxhimi i cookie-ve në shfletues', p('Në çdo kohë mund ta vendosni shfletuesin të bllokojë ose të fshijë cookie-t e çdo faqeje. Udhëzimet gjenden te cilësimet e shfletuesit:') + ul(
   '<b>Chrome</b> — Cilësimet › Privatësia dhe siguria › Cookie-t.', '<b>Safari</b> — Cilësimet › Privatësia › Menaxho të dhënat e faqeve.',
   '<b>Firefox</b> — Cilësimet › Privatësia dhe siguria › Cookie-t dhe të dhënat e faqeve.', '<b>Edge</b> — Cilësimet › Cookie-t dhe lejet e faqeve.')
   + p('Bllokimi i cookie-ve nuk ju pengon të shfletoni këtë faqe.')),
 ('Përditësimet', p('Nëse në të ardhmen do të fusim mjete matjeje ose marketingu, do të aktivizojmë një banner për pëlqim paraprak sipas udhëzimeve të Autoritetit italian për mbrojtjen e të dhënave dhe do ta përditësojmë këtë faqe përpara se këto mjete të vihen në punë.')),
 ])
T['sq']['termini'] = dict(
 title='Kushtet e përdorimit — Danova Real Estate', h1='Kushtet e përdorimit',
 desc='Kushtet e përdorimit të faqes së Danova Tech dhe Danova Real Estate: pronësia intelektuale, ofertat, imazhet ilustruese, përgjegjësia, ligji i zbatueshëm.',
 lead='Kushtet e përdorimit të faqes së Danova Tech dhe të divizionit Danova Real Estate: pronësia e përmbajtjes, përdorimi i lejuar, ofertat, kufizimi i përgjegjësisë, ligji i zbatueshëm dhe gjykata kompetente.',
 sec=[
 ('Objekti dhe pronari i faqes', p('Kjo faqe administrohet nga <b>Danova Tech</b> — P.IVA 05369890263 — me seli në Via Rigole 48, 31040 Rigole di Mansuè (TV), Itali, email ' + MAIL + '. Danova Real Estate është divizioni i ndërtimit dhe i rinovimeve i Danova Tech. Këto kushte rregullojnë hyrjen në faqe dhe përdorimin e përmbajtjes së saj.')),
 ('Pranimi', p('Duke shfletuar faqen, i pranoni plotësisht këto kushte. Nëse nuk jeni dakord me to, ju lutemi mos e përdorni faqen.')),
 ('Përdorimi i lejuar', p('Mund ta shikoni dhe ta përdorni faqen për qëllime informative dhe për të na kontaktuar. Ndalohet: përdorimi i faqes për qëllime të paligjshme ose në kundërshtim me mirëbesimin, përpjekjet për qasje të paautorizuar në sisteme ose zona të rezervuara, nxjerrja automatike dhe masive e përmbajtjes, futja e kodit dashakeq ose çdo veprim që cenon funksionimin apo sigurinë e faqes.')),
 ('Pronësia intelektuale', p('Kodi, grafika, tekstet, faqosja, imazhet e përpunuara, si dhe emrat dhe logot <b>Danova Tech</b> dhe <b>Danova Real Estate</b> i përkasin Danova Tech ose dhënësve të saj të licencës dhe mbrohen nga ligjet për të drejtën e autorit dhe markat tregtare. Riprodhimi, ndryshimi, shpërndarja ose ripërdorimi, i plotë ose i pjesshëm, pa leje me shkrim ndalohen.',
   'Markat, emrat dhe logot e palëve të treta që përmenden u përkasin pronarëve të tyre dhe përdoren vetëm për qëllime përshkruese.')),
 ('Imazhet, shembujt dhe shifrat', p('Imazhet dhe videot në seksionin Danova Real Estate janë <b>ilustruese, të krijuara me inteligjencë artificiale</b> për të treguar llojin e punimeve: nuk paraqesin kantiere, prona apo klientë realë. Shembujt, afatet dhe shifrat e paraqitura u referohen situatave tipike dhe nuk përbëjnë premtim për rezultat të njëjtë në projekte të tjera.')),
 ('Përmbajtja dhe disponueshmëria', p('Përmbajtja ka karakter informues dhe promovues dhe mund të ndryshohet ose të hiqet në çdo kohë pa njoftim. Edhe pse kujdesemi për saktësinë, nuk garantojmë që informacioni është i plotë ose gjithmonë i përditësuar.',
   'Përpiqemi ta mbajmë faqen të arritshme, por nuk garantojmë shërbim të pandërprerë: qasja mund të pezullohet për mirëmbajtje, përditësime ose për arsye jashtë kontrollit tonë.')),
 ('Kërkesat për ofertë dhe lidhja e kontratës', p('Informacionet për shërbimet, afatet dhe metodat e publikuara në faqe janë orientuese dhe <b>nuk përbëjnë ofertë publike</b> sipas nenit 1336 të Kodit Civil italian. Dërgimi i një kërkese përmes formularit ose me email nuk e detyron asnjërën palë.',
   'Marrëdhënia kontraktore lind vetëm me pranimin me shkrim të një oferte të caktuar, e cila përcakton objektin, afatet, çmimin dhe kushtet e punimeve dhe ka përparësi ndaj asaj që thuhet në faqe.')),
 ('Kufizimi i përgjegjësisë', p('Në masën e lejuar nga ligji, Danova Tech nuk mban përgjegjësi për dëmet e tërthorta ose pasuese që rrjedhin nga përdorimi ose pamundësia e përdorimit të faqes, nga ndërprerjet e shërbimit ose nga përmbajtja e faqeve të palëve të treta ku çojnë lidhjet. Asgjë në këto kushte nuk e kufizon përgjegjësinë për dashje, pakujdesi të rëndë ose në rastet kur ligji nuk lejon përjashtime.')),
 ('Lidhjet drejt faqeve të palëve të treta', p('Faqja mund të përmbajë lidhje drejt burimeve të jashtme, të ofruara për lehtësinë tuaj. Nuk i kontrollojmë këto faqe dhe nuk mbajmë përgjegjësi për përmbajtjen, politikat ose shërbimet e tyre.')),
 ('Mbrojtja e të dhënave personale', p('Përpunimi i të dhënave personale të mbledhura përmes faqes përshkruhet në <a href="/sq/privatesia/">Politikën e privatësisë</a> dhe në <a href="/sq/politika-e-cookie-ve/">Politikën e cookie-ve</a>, të cilat janë pjesë përbërëse e këtyre kushteve.')),
 ('Ligji i zbatueshëm dhe gjykata kompetente', p('Këto kushte rregullohen nga ligji italian. Për mosmarrëveshjet me përdoruesit që janë konsumatorë, kompetente është gjykata e vendbanimit ose e vendqëndrimit të konsumatorit. Në të gjitha rastet e tjera, kompetente është gjykata e vendit ku ka selinë pronari i faqes.')),
 ('Ndryshimet e këtyre kushteve', p('Këto kushte mund të përditësohen në çdo kohë. Versioni i zbatueshëm është ai i publikuar në këtë faqe në momentin e hyrjes, me datën e përditësimit të fundit.')),
 ])

# ------------------------------------------------------------------ HINDI (29/10/2026)
T['hi'] = {}
T['hi']['privacy'] = dict(
 title='गोपनीयता नीति — Danova Real Estate', h1='गोपनीयता नीति',
 desc='Danova Tech और Danova Real Estate साइट से मिले व्यक्तिगत डेटा को कैसे संसाधित करते हैं: नियंत्रक, उद्देश्य, संग्रहण अवधि और GDPR के तहत आपके अधिकार।',
 lead='Danova Tech, जिसमें Danova Real Estate डिवीज़न शामिल है, इस साइट से एकत्र व्यक्तिगत डेटा को कैसे संसाधित करता है: नियंत्रक, उद्देश्य, क़ानूनी आधार, संग्रहण अवधि, प्राप्तकर्ता और GDPR के तहत आप अपने अधिकारों का उपयोग कैसे कर सकते हैं।',
 sec=[
 ('डेटा नियंत्रक', p('<b>Danova Tech</b> — P.IVA (इतालवी टैक्स नंबर) 05369890263 — पंजीकृत कार्यालय Via Rigole 48, 31040 Rigole di Mansuè (TV), इटली। ईमेल: ' + MAIL,
   'Danova Real Estate, Danova Tech का कंस्ट्रक्शन और रेनोवेशन डिवीज़न है: डेटा नियंत्रक वही है। Danova Tech इस साइट से एकत्र व्यक्तिगत डेटा का नियंत्रक है, विनियमन (EU) 2016/679 (GDPR) और इतालवी क़ानून (विधायी डिक्री 196/2003, विधायी डिक्री 101/2018 द्वारा संशोधित) के अनुसार। डेटा संरक्षण अधिकारी (DPO) नियुक्त नहीं किया गया है, क्योंकि उसे अनिवार्य बनाने वाली क़ानूनी शर्तें लागू नहीं होतीं।')),
 ('हम कौन-सा डेटा संसाधित करते हैं', p('हम केवल वह डेटा संसाधित करते हैं जो आप स्वेच्छा से देते हैं और साइट चलाने के लिए ज़रूरी तकनीकी डेटा।') + ul(
   'फ़ॉर्म में भरा गया <b>संपर्क डेटा</b>: नाम और कंपनी, ईमेल, फ़ोन, संदेश का पाठ और, अगर आप बताएँ, काम शुरू करने की चाही गई अवधि।',
   'होस्टिंग सर्वर द्वारा अपने-आप दर्ज <b>ब्राउज़िंग डेटा</b>: IP पता, ब्राउज़र और ऑपरेटिंग सिस्टम, अनुरोध की तारीख़ और समय, देखे गए पेज। इनका उपयोग सुरक्षा, निदान और ट्रैफ़िक आँकड़ों के लिए समेकित रूप में होता है।')
   + p('साइट <b>प्रोफ़ाइलिंग कुकीज़ का उपयोग नहीं करती</b> और आगंतुकों की व्यावसायिक प्रोफ़ाइल नहीं बनाती।')),
 ('संपर्क फ़ॉर्म कैसे काम करता है', p('जब आप फ़ॉर्म भेजते हैं, तो डेटा <b>FormSubmit</b> (formsubmit.co) सेवा के ज़रिए भेजा जाता है, जो उसे ईमेल के रूप में ' + MAIL + ' इनबॉक्स में पहुँचाती है; वहाँ यह सामान्य व्यावसायिक पत्राचार की तरह रखा जाता है। अगर भेजना सफल न हो, तो साइट आपके डिवाइस पर ईमेल ऐप तैयार संदेश के साथ खोलती है, जिसे आप ख़ुद भेजते हैं।',
   'आप फ़ॉर्म इस्तेमाल किए बिना सीधे फ़ोन या WhatsApp से भी हमसे संपर्क कर सकते हैं।')),
 ('उद्देश्य और क़ानूनी आधार', ul(
   'जानकारी, साइट सर्वे और कोटेशन के अनुरोधों का जवाब और अनुबंध-पूर्व क़दम — GDPR अनुच्छेद 6(1)(b)।',
   'अनुबंध संबंध और सौंपे गए कामों का प्रबंधन — GDPR अनुच्छेद 6(1)(b)।',
   'कर, लेखा और अन्य क़ानूनी दायित्वों का पालन — GDPR अनुच्छेद 6(1)(c)।',
   'साइट की सुरक्षा और दुरुपयोग या घुसपैठ के प्रयासों की रोकथाम — वैध हित, GDPR अनुच्छेद 6(1)(f)।',
   'हमारी सेवाओं के बारे में प्रचार संदेश, केवल आपकी स्वतंत्र सहमति से, जिसे आप कभी भी वापस ले सकते हैं — GDPR अनुच्छेद 6(1)(a)।')),
 ('क्या डेटा देना अनिवार्य है?', p('फ़ॉर्म में अनिवार्य चिह्नित डेटा देना आपको जवाब देने के लिए ज़रूरी है: उसके बिना हम अनुरोध पर कार्रवाई नहीं कर सकते। बाक़ी डेटा देना वैकल्पिक है और हमारे जवाब पर असर नहीं डालता।')),
 ('हम डेटा किसके साथ साझा करते हैं', p('डेटा अधिकृत कर्मचारियों द्वारा संसाधित किया जा सकता है और हमारे सेवा प्रदाताओं को दिया जा सकता है, जिन्हें ज़रूरत होने पर GDPR अनुच्छेद 28 के तहत प्रोसेसर नियुक्त किया जाता है: साइट होस्टिंग प्रदाता, ईमेल और फ़ॉर्म सेवा प्रदाता, लेखा, कर और क़ानूनी सलाहकार, और क़ानून की माँग पर सार्वजनिक प्राधिकरण।',
   'काम करने के लिए सख़्ती से ज़रूरी डेटा (जैसे प्रॉपर्टी का पता और एक फ़ोन नंबर) आपकी साइट पर काम करने वाली कंपनियों और कारीगरों को दिया जा सकता है।',
   'डेटा <b>कभी प्रकाशित, व्यापार या बेचा नहीं जाता</b> किसी तीसरे पक्ष को व्यावसायिक उद्देश्यों के लिए।')),
 ('यूरोपीय संघ के बाहर स्थानांतरण', p('FormSubmit फ़ॉर्म सेवा और Cloudflare Web Analytics आँकड़ा सेवा यूरोपीय आर्थिक क्षेत्र के बाहर, संयुक्त राज्य अमेरिका सहित, स्थित सर्वरों पर डेटा संसाधित कर सकती हैं। इन स्थानांतरणों के लिए हम GDPR के अध्याय V में दी गई गारंटियों पर भरोसा करते हैं।',
   'साइट के फ़ॉन्ट, तस्वीरें और वीडियो इसी डोमेन पर होस्ट हैं: उन्हें लोड करने के लिए आपका ब्राउज़र Google या YouTube सर्वरों से संपर्क नहीं करता।')),
 ('हम डेटा कितने समय तक रखते हैं', ul(
   'संपर्क अनुरोध जिनके बाद अनुबंध नहीं हुआ: आख़िरी पत्राचार से <b>24 महीने</b>।',
   'अनुबंधों, बिलों और लेखा रिकॉर्ड से जुड़ा डेटा: इतालवी नागरिक और कर क़ानून के अनुसार <b>10 वर्ष</b>।',
   'सर्वर के तकनीकी लॉग: अधिकतम <b>12 महीने</b>, जब तक ग़ैरक़ानूनी गतिविधियों की जाँच के लिए ज़रूरी न हों।',
   'सहमति के आधार पर संसाधित डेटा: सहमति वापस लेने तक।')),
 ('आपके अधिकार', p('आप कभी भी GDPR अनुच्छेद 15–22 में दिए अधिकारों का उपयोग कर सकते हैं: अपने डेटा तक पहुँच, सुधार, मिटाना, प्रसंस्करण पर रोक, पोर्टेबिलिटी, प्रसंस्करण पर आपत्ति और दी गई किसी भी सहमति को वापस लेना।',
   'बस ' + MAIL + ' पर लिखें: हम अनुरोध मिलने के 30 दिनों के भीतर जवाब देते हैं। आपको इतालवी डेटा संरक्षण प्राधिकरण (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">garanteprivacy.it</a>) या, अगर आप EU में रहते हैं, अपने देश के पर्यवेक्षी प्राधिकरण के पास शिकायत करने का भी अधिकार है।')),
 ('डेटा सुरक्षा', p('हम डेटा को अनधिकृत पहुँच, हानि या प्रकटीकरण से बचाने के लिए उचित तकनीकी और संगठनात्मक उपाय अपनाते हैं: एन्क्रिप्टेड HTTPS कनेक्शन, मज़बूत पासवर्ड और दो-चरणीय प्रमाणीकरण वाले ईमेल इनबॉक्स, केवल ज़रूरी कर्मचारियों तक सीमित पहुँच और नियमित बैकअप।')),
 ('नाबालिग', p('हमारी सेवाएँ वयस्कों, कंपनियों और संगठनों के लिए हैं। हम जानबूझकर 16 वर्ष से कम उम्र के बच्चों का व्यक्तिगत डेटा एकत्र नहीं करते। अगर आपको लगता है कि किसी नाबालिग ने हमें डेटा दिया है, तो हमें लिखें और हम उसे तुरंत मिटा देंगे।')),
 ('इस सूचना में बदलाव', p('यह सूचना क़ानून या हमारी सेवाओं में बदलाव दर्शाने के लिए अपडेट की जा सकती है। लागू संस्करण हमेशा इस पेज पर प्रकाशित, आख़िरी अपडेट की तारीख़ वाला संस्करण है।')),
 ])
T['hi']['cookie'] = dict(
 title='कुकी नीति — Danova Real Estate', h1='कुकी नीति',
 desc='Danova Tech और Danova Real Estate की साइट कौन-सी कुकीज़ इस्तेमाल करती है: कोई प्रोफ़ाइलिंग या विज्ञापन कुकी नहीं, बिना कुकी के समेकित आँकड़े।',
 lead='Danova Tech और Danova Real Estate की साइट कौन-सी कुकीज़ इस्तेमाल करती है, वे किस काम की हैं और ब्राउज़र से उन्हें कैसे नियंत्रित करें। कोई प्रोफ़ाइलिंग कुकी नहीं, कोई विज्ञापन ट्रैकिंग नहीं।',
 sec=[
 ('कुकीज़ क्या हैं', p('कुकीज़ छोटी टेक्स्ट फ़ाइलें हैं जिन्हें वेबसाइटें जानकारी याद रखने के लिए आगंतुक के डिवाइस पर सहेजती हैं: पसंद, लॉगिन सत्र या, प्रोफ़ाइलिंग कुकीज़ के मामले में, विज्ञापन के लिए इस्तेमाल होने वाला ब्राउज़िंग व्यवहार। मिलती-जुलती तकनीकें हैं ट्रैकिंग पिक्सेल, लोकल स्टोरेज और ब्राउज़र फ़िंगरप्रिंटिंग।')),
 ('इस साइट द्वारा उपयोग की जाने वाली कुकीज़', p('यह साइट <b>कोई प्रोफ़ाइलिंग, एनालिटिक्स या मार्केटिंग कुकी नहीं लगाती</b> और आगंतुकों के व्यवहार को ट्रैक करने वाले टूल का उपयोग नहीं करती। Google Analytics, Meta Pixel या ऐसी कोई तकनीक नहीं है।',
   'विज़िट <b>Cloudflare Web Analytics</b> से गिनी जाती हैं, जो समेकित आँकड़ों का टूल है: यह कुकी नहीं लगाता, आपके डिवाइस पर कुछ नहीं सहेजता और प्रोफ़ाइल नहीं बनाता।',
   'साइट आपके डिवाइस पर अपनी तकनीकी कुकीज़ भी नहीं सहेजती। इसलिए पहले से सहमति वाले बैनर की ज़रूरत नहीं है।')),
 ('तृतीय-पक्ष सेवाएँ', p('साइट पर इस्तेमाल फ़ॉन्ट (Sora, Inter, JetBrains Mono), तस्वीरें और वीडियो <b>इसी डोमेन पर होस्ट</b> हैं: उन्हें डाउनलोड करने के लिए आपका ब्राउज़र बाहरी सर्वरों से संपर्क नहीं करता।',
   'विज़िट के आँकड़े <b>Cloudflare Web Analytics</b> (Cloudflare, Inc.) से एकत्र होते हैं: समेकित रूप में देखा गया पेज, ट्रैफ़िक का स्रोत, डिवाइस का प्रकार और देश दर्ज होते हैं। किसी भी बाहरी सर्वर अनुरोध की तरह, जवाब देने के लिए IP पता Cloudflare को जाता है। Cloudflare की सूचना: <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">cloudflare.com/privacypolicy</a>। अगर आप ब्राउज़र एक्सटेंशन से स्क्रिप्ट ब्लॉक करें, तो भी साइट वैसे ही चलती है।',
   'जब आप संपर्क फ़ॉर्म भेजते हैं, तो डेटा <b>FormSubmit</b> (formsubmit.co) सेवा को जाता है, जो उसे हमें ईमेल से पहुँचाती है।')),
 ('लिंक और बाहरी सामग्री', p('साइट में तृतीय-पक्ष प्लेटफ़ॉर्म (जैसे WhatsApp, Instagram, Facebook और TikTok) के लिंक हैं। इन लिंक पर जाकर आप ऐसी साइटों पर पहुँचते हैं जिनकी अपनी कुकी नीतियाँ हैं, जिन पर हमारा नियंत्रण नहीं है; हम उन्हें पढ़ने की सलाह देते हैं।')),
 ('ब्राउज़र से कुकीज़ का प्रबंधन', p('आप कभी भी अपने ब्राउज़र को किसी भी साइट की कुकीज़ ब्लॉक करने या मिटाने के लिए सेट कर सकते हैं। निर्देश ब्राउज़र की सेटिंग्स में मिलते हैं:') + ul(
   '<b>Chrome</b> — सेटिंग्स › गोपनीयता और सुरक्षा › कुकीज़।', '<b>Safari</b> — सेटिंग्स › गोपनीयता › वेबसाइट डेटा प्रबंधित करें।',
   '<b>Firefox</b> — सेटिंग्स › गोपनीयता और सुरक्षा › कुकीज़ और साइट डेटा।', '<b>Edge</b> — सेटिंग्स › कुकीज़ और साइट अनुमतियाँ।')
   + p('कुकीज़ ब्लॉक करने से आप इस साइट को ब्राउज़ करने से नहीं रुकते।')),
 ('अपडेट', p('अगर भविष्य में हम मापन या मार्केटिंग टूल जोड़ेंगे, तो इतालवी डेटा संरक्षण प्राधिकरण के दिशानिर्देशों के अनुसार पहले से सहमति वाला बैनर सक्रिय करेंगे और ये टूल सक्रिय होने से पहले इस पेज को अपडेट करेंगे।')),
 ])
T['hi']['termini'] = dict(
 title='उपयोग की शर्तें — Danova Real Estate', h1='उपयोग की शर्तें',
 desc='Danova Tech और Danova Real Estate साइट की उपयोग की शर्तें: बौद्धिक संपदा, कोटेशन, सांकेतिक तस्वीरें, दायित्व, लागू क़ानून।',
 lead='Danova Tech साइट और Danova Real Estate डिवीज़न की उपयोग की शर्तें: सामग्री का स्वामित्व, अनुमत उपयोग, कोटेशन, दायित्व की सीमा, लागू क़ानून और सक्षम न्यायालय।',
 sec=[
 ('उद्देश्य और साइट का स्वामी', p('यह साइट <b>Danova Tech</b> — P.IVA 05369890263 — द्वारा संचालित है, पंजीकृत कार्यालय Via Rigole 48, 31040 Rigole di Mansuè (TV), इटली, ईमेल ' + MAIL + '। Danova Real Estate, Danova Tech का कंस्ट्रक्शन और रेनोवेशन डिवीज़न है। ये शर्तें साइट तक पहुँच और उसकी सामग्री के उपयोग को नियंत्रित करती हैं।')),
 ('स्वीकृति', p('साइट ब्राउज़ करके आप इन शर्तों को पूरी तरह स्वीकार करते हैं। अगर आप सहमत नहीं हैं, तो कृपया साइट का उपयोग न करें।')),
 ('अनुमत उपयोग', p('आप जानकारी के लिए और हमसे संपर्क करने के लिए साइट देख और उपयोग कर सकते हैं। मना है: साइट का ग़ैरक़ानूनी या सद्भाव के विरुद्ध उपयोग, सिस्टम या आरक्षित क्षेत्रों तक अनधिकृत पहुँच का प्रयास, स्वचालित और बड़े पैमाने पर सामग्री निकालना, दुर्भावनापूर्ण कोड डालना या साइट के संचालन या सुरक्षा को नुक़सान पहुँचाने वाला कोई भी काम।')),
 ('बौद्धिक संपदा', p('कोड, ग्राफ़िक्स, पाठ, लेआउट, संसाधित तस्वीरें, और <b>Danova Tech</b> व <b>Danova Real Estate</b> के नाम और लोगो Danova Tech या उसके लाइसेंसदाताओं के हैं और कॉपीराइट व ट्रेडमार्क क़ानूनों से सुरक्षित हैं। लिखित अनुमति के बिना पूरी या आंशिक प्रतिलिपि, संशोधन, वितरण या पुनः उपयोग मना है।',
   'उल्लिखित तृतीय पक्षों के ट्रेडमार्क, नाम और लोगो उनके मालिकों के हैं और केवल वर्णन के लिए उपयोग किए गए हैं।')),
 ('तस्वीरें, उदाहरण और आँकड़े', p('Danova Real Estate अनुभाग की तस्वीरें और वीडियो काम के प्रकार दिखाने के लिए <b>आर्टिफ़िशियल इंटेलिजेंस से बनाई गई सांकेतिक सामग्री</b> हैं: वे असली साइटों, प्रॉपर्टी या ग्राहकों को नहीं दर्शातीं। दिए गए उदाहरण, समय-सीमाएँ और आँकड़े सामान्य स्थितियों से संबंधित हैं और अन्य प्रोजेक्ट के लिए परिणाम का वादा नहीं हैं।')),
 ('सामग्री और उपलब्धता', p('सामग्री सूचनात्मक और प्रचार प्रकृति की है और बिना सूचना के कभी भी बदली या हटाई जा सकती है। हम सही रखने का ध्यान रखते हैं, पर यह गारंटी नहीं देते कि जानकारी पूरी या हमेशा अद्यतन है।',
   'हम साइट को उपलब्ध रखने का प्रयास करते हैं, पर निर्बाध संचालन की गारंटी नहीं देते: रखरखाव, अपडेट या हमारे नियंत्रण से बाहर के कारणों से पहुँच रुक सकती है।')),
 ('कोटेशन के अनुरोध और अनुबंध', p('साइट पर प्रकाशित सेवाओं, समय-सीमाओं और तरीक़ों की जानकारी सांकेतिक है और इतालवी नागरिक संहिता के अनुच्छेद 1336 के अर्थ में <b>सार्वजनिक प्रस्ताव नहीं है</b>। फ़ॉर्म या ईमेल से अनुरोध भेजना किसी भी पक्ष को बाध्य नहीं करता।',
   'अनुबंध संबंध केवल किसी विशिष्ट कोटेशन की लिखित स्वीकृति से बनता है, जो काम का विषय, समय-सीमा, कीमत और शर्तें तय करता है और साइट पर कही गई बातों से ऊपर होता है।')),
 ('दायित्व की सीमा', p('क़ानून द्वारा अनुमत सीमा तक, Danova Tech साइट के उपयोग या उपयोग न कर पाने, सेवा में रुकावट या लिंक की गई तृतीय-पक्ष साइटों की सामग्री से होने वाली अप्रत्यक्ष या परिणामी क्षति के लिए उत्तरदायी नहीं है। इन शर्तों में कुछ भी जानबूझकर किए गए कृत्य, घोर लापरवाही या उन मामलों में दायित्व को सीमित नहीं करता जहाँ क़ानून छूट की अनुमति नहीं देता।')),
 ('तृतीय-पक्ष साइटों के लिंक', p('साइट में आपकी सुविधा के लिए बाहरी संसाधनों के लिंक हो सकते हैं। इन साइटों पर हमारा नियंत्रण नहीं है और हम उनकी सामग्री, नीतियों या सेवाओं के लिए उत्तरदायी नहीं हैं।')),
 ('व्यक्तिगत डेटा की सुरक्षा', p('साइट से एकत्र व्यक्तिगत डेटा का प्रसंस्करण <a href="/hi/privacy/">गोपनीयता नीति</a> और <a href="/hi/cookie-policy/">कुकी नीति</a> में वर्णित है, जो इन शर्तों का अभिन्न अंग हैं।')),
 ('लागू क़ानून और सक्षम न्यायालय', p('ये शर्तें इतालवी क़ानून द्वारा शासित हैं। उपभोक्ता उपयोगकर्ताओं के साथ विवादों के लिए उपभोक्ता के निवास या आवास का न्यायालय सक्षम है। अन्य सभी मामलों में साइट स्वामी के पंजीकृत कार्यालय का न्यायालय सक्षम है।')),
 ('इन शर्तों में बदलाव', p('ये शर्तें कभी भी अपडेट की जा सकती हैं। लागू संस्करण वह है जो पहुँच के समय इस पेज पर प्रकाशित है, आख़िरी अपडेट की तारीख़ के साथ।')),
 ])

UI = {'ro': dict(home='Acasă', eyebrow='Informații juridice', upd='Ultima actualizare: octombrie 2026', rel='Pagini conexe', hreal='Danova Real Estate', loc='ro_RO'),
      'sq': dict(home='Kreu', eyebrow='Informacion ligjor', upd='Përditësuar më: tetor 2026', rel='Faqe të lidhura', hreal='Danova Real Estate', loc='sq_AL'),
      'hi': dict(home='होम', eyebrow='क़ानूनी जानकारी', upd='आख़िरी अपडेट: अक्टूबर 2026', rel='संबंधित पेज', hreal='Danova Real Estate', loc='hi_IN')}
HL = ['it', 'en', 'de', 'ro', 'sq', 'hi']


def hreflang(k):
    a = ALT[k]
    return ''.join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (l, SITE, a[l]) for l in HL) + '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (SITE, a['it'])


def build(lang, k):
    d = T[lang][k]; ui = UI[lang]; url = ALT[k][lang]; home = '/%s/real-estate/' % lang
    s = open(os.path.join(R, lang, 'real-estate', 'index.html'), encoding='utf-8').read()
    e = html.escape
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % e(d['title']), s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % e(d['desc']), s, count=1)
    s = re.sub(r'<link rel="preload" as="image"[^>]*>\n?', '', s)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s%s">' % (SITE, url), s, count=1)
    s = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n?', '', s)
    s = s.replace('<link rel="canonical" href="%s%s">' % (SITE, url), '<link rel="canonical" href="%s%s">\n%s' % (SITE, url, hreflang(k).rstrip('\n')), 1)
    for prop, val in (('og:url', SITE + url), ('og:title', d['title']), ('og:description', d['desc']), ('og:image:alt', d['title'])):
        s = re.sub(r'<meta property="%s" content="[^"]*">' % prop, '<meta property="%s" content="%s">' % (prop, e(val)), s, count=1)
    s = re.sub(r'<meta name="twitter:title" content="[^"]*">', '<meta name="twitter:title" content="%s">' % e(d['title']), s, count=1)
    s = re.sub(r'<meta name="twitter:description" content="[^"]*">', '<meta name="twitter:description" content="%s">' % e(d['desc']), s, count=1)
    s = s.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">')
    g = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": SITE + url + "#webpage", "url": SITE + url, "name": d['h1'], "description": d['desc'], "inLanguage": lang,
         "dateModified": "2026-10-24", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#organization"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui['hreal'], "item": SITE + home},
            {"@type": "ListItem", "position": 2, "name": d['h1'], "item": SITE + url}]}]}
    s = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">\n%s\n</script>' % json.dumps(g, ensure_ascii=False, indent=2), s, count=1, flags=re.S)
    rel = ''.join('<a href="%s">%s</a>' % (ALT[x][lang], T[lang][x]['h1']) for x in ('privacy', 'cookie', 'termini') if x != k) + '<a href="%s">%s</a>' % (home, ui['hreal'])
    main = ('<main id="main">\n<div class="wrap pg-crumbs">\n  <a href="%s">%s</a><em>/</em>%s\n</div>\n'
            '<section class="pg-hero"><div class="wrap"><div class="eyebrow mono">%s</div><h1>%s</h1><p class="lead">%s</p><p class="lead"><small>%s</small></p></div></section>\n'
            % (home, ui['hreal'], e(d['h1']), ui['eyebrow'], e(d['h1']), e(d['lead']), ui['upd'])
            + ''.join('<section><div class="wrap"><div class="sec-head"><h2 class="title">%s</h2></div><div class="pg-testo">%s</div></div></section>\n' % (e(h), b) for h, b in d['sec'])
            + '<section><div class="wrap"><div class="sec-head"><h2 class="title">%s</h2></div><div class="pg-altri">%s</div></div></section>\n</main>' % (ui['rel'], rel))
    s = re.sub(r'<main id="main">.*?</main>', lambda m: main, s, count=1, flags=re.S)
    s = re.sub(r'<a href="[^"]*" hreflang="(it|en|de|ro|sq|hi)"', lambda m: '<a href="%s" hreflang="%s"' % (ALT[k][m.group(1)], m.group(1)), s)
    out = os.path.join(R, url.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    old = open(out, encoding='utf-8').read() if os.path.exists(out) else ''
    if old != s:
        open(out, 'w', encoding='utf-8').write(s)
    return url


def reciproci():
    """aggiunge ro/sq agli hreflang delle pagine legali IT/EN/DE (gia' esistenti)"""
    n = 0
    for k, a in ALT.items():
        for l in ('it', 'en', 'de'):
            f = os.path.join(R, a[l].strip('/'), 'index.html')
            if not os.path.exists(f): continue
            s = open(f, encoding='utf-8').read(); s0 = s
            for x in ('ro', 'sq', 'hi'):
                tag = '<link rel="alternate" hreflang="%s" href="%s%s">' % (x, SITE, a[x])
                if tag in s: continue
                m = list(re.finditer(r'<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n?', s))
                if m:
                    s = s[:m[-1].end()] + ('' if s[m[-1].end() - 1] == '\n' else '\n') + tag + '\n' + s[m[-1].end():]
                else:
                    s = re.sub(r'(<link rel="canonical" href="[^"]*">)', lambda mm: mm.group(1) + '\n' + tag, s, count=1)
            if s != s0:
                open(f, 'w', encoding='utf-8').write(s); n += 1
    return n


if __name__ == '__main__':
    fatte = [build(l, k) for l in ('ro', 'sq', 'hi') for k in ('privacy', 'cookie', 'termini')]
    print('pagine legali RO/SQ/HI:', len(fatte), '| hreflang aggiunti alle pagine IT/EN/DE:', reciproci())
