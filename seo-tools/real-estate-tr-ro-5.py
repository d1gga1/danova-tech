# -*- coding: utf-8 -*-
"""26/10/2026 - Danova Real Estate, RO (5): refacere acoperiș, izolare pod, pavaje exterioare."""
import importlib.util, os
_H = os.path.dirname(os.path.abspath(__file__))
def _ld(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(_H, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B = _ld('rro1', 'real-estate-tr-ro-1.py')
L, LANG, G, _G, u, RE, svc, A, FAQ_BASE = B.L, B.LANG, B.G, B._G, B.u, B.RE, B.svc, B.A, B.FAQ_BASE
PAGINE = []
def P(key, **k): PAGINE.append(dict(lang=LANG, key=key, url=u(key), **k))

P('/rifacimento-tetto/', hero="re-tetto-cantiere", heroalt='Refacerea unui acoperiș în Veneto: schelă, izolație, membrană și țiglă nouă',
 title="Refacere acoperiș în Veneto și Friuli | Acoperișuri izolate la cheie",
 desc="Refacere acoperiș la cheie în Veneto și Friuli: structură, izolație, hidroizolație, țiglă și jgheaburi, cu autorizații și deduceri fiscale.",
 ogtitle="Refacere acoperiș — Danova Real Estate", ogdesc="Un acoperiș nou, izolat și etanș: un singur responsabil de la schelă la jgheaburi, la preț blocat.",
 crumbs=[RE, ("Refacere acoperiș", None)], eyebrow="Acoperișuri · Veneto și Friuli",
 h1=f"Refacere acoperiș: {G}un acoperiș nou, izolat și fără infiltrații.{_G}",
 lead="Refacem acoperișuri de case, vile, blocuri și hale: schelă, demontarea învelitorii, verificarea sau refacerea structurii, izolație, hidroizolație, țiglă, jgheaburi și linie de viață. Cu autorizații și documente pentru deducerile fiscale italiene, la preț blocat și cu termene scrise în contract.",
 cta1="Cereți inspecția", cta2="Ce include",
 badges=["Ventilat și izolat", "Schelă inclusă", "Preț blocat", "Deduceri 2026"],
 sezioni=[
  {"id": "in-breve", "tipo": "breve", "eyebrow": "Pe scurt", "h2": f"Refacerea acoperișului {G}în câteva rânduri{_G}",
   "testo": "<b>Refacerea acoperișului</b> include demontarea învelitorii vechi, verificarea structurii din lemn sau beton (și înlocuirea ei unde e nevoie), <b>izolația termică</b>, <b>membrana hidroizolantă</b> și șipcile pentru <b>ventilare</b>, noua învelitoare din țiglă sau tablă, jgheaburile și burlanele și <b>linia de viață</b> unde este obligatorie. Danova Real Estate se ocupă de tot cu un singur responsabil, în <b>Veneto și Friuli Venezia Giulia</b>.",
   "fatti": [("Clădiri", "Case, vile, blocuri, hale"), ("Structură", "Lemn, beton, oțel"), ("Izolație", "Plăci, fibră de lemn, vată bazaltică"),
             ("Învelitoare", "Țiglă, olane, tablă, panouri"), ("Deducere 2026", "50% locuința principală, 36% altele"), ("Autorizații", "CILA sau SCIA, ne ocupăm noi")]},
  {"id": "cosa", "tipo": "cards", "eyebrow": "Ce include", "h2": f"De la schelă {G}la jgheab{_G}",
   "corpo": [("Schelă și siguranță", "Montarea schelei, protecții și planul de siguranță."), ("Demontare și eliminare", "Azbocimentul (eternit) este îndepărtat de firme autorizate, cu plan de lucru depus la autoritatea sanitară."),
             ("Structură", "Verificarea grinzilor și a dulapilor; înlocuire sau consolidare, cu proiect de rezistență unde e nevoie."), ("Izolație și ventilare", "Plăci izolante, barieră de vapori, strat de ventilare: mai cald iarna, mai răcoros vara."),
             ("Hidroizolație și învelitoare", "Membrane respirabile, țiglă sau tablă, coame și piese speciale."), ("Tinichigerie și linie de viață", "Jgheaburi, burlane, șorțuri și sisteme anticădere conform normelor regionale.")]},
  {"id": "promesse", "tipo": "promesse", "eyebrow": "Garanții", "h2": f"Un acoperiș nou {G}fără surprize{_G}"}],
 faqtitle=f"Întrebări despre {G}refacerea acoperișului.{_G}",
 faq=[("Cât costă refacerea acoperișului?", "Depinde de suprafață, formă, starea structurii, izolație, învelitoare și accesul pentru schelă. De aceea nu publicăm liste de prețuri: după inspecția gratuită primiți o ofertă scrisă la preț blocat, iar deducerile fiscale reduc costul real."),
      ("Cât durează lucrarea?", "La o casă individuală de obicei câteva săptămâni, cu schelă și jgheaburi; data de finalizare o scriem în contract. Casa nu rămâne niciodată descoperită pe ploaie."),
      ("Îndepărtați și acoperișurile din eternit?", "Da, prin firme specializate autorizate: plan de lucru, îndepărtare, eliminare certificată și apoi acoperișul nou, totul coordonat de noi.")] + FAQ_BASE[:3],
 ctabox={"h2": "Acoperișul dvs. are nevoie de noi?", "p": "Trimiteți-ne adresa și câteva fotografii ale acoperișului sau ale infiltrațiilor: stabilim inspecția gratuită.", "btn": "Cereți inspecția"},
 altrititle="Pagini conexe",
 altri=[("Izolare pod", u('/isolamento-sottotetto/')), ("Izolație termică", u('/cappotto-termico/')), ("Blocuri și hale", u('/ristrutturazione-condomini-e-capannoni/')),
        ("Bonus renovare Italia 2026", u('/bonus-ristrutturazione-2026/')), ("Danova Real Estate", u('/real-estate/'))],
 svc=svc("Refacere acoperiș", "Lucrări de acoperiș",
         "Refacere acoperișuri în Veneto și Friuli Venezia Giulia, Italia: schelă, demontare, structură, izolație, hidroizolație, învelitoare, jgheaburi și linie de viață, cu autorizații și deduceri fiscale.",
         ["Schelă", "Demontare și eternit", "Structura acoperișului", "Izolație și ventilare", "Învelitoare", "Jgheaburi și linie de viață"]))

P('/isolamento-sottotetto/', hero="re-sottotetto-insufflaggio", heroalt='Izolarea podului prin insuflare de vată minerală pe planșeu',
 title="Izolare pod și insuflare în Veneto și Friuli",
 desc="Izolarea podului circulabil sau necirculabil și izolație insuflată în Veneto și Friuli: pierderi de căldură mai mici, puțin praf, lucrări rapide și documente pentru ecobonus.",
 ogtitle="Izolare pod — Danova Real Estate", ogdesc="Cel mai rapid mod de a opri pierderea căldurii prin acoperiș: izolarea planșeului podului sau a pantelor, și prin insuflare.",
 crumbs=[RE, ("Izolare pod", None)], eyebrow="Izolație termică · acoperiș și pod",
 h1=f"Izolarea podului: {G}căldura rămâne în casă.{_G}",
 lead="Izolăm poduri circulabile și necirculabile, mansarde și planșee spre spații neîncălzite: cu plăci montate uscat, cu tavane și pereți din rigips izolați sau prin insuflarea materialului izolant în goluri. Lucrări rapide, curate și cu documentele pentru deducerile fiscale.",
 cta1="Cereți inspecția", cta2="Soluții",
 badges=["Circulabil sau nu", "Insuflare", "Gata în câteva zile", "Ecobonus 2026"],
 sezioni=[
  {"id": "in-breve", "tipo": "breve", "eyebrow": "Pe scurt", "h2": f"Izolarea podului {G}în câteva rânduri{_G}",
   "testo": "Într-o casă neizolată o mare parte din căldură se pierde prin acoperiș și ultimul planșeu. <b>Izolarea podului</b> se face pe planșeul dintre camerele încălzite și podul rece sau pe pantele acoperișului dacă mansarda este locuită: cu <b>plăci izolante</b>, cu <b>tavane izolate din rigips</b> sau prin <b>insuflare</b>, fără a reface acoperișul.",
   "fatti": [("Unde", "Planșeul podului, pante, mansarde, goluri"), ("Metode", "Plăci, tavane izolate, insuflare"), ("Materiale", "Vată minerală, fibră de lemn, celuloză, EPS"),
             ("Durată", "De obicei câteva zile"), ("Deducere 2026", "Ecobonus 50% locuința principală, 36% altele"), ("Preț", "Blocat după inspecție")]},
  {"id": "soluzioni", "tipo": "cards", "eyebrow": "Soluții", "h2": f"Ce izolație {G}pentru podul dvs.{_G}",
   "corpo": [("Pod necirculabil", "Plăci sau saltele pe planșeu ori material insuflat: rapid și fără demolări."), ("Pod circulabil", "Plăci rezistente cu pardoseală deasupra, ca podul să rămână depozit."),
             ("Mansardă locuită", "Izolarea pantelor din interior cu tavane izolate din rigips sau din exterior la refacerea acoperișului."), ("Insuflare", "Fulgi sau granule izolante suflate prin orificii mici, apoi închise."),
             ("Barieră de vapori", "Unde e nevoie, contra condensului și mucegaiului."), ("Trape de acces", "Izolate și etanșe, ca lucrarea să nu fie inutilă.")]},
  {"id": "promesse", "tipo": "promesse", "eyebrow": "Garanții", "h2": f"O izolație {G}făcută corect{_G}"}],
 faqtitle=f"Întrebări despre {G}izolarea podului.{_G}",
 faq=[("Ce este izolația insuflată?", "Material izolant vrac (fulgi de vată minerală, celuloză sau granule) este suflat în golurile planșeelor și pereților sau pe planșeul unui pod necirculabil. Durează câteva ore sau zile, fără demolări și cu foarte puțin praf."),
      ("Cât costă izolarea podului?", "Depinde de suprafață, acces, material și grosime. Nu publicăm liste de prețuri: după inspecția gratuită primiți o ofertă scrisă la preț blocat, iar ecobonusul reduce costul real.")] + FAQ_BASE[:3],
 ctabox={"h2": "Izolăm podul dvs.", "p": "Adresa, tipul casei și accesul la pod: venim să vedem și vă propunem soluția.", "btn": "Cereți inspecția"},
 altrititle="Pagini conexe",
 altri=[("Refacere acoperiș", u('/rifacimento-tetto/')), ("Izolație termică", u('/cappotto-termico/')), ("Rigips și tavane false", u('/cartongesso-e-controsoffitti/')),
        ("Bonus renovare Italia 2026", u('/bonus-ristrutturazione-2026/')), ("Danova Real Estate", u('/real-estate/'))],
 svc=svc("Izolare pod", "Izolație termică pentru poduri și acoperișuri",
         "Izolarea podurilor circulabile și necirculabile, a mansardelor și planșeelor în Veneto și Friuli Venezia Giulia, cu plăci, tavane izolate sau insuflare, și documente pentru ecobonus.",
         ["Pod necirculabil", "Pod circulabil", "Mansarde", "Insuflare", "Dosar ENEA"]))

P('/pavimentazioni-esterne/', hero="re-terrazzo-esterno", heroalt='Terasă refăcută cu gresie de exterior format mare, rigolă și hidroizolație',
 title="Pavaje exterioare și terase în Veneto și Friuli | La cheie",
 desc="Pavaje exterioare în Veneto și Friuli: terase, balcoane, curți, alei și margini de piscină din gresie, piatră, pavele sau rășină, cu hidroizolație și drenaj.",
 ogtitle="Pavaje exterioare — Danova Real Estate", ogdesc="Terase, curți și alei refăcute cu șapă, pante și hidroizolații corecte.",
 crumbs=[RE, ("Pavaje exterioare", None)], eyebrow="Exterior · terase, curți, alei",
 h1=f"Pavaje exterioare: {G}terase și curți frumoase, fără infiltrații.{_G}",
 lead="Refacem terase, balcoane, curți, alei, locuri de parcare și margini de piscină pentru case, blocuri, hoteluri și localuri: demolare, șapă, pante, hidroizolație, drenaj și montaj de gresie, piatră, pavele sau rășină, cu un singur responsabil și la preț blocat.",
 cta1="Cereți inspecția", cta2="Materiale",
 badges=["Terase și balcoane", "Curți și alei", "Hidroizolație", "Preț blocat"],
 sezioni=[
  {"id": "in-breve", "tipo": "breve", "eyebrow": "Pe scurt", "h2": f"Pavajele exterioare {G}în câteva rânduri{_G}",
   "testo": "Un pavaj exterior rezistă doar dacă dedesubt totul este făcut bine: bază stabilă, <b>pante</b> corecte spre scurgeri, <b>hidroizolație</b> pe terasele de deasupra spațiilor locuite, rosturi de dilatare și materiale rezistente la îngheț și antiderapante. Danova Real Estate reface terase, balcoane, curți, alei, rampe, parcări și margini de piscină în tot Veneto și Friuli Venezia Giulia.",
   "fatti": [("Unde", "Terase, balcoane, curți, alei, parcări, piscine"), ("Materiale", "Gresie, piatră, pavele, rășină, compozit"), ("Montaj", "Lipit, pe șapă, înălțat sau uscat"),
             ("Terase", "Hidroizolație și scurgeri noi"), ("Autorizații", "Verificate cu regulamentul local"), ("Preț", "Blocat după inspecție")]},
  {"id": "promesse", "tipo": "promesse", "eyebrow": "Garanții", "h2": f"Exterioare noi {G}fără surprize{_G}"}],
 faqtitle=f"Întrebări despre {G}pavajele exterioare.{_G}",
 faq=[("Am nevoie de autorizație?", "Refacerea unui pavaj existent este adesea lucrare liberă în Italia, dar depinde de regulamentul comunei, de suprafața permeabilă cerută și de eventualele restricții. Verificăm noi înainte de a începe."),
      ("Cât costă refacerea unei terase sau a unei curți?", "Depinde de suprafață, demolări, starea bazei, hidroizolație și material. Nu publicăm liste de prețuri: după inspecția gratuită primiți o ofertă scrisă la preț blocat.")] + FAQ_BASE[:3],
 ctabox={"h2": "Refacem terasa sau curtea dvs.", "p": "Trimiteți-ne câteva fotografii și suprafața aproximativă: stabilim inspecția gratuită.", "btn": "Cereți inspecția"},
 altrititle="Pagini conexe",
 altri=[("Pardoseli și tâmplărie", u('/pavimenti-e-serramenti/')), ("Renovare fațade", u('/facciate-ventilate-e-rifacimento-facciate/')), ("Renovare hoteluri", u('/ristrutturazione-hotel/')),
        ("Refacere acoperiș", u('/rifacimento-tetto/')), ("Danova Real Estate", u('/real-estate/'))],
 svc=svc("Pavaje exterioare", "Montaj de pavaje exterioare",
         "Refacerea teraselor, balcoanelor, curților, aleilor, parcărilor și marginilor de piscină în Veneto și Friuli Venezia Giulia: demolare, șapă, hidroizolație, drenaj și montaj.",
         ["Terase și balcoane", "Curți și alei", "Parcări", "Margini de piscină", "Hidroizolații"]))
