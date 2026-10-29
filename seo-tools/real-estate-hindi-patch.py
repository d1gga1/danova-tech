# -*- coding: utf-8 -*-
"""29/10/2026 - Aggiunge l'HINDI (hi) alla sezione Danova Real Estate.
   Modifica (una volta sola, idempotente) gli script condivisi: lingue, build, cornice, SEO, pagine legali, llms,
   citta' nuove, modulo contatti, pulsante WhatsApp, contatto.js, tema (font devanagari), menu video, sito.
   I testi delle pagine sono in real-estate-hi-base.py e real-estate-tr-hi-*.py.
   URL hindi: /hi/<slug inglese>/ (es. /hi/bathroom-renovation/); nomi di citta' in caratteri latini.
   Uso: python3 seo-tools/real-estate-hindi-patch.py   poi   bash seo-tools/real-estate-tutto.sh"""
import os, re
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(H)

def rw(p, f):
    p = os.path.join(R, p); s = open(p, encoding='utf-8').read(); n = f(s)
    if n != s:
        open(p, 'w', encoding='utf-8').write(n); print('aggiornato', os.path.relpath(p, R))
    else:
        print('invariato ', os.path.relpath(p, R))

def sub1(s, old, new):
    assert old in s, 'non trovato: %r' % old[:90]
    return s.replace(old, new, 1)

# ------------------------------------------------------------------ 1) lingue
def lingue(s):
    if "'hi': dict(loc=" in s: return s
    s = sub1(s, "LINGUE = ['it', 'en', 'de', 'ro', 'sq']", "LINGUE = ['it', 'en', 'de', 'ro', 'sq', 'hi']")
    s = sub1(s, " 'hr': dict(loc='hr-HR'",
             " 'hi': dict(loc='hi-IN', og='hi_IN', home='/hi/real-estate/', donor='en/web-design-agency-uk/index.html', hl=['hi'], lab='HI'),  # 29/10/2026\n 'hr': dict(loc='hr-HR'")
    s = sub1(s, """def url(key, lang):
    if lang == 'it': return key
    return '/%s/%s/' % (lang, S[key][LINGUE.index(lang) - 1])""",
             """ORD = ['en', 'de', 'ro', 'sq', 'hr']   # ordine degli slug nelle tuple di S (indipendente da LINGUE)
def url(key, lang):
    if lang == 'it': return key
    if lang == 'hi': return '/hi/%s/' % S[key][0]   # 29/10/2026: l'hindi usa gli slug inglesi (URL in caratteri latini)
    return '/%s/%s/' % (lang, S[key][ORD.index(lang)])""")
    s = sub1(s, "def nome(n, lang):", """for _n, _v in NOMI.items():   # 29/10/2026: in hindi i nomi di luogo restano in caratteri latini, come in inglese
    if 'en' in _v: _v.setdefault('hi', _v['en'])
NOMI['Sottomarina e Chioggia']['hi'] = 'Sottomarina और Chioggia'
def nome(n, lang):""")
    s = sub1(s, "\n}\n\n# cornice del donatore inglese", """
 'hi': dict(prima='पहले', dopo='बाद में', cmp='पहले और बाद की तुलना करें', home='होम',
            nota='काम के प्रकार दिखाने के लिए आर्टिफ़िशियल इंटेलिजेंस से बनाई गई सांकेतिक तस्वीरें और वीडियो: ये असली साइटों या ग्राहकों को नहीं दर्शाते।',
            badges=['Veneto और Friuli', 'मुफ़्त साइट सर्वे', 'फ़िक्स्ड प्राइस', 'एक ही ज़िम्मेदार व्यक्ति']),
}

# cornice del donatore inglese""")
    s = sub1(s, "\n}\n\n# 24/10/2026 - stringhe del footer EN", """
 'hi': _ch('सामग्री पर जाएँ', ['सेवाएँ', 'वीडियो', 'किसके लिए', 'काम', 'प्रक्रिया', 'कीमतें', 'संपर्क'], 'बात करें',
           'Danova Real Estate: Veneto और Friuli में टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर और होटल फ़र्नीचर। Danova Tech का एक डिवीज़न।',
           ['सेवाएँ', 'बाज़ार', 'एजेंसी', 'संपर्क'], 'गोदाम:', 'ऑफ़िस:', 'उपयोग की शर्तें', 'होम पर वापस'),
}

# 24/10/2026 - stringhe del footer EN""")
    s = sub1(s, "               'hr': ['Naša metoda',", "               'hi': ['हमारा तरीक़ा', 'प्रोजेक्ट के उदाहरण', 'हमारे बारे में', 'सभी सेवाएँ', 'गोपनीयता नीति', 'कुकी नीति'],\n               'hr': ['Naša metoda',")
    return s
