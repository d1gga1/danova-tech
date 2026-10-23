#!/usr/bin/env python3
"""Pulsante WhatsApp flottante (in basso a destra) su tutte le pagine del sito.

Idempotente: il blocco sta tra <!-- wa-fab --> e <!-- /wa-fab -->; rilanciando lo
script il blocco viene sostituito, mai duplicato. Da rilanciare dopo ogni build
che rigenera le pagine:  python3 seo-tools/whatsapp-2026-10-23.py
"""
import html, re, sys, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NUMERO = "393884706887"  # +39 388 470 6887
SALTA = {"social", "_archivio", "seo-tools", "assets", ".git", ".github"}

TESTI = {  # lingua: (etichetta, messaggio precompilato)
    "it": ("Scrivici su WhatsApp", "Ciao Danova Tech! Vi scrivo dal sito, vorrei qualche informazione."),
    "en": ("Chat with us on WhatsApp", "Hi Danova Tech! I'm writing from your website, I'd like some information."),
    "de": ("Schreiben Sie uns auf WhatsApp", "Hallo Danova Tech! Ich schreibe Ihnen über Ihre Website und hätte gerne einige Informationen."),
    "es": ("Escríbenos por WhatsApp", "¡Hola Danova Tech! Os escribo desde la web, me gustaría recibir información."),
    "fr": ("Écrivez-nous sur WhatsApp", "Bonjour Danova Tech ! Je vous écris depuis votre site, j'aimerais avoir des informations."),
    "zh-hans": ("在 WhatsApp 上联系我们", "您好 Danova Tech！我从您的网站联系您，想了解一些信息。"),
    "zh-hant": ("在 WhatsApp 上聯繫我們", "您好 Danova Tech！我從您的網站聯繫您，想了解一些資訊。"),
    "ar": ("راسلنا على واتساب", "مرحباً Danova Tech! أكتب إليكم من موقعكم وأود الحصول على بعض المعلومات."),
    "tr": ("WhatsApp'tan bize yazın", "Merhaba Danova Tech! Web sitenizden yazıyorum, bilgi almak istiyorum."),
}

LOGO = ("M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347"
        "m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884"
        "m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z")

