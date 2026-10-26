# -*- coding: utf-8 -*-
"""26/10/2026 - Danova Real Estate, pagina IT (7): LAVORA CON NOI / DIVENTA PARTNER.
   Cerchiamo artigiani, imprese edili, general contractor, architetti, geometri, ingegneri e fornitori in Veneto e Friuli
   a cui affidare i lavori richiesti dai clienti. Modulo di candidatura dedicato (sezione tipo 'html'): la candidatura arriva
   via email a info@danova-tech.com con DTLead.deliver() (assets/js/contatto.js), con lavorazioni e zone gia' separate,
   pronta da copiare nell'albo partner. Pagina solo in italiano (nessuna traduzione: hreflang solo IT)."""
import importlib.util, os, html as _h
_s = importlib.util.spec_from_file_location('re1', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real-estate-dati-1.py'))
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
G, _G, RE, svc = _m.G, _m._G, _m.RE, _m.svc
PAGINE = []

TIPI = ["Artigiano", "Impresa edile", "General contractor", "Architetto", "Geometra", "Ingegnere", "Interior designer", "Fornitore / produttore"]
LAV = ["Demolizioni e opere murarie", "Intonaci e rasature", "Cartongesso e controsoffitti", "Pittura e decorazioni", "Impianti elettrici",
       "Impianti idraulici e termici", "Climatizzazione e pompe di calore", "Fotovoltaico", "Pavimenti e rivestimenti", "Parquet e resine",
       "Serramenti e finestre", "Porte interne e blindate", "Porte REI e antincendio", "Cappotto termico e facciate", "Tetti e lattoneria",
       "Impermeabilizzazioni", "Falegnameria e mobili su misura", "Fabbro e carpenteria metallica", "Pavimentazioni esterne e giardini",
       "Scavi e movimento terra", "Ponteggi", "Progettazione e render 3D", "Pratiche edilizie (CILA, SCIA, catasto)", "Direzione lavori e sicurezza",
       "Certificazione energetica (APE)", "Arredo hotel e contract", "Pulizie di fine cantiere"]
PROV = ["Treviso", "Venezia", "Padova", "Vicenza", "Verona", "Belluno", "Rovigo", "Pordenone", "Udine", "Gorizia", "Trieste"]
REQ = ["DURC regolare", "Assicurazione RC", "Formazione sicurezza (D.Lgs. 81/2008)", "Patente a crediti", "Attestazione SOA",
       "Abilitazione impianti (DM 37/2008)", "Iscrizione all’albo professionale"]
ADD = ["Solo titolare", "2–5", "6–15", "16–50", "Oltre 50"]

def _chips(name, vals, typ='checkbox'):
    return ''.join('<label class="pt-chip"><input type="%s" name="%s" value="%s"><span>%s</span></label>'
                   % (typ, name, _h.escape(v), _h.escape(v)) for v in vals)
def _fld(name, lab, typ='text', req=True, extra=''):
    return ('<div class="fld"><input type="%s" name="%s" id="pt-%s" placeholder=" "%s%s><label for="pt-%s">%s</label></div>'
            % (typ, name, name, ' required' if req else '', extra, name, lab))

CSS = ('<style id="pt-css">'
 '.pt-form{display:grid;gap:22px;max-width:860px;margin:0 auto;text-align:left}'
 '.pt-form fieldset{border:1px solid var(--line);border-radius:var(--r-md);padding:22px 22px 24px;margin:0;background:var(--panel);display:grid;gap:12px}'
 '.pt-form legend{padding:0 10px;font-weight:700;font-size:15px;color:var(--text)}'
 '.pt-form legend small{font-weight:400;color:var(--muted);margin-left:6px}'
 '.pt-2{display:grid;grid-template-columns:1fr 1fr;gap:12px}'
 '.pt-chips{display:flex;flex-wrap:wrap;gap:8px}'
 '.pt-chip{position:relative;cursor:pointer}'
 '.pt-chip input{position:absolute;opacity:0;width:1px;height:1px}'
 '.pt-chip span{display:inline-block;padding:8px 14px;border:1px solid var(--line-strong);border-radius:999px;font-size:14px;color:var(--text);transition:background .2s,color .2s,border-color .2s;user-select:none}'
 '.pt-chip:hover span{border-color:var(--blue-2)}'
 '.pt-chip input:checked+span{background:var(--blue);border-color:var(--blue);color:#0b1008;font-weight:600}'
 '.pt-chip input:focus-visible+span{outline:2px solid var(--blue-2);outline-offset:2px}'
 '.pt-tutte span{border-style:dashed}'
 '.pt-sel{width:100%;padding:16px 14px;border-radius:var(--r-sm);border:1px solid var(--line);background:var(--panel-2);color:var(--text);font:inherit}'
 '.pt-sel option{color:#111}'
 '.pt-ok{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:var(--muted)}'
 '.pt-ok input{margin-top:3px;accent-color:var(--blue)}'
 '.pt-ok a{color:var(--blue-2)}'
 '.pt-form .btn{justify-content:center;width:100%}.pt-form .btn[disabled]{opacity:.6}'
 '.pt-msg{display:none;margin:0;text-align:center;font-size:15px}.pt-msg.on{display:block}.pt-msg.err{color:#ff8b98}.pt-msg.ok{color:#8fe3b0}'
 '.pt-form .form-note{text-align:center;max-width:none;margin:0;font-size:14px;color:var(--muted)}'
 '.pt-form .form-note a{color:var(--blue-2)}'
 '.dt-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;opacity:0}'
 '#candidatura{scroll-margin-top:100px}'
 '@media (max-width:700px){.pt-2{grid-template-columns:1fr}.pt-form fieldset{padding:18px 14px 20px}}'
 '</style>')

JS = r'''<script>(function(){var f=document.getElementById('pt-form');if(!f)return;
var msg=f.querySelector('.pt-msg'),btn=f.querySelector('button[type=submit]');
function v(n){var e=f.elements[n];return e?String(e.value||'').trim():'';}
function all(n){return [].slice.call(f.querySelectorAll('input[name="'+n+'"]:checked')).map(function(i){return i.value;});}
function show(t,c){msg.textContent=t;msg.className='pt-msg on '+(c||'');}
var tutte=f.querySelector('input[name=tutte]');
if(tutte)tutte.addEventListener('change',function(){[].slice.call(f.querySelectorAll('input[name=prov]')).forEach(function(i){i.checked=tutte.checked;});});
f.addEventListener('submit',function(ev){ev.preventDefault();if(v('_honey'))return;
 var tipo=all('tipo')[0]||'',lav=all('lav'),prov=all('prov'),req=all('req');
 var piva=v('piva').replace(/[\s.]/g,'').replace(/^IT/i,'');
 var err='';
 if(!tipo)err='Indicate che tipo di attività siete.';
 else if(!v('rs'))err='Scrivete la ragione sociale o il nome dell’attività.';
 else if(!v('ref'))err='Scrivete il nome del referente.';
 else if(piva&&!/^\d{11}$/.test(piva))err='La partita IVA, se la indicate, deve avere 11 cifre.';
 else if(!v('sede'))err='Indicate il comune della sede.';
 else if(v('tel').replace(/\D/g,'').length<8)err='Inserite un numero di telefono valido.';
 else if(!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(v('email')))err='Inserite un indirizzo email valido.';
 else if(!lav.length)err='Scegliete almeno una lavorazione.';
 else if(!prov.length)err='Scegliete almeno una provincia in cui lavorate.';
 else if(!f.elements['privacy'].checked)err='Per inviare la candidatura serve il consenso al trattamento dei dati.';
 if(err){show(err,'err');return;}
 var zone=prov.length===11?'Tutto il Veneto e il Friuli Venezia Giulia':prov.join(', ');
 var fields=[['Tipo',tipo],['Ragione sociale',v('rs')],['Referente',v('ref')],['Partita IVA',piva],['Sede',v('sede')],['Telefono',v('tel')],['Email',v('email')],
  ['Sito o social',v('web')],['Addetti',v('addetti')],['Lavorazioni',lav.join(', ')],['Zone',zone],['Requisiti dichiarati',req.join(', ')||'nessuno indicato'],
  ['Presentazione',v('msg')],['Riga per l’albo partner',[v('rs'),tipo,lav.join(' / '),zone,v('ref'),v('tel'),v('email'),piva].join(' | ')]];
 var subj='Candidatura partner Real Estate: '+tipo+' · '+v('rs');
 btn.disabled=true;show('Invio in corso…');
 var p=window.DTLead?window.DTLead.deliver(subj,fields,v('email'),'partner'):new Promise(function(r){
   location.href='mailto:info@danova-tech.com?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(fields.filter(function(x){return x[1];}).map(function(x){return x[0]+': '+x[1];}).join('\n'));r(false);});
 p.then(function(ok){btn.disabled=false;
  if(ok){f.reset();show('Candidatura inviata, grazie! La leggiamo e vi ricontattiamo per conoscerci.','ok');}
  else show('Non siamo riusciti a inviare dal sito: si è aperto il vostro programma di posta con la candidatura già scritta, premete invia.','err');});
});})();</script>'''

ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
FORM = (CSS + '\n    <form class="pt-form" id="pt-form" novalidate data-rv="up">\n'
 '      <fieldset><legend>1. Chi siete</legend><div class="pt-chips" role="radiogroup" aria-label="Tipo di attività">' + _chips('tipo', TIPI, 'radio') + '</div>'
 '<div class="pt-2">' + _fld('rs', 'Ragione sociale o nome attività', extra=' autocomplete="organization"') + _fld('ref', 'Nome e cognome del referente', extra=' autocomplete="name"') + '</div>'
 '<div class="pt-2">' + _fld('piva', 'Partita IVA (facoltativa)', req=False, extra=' inputmode="numeric" maxlength="16"') + _fld('sede', 'Comune della sede (es. Oderzo, TV)', extra=' autocomplete="address-level2"') + '</div>'
 '<div class="pt-2">' + _fld('tel', 'Telefono / WhatsApp', 'tel', extra=' autocomplete="tel" inputmode="tel"') + _fld('email', 'Email', 'email', extra=' autocomplete="email" inputmode="email"') + '</div>'
 '<div class="pt-2">' + _fld('web', 'Sito, Instagram o Facebook (facoltativo)', req=False, extra=' autocomplete="url"')
 + '<select name="addetti" class="pt-sel" aria-label="Numero di addetti"><option value="">Numero di addetti</option>' + ''.join('<option>%s</option>' % a for a in ADD) + '</select></div></fieldset>\n'
 '      <fieldset><legend>2. Lavorazioni <small>scegliete tutte quelle che fate</small></legend><div class="pt-chips">' + _chips('lav', LAV) + '</div></fieldset>\n'
 '      <fieldset><legend>3. Dove lavorate <small>province</small></legend><div class="pt-chips">'
 '<label class="pt-chip pt-tutte"><input type="checkbox" name="tutte" value="1"><span>Tutto Veneto e Friuli</span></label>' + _chips('prov', PROV) + '</div></fieldset>\n'
 '      <fieldset><legend>4. Requisiti <small>quelli che avete già</small></legend><div class="pt-chips">' + _chips('req', REQ) + '</div>'
 '<div class="fld"><textarea name="msg" id="pt-msg" placeholder=" "></textarea><label for="pt-msg">Presentatevi: lavori recenti, specializzazioni, mezzi, disponibilità (facoltativo)</label></div></fieldset>\n'
 '      <input type="text" name="_honey" class="dt-hp" tabindex="-1" autocomplete="off" aria-hidden="true">\n'
 '      <label class="pt-ok"><input type="checkbox" name="privacy" required><span>Acconsento al trattamento dei dati per essere ricontattato e inserito nell’albo partner di Danova Real Estate, come descritto nella <a href="/privacy/">privacy policy</a>.</span></label>\n'
 '      <p class="pt-msg" role="status"></p>\n'
 '      <button type="submit" class="btn btn-p" data-mag><span class="sheen"></span><span class="lbl">Invia la candidatura</span>' + ARR + '</button>\n'
 '      <p class="form-note">Preferite parlarne? Chiamate il <a href="tel:+393884706887">+39 388 470 6887</a> o scriveteci su <a href="https://wa.me/393884706887" target="_blank" rel="noopener">WhatsApp</a>.</p>\n'
 '    </form>\n' + JS + '\n')

PAGINE.append(dict(lang="it", url="/diventa-partner/", hero="re-facciata-cantiere", cta_href="#candidatura", solo_it=True,
 faqtitle=f"Domande {G}frequenti.{_G}", altrititle="Pagine collegate",
 title="Lavora con noi: artigiani, imprese e tecnici in Veneto e Friuli",
 desc="Danova Real Estate cerca artigiani, imprese edili, general contractor, architetti, geometri e ingegneri in Veneto e Friuli a cui affidare i lavori dei clienti.",
 ogtitle="Diventa partner di Danova Real Estate", ogdesc="Artigiani, imprese e tecnici di Veneto e Friuli: entrate nella nostra rete e ricevete lavori nella vostra zona.",
 crumbs=[RE, ("Diventa partner", None)], eyebrow="Lavora con noi · Rete partner",
 heroalt="Squadra al lavoro su un cantiere di facciata con ponteggi",
 h1=f"Artigiani, imprese e tecnici: {G}lavoriamo insieme in Veneto e Friuli.{_G}",
 lead="Privati, hotel, negozi e condomini ci chiedono ristrutturazioni, impianti, facciate e finiture in tutto il Veneto e il Friuli. Cerchiamo artigiani edili, imprese, general contractor, architetti, geometri e ingegneri a cui affidare questi lavori, anche in subappalto, nella loro zona e nella loro specialità.",
 cta1="Invia la candidatura", cta2="Chi cerchiamo",
 badges=["Iscrizione gratuita", "Lavori nella vostra zona", "Un referente di cantiere"],
 sezioni=[
  {"id": "chi-cerchiamo", "tipo": "cards", "eyebrow": "Chi cerchiamo", "h2": f"Professionisti seri, {G}in ogni provincia{_G}",
   "lead": "Ci servono partner per ogni fase del cantiere, dal progetto alla pulizia finale, in tutte le province del Veneto e del Friuli Venezia Giulia.",
   "corpo": [("Artigiani", "Muratori, idraulici, elettricisti, imbianchini, cartongessisti, posatori, serramentisti, fabbri, falegnami e lattonieri, anche titolari senza dipendenti."),
             ("Imprese edili", "Imprese con squadre proprie per ristrutturazioni complete, opere murarie, facciate, cappotti, tetti e impermeabilizzazioni."),
             ("General contractor", "Aziende strutturate per gestire cantieri grandi o più cantieri insieme: condomini, hotel, capannoni, negozi."),
             ("Architetti e interior designer", "Progettisti per rilievi, progetti, render e scelta delle finiture sulle richieste che riceviamo, e per realizzare insieme i vostri progetti."),
             ("Geometri e ingegneri", "Tecnici per pratiche CILA e SCIA, catasto, direzione lavori, sicurezza in cantiere, calcoli strutturali e certificazioni energetiche."),
             ("Fornitori e produttori", "Serramenti, porte, pavimenti, sanitari, arredi su misura e materiali da costruzione, con consegna e posa in zona.")]},
  {"id": "cosa-offriamo", "tipo": "cards", "eyebrow": "Cosa offriamo", "h2": f"Perché lavorare {G}con Danova Real Estate{_G}",
   "corpo": [("Lavori nella vostra zona", "Vi proponiamo incarichi nelle province in cui lavorate e nelle lavorazioni che fate: niente trasferte inutili."),
             ("Lavori già definiti", "Il sopralluogo, le misure, il progetto e il rapporto con il cliente li seguiamo noi: ricevete un lavoro chiaro, con capitolato e materiali decisi."),
             ("Condizioni scritte", "Per ogni incarico prezzo, tempi e modalità di pagamento sono messi per iscritto prima di iniziare."),
             ("Un referente di cantiere", "Una sola persona coordina le squadre, le forniture e le date: sapete sempre quando entrare e cosa trovare."),
             ("Clienti diversi", "Privati, hotel, negozi, uffici, ristoranti, condomini e capannoni in Veneto e Friuli Venezia Giulia."),
             ("Più lavoro a chi lavora bene", "A fine lavoro valutiamo insieme qualità, tempi e pulizia: i partner più affidabili vengono interpellati per primi.")]},
  {"id": "come-funziona", "tipo": "passi", "eyebrow": "Come funziona", "h2": f"Dalla candidatura {G}al primo cantiere{_G}",
   "corpo": [("Inviate la candidatura", "Compilate il modulo qui sotto con lavorazioni, province e requisiti: bastano due minuti."),
             ("Ci conosciamo", "Vi chiamiamo, vediamo insieme lavori fatti, referenze e documenti. Se possibile ci incontriamo in cantiere o in sede."),
             ("Entrate nell’albo partner", "Vi inseriamo nella nostra rete per lavorazione e zona, con i vostri contatti e la vostra disponibilità."),
             ("Vi interpelliamo per ogni lavoro", "Quando un cliente ci chiede una lavorazione nella vostra zona vi contattiamo per il sopralluogo, il preventivo delle vostre voci o direttamente per l’esecuzione."),
             ("Lavoriamo e ci valutiamo", "A fine cantiere facciamo il punto su qualità, tempi e rapporto con il cliente, per lavorare sempre meglio insieme.")]},
  {"id": "requisiti", "tipo": "breve", "eyebrow": "Requisiti", "h2": f"Cosa chiediamo {G}ai nostri partner{_G}",
   "testo": "Lavoriamo solo con imprese, artigiani e professionisti <b>in regola</b>: è una garanzia per i nostri clienti e per voi. Non serve avere già tutto quando vi candidate: segnate nel modulo quello che avete già, il resto lo verifichiamo insieme quando ci conosciamo.",
   "fatti": [("Iscrizione", "Camera di Commercio o albo professionale"), ("DURC", "Regolare e aggiornato"), ("Assicurazione", "RC verso terzi e verso i dipendenti"),
             ("Sicurezza", "Formazione D.Lgs. 81/2008, POS per ogni cantiere"), ("Patente a crediti", "Per i cantieri, quando prevista dalla legge"),
             ("Impianti", "Abilitazione DM 37/2008 e dichiarazioni di conformità"), ("Tecnici", "Iscrizione all’albo professionale"), ("Zona", "Veneto e Friuli Venezia Giulia")]},
  {"id": "candidatura", "tipo": "html", "eyebrow": "Candidatura", "h2": f"Entrate nella {G}rete partner{_G}",
   "lead": "Compilate il modulo: la candidatura arriva direttamente al nostro ufficio tecnico. Iscrizione gratuita e senza impegno.",
   "html": FORM}],
 faq=[("Quanto costa entrare nella rete partner?", "Nulla. L’iscrizione è gratuita e non vi impegna ad accettare i lavori che vi proponiamo."),
      ("Sono un artigiano senza dipendenti: posso candidarmi?", "Sì. Molte lavorazioni, come impianti, tinteggiature, posa di pavimenti o montaggio porte, sono affidate proprio ad artigiani singoli o a piccole squadre."),
      ("Ci garantite un numero minimo di lavori?", "No, e diffidate di chi lo promette. Vi interpelliamo quando arriva una richiesta nella vostra lavorazione e nella vostra zona; chi lavora bene viene chiamato più spesso."),
      ("Affidate lavori in subappalto?", "Sì: a seconda dell’incarico affidiamo ai partner singole lavorazioni in subappalto o li coinvolgiamo direttamente con il cliente. In ogni caso le condizioni sono scritte prima di iniziare, con documenti di sicurezza e regolarità contributiva in ordine."),
      ("Sono un operaio senza partita IVA: posso candidarmi?", "Sì. Lasciate vuota la partita IVA e scrivete nel messaggio la vostra specialità e la vostra esperienza: vi ricontattiamo se c’è un’opportunità adatta, anche presso le squadre dei nostri partner."),
      ("Come vengono definiti prezzi e pagamenti?", "Per ogni incarico concordiamo per iscritto, prima di iniziare, il prezzo delle vostre lavorazioni, i tempi e le modalità di pagamento."),
      ("Sono un architetto o un geometra: come collaboriamo?", "In due modi: vi coinvolgiamo per progetti, pratiche, direzione lavori e sicurezza sulle richieste che riceviamo, e realizziamo noi i vostri progetti con le nostre squadre, come descritto nella pagina Impresa edile per architetti."),
      ("Lavorate solo in Veneto e Friuli?", "Sì: province di Treviso, Venezia, Padova, Vicenza, Verona, Belluno, Rovigo, Pordenone, Udine, Gorizia e Trieste. La sede è a Mansuè, in provincia di Treviso."),
      ("In che lingua possiamo parlare?", "Italiano, inglese e rumeno, a voce e per scritto.")],
 ctabox={"h2": "Pronti a lavorare insieme?", "p": "Compilate la candidatura: vi ricontattiamo per conoscerci.", "btn": "Invia la candidatura"},
 altri=[("Danova Real Estate", "/real-estate/"), ("General contractor", "/general-contractor/"), ("Impresa edile per architetti", "/impresa-edile-per-architetti/"),
        ("Ristrutturazioni chiavi in mano", "/ristrutturazioni-chiavi-in-mano/"), ("Pratiche edilizie CILA e SCIA", "/pratiche-edilizie-cila-scia/"), ("Cartongesso e controsoffitti", "/cartongesso-e-controsoffitti/")],
 svc=svc("Rete partner Danova Real Estate", "Collaborazione con artigiani, imprese e tecnici",
         "Danova Real Estate seleziona artigiani, imprese edili, general contractor, architetti, geometri, ingegneri e fornitori in Veneto e Friuli Venezia Giulia a cui affidare i lavori di ristrutturazione richiesti dai clienti.", [])))