rw('seo-tools/real-estate-lingue.py', lingue)

# ------------------------------------------------------------------ 2) build
def build(s):
    if "'hi': 'Danova Tech का कंस्ट्रक्शन" in s: return s
    s = sub1(s, " 'hr': 'Građevinski odjel tvrtke Danova Tech",
             " 'hi': 'Danova Tech का कंस्ट्रक्शन डिवीज़न: इटली के Veneto और Friuli Venezia Giulia में टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर, फ़साड और इंसुलेशन, छतें और अटारी, बाहरी फ़्लोरिंग, दरवाज़े, ड्राईवॉल, फ़र्श, होटल फ़र्नीचर और कस्टम फ़र्नीचर।',\n 'hr': 'Građevinski odjel tvrtke Danova Tech")
    s = sub1(s, " 'hr': [(\"Besplatan obilazak i ponuda\"",
             """ 'hi': [("मुफ़्त साइट सर्वे और कोटेशन", "हम आकर देखते हैं, नाप लेते हैं और हर काम का अलग विस्तृत कोटेशन देते हैं, बिना किसी बाध्यता के।"),
        ("फ़िक्स्ड टर्नकी प्राइस", "तय कीमत ही आप देते हैं: काम शुरू होने के बाद कोई अचानक अतिरिक्त ख़र्च नहीं।"),
        ("कॉन्ट्रैक्ट में समय-सीमा", "शुरू और हैंडओवर की तारीख़ें लिखित में, काम के पूरे शेड्यूल के साथ।"),
        ("एक ही ज़िम्मेदार व्यक्ति", "एक ही व्यक्ति टीमों, सप्लायरों और परमिट का समन्वय करता है और आपको अपडेट देता है।")],
 'hr': [("Besplatan obilazak i ponuda\"""")
    s = sub1(s, "         'hr': ('Gradilište izvan sezone',", "         'hi': ('ऑफ़-सीज़न में साइट', 'होटल बंद रहते हुए ड्राईवॉल, सिस्टम और फ़िनिशिंग।'),\n         'hr': ('Gradilište izvan sezone',")
    s = sub1(s, "        'hr': ('Projekt i 3D vizualizacija',", "        'hi': ('डिज़ाइन और 3D रेंडर', 'हर फ़र्नीचर निर्माण से पहले 3D में मंज़ूर।'),\n        'hr': ('Projekt i 3D vizualizacija',")
    s = sub1(s, "    if lang in ('ro', 'sq', 'hr'):   # shell EN", "    if lang in ('ro', 'sq', 'hr', 'hi'):   # shell EN")
    s = s.replace('in 6 lingue (it, en, de, ro, sq, hr)', 'in 7 lingue (it, en, de, ro, sq, hi, hr)', 1)
    s = s.replace('cornice del donatore inglese tradotta per ro / sq / hr', 'cornice del donatore inglese tradotta per ro / sq / hi / hr', 1)
    return s
rw('seo-tools/real-estate-build.py', build)

