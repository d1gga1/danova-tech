# -*- coding: utf-8 -*-
"""14/11/2026 - Funzioni comuni ai dati delle pagine nuove del 14/11 (vedi pagine-dati-2026-11-14.py)."""
OGGI = "2026-11-14"
IT_A = [{"@type": "Country", "name": "Italia"}, {"@type": "Place", "name": "Europa"}]
EU_A = [{"@type": "Place", "name": "Europa"}, {"@type": "Country", "name": "Italia"}]
DACH = [{"@type": "Country", "name": "Deutschland"}, {"@type": "Country", "name": "Österreich"},
        {"@type": "Country", "name": "Schweiz"}, {"@type": "Country", "name": "Italien"}]
LINGUE = ["it", "en", "de", "fr", "es"]

def svc(name, typ, desc, cat, area=None, offer=None):
    d = {"name": name, "type": typ, "desc": desc, "area": area or IT_A, "lingue": LINGUE, "catalogo": cat}
    if offer: d["offer"] = offer
    return d

def breve(h2, testo, fatti, eyebrow="In breve"):
    return {"id": "in-breve", "tipo": "breve", "eyebrow": eyebrow, "h2": h2, "testo": testo, "fatti": fatti}

def testo(id, eyebrow, h2, corpo, lead=None):
    d = {"id": id, "tipo": "testo", "eyebrow": eyebrow, "h2": h2, "corpo": corpo}
    if lead: d["lead"] = lead
    return d

def cards(id, eyebrow, h2, corpo, lead=None):
    d = {"id": id, "tipo": "cards", "eyebrow": eyebrow, "h2": h2, "corpo": corpo}
    if lead: d["lead"] = lead
    return d

def passi(id, eyebrow, h2, corpo, lead=None):
    d = {"id": id, "tipo": "passi", "eyebrow": eyebrow, "h2": h2, "corpo": corpo}
    if lead: d["lead"] = lead
    return d

def pagina(lang, url, title, desc, crumbs, eyebrow, h1, lead, cta1, cta2, sezioni, faqtitle, faq,
           ctabox, altri, svcd, altrititle=None, ogtitle=None, ogdesc=None, alt=None):
    d = {"lang": lang, "url": url, "title": title, "desc": desc,
         "ogtitle": ogtitle or title.split(' | ')[0] + ' — Danova Tech', "ogdesc": ogdesc or desc,
         "crumbs": crumbs, "eyebrow": eyebrow, "h1": h1, "lead": lead, "cta1": cta1, "cta2": cta2,
         "sezioni": sezioni, "faqtitle": faqtitle, "faq": faq,
         "ctabox": {"h2": ctabox[0], "p": ctabox[1], "btn": ctabox[2]},
         "altrititle": altrititle or {"it": "Approfondisci", "en": "Related pages", "de": "Mehr dazu",
                                      "fr": "Pour aller plus loin", "es": "Más información"}[lang],
         "altri": altri, "svc": svcd}
    if alt: d["alt"] = alt
    return d
