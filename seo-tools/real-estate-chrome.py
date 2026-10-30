# -*- coding: utf-8 -*-
"""24/10/2026 - Cornice (menu desktop/mobile e footer) delle pagine Danova Real Estate, tutta nella lingua della pagina.
   Ogni link del menu e del footer porta a pagine della stessa lingua (IT, EN, DE, RO, SQ): chi naviga in rumeno resta in rumeno.
   Il selettore di lingua (IT EN DE RO SQ) resta l'unico punto per cambiare lingua.
   Va lanciato DOPO real-estate-tema.py (e' gia' nella catena di real-estate-tutto.sh). Idempotente.
   Uso: python3 seo-tools/real-estate-chrome.py"""
import os, re, glob, importlib.util, html
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(HERE)
_s = importlib.util.spec_from_file_location('relg', os.path.join(HERE, 'real-estate-lingue.py')); LG = importlib.util.module_from_spec(_s); _s.loader.exec_module(LG)
L5 = ['it', 'en', 'de', 'ro', 'sq']
def T(*v): return dict(zip(L5, v))
U = lambda k, l: LG.url(k, l)

NAV = [('/ristrutturazioni-chiavi-in-mano/', T('Ristrutturazioni', 'Renovations', 'Renovierung', 'Renovări', 'Rinovime')),
       ('/general-contractor/', T('General contractor', 'General contractor', 'Generalunternehmer', 'Antreprenor general', 'Kontraktor')),
       ('/ristrutturazione-hotel/', T('Hotel', 'Hotels', 'Hotels', 'Hoteluri', 'Hotele')),
       ('/arredo-hotel-contract/', T('Arredo hotel', 'Hotel furniture', 'Hotelmöbel', 'Mobilier hotelier', 'Mobilim hotelesh')),
       ('/facciate-ventilate-e-rifacimento-facciate/', T('Facciate', 'Facades', 'Fassaden', 'Fațade', 'Fasada')),
       ('/impresa-edile-per-architetti/', T('Per architetti', 'For architects', 'Für Architekten', 'Pentru arhitecți', 'Për arkitektë'))]
