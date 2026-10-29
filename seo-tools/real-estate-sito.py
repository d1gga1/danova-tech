# -*- coding: utf-8 -*-
"""24/10/2026 - Collega la sezione Danova Real Estate al resto del sito (pagine IT):
   1) voce "Real Estate" nel menu desktop e mobile (dopo "Stand fieristici")
   2) link nel footer, colonna Servizi
   3) blocco in homepage (prima di #servizi) con cursore prima/dopo, tra <!--re-home--> e <!--/re-home-->
   Idempotente.  Uso: python3 seo-tools/real-estate-sito.py"""
import os, re, glob
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SKIP = ('_archivio/', 'seo-tools/', 'social/', 'assets/', 'fr/', 'es/', 'zh/', 'zh-hant/', 'ar/', 'tr/')
NAVL = {'it': '/real-estate/', 'en': '/en/real-estate/', 'de': '/de/real-estate/', 'ro': '/ro/real-estate/', 'sq': '/sq/real-estate/', 'hr': '/hr/real-estate/', 'hi': '/hi/real-estate/'}
VIDA = re.compile(r'(<a href="[^"]*" data-nav-video[^>]*>[^<]*</a>)(\s*)')
NAV = re.compile(r'(<a href="/stand-fieristici/"[^>]*>Stand fieristici</a>)(\s*)')
HOME = r'''<!--re-home-->
<section id="real-estate" class="re-home">
<style>
.re-home{padding:clamp(60px,8vw,110px) 0}
.re-home .re-card{position:relative;display:grid;grid-template-columns:1.05fr 1fr;gap:clamp(26px,4vw,60px);align-items:center;padding:clamp(22px,3.4vw,46px);border-radius:28px;
 background:linear-gradient(150deg,#121611 0%,#0b0d0a 60%);border:1px solid rgba(169,193,159,.28);box-shadow:0 40px 90px -40px rgba(0,0,0,.9),inset 0 1px 0 rgba(217,211,197,.08);overflow:hidden}
.re-home .re-card::before{content:"";position:absolute;inset:-40% -10% auto auto;width:60%;height:120%;background:radial-gradient(circle,rgba(169,193,159,.22),transparent 60%);pointer-events:none}
.re-home .re-tag{display:inline-flex;gap:8px;align-items:center;font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#b9cdb0;margin-bottom:18px}
.re-home .re-tag i{width:8px;height:8px;border-radius:50%;background:#a9c19f;box-shadow:0 0 0 4px rgba(169,193,159,.18)}
.re-home h2{font-size:clamp(2rem,4.6vw,3.5rem);color:#ecebe4}
.re-home h2 em{font-style:normal;background:linear-gradient(100deg,#ecebe4,#a9c19f 55%,#d9d3c5);-webkit-background-clip:text;background-clip:text;color:transparent}
.re-home p{color:#b5b8aa;margin-top:18px;max-width:58ch}
.re-home .re-l{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 26px}
.re-home .re-l a{font-size:.86rem;padding:8px 13px;border-radius:99px;border:1px solid rgba(169,193,159,.35);color:#dfe6d8;background:rgba(169,193,159,.06);transition:background .3s,border-color .3s}
.re-home .re-l a:hover{background:rgba(169,193,159,.18);border-color:#a9c19f}
.re-home .re-b{display:inline-flex;align-items:center;gap:10px;padding:14px 26px;border-radius:99px;font-weight:600;background:linear-gradient(120deg,#d6e2cd,#b4c9a9 55%,#93ad89);color:#10160e}
.re-home .re-b2{margin-left:10px;color:#dfe6d8;border-bottom:1px solid rgba(169,193,159,.5)}
.re-home .re-ba picture{display:contents}
.re-home .re-card>*{min-width:0}
.re-home .re-ba{position:relative;aspect-ratio:16/9;border-radius:20px;overflow:hidden;border:1px solid rgba(217,211,197,.18);--p:50%;touch-action:pan-y}
.re-home .re-ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.re-home .re-ba .d{clip-path:inset(0 0 0 var(--p))}
.re-home .re-ba .ln{position:absolute;top:0;bottom:0;left:var(--p);width:2px;background:#ecebe4;transform:translateX(-1px)}
.re-home .re-ba .ln::after{content:"\2194";position:absolute;top:50%;left:50%;width:44px;height:44px;transform:translate(-50%,-50%);border-radius:50%;background:#ecebe4;color:#10160e;display:grid;place-items:center;font-weight:700}
.re-home .re-ba .et{position:absolute;top:14px;font-family:"JetBrains Mono",monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;padding:6px 10px;border-radius:99px;background:rgba(8,9,7,.65);color:#ecebe4}
.re-home .re-ba .et.p{left:14px}.re-home .re-ba .et.q{right:14px}
.re-home .re-ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.re-home small{display:block;margin-top:10px;font-size:.74rem;color:#7f8475}
@media(max-width:900px){.re-home .re-card{grid-template-columns:1fr}.re-home .re-b2{display:inline-block;margin:14px 0 0}}
</style>
  <div class="wrap">
    <div class="re-card" data-rv="up">
      <div>
        <div class="re-tag"><i></i>Novità · Danova Real Estate</div>
        <h2>Ristrutturazioni, general contractor e arredo hotel, <em>chiavi in mano.</em></h2>
        <p>Da oggi ci occupiamo anche di edilizia in Veneto e Friuli: ristrutturazioni di case, bagni, negozi e hotel, facciate e cappotto, pareti divisorie, porte e finiture, arredi contract su misura. Sopralluogo gratuito, prezzo bloccato, tempi nel contratto e un unico referente.</p>
        <div class="re-l">
          <a href="/ristrutturazioni-chiavi-in-mano/">Ristrutturazioni</a><a href="/ristrutturazione-bagno/">Bagni</a><a href="/general-contractor/">General contractor</a>
          <a href="/ristrutturazione-hotel/">Hotel</a><a href="/arredo-hotel-contract/">Arredo hotel</a><a href="/cappotto-termico/">Facciate</a><a href="/impresa-edile-per-architetti/">Per architetti</a>
        </div>
        <a class="re-b" href="/real-estate/">Scopri Danova Real Estate <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a class="re-b2" href="/real-estate/#contatti">Prenota il sopralluogo</a>
      </div>
      <div>
        <div class="re-ba"><picture><source type="image/avif" srcset="/assets/img/re/re-soggiorno-prima-480.avif 480w, /assets/img/re/re-soggiorno-prima-800.avif 800w, /assets/img/re/re-soggiorno-prima-1200.avif 1200w, /assets/img/re/re-soggiorno-prima-1600.avif 1600w, /assets/img/re/re-soggiorno-prima-2000.avif 2000w" sizes="(max-width: 900px) calc(100vw - 90px), 560px"><source type="image/webp" srcset="/assets/img/re/re-soggiorno-prima-480.webp 480w, /assets/img/re/re-soggiorno-prima-800.webp 800w, /assets/img/re/re-soggiorno-prima-1200.webp 1200w, /assets/img/re/re-soggiorno-prima-1600.webp 1600w, /assets/img/re/re-soggiorno-prima-2000.webp 2000w" sizes="(max-width: 900px) calc(100vw - 90px), 560px"><img src="/assets/img/re/re-soggiorno-prima-1200.webp" width="1600" height="900" alt="Prima: appartamento da ristrutturare" loading="lazy" decoding="async"></picture><picture><source type="image/avif" srcset="/assets/img/re/re-soggiorno-nuovo-480.avif 480w, /assets/img/re/re-soggiorno-nuovo-800.avif 800w, /assets/img/re/re-soggiorno-nuovo-1200.avif 1200w, /assets/img/re/re-soggiorno-nuovo-1600.avif 1600w, /assets/img/re/re-soggiorno-nuovo-2000.avif 2000w" sizes="(max-width: 900px) calc(100vw - 90px), 560px"><source type="image/webp" srcset="/assets/img/re/re-soggiorno-nuovo-480.webp 480w, /assets/img/re/re-soggiorno-nuovo-800.webp 800w, /assets/img/re/re-soggiorno-nuovo-1200.webp 1200w, /assets/img/re/re-soggiorno-nuovo-1600.webp 1600w, /assets/img/re/re-soggiorno-nuovo-2000.webp 2000w" sizes="(max-width: 900px) calc(100vw - 90px), 560px"><img class="d" src="/assets/img/re/re-soggiorno-nuovo-1200.webp" width="1600" height="900" alt="Dopo: appartamento ristrutturato in bianco e grigio" loading="lazy" decoding="async"></picture><span class="ln"></span><span class="et p">Prima</span><span class="et q">Dopo</span><input type="range" min="0" max="100" value="50" aria-label="Confronta prima e dopo" oninput="this.parentNode.style.setProperty('--p',this.value+'%')"></div>
        <small>Immagine illustrativa creata con l’intelligenza artificiale.</small>
      </div>
    </div>
  </div>
</section>
<!--/re-home-->
'''
FOOT = '<li><a href="/real-estate/" data-re-foot>Real Estate: ristrutturazioni</a></li>'
nm = nf = 0
for f in glob.glob(os.path.join(R, '**', 'index.html'), recursive=True):
    rel = os.path.relpath(f, R).replace('\\', '/')
    if rel.startswith(SKIP): continue
    s = open(f, encoding='utf-8').read(); s0 = s
    top = rel.split('/')[0]; lang = top if top in NAVL else 'it'
    href = NAVL[lang]
    s = re.sub(r'<a href="[^"]*" data-nav-re[^>]*>Real Estate</a>\s*', '', s)
    cur = ' aria-current="page"' if '/' + rel[:-len('index.html')] == href else ''
    lnk = '<a href="%s" data-nav-re%s>Real Estate</a>' % (href, cur)
    def addnav(b):
        body = b.group(2)
        pat = NAV if 'Stand fieristici</a>' in body else VIDA
        return b.group(1) + pat.sub(lambda m: m.group(1) + m.group(2) + lnk + m.group(2), body, count=1) + b.group(3)
    if rel not in ('index.html', 'en/index.html', 'de/index.html'):
        s = re.sub(r'(<nav (?:class="links"|id="mob")[^>]*>)(.*?)(</nav>)', addnav, s, flags=re.S)
    if lang != 'it':
        if s != s0: open(f, 'w', encoding='utf-8').write(s); nm += 1
        continue
    if 'data-re-foot' not in s:
        s = s.replace('<li><a href="/servizi/allestimenti-fieristici/">Allestimenti fieristici</a></li>',
                      '<li><a href="/servizi/allestimenti-fieristici/">Allestimenti fieristici</a></li>\n        ' + FOOT, 1)
    if rel == 'index.html':
        s = re.sub(r'<!--re-home-->.*?<!--/re-home-->\n?', '', s, flags=re.S)
        s = s.replace('<section id="servizi">', HOME + '<section id="servizi">', 1)
    if s != s0:
        open(f, 'w', encoding='utf-8').write(s); nm += 1
print('pagine aggiornate (menu/footer/home):', nm)
