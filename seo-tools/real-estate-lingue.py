# -*- coding: utf-8 -*-
"""24/10/2026 - Danova Real Estate multilingua: mappa URL (IT -> en/de/ro/sq/hr), configurazione lingue,
   etichette dell'interfaccia, traduzione della cornice (menu, footer) per ro/sq/hr costruite sul donatore inglese.
   La versione hr e' scritta in croato standard comprensibile in Bosnia, Serbia e Montenegro (hreflang hr, bs, sr-Latn)."""
LINGUE = ['it', 'en', 'de', 'ro', 'sq', 'hi']  # 'hr' (BHS) in pausa: riattivare aggiungendolo qui
CFG = {
 'it': dict(loc='it-IT', og='it_IT', home='/', donor='quanto-costa-un-sito-web/index.html', hl=['it'], lab='IT'),
 'en': dict(loc='en-GB', og='en_GB', home='/en/', donor='en/web-design-agency-uk/index.html', hl=['en'], lab='EN'),
 'de': dict(loc='de-DE', og='de_DE', home='/de/', donor='de/webagentur-muenchen/index.html', hl=['de'], lab='DE'),
 'ro': dict(loc='ro-RO', og='ro_RO', home='/ro/real-estate/', donor='en/web-design-agency-uk/index.html', hl=['ro'], lab='RO'),
 'sq': dict(loc='sq-AL', og='sq_AL', home='/sq/real-estate/', donor='en/web-design-agency-uk/index.html', hl=['sq'], lab='SQ'),
 'hi': dict(loc='hi-IN', og='hi_IN', home='/hi/real-estate/', donor='en/web-design-agency-uk/index.html', hl=['hi'], lab='HI'),  # 29/10/2026
 'hr': dict(loc='hr-HR', og='hr_HR', home='/hr/real-estate/', donor='en/web-design-agency-uk/index.html', hl=['hr', 'bs', 'sr-Latn'], lab='BHS'),
}
S = {  # slug per lingua (en, de, ro, sq, hr): chiave = URL italiano
 '/real-estate/': ('real-estate', 'real-estate', 'real-estate', 'real-estate', 'real-estate'),
 '/ristrutturazioni-chiavi-in-mano/': ('turnkey-renovation', 'schluesselfertige-renovierung', 'renovari-la-cheie', 'rinovime-celes-ne-dore', 'renoviranje-kljuc-u-ruke'),
 '/ristrutturazione-appartamenti-e-case/': ('apartment-house-renovation', 'wohnung-haus-renovieren', 'renovare-apartamente-case', 'rinovim-apartamentesh-shtepish', 'renoviranje-stanova-i-kuca'),
 '/ristrutturazione-bagno/': ('bathroom-renovation', 'badsanierung', 'renovare-baie', 'rinovim-banjo', 'renoviranje-kupaonice'),
 '/ristrutturazione-negozi-uffici-ristoranti/': ('shop-office-restaurant-renovation', 'umbau-geschaefte-bueros-restaurants', 'renovare-magazine-birouri-restaurante', 'rinovim-dyqanesh-zyrash-restorantesh', 'renoviranje-trgovina-ureda-restorana'),
 '/ristrutturazione-hotel/': ('hotel-renovation', 'hotelrenovierung', 'renovare-hoteluri', 'rinovim-hotelesh', 'renoviranje-hotela'),
 '/ristrutturazione-condomini-e-capannoni/': ('apartment-building-industrial-renovation', 'sanierung-mehrfamilienhaus-gewerbehalle', 'renovare-blocuri-hale', 'rinovim-pallatesh-kapanonesh', 'obnova-zgrada-i-hala'),
 '/general-contractor/': ('general-contractor-italy', 'generalunternehmer', 'antreprenor-general', 'kontraktor-i-pergjithshem', 'generalni-izvodjac'),
 '/hotel-chiavi-in-mano/': ('turnkey-hotel', 'hotel-schluesselfertig', 'hotel-la-cheie', 'hotel-celes-ne-dore', 'hotel-kljuc-u-ruke'),
 '/impresa-edile-per-architetti/': ('building-contractor-for-architects', 'bauunternehmen-fuer-architekten', 'firma-constructii-pentru-arhitecti', 'kompani-ndertimi-per-arkitekte', 'gradjevinska-tvrtka-za-arhitekte'),
 '/pareti-divisorie/': ('room-partition-walls', 'trennwaende', 'pereti-despartitori', 'mure-ndarese', 'pregradni-zidovi'),
 '/cappotto-termico/': ('external-wall-insulation', 'waermedaemmung-fassade', 'izolatie-termica-exterioara', 'termoizolim-i-jashtem', 'toplinska-izolacija-fasade'),
 '/facciate-ventilate-e-rifacimento-facciate/': ('facade-renovation', 'fassadensanierung', 'renovare-fatade', 'rinovim-fasadash', 'obnova-fasada'),
 '/porte-interne-e-blindate/': ('interior-and-security-doors', 'innentueren-sicherheitstueren', 'usi-interioare-blindate', 'dyer-te-brendshme-te-blinduara', 'unutarnja-i-sigurnosna-vrata'),
 '/porte-rei-tagliafuoco/': ('fire-rated-doors', 'brandschutztueren', 'usi-rezistente-la-foc', 'dyer-kunder-zjarrit', 'protupozarna-vrata'),
 '/cartongesso-e-controsoffitti/': ('drywall-suspended-ceilings', 'trockenbau-abgehaengte-decken', 'rigips-tavane-false', 'kartongips-tavane-te-varura', 'gips-spusteni-stropovi'),
 '/rifacimento-tetto/': ('roof-replacement', 'dachsanierung', 'refacere-acoperis', 'rinovim-catie', 'sanacija-krova'),
 '/isolamento-sottotetto/': ('loft-insulation', 'dachbodendaemmung', 'izolare-pod-mansarda', 'izolim-papafingo', 'izolacija-potkrovlja'),
 '/pavimentazioni-esterne/': ('outdoor-paving', 'terrassen-aussenbelaege', 'pavaje-exterioare', 'shtrime-te-jashtme', 'vanjsko-poplocenje'),
 '/pavimenti-e-serramenti/': ('flooring-and-windows', 'boeden-und-fenster', 'pardoseli-si-tamplarie', 'dysheme-dhe-dritare', 'podovi-i-prozori'),
 '/arredo-hotel-contract/': ('hotel-contract-furniture', 'hotelmoebel-objekteinrichtung', 'mobilier-hotelier', 'mobilim-hotelesh', 'namjestaj-za-hotele'),
 '/mobili-su-misura/': ('custom-made-furniture', 'massmoebel', 'mobila-la-comanda', 'mobilje-me-porosi', 'namjestaj-po-mjeri'),
 '/progettazione-e-render-3d/': ('interior-design-3d-rendering', 'planung-3d-visualisierung', 'proiectare-randari-3d', 'projektim-render-3d', 'projektiranje-3d-vizualizacije'),
 '/pratiche-edilizie-cila-scia/': ('building-permits-italy', 'baugenehmigung-italien', 'autorizatii-constructie-italia', 'leje-ndertimi-itali', 'gradjevinske-dozvole-italija'),
 '/bonus-ristrutturazione-2026/': ('italy-renovation-tax-bonus-2026', 'italien-renovierungsbonus-2026', 'bonus-renovare-italia-2026', 'bonus-rinovimi-itali-2026', 'bonus-za-renoviranje-italija-2026'),
 '/guide/come-scegliere-impresa-ristrutturazione/': ('how-to-choose-a-renovation-company', 'renovierungsfirma-auswaehlen', 'cum-alegi-firma-de-renovari', 'si-te-zgjedhesh-kompanine-e-rinovimit', 'kako-odabrati-firmu-za-renoviranje'),
 '/guide/cila-o-scia/': ('cila-or-scia-italy', 'cila-oder-scia', 'cila-sau-scia', 'cila-apo-scia', 'cila-ili-scia'),
 '/guide/ristrutturare-un-hotel/': ('how-to-renovate-a-hotel', 'hotel-renovieren-zeitplan', 'cum-renovezi-un-hotel', 'si-te-rinovosh-nje-hotel', 'kako-renovirati-hotel'),
 '/guide/quando-conviene-il-cappotto-termico/': ('is-external-insulation-worth-it', 'lohnt-sich-waermedaemmung', 'merita-izolatia-termica', 'a-ia-vlen-termoizolimi', 'isplati-li-se-toplinska-izolacija'),
 '/guide/quanto-costa-ristrutturare-casa/': ('renovation-cost-italy', 'renovierungskosten-italien', 'cost-renovare-casa-italia', 'kosto-rinovimi-shtepie-itali', 'troskovi-renoviranja'),
 '/guide/come-rifare-il-bagno/': ('bathroom-renovation-guide', 'badsanierung-ratgeber', 'ghid-renovare-baie', 'udhezues-rinovim-banjoje', 'vodic-renoviranje-kupaonice'),
 '/guide/porte-rei-negli-hotel/': ('fire-doors-in-hotels', 'brandschutztueren-im-hotel', 'usi-rezistente-la-foc-in-hoteluri', 'dyer-kunder-zjarrit-ne-hotele', 'protupozarna-vrata-u-hotelima'),
}
CITTA = ['treviso', 'oderzo', 'conegliano', 'motta-di-livenza', 'castelfranco-veneto', 'montebelluna', 'venezia', 'mestre', 'san-dona-di-piave',
         'portogruaro', 'padova', 'vicenza', 'verona', 'pordenone', 'udine', 'sacile']
