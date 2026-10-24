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
/* hero a tutta pagina: la foto parte dal bordo superiore, dietro menu e briciole di pane (nessun taglio visibile) */
.re-hero{position:relative;min-height:min(86vh,820px);display:flex;align-items:flex-end;padding:120px 0 70px;overflow:visible;z-index:0}
.re-hero .re-bg{position:absolute;left:0;right:0;bottom:0;top:-420px;z-index:0;overflow:hidden}
.re-hero .re-bg picture{display:contents}
.re-hero .re-bg img,.re-hero .re-bg video{width:100%;height:100%;object-fit:cover;object-position:50% 50%;transform-origin:50% 60%;animation:reKen 26s ease-in-out infinite alternate;will-change:transform}
.re-hero .re-bg::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(180deg,rgba(8,9,7,.9) 0,rgba(8,9,7,.72) 90px,rgba(8,9,7,.5) 240px,rgba(8,9,7,.38) 45%,rgba(8,9,7,.6) 70%,rgba(8,9,7,.92) 90%,#080907 100%),radial-gradient(ellipse at 20% 80%,rgba(169,193,159,.16),transparent 60%)}
main>.pg-crumbs{position:relative;z-index:2}
main>.pg-crumbs a,main>.pg-crumbs{color:#d9d8cc}
.re-hero .wrap{position:relative;z-index:2}
.re-hero h1{font-size:clamp(2.1rem,6vw,4.9rem);max-width:17ch;overflow-wrap:break-word}
.re-hero .lead{color:#dcdccf;max-width:62ch}
@keyframes reKen{from{transform:scale(1)}to{transform:scale(1.06)}}
.re-badges{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.re-badges span{font-family:"JetBrains Mono",monospace;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;padding:8px 13px;border-radius:99px;border:1px solid rgba(217,211,197,.28);background:rgba(8,9,7,.55)}
/* testo della copertina centrato */
.re-hero{align-items:center;text-align:center;padding:110px 0 90px}
.re-hero .wrap{display:flex;flex-direction:column;align-items:center}
.re-hero h1{max-width:20ch;margin-inline:auto}
.re-hero .lead{margin-inline:auto;max-width:64ch}
.re-hero .eyebrow{justify-content:center;text-align:center}
.re-hero .hero-cta{display:flex;flex-wrap:wrap;justify-content:center;gap:12px}
.re-badges{justify-content:center}
/* regole comuni ai media: mai piu' larghi della colonna, foto e video sempre interi in 16:9 */
.re-ba-grid>*,.re-gal>*,.re-split>*{min-width:0}
.re-ba picture,.re-gal picture,.re-video picture,.re-m picture{display:contents}
.re-video img,.re-video video,.re-m img,.re-m video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
/* prima / dopo */
.re-ba{position:relative;aspect-ratio:16/9;border-radius:22px;overflow:hidden;border:1px solid rgba(217,211,197,.16);user-select:none;-webkit-user-select:none;touch-action:pan-y;--p:50%;background:#0d0f0c}
.re-ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.re-ba .re-dopo{clip-path:inset(0 0 0 var(--p))}
.re-ba .re-linea{position:absolute;top:0;bottom:0;left:var(--p);width:2px;background:#ecebe4;transform:translateX(-1px);box-shadow:0 0 18px rgba(0,0,0,.5);pointer-events:none}
.re-ba .re-linea::after{content:"\2194";position:absolute;top:50%;left:50%;width:46px;height:46px;transform:translate(-50%,-50%);border-radius:50%;background:#ecebe4;color:#10160e;display:grid;place-items:center;font-size:20px;font-weight:700;box-shadow:0 6px 20px rgba(0,0,0,.4)}
.re-ba .re-et{position:absolute;top:14px;font-family:"JetBrains Mono",monospace;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;padding:6px 11px;border-radius:99px;background:rgba(8,9,7,.66);pointer-events:none}
.re-ba .re-et.p{left:14px}.re-ba .re-et.d{right:14px}
.re-ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0;-webkit-appearance:none;appearance:none}
.re-ba-grid{display:grid;gap:26px;grid-template-columns:repeat(2,minmax(0,1fr))}
.re-ba-fig{margin:0}
.re-ba-fig figcaption{margin-top:12px;font-size:.92rem;color:var(--muted);line-height:1.5}
.re-ba-fig figcaption b{color:var(--text)}
.re-ba-fig:not(.re-wide) figcaption b::after{content:" \00B7 ";color:var(--muted-2);font-weight:400}
/* elemento dispari: occupa tutta la riga, immagine a sinistra e testo a destra (nessun buco) */
.re-ba-fig.re-wide{grid-column:1/-1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:26px;align-items:center}
.re-ba-fig.re-wide figcaption{margin:0;padding:clamp(22px,3vw,40px);border-radius:22px;border:1px solid rgba(217,211,197,.14);background:linear-gradient(160deg,rgba(169,193,159,.09),rgba(255,255,255,.02));font-size:1.02rem}
.re-ba-fig.re-wide figcaption b{display:block;font-family:Sora,sans-serif;font-size:clamp(1.25rem,2vw,1.6rem);letter-spacing:-.02em;margin-bottom:10px}
.re-ba-fig.re-wide figcaption span{display:block}
.re-video.re-solo{grid-column:1/-1;width:min(100%,820px);justify-self:center}
/* striscia video */
.re-video{position:relative;margin:0;border-radius:22px;overflow:hidden;border:1px solid rgba(217,211,197,.16);aspect-ratio:16/9;background:#0d0f0c}
.re-video figcaption{position:absolute;left:16px;bottom:14px;font-family:"JetBrains Mono",monospace;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;padding:7px 12px;border-radius:99px;background:rgba(8,9,7,.66);max-width:calc(100% - 32px)}
/* galleria lavorazioni: griglia a 6 colonne, ogni riga piena; immagini 16:9 intere, testo sotto */
.re-gal{display:grid;gap:20px;grid-template-columns:repeat(6,minmax(0,1fr))}
.re-gal figure{margin:0;border-radius:20px;overflow:hidden;border:1px solid rgba(217,211,197,.14);background:#0d0f0c;display:flex;flex-direction:column;transition:transform .5s var(--ease),box-shadow .5s var(--ease),border-color .5s}
.re-gal .s2{grid-column:span 2}.re-gal .s3{grid-column:span 3}.re-gal .s6{grid-column:span 6}
.re-gal figure:hover{transform:translateY(-4px);border-color:rgba(169,193,159,.4);box-shadow:0 26px 50px -26px rgba(0,0,0,.85)}
.re-gal .re-m{position:relative;aspect-ratio:16/9;overflow:hidden;background:#0d0f0c}
.re-gal .re-m img{transition:transform 1.2s var(--ease)}
.re-gal figure:hover .re-m img{transform:scale(1.04)}
.re-gal figcaption{padding:16px 18px 18px;font-size:.92rem;line-height:1.45}
.re-gal figcaption b{display:block;font-family:Sora,sans-serif;font-size:1.04rem;margin-bottom:4px}
.re-gal figcaption span{color:#c3c5b8}
.re-nota-img{margin-top:16px;font-size:.8rem;color:var(--muted-2)}
.re-split{display:grid;gap:clamp(26px,4vw,56px);grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);align-items:center}
.re-split .pg-testo{max-width:none}
.re-split .pg-testo p{margin-bottom:14px}
@media(max-width:1000px){.re-gal{grid-template-columns:repeat(2,minmax(0,1fr))}.re-gal .s2,.re-gal .s3,.re-gal .s6{grid-column:auto}.re-gal figure:last-child:nth-child(odd){grid-column:1/-1}}
@media(max-width:900px){.re-split{grid-template-columns:minmax(0,1fr)}.re-hero{min-height:82vh;padding-top:110px}
 .re-ba-grid{grid-template-columns:minmax(0,1fr)}.re-ba-fig.re-wide{grid-template-columns:minmax(0,1fr);gap:12px}
 .re-ba-fig.re-wide figcaption{padding:0;border:0;background:none;font-size:.92rem}.re-ba-fig.re-wide figcaption b{font-size:1.05rem;margin-bottom:4px}}
@media(max-width:640px){.re-gal{grid-template-columns:minmax(0,1fr)}.re-gal figure:last-child:nth-child(odd){grid-column:auto}
 .re-ba{border-radius:16px}.re-video{border-radius:16px}.re-ba .re-linea::after{width:40px;height:40px;font-size:18px}
 .re-hero{min-height:88svh;padding:100px 0 44px}.re-badges span{font-size:.62rem;padding:7px 10px}}
/* footer Real Estate (5 colonne, tutto nella lingua della pagina) */
.f-top.re-foot{grid-template-columns:1.25fr repeat(4,minmax(0,1fr));gap:34px}
.f-top.re-foot ul li{margin-bottom:2px}
.f-top.re-foot .re-h5b{margin-top:22px}
.f-top.re-foot a[aria-current="page"]{color:var(--sage)}
@media(max-width:1100px){.f-top.re-foot{grid-template-columns:repeat(4,minmax(0,1fr))}.f-top.re-foot .fb{grid-column:1/-1}}
@media(max-width:760px){.f-top.re-foot{grid-template-columns:repeat(2,minmax(0,1fr));gap:28px 20px}}
@media(max-width:420px){.f-top.re-foot{grid-template-columns:minmax(0,1fr)}}
.f-legal{flex-wrap:wrap}
/* ancore: il titolo della sezione non finisce sotto l'intestazione fissa */
html{scroll-padding-top:96px}
body .dt-lead .form-note a{color:var(--sage)}#contatti{scroll-margin-top:96px}
/* griglie di card senza buchi: l'ultima riga si allarga e riempie la larghezza */
body .pg-link,body .pg-cards,body .pg-altri{display:flex;flex-wrap:wrap}
body .pg-link>*{flex:1 1 250px;min-width:0}
body .pg-cards>*{flex:1 1 260px;min-width:0}
body .pg-altri>*{flex:1 1 230px;min-width:0}
.f-top.re-foot li{color:var(--muted);font-size:.88rem;line-height:1.55}
.form-note a,.pg-testo a{color:var(--sage)}
/* menu desktop: voci su una riga; le meno importanti si nascondono sugli schermi piu' stretti */
nav.links a{white-space:nowrap}
#hdr .brand{flex-shrink:0;margin-right:18px}#hdr .btn-p .lbl{white-space:nowrap}
@media(max-width:1720px){nav.links a.re-nx{display:none}}
@media(max-width:1200px){nav.links a.re-n2{display:none}}
/* numeri / promesse */
.re-promesse{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr))}
.re-promesse div{padding:22px;border-radius:18px;border:1px solid rgba(217,211,197,.14);background:linear-gradient(160deg,rgba(169,193,159,.08),rgba(255,255,255,.02))}
.re-promesse b{display:block;font-family:Sora,sans-serif;font-size:1.12rem;margin-bottom:6px}
.re-promesse span{font-size:.92rem;color:var(--muted)}
.dt-bar-call{background:#b4c9a9!important;color:#10160e!important}
.dt-bar-call svg{color:#10160e}
@media(prefers-reduced-motion:reduce){.re-hero .re-bg img,.re-hero .re-bg video{animation:none}.re-gal figure:hover{transform:none}.re-gal figure:hover .re-m img{transform:none}}
'''

def main():
    src = open(os.path.join(R, 'assets/css/site.css'), encoding='utf-8').read()
    css = '/* GENERATO da seo-tools/real-estate-tema.py: non modificare a mano */\n' + ricolora(src) + EXTRA
    open(os.path.join(R, 'assets/css/real-estate.css'), 'w', encoding='utf-8').write(css)
    import hashlib; ver = hashlib.md5(css.encode('utf-8')).hexdigest()[:10]   # versione nel link: il browser riscarica lo stile quando cambia
    n = 0
    for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
        if '/seo-tools/' in f or '/_archivio/' in f: continue
        s = open(f, encoding='utf-8').read()
        if 'name="dt-sezione" content="real-estate"' not in s: continue
        s0 = s
        s = re.sub(r'(href="[./]*?/?assets/css/)site\.css(\?[^"]*)?"', r'\1real-estate.css"', s)
        s = re.sub(r'(assets/css/real-estate\.css)(\?v=[0-9a-f]+)?"', r'\1?v=%s"' % ver, s)
        s = re.sub(r'(<style\b[^>]*>)(.*?)(</style>)', lambda m: m.group(1) + ricolora(m.group(2)) + m.group(3), s, flags=re.S)
        s = re.sub(r'(style=")([^"]*)(")', lambda m: m.group(1) + ricolora(m.group(2)) + m.group(3), s)
        s = re.sub(r'<span class="wordmark"><b>DANOVA</b><i>[^<]*</i></span>', '<span class="wordmark"><b>DANOVA</b><i>REAL ESTATE</i></span>', s)
        s = s.replace('<meta name="theme-color" content="#04060c">', '<meta name="theme-color" content="#080907">')
        if s != s0:
            open(f, 'w', encoding='utf-8').write(s); n += 1
    print('real-estate.css generato; pagine con il tema applicato:', n)

if __name__ == '__main__':
    main()
