# -*- coding: utf-8 -*-
"""24/10/2026 - Converte le immagini originali della sezione Real Estate
   (seo-tools/real-estate-media/orig/*.png, generate con Higgsfield) nei formati del sito:
   assets/img/re/NOME.webp (1600px), NOME-800.webp, NOME.jpg (1200x630 per og:image).
   Salta i file gia' aggiornati.  Uso: python3 seo-tools/real-estate-media.py"""
import os, glob
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, 'real-estate-media', 'orig'); DST = os.path.join(ROOT, 'assets', 'img', 're')
os.makedirs(DST, exist_ok=True)
def fit(im, w, h):
    r = max(w / im.width, h / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x = (im.width - w) // 2; y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))
n = 0
for f in sorted(glob.glob(os.path.join(SRC, '*.png'))):
    nome = os.path.splitext(os.path.basename(f))[0]
    out = os.path.join(DST, nome + '.webp')
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(f): continue
    im = Image.open(f).convert('RGB')
    fit(im, 1600, 900).save(out, 'WEBP', quality=78, method=6)
    fit(im, 800, 450).save(os.path.join(DST, nome + '-800.webp'), 'WEBP', quality=74, method=6)
    fit(im, 1200, 630).save(os.path.join(DST, nome + '.jpg'), 'JPEG', quality=82, optimize=True, progressive=True)
    n += 1
print('immagini convertite:', n)

# --- video: seo-tools/real-estate-media/vorig/*.mp4 -> assets/video/re/NOME.mp4 (720p, senza audio, faststart)
import subprocess
VS = os.path.join(HERE, 'real-estate-media', 'vorig'); VD = os.path.join(ROOT, 'assets', 'video', 're')
os.makedirs(VD, exist_ok=True); nv = 0
for f in sorted(glob.glob(os.path.join(VS, '*.mp4'))):
    out = os.path.join(VD, os.path.basename(f))
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(f): continue
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f, '-an', '-vf', 'scale=1280:-2,fps=30',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '27', '-pix_fmt', 'yuv420p',
                    '-movflags', '+faststart', out], check=True)
    nv += 1
print('video convertiti:', nv)
