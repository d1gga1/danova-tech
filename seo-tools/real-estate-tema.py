# -*- coding: utf-8 -*-
"""24/10/2026 - Tema "Danova Real Estate" (verde salvia / pietra).
   1) Genera assets/css/real-estate.css da assets/css/site.css: ogni colore bluastro diventa
      salvia con la stessa luminosita' (stesso layout, stessi effetti), piu' gli stili propri
      della sezione (prima/dopo, galleria, video, hero con immagine).
   2) Applica il tema a tutte le pagine con <meta name="dt-sezione" content="real-estate">:
      foglio di stile, colori negli stili in pagina, marchio "DANOVA REAL ESTATE".
   Idempotente: rilanciare dopo build e post-build.  Uso: python3 seo-tools/real-estate-tema.py"""
import os, re, glob, colorsys
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
HUE = 100 / 360.0   # salvia

def sage(r, g, b):
    if not (b > r + 12 and b >= g): return None          # solo i colori bluastri
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    s2 = min(s * .30, .30) if l > .12 else s * .25        # salvia: poco saturo
    if l < .12: l = l * 1.05
    r2, g2, b2 = colorsys.hls_to_rgb(HUE, l, s2)
    return int(round(r2 * 255)), int(round(g2 * 255)), int(round(b2 * 255))