# ------------------------------------------------------------------ 3) cornice (menu e footer)
CHROME_HI = r'''
# 29/10/2026: hindi (hi)
L5.append('hi')
for (_k, _t), _h in zip(NAV, ['रेनोवेशन', 'जनरल कॉन्ट्रैक्टर', 'होटल', 'होटल फ़र्नीचर', 'फ़साड', 'आर्किटेक्ट के लिए']): _t['hi'] = _h
TEL['hi'] = 'फ़ोन'; CONTATTI['hi'] = 'संपर्क'
for _k, _h in {'/ristrutturazioni-chiavi-in-mano/': 'टर्नकी रेनोवेशन', '/ristrutturazione-appartamenti-e-case/': 'अपार्टमेंट और घर', '/ristrutturazione-bagno/': 'बाथरूम रेनोवेशन',
               '/ristrutturazione-negozi-uffici-ristoranti/': 'दुकानें, ऑफ़िस और रेस्टोरेंट', '/ristrutturazione-hotel/': 'होटल रेनोवेशन', '/ristrutturazione-condomini-e-capannoni/': 'अपार्टमेंट बिल्डिंग और गोदाम',
               '/general-contractor/': 'जनरल कॉन्ट्रैक्टर', '/hotel-chiavi-in-mano/': 'टर्नकी होटल', '/impresa-edile-per-architetti/': 'आर्किटेक्ट के लिए कंपनी', '/pareti-divisorie/': 'पार्टीशन दीवारें',
               '/rifacimento-tetto/': 'छत की मरम्मत', '/isolamento-sottotetto/': 'अटारी इंसुलेशन', '/pavimentazioni-esterne/': 'बाहरी फ़्लोरिंग', '/cappotto-termico/': 'बाहरी थर्मल इंसुलेशन',
               '/facciate-ventilate-e-rifacimento-facciate/': 'फ़साड रेनोवेशन', '/porte-interne-e-blindate/': 'अंदरूनी और सिक्योरिटी दरवाज़े', '/porte-rei-tagliafuoco/': 'फ़ायर-रेटेड दरवाज़े',
               '/cartongesso-e-controsoffitti/': 'ड्राईवॉल और सीलिंग', '/pavimenti-e-serramenti/': 'फ़र्श और खिड़कियाँ', '/arredo-hotel-contract/': 'होटल फ़र्नीचर', '/mobili-su-misura/': 'कस्टम फ़र्नीचर',
               '/progettazione-e-render-3d/': 'डिज़ाइन और 3D रेंडर', '/pratiche-edilizie-cila-scia/': 'बिल्डिंग परमिट', '/bonus-ristrutturazione-2026/': 'रेनोवेशन बोनस 2026',
               '/guide/come-scegliere-impresa-ristrutturazione/': 'रेनोवेशन कंपनी कैसे चुनें', '/guide/quanto-costa-ristrutturare-casa/': 'रेनोवेशन की लागत', '/guide/come-rifare-il-bagno/': 'बाथरूम रेनोवेशन गाइड',
               '/guide/cila-o-scia/': 'CILA या SCIA', '/guide/ristrutturare-un-hotel/': 'होटल रेनोवेशन कैसे करें', '/guide/quando-conviene-il-cappotto-termico/': 'क्या इंसुलेशन फ़ायदेमंद है',
               '/guide/porte-rei-negli-hotel/': 'होटलों में फ़ायर-रेटेड दरवाज़े'}.items():
    LAB[_k]['hi'] = _h
IN['hi'] = '%s में रेनोवेशन'
NOMI['venezia']['hi'] = 'Venice'; NOMI['padova']['hi'] = 'Padua'; NOMI['trieste']['hi'] = 'Trieste'
for _c, _h in zip(COL, ['रेनोवेशन', 'काम और फ़र्नीचर', 'इलाक़े', 'गाइड']): _c['hi'] = _h
DESC['hi'] = 'Danova Real Estate: इटली के Veneto और Friuli Venezia Giulia में टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर, फ़साड और होटल फ़र्नीचर। Danova Tech का एक डिवीज़न।'
ADDR['hi'] = 'Via Rigole 48<br>31040 Mansuè (TV) — इटली'
WA['hi'] = 'WhatsApp: हमें लिखें'
LANGS['hi'] = 'हम इतालवी, अंग्रेज़ी और रोमानियाई बोलते हैं; लिखित में हिंदी भी'
LEG['hi'] = [('/hi/privacy/', 'गोपनीयता नीति'), ('/hi/cookie-policy/', 'कुकी नीति'), ('/hi/terms/', 'उपयोग की शर्तें')]

'''
def chrome(s):
    if "L5.append('hi')" in s: return s
    return sub1(s, "\n\ndef nav_links(", CHROME_HI + "\ndef nav_links(")