TEL = T('Telefono', 'Phone', 'Telefon', 'Telefon', 'Telefoni')
CONTATTI = T('Contatti', 'Contact', 'Kontakt', 'Contact', 'Kontakt')
LAB = {
 '/ristrutturazioni-chiavi-in-mano/': T('Ristrutturazioni chiavi in mano', 'Turnkey renovation', 'Schlüsselfertige Renovierung', 'Renovări la cheie', 'Rinovime çelës në dorë'),
 '/ristrutturazione-appartamenti-e-case/': T('Appartamenti e case', 'Apartments and houses', 'Wohnungen und Häuser', 'Apartamente și case', 'Apartamente dhe shtëpi'),
 '/ristrutturazione-bagno/': T('Rifacimento bagno', 'Bathroom renovation', 'Badsanierung', 'Renovare baie', 'Rinovim banjoje'),
 '/ristrutturazione-negozi-uffici-ristoranti/': T('Negozi, uffici e ristoranti', 'Shops, offices and restaurants', 'Geschäfte, Büros, Restaurants', 'Magazine, birouri și restaurante', 'Dyqane, zyra dhe restorante'),
 '/ristrutturazione-hotel/': T('Ristrutturazione hotel', 'Hotel renovation', 'Hotelrenovierung', 'Renovare hoteluri', 'Rinovim hotelesh'),
 '/ristrutturazione-condomini-e-capannoni/': T('Condomini e capannoni', 'Apartment buildings and industrial', 'Mehrfamilienhäuser und Hallen', 'Blocuri și hale', 'Pallate dhe kapanone'),
 '/general-contractor/': T('General contractor', 'General contractor', 'Generalunternehmer', 'Antreprenor general', 'Kontraktor i përgjithshëm'),
 '/hotel-chiavi-in-mano/': T('Hotel chiavi in mano', 'Turnkey hotel', 'Hotel schlüsselfertig', 'Hotel la cheie', 'Hotel çelës në dorë'),
 '/impresa-edile-per-architetti/': T('Impresa per architetti', 'Contractor for architects', 'Bauunternehmen für Architekten', 'Firmă pentru arhitecți', 'Kompani për arkitektë'),
 '/pareti-divisorie/': T('Pareti divisorie', 'Partition walls', 'Trennwände', 'Pereți despărțitori', 'Mure ndarëse'),
 '/rifacimento-tetto/': T('Rifacimento tetto', 'Roof replacement', 'Dachsanierung', 'Refacere acoperiș', 'Rinovim çatie'),
 '/isolamento-sottotetto/': T('Isolamento sottotetto', 'Loft insulation', 'Dachbodendämmung', 'Izolare pod', 'Izolim papafingo'),
 '/pavimentazioni-esterne/': T('Pavimentazioni esterne', 'Outdoor paving', 'Außenbeläge', 'Pavaje exterioare', 'Shtrime të jashtme'),
 '/cappotto-termico/': T('Cappotto termico', 'External wall insulation', 'Wärmedämmung', 'Izolație termică', 'Termoizolim i jashtëm'),
 '/facciate-ventilate-e-rifacimento-facciate/': T('Facciate', 'Facade renovation', 'Fassadensanierung', 'Renovare fațade', 'Rinovim fasadash'),
 '/porte-interne-e-blindate/': T('Porte interne e blindate', 'Interior and security doors', 'Innen- und Sicherheitstüren', 'Uși interioare și blindate', 'Dyer të brendshme dhe të blinduara'),
 '/porte-rei-tagliafuoco/': T('Porte REI tagliafuoco', 'Fire-rated doors', 'Brandschutztüren', 'Uși rezistente la foc', 'Dyer kundër zjarrit'),
 '/cartongesso-e-controsoffitti/': T('Cartongesso e controsoffitti', 'Drywall and ceilings', 'Trockenbau und Decken', 'Rigips și tavane false', 'Gipskarton dhe tavane të varura'),
 '/pavimenti-e-serramenti/': T('Pavimenti e serramenti', 'Flooring and windows', 'Böden und Fenster', 'Pardoseli și tâmplărie', 'Dysheme dhe dritare'),
 '/arredo-hotel-contract/': T('Arredo hotel e contract', 'Hotel contract furniture', 'Hotelmöbel', 'Mobilier hotelier', 'Mobilim hotelesh'),
 '/mobili-su-misura/': T('Mobili su misura', 'Custom-made furniture', 'Maßmöbel', 'Mobilă la comandă', 'Mobilje me porosi'),
 '/progettazione-e-render-3d/': T('Progettazione e render 3D', 'Design and 3D rendering', 'Planung und 3D-Visualisierung', 'Proiectare și randări 3D', 'Projektim dhe render 3D'),
 '/pratiche-edilizie-cila-scia/': T('Pratiche CILA e SCIA', 'Building permits', 'Baugenehmigungen', 'Autorizații de construcție', 'Leje ndërtimi'),
 '/bonus-ristrutturazione-2026/': T('Bonus ristrutturazione 2026', 'Renovation tax bonus 2026', 'Renovierungsbonus 2026', 'Bonus renovare 2026', 'Bonusi i rinovimit 2026'),
 '/guide/come-scegliere-impresa-ristrutturazione/': T('Come scegliere l’impresa', 'Choosing a renovation company', 'Renovierungsfirma auswählen', 'Cum alegi firma de renovări', 'Si të zgjidhni kompaninë'),
 '/guide/quanto-costa-ristrutturare-casa/': T('Quanto costa ristrutturare casa', 'Renovation costs', 'Renovierungskosten', 'Costul renovării', 'Kostoja e rinovimit'),
 '/guide/come-rifare-il-bagno/': T('Rifare il bagno', 'Bathroom renovation guide', 'Ratgeber Badsanierung', 'Ghid renovare baie', 'Udhëzues rinovim banjoje'),
 '/guide/cila-o-scia/': T('CILA o SCIA', 'CILA or SCIA', 'CILA oder SCIA', 'CILA sau SCIA', 'CILA apo SCIA'),
 '/guide/ristrutturare-un-hotel/': T('Ristrutturare un hotel', 'Renovating a hotel', 'Hotel renovieren', 'Renovarea unui hotel', 'Rinovimi i një hoteli'),
 '/guide/quando-conviene-il-cappotto-termico/': T('Quando conviene il cappotto', 'Is insulation worth it', 'Lohnt sich Wärmedämmung', 'Merită izolația termică', 'A ia vlen termoizolimi'),
 '/guide/porte-rei-negli-hotel/': T('Porte REI negli hotel', 'Fire doors in hotels', 'Brandschutztüren im Hotel', 'Uși antifoc în hoteluri', 'Dyer kundër zjarrit në hotele'),
}
CITTA = ['treviso', 'venezia', 'padova', 'vicenza', 'verona', 'rovigo', 'belluno', 'pordenone', 'udine', 'trieste', 'gorizia']  # tutti gli 11 capoluoghi (26/10)
IN = T('Ristrutturazioni a %s', 'Renovation in %s', 'Renovierung in %s', 'Renovări în %s', 'Rinovime në %s')
NOMI = {'venezia': T('Venezia', 'Venice', 'Venedig', 'Veneția', 'Venecia'), 'padova': T('Padova', 'Padua', 'Padua', 'Padova', 'Padova'), 'trieste': T('Trieste', 'Trieste', 'Triest', 'Trieste', 'Trieste')}
COL = [T('Ristrutturazioni', 'Renovations', 'Renovierung', 'Renovări', 'Rinovime'),
       T('Lavorazioni e arredo', 'Works and furniture', 'Gewerke und Einrichtung', 'Lucrări și mobilier', 'Punime dhe mobilim'),
       T('Zone', 'Areas', 'Regionen', 'Zone', 'Zonat'), T('Guide', 'Guides', 'Ratgeber', 'Ghiduri', 'Udhëzues')]
