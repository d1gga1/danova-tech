#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""06/11/2026 - Link interni verso /agenti-ai-per-aziende/ dalle pagine AI e automazioni
(primo elemento del box "Approfondisci"/pg-altri) e dall'hub servizi. Idempotente."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
URL = '/agenti-ai-per-aziende/'
PAG = ['chatbot-aziendale', 'intelligenza-artificiale-per-aziende', 'automazioni-n8n',
       'consulenza-intelligenza-artificiale', 'automazione-processi-aziendali',
       'servizi/software-automazioni', 'whatsapp-aziendale', 'ai-act-aziende']
for p in PAG:
    f = os.path.join(p, 'index.html')
    if not os.path.exists(f): print('manca', p); continue
    s = open(f, encoding='utf-8').read()
    if 'href="%s"' % URL in s: print('gia ok', p); continue
    m = re.search(r'(<div class="pg-altri"[^>]*>\n?)(\s*)(<a )', s)
    if not m: print('nessun pg-altri', p); continue
    s = s[:m.end(1)] + m.group(2) + '<a href="%s">Agenti AI per aziende</a>\n' % URL + s[m.end(1):]
    open(f, 'w', encoding='utf-8').write(s); print('link aggiunto', p)