import os
import importlib.util as _iuN
_spN = _iuN.spec_from_file_location('recn', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real-estate-citta-nuove.py'))
_CN = _iuN.module_from_spec(_spN); _spN.loader.exec_module(_CN)  # 26/10/2026: nuove citta
CITTA = CITTA + _CN.SLUGS
GC = ['treviso', 'venezia', 'padova', 'vicenza', 'verona', 'pordenone', 'udine']
ZONE = ['jesolo', 'caorle', 'bibione', 'cavallino-treporti', 'sottomarina', 'lignano', 'grado', 'cortina', 'dolomiti', 'lago-di-garda', 'venezia', 'verona']
for _c in CITTA: S['/ristrutturazioni-%s/' % _c] = tuple(p + _c for p in ('renovation-', 'renovierung-', 'renovari-', 'rinovime-', 'renoviranje-'))
for _c in GC: S['/general-contractor-%s/' % _c] = tuple(p + _c for p in ('general-contractor-', 'generalunternehmer-', 'antreprenor-general-', 'kontraktor-', 'generalni-izvodjac-'))
for _c in ZONE: S['/arredo-hotel-%s/' % _c] = tuple(p + _c for p in ('hotel-furniture-', 'hotelmoebel-', 'mobilier-hotel-', 'mobilim-hoteli-', 'namjestaj-hotel-'))

ORD = ['en', 'de', 'ro', 'sq', 'hr']   # ordine degli slug nelle tuple di S (indipendente da LINGUE)
def url(key, lang):
    if lang == 'it': return key
    if lang == 'hi': return '/hi/%s/' % S[key][0]   # 29/10/2026: l'hindi usa gli slug inglesi (URL in caratteri latini)
    return '/%s/%s/' % (lang, S[key][ORD.index(lang)])
def alt(key): return {l: url(key, l) for l in LINGUE}

# pagine non Real Estate a cui i testi tradotti possono rimandare
EXT = {'video': {'en': '/en/promotional-video-production/', 'de': '/de/werbevideos-erstellen-lassen/'},
       'servizi': {'en': '/en/services/', 'de': '/de/leistungen/'},
       'sito': {'en': '/en/small-business-web-design/', 'de': '/de/webagentur-deutschland/'},
       'software': {'en': '/en/custom-erp-crm-development-usa/', 'de': '/de/individualsoftware-deutschland/'}}
def ext(k, lang): return EXT[k].get(lang, EXT[k]['en'])

NOMI = {  # nomi di citta' e zone tradotti (dove cambiano)
 'Venezia': {'en': 'Venice', 'de': 'Venedig', 'ro': 'Veneția', 'sq': 'Venecia', 'hr': 'Venecija'},
 'Padova': {'en': 'Padua', 'de': 'Padua'},
 'Trieste': {'de': 'Triest', 'hr': 'Trst'},
 'Lago di Garda': {'en': 'Lake Garda', 'de': 'Gardasee', 'ro': 'Lacul Garda', 'sq': 'Liqeni i Gardës', 'hr': 'Gardsko jezero'},
 'Dolomiti bellunesi': {'en': 'Belluno Dolomites', 'de': 'Belluneser Dolomiten', 'ro': 'Dolomiții din Belluno', 'sq': 'Dolomitet e Bellunos', 'hr': 'Dolomiti Belluna'},
 'Sottomarina e Chioggia': {'en': 'Sottomarina and Chioggia', 'de': 'Sottomarina und Chioggia', 'ro': 'Sottomarina și Chioggia', 'sq': 'Sottomarina dhe Chioggia', 'hr': 'Sottomarina i Chioggia'},
}
for _n, _v in NOMI.items():   # 29/10/2026: in hindi i nomi di luogo restano in caratteri latini, come in inglese
    if 'en' in _v: _v.setdefault('hi', _v['en'])
NOMI['Sottomarina e Chioggia']['hi'] = 'Sottomarina और Chioggia'
def nome(n, lang): return NOMI.get(n, {}).get(lang, n)

UI = {
 'it': dict(prima='Prima', dopo='Dopo', cmp='Confronta prima e dopo', home='Home',
            nota='Immagini e video illustrativi creati con l’intelligenza artificiale per mostrare le lavorazioni: non ritraggono cantieri o clienti reali.',
            badges=['Veneto e Friuli', 'Sopralluogo gratuito', 'Prezzo bloccato', 'Unico referente']),
 'en': dict(prima='Before', dopo='After', cmp='Compare before and after', home='Home',
            nota='Illustrative images and videos created with artificial intelligence to show the type of work: they do not depict real sites or clients.',
            badges=['Veneto & Friuli', 'Free site survey', 'Fixed price', 'Single point of contact']),
 'de': dict(prima='Vorher', dopo='Nachher', cmp='Vorher und nachher vergleichen', home='Startseite',
            nota='Illustrative Bilder und Videos, mit künstlicher Intelligenz erstellt, um die Arbeiten zu zeigen: Sie zeigen keine echten Baustellen oder Kunden.',
            badges=['Venetien & Friaul', 'Kostenlose Besichtigung', 'Festpreis', 'Ein Ansprechpartner']),
 'ro': dict(prima='Înainte', dopo='După', cmp='Comparați înainte și după', home='Acasă',
            nota='Imagini și videoclipuri ilustrative create cu inteligența artificială pentru a arăta lucrările: nu reprezintă șantiere sau clienți reali.',
            badges=['Veneto și Friuli', 'Inspecție gratuită', 'Preț blocat', 'Un singur responsabil']),
 'sq': dict(prima='Para', dopo='Pas', cmp='Krahasoni para dhe pas', home='Kreu',
            nota='Imazhe dhe video ilustruese të krijuara me inteligjencë artificiale për të treguar punimet: nuk paraqesin kantiere apo klientë realë.',
            badges=['Veneto dhe Friuli', 'Inspektim falas', 'Çmim i bllokuar', 'Një person kontakti']),
 'hr': dict(prima='Prije', dopo='Poslije', cmp='Usporedite prije i poslije', home='Početna',
            nota='Ilustrativne slike i videozapisi izrađeni umjetnom inteligencijom kako bi prikazali radove: ne prikazuju stvarna gradilišta ni klijente.',
            badges=['Veneto i Furlanija', 'Besplatan obilazak', 'Fiksna cijena', 'Jedna kontakt osoba']),
 'hi': dict(prima='पहले', dopo='बाद में', cmp='पहले और बाद की तुलना करें', home='होम',
            nota='काम के प्रकार दिखाने के लिए आर्टिफ़िशियल इंटेलिजेंस से बनाई गई सांकेतिक तस्वीरें और वीडियो: ये असली साइटों या ग्राहकों को नहीं दर्शाते।',
            badges=['Veneto और Friuli', 'मुफ़्त साइट सर्वे', 'फ़िक्स्ड प्राइस', 'एक ही ज़िम्मेदार व्यक्ति']),
}

# cornice del donatore inglese tradotta per ro / sq / hr
def _ch(skip, nav, talk, desc, h5, wh, off, terms, back):
    return [('<a href="#main" class="skip">Skip to content</a>', '<a href="#main" class="skip">%s</a>' % skip)] + \
           [('>%s</a>' % a, '>%s</a>' % b) for a, b in zip(['Services', 'Videos', 'Who we serve', 'Work', 'Process', 'Pricing', 'Contact'], nav)] + \
           [("<span class=\"lbl\">Let's talk</span>", '<span class="lbl">%s</span>' % talk),
            ('<p>Tech agency that designs, builds and grows the digital presence of businesses.</p>', '<p>%s</p>' % desc)] + \
           [('<h5>%s</h5>' % a, '<h5>%s</h5>' % b) for a, b in zip(['Services', 'Markets', 'Agency', 'Contact'], h5)] + \
           [('Warehouses:', wh), ('Offices:', off), ('>Terms of use<', '>%s<' % terms), ('>Back to home<', '>%s<' % back)]
CHROME = {
 'ro': _ch('Salt la conținut', ['Servicii', 'Video', 'Pentru cine', 'Lucrări', 'Proces', 'Prețuri', 'Contact'], 'Să vorbim',
           'Danova Real Estate: renovări la cheie, antreprenor general și mobilier hotelier în Veneto și Friuli. O divizie Danova Tech.',
           ['Servicii', 'Piețe', 'Agenția', 'Contact'], 'Depozite:', 'Birouri:', 'Termeni de utilizare', 'Pagina principală'),
 'sq': _ch('Kalo te përmbajtja', ['Shërbimet', 'Video', 'Për kë', 'Punimet', 'Procesi', 'Çmimet', 'Kontakt'], 'Të flasim',
           'Danova Real Estate: rinovime çelës në dorë, kontraktor i përgjithshëm dhe mobilim hotelesh në Veneto dhe Friuli. Një divizion i Danova Tech.',
           ['Shërbimet', 'Tregjet', 'Agjencia', 'Kontakt'], 'Magazina:', 'Zyra:', 'Kushtet e përdorimit', 'Kthehu në kreu'),
 'hr': _ch('Preskoči na sadržaj', ['Usluge', 'Video', 'Za koga', 'Radovi', 'Postupak', 'Cijene', 'Kontakt'], 'Razgovarajmo',
           'Danova Real Estate: renoviranje po sistemu ključ u ruke, generalni izvođač i namještaj za hotele u Venetu i Furlaniji. Odjel tvrtke Danova Tech.',
           ['Usluge', 'Tržišta', 'Agencija', 'Kontakt'], 'Skladišta:', 'Uredi:', 'Uvjeti korištenja', 'Natrag na početnu'),
 'hi': _ch('सामग्री पर जाएँ', ['सेवाएँ', 'वीडियो', 'किसके लिए', 'काम', 'प्रक्रिया', 'कीमतें', 'संपर्क'], 'बात करें',
           'Danova Real Estate: Veneto और Friuli में टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर और होटल फ़र्नीचर। Danova Tech का एक डिवीज़न।',
           ['सेवाएँ', 'बाज़ार', 'एजेंसी', 'संपर्क'], 'गोदाम:', 'ऑफ़िस:', 'उपयोग की शर्तें', 'होम पर वापस'),
}

# 24/10/2026 - stringhe del footer EN rimaste in inglese
for _l, _v in {'ro': ['Metoda noastră', 'Exemple de proiecte', 'Despre noi', 'Toate serviciile', 'Politica de confidențialitate', 'Politica privind cookie-urile'],
               'sq': ['Metoda jonë', 'Shembuj projektesh', 'Rreth nesh', 'Të gjitha shërbimet', 'Politika e privatësisë', 'Politika e cookie-ve'],
               'hi': ['हमारा तरीक़ा', 'प्रोजेक्ट के उदाहरण', 'हमारे बारे में', 'सभी सेवाएँ', 'गोपनीयता नीति', 'कुकी नीति'],
               'hr': ['Naša metoda', 'Primjeri projekata', 'O nama', 'Sve usluge', 'Pravila privatnosti', 'Pravila o kolačićima']}.items():
    CHROME[_l] += [('>%s</a>' % a, '>%s</a>' % b) for a, b in zip(['Our method', 'Example projects', 'About us', 'All services', 'Privacy Policy', 'Cookie Policy'], _v)]
