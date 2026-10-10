# -*- coding: utf-8 -*-
# Campi consigliati da Google per gli eventi (Search Console, 10 ottobre 2026):
# organizer, performer, image, offers. Usato da nuove_common.event_node e da
# patch_eventi.py (che li aggiunge alle pagine gia' generate).
IMG="https://danova-tech.com/assets/img/og-cover.jpg"
def arricchisci(ev):
    n=ev.get("name",""); site=ev.get("url")
    org={"@type":"Organization","name":n}
    if site: org["url"]=site
    ev.setdefault("organizer",org)
    ev.setdefault("performer",dict(org))
    ev.setdefault("image",[IMG])
    off={"@type":"Offer","availability":"https://schema.org/InStock"}
    if site: off["url"]=site
    ev.setdefault("offers",off)
    return ev
