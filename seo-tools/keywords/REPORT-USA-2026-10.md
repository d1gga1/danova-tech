# Mercato USA — analisi Keyword Planner (10 ottobre 2026)

Fonte: 9 CSV di Google Ads in `planner-2026-10/usa/`, Stati Uniti, inglese (+ 1 spagnolo),
periodo set 2025 – ago 2026. 20.138 keyword uniche (riepilogo in `tutte.json`,
rigenerabile con `python3 seo-tools/analizza-planner-usa.py`).

**Attenzione:** l'account non ha spesa attiva, quindi Google mostra i volumi a fasce
(50 / 500 / 5.000 / 50.000 / 500.000). Servono per confrontare, non come numeri esatti.
Le offerte (CPC) sono in euro.

## 1. Cosa cercano davvero nelle città
| Formula | Somma volumi 31 città | Decisione |
|---|---|---|
| website design {città} | ~92.000 | titoli città → "Web Design Company / Website Design" |
| web design {città} | ~83.000 | idem |
| seo company {città} | ~60.000 | pagina nazionale SEO creata; città SEO = prossimo passo |
| web design company {città} | ~49.000 | nel titolo e nell'H1 delle città |
| website development {città} | ~27.000 | nella descrizione |
| mobile app development company {città} | ~10.600 | pagine "App Development Company in {città}" |
| app development / app developers {città} | ~14.600 | idem |
| software development / custom software {città} | ~7.000 | idem |
| ecommerce / shopify / crm / erp {città} | quasi zero | **niente pagine città** per questi |

Città più forti (somma volumi): Dallas, New York, San Diego, Atlanta, Phoenix, Chicago, Houston,
Austin, Miami, Denver, Tampa. Dallas ha **5.000** ricerche per "mobile app development company dallas"
(New York solo 500): per questo Dallas ha la sua pagina app/software.
Città deboli (< 2.500): San Jose, Columbus, Detroit, Las Vegas, Nashville. Le pagine restano, ma
non vanno spinte con Google Ads.

## 2. Ricerche nazionali con volume e valore
| Keyword | Volume | CPC alto | Pagina |
|---|---|---|---|
| custom software development company | 5.000 | 71 € | /en/software-development-company-usa/ (titolo aggiornato) |
| software development company usa | 5.000 | 52 € | idem |
| app development company usa | 5.000 | 39 € | /en/mobile-app-development-company-usa/ |
| hire app developers | 5.000 | 68 € | **nuova** /en/hire-app-developers/ |
| web design for small business / website designers for small business | 5.000 | 28–44 € | **nuova** /en/small-business-web-design/ |
| affordable / cheap / low cost website design | 500 ciascuna | 23–34 € | idem (i prezzi da 350 € sono il vantaggio) |
| wordpress web designer / development | 5.000 | 43–45 € | **nuova** /en/wordpress-web-design/ |
| web app development services / companies | 5.000 | 38–42 € | **nuova** /en/web-app-development-company/ |
| business process automation | 5.000 | 69 € | **nuova** /en/business-process-automation/ |
| api integration / salesforce integration services | 5.000 / 500 | 45–52 € | **nuova** /en/api-integration-services/ |
| crm for small business | 5.000 | 53 € | **nuova** /en/custom-crm-development/ |
| property management software / app | 50.000 / 5.000 | 87–190 € | **nuova** /en/property-management-software-development/ |
| mes software / production scheduling software | 50.000 / 5.000 | 29–104 € | **nuova** /en/mes-software-development/ |
| field service management software | 50.000 | 69 € | /en/field-service-app-development/ (titolo aggiornato) |
| contractor management software | 5.000 | 275 € | /en/construction-management-software/ (titolo aggiornato) |
| law firm / attorney website design | 5.000 | 65–85 € | /en/web-design-for-law-firms/ (titolo aggiornato) |
| contractor / construction website design | 5.000 | 19–20 € | /en/contractor-website-design/ (rinominata da home-services) |
| mvp development company | 500 | 87 € | /en/mvp-development-for-startups/ (titolo aggiornato) |
| how much does it cost to make an app / app development cost | 5.000 | 10–18 € | /en/how-much-does-an-app-cost/ (titolo aggiornato) |
| ada compliance audit | 5.000 | 42 € | **nuova** /en/ada-website-audit/ |
| ada website compliance | 5.000 | 14 € | /en/ada-website-compliance/ |
| hipaa compliant website / hosting | 500 | 37–40 € | citata nella pagina studi medici |

## 3. Spagnolo
Solo "diseño web miami" ha volume (500). Le altre città sono a 50 o meno: le pagine in spagnolo
restano (costano poco e prendono una nicchia senza concorrenza), ma la priorità è l'inglese.

## 4. Prossimi passi consigliati
1. **SEO per città** (seo company {città} ≈ 60.000 ricerche): pagine dedicate per le 9 città con 5.000
   (New York, Los Angeles, Houston, Dallas, Austin, Atlanta, Phoenix, San Diego, Denver).
2. **Google Ads di prova** (budget piccolo) su keyword a CPC basso e intenzione alta: "website design {città}"
   (4–22 €), "web design for small business", "how much does it cost to make an app". Servono anche
   a sbloccare i volumi esatti nel Planner.
3. Profili su **Clutch, GoodFirms, UpCity**: dominano "top web design companies {città}".
4. Dopo la pubblicazione: sitemap in Search Console + `seo-tools/indexnow.sh`.

## Rigenerare le pagine USA
    python3 seo-tools/pagine-build-usa.py
    python3 seo-tools/patch-footer-usa.py
    python3 seo-tools/patch-usa-sitewide.py
    python3 seo-tools/llms-usa.py
    python3 seo-tools/genera-sitemap.py
