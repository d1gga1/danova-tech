/* Dizionario EN — Danova Tech.
   I testi del sito in questa lingua si modificano qui. */
window.I18N=window.I18N||{};
window.I18N.en={
  code:'EN', name:'English', htmlLang:'en',
  nav:{servizi:'Services',settori:'Who we serve',lavori:'Work',processo:'Process',chisiamo:'About us',faq:'FAQ',contatti:'Contact',cta:"Let's talk"},
  hero:{
    l1:'We build', l2:'technology that',
    rot:['converts.','sells.','saves time.','scales.','simplifies.'],
    sub:'Websites, SEO, Meta Ads campaigns, applications, management systems and custom software. From the first line of code to the first sale: <b>one partner for your entire technology stack.</b>',
    cta1:'Request a quote', cta2:'See what we do', scroll:'Scroll',
    stats:['Projects delivered','Clients who renew','Average launch time','Support and monitoring']
  },
  mq:['Websites','E-commerce','SEO','Meta Ads','Mobile apps','ERP systems','CRM','Automations','Landing pages','Custom software','AI integrations','Support'],
  servizi:{
    eyebrow:'Services',
    title:'Everything you need <span class="grad">online</span>,<br>built by one team.',
    lead:'No more vendors pointing fingers at each other. Design, development, search and advertising live inside the same project and work toward the same number: your revenue.',
    items:[
      {t:'Websites & E-commerce',p:'Fast, polished sites built to sell. Not recycled templates: structure, copy and design shaped around your business.',
       l:['Brochure sites, landing pages and one-pagers','E-commerce with payments and shipping','Bookings, quote builders, member areas','Performance, Core Web Vitals and accessibility'],m:'I want a site like this'},
      {t:'SEO & search visibility',p:'We make you findable by people already looking for you. Research, content and technical work to climb Google and stay there.',
       l:['Technical audit and keyword research','Local SEO and Google Business Profile','Content, blog and link strategy','Monthly reports you can actually read'],m:'I want more visibility'},
      {t:'Meta Ads & campaigns',p:'Facebook and Instagram campaigns run as an investment, not an expense. Creative, targeting and continuous optimisation.',
       l:['Business Manager, Pixel and Conversions API setup','Video and static creative built to stop the scroll','Acquisition funnels, retargeting and lead generation','Constant A/B testing and cost-per-lead optimisation'],m:'I want more customers'},
      {t:'Custom apps',p:'Web and mobile applications built around your workflow. If you can describe it, we can develop it.',
       l:['iOS and Android apps · Web apps and PWAs','Login, push notifications, in-app payments','Integration with the systems you already use','Maintenance and updates included'],m:'I have an idea to build'},
      {t:'ERP & CRM systems',p:'No more scattered spreadsheets and paper notebooks. A system that speaks your company\'s language and saves you hours every week.',
       l:['Clients, quotes, orders and invoices','Inventory, production and deadlines','Roles and permissions for every team member','Real-time dashboards and reports'],m:'I want to organise my company'},
      {t:'Software & automation',p:'Custom programs, integrations and automations that take repetitive work off your team\'s hands.',
       l:['Automation between your system, site and email','AI integrations: chatbots, search, document analysis','APIs, syncing and data import/export','Desktop software and internal tools'],m:'I have a process to automate'}
    ]
  },
  settori:{
    eyebrow:'Who we serve',
    title:'Every business deserves<br>its own <span class="grad">custom tool.</span>',
    lead:'We don\'t sell off-the-shelf packages. We start from how you actually work and build the tool you\'re missing. Here are a few concrete examples of what we can create.',
    items:[
      ['food','Restaurants & bars','Digital menu, table booking, takeaway orders and automated reviews.'],
      ['shop','Shops & e-commerce','Online storefront, catalogue synced with inventory, payments and shipping.'],
      ['home','Real estate','Listings portal with advanced search, virtual tours and automated lead handling.'],
      ['gym','Gyms & studios','Membership app, class booking, training plans and automatic renewals.'],
      ['law','Professional firms','Private client area, case management, deadline tracking and document signing.'],
      ['tool','Trades & construction','Quote builder, site and job management, work reports and photo logs.'],
      ['car','Garages & dealerships','Vehicle records, service booking, inspection reminders and online pricing.'],
      ['med','Medical practices','Appointment scheduling, digital records, SMS reminders and online results.']
    ]
  },
  lavori:{
    eyebrow:'Selected work', title:'What comes out of <span class="grad">our studio.</span>',
    lead:'A selection of projects representative of the kind of work we deliver.',
    filters:['All','Sites & E-commerce','Apps','ERP','Ads & SEO'], go:'View project',
    items:[
      {tag:'E-commerce',t:'Online shop for a product brand',d:'Catalogue, optimised checkout and integration with inventory and couriers. Dark, mobile-first design.',k:['Online sales','Load time']},
      {tag:'ERP',t:'Custom company management system',d:'Clients, jobs, inventory and invoicing in a single panel, with roles for every department.',k:['Saved per week','Tools replaced']},
      {tag:'Mobile app',t:'Loyalty and booking app',d:'iOS and Android app with points collection, push notifications and real-time service booking.',k:['Active users','Returning customers']},
      {tag:'Meta Ads',t:'Local lead generation campaign',d:'Full funnel with video creative, retargeting and automated contact handling in the CRM.',k:['Cost per lead','Average ROAS']},
      {tag:'Website',t:'Brochure site for a professional firm',d:'Service presentation, private client area and integrated consultation booking.',k:['Contact requests','Performance score']},
      {tag:'SEO',t:'Multi-location local search',d:'Technical optimisation, city landing pages and Google profile management across 6 locations.',k:['On 42 keywords','Organic traffic']}
    ]
  },
  processo:{
    eyebrow:'How we work', title:'A clear method,<br>zero <span class="grad">surprises.</span>',
    lead:'You always know where we are, what it costs and when it lands. Every phase has a concrete deliverable you can see and approve.',
    items:[
      {t:'Listening and analysis',p:'A call where you do the talking. We learn the business, the numbers, who the customers are and where time or revenue leaks. Everything else grows from here.',m:['Discovery call','Competitor analysis','Measurable goals']},
      {t:'Strategy and quote',p:'We present what we\'ll build, in what order and at what cost. A clear document, no hidden line items and no unnecessary jargon.',m:['Roadmap','Fixed price','Firm timeline']},
      {t:'Design and prototype',p:'Before writing code we show you what it looks like. A clickable prototype with revisions included: we only start building when you actually like it.',m:['UI/UX design','Clickable prototype','Revisions included']},
      {t:'Development and testing',p:'We build in sprints with visible progress. Testing on every device, plus performance, security and speed checks before going live.',m:['Weekly sprints','Staging environment','Quality assurance']},
      {t:'Launch, growth and support',p:'We go live, measure and improve. Campaigns, SEO, updates and support: the project doesn\'t end at delivery, it starts there.',m:['Assisted go-live','Monthly reports','Ongoing support']}
    ]
  },
  numeri:['Projects delivered','Years in the field','Impressions generated','Delivered on schedule'],
  numeriSuffix:['+',' yrs','M+','%'],
  dicono:{
    eyebrow:'What clients say',
    items:[
      ['Our site had been frozen for six years. In three weeks they delivered something that finally looks like us — and that brings in enquiries every day.','MR','Marco R.','Owner, window manufacturer'],
      ['The system they built removed three spreadsheets and two paper notebooks. Our inventory finally adds up.','SL','Sara L.','Operations manager, distribution'],
      ['We had tried Meta campaigns with other agencies. The difference here is that they explain the numbers instead of hiding them behind words.','GF','Giulia F.','Marketing manager, retail'],
      ['We wanted an app and assumed it was out of reach. They proposed a smaller version to start from: it was the right call.','AP','Andrea P.','Founder, sports centre']
    ]
  },
  faq:{
    eyebrow:'Frequently asked', title:'The answers <span class="grad">you need.</span>',
    items:[
      ['How much does a project cost?','It depends on what you actually need, and we\'ll say it plainly: a well-built brochure site starts from a very different figure than a custom management system. After the first call we send a fixed-price quote with every line explained. No cost appears once work has started.'],
      ['How long until we go live?','A landing page or brochure site usually takes 2–4 weeks. An e-commerce site 4–8. A custom system or app is measured in months, but we work in modules: the first usable version arrives well before the end.'],
      ['Do you only work with large companies?','Quite the opposite. Most of our clients are local businesses, professional firms and small companies. Our job is to size the solution to the budget, not the other way around.'],
      ['What if I already have a site or system?','Not a problem. We can improve what\'s there, integrate it or migrate it. First we assess what\'s worth keeping: rebuilding everything isn\'t always the smart move.'],
      ['Is the site mine or does it stay yours?','It\'s yours. Domain, hosting, code and ad accounts are registered in your name. We hold nothing hostage and you can take the project elsewhere whenever you want.'],
      ['What happens after delivery?','We stay. We offer support plans with updates, backups, monitoring and changes. And if you chose SEO or campaigns, the work continues with clear monthly reports.'],
      ['Can you really build anything?','Almost. If it\'s software, most likely yes: sites, apps, management systems, automations, AI integrations. When a project isn\'t in our wheelhouse we say so straight away rather than wasting your time.']
    ]
  },
  cta:{
    eyebrow:'Get started', title:'Tell us the idea.<br>We\'ll <span class="grad">handle the rest.</span>',
    lead:'First call is free and with no obligation. We\'ll tell you honestly whether we can help, what it costs and how long it takes. Even if the answer is "no".',
    list:['Reply within 24 business hours','Clear, fixed-price quote','No lock-in contracts'],
    wa:'Message us on WhatsApp',
    f:{nome:'Full name',tel:'Phone',email:'Email (optional)',azienda:'Company / business',tipo:'What do you need',send:'Send on WhatsApp',pref:'Code',telerr:'Please enter a valid phone number.',emailerr:'Please enter a valid email address or leave the field empty.',
       ok:'All set! WhatsApp opens with your request ready to go — just hit send.',
       note:'By submitting you agree to be contacted. We never share your data with anyone.',
       opts:['Website / e-commerce','SEO and search visibility','Meta Ads and campaigns','Custom app','ERP / CRM system','Software or automation','Not sure yet, let\'s talk'],
       subj:'New enquiry from the website'}
  },
  footer:{
    tagline:'A tech agency that designs, builds and grows the digital presence of ambitious businesses.',
    h1:'Services',h2:'Agency',h3:'Contact',
    c1:['Websites & E-commerce','SEO','Meta Ads','Custom apps','ERP & CRM','Software and automation'],
    c2:['Who we serve','Selected work','Our method','About us','FAQ','Contact'],
    legal:'Privacy Policy · Cookie Policy · Terms'
  },
  legal:{
    eyebrow:'Legal information',
    updated:'Last updated: August 2026',
    close:'Got it',
    nav:['Privacy Policy','Cookie Policy','Terms'],
    docs:{
      privacy:{ t:'Privacy Policy', s:[
        ['Data controller',
         `<p><b>Danova Tech</b> — VAT no. 05369890263 — registered office at Via Rigole 48, 31040 Rigole di Mansuè (TV), Italy.<br>
          Email: <a href="mailto:info@danova-tech.com">info@danova-tech.com</a></p>
          <p>Danova Tech is the controller of the personal data collected through this website, pursuant to Regulation (EU) 2016/679 (GDPR) and Italian Legislative Decree 196/2003 as amended by Legislative Decree 101/2018. No Data Protection Officer has been appointed, as the legal conditions requiring one do not apply.</p>`],
        ['What data we process',
         `<p>We process only the data you provide voluntarily and the technical data required for the website to work.</p>
          <ul>
            <li><b>Contact data</b> entered in the form in the Contact section: full name, email, company or business, the type of need selected and the text of your message.</li>
            <li><b>Browsing data</b> recorded automatically by the hosting server: IP address, browser and operating system, date and time of the request, pages visited. These are used in aggregate form for security, diagnostics and traffic statistics.</li>
          </ul>
          <p>The site <b>does not use profiling cookies</b> and does not build commercial profiles of its visitors.</p>`],
        ['How the contact form works',
         `<p>The form on this site does not send data to a server of ours. On submission it composes a message in the email programme installed on your device, which you then send to <b>info@danova-tech.com</b>. Your data therefore travels through your own email provider and reaches our mailbox, where it is kept as ordinary business correspondence.</p>`],
        ['Purposes and legal bases',
         `<ul>
            <li>Replying to information and quotation requests and taking pre-contractual steps — Art. 6(1)(b) GDPR.</li>
            <li>Managing the contractual relationship and the services commissioned — Art. 6(1)(b) GDPR.</li>
            <li>Complying with tax, accounting and other legal obligations — Art. 6(1)(c) GDPR.</li>
            <li>Keeping the website secure and preventing abuse or intrusion attempts — legitimate interest, Art. 6(1)(f) GDPR.</li>
            <li>Sending promotional communications about our services, only with your freely given consent, revocable at any time — Art. 6(1)(a) GDPR.</li>
          </ul>`],
        ['Whether providing data is mandatory',
         `<p>Providing the data marked as required in the form is necessary for us to reply: without it we cannot follow up on your request. Providing any other data is optional and does not affect our reply.</p>`],
        ['Who we share data with',
         `<p>Data may be handled by authorised staff and shared with the providers of services we rely on, appointed as processors under Art. 28 GDPR where applicable: our website hosting provider, our email service provider, accounting, tax and legal advisors, and public authorities where the law requires it.</p>
          <p>Data is <b>never disclosed publicly, traded or sold</b> to third parties for commercial purposes.</p>`],
        ['Transfers outside the European Union',
         `<p>The site loads its typefaces from Google servers (Google Fonts). This means your IP address is communicated to Google LLC, based in the United States, on the basis of the standard contractual clauses approved by the European Commission and Google's adherence to the EU–U.S. Data Privacy Framework.</p>
          <p>We carry out no other transfers of personal data outside the European Economic Area.</p>`],
        ['How long we keep data',
         `<ul>
            <li>Contact requests not followed by a contract: <b>24 months</b> from the last exchange.</li>
            <li>Data relating to contracts, invoices and accounting records: <b>10 years</b>, as required by Italian civil and tax law.</li>
            <li>Technical server logs: <b>12 months</b> at most, unless needed to investigate unlawful acts.</li>
            <li>Data processed on the basis of consent: until that consent is withdrawn.</li>
          </ul>`],
        ['Your rights',
         `<p>You may at any time exercise the rights set out in Articles 15–22 GDPR: access to your data, rectification, erasure, restriction of processing, portability, objection to processing and withdrawal of any consent given.</p>
          <p>To do so, simply write to <a href="mailto:info@danova-tech.com">info@danova-tech.com</a>: we reply within 30 days of receiving the request. You also have the right to lodge a complaint with the Italian Data Protection Authority (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">garanteprivacy.it</a>) or with the supervisory authority of your country of residence.</p>`],
        ['Data security',
         `<p>We apply appropriate technical and organisational measures to protect data against unauthorised access, loss or disclosure: encrypted HTTPS connections, mailboxes protected by strong credentials and two-factor authentication, access limited to strictly necessary personnel, and regular backups.</p>`],
        ['Minors',
         `<p>Our services are aimed at professionals, companies and organisations. We do not knowingly collect personal data from children under 16. If you believe a minor has provided us with data, please write to us and we will delete it without delay.</p>`],
        ['Changes to this notice',
         `<p>This notice may be updated to reflect changes in the law or in our services. The version in force is always the one published on this page, with its last-updated date.</p>`]
      ]},
      cookie:{ t:'Cookie Policy', s:[
        ['What cookies are',
         `<p>Cookies are small text files that websites store on a visitor's device to hold information: preferences, login sessions or, in the case of profiling cookies, browsing behaviour used for advertising. Similar technologies include tracking pixels, local storage and browser fingerprinting.</p>`],
        ['Cookies used by this site',
         `<p>This website <b>installs no profiling, analytics or marketing cookies</b> and uses no tools that track visitor behaviour. There is no Google Analytics, Meta Pixel or equivalent technology.</p>
          <p>Visits are counted with <b>Cloudflare Web Analytics</b>, an aggregate statistics tool that sets no cookies, stores nothing on your device and builds no profiles: details are in the third-party services section.</p>
          <p>The site does not even store technical cookies of its own on your device: the language you select stays active for the duration of your visit only and is not saved. For this reason no prior consent banner is required.</p>`],
        ['Third-party services',
         `<p>The typefaces used on the site (Sora, Inter, JetBrains Mono) are <b>hosted on this domain</b>. Your browser contacts no external server to download them: no data, not even your IP address, is shared with Google or any other third party.</p>
          <p>If the fonts fail to load, the site falls back to system typefaces.</p>
          <p>Visit statistics are collected with <b>Cloudflare Web Analytics</b> (Cloudflare, Inc.). The script sets no cookies and stores nothing on your device: it records, in aggregate form, the page visited, the traffic source, the device type and the country. As with any request to an external server, your IP address is communicated to Cloudflare in order to deliver the response; Cloudflare states that it does not use it to identify visitors and does not make it available to the site owner. Privacy notice: <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">cloudflare.com/privacypolicy</a>. If you block the script with a browser extension, the site keeps working exactly the same.</p>`],
        ['External links and content',
         `<p>The site contains links to third-party platforms (for example Instagram and LinkedIn). Following those links takes you to sites governed by their own cookie policies, over which we have no control; we encourage you to read them.</p>`],
        ['Managing cookies in your browser',
         `<p>You can still set your browser to block or delete cookies from any site. The instructions are in your browser's preferences:</p>
          <ul>
            <li><b>Chrome</b> — Settings › Privacy and security › Cookies and other site data.</li>
            <li><b>Safari</b> — Settings › Privacy › Manage website data.</li>
            <li><b>Firefox</b> — Settings › Privacy & Security › Cookies and Site Data.</li>
            <li><b>Edge</b> — Settings › Cookies and site permissions.</li>
          </ul>
          <p>Blocking cookies does not affect your ability to browse this site.</p>`],
        ['Updates',
         `<p>If we introduce measurement or marketing tools in future, we will activate a prior consent banner in line with the Italian Data Protection Authority's guidelines and update this page before those tools go live.</p>`]
      ]},
      terms:{ t:'Terms of use', s:[
        ['Subject and site owner',
         `<p>This website is operated by <b>Danova Tech</b> — VAT no. 05369890263 — registered office at Via Rigole 48, 31040 Rigole di Mansuè (TV), Italy, email <a href="mailto:info@danova-tech.com">info@danova-tech.com</a>. These terms govern access to and use of the site and the content it hosts.</p>`],
        ['Acceptance',
         `<p>By browsing the site you accept these terms in full. If you do not agree with them, please do not use the site.</p>`],
        ['Permitted use',
         `<p>You may consult and use the site for information purposes and to get in touch with us. It is prohibited to: use the site for unlawful purposes or contrary to good faith, attempt unauthorised access to systems or restricted areas, carry out automated bulk extraction of content, introduce malicious code, or take any action that compromises the site's operation or security.</p>`],
        ['Intellectual property',
         `<p>The code, graphics, texts, layouts, processed images and the <b>Danova Tech</b> name and logo belong to Danova Tech or its licensors and are protected by copyright and trademark law. Reproduction, modification, distribution or reuse, in whole or in part, is prohibited without written authorisation.</p>
          <p>Any third-party trademarks, names and logos mentioned belong to their respective owners and are used for descriptive purposes only.</p>`],
        ['Content and availability',
         `<p>The content is informational and promotional and may be changed or removed at any time without notice. While we take care over accuracy, we do not warrant that the information is complete or always up to date.</p>
          <p>We aim to keep the site reachable, but we do not guarantee uninterrupted service: access may be suspended for maintenance, updates or reasons beyond our control.</p>`],
        ['Quotation requests and formation of contract',
         `<p>Information about services, timescales and methods published on the site is indicative and <b>does not constitute an offer to the public</b> under Art. 1336 of the Italian Civil Code. Sending a request through the form or by email binds neither party.</p>
          <p>A relationship is formed only upon written acceptance of a specific quotation, which sets out the scope, timescales, fees and conditions of the service and prevails over anything stated on the site.</p>`],
        ['Projects, figures and examples',
         `<p>The cases, examples and performance figures shown on the site relate to specific contexts, markets and periods. They are not a promise or guarantee of equivalent results for other projects, which depend on variables such as sector, budget, competition and target market.</p>`],
        ['Limitation of liability',
         `<p>To the extent permitted by law, Danova Tech is not liable for indirect or consequential damages arising from the use of, or inability to use, the site, from service interruptions, or from the content of linked third-party sites. Nothing in these terms limits liability for wilful misconduct, gross negligence, or in cases where the law does not allow exclusions.</p>`],
        ['Links to third-party sites',
         `<p>The site may contain links to external resources, provided for your convenience. We do not control those sites and are not responsible for their content, their policies or the services they offer.</p>`],
        ['Personal data protection',
         `<p>The processing of personal data collected through the site is described in the <b>Privacy Policy</b> and the <b>Cookie Policy</b>, which form an integral part of these terms.</p>`],
        ['Governing law and jurisdiction',
         `<p>These terms are governed by Italian law. For disputes with users who qualify as consumers, the courts of the consumer's place of residence or elected domicile have exclusive jurisdiction. In all other cases, the courts of the place where the site owner is established have jurisdiction.</p>`],
        ['Changes to these terms',
         `<p>These terms may be updated at any time. The applicable version is the one published on this page at the time of access, with its last-updated date.</p>`]
      ]}
    }
  },
  meta:{title:'Websites, SEO, Meta Ads and custom software | Danova Tech',
        desc:'Italian tech agency building websites and e-commerce, SEO and Meta Ads campaigns, apps, ERP systems and custom software. Free quote, reply within 24h.'}
};
