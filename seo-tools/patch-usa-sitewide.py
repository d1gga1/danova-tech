# -*- coding: utf-8 -*-
"""Collegamenti e dati strutturati per il mercato USA su tutto il sito. Idempotente.
   - link contestuali alle pagine USA nelle pagine servizi inglesi (box "altri")
   - colonna "Mercados" del footer spagnolo: Estados Unidos, Miami, Houston
   - areaServed dell'Organization: aggiunge United States
   Uso:  python3 seo-tools/patch-usa-sitewide.py"""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, h): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(h)

ALTRI = {
 'en/services/index.html': [("Web &amp; software for US businesses","/en/united-states/")],
 'en/services/websites-ecommerce/index.html': [("Small business web design","/en/small-business-web-design/"),("WordPress web design","/en/wordpress-web-design/"),("Web design agency USA","/en/web-design-agency-usa/"),("Shopify development agency","/en/shopify-development-agency/"),("Web design New York","/en/web-design-new-york/"),("Web design Los Angeles","/en/web-design-los-angeles/"),("ADA website compliance","/en/ada-website-compliance/")],
 'en/services/custom-apps/index.html': [("Hire app developers","/en/hire-app-developers/"),("Web app development company","/en/web-app-development-company/"),("Mobile app development USA","/en/mobile-app-development-company-usa/"),("How much does an app cost","/en/how-much-does-an-app-cost/"),("MVP development for startups","/en/mvp-development-for-startups/"),("Software &amp; app development New York","/en/software-development-new-york/")],
 'en/services/erp-crm/index.html': [("Custom CRM development","/en/custom-crm-development/"),("Custom MES software","/en/mes-software-development/"),("Property management software","/en/property-management-software-development/"),("Custom ERP &amp; CRM development USA","/en/custom-erp-crm-development-usa/"),("How much does custom software cost","/en/how-much-does-custom-software-cost/"),("Manufacturing software","/en/manufacturing-software-development/")],
 'en/services/software-automation/index.html': [("Business process automation","/en/business-process-automation/"),("API integration services","/en/api-integration-services/"),("Software development company USA","/en/software-development-company-usa/"),("Outsourcing software development to Europe","/en/outsourcing-software-development-to-europe/"),("Field service apps","/en/field-service-app-development/")],
 'en/services/seo/index.html': [("SEO company for US businesses","/en/seo-company-usa/"),("ADA website audit","/en/ada-website-audit/"),("Web design agency USA","/en/web-design-agency-usa/"),("Contractor website design","/en/contractor-website-design/"),("Law firm websites","/en/web-design-for-law-firms/")],
 'en/services/google-ads/index.html': [("US businesses","/en/united-states/")],
 'en/services/meta-ads/index.html': [("US businesses","/en/united-states/")],
 'en/how-much-does-a-website-cost/index.html': [("How much does an app cost","/en/how-much-does-an-app-cost/"),("How much does custom software cost","/en/how-much-does-custom-software-cost/"),("Web design agency USA","/en/web-design-agency-usa/")],
 'en/software-development-italy/index.html': [("Outsourcing software development to Europe","/en/outsourcing-software-development-to-europe/"),("Software development company USA","/en/software-development-company-usa/")],
 'en/about/index.html': [("Working with US businesses","/en/united-states/")],
}
n = 0
for p, links in ALTRI.items():
    if not os.path.exists(os.path.join(ROOT, p)): print('manca', p); continue
    h = rd(p)
    h2 = re.sub(r'\s*<!-- usa-link -->.*?<!-- /usa-link -->', '', h, flags=re.S)
    h2 = re.sub(r'(<div class="pg-altri"[^>]*>)\s*<!-- usa -->.*?<!-- /usa -->', r'\1', h2, flags=re.S)
    blocco = '\n      <!-- usa-link -->' + ''.join('\n      <a href="%s">%s</a>' % (u, t) for t, u in links) + '\n      <!-- /usa-link -->'
    h2, k = re.subn(r'(<div class="pg-altri"[^>]*>)', lambda m: m.group(1) + blocco, h2, count=1)
    if not k: print('nessun box altri in', p); continue
    if h2 != h: wr(p, h2); n += 1
print('box collegati aggiornati:', n)

# footer spagnolo
ES = [("/es/estados-unidos/","Estados Unidos"),("/es/diseno-web-miami/","Diseño web Miami"),("/es/diseno-web-houston/","Diseño web Houston")]
n = 0
for dp, dn, fn in os.walk(os.path.join(ROOT, 'es')):
    for f in fn:
        if f != 'index.html': continue
        p = os.path.relpath(os.path.join(dp, f), ROOT); h = rd(p)
        h2 = re.sub(r'\s*<!-- usa -->.*?<!-- /usa -->', '', h, flags=re.S)
        b = '\n        <!-- usa -->' + ''.join('\n        <li><a href="%s">%s</a></li>' % l for l in ES) + '\n        <!-- /usa -->'
        h2 = re.sub(r'(<h5>Mercados</h5><ul>)', lambda m: m.group(1) + b, h2, count=1)
        if h2 != h: wr(p, h2); n += 1
print('footer spagnoli aggiornati:', n)

# areaServed: United States nell'Organization di tutte le pagine
USA = {"@type": "Country", "name": "United States"}
n = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('.git', 'seo-tools', 'assets', '_archivio')]
    for f in fn:
        if not f.endswith('.html'): continue
        p = os.path.relpath(os.path.join(dp, f), ROOT); h = rd(p); cambiato = False
        def fix(m):
            global cambiato
            try: d = json.loads(m.group(1))
            except Exception: return m.group(0)
            nodi = d.get('@graph', [d]); mod = False
            for x in nodi:
                if isinstance(x, dict) and str(x.get('@id', '')).endswith('/#organization') and isinstance(x.get('areaServed'), list):
                    if not any(isinstance(a, dict) and a.get('name') in ('United States', 'Stati Uniti', 'Estados Unidos') for a in x['areaServed']):
                        x['areaServed'].append(USA); mod = True
            if not mod: return m.group(0)
            return '<script type="application/ld+json">\n' + json.dumps(d, ensure_ascii=False, indent=2) + '\n</script>'
        h2 = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, h, flags=re.S)
        if h2 != h: wr(p, h2); n += 1
print('Organization con United States:', n, 'pagine')
