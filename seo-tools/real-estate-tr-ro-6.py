# -*- coding: utf-8 -*-
"""26/10/2026 - Danova Real Estate, RO (6): guide costi della ristrutturazione e rifacimento del bagno."""
import importlib.util, os
_H = os.path.dirname(os.path.abspath(__file__))
def _ld(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(_H, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B = _ld('rro1', 'real-estate-tr-ro-1.py')
L, LANG, G, _G, u, RE, svc, A, FAQ_BASE = B.L, B.LANG, B.G, B._G, B.u, B.RE, B.svc, B.A, B.FAQ_BASE
PAGINE = []
def P(key, **k): PAGINE.append(dict(lang=LANG, key=key, url=u(key), faqtitle=f"Întrebări {G}frecvente.{_G}", altrititle="Lecturi conexe", **k))

P('/guide/quanto-costa-ristrutturare-casa/', hero='re-soggiorno-nuovo',
 title='Cât costă renovarea unei case în Italia: ce face prețul',
 desc='De ce depinde costul unei renovări în Italia și de ce prețul pe metru pătrat înșală: instalații, demolări, finisaje, autorizații, TVA 10% și deduceri fiscale 2026.',
 ogtitle='Cât costă renovarea unei case', ogdesc='Pozițiile care fac prețul unei renovări și cum compari ofertele.',
 crumbs=[RE, ('Costul renovării', None)], eyebrow='Ghid · Costuri și oferte',
 h1=f'Cât costă renovarea unei case: {G}ce face prețul.{_G}',
 lead='Două apartamente de aceeași suprafață pot costa foarte diferit la renovare. Iată de ce depinde cu adevărat prețul, cum citești o ofertă și cât contează TVA-ul și deducerile în Italia.',
 cta1='Cereți o ofertă gratuită', cta2='Pozițiile de cost',
 sezioni=[
  {'id': 'in-breve', 'tipo': 'breve', 'eyebrow': 'Ghid', 'h2': f'Pe scurt: {G}ce determină costul{_G}', 'testo': 'Costul unei <b>renovări</b> depinde de cinci factori: <b>cât se demolează</b>, <b>câte instalații se refac</b>, <b>nivelul finisajelor</b>, <b>starea structurii</b> și <b>autorizațiile</b> necesare. Prețul pe metru pătrat dă doar un ordin de mărime: o ofertă serioasă se face după inspecție, poziție cu poziție. În Italia renovările locuințelor au de obicei <b>TVA redus de 10%</b>, iar în 2026 <b>deduceri de 50%</b> pentru locuința principală și 36% pentru alte imobile.', 'fatti': [('Factor principal', 'Instalații și demolări'), ('Finisaje', 'Pot dubla costul'), ('Structură', 'Verificată la inspecție'), ('TVA', '10% la renovarea locuințelor'), ('Deducere 2026', '50% locuința principală, 36% altele'), ('Ofertă', 'Pe poziții, după inspecție')]},
  {'id': 'voci', 'tipo': 'cards', 'eyebrow': 'Pozițiile de cost', 'h2': f'Ce conține {G}o ofertă completă{_G}', 'corpo': [('Demolări și eliminare', 'Îndepărtarea pardoselilor, faianței, pereților și obiectelor sanitare, cu eliminare certificată a deșeurilor.'), ('Instalații', 'Electrice, sanitare, încălzire și eventual climatizare: poziția care variază cel mai mult.'), ('Lucrări de zidărie', 'Pereți, șape, tencuieli, goluri.'), ('Finisaje', 'Pardoseli, faianță, uși, ferestre, sanitare și vopsea: aici alegerea materialelor contează mult.'), ('Autorizații și tehnicieni', 'Releveu, proiect, CILA sau SCIA, diriginte de șantier, siguranță, cadastru și documente pentru bonus.'), ('Șantier', 'Protecții, eventual schelă, ocuparea domeniului public, curățenie finală.')]},
  {'id': 'mq', 'tipo': 'testo', 'eyebrow': 'Preț pe m²', 'h2': f'De ce prețul pe m² {G}înșală{_G}', 'corpo': ['<b>Prețul pe metru pătrat</b> găsit online amestecă lucrări foarte diferite. Într-un apartament de 80 m², a reface doar pardoselile și vopseaua este o lucrare; a reface și baia, bucătăria și toate instalațiile este alta. Aceeași suprafață, altă ofertă.', 'Contează și ce nu se vede: <b>instalații vechi</b> de refăcut complet, <b>ziduri umede</b>, grinzi sau planșee de consolidat, acces dificil (centre istorice, etaje fără lift, Veneția). De aceea inspecția vine înaintea oricărei cifre.']}],
 faq=[('De ce nu publicați prețuri?', 'Pentru că fiecare casă este diferită: instalațiile, structura, accesul și finisajele schimbă costul mai mult decât suprafața. Preferăm să venim și să vă dăm o ofertă scrisă pe poziții, la preț blocat.'), ('Inspecția și oferta sunt gratuite?', 'Da, gratuite și fără obligații în tot Veneto și Friuli Venezia Giulia.'), ('Cum compar două oferte?', 'Verificați să aibă aceleași lucrări, cantități, materiale și excluderi. Dacă lipsește o poziție, nu sunt comparabile.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Vreți să știți cât costă casa dvs.?', 'p': 'Inspecție gratuită și ofertă pe poziții, la preț blocat.', 'btn': 'Cereți o ofertă gratuită'},
 altri=[('Renovări la cheie', u('/ristrutturazioni-chiavi-in-mano/')), ('Bonus renovare Italia 2026', u('/bonus-ristrutturazione-2026/')), ('Cum alegi firma de renovări', u('/guide/come-scegliere-impresa-ristrutturazione/')), ('Ghid renovare baie', u('/guide/come-rifare-il-bagno/'))],
 svc=svc('Ghid costuri renovare', 'Ghid', 'Ce determină costul unei renovări în Italia, TVA, deduceri și cum citești o ofertă.', []))

P('/guide/come-rifare-il-bagno/', hero='re-bagno2-nuovo',
 title='Ghid renovare baie: etape, durată, autorizații, costuri',
 desc='Cum se renovează o baie pas cu pas: demolare, instalații, hidroizolație, faianță, durata șantierului, când e nevoie de CILA, bonusul 2026 și ce influențează costul.',
 ogtitle='Ghid renovare baie', ogdesc='Etape, durată, autorizații și alegerile care contează la renovarea băii.',
 crumbs=[RE, ('Ghid renovare baie', None)], eyebrow='Ghid · Baie',
 h1=f'Renovarea băii: {G}etape, durată, autorizații și costuri.{_G}',
 lead='Baia este camera renovată cel mai des și cea în care greșelile costă cel mai mult. Iată cum decurge lucrarea, cât durează, când e nevoie de autorizație și ce urcă sau coboară prețul.',
 cta1='Renovăm baia dvs.', cta2='Etapele',
 sezioni=[
  {'id': 'fasi', 'tipo': 'passi', 'eyebrow': 'Etapele', 'h2': f'Pas cu pas, {G}până la predare{_G}', 'corpo': [('Releveu și proiect', 'Măsurători, poziția scurgerilor, duș sau cadă, sanitare, mobilier și faianță, cu randare.'), ('Demolare', 'Îndepărtarea faianței, pardoselii, sanitarelor și căzii.'), ('Instalații', 'Țevi noi de alimentare și scurgere, lumini, prize, ventilator și, la cerere, încălzire în pardoseală.'), ('Șapă și hidroizolație', 'Pante pentru duș la nivelul pardoselii și membrană impermeabilă în zonele umede.'), ('Montaj', 'Pardoseală și faianță, cădiță sau rigolă, apoi sanitare, baterii, mobilier și oglindă.'), ('Probe și documente', 'Probe la instalații, curățenie, declarații de conformitate și documente pentru deducere.')]},
  {'id': 'costo', 'tipo': 'cards', 'eyebrow': 'Cost', 'h2': f'Alegerile care {G}mișcă prețul{_G}', 'corpo': [('Mutarea scurgerilor', 'Păstrarea wc-ului și a dușului pe loc costă mai puțin.'), ('Duș la nivelul pardoselii', 'Mai comod, cere șapă și hidroizolație atente.'), ('Formatul plăcilor', 'Plăcile mari cer montaj mai precis; formatele standard costă mai puțin.'), ('Faianță pe toată înălțimea sau parțial', 'Faianță doar în zonele umede și vopsea lavabilă în rest reduc costul.'), ('Sanitare și baterii', 'Suspendate sau pe pardoseală, termostatice sau clasice: gamă largă de prețuri.'), ('Mobilier la comandă', 'Folosește fiecare centimetru în băile mici; mobilierul de serie costă mai puțin.')]},
  {'id': 'permessi', 'tipo': 'testo', 'eyebrow': 'Autorizații și bonus', 'h2': f'E nevoie de CILA? {G}Și bonusul?{_G}', 'corpo': ['Înlocuirea doar a faianței și a sanitarelor în aceeași poziție este de obicei <b>întreținere obișnuită</b>, fără autorizație. Dacă se refac instalațiile sau se mută sanitare ori pereți, este de obicei <b>întreținere extraordinară</b> și e nevoie de <b>CILA</b>, pregătită de tehnicianul nostru. Pentru ea se aplică <b>bonusul de renovare</b>: în 2026, 50% pentru locuința principală și 36% pentru alte imobile.']}],
 faq=[('Cât costă renovarea completă a unei băi?', 'Depinde de dimensiuni, instalații, mutarea scurgerilor și mai ales de finisaje. Nu publicăm liste de prețuri: după inspecția gratuită primiți o ofertă pe poziții la preț blocat.'), ('Cât timp rămân fără baie?', 'Dacă este singura baie, organizăm lucrările ca zilele fără baie să fie cât mai puține și vi le spunem dinainte.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Sunteți gata pentru o baie nouă?', 'p': 'Trimiteți-ne o fotografie a băii actuale și orașul: stabilim inspecția gratuită.', 'btn': 'Renovăm baia dvs.'},
 altri=[('Renovare baie', u('/ristrutturazione-bagno/')), ('Costul renovării', u('/guide/quanto-costa-ristrutturare-casa/')), ('CILA sau SCIA', u('/guide/cila-o-scia/')), ('Bonus renovare Italia 2026', u('/bonus-ristrutturazione-2026/'))],
 svc=svc('Ghid renovare baie', 'Ghid', 'Etape, durată, autorizații, bonus și alegeri care influențează costul renovării unei băi.', []))

