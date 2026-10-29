# -*- coding: utf-8 -*-
"""Contatti - 15 ottobre 2026. Obiettivo: piu' richieste via email, telefono e WhatsApp.
Idempotente: rilanciare dopo ogni build (insieme a post-build-velocita.py e schema-licenza-eventi.py).
1) Carica assets/js/contatto.js su tutte le pagine (invio email dei moduli, barra Chiama/WhatsApp/Scrivici su smartphone).
2) Pagine senza modulo: il box finale "Richiedi un preventivo" (che rimandava all'homepage) diventa un modulo email;
   le pagine senza box finale ricevono una sezione con il modulo; nelle pagine Contatti il modulo va subito dopo l'intestazione.
3) Moduli delle fiere: il pulsante non dice piu' "su WhatsApp" (la richiesta arriva via email), WhatsApp e telefono restano come alternativa.
Uso: python3 seo-tools/post-build-contatti.py"""
import os, re, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
V = '20261015'
TEL_H = '<a href="tel:+393884706887">+39 388 470 6887</a>'
WA_H = lambda t: f'<a href="https://wa.me/393884706887" target="_blank" rel="noopener">{t}</a>'
TX = {
 'it': dict(nome='Nome e azienda', email='Email', tel='Telefono (facoltativo)', msg='Di cosa hai bisogno?', send='Invia la richiesta',
            note=f'Rispondiamo entro 24 ore lavorative. Preferisci parlarne? Chiama il {TEL_H} o scrivici su {WA_H("WhatsApp")}.',
            h='Raccontaci il tuo progetto', p='Bastano due righe: ti rispondiamo con tempi, costi e il passo successivo. Senza impegno.'),
 'ro': dict(nome='Nume și firmă', email='E-mail', tel='Telefon (opțional)', msg='De ce aveți nevoie?', send='Trimite cererea',
            note=f'Răspundem în 24 de ore lucrătoare. Preferați să vorbim? Sunați la {TEL_H} sau scrieți-ne pe {WA_H("WhatsApp")}.',
            h='Povestiți-ne proiectul', p='Două rânduri sunt suficiente: vă răspundem cu termene, costuri și pasul următor. Fără obligații.'),
 'sq': dict(nome='Emri dhe kompania', email='Email', tel='Telefoni (opsional)', msg='Për çfarë keni nevojë?', send='Dërgo kërkesën',
            note=f'Përgjigjemi brenda 24 orëve të punës. Preferoni të flasim? Telefononi {TEL_H} ose na shkruani në {WA_H("WhatsApp")}.',
            h='Na tregoni për projektin', p='Mjaftojnë dy rreshta: ju përgjigjemi me afate, kosto dhe hapin e radhës. Pa detyrim.'),
 'hr': dict(nome='Ime i tvrtka', email='E-mail', tel='Telefon (neobavezno)', msg='Što vam treba?', send='Pošalji upit',
            note=f'Odgovaramo u roku od 24 radna sata. Radije razgovor? Nazovite {TEL_H} ili nam pišite na {WA_H("WhatsApp")}.',
            h='Recite nam nešto o projektu', p='Dovoljna su dva retka: odgovorit ćemo s rokovima, troškovima i sljedećim korakom. Bez obveze.'),
 'hi': dict(nome='नाम और कंपनी', email='ईमेल', tel='फ़ोन (वैकल्पिक)', msg='आपको क्या चाहिए?', send='अनुरोध भेजें',
            note=f'हम 24 कामकाजी घंटों में जवाब देते हैं। बात करना पसंद करेंगे? {TEL_H} पर कॉल करें या {WA_H("WhatsApp")} पर लिखें।',
            h='अपने प्रोजेक्ट के बारे में बताइए', p='दो लाइनें काफ़ी हैं: हम समय, लागत और अगले क़दम के साथ जवाब देंगे। कोई बाध्यता नहीं।'),
 'en': dict(nome='Name and company', email='Email', tel='Phone (optional)', msg='What do you need?', send='Send request',
            note=f'We reply within 24 working hours. Prefer to talk? Call {TEL_H} or message us on {WA_H("WhatsApp")}.',
            h='Tell us about your project', p='A couple of lines is enough: we reply with timing, costs and the next step. No obligation.'),
 'de': dict(nome='Name und Firma', email='E-Mail', tel='Telefon (optional)', msg='Was brauchen Sie?', send='Anfrage senden',
            note=f'Wir antworten innerhalb von 24 Arbeitsstunden. Lieber telefonieren? Rufen Sie {TEL_H} an oder schreiben Sie uns per {WA_H("WhatsApp")}.',
            h='Erzählen Sie uns von Ihrem Projekt', p='Ein paar Zeilen genügen: Wir antworten mit Zeitrahmen, Kosten und dem nächsten Schritt. Unverbindlich.'),
 'fr': dict(nome='Nom et entreprise', email='E-mail', tel='Téléphone (facultatif)', msg='De quoi avez-vous besoin ?', send='Envoyer la demande',
            note=f'Nous répondons sous 24 heures ouvrées. Vous préférez en parler ? Appelez le {TEL_H} ou écrivez-nous sur {WA_H("WhatsApp")}.',
            h='Parlez-nous de votre projet', p='Deux lignes suffisent : nous répondons avec délais, coûts et prochaine étape. Sans engagement.'),
 'es': dict(nome='Nombre y empresa', email='Email', tel='Teléfono (opcional)', msg='¿Qué necesitas?', send='Enviar solicitud',
            note=f'Respondemos en 24 horas laborables. ¿Prefieres hablar? Llama al {TEL_H} o escríbenos por {WA_H("WhatsApp")}.',
            h='Cuéntanos tu proyecto', p='Con dos líneas basta: te respondemos con plazos, costes y el siguiente paso. Sin compromiso.'),
}
ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
def form(t):
    return (f'<form class="dt-lead" id="dt-scrivi" novalidate>'
      f'<div class="dt-lead-2"><div class="fld"><input type="text" name="nome" id="dtl-nome" placeholder=" " required autocomplete="name"><label for="dtl-nome">{t["nome"]}</label></div>'
      f'<div class="fld"><input type="email" name="email" id="dtl-email" placeholder=" " required autocomplete="email" inputmode="email"><label for="dtl-email">{t["email"]}</label></div></div>'
      f'<div class="fld"><input type="tel" name="tel" id="dtl-tel" placeholder=" " autocomplete="tel" inputmode="tel"><label for="dtl-tel">{t["tel"]}</label></div>'
      f'<div class="fld"><textarea name="msg" id="dtl-msg" placeholder=" " required></textarea><label for="dtl-msg">{t["msg"]}</label></div>'
      f'<input type="text" name="_honey" class="dt-hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
      f'<p class="dt-lead-msg" role="status"></p>'
      f'<button type="submit" class="btn btn-p" data-mag><span class="sheen"></span><span class="lbl">{t["send"]}</span>{ARR}</button>'
      f'<p class="form-note">{t["note"]}</p></form>')