rw('seo-tools/real-estate-chrome.py', chrome)

# ------------------------------------------------------------------ 4) SEO
SEO_HI = r'''
# 29/10/2026: hindi (hi)
L5.append('hi')
CONG['hi'] = 'और'
for (_p, _sl, _t), _h in zip(GRUPPI, ['रेनोवेशन', 'जनरल कॉन्ट्रैक्टर', 'होटल फ़र्नीचर']): _t['hi'] = _h
TIT['hi'] = 'हम कहाँ काम करते हैं'
H2['hi'] = 'Veneto और Friuli Venezia Giulia, <span class="grad">शहर-दर-शहर</span>'
LEAD['hi'] = 'उत्तर-पूर्वी इटली के Veneto और Friuli Venezia Giulia के हर प्रांत में मुफ़्त साइट सर्वे। ये वे इलाक़े हैं जहाँ हम सबसे ज़्यादा काम करते हैं।'
PILASTRO['hi'] = 'Danova Real Estate: इटली के Veneto में रेनोवेशन कंपनी'
TT['citta']['hi'] = ('%s, इटली में बिल्डर | टर्नकी रेनोवेशन', '%s में बिल्डर | रेनोवेशन')
TT['gc']['hi'] = ('%s, इटली में जनरल कॉन्ट्रैक्टर | फ़िक्स्ड प्राइस', '%s में जनरल कॉन्ट्रैक्टर')
TT['hotel']['hi'] = ('%s में होटल फ़र्नीचर | कस्टम कॉन्ट्रैक्ट फ़र्नीचर', '%s में होटल फ़र्नीचर | कस्टम')
KNOWS['hi'] = ['टर्नकी रेनोवेशन', 'बाथरूम रेनोवेशन', 'कंस्ट्रक्शन कंपनी', 'जनरल कॉन्ट्रैक्टर', 'बाहरी थर्मल इंसुलेशन', 'अटारी इंसुलेशन', 'छत की मरम्मत',
               'वेंटिलेटेड फ़साड', 'बाहरी फ़्लोरिंग', 'ड्राईवॉल और फ़ॉल्स सीलिंग', 'फ़ायर-रेटेड दरवाज़े', 'फ़र्श और खिड़कियाँ', 'होटल फ़र्नीचर', 'कस्टम फ़र्नीचर',
               'इटली में बिल्डिंग परमिट (CILA, SCIA)', 'इटली रेनोवेशन टैक्स बोनस']
SLOGAN['hi'] = 'मुफ़्त साइट सर्वे, फ़िक्स्ड प्राइस, कॉन्ट्रैक्ट में समय-सीमा, एक ही ज़िम्मेदार व्यक्ति।'
for _k in LG.S:
    INV[LG.url(_k, 'hi')] = (_k, 'hi')

'''
def seo(s):
    if "CONG['hi']" in s: return s
    s = sub1(s, r"(?:e|ed|and|und|sowie|și|dhe)", r"(?:e|ed|and|und|sowie|și|dhe|और)")
    # l'hindi chiude le frasi con il danda (।), non con il punto
    s = sub1(s, "    corpo = frase.rstrip().rstrip('.')", "    corpo = frase.rstrip().rstrip('.').rstrip('।'); fine = '।' if l == 'hi' else '.'")
    s = sub1(s, "        return parti[0] + '.'", "        return parti[0] + fine")
    s = sub1(s, "    return ', '.join(parti[:-1]) + ' ' + CONG[l] + ' ' + parti[-1] + '.'", "    return ', '.join(parti[:-1]) + ' ' + CONG[l] + ' ' + parti[-1] + fine")
    s = sub1(s, r"frasi = re.split(r'(?<=[.!?])\s+', d.strip())", r"frasi = re.split(r'(?<=[.!?।])\s+', d.strip())")
    s = sub1(s, "        for sep in ('. ', ': ', ', '):", "        for sep in ('. ', '। ', ': ', ', '):")
    s = sub1(s, "                return cut[:i].rstrip(',:') + '.'", "                return cut[:i].rstrip(',:') + ('।' if l == 'hi' else '.')")
    return sub1(s, "\n\ndef schema(", SEO_HI + "\ndef schema(")
