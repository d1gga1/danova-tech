# -*- coding: utf-8 -*-
"""Aggiunge alle pagine di servizio gia' esistenti una sezione con le citta',
   invece di creare decine di pagine sottili quasi identiche."""
import os, re, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def e(s): return html.escape(s, quote=False)

SEZ = {
 'de/leistungen/google-ads': dict(
  id='staedte', eyebrow='Nach Stadt',
  h2='Google-Ads-Agentur <span class="grad">für Ihre Stadt</span>',
  lead='Der Ablauf ist überall derselbe. Was sich unterscheidet, sind Klickpreise, Wettbewerbsdichte und die Sprache, in der Ihre Kunden suchen. Ein paar Beobachtungen aus Konten, die wir betreut haben.',
  voci=[
   ('Google Ads Agentur Berlin','Viele Onlineshops und junge Unternehmen bieten auf dieselben breiten Begriffe. Der Gewinn liegt fast immer in engeren Anzeigengruppen und in sauber ausgeschlossenen Suchbegriffen, nicht in einem höheren Budget.'),
   ('Google Ads Agentur München','Der teuerste B2B-Klickmarkt Deutschlands. Das ist tragbar, weil eine einzige Anfrage bei Industriezulieferern fünfstellig sein kann — aber nur mit sauber gemessenen Conversions statt gezählter Klicks.'),
   ('Google Ads Agentur Hamburg','Handel, Logistik und Import prägen die Nachfrage. Suchanfragen sind oft sehr konkret auf Ware, Menge und Abwicklung bezogen, was enge Kampagnen mit klarer Zielseite belohnt.'),
   ('Google Ads Agentur Köln','Handel, Messegeschäft und Dienstleistung. Köln und Düsseldorf sollte man als ein Einzugsgebiet planen, nicht als zwei Konten: sonst bieten Ihre eigenen Kampagnen gegeneinander.'),
   ('Google Ads Agentur Düsseldorf','Beratung, Handel und Mode, dazu viel internationaler Mittelstand. Zweisprachige Kampagnen auf Deutsch und Englisch sind hier häufiger sinnvoll als anderswo.'),
   ('Google Ads Agentur Stuttgart','Maschinenbau und Automobilzulieferer. Die Suchbegriffe sind technisch und volumenarm, die Anfragen dafür wertvoll. Wer hier mit Marketingsprache statt Fachsprache bietet, zahlt für die falschen Klicks.'),
   ('Google Ads Agentur Frankfurt','Finanz- und Beratungsdienstleistungen mit sehr hohen Klickpreisen. Anzeigentexte müssen zusätzlich die Vorgaben der Branche einhalten, was die Gestaltungsfreiheit real einschränkt.'),
   ('Google Ads Agentur Leipzig','Deutlich niedrigere Klickpreise als in München oder Frankfurt, bei wachsender Nachfrage. Für Unternehmen mit begrenztem Budget oft der Markt mit dem besten Verhältnis von Einsatz und Ertrag.'),
   ('Google Ads Agentur Wien','Kampagnen laufen auf google.at und stehen in einem kleineren Wettbewerb: für dieselbe Branche zahlt man häufig spürbar weniger je Klick als in Deutschland.'),
   ('Google Ads Agentur Zürich','Hohe Kaufkraft, hohe Klickpreise, Abrechnung in Franken. Entscheidend sind die richtige Landes- und Sprachausrichtung und getrennte Kampagnen für die Deutschschweiz.')]),
 'de/leistungen/seo': dict(
  id='staedte', eyebrow='Nach Stadt',
  h2='SEO-Agentur <span class="grad">für Ihre Stadt</span>',
  lead='Für München, Berlin und Wien haben wir eigene Seiten. Für die übrigen deutschsprachigen Märkte hier das Wesentliche in je zwei Sätzen — Wettbewerb, Besonderheiten und was zuerst zu tun ist.',
  voci=[
   ('SEO-Agentur Hamburg','Handel, Logistik und Medien. Ein großer Teil der Nachfrage läuft über sehr konkrete Produkt- und Abwicklungsfragen, die auf Kategorieseiten gehören und nicht auf die Startseite.'),
   ('SEO-Agentur Köln','Hohe Agenturdichte und entsprechend guter Wettbewerb auf den breiten Begriffen. Der Einstieg gelingt über Stadtteil- und Leistungsseiten, die fast niemand ordentlich pflegt.'),
   ('SEO-Agentur Düsseldorf','Viel internationaler Mittelstand: Eine saubere englische Version mit eigenen Adressen und hreflang bringt hier regelmäßig mehr als weitere Monate Arbeit an der deutschen Seite.'),
   ('SEO-Agentur Stuttgart','Maschinenbau und Zulieferindustrie suchen technisch und in Fachsprache. Wer die Begriffe seiner Kunden verwendet statt der eigenen Marketingsprache, steht oft nach wenigen Monaten vorn.'),
   ('SEO-Agentur Frankfurt','Finanzen, Beratung und Logistik, mit starkem Wettbewerb und hohen Ansprüchen an Nachweisbarkeit. Inhalte müssen fachlich belegt sein, sonst halten sie die Position nicht.'),
   ('SEO-Agentur Leipzig','Ein wachsender Markt mit deutlich geringerem Wettbewerb. Positionen, die in München zwölf Monate kosten, sind hier häufig in vier bis sechs Monaten erreichbar.'),
   ('SEO-Agentur Zürich','Schweizer Suchergebnisse folgen eigenen Signalen: .ch-Domain, Schweizer Adresse und Verweise von Schweizer Seiten. Eine deutsche Seite rankt in der Schweiz selten von allein.'),
   ('SEO-Agentur Bern','Kleinerer, ruhigerer Markt mit zweisprachigem Umfeld. Wer Deutsch und Französisch sauber trennt, bedient zwei Suchmärkte mit einer Website.')]),
 'fr/agence-seo-france': dict(
  id='villes', eyebrow='Par ville',
  h2='Agence SEO <span class="grad">dans votre ville</span>',
  lead='La méthode ne change pas d\'une ville à l\'autre. Ce qui change, c\'est la concurrence et le tissu économique local. Bordeaux a sa page dédiée ; voici l\'essentiel pour les autres.',
  voci=[
   ('Agence SEO Nantes','Marché dynamique et concurrence encore modérée. Le numérique local y est bien installé, ce qui veut dire des concurrents corrects mais rarement excellents : l\'écart se fait sur le contenu.'),
   ('Agence SEO Toulouse','Aéronautique, spatial et sous-traitance technique. Les requêtes sont précises et en langage métier ; les pages génériques y tiennent mal la première place.'),
   ('Agence SEO Montpellier','Beaucoup de petites structures et de professions libérales. La fiche d\'établissement et les avis pèsent souvent plus que le référencement national.'),
   ('Agence SEO Rennes','Agroalimentaire et services aux entreprises, avec une concurrence plus faible que la moyenne. Les positions s\'obtiennent vite quand la base technique est saine.'),
   ('Agence SEO Lille','Commerce, logistique et e-commerce, avec un débouché belge naturel. Une version adaptée au marché belge est un levier que peu d\'entreprises exploitent.'),
   ('Agence SEO Nice','Tourisme, immobilier et services, avec une part de recherche en anglais et en italien plus forte qu\'ailleurs en France.'),
   ('Agence SEO Strasbourg','Position frontalière avec l\'Allemagne : une version allemande correctement installée ouvre un marché voisin bien plus grand que le marché local.'),
   ('Agence SEO Marseille','Port, logistique et commerce méditerranéen. Les espaces clients et le suivi de dossier rapportent souvent plus que la refonte graphique du site vitrine.')]),
 'es/agencia-seo-espana': dict(
  id='ciudades', eyebrow='Por ciudad',
  h2='Agencia SEO <span class="grad">en tu ciudad</span>',
  lead='El método no cambia de una ciudad a otra. Lo que cambia es la competencia y el tejido económico. Valencia tiene página propia; aquí va lo esencial del resto.',
  voci=[
   ('Agencia SEO Madrid','El mercado más competido de España: en casi cualquier búsqueda comercial hay diez empresas haciendo SEO en serio. Se entra por búsquedas concretas, nunca por las genéricas con "Madrid" dentro.'),
   ('Agencia SEO Barcelona','Competencia alta y una particularidad útil: buena parte de las búsquedas se hacen en catalán. Trabajar las dos lenguas bien separadas es una ventaja que muchos competidores no aprovechan.'),
   ('Agencia SEO Sevilla','Competencia bastante menor que en Madrid o Barcelona. Lo que allí lleva doce meses, aquí suele conseguirse en cuatro o seis con un trabajo parecido.'),
   ('Agencia SEO Bilbao','Industria, ingeniería y servicios técnicos. Las búsquedas son precisas y en lenguaje de oficio; las páginas genéricas aguantan mal la primera posición.'),
   ('Agencia SEO Zaragoza','Logística y agroalimentario, con poca competencia digital real. Un buen trabajo técnico basta a menudo para subir sin necesidad de grandes inversiones en contenidos.'),
   ('Agencia SEO Málaga','Turismo, servicios y un polo tecnológico en crecimiento, con mucha búsqueda en inglés. Una versión inglesa bien montada abre un mercado que la competencia local suele dejar libre.'),
   ('Agencia SEO Alicante','Calzado, turismo y construcción, con exportación hacia Europa. La versión en otro idioma rinde con frecuencia más que meses extra sobre la española.'),
   ('Agencia SEO Murcia','Agroalimentario y exportación hortofrutícola. El comprador está en Alemania, Francia o Reino Unido y busca en su idioma: ahí está el hueco.')]),
}