def section(t):
    return (f'<section class="pg-cta" id="scrivici"><div class="wrap"><div class="box" data-rv="up">'
            f'<h2 class="title">{t["h"]}</h2><p>{t["p"]}</p>{form(t)}</div></div></section>\n')

FR_REQ = [  # moduli fiere: (vecchio, nuovo)
 ('<span class="lbl">Invia la richiesta su WhatsApp</span>', '<span class="lbl">Invia la richiesta</span>'),
 ('<span class="lbl">Send the request on WhatsApp</span>', '<span class="lbl">Send the request</span>'),
 ('<span class="lbl">通过WhatsApp发送询价</span>', '<span class="lbl">发送询价</span>'),
 ('<span class="lbl">通過WhatsApp發送詢價</span>', '<span class="lbl">發送詢價</span>'),
 ('Preferisci l\'email? <a class="fr-req-mail" href="mailto:info@danova-tech.com">Scrivici a info@danova-tech.com</a>.',
  'Preferisci WhatsApp? <a class="fr-req-wa" href="https://wa.me/393884706887" target="_blank" rel="noopener">Scrivici su WhatsApp</a> o chiama il <a href="tel:+393884706887">+39 388 470 6887</a>.'),
 ('Prefer email or cannot use WhatsApp? <a class="fr-req-mail" href="mailto:info@danova-tech.com">Write to info@danova-tech.com</a>.',
  'Prefer WhatsApp? <a class="fr-req-wa" href="https://wa.me/393884706887" target="_blank" rel="noopener">Message us on WhatsApp</a> or call <a href="tel:+393884706887">+39 388 470 6887</a>.'),
 ('更习惯用邮件，或无法使用WhatsApp？ <a class="fr-req-mail" href="mailto:info@danova-tech.com">发邮件到 info@danova-tech.com</a>.',
  '也可以<a class="fr-req-wa" href="https://wa.me/393884706887" target="_blank" rel="noopener">通过WhatsApp联系我们</a>，或发邮件到 <a href="mailto:info@danova-tech.com">info@danova-tech.com</a>。'),
 ('更習慣用郵件，或無法使用WhatsApp？ <a class="fr-req-mail" href="mailto:info@danova-tech.com">發郵件到 info@danova-tech.com</a>.',
  '也可以<a class="fr-req-wa" href="https://wa.me/393884706887" target="_blank" rel="noopener">通過WhatsApp聯繫我們</a>，或發郵件到 <a href="mailto:info@danova-tech.com">info@danova-tech.com</a>。'),
]
CONTACT_PAGES = {'contatti', 'en/contact', 'de/kontakt', 'fr/contact', 'es/contacto'}
st = dict(script=0, box=0, sez=0, contatti=0, fiere=0, link=0)
for f in sorted(glob.glob(os.path.join(R, '**', 'index.html'), recursive=True)):
    rel = os.path.relpath(f, R).replace('\\', '/')
    if rel.startswith(('seo-tools/', 'assets/')): continue
    s = open(f, encoding='utf-8').read(); s0 = s
    lang = (re.search(r'<html[^>]*\blang="([^"]+)"', s) or [None, 'it'])[1].lower()
    t = TX.get(lang[:2], TX['en'])
    # 1) script contatto.js
    if 'contatto.js' not in s:
        m = re.search(r'<script src="([^"]*?)assets/js/(?:pagina|home)\.js', s)
        pre = m.group(1) if m else '/'
        s = s.replace('</body>', f'<script src="{pre}assets/js/contatto.js?v={V}" defer></script>\n</body>', 1); st['script'] += 1
    # 3) moduli fiere
    if 'class="fr-req"' in s:
        for a, b in FR_REQ:
            if a in s: s = s.replace(a, b); st['fiere'] += 1
    # 2) modulo email dove manca
    if '<form' not in s and not lang.startswith('zh'):
        page = rel[:-len('/index.html')] if rel != 'index.html' else ''
        if page in CONTACT_PAGES:
            s = re.sub(r'(<section class="pg-hero".*?</section>\n?)', lambda m: m.group(1) + section(t), s, count=1, flags=re.S); st['contatti'] += 1
        else:
            m = re.search(r'<section class="pg-cta"[^>]*>.*?</section>', s, re.S)
            if m:
                box = m.group(0)
                nb = re.sub(r'<a href="[^"]*" class="btn btn-p"[^>]*>.*?</a>', lambda _: form(t), box, count=1, flags=re.S)
                if nb == box: nb = box.replace('</div>\n  </div>\n</section>', form(t) + '</div>\n  </div>\n</section>', 1)
                if nb != box: s = s.replace(box, nb, 1); st['box'] += 1
            elif '</main>' in s:
                s = s.replace('</main>', section(t) + '</main>', 1); st['sez'] += 1
    # 4) i pulsanti "preventivo" portano al modulo della pagina stessa, non all'homepage
    if rel not in ('index.html', 'en/index.html', 'de/index.html', 'fr/index.html', 'es/index.html'):
        dest = '#dt-scrivi' if 'id="dt-scrivi"' in s else ('#richiesta' if 'id="richiesta"' in s and 'class="fr-req"' in s else None)
        if dest:
            s, k = re.subn(r'href="(?:(?:\.\./)+|/(?:en/|de/|fr/|es/)?)?#contatti"', f'href="{dest}"', s); st['link'] += k
    if s != s0: open(f, 'w', encoding='utf-8').write(s)
print('script contatto.js aggiunto: {script} | box finali trasformati in modulo: {box} | sezioni modulo aggiunte: {sez} | pagine Contatti: {contatti} | sostituzioni moduli fiere: {fiere} | pulsanti puntati al modulo della pagina: {link}'.format(**st))
