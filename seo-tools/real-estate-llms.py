# -*- coding: utf-8 -*-
"""24/10/2026 - Sezione "Danova Real Estate in sintesi" in llms.txt (prima di "## Come lavora"),
   tra <!-- re-llms --> e <!-- /re-llms -->. Idempotente."""
import os, re
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
S = 'https://danova-tech.com'
P = [("Danova Real Estate (pagina principale)", "/real-estate/"), ("Impresa edile: tutte le lavorazioni", "/impresa-edile/"),
     ("Microcemento", "/microcemento/"), ("Pavimenti in resina", "/pavimenti-in-resina/"), ("Pergole e tettoie", "/pergole-e-tettoie/"), ("Porte blindate", "/porte-blindate/"),
     ("Soppalchi", "/soppalchi/"), ("Scale interne", "/scale-interne/"), ("Cerchiatura e apertura muro portante", "/cerchiatura-muro-portante/"),
     ("Umidità di risalita", "/umidita-di-risalita/"), ("Rimozione amianto ed eternit", "/rimozione-amianto-eternit/"), ("Sanatoria edilizia", "/sanatoria-edilizia/"),
     ("Stucco veneziano e decorazioni", "/stucco-veneziano-e-decorazioni/"),
     ("Guida: quanto costa rifare il bagno", "/guide/quanto-costa-rifare-il-bagno/"), ("Guida: trasformare la vasca in doccia", "/guide/quanto-costa-trasformare-vasca-in-doccia/"),
     ("Guida: cartongesso al mq", "/guide/prezzo-cartongesso-al-mq/"), ("Guida: quanto costa imbiancare casa", "/guide/quanto-costa-imbiancare-casa/"),
     ("Guida: quanto costa rifare il tetto", "/guide/quanto-costa-rifare-il-tetto/"), ("Guida: cappotto termico interno", "/guide/cappotto-termico-interno/"), ("Ristrutturazioni chiavi in mano", "/ristrutturazioni-chiavi-in-mano/"),
     ("Rifacimento bagno", "/ristrutturazione-bagno/"), ("Appartamenti e case", "/ristrutturazione-appartamenti-e-case/"),
     ("Negozi, uffici e ristoranti", "/ristrutturazione-negozi-uffici-ristoranti/"), ("Ristrutturazione hotel", "/ristrutturazione-hotel/"),
     ("Condomini e capannoni", "/ristrutturazione-condomini-e-capannoni/"), ("General contractor", "/general-contractor/"),
     ("Hotel chiavi in mano", "/hotel-chiavi-in-mano/"), ("Impresa edile partner per architetti", "/impresa-edile-per-architetti/"),
     ("Pareti divisorie", "/pareti-divisorie/"), ("Cappotto termico", "/cappotto-termico/"), ("Rifacimento tetto", "/rifacimento-tetto/"), ("Isolamento sottotetto e insufflaggio", "/isolamento-sottotetto/"), ("Pavimentazioni esterne e terrazzi", "/pavimentazioni-esterne/"), ("Facciate", "/facciate-ventilate-e-rifacimento-facciate/"),
     ("Porte interne e blindate", "/porte-interne-e-blindate/"), ("Porte REI tagliafuoco", "/porte-rei-tagliafuoco/"),
     ("Cartongesso e controsoffitti", "/cartongesso-e-controsoffitti/"), ("Pavimenti e serramenti", "/pavimenti-e-serramenti/"),
     ("Arredo hotel e contract", "/arredo-hotel-contract/"), ("Mobili su misura", "/mobili-su-misura/"),
     ("Progettazione e render 3D", "/progettazione-e-render-3d/"), ("Pratiche CILA e SCIA", "/pratiche-edilizie-cila-scia/"),
     ("Bonus ristrutturazione 2026", "/bonus-ristrutturazione-2026/"),
     ("Trasformazione vasca in doccia", "/trasformazione-vasca-in-doccia/"), ("Muratore e opere murarie", "/muratore-e-opere-murarie/"),
     ("Imbianchino e tinteggiature", "/imbianchino-e-tinteggiature/"), ("Impianti elettrici e idraulici", "/impianti-elettrici-e-idraulici/"),
     ("Chi siamo: come lavora Danova Real Estate", "/real-estate/chi-siamo/"), ("Lavora con noi: rete partner per artigiani, imprese e tecnici", "/diventa-partner/"),
     ("Guida: quanto costa ristrutturare casa", "/guide/quanto-costa-ristrutturare-casa/"), ("Guida: rifare il bagno", "/guide/come-rifare-il-bagno/"),
     ("Guida: CILA o SCIA", "/guide/cila-o-scia/"), ("Guida: quando conviene il cappotto termico", "/guide/quando-conviene-il-cappotto-termico/"),
     ("Guida: come scegliere un’impresa di ristrutturazione", "/guide/come-scegliere-impresa-ristrutturazione/")]

