# -*- coding: utf-8 -*-
"""26/10/2026 - Danova Real Estate, SQ (5): rinovim çatie, izolim papafingo, shtrime të jashtme."""
import importlib.util, os
_H = os.path.dirname(os.path.abspath(__file__))
def _ld(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(_H, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B = _ld('rsq1', 'real-estate-tr-sq-1.py')
L, LANG, G, _G, u, RE, svc, A, FAQ_BASE = B.L, B.LANG, B.G, B._G, B.u, B.RE, B.svc, B.A, B.FAQ_BASE
PAGINE = []
def P(key, **k): PAGINE.append(dict(lang=LANG, key=key, url=u(key), **k))

P('/rifacimento-tetto/', hero="re-tetto-cantiere", heroalt='Rinovim çatie në Veneto: skelë, izolim, membranë dhe tjegulla të reja',
 title="Rinovim çatie në Veneto dhe Friuli | Çati të izoluara",
 desc="Rinovim çatie çelës në dorë në Veneto dhe Friuli: çmontim, strukturë, izolim, hidroizolim, tjegulla, ulluqe dhe linjë jete, me leje dhe zbritje fiskale. Inspektim falas.",
 ogtitle="Rinovim çatie — Danova Real Estate", ogdesc="Një çati e re, e izoluar dhe pa rrjedhje: një person i vetëm nga skela te ulluqet, me çmim të bllokuar.",
 crumbs=[RE, ("Rinovim çatie", None)], eyebrow="Çati · Veneto dhe Friuli",
 h1=f"Rinovim çatie: {G}një çati e re, e izoluar dhe pa rrjedhje.{_G}",
 lead="Rinovojmë çatitë e shtëpive, vilave, pallateve dhe kapanoneve: skelë, çmontim i mbulesës, kontroll ose rindërtim i strukturës, izolim, hidroizolim, tjegulla, ulluqe dhe linjë jete. Me leje dhe dokumente për zbritjet fiskale italiane, me çmim të bllokuar dhe afate të shkruara në kontratë.",
 cta1="Kërkoni inspektimin", cta2="Çfarë përfshin",
 badges=["E ajrosur dhe e izoluar", "Skela e përfshirë", "Çmim i bllokuar", "Zbritje 2026"],
 sezioni=[
  {"id": "in-breve", "tipo": "breve", "eyebrow": "Shkurt", "h2": f"Rinovimi i çatisë {G}në pak rreshta{_G}",
   "testo": "<b>Rinovimi i çatisë</b> përfshin çmontimin e mbulesës së vjetër, kontrollin e strukturës prej druri ose betoni (dhe zëvendësimin e saj kur duhet), <b>izolimin termik</b>, <b>membranën hidroizoluese</b> dhe listelat për <b>ajrosjen</b>, mbulesën e re me tjegulla ose llamarinë, ulluqet dhe <b>linjën e jetës</b> kur kërkohet. Danova Real Estate ndjek gjithçka me një person të vetëm kontakti, në <b>Veneto dhe Friuli Venezia Giulia</b>.",
   "fatti": [("Ndërtesa", "Shtëpi, vila, pallate, kapanone"), ("Struktura", "Dru, beton, çelik"), ("Izolimi", "Pllaka, fibër druri, lesh shkëmbi"),
             ("Mbulesa", "Tjegulla, llamarinë, panele"), ("Zbritja 2026", "50% banesa kryesore, 36% të tjerat"), ("Lejet", "CILA ose SCIA, i ndjekim ne")]},
  {"id": "cosa", "tipo": "cards", "eyebrow": "Çfarë përfshin", "h2": f"Nga skela {G}te ulluku{_G}",
   "corpo": [("Skela dhe siguria", "Montimi i skelës, mbrojtjet dhe plani i sigurisë."), ("Çmontim dhe asgjësim", "Eterniti hiqet nga firma të autorizuara, me plan pune te autoriteti shëndetësor."),
             ("Struktura", "Kontroll i trarëve dhe dërrasave; zëvendësim ose përforcim, me projekt strukturor kur duhet."), ("Izolim dhe ajrosje", "Pllaka izoluese, barrierë avulli, shtresë ajrosjeje: më ngrohtë në dimër, më freskët në verë."),
             ("Hidroizolim dhe mbulesë", "Membrana që marrin frymë, tjegulla ose llamarinë, kulme dhe pjesë speciale."), ("Ulluqe dhe linjë jete", "Ulluqe, gypa shkarkimi dhe sisteme kundër rënies sipas rregullave rajonale.")]},
  {"id": "promesse", "tipo": "promesse", "eyebrow": "Garancitë", "h2": f"Një çati e re {G}pa surpriza{_G}"}],
 faqtitle=f"Pyetje për {G}rinovimin e çatisë.{_G}",
 faq=[("Sa kushton rinovimi i çatisë?", "Varet nga sipërfaqja, forma, gjendja e strukturës, izolimi, mbulesa dhe aksesi për skelën. Prandaj nuk publikojmë lista çmimesh: pas inspektimit falas merrni një ofertë me shkrim me çmim të bllokuar, dhe zbritjet fiskale e ulin koston reale."),
      ("Sa zgjat kantieri?", "Për një shtëpi private zakonisht disa javë, me skelë dhe ulluqe; datën e përfundimit e shkruajmë në kontratë. Shtëpia nuk mbetet kurrë e pambuluar në shi.")] + FAQ_BASE[:3],
 ctabox={"h2": "A ka nevojë çatia juaj për ne?", "p": "Na dërgoni adresën dhe disa foto të çatisë ose të rrjedhjeve: caktojmë inspektimin falas.", "btn": "Kërkoni inspektimin"},
 altrititle="Faqe të lidhura",
 altri=[("Izolim papafingo", u('/isolamento-sottotetto/')), ("Izolim termik", u('/cappotto-termico/')), ("Pallate dhe kapanone", u('/ristrutturazione-condomini-e-capannoni/')),
        ("Bonusi i rinovimit në Itali 2026", u('/bonus-ristrutturazione-2026/')), ("Danova Real Estate", u('/real-estate/'))],
 svc=svc("Rinovim çatie", "Punime çatie",
         "Rinovim çatish në Veneto dhe Friuli Venezia Giulia, Itali: skelë, çmontim, strukturë, izolim, hidroizolim, mbulesë, ulluqe dhe linjë jete, me leje dhe zbritje fiskale.",
         ["Skelë", "Çmontim dhe eternit", "Struktura e çatisë", "Izolim dhe ajrosje", "Mbulesa", "Ulluqe dhe linjë jete"]))

P('/isolamento-sottotetto/', hero="re-sottotetto-insufflaggio", heroalt='Izolim i papafingos me fryrje leshi mineral mbi soletë',
 title="Izolim papafingo dhe izolim me fryrje në Veneto dhe Friuli",
 desc="Izolimi i papafingos së shkelshme dhe të pashkelshme dhe izolim me fryrje në Veneto dhe Friuli: më pak humbje nxehtësie, pak pluhur, punime të shpejta dhe dokumente për ecobonus.",
 ogtitle="Izolim papafingo — Danova Real Estate", ogdesc="Mënyra më e shpejtë për të ndalur humbjen e nxehtësisë nga çatia: izolimi i soletës së papafingos ose i pjerrësive.",
 crumbs=[RE, ("Izolim papafingo", None)], eyebrow="Izolim termik · çati dhe papafingo",
 h1=f"Izolimi i papafingos: {G}nxehtësia mbetet në shtëpi.{_G}",
 lead="Izolojmë papafingo të shkelshme dhe të pashkelshme, mansarda dhe soleta drejt hapësirave të pangrohura: me pllaka të shtruara thatë, me tavane e mure gipskartoni të izoluara ose duke fryrë material izolues në boshllëqe. Punime të shpejta, të pastra dhe me dokumentet për zbritjet fiskale.",
 cta1="Kërkoni inspektimin", cta2="Zgjidhjet",
 badges=["E shkelshme ose jo", "Izolim me fryrje", "Gati në pak ditë", "Ecobonus 2026"],
 sezioni=[
  {"id": "in-breve", "tipo": "breve", "eyebrow": "Shkurt", "h2": f"Izolimi i papafingos {G}në pak rreshta{_G}",
   "testo": "Në një shtëpi të paizoluar një pjesë e madhe e nxehtësisë humbet nga çatia dhe soleta e fundit. <b>Izolimi i papafingos</b> bëhet mbi soletën mes dhomave të ngrohura dhe papafingos së ftohtë, ose në pjerrësitë e çatisë nëse mansarda banohet: me <b>pllaka izoluese</b>, me <b>tavane të izoluara</b> ose me <b>fryrje</b>, pa rindërtuar çatinë.",
   "fatti": [("Ku", "Soleta e papafingos, pjerrësi, mansarda, boshllëqe"), ("Metodat", "Pllaka, tavane të izoluara, fryrje"), ("Materialet", "Lesh mineral, fibër druri, celulozë, EPS"),
             ("Kohëzgjatja", "Zakonisht pak ditë"), ("Zbritja 2026", "Ecobonus 50% banesa kryesore, 36% të tjerat"), ("Çmimi", "I bllokuar pas inspektimit")]},
  {"id": "promesse", "tipo": "promesse", "eyebrow": "Garancitë", "h2": f"Një izolim {G}i bërë si duhet{_G}"}],
 faqtitle=f"Pyetje për {G}izolimin e papafingos.{_G}",
 faq=[("Çfarë është izolimi me fryrje?", "Material izolues i shkrifët (fije leshi mineral, celulozë ose granula) fryhet në boshllëqet e soletave dhe mureve ose mbi soletën e një papafingoje të pashkelshme. Zgjat disa orë ose pak ditë, pa prishje dhe me shumë pak pluhur."),
      ("Sa kushton izolimi i papafingos?", "Varet nga sipërfaqja, aksesi, materiali dhe trashësia. Nuk publikojmë lista çmimesh: pas inspektimit falas merrni një ofertë me shkrim me çmim të bllokuar.")] + FAQ_BASE[:3],
 ctabox={"h2": "Izolojmë papafingon tuaj.", "p": "Adresa, lloji i shtëpisë dhe aksesi në papafingo: vijmë ta shohim dhe ju propozojmë zgjidhjen.", "btn": "Kërkoni inspektimin"},
 altrititle="Faqe të lidhura",
 altri=[("Rinovim çatie", u('/rifacimento-tetto/')), ("Izolim termik", u('/cappotto-termico/')), ("Gipskarton dhe tavane të varura", u('/cartongesso-e-controsoffitti/')),
        ("Bonusi i rinovimit në Itali 2026", u('/bonus-ristrutturazione-2026/')), ("Danova Real Estate", u('/real-estate/'))],
 svc=svc("Izolim papafingo", "Izolim termik i papafingove dhe çative",
         "Izolimi i papafingove të shkelshme dhe të pashkelshme, mansardave dhe soletave në Veneto dhe Friuli Venezia Giulia, me pllaka, tavane të izoluara ose fryrje, dhe dokumente për ecobonus.",
         ["Papafingo e pashkelshme", "Papafingo e shkelshme", "Mansarda", "Izolim me fryrje", "Dosja ENEA"]))

P('/pavimentazioni-esterne/', hero="re-terrazzo-esterno", heroalt='Tarracë e rinovuar me pllaka të jashtme format të madh, kanal dhe hidroizolim',
 title="Shtrime të jashtme dhe tarraca në Veneto dhe Friuli | Çelës në dorë",
 desc="Shtrime të jashtme në Veneto dhe Friuli: tarraca, ballkone, oborre, shtigje dhe anë pishinash me pllaka, gur, kubëza ose rrëshirë, me hidroizolim dhe drenazh.",
 ogtitle="Shtrime të jashtme — Danova Real Estate", ogdesc="Tarraca, oborre dhe shtigje të rinovuara me bazë, pjerrësi dhe hidroizolim të sakta.",
 crumbs=[RE, ("Shtrime të jashtme", None)], eyebrow="Jashtë · tarraca, oborre, shtigje",
 h1=f"Shtrime të jashtme: {G}tarraca dhe oborre të bukura, pa rrjedhje.{_G}",
 lead="Rinovojmë tarraca, ballkone, oborre, shtigje, vende parkimi dhe anë pishinash për shtëpi, pallate, hotele dhe lokale: prishje, bazë, pjerrësi, hidroizolim, drenazh dhe shtrim me pllaka, gur, kubëza ose rrëshirë, me një person të vetëm kontakti dhe çmim të bllokuar.",
 cta1="Kërkoni inspektimin", cta2="Materialet",
 badges=["Tarraca dhe ballkone", "Oborre dhe shtigje", "Hidroizolim", "Çmim i bllokuar"],
 sezioni=[
  {"id": "in-breve", "tipo": "breve", "eyebrow": "Shkurt", "h2": f"Shtrimet e jashtme {G}në pak rreshta{_G}",
   "testo": "Një shtrim i jashtëm zgjat vetëm nëse poshtë është bërë mirë: bazë e qëndrueshme, <b>pjerrësi</b> të sakta drejt shkarkimeve, <b>hidroizolim</b> mbi tarracat që mbulojnë ambiente të banuara, fuga zgjerimi dhe materiale rezistente ndaj ngricës dhe jo të rrëshqitshme. Danova Real Estate rinovon tarraca, ballkone, oborre, shtigje, rampa, parkime dhe anë pishinash në të gjithë Veneton dhe Friuli Venezia Giulian.",
   "fatti": [("Ku", "Tarraca, ballkone, oborre, shtigje, parkime, pishina"), ("Materialet", "Pllaka, gur, kubëza, rrëshirë, kompozit"), ("Shtrimi", "Me ngjitës, mbi bazë, i ngritur ose i thatë"),
             ("Tarracat", "Hidroizolim dhe shkarkime të reja"), ("Lejet", "Të verifikuara me rregulloren e komunës"), ("Çmimi", "I bllokuar pas inspektimit")]},
  {"id": "promesse", "tipo": "promesse", "eyebrow": "Garancitë", "h2": f"Ambiente të jashtme të reja {G}pa surpriza{_G}"}],
 faqtitle=f"Pyetje për {G}shtrimet e jashtme.{_G}",
 faq=[("A më duhet leje?", "Rinovimi i një shtrimi ekzistues shpesh është punim i lirë në Itali, por varet nga rregullorja e komunës, sipërfaqja e përshkueshme e kërkuar dhe kufizimet e mundshme. E verifikojmë ne para se të fillojmë."),
      ("Sa kushton rinovimi i një tarrace ose oborri?", "Varet nga sipërfaqja, prishjet, gjendja e bazës, hidroizolimi dhe materiali. Nuk publikojmë lista çmimesh: pas inspektimit falas merrni një ofertë me shkrim me çmim të bllokuar.")] + FAQ_BASE[:3],
 ctabox={"h2": "Rinovojmë tarracën ose oborrin tuaj.", "p": "Na dërgoni disa foto dhe sipërfaqen e përafërt: caktojmë inspektimin falas.", "btn": "Kërkoni inspektimin"},
 altrititle="Faqe të lidhura",
 altri=[("Dysheme dhe dritare", u('/pavimenti-e-serramenti/')), ("Rinovim fasadash", u('/facciate-ventilate-e-rifacimento-facciate/')), ("Rinovim hotelesh", u('/ristrutturazione-hotel/')),
        ("Rinovim çatie", u('/rifacimento-tetto/')), ("Danova Real Estate", u('/real-estate/'))],
 svc=svc("Shtrime të jashtme", "Shtrim i ambienteve të jashtme",
         "Rinovimi i tarracave, ballkoneve, oborreve, shtigjeve, parkimeve dhe anëve të pishinave në Veneto dhe Friuli Venezia Giulia: prishje, bazë, hidroizolim, drenazh dhe shtrim.",
         ["Tarraca dhe ballkone", "Oborre dhe shtigje", "Parkime", "Anë pishinash", "Hidroizolime"]))
