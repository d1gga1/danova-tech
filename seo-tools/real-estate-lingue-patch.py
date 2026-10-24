# -*- coding: utf-8 -*-
"""24/10/2026 - Aggiunge rumeno (ro), albanese (sq) e croato/bosniaco (hr) agli script e al JS condivisi:
   post-build-contatti.py (modulo), whatsapp-2026-10-23.py (pulsante), assets/js/contatto.js (barra mobile, messaggi modulo).
   Idempotente.  Uso: python3 seo-tools/real-estate-lingue-patch.py"""
import os, re
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
def rw(p, f):
    p = os.path.join(R, p); s = open(p, encoding='utf-8').read(); n = f(s)
    if n != s: open(p, 'w', encoding='utf-8').write(n); print('aggiornato', p)

TX = ''' 'ro': dict(nome='Nume și firmă', email='E-mail', tel='Telefon (opțional)', msg='De ce aveți nevoie?', send='Trimite cererea',
            note=f'Răspundem în 24 de ore lucrătoare. Preferați să vorbim? Sunați la {TEL_H} sau scrieți-ne pe {WA_H("WhatsApp")}.',
            h='Povestiți-ne proiectul', p='Două rânduri sunt suficiente: vă răspundem cu termene, costuri și pasul următor. Fără obligații.'),
 'sq': dict(nome='Emri dhe kompania', email='Email', tel='Telefoni (opsional)', msg='Për çfarë keni nevojë?', send='Dërgo kërkesën',
            note=f'Përgjigjemi brenda 24 orëve të punës. Preferoni të flasim? Telefononi {TEL_H} ose na shkruani në {WA_H("WhatsApp")}.',
            h='Na tregoni për projektin', p='Mjaftojnë dy rreshta: ju përgjigjemi me afate, kosto dhe hapin e radhës. Pa detyrim.'),
 'hr': dict(nome='Ime i tvrtka', email='E-mail', tel='Telefon (neobavezno)', msg='Što vam treba?', send='Pošalji upit',
            note=f'Odgovaramo u roku od 24 radna sata. Radije razgovor? Nazovite {TEL_H} ili nam pišite na {WA_H("WhatsApp")}.',
            h='Recite nam nešto o projektu', p='Dovoljna su dva retka: odgovorit ćemo s rokovima, troškovima i sljedećim korakom. Bez obveze.'),
'''
def contatti(s):
    if "'ro': dict(" in s: return s
    return s.replace(" 'en': dict(", TX + " 'en': dict(", 1)
rw('seo-tools/post-build-contatti.py', contatti)

WA = '''    "ro": ("Scrieți-ne pe WhatsApp", "Bună ziua, Danova! Vă scriu de pe site, aș dori câteva informații."),
    "sq": ("Na shkruani në WhatsApp", "Përshëndetje Danova! Ju shkruaj nga faqja, do të doja disa informacione."),
    "hr": ("Pišite nam na WhatsApp", "Pozdrav Danova! Pišem vam s web stranice, trebam neke informacije."),
'''
def wa(s):
    if '"ro": (' in s: return s
    return s.replace('    "en": (', WA + '    "en": (', 1)
rw('seo-tools/whatsapp-2026-10-23.py', wa)

JS1 = ("ro:{call:'Sunați',wa:'WhatsApp',write:'Scrieți-ne',sending:'Se trimite…',ok:'Cerere trimisă! Vă răspundem prin e-mail cât mai curând.',"
       "fail:'Nu am putut trimite de pe site: s-a deschis aplicația de e-mail cu mesajul pregătit, apăsați trimite.',"
       "e_nome:'Introduceți numele.',e_mail:'Introduceți o adresă de e-mail validă.',e_msg:'Spuneți-ne în două rânduri de ce aveți nevoie.',subj:'Cerere de pe site'},\n"
       "        sq:{call:'Telefononi',wa:'WhatsApp',write:'Na shkruani',sending:'Po dërgohet…',ok:'Kërkesa u dërgua! Do t’ju përgjigjemi me email sa më shpejt.',"
       "fail:'Nuk mundëm ta dërgonim nga faqja: u hap aplikacioni i email-it me mesazhin gati, shtypni dërgo.',"
       "e_nome:'Shkruani emrin.',e_mail:'Shkruani një adresë email të vlefshme.',e_msg:'Na tregoni në dy rreshta për çfarë keni nevojë.',subj:'Kërkesë nga faqja'},\n"
       "        hr:{call:'Nazovite',wa:'WhatsApp',write:'Pišite nam',sending:'Šalje se…',ok:'Upit je poslan! Odgovorit ćemo e-mailom što prije.',"
       "fail:'Nismo uspjeli poslati sa stranice: otvorila se aplikacija za e-mail s pripremljenom porukom, samo pritisnite pošalji.',"
       "e_nome:'Upišite ime.',e_mail:'Upišite ispravnu e-mail adresu.',e_msg:'Recite nam u dva retka što vam treba.',subj:'Upit sa stranice'},\n        ")
JS2 = ("ro:{q:'Când ați vrea să începeți?',o:['Imediat, în 2 săptămâni','În decurs de o lună','În 1–3 luni','Doar mă informez'],hot:'Perfect, cererea dvs. ajunge prima pe listă.'},\n"
       "        sq:{q:'Kur do të donit të fillonit?',o:['Menjëherë, brenda 2 javësh','Brenda një muaji','Për 1 deri në 3 muaj','Thjesht po informohem'],hot:'Shkëlqyeshëm, kërkesa juaj del e para në listë.'},\n"
       "        hr:{q:'Kada biste željeli početi?',o:['Odmah, u roku od 2 tjedna','U roku od mjesec dana','Za 1 do 3 mjeseca','Samo se informiram'],hot:'Odlično, vaš upit stavljamo na vrh popisa.'},\n        ")
def js(s):
    if "ro:{call:" in s: return s
    i = s.find("en:{call:"); s = s[:i] + JS1 + s[i:]
    i = s.find("en:{q:"); s = s[:i] + JS2 + s[i:]
    return s
rw('assets/js/contatto.js', js)
