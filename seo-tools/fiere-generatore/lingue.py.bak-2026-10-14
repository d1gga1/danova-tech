# -*- coding: utf-8 -*-
import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
from urllib.parse import quote
import lingue_data1,lingue_data2,lingue_zh,lingue_tr,lingue_ar
D={**lingue_data1.D,**lingue_data2.D,**lingue_zh.D,**lingue_tr.D,**lingue_ar.D}
FIERE=["Vinitaly","Marmomac","Salone del Mobile","EICMA","Host","Cosmoprof","Cersaie","EIMA","Sicam","Samuexpo"]
ALTS={'it':'/servizi/allestimenti-fieristici/',**{l:D[l]['path'] for l in D}}
SUBJ={'en':'Exhibition stand request','de':'Anfrage Messestand','fr':'Demande de stand','es':'Solicitud de stand','zh':'展台询价','tr':'Fuar standı talebi','ar':'طلب جناح معرض'}
for L,d in D.items():
    ct='#contatti-fiera'
    m=hero(d['eyebrow'],d['h1'],d['lead'],d['cta'],ct,d['cta2'],'#metodo')
    m+=cards('cosa',d['c_t'],d['c_l'],d['cards'])
    m+=testo('perche',d['t_t'],None,d['paras'],d['lista'])
    m+=chips('fiere',d['f_t'],d['f_l'],[(p,None) for p in d['places']])
    m+=chips('esperienza',d['e_t'],None,[(f,None) for f in FIERE])
    m+=passi('metodo',d['p_ey'],d['p_t'],None,d['steps'])
    m+=faq(d['faq_ey'],d['faq_t'],d['qa'])
    m+=f'''<section class="pg-cta" id="contatti-fiera">
  <div class="wrap">
    <div class="box" data-rv="up">
      <h2 class="title">{d['k_t']}</h2>
      <p>{d['k_p']}</p>
      <div class="hero-cta fr-ct">
        <a href="mailto:info@danova-tech.com?subject={quote(SUBJ[L])}" class="btn btn-p" data-mag><span class="sheen"></span><span class="lbl">{d['mail']} · <bdi dir="ltr">info@danova-tech.com</bdi></span>
          {ARR}</a>
        <a href="https://wa.me/393884706887" class="btn btn-g" data-mag rel="noopener"><span class="lbl">{d['wa']} <bdi dir="ltr">+39 388 470 6887</bdi></span></a>
      </div>
    </div>
  </div>
</section>
'''
    node=service_node(SITE+d['path'],d['svc_name'],d['svc_name'],d['svc_desc'],
      [{"@type":"Country","name":"Italy"},{"@type":"Place","name":"Europe"}],d['offers'],L)
    print(build(L,d['path'],d['title'],d['desc'],d['ogt'],d['ogd'],d['crumbs'],m,d['qa'],[node],ALTS))