rw('seo-tools/real-estate-seo.py', seo)

# ------------------------------------------------------------------ 5) pagine legali
LEG_TXT = open(os.path.join(H, 'real-estate-hindi-legale.txt'), encoding='utf-8').read() if os.path.exists(os.path.join(H, 'real-estate-hindi-legale.txt')) else None
def legale(s):
    if "T['hi'] = {}" in s: return s
    assert LEG_TXT, 'manca seo-tools/real-estate-hindi-legale.txt'
    s = sub1(s, "'sq': '/sq/privatesia/'}", "'sq': '/sq/privatesia/', 'hi': '/hi/privacy/'}")
    s = sub1(s, "'sq': '/sq/politika-e-cookie-ve/'}", "'sq': '/sq/politika-e-cookie-ve/', 'hi': '/hi/cookie-policy/'}")
    s = sub1(s, "'sq': '/sq/kushtet-e-perdorimit/'}", "'sq': '/sq/kushtet-e-perdorimit/', 'hi': '/hi/terms/'}")
    s = sub1(s, "\nUI = {'ro':", "\n" + LEG_TXT + "UI = {'ro':")
    s = sub1(s, "rel='Faqe të lidhura', hreal='Danova Real Estate', loc='sq_AL')}",
             "rel='Faqe të lidhura', hreal='Danova Real Estate', loc='sq_AL'),\n      'hi': dict(home='होम', eyebrow='क़ानूनी जानकारी', upd='आख़िरी अपडेट: अक्टूबर 2026', rel='संबंधित पेज', hreal='Danova Real Estate', loc='hi_IN')}")
    s = sub1(s, "HL = ['it', 'en', 'de', 'ro', 'sq']", "HL = ['it', 'en', 'de', 'ro', 'sq', 'hi']")
    s = sub1(s, '"publisher": {"@id": SITE + "/#org"}', '"publisher": {"@id": SITE + "/#organization"}')   # 29/10/2026: stesso @id del resto del sito
    s = sub1(s, 'hreflang="(it|en|de|ro|sq)"', 'hreflang="(it|en|de|ro|sq|hi)"')
    s = sub1(s, "            for x in ('ro', 'sq'):", "            for x in ('ro', 'sq', 'hi'):")
    s = sub1(s, "for l in ('ro', 'sq') for k in", "for l in ('ro', 'sq', 'hi') for k in")
    s = s.replace("print('pagine legali RO/SQ:'", "print('pagine legali RO/SQ/HI:'", 1)
    return s
rw('seo-tools/real-estate-legale.py', legale)

# ------------------------------------------------------------------ 6) citta' nuove
CN_TXT = open(os.path.join(H, 'real-estate-hindi-citta.txt'), encoding='utf-8').read() if os.path.exists(os.path.join(H, 'real-estate-hindi-citta.txt')) else None
def citta(s):
    if "TR['hi']" in s: return s
    assert CN_TXT, 'manca seo-tools/real-estate-hindi-citta.txt'
    return sub1(s, "\ndef citta(lang):", "\n" + CN_TXT + "def citta(lang):")
rw('seo-tools/real-estate-citta-nuove.py', citta)