K1 = ['/ristrutturazioni-chiavi-in-mano/', '/ristrutturazione-appartamenti-e-case/', '/ristrutturazione-bagno/', '/ristrutturazione-negozi-uffici-ristoranti/',
      '/ristrutturazione-hotel/', '/ristrutturazione-condomini-e-capannoni/', '/general-contractor/', '/hotel-chiavi-in-mano/', '/impresa-edile-per-architetti/']
K2 = ['/pareti-divisorie/', '/cartongesso-e-controsoffitti/', '/cappotto-termico/', '/isolamento-sottotetto/', '/rifacimento-tetto/', '/pavimentazioni-esterne/', '/facciate-ventilate-e-rifacimento-facciate/', '/porte-interne-e-blindate/',
      '/porte-rei-tagliafuoco/', '/pavimenti-e-serramenti/', '/arredo-hotel-contract/', '/mobili-su-misura/', '/progettazione-e-render-3d/',
      '/pratiche-edilizie-cila-scia/', '/bonus-ristrutturazione-2026/']
KG = [k for k in LAB if k.startswith('/guide/')]
DESC = T('Danova Real Estate: ristrutturazioni chiavi in mano, general contractor, facciate e arredo hotel in Veneto e Friuli Venezia Giulia. Una divisione di Danova Tech.',
         'Danova Real Estate: turnkey renovations, general contracting, facades and hotel furniture in Veneto and Friuli Venezia Giulia, Italy. A division of Danova Tech.',
         'Danova Real Estate: schlüsselfertige Renovierungen, Generalunternehmer, Fassaden und Hoteleinrichtung in Venetien und Friaul-Julisch Venetien. Ein Geschäftsbereich von Danova Tech.',
         'Danova Real Estate: renovări la cheie, antreprenor general, fațade și mobilier hotelier în Veneto și Friuli Venezia Giulia, Italia. O divizie a Danova Tech.',
         'Danova Real Estate: rinovime çelës në dorë, kontraktor i përgjithshëm, fasada dhe mobilim hotelesh në Veneto dhe Friuli Venezia Giulia, Itali. Një divizion i Danova Tech.')
