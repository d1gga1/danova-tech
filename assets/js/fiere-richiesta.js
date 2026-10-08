/* Modulo "Richiedi lo stand" delle pagine fiere: prepara il messaggio su WhatsApp (o email). Danova Tech, ottobre 2026 */
(function(){
  var WA='393884706887', MAIL='info@danova-tech.com';
  function val(f,n){var e=f.elements[n];return e?String(e.value||'').trim():'';}
  function testo(f){
    var r=['Richiesta stand dal sito danova-tech.com','','Fiera: '+val(f,'fiera')];
    if(val(f,'mq')) r.push('Metri quadri: '+val(f,'mq'));
    if(val(f,'spazio')) r.push('Tipo di spazio: '+val(f,'spazio'));
    r.push('Nome: '+val(f,'nome'),'Azienda: '+val(f,'azienda'),'Telefono: '+val(f,'tel'));
    if(val(f,'email')) r.push('Email: '+val(f,'email'));
    if(val(f,'note')) r.push('','Note: '+val(f,'note'));
    r.push('','Pagina: '+location.href.split('#')[0]);
    return r.join('\n');
  }
  function aggiornaMail(f){
    var a=f.querySelector('.fr-req-mail'); if(!a) return;
    a.href='mailto:'+MAIL+'?subject='+encodeURIComponent('Richiesta stand: '+(val(f,'fiera')||'fiera'))+'&body='+encodeURIComponent(testo(f));
  }
  function errore(f,msg,el){
    var p=f.querySelector('.fr-req-err'); if(p){p.textContent=msg;p.classList.add('on');}
    if(el){el.classList.add('bad');el.focus();}
  }
  document.querySelectorAll('form.fr-req').forEach(function(f){
    f.addEventListener('input',function(e){if(e.target.classList)e.target.classList.remove('bad');var p=f.querySelector('.fr-req-err');if(p)p.classList.remove('on');aggiornaMail(f);});
    aggiornaMail(f);
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var req=[['fiera','Indica la fiera a cui partecipi.'],['nome','Inserisci nome e cognome.'],['azienda',"Inserisci il nome dell'azienda."],['tel','Inserisci un numero di telefono.']];
      for(var i=0;i<req.length;i++){ if(!val(f,req[i][0])) return errore(f,req[i][1],f.elements[req[i][0]]); }
      if(val(f,'tel').replace(/\D/g,'').length<6) return errore(f,'Il numero di telefono sembra incompleto.',f.elements.tel);
      var em=val(f,'email'); if(em && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)) return errore(f,"L'email non sembra valida: correggila o lascia il campo vuoto.",f.elements.email);
      try{ if(window.gtag) gtag('event','generate_lead',{form:'richiesta_stand',fiera:val(f,'fiera')}); }catch(_){}
      window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(testo(f)),'_blank','noopener');
      var p=f.querySelector('.fr-req-err'); if(p){p.textContent='Perfetto: si è aperto WhatsApp con la richiesta pronta, premi invio per mandarcela.';p.classList.add('on','ok');}
    });
  });
  /* pulsanti "Richiedi lo stand" (calendario e schede): compilano il modulo e ci portano li' */
  function compila(nome){
    var f=document.querySelector('form.fr-req'); if(!f) return false;
    f.elements.fiera.value=nome; aggiornaMail(f);
    var sec=f.closest('section')||f; sec.scrollIntoView({behavior:'smooth',block:'start'});
    setTimeout(function(){ (f.elements.mq||f.elements.nome).focus({preventScroll:true}); },600);
    return true;
  }
  window.frRichiedi=compila;
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('[data-req]'); if(!b) return;
    if(compila(b.getAttribute('data-req'))) e.preventDefault();
  });
  try{ var q=new URLSearchParams(location.search).get('fiera'); if(q){ var f=document.querySelector('form.fr-req'); if(f&&!f.elements.fiera.value){f.elements.fiera.value=q.slice(0,120);aggiornaMail(f);} } }catch(_){}
})();
