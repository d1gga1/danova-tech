#!/usr/bin/env bash
# ==========================================================
# IndexNow — avvisa Bing (e quindi ChatGPT/Copilot), Yandex, Seznam e Naver
# che il sito è cambiato. Google NON usa IndexNow: per Google bastano la
# sitemap e "Controllo URL > Richiedi indicizzazione" in Search Console.
#
# Uso:  bash seo-tools/indexnow.sh          (solo pagine nuove/modificate)
#       bash seo-tools/indexnow.sh --tutte  (tutte le pagine della sitemap)
#
# 23/10/2026: 1) aspetta che GitHub Pages abbia pubblicato la sitemap nuova
# (prima partiva subito dopo il push e leggeva quella vecchia);
# 2) invia solo gli indirizzi con <lastmod> più recente dell'ultimo invio
# (registro in seo-tools/indexnow-ultimo-invio.txt).
# ==========================================================
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - "${1:-}" <<'PY'
import json, re, sys, time, urllib.request, datetime, os
HOST = "danova-tech.com"; KEY = "81da9a431c4048adb4cd4e8beba20b8f"
REG = "seo-tools/indexnow-ultimo-invio.txt"
locale = open("sitemap.xml", encoding="utf-8").read()
def voci(xml):
    return re.findall(r"<url>\s*<loc>(.*?)</loc>.*?<lastmod>(.*?)</lastmod>", xml, re.S)
attese = len(voci(locale))
print("Attendo la pubblicazione su GitHub Pages (%d pagine nella sitemap locale)..." % attese)
for i in range(30):
    try:
        req = urllib.request.Request("https://%s/sitemap.xml?nocache=%d" % (HOST, time.time()), headers={"Cache-Control": "no-cache"})
        online = urllib.request.urlopen(req, timeout=20).read().decode()
        if len(voci(online)) == attese and online.strip() == locale.strip():
            print("Sitemap online aggiornata."); break
    except Exception as e:
        print("  (attesa:", e, ")")
    time.sleep(20)
else:
    print("ATTENZIONE: dopo 10 minuti la sitemap online non coincide ancora con quella locale. Riprova più tardi."); sys.exit(1)
tutte = sys.argv[1] == "--tutte"
ultimo = open(REG).read().strip() if os.path.exists(REG) and not tutte else "0000-00-00"
urls = [u for u, lm in voci(locale) if lm >= ultimo]
if not urls:
    print("Nessuna pagina nuova o modificata dall'ultimo invio (%s)." % ultimo); sys.exit(0)
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": "https://%s/%s.txt" % (HOST, KEY), "urlList": urls[:10000]}).encode()
r = urllib.request.urlopen(urllib.request.Request("https://api.indexnow.org/IndexNow", data=body,
        headers={"Content-Type": "application/json; charset=utf-8"}), timeout=60)
print("Inviati %d indirizzi a IndexNow: HTTP %d (200 o 202 = accettato)." % (len(urls), r.status))
open(REG, "w").write(datetime.date.today().isoformat())
PY
