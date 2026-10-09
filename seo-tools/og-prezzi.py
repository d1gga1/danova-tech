# -*- coding: utf-8 -*-
"""Immagini social (1200x630) delle cinque pagine listino, con le cifre.
   Uso: python3 seo-tools/og-prezzi.py   (rifarle se cambiano i prezzi)"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
FD=os.path.join(ROOT,'assets/fonts')
def F(name,size,w):
    f=ImageFont.truetype(os.path.join(FD,name),size); f.set_variation_by_axes([w]); return f
T={
 'it':('Listino 2026','Prezzi scritti, non sussurrati.',
       [('Sito web','24,80 € / mese','oppure 350 € una tantum'),
        ('Applicazione web','50 € / mese','oppure pronta da 750 €'),
        ('Gestionale su misura','da 1.500 €','prezzo fisso dopo l\'analisi')],
       'Tutti i prezzi IVA inclusa','danova-tech.com/prezzi'),
 'en':('Price list 2026','Prices written down, not whispered.',
       [('Website','€24.80 / month','or €350 one-off'),
        ('Web app','€50 / month','or ready-made from €750'),
        ('Custom ERP','from €1,500','fixed price after analysis')],
       'All prices VAT included','danova-tech.com/en/pricing'),
 'de':('Preisliste 2026','Preise, die schwarz auf weiß stehen.',
       [('Website','24,80 € / Monat','oder 350 € einmalig'),
        ('Web-App','50 € / Monat','oder fertig ab 750 €'),
        ('ERP nach Maß','ab 1.500 €','Festpreis nach der Analyse')],
       'Alle Preise inkl. MwSt.','danova-tech.com/de/preise'),
 'fr':('Tarifs 2026','Des prix écrits, pas murmurés.',
       [('Site internet','24,80 € / mois','ou 350 € en une fois'),
        ('Application web','50 € / mois','ou prête dès 750 €'),
        ('Logiciel de gestion','dès 1 500 €','prix fixe après analyse')],
       'Tous les prix TVA incluse','danova-tech.com/fr/tarifs'),
 'es':('Precios 2026','Precios escritos, no susurrados.',
       [('Página web','24,80 € / mes','o 350 € en un pago'),
        ('Aplicación web','50 € / mes','o lista desde 750 €'),
        ('Software de gestión','desde 1.500 €','precio cerrado tras el análisis')],
       'Todos los precios con IVA incluido','danova-tech.com/es/precios'),
}
W,H=1200,630
def make(lang):
    eb,h,rows,vat,url=T[lang]
    im=Image.new('RGB',(W,H),(4,6,12))
    glow=Image.new('RGB',(W,H),(0,0,0)); g=ImageDraw.Draw(glow)
    g.ellipse((700,-260,1400,380),fill=(20,70,190)); g.ellipse((-300,420,400,900),fill=(10,40,120))
    glow=glow.filter(ImageFilter.GaussianBlur(160))
    im=Image.blend(im,glow,.55)
    d=ImageDraw.Draw(im)
    logo=Image.open(os.path.join(ROOT,'assets/img/logo.png')).convert('RGBA').resize((56,56),Image.LANCZOS)
    im.paste(logo,(64,52),logo)
    d.text((134,58),'DANOVA',font=F('sora-latin.woff2',26,800),fill=(255,255,255))
    d.text((134+d.textlength('DANOVA ',font=F('sora-latin.woff2',26,800)),58),'TECH',font=F('sora-latin.woff2',26,300),fill=(188,214,255))
    d.text((W-64,66),eb.upper(),font=F('inter-latin.woff2',18,600),fill=(77,139,255),anchor='ra')
    d.text((64,140),h,font=F('sora-latin.woff2',44,700),fill=(255,255,255))
    y=232
    for name,amt,sub in rows:
        d.rounded_rectangle((64,y,W-64,y+92),radius=18,fill=(14,20,36),outline=(40,60,110),width=2)
        d.text((96,y+22),name,font=F('inter-latin.woff2',28,600),fill=(233,237,247))
        d.text((96,y+58),sub,font=F('inter-latin.woff2',19,400),fill=(141,151,174))
        d.text((W-96,y+46),amt,font=F('sora-latin.woff2',40,700),fill=(255,255,255),anchor='rm')
        y+=106
    d.text((64,H-44),vat,font=F('inter-latin.woff2',20,500),fill=(188,214,255),anchor='ls')
    d.text((W-64,H-44),url,font=F('inter-latin.woff2',20,500),fill=(77,139,255),anchor='rs')
    out=os.path.join(ROOT,'assets/img/og-prezzi-%s.jpg'%lang)
    im.save(out,'JPEG',quality=88,optimize=True,progressive=True); return out
if __name__=='__main__':
    for l in T: print(make(l), os.path.getsize(make(l)))
