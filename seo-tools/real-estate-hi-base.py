# -*- coding: utf-8 -*-
"""29/10/2026 - Danova Real Estate, HI (हिंदी): base comune ai file real-estate-tr-hi-*.py (helper, FAQ di base).
   Non e' un file di dati (il nome non inizia con real-estate-tr-): lo caricano i file tr-hi.
   Nomi di citta' e localita' in caratteri latini (come li cercano gli indiani in Italia: Treviso, Venice, Padua)."""
import importlib.util, os
_H = os.path.dirname(os.path.abspath(__file__))
def _ld(n, f):
    s = importlib.util.spec_from_file_location(n, os.path.join(_H, f)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
L = _ld('relingue', 'real-estate-lingue.py'); IT = _ld('re1', 'real-estate-dati-1.py')
LANG = 'hi'; OGGI = IT.OGGI; G = IT.G; _G = IT._G
u = lambda k: L.url(k, LANG)
N = lambda n: L.nome(n, LANG)
RE = ("Real Estate", u('/real-estate/'))
def svc(name, typ, desc, cat, area=IT.AREA):
    return {"name": name, "type": typ, "desc": desc, "area": area, "lingue": IT.LG, "catalogo": cat}
def A(k, t): return '<a href="%s">%s</a>' % (u(k), t)
FAQ_BASE = [
 ("क्या साइट सर्वे सच में मुफ़्त है?", "हाँ। हम प्रॉपर्टी पर आते हैं, नाप लेते हैं, प्लंबिंग-बिजली और ढाँचे की जाँच करते हैं और आपको हर काम की अलग-अलग कीमत के साथ लिखित कोटेशन देते हैं। आपको कुछ भी नहीं देना पड़ता और कोई बाध्यता नहीं होती।"),
 ("फ़िक्स्ड प्राइस का क्या मतलब है?", "कॉन्ट्रैक्ट में लिखी कीमत ही बताए गए कामों की अंतिम कीमत है। अगर काम के दौरान आप कुछ जोड़ना या बदलना चाहें, तो हम पहले उसका लिखित कोटेशन देते हैं: आपकी मंज़ूरी के बिना बिल में कोई अतिरिक्त ख़र्च नहीं जुड़ता।"),
 ("आप समय-सीमा की गारंटी कैसे देते हैं?", "काम शुरू होने की तारीख़, हैंडओवर की तारीख़ और बीच के चरण कॉन्ट्रैक्ट में काम के शेड्यूल के साथ लिखे जाते हैं। टीमें और सामान साइट खुलने से पहले ही तय कर लिए जाते हैं, इसलिए समय-सीमा आख़िरी समय की उपलब्धता पर निर्भर नहीं रहती।"),
 ("आप किन इलाक़ों में काम करते हैं?", "पूरे Veneto और Friuli Venezia Giulia (उत्तर-पूर्वी इटली) में: Treviso, Venice, Padua, Vicenza, Verona, Belluno, Rovigo, Pordenone, Udine, Gorizia और Trieste प्रांत। हमारा मुख्यालय Treviso प्रांत के Mansuè में है, Treviso, Pordenone और Venice के बीच।"),
 ("क्या मैं आपसे हिंदी में बात कर सकता हूँ?", "हाँ, लिखित रूप में: कोटेशन, कॉन्ट्रैक्ट का सारांश और साइट के अपडेट आप हिंदी में भी पा सकते हैं (WhatsApp और ईमेल पर)। हमारी टीम इतालवी, अंग्रेज़ी और रोमानियाई बोलती है, इसलिए साइट पर मीटिंग इनमें से किसी भाषा में या आपके किसी परिचित की मदद से होती है।"),
]
