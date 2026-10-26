# -*- coding: utf-8 -*-
"""26/10/2026 - Danova Real Estate, DE (6): guide costi della ristrutturazione e rifacimento del bagno."""
import importlib.util, os
_H = os.path.dirname(os.path.abspath(__file__))
def _ld(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(_H, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B = _ld('rde1', 'real-estate-tr-de-1.py')
L, LANG, G, _G, u, RE, svc, A, FAQ_BASE = B.L, B.LANG, B.G, B._G, B.u, B.RE, B.svc, B.A, B.FAQ_BASE
PAGINE = []
def P(key, **k): PAGINE.append(dict(lang=LANG, key=key, url=u(key), faqtitle=f"Häufige {G}Fragen.{_G}", altrititle="Weiterlesen", **k))

P('/guide/quanto-costa-ristrutturare-casa/', hero='re-soggiorno-nuovo',
 title='Was kostet eine Hausrenovierung in Italien? Die Kostenfaktoren',
 desc='Wovon die Kosten einer Renovierung in Italien abhängen und warum der Quadratmeterpreis täuscht: Haustechnik, Abbruch, Ausstattung, Genehmigungen, 10% MwSt. und Steuerbonus.',
 ogtitle='Renovierungskosten in Italien', ogdesc='Die Positionen, die den Preis einer Renovierung bestimmen, und wie man Angebote vergleicht.',
 crumbs=[RE, ('Renovierungskosten', None)], eyebrow='Ratgeber · Kosten und Angebote',
 h1=f'Was kostet eine Renovierung: {G}die Faktoren hinter dem Preis.{_G}',
 lead='Zwei gleich große Wohnungen können bei der Renovierung sehr unterschiedlich kosten. Hier erfahren Sie, was den Preis wirklich bestimmt, wie man ein Angebot liest und was MwSt. und Steuerbonus in Italien ausmachen.',
 cta1='Kostenloses Angebot anfragen', cta2='Kostenpositionen',
 sezioni=[
  {'id': 'in-breve', 'tipo': 'breve', 'eyebrow': 'Ratgeber', 'h2': f'Kurz gesagt: {G}was die Kosten bestimmt{_G}', 'testo': 'Die Kosten einer <b>Renovierung</b> hängen von fünf Faktoren ab: <b>Umfang des Abbruchs</b>, <b>erneuerte Haustechnik</b>, <b>Ausstattungsniveau</b>, <b>Zustand der Bausubstanz</b> und nötige <b>Genehmigungen</b>. Der Quadratmeterpreis gibt nur eine Größenordnung: Ein seriöses Angebot entsteht nach der Besichtigung, Position für Position. In Italien gilt für Wohnungsrenovierungen meist der <b>ermäßigte MwSt.-Satz von 10%</b>, und 2026 ein <b>Steuerbonus von 50%</b> auf den Hauptwohnsitz und 36% auf andere Immobilien.', 'fatti': [('Hauptfaktor', 'Haustechnik und Abbruch'), ('Ausstattung', 'Kann die Kosten verdoppeln'), ('Bausubstanz', 'Bei der Besichtigung geprüft'), ('MwSt.', '10% auf Renovierungen von Wohnungen'), ('Steuerbonus 2026', '50% Hauptwohnsitz, 36% sonst'), ('Angebot', 'Nach Positionen, nach Besichtigung')]},
  {'id': 'voci', 'tipo': 'cards', 'eyebrow': 'Kostenpositionen', 'h2': f'Was ein vollständiges Angebot {G}enthält{_G}', 'corpo': [('Abbruch und Entsorgung', 'Entfernen von Böden, Fliesen, Wänden und Sanitärobjekten, mit zertifizierter Entsorgung.'), ('Haustechnik', 'Elektro, Sanitär, Heizung, ggf. Klima: die Position mit den größten Unterschieden.'), ('Maurerarbeiten', 'Trennwände, Estrich, Putz, Öffnungen.'), ('Ausstattung', 'Böden, Fliesen, Türen, Fenster, Sanitär und Anstrich: hier zählt die Materialwahl.'), ('Genehmigungen und Technik', 'Aufmaß, Planung, CILA oder SCIA, Bauleitung, Sicherheit, Kataster und Bonusunterlagen.'), ('Baustelle', 'Schutz, ggf. Gerüst, öffentliche Flächen, Endreinigung.')]},
  {'id': 'mq', 'tipo': 'testo', 'eyebrow': 'Preis pro m²', 'h2': f'Warum der m²-Preis {G}täuscht{_G}', 'corpo': ['Der online gefundene <b>Quadratmeterpreis</b> mischt sehr unterschiedliche Arbeiten. In einer 80-m²-Wohnung sind neue Böden und Anstrich das eine; zusätzlich Bad, Küche und alle Leitungen etwas ganz anderes. Gleiche Fläche, anderes Angebot.', 'Auch Unsichtbares zählt: <b>veraltete Leitungen</b>, <b>feuchtes Mauerwerk</b>, zu verstärkende Balken oder Decken, schwieriger Zugang (Altstädte, obere Stockwerke ohne Aufzug, Venedig). Deshalb kommt die Besichtigung vor jeder Zahl.']}],
 faq=[('Warum veröffentlichen Sie keine Preise?', 'Weil jedes Haus anders ist: Haustechnik, Substanz, Zugang und Ausstattung verändern die Kosten mehr als die Fläche. Wir kommen lieber vorbei und geben ein schriftliches Festpreisangebot nach Positionen.'), ('Sind Besichtigung und Angebot kostenlos?', 'Ja, kostenlos und unverbindlich in ganz Venetien und Friaul-Julisch Venetien.'), ('Wie vergleiche ich zwei Angebote?', 'Prüfen Sie, ob Arbeiten, Mengen, Materialien und Ausschlüsse gleich sind. Fehlt eine Position, sind sie nicht vergleichbar.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Möchten Sie wissen, was Ihre Renovierung kostet?', 'p': 'Kostenlose Besichtigung und Festpreisangebot nach Positionen.', 'btn': 'Kostenloses Angebot anfragen'},
 altri=[('Schlüsselfertige Renovierung', u('/ristrutturazioni-chiavi-in-mano/')), ('Renovierungsbonus Italien 2026', u('/bonus-ristrutturazione-2026/')), ('Renovierungsfirma auswählen', u('/guide/come-scegliere-impresa-ristrutturazione/')), ('Ratgeber Badsanierung', u('/guide/come-rifare-il-bagno/'))],
 svc=svc('Ratgeber Renovierungskosten', 'Ratgeber', 'Was die Kosten einer Renovierung in Italien bestimmt, MwSt., Steuerbonus und wie man ein Angebot liest.', []))

P('/guide/come-rifare-il-bagno/', hero='re-bagno2-nuovo',
 title='Ratgeber Badsanierung: Ablauf, Dauer, Genehmigung, Kosten',
 desc='So läuft eine Badsanierung ab: Abbruch, Leitungen, Abdichtung, Fliesen, Bauzeit, wann eine CILA nötig ist, italienischer Steuerbonus 2026 und was die Kosten beeinflusst.',
 ogtitle='Ratgeber Badsanierung', ogdesc='Ablauf, Dauer, Genehmigungen und Entscheidungen bei der Badsanierung.',
 crumbs=[RE, ('Ratgeber Badsanierung', None)], eyebrow='Ratgeber · Bad',
 h1=f'Badsanierung: {G}Ablauf, Dauer, Genehmigung und Kosten.{_G}',
 lead='Das Bad wird am häufigsten renoviert, und hier kosten Fehler am meisten. So läuft die Arbeit ab, so lange dauert sie, dann braucht es eine Genehmigung, und das beeinflusst den Preis.',
 cta1='Bad sanieren lassen', cta2='Ablauf',
 sezioni=[
  {'id': 'fasi', 'tipo': 'passi', 'eyebrow': 'Ablauf', 'h2': f'Schritt für Schritt, {G}bis zur Übergabe{_G}', 'corpo': [('Aufmaß und Planung', 'Maße, Lage der Abflüsse, Dusche oder Wanne, Sanitär, Möbel und Fliesen, mit Rendering.'), ('Abbruch', 'Entfernen von Fliesen, Boden, Sanitärobjekten und Wanne.'), ('Leitungen', 'Neue Zu- und Abwasserleitungen, Licht, Steckdosen, Lüfter, ggf. Fußbodenheizung.'), ('Estrich und Abdichtung', 'Gefälle für bodengleiche Dusche und Abdichtung in Nassbereichen.'), ('Fliesen und Montage', 'Boden und Wand, Duschwanne oder Rinne, dann Sanitär, Armaturen, Möbel und Spiegel.'), ('Prüfung und Unterlagen', 'Dichtheitsprüfung, Reinigung, Konformitätserklärungen und Bonusunterlagen.')]},
  {'id': 'costo', 'tipo': 'cards', 'eyebrow': 'Kosten', 'h2': f'Entscheidungen, die {G}den Preis bewegen{_G}', 'corpo': [('Abflüsse versetzen', 'WC und Dusche an Ort und Stelle zu lassen ist günstiger.'), ('Bodengleiche Dusche', 'Komfortabler, braucht sorgfältigen Estrich und Abdichtung.'), ('Fliesenformat', 'Große Platten brauchen präzisere Verlegung; Standardformate sind günstiger.'), ('Voll oder teilweise gefliest', 'Nur Nassbereiche fliesen und den Rest streichen spart Geld.'), ('Sanitär und Armaturen', 'Wandhängend oder stehend, Thermostat oder Mischer: große Preisspanne.'), ('Maßmöbel', 'Nutzen in kleinen Bädern jeden Zentimeter; Serienmöbel sind günstiger.')]},
  {'id': 'permessi', 'tipo': 'testo', 'eyebrow': 'Genehmigung und Bonus', 'h2': f'Braucht es eine CILA? {G}Und der Bonus?{_G}', 'corpo': ['Nur Fliesen und Sanitärobjekte an gleicher Stelle zu tauschen ist meist <b>gewöhnliche Instandhaltung</b> ohne Genehmigung. Werden Leitungen erneuert oder Objekte und Wände versetzt, ist es meist <b>außerordentliche Instandhaltung</b> mit <b>CILA</b>, die unser Techniker vorbereitet. Dafür gilt der italienische <b>Renovierungsbonus</b>: 2026 50% auf den Hauptwohnsitz, 36% auf andere Immobilien.']}],
 faq=[('Was kostet eine komplette Badsanierung?', 'Das hängt von Größe, Leitungen, versetzten Abflüssen und vor allem der Ausstattung ab. Wir veröffentlichen keine Preislisten: Nach der kostenlosen Besichtigung erhalten Sie ein Festpreisangebot nach Positionen.'), ('Wie lange bin ich ohne Bad?', 'Ist es das einzige Bad, planen wir die Arbeiten so, dass die Tage ohne Bad möglichst wenige sind, und sagen sie Ihnen vorher.')] + FAQ_BASE[:2],
 ctabox={'h2': 'Bereit für ein neues Bad?', 'p': 'Senden Sie uns ein Foto des jetzigen Bades und den Ort: Wir vereinbaren die kostenlose Besichtigung.', 'btn': 'Bad sanieren lassen'},
 altri=[('Badsanierung', u('/ristrutturazione-bagno/')), ('Renovierungskosten', u('/guide/quanto-costa-ristrutturare-casa/')), ('CILA oder SCIA', u('/guide/cila-o-scia/')), ('Renovierungsbonus Italien 2026', u('/bonus-ristrutturazione-2026/'))],
 svc=svc('Ratgeber Badsanierung', 'Ratgeber', 'Ablauf, Dauer, Genehmigungen, Bonus und Kostenfaktoren einer Badsanierung.', []))