CSS = (
    ".wa-fab{position:fixed;right:24px;bottom:24px;z-index:9996;width:62px;height:62px;border-radius:50%;"
    "display:grid;place-items:center;color:#fff;text-decoration:none;"
    "background:linear-gradient(145deg,#6fdc7f,#25d366 55%,#1fb457);"
    "box-shadow:0 10px 28px rgba(37,211,102,.38),0 0 0 14px rgba(37,211,102,.07),0 0 60px 22px rgba(37,211,102,.10);"
    "animation:wa-in .7s cubic-bezier(.16,1,.3,1) 1.2s backwards;transition:transform .35s cubic-bezier(.16,1,.3,1),box-shadow .35s}"
    ".wa-fab svg{width:32px;height:32px;position:relative;z-index:1;animation:wa-ring 6s ease-in-out 3s infinite}"
    ".wa-fab:before,.wa-fab:after{content:'';position:absolute;inset:0;border-radius:50%;background:#25d366;"
    "opacity:.45;z-index:-1;animation:wa-pulse 2.6s cubic-bezier(.2,.6,.3,1) 2s infinite}"
    ".wa-fab:after{animation-delay:3.3s}"
    ".wa-fab:hover,.wa-fab:focus-visible{transform:scale(1.08);"
    "box-shadow:0 14px 34px rgba(37,211,102,.5),0 0 0 16px rgba(37,211,102,.10),0 0 70px 26px rgba(37,211,102,.14)}"
    ".wa-fab:focus-visible{outline:3px solid #fff;outline-offset:4px}"
    ".wa-fab span{position:absolute;right:calc(100% + 14px);top:50%;white-space:nowrap;pointer-events:none;"
    "font:600 14px/1 Inter,system-ui,sans-serif;color:#0b1a10;background:#fff;padding:10px 14px;border-radius:999px;"
    "box-shadow:0 8px 24px rgba(0,0,0,.25);opacity:0;transform:translate(8px,-50%);transition:opacity .3s,transform .3s}"
    ".wa-fab:hover span,.wa-fab:focus-visible span{opacity:1;transform:translate(0,-50%)}"
    "html body #top{bottom:104px}"
    "@keyframes wa-in{from{opacity:0;transform:scale(.3) translateY(30px)}to{opacity:1;transform:none}}"
    "@keyframes wa-pulse{0%{transform:scale(1);opacity:.45}100%{transform:scale(1.9);opacity:0}}"
    "@keyframes wa-ring{0%,88%,100%{transform:rotate(0)}90%{transform:rotate(-14deg)}92%{transform:rotate(12deg)}"
    "94%{transform:rotate(-9deg)}96%{transform:rotate(6deg)}98%{transform:rotate(-3deg)}}"
    "@media (max-width:640px){.wa-fab{right:16px;bottom:16px;width:56px;height:56px}.wa-fab svg{width:29px;height:29px}"
    ".wa-fab span{display:none}html body #top{right:20px;bottom:88px}}"
    # sotto i 760px c'e' la barra contatti di contatto.js: il pulsante sale sopra la barra
    "@media (max-width:760px){body.has-dt-bar .wa-fab{bottom:calc(82px + env(safe-area-inset-bottom))}"
    "html body.has-dt-bar #top{bottom:calc(150px + env(safe-area-inset-bottom))}"
    "body:has(.dt-bar.hide) .wa-fab{opacity:0;pointer-events:none;transform:scale(.6)}}"
    "@media (hover:none){.wa-fab span{display:none}}"
    "@media (prefers-reduced-motion:reduce){.wa-fab,.wa-fab svg,.wa-fab:before,.wa-fab:after{animation:none}"
    ".wa-fab:before,.wa-fab:after{display:none}}"
    "@media print{.wa-fab{display:none}}"
)

BLOCCO_RE = re.compile(r"\n?<!-- wa-fab -->.*?<!-- /wa-fab -->\n?", re.S)
LANG_RE = re.compile(r'<html[^>]*\blang="([^"]+)"', re.I)


def lingua(testo):
    m = LANG_RE.search(testo)
    l = (m.group(1) if m else "it").lower()
    if l.startswith("zh"):
        return "zh-hant" if "hant" in l or l.endswith(("-tw", "-hk")) else "zh-hans"
    return l.split("-")[0] if l.split("-")[0] in TESTI else "it"


def blocco(l):
    etichetta, msg = TESTI[l]
    url = f"https://wa.me/{NUMERO}?text={urllib.parse.quote(msg)}"
    e = html.escape(etichetta, quote=True)
    return (
        f"\n<!-- wa-fab -->\n<style>{CSS}</style>\n"
        f'<a class="wa-fab" href="{url}" target="_blank" rel="noopener" aria-label="{e}">'
        f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="{LOGO}"/></svg>'
        f'<span dir="auto">{e}</span></a>\n<!-- /wa-fab -->\n'
    )


def main():
    cambiate = saltate = 0
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SALTA:
            continue
        t = p.read_text(encoding="utf-8")
        i = t.lower().rfind("</body>")
        if i == -1:
            saltate += 1
            continue
        pulito = BLOCCO_RE.sub("\n", t)
        i = pulito.lower().rfind("</body>")
        nuovo = pulito[:i].rstrip("\n") + blocco(lingua(pulito)) + pulito[i:]
        if nuovo != t:
            p.write_text(nuovo, encoding="utf-8")
            cambiate += 1
    print(f"pagine aggiornate: {cambiate} - senza </body> saltate: {saltate}")


if __name__ == "__main__":
    sys.exit(main())
