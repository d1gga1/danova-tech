# -*- coding: utf-8 -*-
"""24/10/2026 (v2) - Media della sezione Real Estate, ottimizzati per qualita' e peso.
   IMMAGINI  seo-tools/real-estate-media/orig/NOME.png (2688x1520, Higgsfield) ->
     assets/img/re/NOME-{480,800,1200,1600,2000,2688}.avif + .webp   (16:9 intero, nessun ritaglio)
     assets/img/re/NOME.webp (1600) e NOME-800.webp                   (compatibilita' con i vecchi riferimenti)
     assets/img/re/NOME.jpg (1200x630)                                (og:image / anteprime social)
   VIDEO     seo-tools/real-estate-media/vorig/NOME.mp4 (1276x720, 24 fps) ->
     assets/video/re/NOME.av1.mp4  (AV1, browser moderni, ~0,8 MB)
     assets/video/re/NOME.mp4      (H.264 alta qualita', riserva per tutti)
     assets/img/re/NOME-poster.webp/.avif (primo fotogramma, locandina leggera)
   Risoluzione e fotogrammi originali (niente ridimensionamento ne' 30 fps forzati), senza audio, faststart.
   Salta i file gia' aggiornati.  Uso: python3 seo-tools/real-estate-media.py [img|video] [filtro-nome]"""
import os, glob, sys, subprocess, shutil
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, 'real-estate-media', 'orig'); DST = os.path.join(ROOT, 'assets', 'img', 're')
VS = os.path.join(HERE, 'real-estate-media', 'vorig'); VD = os.path.join(ROOT, 'assets', 'video', 're')
os.makedirs(DST, exist_ok=True); os.makedirs(VD, exist_ok=True)
W = [480, 800, 1200, 1600, 2000, 2688]
cosa = sys.argv[1] if len(sys.argv) > 1 else 'tutto'; filtro = sys.argv[2] if len(sys.argv) > 2 else ''

def fit(im, w, h):
    r = max(w / im.width, h / im.height); im2 = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x = (im2.width - w) // 2; y = (im2.height - h) // 2
    return im2.crop((x, y, x + w, y + h))
def h169(w): return round(w * 9 / 16 / 2) * 2
def nuovo(out, src): return os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src)
def salva(im, base, w):
    x = fit(im, w, h169(w))
    x.save(base + '.webp', 'WEBP', quality=84 if w <= 1200 else 82, method=6)
    x.save(base + '.avif', 'AVIF', quality=62 if w <= 1200 else 58, speed=4)
    return x

if cosa in ('tutto', 'img'):
    n = 0
    for f in sorted(glob.glob(os.path.join(SRC, '*.png'))):
        nome = os.path.splitext(os.path.basename(f))[0]
        if filtro and filtro not in nome: continue
        if nuovo(os.path.join(DST, nome + '-2688.avif'), f): continue
        im = Image.open(f).convert('RGB')
        for w in W: salva(im, os.path.join(DST, '%s-%d' % (nome, w)), w)
        shutil.copyfile(os.path.join(DST, nome + '-1600.webp'), os.path.join(DST, nome + '.webp'))
        fit(im, 1200, 630).save(os.path.join(DST, nome + '.jpg'), 'JPEG', quality=86, optimize=True, progressive=True)
        n += 1
    print('immagini convertite:', n)

if cosa in ('tutto', 'video'):
    nv = 0
    for f in sorted(glob.glob(os.path.join(VS, '*.mp4'))):
        nome = os.path.splitext(os.path.basename(f))[0]
        if filtro and filtro not in nome: continue
        h264 = os.path.join(VD, nome + '.mp4'); av1 = os.path.join(VD, nome + '.av1.mp4')
        poster = os.path.join(DST, nome + '-poster.webp')
        if nuovo(av1, f) and nuovo(h264, f) and os.path.exists(poster): continue
        base = ['ffmpeg', '-y', '-loglevel', 'error', '-i', f, '-an', '-vf', 'crop=trunc(iw/2)*2:trunc(ih/2)*2', '-pix_fmt', 'yuv420p', '-movflags', '+faststart']
        if not (nuovo(av1, f) and nuovo(h264, f)):   # 29/10/2026: se manca solo la locandina, si rifà solo quella
          subprocess.run(base + ['-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-profile:v', 'high', '-tune', 'film', h264], check=True)
          subprocess.run(base + ['-c:v', 'libaom-av1', '-crf', '32', '-b:v', '0', '-cpu-used', '6', '-row-mt', '1', '-tiles', '2x2', av1], check=True)
        import tempfile; png = os.path.join(tempfile.gettempdir(), nome + '-poster.png')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f, '-frames:v', '1', png], check=True)
        p = Image.open(png).convert('RGB'); os.remove(png)
        p.save(os.path.join(DST, nome + '-poster.webp'), 'WEBP', quality=80, method=6)
        nv += 1
    print('video convertiti:', nv)