def sezione(d):
    o=['\n<section id="%s">\n  <div class="wrap">\n    <div class="sec-head">\n'
       '      <div class="eyebrow mono" data-scramble>%s</div>\n'
       '      <h2 class="title" data-rv="up">%s</h2>\n'
       '      <p class="lead" data-rv="up">%s</p>\n    </div>\n    <div class="pg-cards">\n'
       % (d['id'], e(d['eyebrow']), d['h2'], e(d['lead']))]
    for i,(h3,p) in enumerate(d['voci'], start=1):
        o.append('      <article class="pg-card" data-tilt data-rv="blur">\n'
                 '        <span class="n">%02d</span>\n        <h3>%s</h3>\n        <p>%s</p>\n'
                 '      </article>\n' % (i, e(h3), e(p)))
    o.append('    </div>\n  </div>\n</section>\n')
    return ''.join(o)

n=0
for rel, d in SEZ.items():
    path=os.path.join(ROOT, rel, 'index.html')
    s=open(path,encoding='utf-8').read()
    if 'id="%s"'%d['id'] in s: print('gia presente:',rel); continue
    anchor='<section id="faq">' if '<section id="faq">' in s else '<section class="pg-cta">'
    i=s.index(anchor); s=s[:i]+sezione(d)+'\n'+s[i:]
    open(path,'w',encoding='utf-8').write(s); n+=1; print('ok:',rel)
print('sezioni citta aggiunte:',n)
