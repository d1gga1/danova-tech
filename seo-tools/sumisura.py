# -*- coding: utf-8 -*-
"""Blocco 'Un gestionale solo vostro, non un programma uguale per tutti' nelle pagine software italiane (14 ottobre 2026).
Dati confermati dal titolare: prima versione in pochi giorni o poche settimane; integrazione con Excel e programmi esistenti;
funziona da PC, tablet e telefono; il cliente sceglie fra canone mensile e pagamento unico. Idempotente.
Uso: python3 seo-tools/sumisura.py   (da rilanciare dopo pagine-build*.py)"""
import os, re, glob
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A, B = '<!--su-misura-->', '<!--/su-misura-->'
G = '<span class="grad">'; _G = '</span>'
PAT = re.compile(r'^(servizi/(gestionali-crm|app-su-misura|software-automazioni)|gestional|software-|crm-|erp|app-|sviluppo-|automazion|portale-|integrazione-|digitalizzazione-|chatbot|intelligenza-artificiale|ecommerce-b2b|ecommerce-collegato|quanto-costa-un-gestionale|quanto-costa-una-app|web-app|dashboard|gestionale|rpa|guide/(cos-e-un-gestionale|cos-e-un-crm|come-scegliere-un-gestionale|differenza-gestionale-erp-crm|gestionale-cloud-o-server|sostituire-excel-con-un-gestionale|gestione-magazzino-con-excel|gestionale-su-misura-o-standard|cos-e-la-rpa))')
APP = re.compile(r'^(servizi/app-su-misura|app-|sviluppo-app|quanto-costa-una-app|web-app)')

def blocco(app):
    if app:
        t = f"Un'app solo vostra, {G}non una piattaforma uguale per tutti.{_G}"
        lead = "Le app a pacchetto sono pensate per andare bene a migliaia di aziende diverse, e per questo costringono tutte a lavorare nello stesso modo. Noi facciamo il contrario: partiamo da come lavorate voi e costruiamo un'applicazione che esiste solo per la vostra azienda."
        c1 = ("Costruita sul vostro lavoro", "Schermate, campi e passaggi sono quelli che usate davvero, con i vostri nomi. Niente menu pieni di funzioni che non vi servono.")
    else:
        t = f"Un gestionale solo vostro, {G}non un programma uguale per tutti.{_G}"
        lead = "I gestionali commerciali sono fatti per andare bene a migliaia di aziende diverse, e per questo costringono tutte a lavorare nello stesso modo. Noi facciamo il contrario: partiamo da come lavorate voi e costruiamo un software che esiste solo per la vostra azienda."
        c1 = ("Costruito sui vostri processi", "Schermate, campi, documenti e passaggi sono quelli che usate davvero, con i vostri nomi. Niente menu pieni di funzioni che non vi servono.")
    cards = [c1,
      ("Prima versione in pochi giorni", "Partiamo dal pezzo che vi fa perdere più tempo: una prima versione funzionante arriva in pochi giorni o in poche settimane, poi si migliora a fasi."),
      ("I vostri dati, senza ripartire da zero", "Importiamo i fogli Excel e gli archivi che avete già e colleghiamo il software ai programmi che usate: fatturazione, contabilità, e-commerce."),
      ("Da PC, tablet e telefono", "Si apre dal browser o come app: in ufficio, in magazzino, in cantiere o dal cliente, con utenti e permessi diversi."),
      ("Canone o pagamento unico", "Scegliete voi: un canone mensile con tutto incluso oppure un pagamento unico. Le cifre sono nel nostro <a href=\"/prezzi/\">listino prezzi</a>."),
      ("Cresce con voi", "Quando cambia il vostro modo di lavorare cambia anche il software: nuovi moduli, report e collegamenti, uno alla volta.")]
    cs = ''.join(f'''
      <article class="pg-card" data-tilt data-rv="blur">
        <span class="n">{i+1:02d}</span>
        <h3>{h}</h3>
        <p>{p}</p>
      </article>''' for i, (h, p) in enumerate(cards))
    return (f'{A}<section id="solo-vostro">\n  <div class="wrap">\n    <div class="sec-head">\n      <div class="eyebrow mono">Su misura, davvero</div>\n'
            f'      <h2 class="title" data-rv="up">{t}</h2>\n      <p class="lead" data-rv="up">{lead}</p>\n    </div>\n'
            f'    <div class="pg-cards">{cs}\n    </div>\n  </div>\n</section>\n{B}\n')

n = 0; pagine = []
for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
    rel = os.path.relpath(os.path.dirname(f), R).replace('\\', '/')
    if rel.split('/')[0] in ('en', 'de', 'fr', 'es', 'zh', 'zh-hant', 'tr', 'ar', 'seo-tools') or not PAT.search(rel): continue
    s = open(f, encoding='utf-8').read(); o = s
    s = re.sub(re.escape(A) + r'.*?' + re.escape(B) + r'\n?', '', s, flags=re.S)
    i = s.find('<section id="faq">')
    if i < 0: continue
    s = s[:i] + blocco(bool(APP.search(rel))) + s[i:]
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1; pagine.append(rel)
print('pagine software con il blocco:', n)
for p in sorted(pagine): print('  ', p)
