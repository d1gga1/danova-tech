# -*- coding: utf-8 -*-
"""20/09/2026 — secondo giro: blocco prezzi (schede + offerte nei dati
   strutturati) anche nelle pagine di servizio principali e nelle landing
   per citta'/paese. Riusa patch_block di prezzi-pagine.py; si puo'
   rilanciare: le pagine gia' fatte vengono saltate."""
import os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('pp', os.path.join(HERE, 'prezzi-pagine.py'))
pp = importlib.util.module_from_spec(spec); spec.loader.exec_module(pp)

CITTA_IT = ['padova','pordenone','treviso','udine','veneto','venezia-mestre','verona','vicenza']
PAGES = {
 'it': [('realizzazione-siti-internet',0),('sito-web-aziendale',0),('restyling-sito-web',0)]
       + [('realizzazione-siti-web-'+c,0) for c in CITTA_IT]
       + [('sviluppo-web-app',1),('sviluppo-app-aziendali-veneto',1)]
       + [('software-gestionale-aziendale',2),('gestionale-cloud',2),('crm-aziendale',2),('software-per-pmi',2)]
       + [('gestionali-su-misura-'+c,2) for c in CITTA_IT],
 'en': [('en/web-design-agency-uk',0),('en/web-design-agency-london',0),
        ('en/mobile-app-development-company-uk',1),
        ('en/software-development-company-uk',2),('en/software-development-italy',2)],
 'de': [('de/webagentur-'+c,0) for c in ['deutschland','berlin','frankfurt','hamburg','muenchen',
        'oesterreich','wien','graz','kaernten','schweiz','zuerich','suedtirol']]
       + [('de/individualsoftware-deutschland',2),('de/individualsoftware-oesterreich',2),
          ('de/softwareentwicklung-schweiz',2)],
 'fr': [('fr/agence-web-'+c,0) for c in ['paris','lyon','marseille','bruxelles','geneve']]
       + [('fr/creation-site-internet-france',0),('fr/creation-site-internet-belgique',0),
          ('fr/logiciel-sur-mesure-france',2)],
 'es': [('es/diseno-web-'+c,0) for c in ['espana','madrid','barcelona','valencia','sevilla']]
       + [('es/software-a-medida-espana',2)],
}
if __name__ == '__main__':
    for lang, items in PAGES.items():
        for rel, cat in items:
            print('%-3s  %-45s  %s' % (lang, rel, pp.patch_block(lang, rel, cat)))