ADDR = T('Via Rigole 48<br>31040 Mansuè (TV) — Italia', 'Via Rigole 48<br>31040 Mansuè (TV) — Italy', 'Via Rigole 48<br>31040 Mansuè (TV) — Italien',
         'Via Rigole 48<br>31040 Mansuè (TV) — Italia', 'Via Rigole 48<br>31040 Mansuè (TV) — Itali')
WA = T('WhatsApp: scriveteci', 'WhatsApp: message us', 'WhatsApp: schreiben Sie uns', 'WhatsApp: scrieți-ne', 'WhatsApp: na shkruani')
LANGS = T('Parliamo italiano, inglese e rumeno', 'We speak Italian, English and Romanian', 'Wir sprechen Italienisch, Englisch und Rumänisch',
          'Vorbim italiană, engleză și română', 'Flasim italisht, anglisht dhe rumanisht')
LEG = {'it': [('/privacy/', 'Privacy Policy'), ('/cookie-policy/', 'Cookie Policy'), ('/termini/', 'Termini d’uso')],
       'en': [('/en/privacy/', 'Privacy Policy'), ('/en/cookie-policy/', 'Cookie Policy'), ('/en/terms/', 'Terms of use')],
       'de': [('/de/datenschutz/', 'Datenschutzerklärung'), ('/de/cookie-richtlinie/', 'Cookie-Richtlinie'), ('/de/agb/', 'Nutzungsbedingungen')],
       'ro': [('/ro/confidentialitate/', 'Politica de confidențialitate'), ('/ro/politica-cookie/', 'Politica privind cookie-urile'), ('/ro/termeni-de-utilizare/', 'Termeni de utilizare')],
       'sq': [('/sq/privatesia/', 'Politika e privatësisë'), ('/sq/politika-e-cookie-ve/', 'Politika e cookie-ve'), ('/sq/kushtet-e-perdorimit/', 'Kushtet e përdorimit')]}
TECH = {'it': ('/', 'Danova Tech: siti, app e software'), 'en': ('/en/', 'Danova Tech: web, apps and software'), 'de': ('/de/', 'Danova Tech: Web, Apps und Software')}

# 29/10/2026: hindi (hi)
L5.append('hi')
for (_k, _t), _h in zip(NAV, ['रेनोवेशन', 'जनरल कॉन्ट्रैक्टर', 'होटल', 'होटल फ़र्नीचर', 'फ़साड', 'आर्किटेक्ट के लिए']): _t['hi'] = _h
TEL['hi'] = 'फ़ोन'; CONTATTI['hi'] = 'संपर्क'
for _k, _h in {'/ristrutturazioni-chiavi-in-mano/': 'टर्नकी रेनोवेशन', '/ristrutturazione-appartamenti-e-case/': 'अपार्टमेंट और घर', '/ristrutturazione-bagno/': 'बाथरूम रेनोवेशन',
               '/ristrutturazione-negozi-uffici-ristoranti/': 'दुकानें, ऑफ़िस और रेस्टोरेंट', '/ristrutturazione-hotel/': 'होटल रेनोवेशन', '/ristrutturazione-condomini-e-capannoni/': 'अपार्टमेंट बिल्डिंग और गोदाम',
               '/general-contractor/': 'जनरल कॉन्ट्रैक्टर', '/hotel-chiavi-in-mano/': 'टर्नकी होटल', '/impresa-edile-per-architetti/': 'आर्किटेक्ट के लिए कंपनी', '/pareti-divisorie/': 'पार्टीशन दीवारें',
               '/rifacimento-tetto/': 'छत की मरम्मत', '/isolamento-sottotetto/': 'अटारी इंसुलेशन', '/pavimentazioni-esterne/': 'बाहरी फ़्लोरिंग', '/cappotto-termico/': 'बाहरी थर्मल इंसुलेशन',
               '/facciate-ventilate-e-rifacimento-facciate/': 'फ़साड रेनोवेशन', '/porte-interne-e-blindate/': 'अंदरूनी और सिक्योरिटी दरवाज़े', '/porte-rei-tagliafuoco/': 'फ़ायर-रेटेड दरवाज़े',
               '/cartongesso-e-controsoffitti/': 'ड्राईवॉल और सीलिंग', '/pavimenti-e-serramenti/': 'फ़र्श और खिड़कियाँ', '/arredo-hotel-contract/': 'होटल फ़र्नीचर', '/mobili-su-misura/': 'कस्टम फ़र्नीचर',
               '/progettazione-e-render-3d/': 'डिज़ाइन और 3D रेंडर', '/pratiche-edilizie-cila-scia/': 'बिल्डिंग परमिट', '/bonus-ristrutturazione-2026/': 'रेनोवेशन बोनस 2026',
               '/guide/come-scegliere-impresa-ristrutturazione/': 'रेनोवेशन कंपनी कैसे चुनें', '/guide/quanto-costa-ristrutturare-casa/': 'रेनोवेशन की लागत', '/guide/come-rifare-il-bagno/': 'बाथरूम रेनोवेशन गाइड',
               '/guide/cila-o-scia/': 'CILA या SCIA', '/guide/ristrutturare-un-hotel/': 'होटल रेनोवेशन कैसे करें', '/guide/quando-conviene-il-cappotto-termico/': 'क्या इंसुलेशन फ़ायदेमंद है',
               '/guide/porte-rei-negli-hotel/': 'होटलों में फ़ायर-रेटेड दरवाज़े'}.items():
    LAB[_k]['hi'] = _h
