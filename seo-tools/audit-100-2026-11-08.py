# Audit automatico dei punti "on-site" della lista delle 100 discipline (8/11/2026)
import os, re, json, collections, sys
from bs4 import BeautifulSoup
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP=('.git','_to_delete','_archivio','seo-tools','assets','node_modules')
pages={}
for d,ds,fs in os.walk(ROOT):
    ds[:]=[x for x in ds if x not in SKIP]
    for f in fs:
        if f.endswith('.html'):
            p=os.path.join(d,f); pages[os.path.relpath(p,ROOT)]=open(p,encoding='utf-8',errors='ignore').read()
redirect={k for k,v in pages.items() if re.search(r'http-equiv=["\']refresh',v[:4000],re.I)}
real={k:v for k,v in pages.items() if k not in redirect}
noidx={k for k,v in real.items() if re.search(r'<meta name="robots" content="[^"]*noindex',v)}
print('html',len(pages),'redirect',len(redirect),'reali',len(real),'noindex',len(noidx))
C=collections.Counter(); ex=collections.defaultdict(list)
types=collections.Counter(); titles=collections.defaultdict(list)
def flag(k,p):
    C[k]+=1
    if len(ex[k])<4: ex[k].append(p)
for p,h in real.items():
    s=BeautifulSoup(h,'html.parser')
    t=s.title.string.strip() if s.title and s.title.string else ''
    titles[t].append(p)
    if not t: flag('no_title',p)
    elif len(t)>65: flag('title>65',p)
    md=s.find('meta',attrs={'name':'description'})
    if not md: flag('no_desc',p)
    elif len(md.get('content',''))>160: flag('desc>160',p)
    elif len(md.get('content',''))<70: flag('desc<70',p)
    if not s.find('link',rel='canonical'): flag('no_canonical',p)
    h1=s.find_all('h1')
    if len(h1)!=1: flag('h1!=1',p)
    if not s.html.get('lang'): flag('no_lang',p)
    if not s.find('meta',property='og:image'): flag('no_og_image',p)
    if not s.find('meta',attrs={'name':'twitter:card'}): flag('no_twitter',p)
    lds=s.find_all('script',type='application/ld+json')
    if not lds: flag('no_jsonld',p)
    tt=set()
    for l in lds:
        try:
            j=json.loads(l.string or '')
        except Exception: flag('jsonld_invalid',p); continue
        def walk(o):
            if isinstance(o,dict):
                ty=o.get('@type')
                if ty: [tt.add(x) for x in (ty if isinstance(ty,list) else [ty])]
                for v in o.values(): walk(v)
            elif isinstance(o,list):
                for v in o: walk(v)
        walk(j)
    for x in tt: types[x]+=1
    if 'BreadcrumbList' not in tt and p!='index.html': flag('no_breadcrumb',p)
    if 'dateModified' not in h: flag('no_dateModified',p)
    if not re.search(r'"author"',h): flag('no_author',p)
    if 'speakable' not in h: flag('no_speakable',p)
    if not s.find('a',href=re.compile('^#(main|contenuto|content)')): flag('no_skiplink',p)
    if not s.find('main'): flag('no_main',p)
    for im in s.find_all('img'):
        if im.get('alt') is None: flag('img_no_alt',p)
        if not (im.get('width') and im.get('height')): flag('img_no_dims',p)
    for b in s.find_all('button'):
        if not (b.get_text(strip=True) or b.get('aria-label') or b.get('title')): flag('button_no_name',p)
    for a in s.find_all('a'):
        if not (a.get_text(strip=True) or a.get('aria-label') or a.find('img',alt=True)): flag('link_no_name',p)
    for i in s.find_all(['input','textarea','select']):
        if i.get('type') in ('hidden','submit'): continue
        iid=i.get('id')
        if not (i.get('aria-label') or (iid and s.find('label',attrs={'for':iid})) or i.find_parent('label')): flag('input_no_label',p)
    for sc in s.find_all('script',src=True):
        if not (sc.has_attr('defer') or sc.has_attr('async') or sc.get('type')=='module'): flag('script_blocking',p)
    if len(h)>250000: flag('html>250KB',p)
    if s.find('video') and 'VideoObject' not in tt: flag('video_no_schema',p)
    if re.search(r'<details|class="faq',h) and 'FAQPage' not in tt: flag('faq_no_schema',p)
    if not s.find('meta',attrs={'name':'viewport'}): flag('no_viewport',p)
    if 'hreflang' not in h: flag('no_hreflang',p)
dup={t:v for t,v in titles.items() if len(v)>1}
print('titoli duplicati',len(dup), list(dup.items())[:3])
for k,v in sorted(C.items(),key=lambda x:-x[1]): print(f'{k:20} {v:6}  es: {ex[k][:3]}')
print('\nTIPI SCHEMA:',types.most_common(40))