# ------------------------------------------------------------------ 7) llms.txt
LLMS_HI = ''' 'hi': ("Danova Real Estate — हिंदी में सारांश",
        "Danova Real Estate, Danova Tech का कंस्ट्रक्शन डिवीज़न है (वही कंपनी, P.IVA IT05369890263, Via Rigole 48, 31040 Mansuè, Treviso, इटली): अपार्टमेंट, घरों, बाथरूम, दुकानों, ऑफ़िसों, रेस्टोरेंट, होटलों और अपार्टमेंट बिल्डिंगों का टर्नकी रेनोवेशन, जनरल कॉन्ट्रैक्टर, फ़साड और थर्मल इंसुलेशन, अंदरूनी, सिक्योरिटी और फ़ायर-रेटेड दरवाज़े, ड्राईवॉल, फ़र्श और खिड़कियाँ, होटल फ़र्नीचर और कस्टम फ़र्नीचर, 3D डिज़ाइन, इतालवी बिल्डिंग परमिट (CILA, SCIA) और टैक्स बोनस।",
        ["इलाक़ा: Veneto और Friuli Venezia Giulia, उत्तर-पूर्वी इटली", "वादे: मुफ़्त साइट सर्वे और कोटेशन, फ़िक्स्ड टर्नकी प्राइस, कॉन्ट्रैक्ट में लिखी समय-सीमा, एक ही ज़िम्मेदार व्यक्ति",
         "कीमतें: प्रकाशित नहीं; मुफ़्त साइट सर्वे के बाद लिखित कोटेशन", "भाषाएँ: इतालवी, अंग्रेज़ी, रोमानियाई; लिखित बातचीत हिंदी में भी", "संपर्क: +39 388 470 6887 (फ़ोन और WhatsApp), info@danova-tech.com",
         "साइट की तस्वीरें सांकेतिक हैं, आर्टिफ़िशियल इंटेलिजेंस से बनाई गई"],
        ["Danova Real Estate (मुख्य पेज)", "टर्नकी रेनोवेशन", "बाथरूम रेनोवेशन", "होटल रेनोवेशन", "जनरल कॉन्ट्रैक्टर", "टर्नकी होटल", "बाहरी थर्मल इंसुलेशन", "होटल फ़र्नीचर", "आर्किटेक्ट के लिए कंस्ट्रक्शन कंपनी", "इटली रेनोवेशन बोनस 2026"]),
}
_NOMI_CITTA ='''
def llms(s):
    if "'hi': (\"Danova Real Estate — हिंदी" in s: return s
    return sub1(s, "}\n_NOMI_CITTA =", LLMS_HI)
rw('seo-tools/real-estate-llms.py', llms)

# ------------------------------------------------------------------ 8) modulo contatti, WhatsApp, contatto.js
def contatti(s):
    if "'hi': dict(nome=" in s: return s
    return sub1(s, " 'en': dict(nome='Name and company'", """ 'hi': dict(nome='नाम और कंपनी', email='ईमेल', tel='फ़ोन (वैकल्पिक)', msg='आपको क्या चाहिए?', send='अनुरोध भेजें',
            note=f'हम 24 कामकाजी घंटों में जवाब देते हैं। बात करना पसंद करेंगे? {TEL_H} पर कॉल करें या {WA_H("WhatsApp")} पर लिखें।',
            h='अपने प्रोजेक्ट के बारे में बताइए', p='दो लाइनें काफ़ी हैं: हम समय, लागत और अगले क़दम के साथ जवाब देंगे। कोई बाध्यता नहीं।'),
 'en': dict(nome='Name and company'""")
rw('seo-tools/post-build-contatti.py', contatti)

def wa(s):
    if '"hi": (' in s: return s
    return sub1(s, '    "en": (', '    "hi": ("WhatsApp पर हमें लिखें", "नमस्ते Danova! मैं वेबसाइट से लिख रहा/रही हूँ, मुझे कुछ जानकारी चाहिए।"),\n    "en": (')
rw('seo-tools/whatsapp-2026-10-23.py', wa)

