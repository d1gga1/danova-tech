#!/usr/bin/env bash
# ==========================================================
# IndexNow — avvisa Bing, Yandex, Seznam e Naver che il sito
# è cambiato. Google NON usa IndexNow: per Google basta la
# sitemap più "Controllo URL > Richiedi indicizzazione" in
# Search Console.
#
# Uso:  bash seo-tools/indexnow.sh
# Da rilanciare ogni volta che pubblichi pagine nuove.
# ==========================================================
set -euo pipefail

HOST="danova-tech.com"
KEY="81da9a431c4048adb4cd4e8beba20b8f"
KEY_LOCATION="https://$HOST/$KEY.txt"

URLS=$(python3 - <<'PY'
import urllib.request, re
xml = urllib.request.urlopen("https://danova-tech.com/sitemap.xml").read().decode()
locs = re.findall(r"<loc>(.*?)</loc>", xml)
print(",".join('"%s"' % u for u in locs))
PY
)

BODY=$(cat <<JSON
{
  "host": "$HOST",
  "key": "$KEY",
  "keyLocation": "$KEY_LOCATION",
  "urlList": [$URLS]
}
JSON
)

echo "Invio a IndexNow..."
curl -sS -X POST "https://api.indexnow.org/IndexNow" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d "$BODY" -w "\nHTTP %{http_code}\n"
echo "Fatto. HTTP 200 o 202 = accettato."
