# -*- coding: utf-8 -*-
"""14/11/2026 - Meta description sopra i 160 caratteri accorciate (anche og/twitter se uguali). Idempotente.
Da rilanciare dopo i build che rigenerano queste pagine. Uso: python3 seo-tools/descrizioni-2026-11-14.py"""
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = {
 'agenti-ai-per-aziende': "Agenti AI su misura per PMI: leggono email e documenti, aggiornano gestionale e CRM, preparano preventivi e chiedono conferma prima di agire.",
 'agenzia-seo-milano': "Agenzia SEO per aziende di Milano e provincia, ufficio a Vermezzo con Zelo (MI): audit tecnico, contenuti, SEO locale e report mensili chiari.",
 'app-su-misura-per-ogni-attivita': "App personalizzate per ogni attività: prenotazioni, ordini, fidelity, cantieri, magazzino, agenti, palestre. iOS, Android e web, demo in 48-72 ore.",
 'ar': "Danova Tech شركة تقنية إيطالية في تريفيزو: مواقع إيطالية، متاجر إلكترونية، برامج إدارة مخصصة، أتمتة بالذكاء الاصطناعي. عرض سعر ثابت خلال 24 ساعة.",
 'de/website-in-24-stunden': "Professionelle Website in 24 Stunden für 350 € inkl. MwSt.: Texte, Bilder, Kontaktformular und WhatsApp übernehmen wir. Zahlung nur bei Gefallen.",
 'en/custom-apps-for-every-business': "Custom apps for any business: bookings, orders, loyalty, field service, warehouse, sales reps, gyms. iOS, Android and web, demo in 48–72 hours.",
 'en/website-in-24-hours': "A professional website live in 24 hours for €350 incl. VAT. We write the copy, source images and set up the form and WhatsApp. Pay only if you like it.",
 'es/aplicaciones-a-medida': "Aplicaciones a medida para cualquier negocio: reservas, pedidos, fidelización, obras, almacén, comerciales. iOS, Android y web, demo en 48–72 horas.",
 'fr/creation-video-publicitaire': "Vidéos publicitaires pour produits et services : spots IA, motion design 3D et reels pour Instagram, TikTok et Meta Ads. Livrées en 24 h, sans tournage.",
 'fr/site-internet-en-24-heures': "Un site internet professionnel en ligne en 24 heures pour 350 € TTC : textes, images, formulaire et WhatsApp inclus. Vous payez seulement s’il vous plaît.",
 'gestionale-studio-legale': "Gestionale per studio legale su misura: pratiche, scadenze, udienze, ore, parcelle e documenti, da PC e telefono. Demo in 48-72 ore.",
 'intelligenza-artificiale-per-avvocati': "Intelligenza artificiale per studi legali: ricerca nei fascicoli, sintesi di atti, bozze di lettere e classificazione documenti, con dati riservati protetti.",
 'spot-pubblicitari-con-intelligenza-artificiale': "Spot e video creati con intelligenza artificiale per aziende: come funzionano, cosa si può fare, limiti e diritti. Esempi reali, consegna in 24 ore.",
 'tr': "Danova Tech, Treviso merkezli İtalyan yazılım ve web ajansı: İtalyanca web siteleri, e-ticaret, özel yazılım, yapay zekâ ve SEO. 24 saatte teklif.",
 'video-promozionali-per-attivita-locali': "Reel e video promozionali per negozi, ristoranti, bar, parrucchieri, palestre e studi, per farsi conoscere in zona su Instagram e TikTok. In 24 ore.",
 'video-pubblicitari': "Video pubblicitari per prodotti e servizi: spot con intelligenza artificiale, motion design 3D e reel per Instagram, TikTok e Meta Ads. Pronti in 24 ore.",
}
if __name__ == '__main__':
    for rel, new in D.items():
        assert len(new) <= 160, (rel, len(new))
        p = os.path.join(ROOT, rel, 'index.html'); s = open(p, encoding='utf-8').read()
        m = re.search(r'<meta name="description" content="([^"]*)"', s); old = html.unescape(m.group(1))
        if old == new: print('gia ok', rel); continue
        e = html.escape(new, quote=True)
        s = s.replace(m.group(0), '<meta name="description" content="%s"' % e, 1)
        for k in ('og:description', 'twitter:description'):
            s = re.sub(rf'(<meta (?:property|name)="{k}" content=")([^"]*)"',
                       lambda mm: mm.group(1) + (e if html.unescape(mm.group(2)) == old else mm.group(2)) + '"', s)
        s = s.replace('"description": "%s"' % old.replace('"', '\\"'), '"description": "%s"' % new.replace('"', '\\"'))
        open(p, 'w', encoding='utf-8').write(s); print(rel, len(old), '->', len(new))
