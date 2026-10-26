# -*- coding: utf-8 -*-
"""26/10/2026 - Danova Real Estate, SQ (6): guide costi della ristrutturazione e rifacimento del bagno."""
import importlib.util, os
_H = os.path.dirname(os.path.abspath(__file__))
def _ld(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(_H, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B = _ld('rsq1', 'real-estate-tr-sq-1.py')
L, LANG, G, _G, u, RE, svc, A, FAQ_BASE = B.L, B.LANG, B.G, B._G, B.u, B.RE, B.svc, B.A, B.FAQ_BASE
PAGINE = []
def P(key, **k): PAGINE.append(dict(lang=LANG, key=key, url=u(key), faqtitle=f"Pyetje të {G}shpeshta.{_G}", altrititle="Lexime të lidhura", **k))

P('/guide/quanto-costa-ristrutturare-casa/', hero='re-soggiorno-nuovo',
 title='Sa kushton rinovimi i një shtëpie në Itali: çfarë e bën çmimin',
 desc='Nga çfarë varet kostoja e një rinovimi në Itali dhe pse çmimi për metër katror mashtron: impiante, prishje, përfundime, leje, TVSH 10% dhe zbritje fiskale 2026.',
 ogtitle='Sa kushton rinovimi i shtëpisë', ogdesc='Zërat që bëjnë çmimin e një rinovimi dhe si krahasohen ofertat.',
 crumbs=[RE, ('Kostoja e rinovimit', None)], eyebrow='Udhëzues · Kosto dhe oferta',
 h1=f'Sa kushton rinovimi i një shtëpie: {G}çfarë e bën çmimin.{_G}',
 lead='Dy apartamente me të njëjtën sipërfaqe mund të kushtojnë shumë ndryshe për t’u rinovuar. Ja nga çfarë varet vërtet çmimi, si lexohet një ofertë dhe sa ndikojnë TVSH-ja dhe zbritjet në Itali.',
 cta1='Kërkoni një ofertë falas', cta2='Zërat e kostos',
 sezioni=[
  {'id': 'in-breve', 'tipo': 'breve', 'eyebrow': 'Udhëzues', 'h2': f'Shkurt: {G}çfarë e përcakton koston{_G}', 'testo': 'Kostoja e një <b>rinovimi</b> varet nga pesë faktorë: <b>sa prishet</b>, <b>sa impiante rinovohen</b>, <b>niveli i përfundimeve</b>, <b>gjendja e strukturës</b> dhe <b>lejet</b> e nevojshme. Çmimi për metër katror jep vetëm një ide të përafërt: një ofertë serioze bëhet pas inspektimit, zë për zë. Në Itali rinovimet e banesave kanë zakonisht <b>TVSH të reduktuar 10%</b> dhe, në 2026, <b>zbritje fiskale 50%</b> për banesën kryesore dhe 36% për pronat e tjera.', 'fatti': [('Faktori kryesor', 'Impiantet dhe prishjet'), ('Përfundimet', 'Mund ta dyfishojnë koston'), ('Struktura', 'Kontrollohet në inspektim'), ('TVSH', '10% për rinovimin e banesave'), ('Zbritja 2026', '50% banesa kryesore, 36% të tjerat'), ('Oferta', 'Zë për zë, pas inspektimit')]},
  {'id': 'voci', 'tipo': 'cards', 'eyebrow': 'Zërat e kostos', 'h2': f'Çfarë përmban {G}një ofertë e plotë{_G}', 'corpo': [('Prishje dhe asgjësim', 'Heqja e dyshemeve, pllakave, mureve ndarëse dhe sanitareve, me asgjësim të certifikuar.'), ('Impiantet', 'Elektrike, hidraulike, ngrohje dhe ndoshta klimatizim: zëri që ndryshon më shumë.'), ('Punime murature', 'Mure ndarëse, betonime, suva, hapje.'), ('Përfundimet', 'Dysheme, pllaka, dyer, dritare, sanitare dhe bojë: këtu zgjedhja e materialeve peshon shumë.'), ('Leje dhe teknikë', 'Rilevim, projekt, CILA ose SCIA, drejtim punimesh, siguri, kadastër dhe dokumente për bonusin.'), ('Kantieri', 'Mbrojtje, skelë kur duhet, zënie e hapësirës publike, pastrim përfundimtar.')]},
  {'id': 'mq', 'tipo': 'testo', 'eyebrow': 'Çmimi për m²', 'h2': f'Pse çmimi për m² {G}mashtron{_G}', 'corpo': ['<b>Çmimi për metër katror</b> që gjendet në internet përzien punime shumë të ndryshme. Në një apartament 80 m², rinovimi vetëm i dyshemeve dhe bojës është një punë; rinovimi edhe i banjës, kuzhinës dhe gjithë impianteve është tjetër. E njëjta sipërfaqe, ofertë tjetër.', 'Ndikojnë edhe gjërat që nuk duken: <b>impiante të vjetra</b>, <b>mure me lagështi</b>, trarë ose soleta për t’u përforcuar, akses i vështirë (qendra historike, kate pa ashensor, Venecia). Prandaj inspektimi vjen para çdo shifre.']}],
 faq=[('Pse nuk publikoni çmime?', 'Sepse çdo shtëpi është ndryshe: impiantet, struktura, aksesi dhe përfundimet e ndryshojnë koston më shumë se sipërfaqja. Preferojmë të vijmë dhe t’ju japim një ofertë me shkrim zë për zë, me çmim të bllokuar.'), ('A janë falas inspektimi dhe oferta?', 'Po, falas dhe pa detyrime në të gjithë Veneton dhe Friuli Venezia Giulian.'), ('Si krahasoj dy oferta?', 'Kontrolloni që të kenë të njëjtat punime, sasi, materiale dhe përjashtime. Nëse mungon një zë, nuk janë të krahasueshme.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Doni të dini sa kushton shtëpia juaj?', 'p': 'Inspektim falas dhe ofertë zë për zë, me çmim të bllokuar.', 'btn': 'Kërkoni një ofertë falas'},
 altri=[('Rinovime çelës në dorë', u('/ristrutturazioni-chiavi-in-mano/')), ('Bonusi i rinovimit në Itali 2026', u('/bonus-ristrutturazione-2026/')), ('Si të zgjedhësh kompaninë e rinovimit', u('/guide/come-scegliere-impresa-ristrutturazione/')), ('Udhëzues rinovim banjoje', u('/guide/come-rifare-il-bagno/'))],
 svc=svc('Udhëzues për koston e rinovimit', 'Udhëzues', 'Çfarë e përcakton koston e një rinovimi në Itali, TVSH, zbritjet dhe si lexohet një ofertë.', []))

P('/guide/come-rifare-il-bagno/', hero='re-bagno2-nuovo',
 title='Udhëzues rinovim banjoje: hapat, kohëzgjatja, lejet, kostoja',
 desc='Si rinovohet një banjo hap pas hapi: prishje, impiante, hidroizolim, pllaka, kohëzgjatja e kantierit, kur duhet CILA, bonusi 2026 dhe çfarë ndikon në kosto.',
 ogtitle='Udhëzues rinovim banjoje', ogdesc='Hapat, kohëzgjatja, lejet dhe zgjedhjet që kanë rëndësi në rinovimin e banjës.',
 crumbs=[RE, ('Udhëzues rinovim banjoje', None)], eyebrow='Udhëzues · Banjo',
 h1=f'Rinovimi i banjës: {G}hapat, kohëzgjatja, lejet dhe kostoja.{_G}',
 lead='Banja është dhoma që rinovohet më shpesh dhe ajo ku gabimet kushtojnë më shumë. Ja si zhvillohet puna, sa zgjat, kur duhet leje dhe çfarë e rrit ose e ul çmimin.',
 cta1='Rinovojmë banjën tuaj', cta2='Hapat',
 sezioni=[
  {'id': 'fasi', 'tipo': 'passi', 'eyebrow': 'Hapat', 'h2': f'Hap pas hapi, {G}deri në dorëzim{_G}', 'corpo': [('Rilevim dhe projekt', 'Matje, pozicioni i shkarkimeve, dush apo vaskë, sanitare, mobilje dhe pllaka, me render.'), ('Prishja', 'Heqja e pllakave, dyshemesë, sanitareve dhe vaskës.'), ('Impiantet', 'Tuba të rinj furnizimi dhe shkarkimi, drita, priza, aspirator dhe, sipas dëshirës, ngrohje në dysheme.'), ('Betonimi dhe hidroizolimi', 'Pjerrësi për dushin në nivel të dyshemesë dhe membranë hidroizoluese në zonat e lagura.'), ('Shtrimi dhe montimi', 'Dysheme dhe mure, pjatë dushi ose kanal, pastaj sanitare, rubinete, mobilje dhe pasqyrë.'), ('Provat dhe dokumentet', 'Provë e impianteve, pastrim, deklarata konformiteti dhe dokumente për zbritjen.')]},
  {'id': 'costo', 'tipo': 'cards', 'eyebrow': 'Kostoja', 'h2': f'Zgjedhjet që {G}lëvizin çmimin{_G}', 'corpo': [('Zhvendosja e shkarkimeve', 'Mbajtja e wc-së dhe dushit në vend kushton më pak.'), ('Dush në nivel të dyshemesë', 'Më i rehatshëm, kërkon betonim dhe hidroizolim të kujdesshëm.'), ('Formati i pllakave', 'Pllakat e mëdha kërkojnë shtrim më të saktë; formatet standarde kushtojnë më pak.'), ('Pllaka deri në tavan ose pjesërisht', 'Pllaka vetëm në zonat e lagura dhe bojë e larëshme në pjesën tjetër ulin koston.'), ('Sanitare dhe rubinete', 'Të varura ose në dysheme, termostatike ose të zakonshme: gamë e gjerë çmimesh.'), ('Mobilje me porosi', 'Shfrytëzon çdo centimetër në banjot e vogla; mobiljet standarde kushtojnë më pak.')]},
  {'id': 'permessi', 'tipo': 'testo', 'eyebrow': 'Leje dhe bonus', 'h2': f'Duhet CILA? {G}Po bonusi?{_G}', 'corpo': ['Zëvendësimi vetëm i pllakave dhe sanitareve në të njëjtin pozicion zakonisht është <b>mirëmbajtje e zakonshme</b>, pa leje. Nëse rinovohen impiantet ose zhvendosen sanitare apo mure, zakonisht është <b>mirëmbajtje e jashtëzakonshme</b> dhe duhet <b>CILA</b>, që e përgatit tekniku ynë. Për të vlen <b>bonusi i rinovimit</b>: në 2026, 50% për banesën kryesore dhe 36% për pronat e tjera.']}],
 faq=[('Sa kushton rinovimi i plotë i një banjoje?', 'Varet nga përmasat, impiantet, zhvendosja e shkarkimeve dhe mbi të gjitha nga përfundimet. Nuk publikojmë lista çmimesh: pas inspektimit falas merrni një ofertë zë për zë me çmim të bllokuar.'), ('Sa kohë mbetem pa banjo?', 'Nëse është banja e vetme, i organizojmë punimet që ditët pa banjo të jenë sa më pak dhe jua themi më parë.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Gati për një banjo të re?', 'p': 'Na dërgoni një foto të banjës aktuale dhe qytetin: caktojmë inspektimin falas.', 'btn': 'Rinovojmë banjën tuaj'},
 altri=[('Rinovim banjoje', u('/ristrutturazione-bagno/')), ('Kostoja e rinovimit', u('/guide/quanto-costa-ristrutturare-casa/')), ('CILA apo SCIA', u('/guide/cila-o-scia/')), ('Bonusi i rinovimit në Itali 2026', u('/bonus-ristrutturazione-2026/'))],
 svc=svc('Udhëzues rinovim banjoje', 'Udhëzues', 'Hapat, kohëzgjatja, lejet, bonusi dhe zgjedhjet që ndikojnë në koston e rinovimit të një banjoje.', []))