def ricolora(css):
    def rgba(m):
        r, g, b = int(m.group(2)), int(m.group(3)), int(m.group(4))
        x = sage(r, g, b)
        return m.group(0) if not x else '%s(%d,%d,%d%s' % (m.group(1), x[0], x[1], x[2], m.group(5))
    css = re.sub(r'(rgba?)\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(\s*[,)])', rgba, css)
    def hx(m):
        h = m.group(1)
        if len(h) == 3: h = ''.join(c * 2 for c in h)
        x = sage(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
        return m.group(0) if not x else '#%02x%02x%02x' % x
    return re.sub(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b(?![\w-])', hx, css)

EXTRA = r'''
/* ===== DANOVA REAL ESTATE: aggiunte ===== */
:root{--text:#ecebe4;--muted:#a6a99a;--muted-2:#8a8d7f;--stone:#d9d3c5;--sage:#a9c19f;--sage-d:#6f8a66}
body{background:#080907}
.btn-p{background:linear-gradient(120deg,#d6e2cd,#b4c9a9 55%,#93ad89);color:#10160e}
.btn-p .lbl,.btn-p svg{color:#10160e}
.btn-p::before{background:linear-gradient(120deg,#e7eedf,#b4c9a9)}
.btn-p:hover{box-shadow:0 16px 46px -12px rgba(169,193,159,.75)}
.wordmark i{letter-spacing:.18em}
/* hero con immagine o video di sfondo */
.re-hero{position:relative;min-height:min(86vh,820px);display:flex;align-items:flex-end;padding:120px 0 70px;overflow:hidden}
.re-hero .re-bg{position:absolute;inset:0;z-index:0}
.re-hero .re-bg img,.re-hero .re-bg video{width:100%;height:100%;object-fit:cover;transform:scale(1.06);animation:reKen 22s ease-in-out infinite alternate}
.re-hero::after{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(8,9,7,.35) 0%,rgba(8,9,7,.55) 45%,#080907 100%),radial-gradient(ellipse at 20% 80%,rgba(169,193,159,.18),transparent 60%)}
.re-hero .wrap{position:relative;z-index:2}
.re-hero h1{font-size:clamp(2.3rem,6vw,4.9rem);max-width:17ch}
.re-hero .lead{color:#dcdccf;max-width:62ch}
@keyframes reKen{to{transform:scale(1.14) translate(-1.5%,-1%)}}
.re-badges{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.re-badges span{font-family:"JetBrains Mono",monospace;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;padding:8px 13px;border-radius:99px;border:1px solid rgba(217,211,197,.28);background:rgba(8,9,7,.45);backdrop-filter:blur(8px)}
/* prima / dopo */
.re-ba{position:relative;aspect-ratio:16/9;border-radius:22px;overflow:hidden;border:1px solid rgba(217,211,197,.16);user-select:none;touch-action:pan-y;--p:50%}
.re-ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.re-ba .re-dopo{clip-path:inset(0 0 0 var(--p))}
.re-ba .re-linea{position:absolute;top:0;bottom:0;left:var(--p);width:2px;background:#ecebe4;transform:translateX(-1px);box-shadow:0 0 18px rgba(0,0,0,.5)}
.re-ba .re-linea::after{content:"\2194";position:absolute;top:50%;left:50%;width:46px;height:46px;transform:translate(-50%,-50%);border-radius:50%;background:#ecebe4;color:#10160e;display:grid;place-items:center;font-size:20px;font-weight:700}
.re-ba .re-et{position:absolute;top:16px;font-family:"JetBrains Mono",monospace;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;padding:6px 11px;border-radius:99px;background:rgba(8,9,7,.6);backdrop-filter:blur(6px)}
.re-ba .re-et.p{left:16px}.re-ba .re-et.d{right:16px}
.re-ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.re-ba-grid{display:grid;gap:26px;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr))}
.re-ba-fig{margin:0}.re-ba-fig figcaption{margin-top:12px;font-size:.92rem;color:var(--muted)}
.re-ba-fig figcaption b{color:var(--text)}
/* galleria lavorazioni con effetto 3D */
.re-gal{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));perspective:1200px}
.re-gal figure{margin:0;position:relative;border-radius:20px;overflow:hidden;border:1px solid rgba(217,211,197,.14);transform-style:preserve-3d;transition:transform .6s var(--ease),box-shadow .6s var(--ease);background:#0d0f0c}
.re-gal figure:hover{transform:rotateX(4deg) rotateY(-5deg) translateZ(10px);box-shadow:0 30px 60px -25px rgba(0,0,0,.8),0 0 0 1px rgba(169,193,159,.35)}
.re-gal img,.re-gal video{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;transition:transform 1.2s var(--ease)}
.re-gal figure:hover img{transform:scale(1.06)}
.re-gal figcaption{position:absolute;left:0;right:0;bottom:0;padding:40px 18px 16px;background:linear-gradient(180deg,transparent,rgba(8,9,7,.92));font-size:.9rem;line-height:1.4}
.re-gal figcaption b{display:block;font-family:Sora,sans-serif;font-size:1.02rem;margin-bottom:3px}
.re-gal figcaption span{color:#c9cabd}
.re-nota-img{margin-top:16px;font-size:.8rem;color:var(--muted-2)}
/* striscia video */
.re-video{position:relative;border-radius:24px;overflow:hidden;border:1px solid rgba(217,211,197,.16);aspect-ratio:16/9;background:#0d0f0c}
.re-video video{width:100%;height:100%;object-fit:cover;display:block}
.re-video figcaption{position:absolute;left:20px;bottom:18px;font-family:"JetBrains Mono",monospace;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;padding:7px 12px;border-radius:99px;background:rgba(8,9,7,.6);backdrop-filter:blur(6px)}
.re-split{display:grid;gap:clamp(26px,4vw,56px);grid-template-columns:1.05fr 1fr;align-items:center}
.re-split .pg-testo p{margin-bottom:14px}
@media(max-width:900px){.re-split{grid-template-columns:1fr}.re-hero{min-height:78vh;padding-top:110px}}
/* numeri / promesse */
.re-promesse{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr))}
.re-promesse div{padding:22px;border-radius:18px;border:1px solid rgba(217,211,197,.14);background:linear-gradient(160deg,rgba(169,193,159,.08),rgba(255,255,255,.02))}
.re-promesse b{display:block;font-family:Sora,sans-serif;font-size:1.12rem;margin-bottom:6px}
.re-promesse span{font-size:.92rem;color:var(--muted)}
.dt-bar-call{background:#b4c9a9!important;color:#10160e!important}
.dt-bar-call svg{color:#10160e}
@media(prefers-reduced-motion:reduce){.re-hero .re-bg img,.re-hero .re-bg video{animation:none}.re-gal figure:hover{transform:none}}
'''

def main():
    src = open(os.path.join(R, 'assets/css/site.css'), encoding='utf-8').read()
    css = '/* GENERATO da seo-tools/real-estate-tema.py: non modificare a mano */\n' + ricolora(src) + EXTRA
    open(os.path.join(R, 'assets/css/real-estate.css'), 'w', encoding='utf-8').write(css)
    n = 0
    for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
        if '/seo-tools/' in f or '/_archivio/' in f: continue
        s = open(f, encoding='utf-8').read()
        if 'name="dt-sezione" content="real-estate"' not in s: continue
        s0 = s
        s = re.sub(r'(href="[./]*?/?assets/css/)site\.css(\?[^"]*)?"', r'\1real-estate.css"', s)
        s = re.sub(r'(<style\b[^>]*>)(.*?)(</style>)', lambda m: m.group(1) + ricolora(m.group(2)) + m.group(3), s, flags=re.S)
        s = re.sub(r'(style=")([^"]*)(")', lambda m: m.group(1) + ricolora(m.group(2)) + m.group(3), s)
        s = re.sub(r'<span class="wordmark"><b>DANOVA</b><i>[^<]*</i></span>', '<span class="wordmark"><b>DANOVA</b><i>REAL ESTATE</i></span>', s)
        s = s.replace('<meta name="theme-color" content="#04060c">', '<meta name="theme-color" content="#080907">')
        if s != s0:
            open(f, 'w', encoding='utf-8').write(s); n += 1
    print('real-estate.css generato; pagine con il tema applicato:', n)

if __name__ == '__main__':
    main()
