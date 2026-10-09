# -*- coding: utf-8 -*-
"""Collega le pagine del 9/10/2026 dai box 'Pagine collegate' delle pagine affini. Idempotente.
   Uso: python3 seo-tools/link-pagine-2026-10.py"""
import os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N={"gads":("/quanto-costa-google-ads/","Quanto costa Google Ads"),
   "lp":("/realizzazione-landing-page/","Realizzazione landing page"),
   "ai":("/seo-per-intelligenza-artificiale/","SEO per l&#8217;intelligenza artificiale"),
   "fiere":("/contributi-fiere-2026/","Contributi per le fiere 2026"),
   "bandi":("/bandi-digitalizzazione-veneto-2026/","Bandi digitalizzazione 2026 in Veneto"),
   "iper":("/iperammortamento-2026/","Iperammortamento 2026"),
   "aiact":("/ai-act-aziende/","AI Act per le aziende"),
   "n8n":("/automazioni-n8n/","Automazioni con n8n"),
   "rec":("/come-ottenere-recensioni-google/","Come ottenere recensioni Google"),
   "wms":("/software-wms/","Software WMS"),
   "riv":("/portale-rivenditori-b2b/","Portale rivenditori B2B"),
   "hotel":("/siti-web-per-hotel/","Siti web per hotel e B&amp;B"),
   "avv":("/siti-web-per-avvocati/","Siti web per avvocati"),
   "calbo":("/calendario-fiere-bologna/","Calendario fiere Bologna"),
   "calmi":("/calendario-fiere-milano/","Calendario fiere Milano"),
   "calri":("/calendario-fiere-rimini/","Calendario fiere Rimini"),
   "calpr":("/calendario-fiere-parma/","Calendario fiere Parma"),
   "idx":("/come-indicizzare-un-sito-su-google/","Come indicizzare un sito su Google"),
   "idee":("/idee-stand-fieristici/","Idee per stand fieristici"),
   "imm":("/siti-web-per-agenzie-immobiliari/","Siti web per agenzie immobiliari"),
   "rist":("/siti-web-per-ristoranti/","Siti web per ristoranti")}
MAP2={"guide/transizione-5-0":["iper"],"digitalizzazione-aziendale":["iper"],"software-mes-produzione":["iper"],"software-gestionale-produzione":["iper"],
 "bandi-digitalizzazione-veneto-2026":["iper"],
 "intelligenza-artificiale-per-aziende":["aiact","n8n"],"chatbot-aziendale":["aiact","n8n"],"automazione-processi-aziendali":["n8n"],
 "integrazione-software-aziendali":["n8n"],"servizi/software-automazioni":["n8n","aiact"],
 "guide/google-business-profile-guida":["rec"],"servizi/seo":["rec"],"consulente-seo-treviso":["rec"],"posizionamento-sito-google":["rec"],
 "software-gestionale-magazzino":["wms"],"app-magazzino-codici-a-barre":["wms"],"software-gestionale-trasporti-logistica":["wms"],"servizi/gestionali-crm":["wms","riv"],
 "ecommerce-b2b":["riv"],"ecommerce-collegato-al-gestionale":["riv","wms"],"app-per-agenti-di-commercio":["riv"],
 "servizi/siti-web-ecommerce":["hotel","avv"],"lavori/oasi-ponza":["hotel"],"app-prenotazioni":["hotel"],"web-agency-conegliano":["hotel"],
 "software-gestionale-studi-professionali":["avv"],"sito-web-aziendale":["hotel","avv"]}
MAP3={"calendario-fiere":["calmi","calbo","calri","calpr"],"allestimenti-fieristici-bologna":["calbo"],"allestimenti-fieristici-milano":["calmi"],
 "allestimenti-fieristici-rimini":["calri"],"allestimenti-fieristici-parma":["calpr"],"stand-eima":["calbo"],"stand-cosmoprof":["calbo"],"stand-cersaie":["calbo"],
 "stand-salone-del-mobile":["calmi"],"stand-eicma":["calmi"],"stand-host":["calmi"],"stand-mido":["calmi"],"stand-micam":["calmi"],
 "stand-ecomondo":["calri"],"stand-sigep":["calri"],"stand-macfrut":["calri"],"stand-cibus":["calpr"],"guide/come-preparare-una-fiera":["calmi","calbo"]}
MAP4={"posizionamento-sito-google":["idx"],"servizi/seo":["idx"],"consulente-seo":["idx"],"guide/rifare-sito-senza-perdere-posizioni":["idx"],
 "seo-per-intelligenza-artificiale":["idx"],"servizi/allestimenti-fieristici":["idee"],"progettazione-stand-fieristici":["idee"],"stand-fieristici-piccoli":["idee"],
 "guide/come-preparare-una-fiera":["idee"],"stand-fieristici-su-misura":["idee"],"servizi/siti-web-ecommerce":["imm","rist"],"siti-web-per-hotel":["rist","imm"],
 "siti-web-per-avvocati":["imm"],"come-ottenere-recensioni-google":["rist"],"app-prenotazioni":["rist"]}
MAP={"servizi/google-ads":["gads","lp"],"servizi/meta-ads":["lp","gads"],"lead-generation-b2b":["lp","gads"],
 "servizi/siti-web-ecommerce":["lp"],"servizi/seo":["ai"],"consulente-seo":["ai"],"posizionamento-sito-google":["ai"],
 "agenzia-seo-milano":["ai"],"guide/google-business-profile-guida":["ai"],"intelligenza-artificiale-per-aziende":["ai","bandi"],
 "servizi/allestimenti-fieristici":["fiere"],"quanto-costa-uno-stand-fieristico":["fiere"],"calendario-fiere":["fiere"],
 "allestimenti-fieristici-estero":["fiere"],"guide/come-preparare-una-fiera":["fiere"],"noleggio-stand-fieristici":["fiere"],
 "digitalizzazione-aziendale":["bandi"],"guide/transizione-5-0":["bandi"],"software-mes-produzione":["bandi"],
 "gestionali-su-misura-veneto":["bandi"],"automazione-processi-aziendali":["bandi"]}
for page,keys in list(MAP.items())+list(MAP2.items())+list(MAP3.items())+list(MAP4.items()):
    p=os.path.join(ROOT,page,"index.html"); h=open(p,encoding="utf-8").read()
    m=re.search(r'<div class="pg-altri"[^>]*>',h)
    if not m: print("NO BOX",page); continue
    add="".join('<a href="%s">%s</a>'%N[k] for k in keys if 'href="%s"'%N[k][0] not in h)
    if add:
        h=h[:m.end()]+add+h[m.end():]; open(p,"w",encoding="utf-8").write(h); print("+",page)
