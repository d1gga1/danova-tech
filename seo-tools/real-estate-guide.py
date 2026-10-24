# -*- coding: utf-8 -*-
"""24/10/2026 - Aggiunge le guide Real Estate in testa all'indice /guide/ (tra <!--re-guide--> e <!--/re-guide-->). Idempotente."""
import os, re
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
G = [("/guide/come-scegliere-impresa-ristrutturazione/", "Come scegliere un’impresa di ristrutturazione: 10 controlli", "Sopralluogo, preventivo voce per voce, prezzo bloccato, tempi, pratiche e pagamenti: cosa verificare prima di firmare."),
     ("/guide/cila-o-scia/", "CILA o SCIA: quale pratica serve per ristrutturare", "Edilizia libera, CILA e SCIA spiegate con esempi di lavori comuni, e cosa si rischia senza pratica."),
     ("/guide/ristrutturare-un-hotel/", "Ristrutturare un hotel senza perdere la stagione", "Il calendario di progetto, ordini, cantiere e arredi per riaprire nella data prevista."),
     ("/guide/quando-conviene-il-cappotto-termico/", "Quando conviene il cappotto termico", "Gli edifici in cui rende di più, i limiti, le detrazioni 2026 e le alternative."),
     ("/guide/porte-rei-negli-hotel/", "Porte REI negli hotel: dove servono e come sceglierle", "Vani scala, compartimenti, locali tecnici, classi EI e documentazione per i controlli.")]
IC = '<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"></path><path d="M5 9.5V21h14V9.5"></path><path d="M10 21v-6h4v6"></path></svg>'
GO = '<span class="go">Leggi la guida <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span>'
f = os.path.join(R, 'guide', 'index.html'); s = open(f, encoding='utf-8').read(); s0 = s
s = re.sub(r'<!--re-guide-->.*?<!--/re-guide-->', '', s, flags=re.S)
blocco = '<!--re-guide-->' + ''.join('<a class="sect sect-zone" href="%s"><div class="ic">%s</div><h4>%s</h4><p>%s</p>%s</a>' % (h, IC, t, p, GO) for h, t, p in G) + '<!--/re-guide-->'
s = s.replace('<div class="sect-grid">', '<div class="sect-grid">' + blocco, 1)
if s != s0: open(f, 'w', encoding='utf-8').write(s)
print('indice guide: %d guide Real Estate' % len(G))