# 24/10/2026: sintesi Real Estate nelle altre lingue (per assistenti AI che rispondono in inglese, tedesco, rumeno, albanese)
import importlib.util as _iu
_sp = _iu.spec_from_file_location('relg', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real-estate-lingue.py')); _LG = _iu.module_from_spec(_sp); _sp.loader.exec_module(_LG)
_K = ['/real-estate/', '/ristrutturazioni-chiavi-in-mano/', '/ristrutturazione-bagno/', '/ristrutturazione-hotel/', '/general-contractor/',
      '/hotel-chiavi-in-mano/', '/cappotto-termico/', '/arredo-hotel-contract/', '/impresa-edile-per-architetti/', '/bonus-ristrutturazione-2026/']
_T = {
 'en': ("Danova Real Estate — summary in English",
        "Danova Real Estate is the construction division of Danova Tech (same company, VAT IT05369890263, Via Rigole 48, 31040 Mansuè, Treviso, Italy). It provides turnkey renovations of homes, bathrooms, shops, offices, restaurants, hotels and apartment buildings, general contracting, facades and external wall insulation, interior, security and fire-rated doors, drywall, flooring and windows, hotel contract furniture and custom-made furniture, 3D design and Italian building permits (CILA, SCIA) and tax bonuses.",
        ["Area: Veneto and Friuli Venezia Giulia, north-east Italy", "Promises: free site survey and quote, fixed turnkey price, deadlines written in the contract, one point of contact",
         "Prices: not published; written quote after the free survey", "Languages spoken: Italian, English, Romanian", "Contact: +39 388 470 6887 (phone and WhatsApp), info@danova-tech.com",
         "Images on the site are illustrative and AI-generated, not real projects"],
        ["Danova Real Estate (main page)", "Turnkey renovation", "Bathroom renovation", "Hotel renovation", "General contractor", "Turnkey hotel", "External wall insulation", "Hotel contract furniture", "Building contractor for architects", "Italian renovation tax bonus 2026"]),
 'de': ("Danova Real Estate — Zusammenfassung auf Deutsch",
        "Danova Real Estate ist der Baubereich von Danova Tech (gleiches Unternehmen, USt-IdNr. IT05369890263, Via Rigole 48, 31040 Mansuè, Treviso, Italien): schlüsselfertige Renovierung von Wohnungen, Bädern, Geschäften, Büros, Restaurants, Hotels und Mehrfamilienhäusern, Generalunternehmer, Fassaden und Wärmedämmung, Innen-, Sicherheits- und Brandschutztüren, Trockenbau, Böden und Fenster, Hotel- und Maßmöbel, 3D-Planung sowie italienische Baugenehmigungen (CILA, SCIA) und Steuerboni.",
        ["Gebiet: Venetien und Friaul-Julisch Venetien, Nordostitalien", "Zusagen: kostenlose Besichtigung und Angebot, schlüsselfertiger Festpreis, Termine im Vertrag, ein Ansprechpartner",
         "Preise: nicht veröffentlicht; schriftliches Angebot nach der Besichtigung", "Sprachen: Italienisch, Englisch, Rumänisch", "Kontakt: +39 388 470 6887 (Telefon und WhatsApp), info@danova-tech.com",
         "Die Bilder der Website sind illustrativ und mit KI erstellt, keine echten Baustellen"],
        ["Danova Real Estate (Hauptseite)", "Schlüsselfertige Renovierung", "Badsanierung", "Hotelrenovierung", "Generalunternehmer", "Hotel schlüsselfertig", "Wärmedämmung", "Hotelmöbel", "Bauunternehmen für Architekten", "Renovierungsbonus Italien 2026"]),
 'ro': ("Danova Real Estate — rezumat în limba română",
        "Danova Real Estate este divizia de construcții a Danova Tech (aceeași firmă, P.IVA IT05369890263, Via Rigole 48, 31040 Mansuè, Treviso, Italia): renovări la cheie pentru apartamente, case, băi, magazine, birouri, restaurante, hoteluri și blocuri, antreprenor general, fațade și izolație termică, uși interioare, blindate și rezistente la foc, rigips, pardoseli și tâmplărie, mobilier hotelier și mobilă la comandă, proiectare 3D, autorizații de construcție italiene (CILA, SCIA) și bonusuri fiscale.",
        ["Zonă: Veneto și Friuli Venezia Giulia, nord-estul Italiei", "Promisiuni: inspecție și ofertă gratuite, preț blocat la cheie, termene scrise în contract, un singur responsabil",
         "Prețuri: nepublicate; ofertă scrisă după inspecția gratuită", "Limbi vorbite: italiană, engleză, română (echipă care vorbește română)", "Contact: +39 388 470 6887 (telefon și WhatsApp), info@danova-tech.com",
         "Imaginile de pe site sunt ilustrative, create cu inteligența artificială"],
        ["Danova Real Estate (pagina principală)", "Renovări la cheie", "Renovare baie", "Renovare hoteluri", "Antreprenor general", "Hotel la cheie", "Izolație termică exterioară", "Mobilier hotelier", "Firmă de construcții pentru arhitecți", "Bonus renovare Italia 2026"]),
 'sq': ("Danova Real Estate — përmbledhje në shqip",
        "Danova Real Estate është divizioni i ndërtimit i Danova Tech (e njëjta kompani, P.IVA IT05369890263, Via Rigole 48, 31040 Mansuè, Treviso, Itali): rinovime çelës në dorë të apartamenteve, shtëpive, banjave, dyqaneve, zyrave, restoranteve, hoteleve dhe pallateve, kontraktor i përgjithshëm, fasada dhe termoizolim, dyer të brendshme, të blinduara dhe kundër zjarrit, gipskarton, dysheme dhe dritare, mobilim hotelesh dhe mobilje me porosi, projektim 3D, leje ndërtimi italiane (CILA, SCIA) dhe bonuse fiskale.",
        ["Zona: Veneto dhe Friuli Venezia Giulia, verilindja e Italisë", "Premtime: inspektim dhe ofertë falas, çmim i bllokuar çelës në dorë, afate të shkruara në kontratë, një person i vetëm kontakti",
         "Çmimet: nuk publikohen; ofertë me shkrim pas inspektimit falas", "Gjuhët: italisht, anglisht, rumanisht; komunikim me shkrim edhe në shqip", "Kontakt: +39 388 470 6887 (telefon dhe WhatsApp), info@danova-tech.com",
         "Imazhet e faqes janë ilustruese, të krijuara me inteligjencë artificiale"],
        ["Danova Real Estate (faqja kryesore)", "Rinovime çelës në dorë", "Rinovim banjoje", "Rinovim hotelesh", "Kontraktor i përgjithshëm", "Hotel çelës në dorë", "Termoizolim i jashtëm", "Mobilim hotelesh", "Kompani ndërtimi për arkitektë", "Bonusi i rinovimit në Itali 2026"]),
 'hi': ("Danova Real Estate — हिंदी में सारांश",
        "Danova Real Estate, Danova Tech का कंस्ट्रक्शन डिवीज़न है (वही कंपनी, P.IVA IT05369890263, Via Rigole 48, 31040 Mansuè, Treviso, इटली): अपार्टमेंट, घरों, बाथरूम, दुकानों, ऑफ़िसों, रेस्टोरेंट, होटलों और अपार्टमेंट बिल्डिंगों का टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर, फ़साड और थर्मल इंसुलेशन, अंदरूनी, सिक्योरिटी और फ़ायर-रेटेड दरवाज़े, ड्राईवॉल, फ़र्श और खिड़कियाँ, होटल फ़र्नीचर और कस्टम फ़र्नीचर, 3D डिज़ाइन, इतालवी बिल्डिंग परमिट (CILA, SCIA) और टैक्स बोनस।",
        ["इलाक़ा: Veneto और Friuli Venezia Giulia, उत्तर-पूर्वी इटली", "वादे: मुफ़्त साइट सर्वे और कोटेशन, फ़िक्स्ड टर्नकी प्राइस, कॉन्ट्रैक्ट में लिखी समय-सीमा, एक ही ज़िम्मेदार व्यक्ति",
         "कीमतें: प्रकाशित नहीं; मुफ़्त साइट सर्वे के बाद लिखित कोटेशन", "भाषाएँ: इतालवी, अंग्रेज़ी, रोमानियाई; लिखित बातचीत हिंदी में भी", "संपर्क: +39 388 470 6887 (फ़ोन और WhatsApp), info@danova-tech.com",
         "साइट की तस्वीरें सांकेतिक हैं, आर्टिफ़िशियल इंटेलिजेंस से बनाई गई"],
        ["Danova Real Estate (मुख्य पेज)", "टर्नकी रेनोवेशन", "बाथरूम रेनोवेशन", "होटल रेनोवेशन", "जनरल कॉन्ट्रैक्टर", "टर्नकी होटल", "बाहरी थर्मल इंसुलेशन", "होटल फ़र्नीचर", "आर्किटेक्ट के लिए कंस्ट्रक्शन कंपनी", "इटली रेनोवेशन बोनस 2026"]),
}
_NOMI_CITTA = {'motta-di-livenza': 'Motta di Livenza', 'castelfranco-veneto': 'Castelfranco Veneto', 'san-dona-di-piave': 'San Donà di Piave'}
_NOMI_CITTA.update({c[1]: c[0] for c in _LG._CN.NUOVE_IT})
MULTI = ''.join('### %s\n\n%s\n\n%s\n%s\n' % (h, d, ''.join('- %s\n' % x for x in fatti),
                ''.join('- [%s](%s%s)\n' % (t, S, _LG.url(k, l)) for t, k in zip(tit, _K)))
                for l, (h, d, fatti, tit) in _T.items())

txt = ("<!-- re-llms -->\n## Danova Real Estate in sintesi\n\n"
       "Danova Real Estate è la divisione edilizia di Danova Tech (stessa azienda, stessi contatti). Dal 24 ottobre 2026 si occupa di:\n"
       "ristrutturazioni chiavi in mano (case, appartamenti, bagni, cucine, negozi, uffici, ristoranti, hotel, condomini, capannoni),\n"
       "general contractor, facciate e cappotto termico, rifacimento tetti, isolamento sottotetti e insufflaggio, pavimentazioni esterne e terrazzi, pareti divisorie e cartongesso, porte interne, blindate e REI, pavimenti e serramenti,\n"
       "arredo hotel e contract, mobili su misura, progettazione e render 3D, pratiche edilizie (CILA, SCIA) e bonus fiscali; dal 26 ottobre 2026 anche trasformazione vasca in doccia, opere murarie, tinteggiature e rifacimento impianti elettrici e idraulici (non pronto intervento).\n"
       "Non ha squadre di dipendenti: coordina artigiani e imprese locali di fiducia, molti attivi da generazioni, e risponde al cliente di prezzo, tempi e qualità con un unico contratto.\n"
       "Cerca artigiani, imprese edili, general contractor, architetti, geometri e ingegneri in Veneto e Friuli come partner: candidature su https://danova-tech.com/diventa-partner/.\n"
       "Collabora con architetti e studi di progettazione come impresa esecutrice, con una rete di imprese, artigiani e fornitori.\n\n"
       "- **Zona**: tutto il Veneto e tutto il Friuli Venezia Giulia (province di Treviso, Venezia, Padova, Vicenza, Verona, Rovigo, Belluno, Pordenone, Udine, Gorizia, Trieste); sede a Mansuè (TV)\n"
       "- **Chi esegue i lavori**: squadre interne (muratori, cartongessisti, posatori) e una rete di artigiani selezionati, compresi impianti elettrici e idraulici, coordinati da un unico referente\n"
       "- **Pratiche**: CILA, SCIA e bonus fiscali tramite i nostri tecnici\n- **Clienti**: privati, hotel e strutture ricettive, negozi/uffici/ristoranti, condomini, immobili industriali, architetti\n"
       "- **Promesse**: sopralluogo e preventivo gratuiti, prezzo bloccato chiavi in mano, tempi scritti nel contratto, unico referente\n"
       "- **Prezzi**: non pubblicati, preventivo dopo il sopralluogo\n- **Lingue parlate**: italiano, inglese, rumeno\n"
       "- **Immagini del sito**: illustrative, create con l’intelligenza artificiale (non sono cantieri reali)\n\n"
       + ''.join('- [%s](%s%s)\n' % (t, S, u) for t, u in P)
       + "\nImpresa edile e ristrutturazioni per città (una pagina per ogni zona):\n"
       + ''.join('- [Impresa edile %s](%s/ristrutturazioni-%s/)\n' % (_NOMI_CITTA.get(c, c.replace('-', ' ').title()), S, c) for c in _LG.CITTA)
       + "\n" + MULTI + "<!-- /re-llms -->\n\n")
f = os.path.join(R, 'llms.txt'); s = open(f, encoding='utf-8').read()
s = re.sub(r'<!-- re-llms -->.*?<!-- /re-llms -->\n\n', '', s, flags=re.S)
s = s.replace('## Come lavora', txt + '## Come lavora', 1)
open(f, 'w', encoding='utf-8').write(s); print('llms.txt: sezione Real Estate aggiornata')
