# -*- coding: utf-8 -*-
"""26/10/2026 - Danova Real Estate, EN (6): guide costi della ristrutturazione e rifacimento del bagno."""
import importlib.util, os
_H = os.path.dirname(os.path.abspath(__file__))
def _ld(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(_H, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B = _ld('ren1', 'real-estate-tr-en-1.py')
L, LANG, G, _G, u, RE, svc, A, FAQ_BASE = B.L, B.LANG, B.G, B._G, B.u, B.RE, B.svc, B.A, B.FAQ_BASE
PAGINE = []
def P(key, **k): PAGINE.append(dict(lang=LANG, key=key, url=u(key), faqtitle=f"Frequently asked {G}questions.{_G}", altrititle="Related reading", **k))

P('/guide/quanto-costa-ristrutturare-casa/', hero='re-soggiorno-nuovo',
 title='How much does it cost to renovate a house in Italy?',
 desc='What drives the cost of a renovation in Italy and why price per square metre misleads: systems, demolition, finishes, permits, 10% VAT and 2026 tax deductions.',
 ogtitle='Renovation costs in Italy', ogdesc='The items that make up the price of a renovation and how to compare quotes.',
 crumbs=[RE, ('Renovation costs', None)], eyebrow='Guide · Costs and quotes',
 h1=f'How much does it cost to renovate a house: {G}what makes up the price.{_G}',
 lead='Two apartments of the same size can cost very differently to renovate. Here is what really drives the price, how to read a quote and how Italian VAT and tax deductions affect it.',
 cta1='Request a free quote', cta2='Cost items',
 sezioni=[
  {'id': 'in-breve', 'tipo': 'breve', 'eyebrow': 'Guide', 'h2': f'In short: {G}what drives the cost{_G}', 'testo': 'The cost of a <b>renovation</b> depends on five factors: <b>how much is demolished</b>, <b>how many systems are replaced</b>, the <b>level of finishes</b>, the <b>condition of the structure</b> and the <b>permits</b> needed. Price per square metre only gives an order of magnitude: a serious quote comes after the survey, item by item. In Italy home renovations usually carry <b>reduced 10% VAT</b> and, in 2026, <b>tax deductions of 50%</b> on the main residence and 36% on other properties.', 'fatti': [('Main factor', 'Systems and demolition'), ('Finishes', 'Can double the cost'), ('Structure', 'Checked at the survey'), ('VAT', '10% on home renovation work'), ('2026 deduction', '50% main home, 36% other'), ('Quote', 'Itemised, after the survey')]},
  {'id': 'voci', 'tipo': 'cards', 'eyebrow': 'Cost items', 'h2': f'What a complete quote {G}contains{_G}', 'corpo': [('Demolition and disposal', 'Removal of floors, tiles, partitions and fixtures, with certified waste disposal.'), ('Systems', 'Electrical, plumbing, heating and possibly air conditioning: the item that varies most from home to home.'), ('Building works', 'Partitions, screeds, plaster, openings.'), ('Finishes', 'Floors, tiles, doors, windows, fixtures and paint: material choice weighs heavily here.'), ('Permits and professionals', 'Survey, design, CILA or SCIA, site supervision, safety, land registry update and bonus documents.'), ('Site', 'Protection, scaffolding if needed, public-land permits, final cleaning.')]},
  {'id': 'mq', 'tipo': 'testo', 'eyebrow': 'Price per m²', 'h2': f'Why price per m² {G}misleads{_G}', 'corpo': ['The <b>price per square metre</b> found online lumps together very different jobs. In an 80 m² apartment, redoing floors and paint is one job; also redoing bathroom, kitchen and all systems is another. Same size, different quote.', 'Hidden factors matter too: <b>non-compliant systems</b> to replace entirely, <b>damp walls</b>, beams or floors to reinforce, difficult access for materials (historic centres, upper floors without a lift, Venice). That is why the survey comes before any figure.']}],
 faq=[('Why don’t you publish prices?', 'Because every home is different: systems, structure, access and finishes change the cost more than floor area. We prefer to visit and give you a written, itemised fixed-price quote rather than a figure that grows on site.'), ('Are the survey and quote free?', 'Yes, free and without obligation across Veneto and Friuli Venezia Giulia.'), ('How do I compare two quotes?', 'Check that they have the same works, quantities, materials and exclusions. If an item is missing from one, they are not comparable.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Want to know what your home will cost?', 'p': 'Free survey and itemised fixed-price quote.', 'btn': 'Request a free quote'},
 altri=[('Turnkey renovation', u('/ristrutturazioni-chiavi-in-mano/')), ('Italian renovation bonus 2026', u('/bonus-ristrutturazione-2026/')), ('How to choose a renovation company', u('/guide/come-scegliere-impresa-ristrutturazione/')), ('Bathroom renovation guide', u('/guide/come-rifare-il-bagno/'))],
 svc=svc('Renovation cost guide', 'Guide', 'What determines the cost of a renovation in Italy, VAT, deductions and how to read a quote.', []))

P('/guide/come-rifare-il-bagno/', hero='re-bagno2-nuovo',
 title='Bathroom renovation guide: steps, timing, permits, costs',
 desc='How a bathroom renovation works step by step: demolition, plumbing, waterproofing, tiling, site time, when a CILA is needed, 2026 Italian bonus and what affects the cost.',
 ogtitle='Bathroom renovation guide', ogdesc='Steps, timing, permits and the choices that matter when renovating a bathroom.',
 crumbs=[RE, ('Bathroom renovation guide', None)], eyebrow='Guide · Bathroom',
 h1=f'Renovating a bathroom: {G}steps, timing, permits and costs.{_G}',
 lead='The bathroom is the room renovated most often, and the one where mistakes cost most. Here is how the work goes, how long it takes, when a permit is needed and what pushes the price up or down.',
 cta1='Renovate your bathroom', cta2='Steps',
 sezioni=[
  {'id': 'fasi', 'tipo': 'passi', 'eyebrow': 'Steps', 'h2': f'Step by step, {G}from survey to keys{_G}', 'corpo': [('Survey and design', 'Measurements, drain positions, shower or bath, fixtures, vanity and tiles, with a render.'), ('Demolition', 'Removal of tiles, floor, fixtures and bath, with waste disposal.'), ('Systems', 'New supply and drain pipes, lights, sockets, extractor fan and, if wanted, underfloor heating.'), ('Screed and waterproofing', 'Falls for a level-access shower and waterproof membrane in wet areas.'), ('Tiling and fitting', 'Floor and wall tiles, shower tray or drain, then fixtures, taps, vanity and mirror.'), ('Testing and documents', 'System tests, cleaning, compliance certificates and tax-deduction documents.')]},
  {'id': 'costo', 'tipo': 'cards', 'eyebrow': 'Cost', 'h2': f'Choices that push {G}the price up or down{_G}', 'corpo': [('Moving drains', 'Keeping toilet and shower in place costs less; moving them needs new falls.'), ('Level-access shower', 'More comfortable, needs careful screed and waterproofing.'), ('Tile size', 'Large slabs need more precise laying; standard sizes cost less.'), ('Full or partial tiling', 'Tiling only wet areas and painting the rest saves money.'), ('Fixtures and taps', 'Wall-hung or floor-standing, thermostatic or mixer: a wide price range.'), ('Custom vanity', 'Uses every centimetre in small bathrooms; standard units cost less.')]},
  {'id': 'permessi', 'tipo': 'testo', 'eyebrow': 'Permits and bonus', 'h2': f'Do you need a CILA? {G}And the bonus?{_G}', 'corpo': ['Replacing only tiles and fixtures in the same position is usually <b>ordinary maintenance</b>, with no permit. Redoing systems or moving fixtures or walls is usually <b>extraordinary maintenance</b> and needs a <b>CILA</b>, which our technician prepares. Extraordinary maintenance qualifies for the Italian <b>renovation bonus</b>: 50% on the main residence and 36% on other properties in 2026.']}],
 faq=[('How much does a full bathroom renovation cost?', 'It depends on size, systems, drain changes and above all the finishes chosen. We do not publish price lists: after the free survey you get an itemised fixed-price quote.'), ('How long will I be without a bathroom?', 'If it is the only one, we plan the works to keep the days without facilities to a minimum and tell you in advance.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Ready for a new bathroom?', 'p': 'Send us a photo of your current bathroom and the town: we will arrange the free survey.', 'btn': 'Renovate your bathroom'},
 altri=[('Bathroom renovation', u('/ristrutturazione-bagno/')), ('Renovation costs', u('/guide/quanto-costa-ristrutturare-casa/')), ('CILA or SCIA', u('/guide/cila-o-scia/')), ('Italian renovation bonus 2026', u('/bonus-ristrutturazione-2026/'))],
 svc=svc('Bathroom renovation guide', 'Guide', 'Steps, timing, permits, bonus and the choices that affect the cost of a bathroom renovation.', []))