def js(s):
    if "hi:{call:" in s: return s
    s = sub1(s, "en:{call:", "hi:{call:'कॉल करें',wa:'WhatsApp',write:'लिखें',sending:'भेजा जा रहा है…',ok:'अनुरोध भेज दिया गया! हम जल्द ही ईमेल से जवाब देंगे।',"
                "fail:'साइट से भेजा नहीं जा सका: आपका ईमेल ऐप तैयार संदेश के साथ खुल गया है, बस भेजें दबाएँ।',"
                "e_nome:'अपना नाम लिखें।',e_mail:'सही ईमेल पता लिखें।',e_msg:'दो लाइनों में बताइए कि आपको क्या चाहिए।',subj:'वेबसाइट से अनुरोध'},\n        en:{call:")
    s = sub1(s, "en:{q:", "hi:{q:'आप कब शुरू करना चाहेंगे?',o:['तुरंत, 2 हफ़्ते में','एक महीने के अंदर','1 से 3 महीने में','बस जानकारी ले रहा/रही हूँ'],hot:'बढ़िया, आपका अनुरोध सूची में सबसे ऊपर जाएगा।'},\n        en:{q:")
    s = sub1(s, "hr:'Unesite ispravan broj telefona.',", "hr:'Unesite ispravan broj telefona.',hi:'सही फ़ोन नंबर लिखें।',")
    return s
rw('assets/js/contatto.js', js)

# ------------------------------------------------------------------ 9) tema: font devanagari, niente spaziatura tra le lettere
TEMA_CSS = r'''/* 29/10/2026 hindi: font devanagari di sistema, niente letter-spacing (spezza le legature), righe piu' alte per le matra */
html[lang="hi"] body{font-family:Inter,"Noto Sans Devanagari","Kohinoor Devanagari","Devanagari Sangam MN","Nirmala UI",Mangal,system-ui,sans-serif}
html[lang="hi"] h1,html[lang="hi"] h2,html[lang="hi"] h3,html[lang="hi"] h4,html[lang="hi"] h5,html[lang="hi"] .title,html[lang="hi"] b{font-family:Sora,"Noto Sans Devanagari","Kohinoor Devanagari","Devanagari Sangam MN","Nirmala UI",Mangal,system-ui,sans-serif}
html[lang="hi"] main *,html[lang="hi"] nav *,html[lang="hi"] footer *{letter-spacing:normal!important}
html[lang="hi"] h1,html[lang="hi"] h2,html[lang="hi"] .title{line-height:1.32}
html[lang="hi"] h3,html[lang="hi"] summary,html[lang="hi"] figcaption b{line-height:1.45}
html[lang="hi"] .lead,html[lang="hi"] p,html[lang="hi"] li,html[lang="hi"] dd{line-height:1.75}
html[lang="hi"] .eyebrow,html[lang="hi"] .re-badges span,html[lang="hi"] .re-et{font-family:Inter,"Noto Sans Devanagari","Kohinoor Devanagari","Nirmala UI",Mangal,sans-serif;font-size:.8rem;text-transform:none}
'''
def tema(s):
    if 'html[lang="hi"]' in s: return s
    return sub1(s, "@media(prefers-reduced-motion:reduce){.re-hero .re-bg img", TEMA_CSS + "@media(prefers-reduced-motion:reduce){.re-hero .re-bg img")
rw('seo-tools/real-estate-tema.py', tema)

# ------------------------------------------------------------------ 10) menu video, sito, org-descrizione: /hi/ non e' una lingua del sito principale
rw('seo-tools/menu-video-2026-10-23.py', lambda s: s if "'sq', 'hr', 'hi')" in s else sub1(s, "'ro', 'sq', 'hr')", "'ro', 'sq', 'hr', 'hi')"))
rw('seo-tools/real-estate-sito.py', lambda s: s if "'hi': '/hi/real-estate/'" in s else sub1(s, "'hr': '/hr/real-estate/'}", "'hr': '/hr/real-estate/', 'hi': '/hi/real-estate/'}"))
rw('seo-tools/org-descrizione.py', lambda s: s if "'tr','hi')" in s else sub1(s, "if top in ('zh','zh-hant','ar','tr'): continue", "if top in ('zh','zh-hant','ar','tr','hi'): continue"))
print('fatto: ora lanciare  bash seo-tools/real-estate-tutto.sh')