IN['hi'] = '%s में रेनोवेशन'
NOMI['venezia']['hi'] = 'Venice'; NOMI['padova']['hi'] = 'Padua'; NOMI['trieste']['hi'] = 'Trieste'
for _c, _h in zip(COL, ['रेनोवेशन', 'काम और फ़र्नीचर', 'इलाक़े', 'गाइड']): _c['hi'] = _h
DESC['hi'] = 'Danova Real Estate: इटली के Veneto और Friuli Venezia Giulia में टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर, फ़साड और होटल फ़र्नीचर। Danova Tech का एक डिवीज़न।'
ADDR['hi'] = 'Via Rigole 48<br>31040 Mansuè (TV) — इटली'
WA['hi'] = 'WhatsApp: हमें लिखें'
LANGS['hi'] = 'हम इतालवी, अंग्रेज़ी और रोमानियाई बोलते हैं; लिखित में हिंदी भी'
LEG['hi'] = [('/hi/privacy/', 'गोपनीयता नीति'), ('/hi/cookie-policy/', 'कुकी नीति'), ('/hi/terms/', 'उपयोग की शर्तें')]


def nav_links(l, cur, contact, ind):
    o = []
    for i, (k, t) in enumerate(NAV):
        u = U(k, l)
        nx = (' class="re-nx"' if i >= 4 else ' class="re-n2"' if i >= 2 else '') if ind.startswith('\n      ') else ''
        o.append('<a href="%s"%s%s>%s</a>' % (u, nx, ' aria-current="page"' if u == cur else '', t[l]))
    o.append('<a href="%s">%s</a>' % (contact, CONTATTI[l]))
    return ind + ind.join(o)


def li(u, t, cur):
    return '<li><a href="%s"%s>%s</a></li>' % (u, ' aria-current="page"' if u == cur else '', html.escape(t))


