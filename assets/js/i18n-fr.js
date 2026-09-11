/* Dizionario FR — Danova Tech.
   I testi del sito in questa lingua si modificano qui. */
window.I18N=window.I18N||{};
window.I18N.fr={
  code:'FR', name:'Français', htmlLang:'fr',
  nav:{servizi:'Services',settori:'Pour qui',lavori:'Réalisations',processo:'Méthode',chisiamo:'À propos',faq:'FAQ',contatti:'Contact',cta:'Parlons-en'},
  hero:{
    l1:'Nous construisons', l2:'une technologie qui',
    rot:['convertit.','vend.','fait gagner du temps.','passe à l\'échelle.','simplifie.'],
    sub:'Sites web, référencement, campagnes Meta Ads, applications, ERP et logiciels sur mesure. De la première ligne de code à la première vente : <b>un seul partenaire pour toute votre technologie.</b>',
    cta1:'Demander un devis', cta2:'Voir ce que nous faisons', scroll:'Défiler',
    stats:['Projets livrés','Clients qui renouvellent','Délai moyen de mise en ligne','Support et supervision']
  },
  mq:['Sites web','E-commerce','SEO','Meta Ads','Applications mobiles','ERP','CRM','Automatisations','Landing pages','Logiciels sur mesure','Intégrations IA','Support'],
  servizi:{
    eyebrow:'Services',
    title:'Tout ce qu\'il vous faut <span class="grad">en ligne</span>,<br>construit par une seule équipe.',
    lead:'Fini les prestataires qui se renvoient la balle. Design, développement, référencement et publicité vivent dans le même projet et travaillent pour le même chiffre : votre chiffre d\'affaires.',
    items:[
      {t:'Sites web & E-commerce',p:'Des sites rapides et soignés, construits pour vendre. Pas des modèles recyclés : structure, textes et design partent de votre activité.',
       l:['Sites vitrines, landing pages et one-pagers','Boutiques en ligne avec paiements et livraisons','Réservations, devis en ligne, espaces clients','Performance, Core Web Vitals et accessibilité'],m:'Je veux un site comme ça'},
      {t:'SEO & visibilité',p:'Nous vous rendons trouvable par ceux qui vous cherchent déjà. Recherche, contenus et travail technique pour monter sur Google et y rester.',
       l:['Audit technique et recherche de mots-clés','Référencement local et fiche Google Business','Contenus, blog et stratégie de liens','Rapports mensuels réellement lisibles'],m:'Je veux plus de visibilité'},
      {t:'Meta Ads & campagnes',p:'Des campagnes Facebook et Instagram gérées comme un investissement, pas comme une dépense. Créations, ciblage et optimisation continue.',
       l:['Business Manager, Pixel et API de conversion','Créations vidéo et statiques qui arrêtent le pouce','Entonnoirs d\'acquisition, reciblage et génération de contacts','Tests A/B constants et coût par contact optimisé'],m:'Je veux plus de clients'},
      {t:'Applications sur mesure',p:'Applications web et mobiles construites autour de votre flux de travail. Si vous savez le décrire, nous savons le développer.',
       l:['Applications iOS et Android · Web apps et PWA','Connexion, notifications push, paiements intégrés','Intégration avec les systèmes que vous utilisez déjà','Maintenance et mises à jour incluses'],m:'J\'ai une idée à construire'},
      {t:'ERP & CRM',p:'Fini les tableurs éparpillés et les carnets papier. Un système qui parle la langue de votre entreprise et vous fait gagner des heures chaque semaine.',
       l:['Clients, devis, commandes et factures','Stock, production et échéances','Rôles et droits pour chaque collaborateur','Tableaux de bord et rapports en temps réel'],m:'Je veux organiser mon entreprise'},
      {t:'Logiciels & automatisation',p:'Des programmes sur mesure, des intégrations et des automatisations qui retirent le travail répétitif des mains de vos équipes.',
       l:['Automatisation entre ERP, site et messagerie','Intégrations IA : agents, recherche, analyse de documents','API, synchronisations et import/export de données','Logiciels de bureau et outils internes'],m:'J\'ai un processus à automatiser'}
    ]
  },
  settori:{
    eyebrow:'Pour qui',
    title:'Chaque entreprise mérite<br>son <span class="grad">outil sur mesure.</span>',
    lead:'Nous ne vendons pas de progiciels tout faits. Nous partons de votre façon de travailler et nous construisons l\'outil qui vous manque. Voici quelques exemples concrets.',
    items:[
      ['food','Restaurants & bars','Carte numérique, réservation de tables, commandes à emporter et avis automatisés.'],
      ['shop','Commerces & e-commerce','Boutique en ligne, catalogue synchronisé avec le stock, paiements et livraisons.'],
      ['home','Immobilier','Portail d\'annonces avec recherche avancée, visites virtuelles et traitement automatique des contacts.'],
      ['gym','Salles & studios','Application d\'abonnement, réservation de cours, plans d\'entraînement et renouvellements automatiques.'],
      ['law','Cabinets & professions libérales','Espace client privé, gestion des dossiers, suivi des échéances et signature de documents.'],
      ['tool','Artisans & bâtiment','Générateur de devis, gestion des chantiers, rapports d\'intervention et photos.'],
      ['car','Garages & concessions','Fiches véhicules, prise de rendez-vous, rappels de révision et tarifs en ligne.'],
      ['med','Cabinets médicaux','Agenda de rendez-vous, dossiers numériques, rappels SMS et résultats en ligne.']
    ]
  },
  lavori:{
    eyebrow:'Réalisations', title:'Ce qui sort de <span class="grad">notre atelier.</span>',
    lead:'Une sélection de projets représentatifs du type de travail que nous livrons.',
    filters:['Tout','Sites & E-commerce','Applications','ERP','Ads & SEO'], go:'Voir le projet',
    items:[
      {tag:'E-commerce',t:'Boutique en ligne pour une marque produit',d:'Catalogue, tunnel d\'achat optimisé et intégration avec le stock et les transporteurs. Design sombre, pensé mobile d\'abord.',k:['Ventes en ligne','Temps de chargement']},
      {tag:'ERP',t:'ERP d\'entreprise sur mesure',d:'Clients, affaires, stock et facturation dans un seul panneau, avec des rôles pour chaque service.',k:['Gagné par semaine','Outils remplacés']},
      {tag:'Application mobile',t:'Application de fidélité et de réservation',d:'Application iOS et Android avec cumul de points, notifications push et réservation en temps réel.',k:['Utilisateurs actifs','Clients qui reviennent']},
      {tag:'Meta Ads',t:'Campagne de génération de contacts locale',d:'Entonnoir complet avec créations vidéo, reciblage et traitement automatique des contacts dans le CRM.',k:['Coût par contact','ROAS moyen']},
      {tag:'Site web',t:'Site vitrine pour un cabinet',d:'Présentation des prestations, espace client privé et prise de rendez-vous intégrée.',k:['Demandes de contact','Score de performance']},
      {tag:'SEO',t:'Référencement local multi-sites',d:'Optimisation technique, pages par ville et gestion des fiches Google sur 6 établissements.',k:['Sur 42 mots-clés','Trafic naturel']}
    ]
  },
  processo:{
    eyebrow:'Notre méthode', title:'Une méthode claire,<br>zéro <span class="grad">surprise.</span>',
    lead:'Vous savez toujours où nous en sommes, ce que cela coûte et quand cela arrive. Chaque phase a un livrable concret que vous voyez et validez.',
    items:[
      {t:'Écoute et analyse',p:'Un échange où c\'est vous qui parlez. Nous apprenons l\'activité, les chiffres, qui sont les clients et où fuient le temps ou le chiffre d\'affaires. Tout le reste part de là.',m:['Appel de découverte','Analyse des concurrents','Objectifs mesurables']},
      {t:'Stratégie et devis',p:'Nous présentons ce que nous allons construire, dans quel ordre et à quel prix. Un document clair, sans lignes cachées ni jargon inutile.',m:['Feuille de route','Prix ferme','Délais engagés']},
      {t:'Design et prototype',p:'Avant d\'écrire du code, nous vous montrons à quoi cela ressemble. Un prototype cliquable, révisions comprises : on ne construit que lorsque cela vous plaît vraiment.',m:['Design UI/UX','Prototype cliquable','Révisions incluses']},
      {t:'Développement et tests',p:'Nous construisons par sprints, avec une avancée visible. Tests sur chaque appareil, plus contrôles de performance, de sécurité et de vitesse avant la mise en ligne.',m:['Sprints hebdomadaires','Environnement de préproduction','Contrôle qualité']},
      {t:'Lancement, croissance et support',p:'On publie, on mesure, on améliore. Campagnes, référencement, mises à jour et support : le projet ne se termine pas à la livraison, il y commence.',m:['Mise en ligne accompagnée','Rapports mensuels','Support continu']}
    ]
  },
  numeri:['Projets livrés','Ans de métier','Impressions générées','Livrés dans les délais'],
  numeriSuffix:['+',' ans','M+','%'],
  dicono:{
    eyebrow:'Ce que disent nos clients',
    items:[
      ['Notre site n\'avait pas bougé depuis six ans. En trois semaines ils ont livré quelque chose qui nous ressemble enfin — et qui fait rentrer des demandes tous les jours.','MR','Marco R.','Dirigeant, fabricant de menuiseries'],
      ['Le système qu\'ils ont construit a supprimé trois tableurs et deux carnets papier. Notre stock tombe enfin juste.','SL','Sara L.','Responsable des opérations, distribution'],
      ['Nous avions déjà essayé les campagnes Meta avec d\'autres agences. La différence ici, c\'est qu\'ils expliquent les chiffres au lieu de les cacher derrière des mots.','GF','Giulia F.','Responsable marketing, commerce'],
      ['Nous voulions une application et nous pensions que c\'était hors de portée. Ils ont proposé une version plus petite pour commencer : c\'était le bon choix.','AP','Andrea P.','Fondateur, centre sportif']
    ]
  },
  faq:{
    eyebrow:'Questions fréquentes', title:'Les réponses <span class="grad">dont vous avez besoin.</span>',
    items:[
      ['Combien coûte un projet ?','Cela dépend de ce dont vous avez réellement besoin, et nous le disons franchement : un site vitrine bien construit et un ERP sur mesure ne partent pas du même endroit. Après le premier échange nous envoyons un devis à prix ferme, chaque ligne expliquée. Aucun coût n\'apparaît une fois le travail commencé.'],
      ['En combien de temps sommes-nous en ligne ?','Une landing page ou un site vitrine demande en général 2 à 4 semaines. Une boutique en ligne 4 à 8. Un ERP ou une application se comptent en mois, mais nous travaillons par modules : la première version utilisable arrive bien avant la fin.'],
      ['Travaillez-vous uniquement avec de grandes entreprises ?','C\'est plutôt l\'inverse. La plupart de nos clients sont des commerces, des cabinets et des PME. Notre travail est d\'adapter la solution au budget, pas le contraire.'],
      ['Et si j\'ai déjà un site ou un système ?','Aucun problème. Nous pouvons améliorer l\'existant, l\'intégrer ou le migrer. Nous évaluons d\'abord ce qui vaut la peine d\'être gardé : tout refaire n\'est pas toujours le choix intelligent.'],
      ['Le site est-il à moi ou reste-t-il chez vous ?','Il est à vous. Domaine, hébergement, code et comptes publicitaires sont enregistrés à votre nom. Nous ne retenons rien en otage et vous pouvez emporter le projet quand vous voulez.'],
      ['Que se passe-t-il après la livraison ?','Nous restons. Nous proposons des formules de support avec mises à jour, sauvegardes, supervision et modifications. Et si vous avez choisi le référencement ou les campagnes, le travail continue avec des rapports mensuels clairs.'],
      ['Pouvez-vous vraiment tout construire ?','Presque. Si c\'est du logiciel, très probablement oui : sites, applications, ERP, automatisations, intégrations IA. Quand un projet n\'est pas dans nos cordes, nous le disons tout de suite plutôt que de vous faire perdre du temps.']
    ]
  },
  cta:{
    eyebrow:'On commence', title:'Racontez-nous l\'idée.<br>Nous <span class="grad">nous occupons du reste.</span>',
    lead:'Le premier échange est gratuit et sans engagement. Nous vous dirons honnêtement si nous pouvons aider, ce que cela coûte et combien de temps cela prend. Même si la réponse est « non ».',
    list:['Réponse sous 24 heures ouvrées','Devis clair, à prix ferme','Aucun engagement de durée'],
    wa:'Nous écrire sur WhatsApp',
    f:{nome:'Nom et prénom',tel:'Téléphone',email:'E-mail (facultatif)',azienda:'Entreprise / activité',tipo:'Ce dont vous avez besoin',send:'Envoyer sur WhatsApp',pref:'Indicatif',telerr:'Merci d\'indiquer un numéro de téléphone valide.',emailerr:'Merci d\'indiquer une adresse e-mail valide ou de laisser le champ vide.',
       ok:'C\'est prêt ! WhatsApp s\'ouvre avec votre demande, il ne reste qu\'à l\'envoyer.',
       note:'En envoyant ce formulaire vous acceptez d\'être recontacté. Nous ne transmettons jamais vos données à qui que ce soit.',
       opts:['Site web / e-commerce','SEO et visibilité','Meta Ads et campagnes','Application sur mesure','ERP / CRM','Logiciel ou automatisation','Je ne sais pas encore, parlons-en'],
       subj:'Nouvelle demande depuis le site'}
  },
  footer:{
    tagline:'Une agence tech qui conçoit, développe et fait grandir la présence numérique des entreprises ambitieuses.',
    h1:'Services',h2:'Agence',h3:'Contact',
    c1:['Sites web & E-commerce','SEO','Meta Ads','Applications sur mesure','ERP & CRM','Logiciels et automatisation'],
    c2:['Pour qui nous travaillons','Réalisations','Notre méthode','À propos','FAQ','Contact'],
    legal:'Politique de confidentialité · Cookies · Conditions'
  },
  legal:{
    eyebrow:'Informations légales',
    updated:'Dernière mise à jour : août 2026',
    close:'J\'ai compris',
    nav:['Politique de confidentialité','Cookies','Conditions'],
    docs:{
      privacy:{ t:'Politique de confidentialité', s:[
        ['Responsable du traitement',
         `<p><b>Danova Tech</b> — n° de TVA 05369890263 — siège social Via Rigole 48, 31040 Rigole di Mansuè (TV), Italie.<br>
          E-mail : <a href="mailto:info@danova-tech.com">info@danova-tech.com</a></p>
          <p>Danova Tech est responsable du traitement des données personnelles collectées via ce site, conformément au règlement (UE) 2016/679 (RGPD) et au décret législatif italien 196/2003 modifié par le décret législatif 101/2018. Aucun délégué à la protection des données n'a été désigné, les conditions légales rendant cette désignation obligatoire n'étant pas réunies.</p>`],
        ['Quelles données nous traitons',
         `<p>Nous traitons uniquement les données que vous fournissez volontairement et les données techniques nécessaires au fonctionnement du site.</p>
          <ul>
            <li><b>Données de contact</b> saisies dans le formulaire de la section Contact : nom et prénom, e-mail, entreprise ou activité, type de besoin sélectionné et texte de votre message.</li>
            <li><b>Données de navigation</b> enregistrées automatiquement par le serveur d'hébergement : adresse IP, navigateur et système d'exploitation, date et heure de la requête, pages consultées. Elles sont utilisées sous forme agrégée à des fins de sécurité, de diagnostic et de statistiques de trafic.</li>
          </ul>
          <p>Le site <b>n'utilise aucun cookie de profilage</b> et n'établit aucun profil commercial de ses visiteurs.</p>`],
        ['Comment fonctionne le formulaire de contact',
         `<p>Le formulaire de ce site n'envoie aucune donnée vers un serveur qui nous appartiendrait. À l'envoi, il compose un message dans le programme de messagerie installé sur votre appareil, que vous adressez ensuite à <b>info@danova-tech.com</b>. Vos données transitent donc par votre propre fournisseur de messagerie et arrivent dans notre boîte, où elles sont conservées comme une correspondance professionnelle ordinaire.</p>`],
        ['Finalités et bases légales',
         `<ul>
            <li>Répondre aux demandes d'information et de devis et accomplir des mesures précontractuelles — art. 6.1.b du RGPD.</li>
            <li>Gérer la relation contractuelle et les prestations commandées — art. 6.1.b du RGPD.</li>
            <li>Respecter les obligations fiscales, comptables et légales — art. 6.1.c du RGPD.</li>
            <li>Assurer la sécurité du site et prévenir les abus ou tentatives d'intrusion — intérêt légitime, art. 6.1.f du RGPD.</li>
            <li>Envoyer des communications promotionnelles sur nos services, uniquement avec votre consentement libre et révocable à tout moment — art. 6.1.a du RGPD.</li>
          </ul>`],
        ['Caractère obligatoire ou facultatif des données',
         `<p>La communication des données signalées comme obligatoires dans le formulaire est nécessaire pour que nous puissions répondre : sans elles, nous ne pouvons pas donner suite à votre demande. Toute autre donnée est facultative et n'a aucune incidence sur notre réponse.</p>`],
        ['Destinataires des données',
         `<p>Les données peuvent être traitées par du personnel autorisé et communiquées aux prestataires des services auxquels nous recourons, désignés sous-traitants au sens de l'art. 28 du RGPD lorsque cela s'applique : notre hébergeur, notre fournisseur de messagerie, nos conseils comptables, fiscaux et juridiques, ainsi que les autorités publiques lorsque la loi l'exige.</p>
          <p>Les données ne sont <b>jamais diffusées publiquement, échangées ni vendues</b> à des tiers à des fins commerciales.</p>`],
        ['Transferts hors de l\'Union européenne',
         `<p>Les statistiques de visite sont collectées avec Cloudflare Web Analytics (Cloudflare, Inc.). Comme pour toute requête vers un serveur externe, votre adresse IP est communiquée à Cloudflare afin de délivrer la réponse, sur la base des clauses contractuelles types approuvées par la Commission européenne.</p>
          <p>Nous n'effectuons aucun autre transfert de données personnelles en dehors de l'Espace économique européen.</p>`],
        ['Durées de conservation',
         `<ul>
            <li>Demandes de contact non suivies d'un contrat : <b>24 mois</b> à compter du dernier échange.</li>
            <li>Données relatives aux contrats, factures et documents comptables : <b>10 ans</b>, comme l'exige la loi civile et fiscale italienne.</li>
            <li>Journaux techniques du serveur : <b>12 mois</b> au maximum, sauf nécessité d'enquêter sur des faits illicites.</li>
            <li>Données traitées sur la base du consentement : jusqu'au retrait de ce consentement.</li>
          </ul>`],
        ['Vos droits',
         `<p>Vous pouvez à tout moment exercer les droits prévus aux articles 15 à 22 du RGPD : accès à vos données, rectification, effacement, limitation du traitement, portabilité, opposition au traitement et retrait de tout consentement donné.</p>
          <p>Il suffit d'écrire à <a href="mailto:info@danova-tech.com">info@danova-tech.com</a> : nous répondons dans les 30 jours suivant la réception de la demande. Vous avez également le droit d'introduire une réclamation auprès de l'autorité italienne de protection des données (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">garanteprivacy.it</a>), auprès de la CNIL ou auprès de l'autorité de contrôle de votre pays de résidence.</p>`],
        ['Sécurité des données',
         `<p>Nous appliquons des mesures techniques et organisationnelles appropriées pour protéger les données contre l'accès non autorisé, la perte ou la divulgation : connexions chiffrées HTTPS, boîtes de messagerie protégées par des identifiants robustes et une authentification à deux facteurs, accès limité au personnel strictement nécessaire et sauvegardes régulières.</p>`],
        ['Mineurs',
         `<p>Nos services s'adressent à des professionnels, des entreprises et des organisations. Nous ne collectons pas sciemment de données personnelles concernant des mineurs de moins de 16 ans. Si vous pensez qu'un mineur nous a communiqué des données, écrivez-nous et nous les supprimerons sans délai.</p>`],
        ['Modifications de cette politique',
         `<p>Cette politique peut être mise à jour pour tenir compte d'évolutions législatives ou de nos services. La version en vigueur est toujours celle publiée sur cette page, avec sa date de dernière mise à jour.</p>`]
      ]},
      cookie:{ t:'Politique relative aux cookies', s:[
        ['Ce que sont les cookies',
         `<p>Les cookies sont de petits fichiers texte que les sites déposent sur l'appareil d'un visiteur pour conserver une information : préférences, session de connexion ou, dans le cas des cookies de profilage, comportement de navigation utilisé à des fins publicitaires. Les technologies similaires comprennent les pixels de suivi, le stockage local et l'empreinte numérique du navigateur.</p>`],
        ['Cookies utilisés par ce site',
         `<p>Ce site <b>n'installe aucun cookie de profilage, de mesure d'audience ou de marketing</b> et n'utilise aucun outil qui suit le comportement des visiteurs. Il n'y a ni Google Analytics, ni Pixel Meta, ni technologie équivalente.</p>
          <p>Les visites sont comptées avec <b>Cloudflare Web Analytics</b>, un outil de statistiques agrégées qui ne dépose aucun cookie, ne stocke rien sur votre appareil et n'établit aucun profil : les détails figurent dans la section consacrée aux services tiers.</p>
          <p>Le site ne conserve pas non plus de cookie technique qui lui soit propre : la langue sélectionnée reste active le temps de votre visite uniquement et n'est pas enregistrée. Aucun bandeau de consentement préalable n'est donc nécessaire.</p>`],
        ['Services tiers',
         `<p>Les polices de caractères utilisées sur le site (Sora, Inter, JetBrains Mono) sont <b>hébergées sur ce domaine</b>. Votre navigateur ne contacte aucun serveur externe pour les télécharger : aucune donnée, pas même votre adresse IP, n'est communiquée à Google ni à un autre tiers.</p>
          <p>Si les polices ne se chargent pas, le site utilise les polices du système.</p>
          <p>Les statistiques de visite sont collectées avec <b>Cloudflare Web Analytics</b> (Cloudflare, Inc.). Le script ne dépose aucun cookie et ne stocke rien sur votre appareil : il enregistre, sous forme agrégée, la page consultée, la source du trafic, le type d'appareil et le pays. Comme pour toute requête vers un serveur externe, votre adresse IP est communiquée à Cloudflare afin de délivrer la réponse ; Cloudflare déclare ne pas l'utiliser pour identifier les visiteurs et ne pas la mettre à la disposition du propriétaire du site. Politique de confidentialité : <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">cloudflare.com/privacypolicy</a>. Si vous bloquez le script avec une extension de navigateur, le site continue de fonctionner exactement de la même manière.</p>`],
        ['Liens et contenus externes',
         `<p>Le site contient des liens vers des plateformes tierces (par exemple Instagram et LinkedIn). En suivant ces liens vous accédez à des sites régis par leurs propres politiques en matière de cookies, sur lesquelles nous n'avons aucun contrôle ; nous vous invitons à en prendre connaissance.</p>`],
        ['Gérer les cookies dans votre navigateur',
         `<p>Vous pouvez à tout moment configurer votre navigateur pour bloquer ou supprimer les cookies de n'importe quel site. Les instructions se trouvent dans les préférences de votre navigateur :</p>
          <ul>
            <li><b>Chrome</b> — Paramètres › Confidentialité et sécurité › Cookies et autres données des sites.</li>
            <li><b>Safari</b> — Réglages › Confidentialité › Gérer les données de sites web.</li>
            <li><b>Firefox</b> — Paramètres › Vie privée et sécurité › Cookies et données de sites.</li>
            <li><b>Edge</b> — Paramètres › Cookies et autorisations de site.</li>
          </ul>
          <p>Bloquer les cookies n'empêche en rien la consultation de ce site.</p>`],
        ['Mises à jour',
         `<p>Si nous introduisons à l'avenir des outils de mesure ou de marketing, nous activerons un bandeau de consentement préalable conforme aux lignes directrices applicables et mettrons cette page à jour avant leur mise en service.</p>`]
      ]},
      terms:{ t:'Conditions d\'utilisation', s:[
        ['Objet et éditeur du site',
         `<p>Ce site est édité par <b>Danova Tech</b> — n° de TVA 05369890263 — siège social Via Rigole 48, 31040 Rigole di Mansuè (TV), Italie, e-mail <a href="mailto:info@danova-tech.com">info@danova-tech.com</a>. Les présentes conditions régissent l'accès au site et l'utilisation des contenus qu'il héberge.</p>`],
        ['Acceptation',
         `<p>En naviguant sur le site, vous acceptez ces conditions dans leur intégralité. Si vous n'y adhérez pas, n'utilisez pas le site.</p>`],
        ['Utilisation autorisée',
         `<p>Vous pouvez consulter et utiliser le site à des fins d'information et pour entrer en contact avec nous. Il est interdit d'utiliser le site à des fins illicites ou contraires à la bonne foi, de tenter un accès non autorisé aux systèmes ou aux espaces réservés, de procéder à une extraction automatisée et massive des contenus, d'introduire du code malveillant ou d'accomplir tout acte compromettant le fonctionnement ou la sécurité du site.</p>`],
        ['Propriété intellectuelle',
         `<p>Le code, les éléments graphiques, les textes, les mises en page, les images retravaillées ainsi que la dénomination et le logo <b>Danova Tech</b> appartiennent à Danova Tech ou à ses concédants et sont protégés par le droit d'auteur et le droit des marques. Toute reproduction, modification, distribution ou réutilisation, totale ou partielle, est interdite sans autorisation écrite.</p>
          <p>Les marques, dénominations et logos de tiers éventuellement cités appartiennent à leurs titulaires respectifs et ne sont mentionnés qu'à titre descriptif.</p>`],
        ['Contenus et disponibilité',
         `<p>Les contenus ont une valeur informative et promotionnelle et peuvent être modifiés ou retirés à tout moment sans préavis. Malgré le soin apporté à leur exactitude, nous ne garantissons pas que les informations soient complètes ou constamment à jour.</p>
          <p>Nous nous efforçons de maintenir le site accessible, sans garantir une continuité de service : l'accès peut être suspendu pour maintenance, mise à jour ou pour des raisons indépendantes de notre volonté.</p>`],
        ['Demandes de devis et formation du contrat',
         `<p>Les informations relatives aux prestations, aux délais et aux modalités publiées sur le site sont indicatives et <b>ne constituent pas une offre au public</b> au sens de l'art. 1336 du code civil italien. L'envoi d'une demande via le formulaire ou par e-mail n'engage aucune des parties.</p>
          <p>La relation ne se forme qu'à l'acceptation écrite d'un devis déterminé, qui définit le périmètre, les délais, les honoraires et les conditions de la prestation et prévaut sur tout élément figurant sur le site.</p>`],
        ['Projets, chiffres et exemples',
         `<p>Les cas, exemples et chiffres de performance présentés sur le site se rapportent à des contextes, des marchés et des périodes déterminés. Ils ne constituent ni une promesse ni une garantie de résultats équivalents pour d'autres projets, lesquels dépendent de variables telles que le secteur, le budget, la concurrence et le marché visé.</p>`],
        ['Limitation de responsabilité',
         `<p>Dans les limites permises par la loi, Danova Tech n'est pas responsable des dommages indirects ou consécutifs résultant de l'utilisation ou de l'impossibilité d'utiliser le site, d'interruptions de service ou du contenu de sites tiers liés. Rien dans les présentes conditions ne limite la responsabilité en cas de faute intentionnelle, de faute lourde ou dans les cas où la loi n'autorise pas d'exclusion.</p>`],
        ['Liens vers des sites tiers',
         `<p>Le site peut contenir des liens vers des ressources externes, proposés pour votre commodité. Nous ne contrôlons pas ces sites et ne sommes responsables ni de leur contenu, ni de leurs politiques, ni des services qu'ils proposent.</p>`],
        ['Protection des données personnelles',
         `<p>Le traitement des données personnelles collectées via le site est décrit dans la <b>Politique de confidentialité</b> et dans la <b>Politique relative aux cookies</b>, qui font partie intégrante des présentes conditions.</p>`],
        ['Droit applicable et juridiction',
         `<p>Les présentes conditions sont régies par le droit italien. Pour les litiges avec des utilisateurs ayant la qualité de consommateur, le tribunal du lieu de résidence ou du domicile élu du consommateur est seul compétent. Dans tous les autres cas, le tribunal du lieu d'établissement de l'éditeur du site est compétent.</p>`],
        ['Modification des présentes conditions',
         `<p>Ces conditions peuvent être mises à jour à tout moment. La version applicable est celle publiée sur cette page au moment de l'accès, avec sa date de dernière mise à jour.</p>`]
      ]}
    }
  },
  meta:{title:'Création de sites web, SEO et logiciels sur mesure | Danova Tech',
        desc:'Agence tech italienne : sites web et e-commerce, référencement, campagnes Meta Ads, applications, ERP et logiciels sur mesure. Devis gratuit, réponse sous 24 h.'}
};
