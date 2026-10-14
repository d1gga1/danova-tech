# Aggiunge la recensione Google reale di Expo Fairs S.R.O in cima a "Dicono di noi" + badge Google.
import os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
Q="We worked with Danova on our trade fair booth in Milan and they did an absolutely beautiful job. Highly recommended!"
MAPS="https://maps.app.goo.gl/gPgYPeA5Rtc12wve8"
ROLE={'it':'Recensione Google · stand fieristico a Milano','en':'Google review · trade fair stand in Milan',
      'de':'Google-Bewertung · Messestand in Mailand','fr':'Avis Google · stand de salon à Milan','es':'Reseña de Google · stand ferial en Milán'}
BADGE={'it':'5,0 su Google · leggi le recensioni','en':'5.0 on Google · read the reviews','de':'5,0 bei Google · Bewertungen lesen',
       'fr':'5,0 sur Google · lire les avis','es':'5,0 en Google · leer las reseñas'}
PAGE={'it':'index.html','en':'en/index.html','de':'de/index.html','fr':'fr/index.html','es':'es/index.html'}
for l in ROLE:
    js=f'assets/js/i18n-{l}.js'; s=open(js,encoding='utf-8').read()
    if 'Expo Fairs' not in s:
        s=re.sub(r"(dicono:\{\s*eyebrow:[^\n]*\n\s*items:\[\n)",lambda m:m.group(1)+f"      ['{Q}','EF','Expo Fairs S.R.O','{ROLE[l]}'],\n",s,1)
        assert 'Expo Fairs' in s, js; open(js,'w',encoding='utf-8').write(s)
    p=PAGE[l]; h=open(p,encoding='utf-8').read()
    if 'Expo Fairs' not in h:
        h=h.replace('<div class="q on">','<div class="q ">')
        new=f'''<div class="tst" id="tst">
    <div class="q on">
      <blockquote>“{Q}”</blockquote>
      <div class="who"><div class="av">EF</div><div><b>Expo Fairs S.R.O</b><small>{ROLE[l]}</small></div></div>
    </div>'''
        assert h.count('<div class="tst" id="tst">')==1; h=h.replace('<div class="tst" id="tst">',new)
        h=re.sub(r'<div class="tst-dots" id="tstDots">.*?</div>',
          '<div class="tst-dots" id="tstDots">'+''.join(f'<i class="{"on" if i==0 else ""}" data-i="{i}"></i>' for i in range(5))+'</div>\n'
          f'    <a class="tst-g" href="{MAPS}" target="_blank" rel="noopener"><span aria-hidden="true">★★★★★</span> {BADGE[l]}</a>',h,1,flags=re.S)
        h=h.replace('.tst-dots i.on{','.tst-g{display:inline-flex;gap:10px;align-items:center;margin-top:26px;font-size:14px;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:8px 16px;transition:border-color .3s,color .3s}.tst-g span{color:#f5b301;letter-spacing:2px}.tst-g:hover{color:var(--text);border-color:var(--line-strong)}\n.tst-dots i.on{',1)
        h=re.sub(rf'(/assets/js/i18n-{l}\.js)(\?v=[^"]*)?"',r'\1?v=20261014r"',h)
        open(p,'w',encoding='utf-8').write(h)
    print(l,'ok')