def footer(l, cur, s):
    m = re.search(r'(<span class="brand">.*?</span></span>)', s, re.S)
    brand = m.group(1) if m else ''
    c1 = ''.join(li(U(k, l), LAB[k][l], cur) for k in K1)
    c2 = ''.join(li(U(k, l), LAB[k][l], cur) for k in K2)
    if l == 'it':   # 26/10/2026: pagine solo IT (ricerca Google Ads)
        c2 += ''.join(li(u, t, cur) for u, t in [('/impresa-edile/', 'Impresa edile: tutte le lavorazioni'), ('/microcemento/', 'Microcemento'), ('/pavimenti-in-resina/', 'Pavimenti in resina'), ('/porte-blindate/', 'Porte blindate'), ('/pergole-e-tettoie/', 'Pergole e tettoie'), ('/soppalchi/', 'Soppalchi'), ('/scale-interne/', 'Scale interne'), ('/cerchiatura-muro-portante/', 'Cerchiatura muro portante'), ('/umidita-di-risalita/', 'Umidità di risalita'), ('/rimozione-amianto-eternit/', 'Rimozione amianto ed eternit'), ('/sanatoria-edilizia/', 'Sanatoria edilizia'), ('/stucco-veneziano-e-decorazioni/', 'Stucco veneziano'), ('/abbattimento-barriere-architettoniche/', 'Barriere architettoniche'), ('/impermeabilizzazioni/', 'Impermeabilizzazioni'), ('/muffa-e-infiltrazioni/', 'Muffa e infiltrazioni'), ('/adeguamento-sismico-e-consolidamento/', 'Adeguamento sismico'), ('/demolizioni-e-sgomberi/', 'Demolizioni e sgomberi'), ('/costruzione-case-e-ampliamenti/', 'Costruzione case'), ('/ristrutturazione-casali-e-rustici/', 'Casali e rustici'), ('/recinzioni-piscine-e-box-auto/', 'Recinzioni e piscine'), ('/grondaie-lattoneria-e-linea-vita/', 'Grondaie e linea vita'), ('/fotovoltaico-e-pompa-di-calore/', 'Fotovoltaico e pompa di calore'), ('/cabine-armadio-pareti-attrezzate-e-boiserie/', 'Cabine armadio e boiserie'), ('/cambio-destinazione-d-uso-e-ape/', 'Cambio d’uso e APE'), ('/home-staging/', 'Home staging'), ('/compriamo-case-da-ristrutturare/', 'Compriamo case da ristrutturare'), ('/ristrutturazione-e-gestione-affitti-brevi/', 'Affitti brevi'), ('/trasformazione-vasca-in-doccia/', 'Trasformazione vasca in doccia'), ('/muratore-e-opere-murarie/', 'Muratore e opere murarie'),
                                                  ('/imbianchino-e-tinteggiature/', 'Imbianchino e tinteggiature'), ('/impianti-elettrici-e-idraulici/', 'Impianti elettrici e idraulici')])
    c3 = ''.join(li(U('/ristrutturazioni-%s/' % c, l), IN[l] % NOMI.get(c, {}).get(l, c.capitalize()), cur) for c in CITTA)
    cg = ''.join(li(U(k, l), LAB[k][l], cur) for k in KG)
    c4 = ('<li><a href="tel:+393884706887">+39 388 470 6887</a></li><li><a href="https://wa.me/393884706887" target="_blank" rel="noopener">%s</a></li>'
          '<li><a href="mailto:info@danova-tech.com">info@danova-tech.com</a></li><li>%s</li><li>%s</li>'
          '<li><a href="https://www.instagram.com/danova_techh/" target="_blank" rel="noopener me">Instagram</a> · '
          '<a href="https://www.facebook.com/profile.php?id=61594907955699" target="_blank" rel="noopener me">Facebook</a> · '
          '<a href="https://www.tiktok.com/@danova.tech" target="_blank" rel="noopener me">TikTok</a></li>') % (WA[l], ADDR[l], LANGS[l])
    if l == 'it':   # 26/10/2026: pagina reclutamento partner (solo IT)
        c4 += li('/real-estate/chi-siamo/', 'Chi siamo', cur) + li('/real-estate/domande-frequenti/', 'Domande frequenti', cur) + li('/real-estate/esempi-di-intervento/', 'Esempi di intervento', cur) + li('/diventa-partner/', 'Lavora con noi: diventa partner', cur)
    leg = '<i>·</i>'.join('<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if u == cur else '', t) for u, t in LEG[l])
    if l in TECH:
        leg += '<i>·</i><a href="%s">%s</a>' % TECH[l]
    return ('<footer class="re-footer">\n  <div class="wrap">\n    <div class="f-top re-foot">\n'
            '      <div class="fb">\n        %s\n        <p>%s</p>\n      </div>\n'
            '      <div><h5>%s</h5><ul>%s</ul></div>\n      <div><h5>%s</h5><ul>%s</ul></div>\n'
            '      <div><h5>%s</h5><ul>%s</ul><h5 class="re-h5b">%s</h5><ul>%s</ul></div>\n'
            '      <div><h5>%s</h5><ul>%s</ul></div>\n    </div>\n'
            '    <div class="f-bot">\n      <span>© <span id="yy">2026</span> Danova Tech — P.IVA 05369890263</span>\n'
            '      <span class="f-legal">%s</span></div>\n  </div>\n  <div class="giant">DANOVA</div>\n</footer>'
            % (brand, DESC[l], COL[0][l], c1, COL[1][l], c2, COL[2][l], c3, COL[3][l], cg, CONTATTI[l], c4, leg))


def main():
    n = 0
    for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
        rel = os.path.relpath(f, R).replace('\\', '/')
        if rel.startswith(('seo-tools/', '_archivio/', 'social/')):
            continue
        s = open(f, encoding='utf-8').read()
        if 'name="dt-sezione" content="real-estate"' not in s:
            continue
        m = re.search(r'<html lang="([a-z]{2})', s)
        l = m.group(1) if m else ''
        if l not in L5:
            continue
        s0 = s
        cur = '/' + rel[:-len('index.html')]
        home = U('/real-estate/', l)
        contact = '#contatti' if 'id="dt-scrivi"' in s else home + '#contatti'
        s = re.sub(r'(<a href=")[^"]*(" class="brand")', lambda m: m.group(1) + home + m.group(2), s, count=1)
        s = re.sub(r'(<a href=")[^"]*(" class="btn btn-p" data-mag><span class="lbl">)', lambda m: m.group(1) + contact + m.group(2), s, count=1)
        s = re.sub(r'(<nav class="links"[^>]*>).*?(\s*</nav>)', lambda m: m.group(1) + nav_links(l, cur, contact, '\n      ') + m.group(2), s, count=1, flags=re.S)
        s = re.sub(r'(<nav id="mob"[^>]*>).*?(\s*<div class="mob-lang-links">)', lambda m: m.group(1) + nav_links(l, cur, contact, '\n  ') + '\n\n  ' + m.group(2).lstrip(), s, count=1, flags=re.S)
        # 24/10/2026: ancora #contatti sulla sezione del modulo (il titolo resta visibile sotto l'intestazione fissa),
        # telefono ed email obbligatori, versione aggiornata di contatto.js
        s = s.replace('<section class="pg-cta" id="contatti">', '<section class="pg-cta">')
        s = re.sub(r'(<section class="pg-cta">\s*<div class="wrap">\s*<div class="box")(?! id=)([^>]*>(?:(?!</section>).)*?id="dt-scrivi")', r'\1 id="contatti"\2', s, count=1, flags=re.S)
        s = s.replace('href="#dt-scrivi"', 'href="#contatti"')
        s = re.sub(r'<input type="tel" name="tel" id="dtl-tel" placeholder=" "(?! required)', '<input type="tel" name="tel" id="dtl-tel" placeholder=" " required', s)
        s = re.sub(r'(<label for="dtl-tel">)[^<(]*?\s*\([^)<]*\)(</label>)', lambda m: m.group(1) + TEL[l] + m.group(2), s)
        s = re.sub(r'assets/js/contatto\.js\?v=\d+', 'assets/js/contatto.js?v=20261024', s)
        s = re.sub(r'<footer[^>]*>.*?</footer>', lambda m: footer(l, cur, m.group(0)), s, count=1, flags=re.S)
        if s != s0:
            open(f, 'w', encoding='utf-8').write(s)
            n += 1
    print('cornice Real Estate nella lingua della pagina:', n)


if __name__ == '__main__':
    main()
