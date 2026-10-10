# -*- coding: utf-8 -*-
"""Pagine per il mercato USA (inglese americano, en-US).
   Si modifica qui, poi si rilancia:
       python3 seo-tools/pagine-build-usa.py
   Niente allestimenti fieristici in queste pagine: solo siti, app, software e gestionali."""
OGGI = "2026-10-10"
PAGINE = []
US = {"@type": "Country", "name": "United States"}

def area(city, state):
    return [{"@type": "City", "name": city},
            {"@type": "State", "name": state}, US]

def short_title(t, brand=" | Danova Tech"):
    return t + brand if len(t + brand) <= 60 else t

# ---------------------------------------------------------------------------
# Fusi orari: Italia rispetto alla citta' (ora legale allineata quasi tutto l'anno)
TZ = {
 "ET": ("Eastern", 6,
        "Italy is six hours ahead of {c}. Our afternoon is your morning: between 9am and noon Eastern we are both at our desks, and that is where calls, reviews and decisions go. The rest of our working day happens while you are still asleep, so you start the morning with yesterday's questions answered and new work to look at."),
 "CT": ("Central", 7,
        "Italy is seven hours ahead of {c}. Between 8 and 11am Central we are both working, and that window is where calls and decisions go. Most of our build time happens before your day starts, so a question you send in the evening usually has an answer, and often a working fix, by the time you open your laptop."),
 "MT": ("Mountain", 8,
        "Italy is eight hours ahead of {c}. The shared window is your early morning, roughly 7 to 10am Mountain, which is our late afternoon. It is enough for a weekly review and quick decisions; it is not enough for a supplier who sits in your Slack all day, and we would rather say that now."),
 "AZ": ("Arizona", 8,
        "Italy is eight hours ahead of {c} in winter and nine in summer, because Arizona does not change its clocks. The shared window is your early morning, roughly 7 to 9am, our late afternoon. It works for weekly reviews and quick decisions; if you need a supplier available on chat all afternoon, a local firm fits better."),
 "PT": ("Pacific", 9,
        "Italy is nine hours ahead of {c}. That is the widest gap in the country, and we will not pretend otherwise: the shared window is your early morning, about 7 to 9am Pacific, our late afternoon. It works well for weekly reviews and decisions, and the upside is real — we build while you sleep, so you wake up to progress. It does not work if you need someone on a call with you at 3pm."),
}

def tz_par(code, city):
    return TZ[code][2].format(c=city)

# ---------------------------------------------------------------------------
# Blocchi condivisi
def servizi_cards(city):
    return {"id":"build","tipo":"cards","eyebrow":"What we build",
     "h2":"Websites, apps and software<br>for <span class=\"grad\">%s companies</span>" % city,
     "lead":"Six kinds of project cover almost everything that reaches us from the US. The first job on any call is working out which one you actually need — fairly often it is smaller than the one you came in asking for.",
     "corpo":[
      ("Company website","A handful of pages done properly: who you are, what you do, who for, how to reach you. Fast on a phone, accessible, and written around the words your customers actually type into Google. From €350 one-off, or €24.80 a month with hosting and changes included."),
      ("E-commerce","Product pages, checkout, shipping rules, sales tax settings, order handling. Shopify when it fits, custom when it does not, and connected to your inventory or accounting so nothing gets keyed in twice."),
      ("Mobile apps","iOS and Android apps, or an installable web app when the App Store adds nothing. Booking, loyalty, field service, ordering, internal tools for crews who are never at a desk."),
      ("Custom business software","Inventory, jobs, scheduling, quoting, service reports. Built around how your company works instead of how a SaaS vendor decided everyone should work. Custom systems start from €1,500."),
      ("CRM and client portals","Leads, deals, orders and documents in one place, plus a portal where clients check status themselves instead of emailing you. Usually saves more hours than the public website."),
      ("Integrations and automation","Two systems that do not talk, and a person retyping data between them: QuickBooks, Shopify, HubSpot, Salesforce, spreadsheets. Automating that handover has the fastest payback of anything on this list.")]}

def metodo():
    return {"id":"method","tipo":"passi","eyebrow":"How we work",
     "h2":"Fixed price,<br>no <span class=\"grad\">surprises.</span>",
     "corpo":[
      ("Free 30-minute call","What you sell, who to, and what the site or software has to do. No sales deck. Sometimes the honest conclusion is that you need less than you thought."),
      ("Fixed-price quote","One figure in writing, covering everything needed to go live. It does not move mid-project: anything you add later is quoted separately, and only if you ask."),
      ("Built in stages","You see something usable within the first weeks, then every week after. Corrections happen during the build, not in a big review at the end."),
      ("Launch and after","Go-live, checks, training for your team. Maintenance is optional — you are not locked in, and the domain, accounts and source code are in your company's name.")]}

def faq_comuni(city, tz):
    nome, ore, _ = TZ[tz]
    return [
     ("How much does a website cost?","A company website costs €350 one-off, plus €150 if you want the initial optimization for Google and Bing, or €24.80 a month with hosting, domain, maintenance and content changes included on a 24-month minimum term. Web apps start at €50 a month or €750 one-off; custom business software starts at €1,500. Larger projects get a fixed quote after a free analysis."),
     ("How do the time zones work with %s?" % city,"Italy is %d hours ahead of %s time. We schedule calls in your morning, which is our afternoon, and do most of the build while you are offline. In practice you get answers overnight rather than waiting for them during your day." % (ore, nome)),
     ("Do we pay VAT or sales tax on your invoice?","Our invoices to US businesses are issued without Italian VAT, because business services sold outside the EU are not subject to it, and as a foreign service provider we do not add US sales tax. Your accountant will confirm how to record it on your side — it is a standard cross-border arrangement."),
     ("How do we pay, and in what currency?","Prices are set in euros and invoiced in euros; most US clients pay by international wire or card, and the bank converts at the day's rate. Projects are split into stages, each paid when it is delivered, so you are never far ahead of the work."),
     ("Will we own the website and the code?","Yes. On the one-off option the domain, hosting, content and source code are registered in your company's name from go-live, and the code lives in your repository. There is no license tied to us and no lock-in."),
     ("How long until we go live?","Two to eight weeks for a website, depending on scope; four to eight weeks for the first usable stage of an app or business system. What stretches a project is almost never the code — it is the copy, the photos and the decisions."),
    ]

def ctabox(city):
    return {"h2":"Got a project in %s?" % city,
            "p":"Thirty minutes on a video call, free and with no sales deck: we tell you what you actually need, what it costs and how long it takes to go live. If we are not the right fit, we tell you that too.",
            "btn":"Book a free call"}

ALTRI_BASE = [("Web design agency USA","/en/web-design-agency-usa/"),
              ("Software development company USA","/en/software-development-company-usa/"),
              ("Mobile app development USA","/en/mobile-app-development-company-usa/"),
              ("Custom ERP &amp; CRM development","/en/custom-erp-crm-development-usa/"),
              ("All US cities we work with","/en/united-states/"),
              ("Pricing","/en/pricing/")]

# ---------------------------------------------------------------------------
# Citta'. slug -> (nome, stato, codice fuso)
CITTA = [
 ("new-york","New York","New York","ET"),
 ("los-angeles","Los Angeles","California","PT"),
 ("chicago","Chicago","Illinois","CT"),
 ("houston","Houston","Texas","CT"),
 ("dallas","Dallas","Texas","CT"),
 ("miami","Miami","Florida","ET"),
 ("san-francisco","San Francisco","California","PT"),
 ("boston","Boston","Massachusetts","ET"),
 ("seattle","Seattle","Washington","PT"),
 ("austin","Austin","Texas","CT"),
 ("atlanta","Atlanta","Georgia","ET"),
 ("phoenix","Phoenix","Arizona","AZ"),
 ("philadelphia","Philadelphia","Pennsylvania","ET"),
 ("san-diego","San Diego","California","PT"),
 ("denver","Denver","Colorado","MT"),
 # seconda fascia (10 ottobre 2026)
 ("washington-dc","Washington, DC","District of Columbia","ET"),
 ("san-antonio","San Antonio","Texas","CT"),
 ("san-jose","San Jose","California","PT"),
 ("nashville","Nashville","Tennessee","CT"),
 ("charlotte","Charlotte","North Carolina","ET"),
 ("orlando","Orlando","Florida","ET"),
 ("tampa","Tampa","Florida","ET"),
 ("las-vegas","Las Vegas","Nevada","PT"),
 ("minneapolis","Minneapolis","Minnesota","CT"),
 ("detroit","Detroit","Michigan","ET"),
 ("portland","Portland","Oregon","PT"),
 ("raleigh","Raleigh","North Carolina","ET"),
 ("salt-lake-city","Salt Lake City","Utah","MT"),
 ("columbus","Columbus","Ohio","ET"),
 ("kansas-city","Kansas City","Missouri","CT"),
]
NOME = {s:n for s,n,_,_ in CITTA}
TOP3 = ("new-york","los-angeles","chicago")
# citta' con pagina software/app dedicata (volumi Keyword Planner 10/2026)
SW_CITTA = ("new-york","los-angeles","chicago","dallas","houston","miami","atlanta","austin","san-francisco","denver","orlando")

REGIONI = [
 ("Northeast", ["new-york","boston","philadelphia","washington-dc"]),
 ("Southeast", ["miami","atlanta","orlando","tampa","charlotte","raleigh","nashville"]),
 ("Midwest", ["chicago","minneapolis","detroit","columbus","kansas-city"]),
 ("Texas and the Southwest", ["houston","dallas","austin","san-antonio","phoenix","las-vegas"]),
 ("West Coast and Mountain", ["los-angeles","san-francisco","san-jose","san-diego","seattle","portland","denver","salt-lake-city"]),
]
REG = {s:i for i,(_,ss) in enumerate(REGIONI) for s in ss}

def altri_citta(slug, n=5):
    stessa = [s for s in REGIONI[REG[slug]][1] if s != slug]
    resto = [s for s in TOP3 if s != slug and s not in stessa]
    vicine = (stessa + resto)[:n]
    return [("Web design %s" % NOME[s], "/en/web-design-%s/" % s) for s in vicine]

# Pagine di settore e guide (contenuto in pagine-dati-usa-2.py): elenco per i link
INDUSTRIE = [
 ("Web design for law firms","/en/web-design-for-law-firms/"),
 ("Medical and dental practice websites","/en/medical-practice-website-design/"),
 ("Contractor website design","/en/contractor-website-design/"),
 ("Construction management software","/en/construction-management-software/"),
 ("Restaurant websites and ordering apps","/en/restaurant-website-design/"),
 ("Real estate website development","/en/real-estate-website-development/"),
 ("Shopify development agency","/en/shopify-development-agency/"),
 ("Trucking and logistics software","/en/trucking-logistics-software-development/"),
 ("Manufacturing software development","/en/manufacturing-software-development/"),
 ("MVP development for startups","/en/mvp-development-for-startups/"),
 ("Gym and fitness app development","/en/gym-fitness-app-development/"),
 ("Field service app development","/en/field-service-app-development/"),
]
# Servizi specifici aggiunti dopo il Keyword Planner USA (10/2026)
EXTRA = [
 ("Small business web design","/en/small-business-web-design/"),
 ("WordPress web design and development","/en/wordpress-web-design/"),
 ("Web app development company","/en/web-app-development-company/"),
 ("Hire app developers","/en/hire-app-developers/"),
 ("Business process automation","/en/business-process-automation/"),
 ("API integration services","/en/api-integration-services/"),
 ("Custom CRM development","/en/custom-crm-development/"),
 ("Custom property management software","/en/property-management-software-development/"),
 ("Custom MES software","/en/mes-software-development/"),
 ("ADA website audit","/en/ada-website-audit/"),
 ("SEO company for US businesses","/en/seo-company-usa/"),
]
GUIDE = [
 ("How much does an app cost","/en/how-much-does-an-app-cost/"),
 ("How much does custom software cost","/en/how-much-does-custom-software-cost/"),
 ("ADA website compliance","/en/ada-website-compliance/"),
 ("Website privacy laws by US state","/en/website-privacy-laws-us-states/"),
 ("Outsourcing software development to Europe","/en/outsourcing-software-development-to-europe/"),
 ("How much does a website cost","/en/how-much-does-a-website-cost/"),
]

# Contenuto specifico per citta'
C = {}

C["new-york"] = {
 "lead":"Straight answer first: we are not in Manhattan. We are a ten-person web and software team in northern Italy, working in English for US companies. Below is why that usually works in your favor, when it does not, and what we build for New York businesses.",
 "sectors":[
  ("Professional services and law firms","Practice-area pages that rank on their own, intake forms that route to the right partner, client portals for documents and case status. Built to WCAG 2.1 AA, which in New York is not optional."),
  ("Real estate","Listing sites fed from your MLS or CRM, owner and tenant portals, maintenance request apps for property managers running buildings across several boroughs."),
  ("Restaurants and hospitality","Fast menus that load on a subway connection, reservation and ordering flows that skip the marketplace fees, loyalty apps for groups with more than one location."),
  ("Finance and insurance","Quote calculators, onboarding flows, secure document upload and internal dashboards — the tools that sit around your core platform and currently live in spreadsheets."),
  ("Fashion, beauty and retail","DTC shops with real product photography front and center, wholesale ordering portals for buyers, inventory synced between the store on Spring Street and the website."),
  ("Italian importers and brands","Food, wine, design and fashion brands bringing Italian products to the US: bilingual sites, B2B ordering for distributors, and a team that speaks both sides of the deal.")],
 "market":[
  "Manhattan agency rates are a structure cost. Midtown rent, New York salaries and an account team between you and the people doing the work all end up in the quote. For some projects that is worth every dollar; for most company websites and internal tools it is not.",
  "We are a small team with low fixed costs. For the same work the quote is a fraction of a typical New York agency's, and not because we cut hours — there is simply less overhead to carry. You also talk directly to the person building your project rather than to an account manager who relays it.",
  "New York has one specific risk worth knowing before you build anything: <b>website accessibility lawsuits</b>. A large share of ADA website cases in the country are filed in New York's federal courts, many against small and mid-size businesses. Every site we build follows WCAG 2.1 AA — contrast, keyboard navigation, alt text, form labels, screen-reader testing — because retrofitting it after a demand letter costs far more than building it right."],
 "search":[
  "On a query like \"web design NYC\" you are up against directories, review platforms and agencies with fifteen-year-old domains. Aiming there in month one is the fastest way to spend a budget without moving a position.",
  "New York search is local in a very particular way: people search by borough and neighborhood — Brooklyn, Queens, Long Island City, the Upper East Side, Williamsburg — far more than by \"New York\". If you have a physical address, a Google Business Profile done properly plus pages written for the areas you actually serve compete in a much smaller, much more winnable field.",
  "The other door is the problem itself. Not \"accountant New York\" but \"accountant for restaurant groups Brooklyn\"; not \"IT company NYC\" but the specific system you fix. Those searches have a few dozen visits a month each and convert far better, and the pages currently ranking for them are often generic filler that better writing simply overtakes."],
 "faq":[
  ("Do you work with New York companies from Italy?","Yes, in English. Italy is six hours ahead of New York, so your morning overlaps with our afternoon every working day. Video calls handle almost everything; for larger projects we fly over for the kickoff workshop when it genuinely helps."),
  ("Will our website be ADA compliant?","We build every site to WCAG 2.1 AA, the standard US courts and the Department of Justice refer to, and we test with keyboard navigation and screen readers before launch. No developer can promise you will never receive a demand letter, but a site built this way gives a plaintiff's firm very little to work with — which is the point."),
  ("Do you work with Italian companies opening in New York?","Yes, often. Bilingual sites, US-ready e-commerce with sales tax and shipping set up correctly, and B2B portals for distributors. We speak Italian with headquarters and English with the US team, which removes a surprising amount of friction.")],
}

C["los-angeles"] = {
 "lead":"We are not in Santa Monica or Culver City. We are a ten-person web and software team in northern Italy, working in English for US companies — nine hours ahead of you, which turns out to be useful. Here is what we build for Los Angeles businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("DTC and e-commerce brands","Shopify or custom stores built for conversion, not for an awards site: fast product pages, subscriptions, bundles, and inventory synced with your 3PL or warehouse in the Inland Empire."),
  ("Fashion and apparel","Lookbook sites that load fast despite the photography, wholesale ordering portals for buyers, and production tracking tools for brands working with Downtown's Fashion District."),
  ("Entertainment and creative studios","Portfolio sites, casting and booking tools, project and asset trackers for production companies that currently run on shared drives and group texts."),
  ("Beauty, wellness and clinics","Booking apps, membership and loyalty programs, patient intake forms, and sites that make treatments easy to understand before anyone calls."),
  ("Real estate and property management","Listing sites, owner portals, maintenance apps for portfolios spread from the Valley to Long Beach."),
  ("Logistics and import","With the ports of Los Angeles and Long Beach next door: shipment tracking portals, customs document workflows, warehouse and inventory systems built around your actual process.")],
 "market":[
  "Los Angeles agency pricing reflects Los Angeles: Westside rent, creative salaries and long account chains. You pay for the brand on the credentials slide as much as for the work, and for a company website or an internal tool that is rarely where the value is.",
  "We are a small team with low fixed costs, so for the same scope the quote is a fraction of a typical LA agency's. You speak to the person who builds your project. And the time difference works in your favor more than you would expect: we build while you sleep, so a request sent at 6pm often has a working version waiting at 9am.",
  "California also has two legal layers worth knowing. The <b>CCPA/CPRA</b> governs how you collect and use personal data from California residents, and accessibility claims can be brought under both the ADA and California's Unruh Act. Every site we build follows WCAG 2.1 AA and ships with a proper cookie and privacy setup — your lawyer decides the policy wording, we make sure the site actually does what the policy says."],
 "search":[
  "Nobody in Los Angeles searches for Los Angeles. People search for Pasadena, Burbank, Santa Monica, Silver Lake, Torrance, Long Beach, the Valley. The metro is really dozens of cities, and Google treats it that way.",
  "That is good news if you have an address: a well-run Google Business Profile plus pages written for the specific areas you serve compete in a far smaller field than \"web design Los Angeles\", which belongs to directories and agencies with years of backlinks.",
  "For e-commerce brands the game is different — it is national, not local — and the narrow door is the product itself: long, specific searches with buying intent, product pages with real content and structured data, and category pages that answer the question instead of just listing items."],
 "faq":[
  ("A nine-hour time difference — how does that actually work?","Calls go in your early morning, roughly 7 to 9am Pacific, which is our late afternoon. Then we work while you are offline. Most LA clients end up liking it: feedback sent in the evening becomes a new version by the next morning. What it does not support is a supplier on a call with you at 3pm — if you need that, choose someone local."),
  ("Is our site going to be CCPA compliant?","We build the technical side: a consent banner that actually blocks trackers until consent, a working \"Do Not Sell or Share\" link where needed, forms that collect only what you need, and a site that does what your privacy policy says. The policy wording and your obligations are for your counsel to confirm."),
  ("Do you work with Shopify?","Yes. Shopify is the right answer for many DTC brands, and we build themes, apps and integrations on it. When a store outgrows it — complex B2B pricing, custom configurators, unusual fulfillment — we build custom and connect it to the same back office.")],
}

C["chicago"] = {
 "lead":"We are not in the Loop. We are a ten-person web and software team in northern Italy, working in English for US companies, seven hours ahead of Chicago. Here is what we build for Chicago businesses, what it costs, and the cases where a local agency is the better choice.",
 "sectors":[
  ("Logistics and freight","Chicago moves a huge share of the country's freight. Shipment tracking portals for customers, dispatch and driver apps, dock scheduling, and the integrations between TMS, WMS and accounting that are currently somebody's full-time job."),
  ("Manufacturing","Product configurators and quoting tools, dealer and distributor portals, production tracking on the shop floor, maintenance scheduling for machines across several plants."),
  ("Food and beverage","B2B ordering for restaurants and grocers, lot traceability, recipe and cost management, and sites that help buyers find you before the trade show, not at it."),
  ("Professional services","Sites for accounting, legal and consulting firms that rank on specific services, plus client portals for document exchange that replace the email attachment chain."),
  ("Healthcare and clinics","Booking and intake flows, patient-facing apps, internal scheduling — built with HIPAA-conscious hosting and data handling where health data is involved."),
  ("Trades and home services","For contractors across the suburbs: estimating tools, job scheduling, crew time tracking, and websites that bring calls from Naperville, Schaumburg or Evanston rather than from nowhere.")],
 "market":[
  "Chicago is a practical market, and Chicago businesses tend to ask the practical question first: what does it cost and what does it save? That suits us. Our quotes are fixed, written and usually a fraction of a Loop agency's, because we carry far less overhead — not because we cut the hours.",
  "A lot of what reaches us from the Midwest is not a website at all. It is a company that runs on spreadsheets, a legacy system nobody wants to touch, and three people retyping orders between them. Replacing that with a system built around your actual process is often the project with the fastest payback.",
  "Illinois has one law every app builder here should know: <b>BIPA</b>, the Biometric Information Privacy Act. If an app or time clock uses fingerprints or face scans, written consent and a retention policy are required, and the lawsuits have been expensive. We design time-tracking and access apps to avoid biometrics unless you truly need them — and when you do, consent and retention are built into the flow."],
 "search":[
  "\"Web design Chicago\" is held by agencies and directories with years of links behind them. Chasing it in month one burns budget without moving a position.",
  "Chicagoland search splits by neighborhood and suburb — West Loop, Lincoln Park, Naperville, Oak Brook, Schaumburg, Evanston — and for B2B by the problem: \"freight broker software\", \"food distributor ordering portal\". Those narrow searches are where a well-written page ranks in months instead of years.",
  "For companies selling to other businesses across the Midwest, the most valuable pages are often the boring ones: a specific service, a specific industry, a specific integration. Fewer visits, far better leads."],
 "faq":[
  ("Do you work with Chicago companies from Italy?","Yes, in English. Italy is seven hours ahead of Chicago, so calls go in your morning, between about 8 and 11am Central. Most of the build happens before your day starts, which means questions sent in the evening usually have answers by morning."),
  ("Can you build an employee time-tracking app that is BIPA-safe?","Yes. The simplest approach is to avoid biometrics entirely — PIN, badge, GPS check-in or photo confirmation without facial recognition. If you need fingerprint or face scans, the app collects written consent, follows a published retention schedule and deletes data on time. Your counsel should review the policy wording."),
  ("Can you connect our ERP, TMS or accounting system?","Usually, yes. If a system has an API, or even just a reliable export, we can integrate it. We check feasibility on the first call before quoting, so you do not pay for an integration that turns out to be impossible.")],
}

C["houston"] = {
 "lead":"We are not in the Energy Corridor. We are a ten-person web and software team in northern Italy, working in English for US companies. Here is what we build for Houston businesses — from websites to field apps for crews who never see a desk — and when a local firm is the better call.",
 "sectors":[
  ("Energy and oilfield services","Field tickets, inspection checklists and job reports on a tablet that works offline at the well site, synced to the office when signal comes back. Plus asset and maintenance tracking."),
  ("Petrochemical and industrial","Maintenance management, contractor onboarding and safety documentation, permit workflows — the paperwork that currently lives in binders and shared drives."),
  ("Healthcare and clinics","Around the largest medical center in the world, clinics and practices need booking, intake and patient communication that does not leak data. HIPAA-conscious hosting where it applies."),
  ("Construction and contractors","Estimating and bid tools, daily reports with photos, crew scheduling and time tracking, job costing that tells you which projects actually made money."),
  ("Port, logistics and import","Shipment tracking for customers, warehouse and inventory systems, customs document workflows for companies working through the Port of Houston."),
  ("Restaurants and local services","Fast mobile sites, online ordering without marketplace commissions, booking and loyalty apps — and Google Business Profile work for Katy, Sugar Land, The Woodlands and Pearland.")],
 "market":[
  "Houston is an industrial city, and its software problems are industrial: crews in the field, equipment to maintain, paperwork that must be right. Most of what we build here is not a pretty website, it is a tool that saves hours every week and holds up when a supervisor uses it with gloves on.",
  "We quote it at a fixed price, in writing, split into stages that each deliver something usable. Our overhead is low, so the figure is a fraction of what a Houston firm with a downtown office typically charges — and you talk to the people building it.",
  "Texas now has its own privacy law, the <b>Texas Data Privacy and Security Act</b>, which applies to most businesses that process Texans' personal data. We build forms, cookie consent and data handling to match it, and your counsel confirms the policy side."],
 "search":[
  "Houston sprawls, and so does its search: people look for services in Katy, Cypress, Sugar Land, Pearland, The Woodlands, Spring, Pasadena — not in \"Houston\". For any business with an address, a properly run Google Business Profile and pages for the areas you actually serve are the fastest route to calls.",
  "For B2B companies in energy and industrial supply, the search is narrow and national: specific equipment, specific services, specific certifications. Pages that answer those exact questions, with real technical detail, win against generic competitors faster than any amount of \"Houston\" keywords.",
  "Spanish matters here too. A large share of Houston's customers search in Spanish, and we work in Spanish as well as English — a proper bilingual site, not an automatic translator bolted on top."],
 "faq":[
  ("Can your field apps work without signal?","Yes, and for Houston clients that is usually requirement number one. The app stores everything on the device, works offline at the site, and syncs automatically when it reconnects. Photos, signatures and timestamps included."),
  ("Do you build bilingual English and Spanish sites?","Yes. We write and structure both languages properly — separate URLs, correct hreflang tags, content written for each audience rather than machine-translated — so both versions can rank."),
  ("Do you work with Houston companies from Italy?","Yes, in English. Italy is seven hours ahead of Houston, so calls go in your morning and most of the build happens before your day starts.")],
}

C["dallas"] = {
 "lead":"We are not in Uptown or Las Colinas. We are a ten-person web and software team in northern Italy, working in English for US companies. Here is what we build for Dallas–Fort Worth businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("Corporate and regional HQs","Internal tools that sit alongside your main systems: approval workflows, reporting dashboards, vendor and contract portals — the things IT never gets to because the backlog is two years long."),
  ("Financial services and insurance","Quote and application flows, agent portals, secure document upload, and calculators that turn a visitor into a qualified lead instead of a phone call."),
  ("Logistics and distribution","DFW is one of the country's big distribution hubs: order tracking portals, warehouse and inventory apps, driver and delivery apps, and the integrations between them."),
  ("Real estate and construction","Listing and development sites, investor portals, construction daily reports and job costing for builders working across a metro that keeps expanding north."),
  ("Franchises and multi-location","One site with proper location pages, centralized booking and ordering, loyalty apps, and reporting by location — built so each franchisee can rank locally."),
  ("Home services","HVAC, roofing, plumbing, pest control: fast sites that rank in Plano, Frisco, McKinney, Arlington and Fort Worth, plus scheduling and estimating tools for the crews.")],
 "market":[
  "Dallas is a headquarters town, and much of what reaches us from DFW is the gap between the big enterprise systems and the way teams really work. A department needs a tool now; the official roadmap says next year. A focused custom application, built in stages at a fixed price, fills that gap in weeks.",
  "Our overhead is low, so the quote is a fraction of what a Dallas agency with an Uptown office charges for the same scope. You talk directly to the people building the project, and the code ends up in your company's repository.",
  "Texas has its own privacy law, the <b>Texas Data Privacy and Security Act</b>. We build forms, consent and data handling to match it; your counsel confirms the policy side."],
 "search":[
  "DFW is not one market, it is a dozen cities: Plano, Frisco, McKinney, Irving, Arlington, Fort Worth, Denton. Local searches carry those names. For any business with a physical address, a solid Google Business Profile and real location pages beat a generic \"Dallas\" page every time.",
  "For franchise and multi-location businesses, the structure decides everything: one page per location with its own content, reviews and opening hours, all tied together with correct structured data. Done right, each location ranks in its own neighborhood.",
  "B2B companies should enter through the narrow door: the specific service and the specific industry. Those searches are small, the buyers are serious, and the competition is usually thin."],
 "faq":[
  ("Can you build tools that work alongside Salesforce, SAP or Microsoft 365?","Yes, that is common work for us. We build the missing piece and connect it through the platform's API, so data stays in the system of record and nobody retypes it."),
  ("Do you build multi-location sites for franchises?","Yes: one site, one page per location with its own content and structured data, centralized forms and booking, and reporting per location. It is one of the most effective local SEO structures there is."),
  ("Do you work with Dallas companies from Italy?","Yes, in English. Italy is seven hours ahead of Dallas, so calls go in your morning, roughly 8 to 11am Central.")],
}

C["miami"] = {
 "lead":"We are not in Brickell. We are a ten-person web and software team in northern Italy, working in English and Spanish — and Italian — for US companies. Here is what we build for Miami businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("Real estate and developers","Pre-construction project sites in English and Spanish, listing sites, investor and buyer portals, CRM for brokers who sell to clients in three countries."),
  ("Hospitality, restaurants and nightlife","Fast mobile sites, direct reservations and ordering without marketplace commissions, loyalty apps, and events calendars that actually stay up to date."),
  ("Trade with Latin America","Miami is the gateway to Latin America: B2B ordering portals, multilingual catalogs, shipment tracking and document workflows for importers, exporters and freight forwarders in Doral."),
  ("Finance and family offices","Secure client portals, onboarding flows, document vaults and reporting dashboards for wealth managers and the growing financial sector."),
  ("Health, aesthetics and wellness","Booking apps, intake forms, memberships and before-and-after galleries that load fast — with HIPAA-conscious handling where health data is involved."),
  ("Italian brands in Florida","Food, fashion, design and yachting brands from Italy with a Miami office: bilingual sites, US e-commerce set up correctly, and a team that speaks with headquarters in Italian.")],
 "market":[
  "Miami is the most multilingual business market in the country, and most websites here handle it badly: a Spanish version run through a translator, or no Spanish at all. We work natively in English, Spanish and Italian, and we build multilingual sites the way Google expects — separate URLs, correct hreflang tags, content written for each audience.",
  "Our overhead is low, so for the same scope the quote is a fraction of a Brickell agency's. Fixed price, in writing, split into stages. You talk to the people building the project.",
  "Florida is also one of the states where <b>ADA website accessibility lawsuits</b> are most frequent. Every site we build follows WCAG 2.1 AA and is tested with keyboard and screen reader before launch, so it is not an easy target."],
 "search":[
  "South Florida searches by place: Brickell, Doral, Coral Gables, Wynwood, Miami Beach, Aventura, Fort Lauderdale, Boca Raton. A Google Business Profile done properly and pages written for the areas you serve are the fastest path to calls.",
  "Then there is the second language. A real Spanish version opens a set of searches your English-only competitors are not even competing for — and often a Portuguese or Italian one does the same for international buyers.",
  "For real estate, the search is global: buyers in Bogotá, Madrid, Milan or Toronto search for Miami projects in their own language. A multilingual project site with proper structure can rank in those markets with surprisingly little competition."],
 "faq":[
  ("Do you build sites in English and Spanish?","Yes, natively — we work in English, Spanish, Italian, French and German. Each language gets its own URLs, correct hreflang tags and content written for that audience, not machine translation."),
  ("Do you work with Italian companies opening in Miami?","Yes, regularly. We talk with headquarters in Italian and with the US team in English, and set up the US side properly: sales tax, shipping, payment methods, accessibility."),
  ("Do you work with Miami companies from Italy?","Yes. Italy is six hours ahead of Miami, so calls go in your morning, between about 9am and noon Eastern, and most of the build happens while you are offline.")],
}

C["san-francisco"] = {
 "lead":"We are not in SoMa, and our rates show it. We are a ten-person web and software team in northern Italy, working in English for US companies. Here is what we build for Bay Area companies — mostly the things your engineers do not have time for — and when we are the wrong choice.",
 "sectors":[
  ("Startups: MVPs and prototypes","A first version you can put in front of users and investors in weeks, at a fixed price, with clean code your future engineering team can take over without a rewrite."),
  ("SaaS companies: marketing sites","Fast, accessible marketing sites and documentation that your growth team can edit without a pull request — so your engineers stay on the product."),
  ("Internal tools","Admin panels, ops dashboards, onboarding flows, support tooling. The internal software every company needs and no product roadmap ever prioritizes."),
  ("Biotech and life sciences","Sites that explain the science clearly to investors and partners, plus sample tracking, lab scheduling and data intake tools that replace shared spreadsheets."),
  ("Restaurants, retail and local services","Direct ordering, reservations, loyalty and fast mobile sites for businesses in the city and across the Peninsula and East Bay."),
  ("Integrations and automation","Connecting Stripe, HubSpot, Salesforce, Notion, your data warehouse and the spreadsheet finance refuses to give up — so the handover happens without a person in the middle.")],
 "market":[
  "Bay Area engineering time is the most expensive in the world, and it should go to your product. Everything around it — the marketing site, the internal admin, the integration nobody wants to own — is where an outside team at a fraction of the cost makes sense.",
  "That is most of what we do for San Francisco companies. Fixed price, written scope, code in your GitHub from day one, documented so your team can take it over. We are not cheap because we are junior; we are cheaper because we are in Italy and carry little overhead.",
  "California rules apply: the <b>CCPA/CPRA</b> for personal data, and accessibility claims under both the ADA and the Unruh Act. We build to WCAG 2.1 AA and implement consent properly; your counsel confirms the policy side."],
 "search":[
  "For SaaS and startups, organic search is national and international, not local. The pages that win are the specific ones: comparisons, integrations, use cases, alternatives. We build that structure into the marketing site from the start, with clean technical SEO underneath.",
  "For local businesses the Bay Area splits into dozens of searches: the Mission, Hayes Valley, Oakland, Berkeley, Palo Alto, San Mateo, San Jose. A real Google Business Profile and area pages beat any attempt at \"San Francisco\" as a whole.",
  "One more thing worth doing early: make your site readable by AI search. Clear structure, structured data and pages that answer specific questions are what ChatGPT, Perplexity and Google's AI answers quote."],
 "faq":[
  ("Will our engineers be able to take over the code?","Yes. Mainstream stacks (TypeScript, React, Next.js, Node, Python, PostgreSQL), code in your repository from the first commit, tests where they matter and documentation written for the next developer, not for us."),
  ("Is a nine-hour time difference workable?","For well-scoped work, yes. Calls go in your early morning, about 7 to 9am Pacific; we build while you are offline and you review in the morning. It does not work for a team that needs to pair with your engineers all afternoon."),
  ("Do you sign NDAs and assign IP?","Yes. Intellectual property in the work is assigned to your company in the contract, and we are happy to sign a reasonable NDA before discussing details.")],
}

C["boston"] = {
 "lead":"We are not in Kendall Square. We are a ten-person web and software team in northern Italy, working in English for US companies, six hours ahead of Boston. Here is what we build for Boston businesses, what it costs, and when a local firm is the better choice.",
 "sectors":[
  ("Biotech and life sciences","Investor-ready sites that explain the science without dumbing it down, plus sample tracking, lab scheduling and data intake tools that replace a wall of spreadsheets."),
  ("Healthcare practices","Booking, intake and patient communication built with HIPAA-conscious hosting and data handling, and sites that make services easy to understand before anyone calls."),
  ("Education and training","Course and program sites, enrollment flows, student and alumni portals for schools, bootcamps and training companies."),
  ("Robotics and hardware","Product sites with real technical depth, distributor portals, configurators and quoting tools for companies selling complex equipment."),
  ("Financial and professional services","Sites for firms that need to look established without looking dated, client portals for documents, and internal tools for reporting."),
  ("Restaurants and local services","Fast mobile sites, direct ordering and reservations, and Google Business Profile work for Cambridge, Somerville, Brookline, Newton and the North Shore.")],
 "market":[
  "Boston clients tend to read the whole proposal, and so they notice when a quote is mostly overhead. Ours is fixed, written and split into stages, and it is a fraction of what a Back Bay or Seaport agency charges for the same scope — because there is less overhead to carry, not fewer hours.",
  "A lot of what we build here sits around a core system: the internal tool a lab needs now, the portal a practice needs before the EHR vendor delivers one, the integration between two platforms that should talk and do not.",
  "Massachusetts has some of the strictest data security rules in the country (<b>201 CMR 17.00</b>) for anyone holding residents' personal information. We build with encryption, access control and logging by default, which makes your written security program easier to back up."],
 "search":[
  "Greater Boston searches by town: Cambridge, Somerville, Brookline, Newton, Quincy, Waltham, Burlington. If you have an address, a properly maintained Google Business Profile and area pages win calls far faster than a generic \"Boston\" page.",
  "For life sciences and B2B tech, the search is narrow and technical. Pages that answer specific questions with real depth — methods, specifications, integrations — outrank generic competitors and get cited by AI search tools.",
  "The order matters: narrow queries first, broad ones later, once the site has the history and links to compete."],
 "faq":[
  ("Do you build HIPAA-compliant apps?","We build with HIPAA in mind: hosting providers that sign a Business Associate Agreement, encryption in transit and at rest, access logs, minimal data collection. Compliance itself is a property of your whole organization, so your compliance lead signs off on the setup."),
  ("Can you work with our scientists on technical content?","Yes. We interview them, draft the pages, and they correct the science. It is the only way technical pages end up both accurate and readable."),
  ("Do you work with Boston companies from Italy?","Yes, in English. Italy is six hours ahead of Boston, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["seattle"] = {
 "lead":"We are not in South Lake Union. We are a ten-person web and software team in northern Italy, working in English for US companies, nine hours ahead of Seattle. Here is what we build for Seattle businesses, what it costs, and when a local firm is the better call.",
 "sectors":[
  ("E-commerce and Amazon sellers","A direct-to-consumer store alongside your marketplace listings, so you own the customer relationship — plus inventory sync so the two never oversell."),
  ("Tech companies: what engineers skip","Marketing sites, internal admin tools and integrations, at a fixed price, so your engineers stay on the product."),
  ("Aerospace and manufacturing suppliers","Quote and RFQ tools, supplier portals, document control and production tracking for shops in the Boeing supply chain and beyond."),
  ("Maritime and logistics","Vessel and fleet maintenance tracking, shipment portals and warehouse tools for companies working the Port of Seattle and Tacoma."),
  ("Health and fitness apps","Booking, membership and coaching apps — built with Washington's My Health My Data Act in mind, which covers far more apps than HIPAA does."),
  ("Coffee, food and hospitality","Online ordering, subscriptions, loyalty and fast mobile sites for local brands in Capitol Hill, Ballard, Fremont and across the Eastside.")],
 "market":[
  "Seattle engineering salaries are among the highest in the country, and they belong on your product. Everything around it — the marketing site, the admin panel, the integration — is where an outside team at a fraction of the cost makes sense.",
  "We quote fixed prices, in writing, in stages, with the code in your repository from the first commit. The nine-hour gap means we build while you sleep and you review in the morning.",
  "Washington's <b>My Health My Data Act</b> deserves attention before building any app that touches health, fitness, wellness or even some location data. It applies far beyond hospitals and clinics, with consent requirements stricter than most teams expect. We design data collection to match it from the start."],
 "search":[
  "Local search here splits by neighborhood and city: Capitol Hill, Ballard, Fremont, Bellevue, Redmond, Kirkland, Tacoma. A real Google Business Profile and area pages win local calls.",
  "For e-commerce brands the competition is national, and the narrow door is the product: specific, long searches with buying intent, product pages with real content, and structured data that earns rich results.",
  "For B2B suppliers, the pages that win are the technical ones — capabilities, certifications, materials, tolerances. Buyers search for those exact words."],
 "faq":[
  ("Does the My Health My Data Act apply to our app?","If your app collects data that could reveal a consumer's health status — including some fitness, wellness or location data — it may. We design consent flows and data minimization to match the law; your counsel confirms whether and how it applies to you."),
  ("Can you connect our store to Amazon?","Yes, through Amazon's APIs or your existing inventory platform: stock levels, orders and product data stay in sync so the website and the marketplace never oversell."),
  ("Is a nine-hour time difference workable?","For well-scoped work, yes. Calls go in your early morning, about 7 to 9am Pacific, and we build while you are offline.")],
}

C["austin"] = {
 "lead":"We are not on East 6th. We are a ten-person web and software team in northern Italy, working in English for US companies, seven hours ahead of Austin. Here is what we build for Austin businesses — from MVPs to booking apps — and when a local agency is the better choice.",
 "sectors":[
  ("Startups and MVPs","A first version you can show users and investors in weeks, at a fixed price, built on mainstream technology your future team can take over."),
  ("SaaS and tech companies","Marketing sites your growth team can edit, internal admin tools and integrations — the work that keeps engineers off the product."),
  ("Hospitality, music and events","Ticketing and booking flows, venue sites, event calendars, loyalty apps for a city that runs on live events."),
  ("Real estate and home builders","Community and listing sites, buyer portals, and construction tracking for builders working the fast-growing suburbs."),
  ("Semiconductor and manufacturing suppliers","Supplier portals, RFQ tools, document control and technical sites for companies serving the region's growing chip industry."),
  ("Home and local services","Fast sites and scheduling tools for contractors working Round Rock, Cedar Park, Georgetown, Pflugerville and San Marcos.")],
 "market":[
  "Austin grew faster than its agency market, and local rates followed tech salaries up. For an MVP, a marketing site or an internal tool, that premium rarely buys anything you need.",
  "We work at a fixed price, in stages, with code in your repository from day one — at a fraction of a local agency's quote, because our overhead is a fraction of theirs. You talk to the people building the project.",
  "Texas has its own privacy law, the <b>Texas Data Privacy and Security Act</b>. We build forms, consent and data handling to match it; your counsel confirms the policy side."],
 "search":[
  "Local Austin search splits by area — Downtown, South Congress, East Austin, the Domain, Round Rock, Cedar Park. A well-run Google Business Profile and real area pages win calls faster than a generic page.",
  "For startups, search is national: comparisons, alternatives, integrations, use cases. We build that page structure into the marketing site from the first version so it can grow without a redesign.",
  "And make the site readable by AI search from day one: structured data, clear answers to specific questions, and fast pages."],
 "faq":[
  ("How fast can you ship an MVP?","A focused MVP typically takes six to ten weeks, depending on scope. We cut it to the smallest version that tests the idea, fix the price, and ship working builds every week."),
  ("Will our future engineers be able to take over the code?","Yes. Mainstream stacks, code in your GitHub from the first commit, and documentation written for the next developer."),
  ("Do you work with Austin companies from Italy?","Yes, in English. Italy is seven hours ahead of Austin, so calls go in your morning, roughly 8 to 11am Central.")],
}

C["atlanta"] = {
 "lead":"We are not in Midtown or Buckhead. We are a ten-person web and software team in northern Italy, working in English for US companies, six hours ahead of Atlanta. Here is what we build for Atlanta businesses, what it costs, and when a local firm is the better call.",
 "sectors":[
  ("Logistics and distribution","With one of the busiest airports in the world and a dense network of warehouses: shipment tracking portals, warehouse and inventory apps, driver apps and integrations."),
  ("Fintech and payments","Onboarding flows, merchant and partner portals, internal dashboards — the tools around your core platform."),
  ("Film and production","Production tracking, crew and location scheduling, asset management for the studios and production services that work in Georgia."),
  ("Corporate offices","Internal tools and portals that fill the gap between enterprise systems and how teams really work."),
  ("Healthcare and clinics","Booking, intake and patient communication with HIPAA-conscious hosting where health data is involved."),
  ("Home services and contractors","Fast sites, estimating and scheduling tools for businesses working Alpharetta, Marietta, Decatur, Roswell and Sandy Springs.")],
 "market":[
  "Atlanta is a logistics and headquarters city, and much of what reaches us from here is operational: tracking, scheduling, inventory, the integration between two systems that should already talk.",
  "We quote it at a fixed price, in writing, in stages that each deliver something usable. Our overhead is low, so the figure is a fraction of a Midtown agency's, and you talk to the people building it.",
  "Every site we build follows WCAG 2.1 AA accessibility, tested with keyboard and screen reader before launch — the standard US courts and the Department of Justice refer to in ADA cases."],
 "search":[
  "Metro Atlanta searches by area: Midtown, Buckhead, Decatur, Alpharetta, Marietta, Sandy Springs, Roswell. A Google Business Profile run properly and real area pages win calls faster than a generic \"Atlanta\" page.",
  "For B2B logistics and fintech companies, search is national and narrow: the specific service, the specific integration, the specific industry. Those pages win in months.",
  "The order matters: narrow first, broad later."],
 "faq":[
  ("Can you integrate with our WMS or TMS?","Usually, yes. If the system has an API or a reliable export, we can connect it. We check feasibility before quoting."),
  ("Do you build ADA-accessible websites?","Yes, every site follows WCAG 2.1 AA and is tested before launch with keyboard navigation and screen readers."),
  ("Do you work with Atlanta companies from Italy?","Yes, in English. Italy is six hours ahead of Atlanta, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["phoenix"] = {
 "lead":"We are not in Scottsdale or Tempe. We are a ten-person web and software team in northern Italy, working in English for US companies. Here is what we build for Phoenix businesses, what it costs, and when a local agency is the better choice.",
 "sectors":[
  ("Home services","HVAC, pool, solar, roofing, pest control: fast sites that rank in Scottsdale, Mesa, Chandler, Gilbert and Glendale, plus scheduling, estimating and crew apps."),
  ("Construction and home builders","Community sites, buyer portals, daily reports, job costing and subcontractor scheduling for one of the fastest-growing metros in the country."),
  ("Semiconductor and manufacturing suppliers","Supplier portals, RFQ and quoting tools, document control and technical sites for companies serving the new fabs."),
  ("Healthcare and senior care","Booking, intake, family portals and staff scheduling, with HIPAA-conscious handling where health data is involved."),
  ("Real estate","Listing sites, property management portals and maintenance apps for portfolios across the Valley."),
  ("Hospitality and golf","Direct booking, event and tee-time flows, memberships and loyalty for resorts, restaurants and clubs.")],
 "market":[
  "Phoenix is growing faster than almost any metro in the country, and its businesses are mostly busy rather than digital: crews, jobs, estimates and schedules running on paper and group texts. A system built around that work pays for itself quickly.",
  "We quote it at a fixed price, in writing, in stages, at a fraction of what a local agency typically charges — because our overhead is low, not because we cut hours.",
  "Every site we build follows WCAG 2.1 AA accessibility and ships with proper consent handling."],
 "search":[
  "The Valley searches by city: Scottsdale, Mesa, Chandler, Gilbert, Tempe, Glendale, Peoria. For home services, a strong Google Business Profile, real reviews and service-area pages decide who gets the call.",
  "Seasonal demand matters here: AC repair in June, pool services in spring. Pages and campaigns timed to the season outperform year-round generic content.",
  "For B2B suppliers, the narrow technical pages — capabilities, certifications, materials — are where buyers actually search."],
 "faq":[
  ("Can you build a scheduling app for our crews?","Yes: jobs, routes, photos, signatures and time tracking on the phone, working offline, synced with the office and your invoicing system."),
  ("How does the time difference work with Arizona?","Arizona does not change its clocks, so Italy is eight hours ahead in winter and nine in summer. Calls go in your early morning; we build while you are offline."),
  ("Do you work with Phoenix companies from Italy?","Yes, in English, with calls in your morning and the build happening overnight.")],
}

C["philadelphia"] = {
 "lead":"We are not in Center City. We are a ten-person web and software team in northern Italy, working in English for US companies, six hours ahead of Philadelphia. Here is what we build for Philadelphia businesses, what it costs, and when a local firm is the better call.",
 "sectors":[
  ("Life sciences and cell and gene therapy","Investor-ready sites that explain the science, plus sample tracking, scheduling and data intake tools for the region's fast-growing biotech cluster."),
  ("Healthcare and practices","Booking, intake and patient communication with HIPAA-conscious hosting and data handling."),
  ("Law and professional services","Practice-area pages that rank, intake forms that route to the right person, client portals for documents — built to WCAG 2.1 AA."),
  ("Manufacturing and distribution","Configurators, quoting tools, distributor portals and inventory systems for companies across the region and South Jersey."),
  ("Education","Program and enrollment sites, student and alumni portals for schools and training providers."),
  ("Restaurants and local services","Fast mobile sites, direct ordering and Google Business Profile work for Fishtown, South Philly, Manayunk, the Main Line and King of Prussia.")],
 "market":[
  "Philadelphia sits between New York and Washington, and its agency prices often follow New York's. For a company website, a portal or an internal tool, that premium rarely buys anything you need.",
  "Our quotes are fixed, written and split into stages, at a fraction of a Center City agency's — because our overhead is low, not because we cut hours. You talk directly to the people building the project.",
  "Every site we build follows WCAG 2.1 AA accessibility, tested before launch, which matters in a region where ADA website claims are common."],
 "search":[
  "Philadelphia searches by neighborhood and suburb: Fishtown, Northern Liberties, Manayunk, the Main Line, King of Prussia, Cherry Hill. A strong Google Business Profile and real area pages win local calls.",
  "For life sciences and B2B, search is narrow and technical. Pages that answer precise questions in real depth outrank generic competitors and get quoted by AI search tools.",
  "Narrow first, broad later — that order cannot be reversed."],
 "faq":[
  ("Do you build HIPAA-conscious apps for practices?","Yes: hosting providers that sign a BAA, encryption, access logs and minimal data collection. Your compliance lead signs off on the setup."),
  ("Can you take over an existing site?","Yes. We check first whether fixing beats rebuilding, and if we rebuild, the redirect plan is ready before launch so rankings survive."),
  ("Do you work with Philadelphia companies from Italy?","Yes, in English. Italy is six hours ahead of Philadelphia, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["san-diego"] = {
 "lead":"We are not in Sorrento Valley. We are a ten-person web and software team in northern Italy, working in English and Spanish for US companies, nine hours ahead of San Diego. Here is what we build for San Diego businesses, what it costs, and when a local firm is the better call.",
 "sectors":[
  ("Biotech and life sciences","Sites that explain the science clearly, plus sample tracking, lab scheduling and data intake tools for companies in Torrey Pines and Sorrento Valley."),
  ("Defense and technical suppliers","Capability sites with real technical depth, RFQ tools and document control for companies serving the region's defense and telecom sectors."),
  ("Cross-border trade","Bilingual sites, shipment tracking and document workflows for companies working with manufacturing across the border in Baja California."),
  ("Tourism and hospitality","Direct booking, tours and activities, loyalty and fast mobile sites for hotels, restaurants and attractions."),
  ("Craft beverage and food brands","E-commerce, wholesale ordering portals for distributors and taprooms, and sites with real personality."),
  ("Home and local services","Fast sites and scheduling tools for businesses in Carlsbad, Oceanside, Chula Vista, Escondido and La Jolla.")],
 "market":[
  "San Diego businesses often pay Los Angeles agency rates without getting anything for the premium. For a company website, a portal or an internal tool, the value is in the work, not in the address.",
  "We quote it at a fixed price, in writing, in stages, at a fraction of a local agency's — and we build while you sleep, so you review progress every morning.",
  "California rules apply: the <b>CCPA/CPRA</b> for personal data, and accessibility claims under both the ADA and the Unruh Act. We build to WCAG 2.1 AA and implement consent properly."],
 "search":[
  "San Diego County searches by area: Downtown, North Park, La Jolla, Carlsbad, Encinitas, Chula Vista, Escondido. A well-run Google Business Profile and real area pages win local calls.",
  "Spanish is the second door: a real Spanish version opens searches that English-only competitors are not competing for.",
  "For biotech and technical B2B, the narrow technical pages are where buyers and partners search — and where AI search tools find answers worth quoting."],
 "faq":[
  ("Do you build bilingual English and Spanish sites?","Yes, natively: separate URLs, correct hreflang tags and content written for each audience."),
  ("Is a nine-hour time difference workable?","For well-scoped work, yes. Calls go in your early morning, about 7 to 9am Pacific, and we build while you are offline."),
  ("Is our site going to be CCPA compliant?","We build the technical side: consent that actually blocks trackers, opt-out links where required, minimal data collection. Your counsel confirms the policy wording.")],
}

C["denver"] = {
 "lead":"We are not in LoDo or RiNo. We are a ten-person web and software team in northern Italy, working in English for US companies, eight hours ahead of Denver. Here is what we build for Denver businesses, what it costs, and when a local agency is the better choice.",
 "sectors":[
  ("Outdoor and recreation brands","E-commerce with real product depth, rentals and booking flows, and wholesale portals for retailers."),
  ("Construction and real estate","Daily reports, job costing, subcontractor scheduling, buyer and investor portals for a metro still growing in every direction."),
  ("Aerospace and technical suppliers","Capability sites, RFQ tools, document control and supplier portals."),
  ("Energy and field services","Offline-ready field apps, inspection checklists and maintenance tracking for crews working across the Front Range and beyond."),
  ("Healthcare and wellness","Booking, intake and memberships with HIPAA-conscious handling where health data is involved."),
  ("Hospitality and local services","Fast sites, direct booking and Google Business Profile work for Boulder, Aurora, Lakewood, Littleton and the Denver Tech Center.")],
 "market":[
  "Denver's agency rates rose with its tech scene. For an online store, a field app or an internal tool, that premium rarely buys anything you need.",
  "We work at a fixed price, in writing, in stages, at a fraction of a local agency's quote. You talk to the people building the project, and the code ends up in your repository.",
  "Colorado has its own privacy law, the <b>Colorado Privacy Act</b>, including rules on universal opt-out signals. We build consent and data handling to respect them; your counsel confirms the policy side."],
 "search":[
  "The Front Range searches by city and neighborhood: LoDo, RiNo, Highlands, Cherry Creek, Boulder, Aurora, Lakewood, Littleton. A strong Google Business Profile and real area pages win local calls.",
  "For outdoor brands, search is national and seasonal: specific gear, specific activities, specific conditions. Product pages with real content beat thin catalogs every time.",
  "For B2B, the narrow technical pages are where buyers search."],
 "faq":[
  ("Do your field apps work offline in the mountains?","Yes. Data is stored on the device and syncs automatically when signal returns, with photos, signatures and timestamps."),
  ("Do you handle the Colorado Privacy Act's opt-out signals?","We implement the technical side, including honoring Global Privacy Control signals where required. Your counsel confirms how the law applies to you."),
  ("Do you work with Denver companies from Italy?","Yes, in English. Italy is eight hours ahead of Denver, so calls go in your early morning, about 7 to 10am Mountain.")],
}

# ---------------------------------------------------------------------------
# Seconda fascia di citta'
C["washington-dc"] = {
 "lead":"We are not on K Street. We are a ten-person web and software team in northern Italy, working in English for US organizations, six hours ahead of Washington. Here is what we build for DC-area businesses, associations and nonprofits, what it costs, and when a local firm is the better call.",
 "sectors":[
  ("Associations and nonprofits","Member portals, event registration, donation flows and resource libraries — on a budget a board can approve, and accessible to everyone who visits."),
  ("Government contractors","Capability sites with real past-performance detail, proposal and compliance trackers, and internal tools for teams that live in spreadsheets between contracts."),
  ("Law, policy and lobbying firms","Practice and issue pages that rank, publication libraries that are easy to search, and secure client portals for documents."),
  ("Consulting and professional services","Sites that make expertise concrete, plus client portals and reporting dashboards that replace weekly email updates."),
  ("Healthcare and clinics","Booking, intake and patient communication across DC, Maryland and Northern Virginia, with HIPAA-conscious hosting where health data is involved."),
  ("Hospitality and local services","Fast mobile sites, direct reservations and Google Business Profile work for Arlington, Alexandria, Bethesda, Silver Spring and Tysons.")],
 "market":[
  "Washington runs on organizations that need to look credible and be accessible — to members, to agencies, to the public. Much of what reaches us from the region is not a flashy site; it is a member portal, a resource library or an internal tracker that has outgrown its spreadsheet.",
  "Our quotes are fixed, written and split into stages, at a fraction of what a DC agency charges for the same scope, because our overhead is a fraction of theirs. You talk directly to the people building the project.",
  "Accessibility matters more here than almost anywhere. Federal agencies are bound by <b>Section 508</b>, many grants and contracts pass that expectation on, and private organizations face ADA claims. We build every site to WCAG 2.1 AA, which is the technical standard Section 508 points to, and test with keyboard and screen reader before launch."],
 "search":[
  "The DC metro spans three jurisdictions, and local searches carry their names: Arlington, Alexandria, Bethesda, Silver Spring, Tysons, Reston. A Google Business Profile done properly and pages for the areas you serve win local calls.",
  "For associations, think and policy organizations, organic search is about topics, not location: research, reports and explainers that answer specific questions. Clear structure and structured data also make that content easy for AI search tools to quote.",
  "For contractors, the narrow door is the capability itself — the specific service, certification or contract vehicle buyers search for."],
 "faq":[
  ("Do you build Section 508 compliant websites?","We build to WCAG 2.1 AA, which is the standard the Section 508 rules incorporate, and we test with keyboard navigation and screen readers. If you need a formal accessibility conformance report for a contract, we can document what was tested."),
  ("Can you build a member portal for our association?","Yes: member accounts, renewals, directories, gated resources and event registration, connected to your payment provider and, where possible, to your existing association management system."),
  ("Do you work with DC organizations from Italy?","Yes, in English. Italy is six hours ahead of Washington, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["san-antonio"] = {
 "lead":"We are not on the River Walk. We are a ten-person web and software team in northern Italy, working in English and Spanish for US companies, seven hours ahead of San Antonio. Here is what we build for San Antonio businesses, what it costs, and when a local agency is the better choice.",
 "sectors":[
  ("Healthcare and bioscience","Booking, intake and patient communication for practices and clinics around the South Texas Medical Center, with HIPAA-conscious hosting where it applies."),
  ("Military and defense suppliers","Capability sites, RFQ tools and document control for companies serving the bases that make up Joint Base San Antonio."),
  ("Cybersecurity and IT firms","Sites that make technical services concrete for buyers, plus client portals and reporting dashboards."),
  ("Tourism and hospitality","Direct booking, tours and events, and fast mobile sites for hotels, restaurants and attractions downtown and on the River Walk."),
  ("Construction and home services","Estimating, scheduling and crew apps, plus sites that rank in Stone Oak, Alamo Heights, New Braunfels and Schertz."),
  ("Bilingual local businesses","Real English and Spanish sites — separate pages, correct hreflang, content written for each audience — for a city where a large share of customers search in Spanish.")],
 "market":[
  "San Antonio is one of the most bilingual large cities in the country, and most local websites ignore it or bolt on an automatic translator. We work natively in English and Spanish and build both versions the way Google expects, which opens searches your competitors are not even competing for.",
  "Our quotes are fixed, in writing, in stages, at a fraction of a local agency's — because our overhead is low, not because we cut hours.",
  "Texas has its own privacy law, the <b>Texas Data Privacy and Security Act</b>. We build forms, consent and data handling to match it; your counsel confirms the policy side."],
 "search":[
  "Local searches here carry area names: Stone Oak, Alamo Heights, the Pearl, Medical Center, New Braunfels, Boerne. A strong Google Business Profile and real area pages win calls.",
  "The Spanish version is the second door, and for many service businesses it is the bigger one.",
  "For defense and cyber suppliers, the narrow technical pages — capabilities, certifications, past performance — are where buyers search."],
 "faq":[
  ("Do you build bilingual English and Spanish sites?","Yes, natively: separate URLs per language, correct hreflang tags, and content written for each audience rather than machine-translated."),
  ("Can you build a booking system for our clinic?","Yes: online booking, reminders, intake forms and cancellations, with HIPAA-conscious hosting and minimal data collection."),
  ("Do you work with San Antonio companies from Italy?","Yes, in English or Spanish. Italy is seven hours ahead of San Antonio, so calls go in your morning, roughly 8 to 11am Central.")],
}

C["san-jose"] = {
 "lead":"We are not in North San Jose's office parks, and our rates show it. We are a ten-person web and software team in northern Italy, working in English for US companies. Here is what we build for Silicon Valley companies — mostly the work your engineers should not be doing — and when we are the wrong choice.",
 "sectors":[
  ("Hardware and semiconductor companies","Product sites with real technical depth, datasheet libraries, distributor portals and RFQ tools that turn engineers' questions into qualified leads."),
  ("Enterprise SaaS","Marketing sites, documentation and integration pages your growth team can edit without a pull request."),
  ("Internal tools","Admin panels, ops dashboards and approval flows — the internal software no product roadmap ever prioritizes."),
  ("Startups","MVPs at a fixed price on mainstream technology, with code your future team can take over."),
  ("Manufacturing and supply chain","Supplier portals, quality and document control, production tracking for the Valley's remaining contract manufacturers."),
  ("Local businesses","Fast sites, ordering and booking for businesses in Santa Clara, Sunnyvale, Cupertino, Milpitas and Campbell.")],
 "market":[
  "Silicon Valley engineering time is among the most expensive anywhere, and it belongs on your product. The marketing site, the admin panel and the integration nobody owns are where an outside team at a fraction of the cost makes sense.",
  "Fixed price, written scope, code in your GitHub from day one, documented so your engineers can take it over. We build while you sleep and you review in the morning.",
  "California rules apply: the <b>CCPA/CPRA</b> for personal data, and accessibility claims under both the ADA and the Unruh Act. We build to WCAG 2.1 AA and implement consent properly."],
 "search":[
  "For B2B tech, search is national and technical: part numbers, specifications, integrations, comparisons. Pages that answer those precisely win, and get quoted by AI search tools.",
  "For local businesses the South Bay splits into cities — Santa Clara, Sunnyvale, Mountain View, Cupertino, Milpitas — and Google treats each as its own market.",
  "Technical SEO matters more for documentation-heavy sites than for any other kind: crawlable docs, clean URLs and structured data."],
 "faq":[
  ("Can you build a datasheet and documentation site?","Yes: searchable product and documentation pages, downloadable files, version history and structured data, editable by your product team."),
  ("Will our engineers be able to take over the code?","Yes. Mainstream stacks, your repository from the first commit, and documentation written for the next developer."),
  ("Is a nine-hour time difference workable?","For well-scoped work, yes. Calls go in your early morning, about 7 to 9am Pacific, and we build while you are offline.")],
}

C["nashville"] = {
 "lead":"We are not on Music Row. We are a ten-person web and software team in northern Italy, working in English for US companies, seven hours ahead of Nashville. Here is what we build for Nashville businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("Healthcare companies","Nashville is a national center of healthcare management: patient portals, scheduling, provider directories and internal tools, with HIPAA-conscious hosting and data handling."),
  ("Music and entertainment","Artist and label sites, booking and tour tools, merch stores and fan clubs that do not depend on social platforms."),
  ("Hospitality and tourism","Direct booking, events, and fast mobile sites for the venues, hotels and restaurants that serve millions of visitors a year."),
  ("Construction and real estate","Daily reports, job costing, scheduling and buyer portals for a metro that has been building nonstop."),
  ("Professional services","Sites that rank on specific services and client portals for accounting, legal and consulting firms."),
  ("Home services","Fast sites and scheduling tools for contractors working Franklin, Brentwood, Murfreesboro, Hendersonville and Mount Juliet.")],
 "market":[
  "Nashville grew fast, and local agency prices grew with it. For a company website, a booking system or an internal tool, that premium rarely buys anything you need.",
  "Our quotes are fixed, in writing, in stages, at a fraction of a local agency's — and you talk to the people building the project.",
  "Tennessee now has its own privacy law, the <b>Tennessee Information Protection Act</b>, which applies to larger businesses processing Tennesseans' data. We build consent and data handling to match it; your counsel confirms how it applies."],
 "search":[
  "Middle Tennessee searches by area: East Nashville, the Gulch, 12 South, Germantown, Franklin, Brentwood, Murfreesboro. A strong Google Business Profile and real area pages win calls.",
  "For healthcare companies, search is national and specific: the solution, the specialty, the problem. Narrow pages win faster than broad ones.",
  "For artists and venues, the most valuable search is your own name — make sure the official site, not a ticketing aggregator, is the first result."],
 "faq":[
  ("Do you build HIPAA-conscious portals?","Yes: hosting providers that sign a Business Associate Agreement, encryption, access logs and minimal data collection. Your compliance lead signs off on the setup."),
  ("Can you build a merch store and fan club for an artist?","Yes: a store, memberships, presale codes and mailing lists you own, connected to your fulfillment provider."),
  ("Do you work with Nashville companies from Italy?","Yes, in English. Italy is seven hours ahead of Nashville, so calls go in your morning, roughly 8 to 11am Central.")],
}

C["charlotte"] = {
 "lead":"We are not in Uptown. We are a ten-person web and software team in northern Italy, working in English for US companies, six hours ahead of Charlotte. Here is what we build for Charlotte businesses, what it costs, and when a local firm is the better choice.",
 "sectors":[
  ("Banking and fintech","Onboarding flows, client portals, calculators and internal dashboards for the second-largest banking center in the country and the fintechs around it."),
  ("Energy and utilities suppliers","Field apps, inspection and maintenance tracking, and capability sites for companies in the energy supply chain."),
  ("Motorsports and manufacturing","Product configurators, dealer portals and production tracking for the region's racing industry and manufacturers."),
  ("Logistics and distribution","Order tracking, warehouse and driver apps for distribution centers along I-85 and I-77."),
  ("Healthcare and clinics","Booking, intake and patient communication with HIPAA-conscious handling where health data is involved."),
  ("Home services and local businesses","Fast sites and scheduling tools for businesses in South End, Ballantyne, Matthews, Huntersville and Fort Mill.")],
 "market":[
  "Charlotte is a finance town, and finance teams know what overhead looks like in a quote. Ours is fixed, written and a fraction of an Uptown agency's for the same scope.",
  "Much of what reaches us here sits next to the big systems: the client-facing calculator, the onboarding flow, the internal dashboard that pulls data from three places.",
  "Every site we build follows WCAG 2.1 AA accessibility and handles consent properly — basic hygiene for regulated industries."],
 "search":[
  "Charlotte searches by neighborhood and town: South End, NoDa, Plaza Midwood, Ballantyne, Matthews, Huntersville, and across the state line in Fort Mill and Rock Hill.",
  "For financial and B2B services, the narrow pages — a specific product, a specific client type — win in months.",
  "Narrow first, broad later."],
 "faq":[
  ("Can you build tools for regulated financial firms?","Yes, with encryption, audit logs, roles and permissions, and hosting under your account. Your compliance team defines the requirements; we build to them and document it."),
  ("Can you build a dealer portal for our products?","Yes: price lists, orders, documents and warranty claims, connected to your ERP or accounting system."),
  ("Do you work with Charlotte companies from Italy?","Yes, in English. Italy is six hours ahead of Charlotte, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["orlando"] = {
 "lead":"We are not on International Drive. We are a ten-person web and software team in northern Italy, working in English and Spanish for US companies, six hours ahead of Orlando. Here is what we build for Orlando businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("Tourism and attractions","Direct booking for tours, tickets and activities, so a bigger share of sales skips the reseller commission."),
  ("Hotels and vacation rentals","Direct booking sites, guest apps and owner portals for property managers handling dozens of rentals around the parks."),
  ("Events and conventions","Registration, agendas, exhibitor portals and event apps for organizers and the suppliers who serve them."),
  ("Simulation and training companies","Capability sites with technical depth and internal tools for one of the country's simulation and training clusters."),
  ("Healthcare and clinics","Booking, intake and patient communication with HIPAA-conscious handling."),
  ("Home services","Fast sites, scheduling and estimating tools for businesses in Winter Park, Kissimmee, Lake Nona, Sanford and Clermont.")],
 "market":[
  "Orlando's economy runs on visitors, and every booking that goes through a reseller costs 15 to 30 percent. A fast direct-booking site with a good mobile checkout is often the project with the quickest payback in the city.",
  "We quote it fixed, in writing, in stages, at a fraction of a local agency's price. And we build in Spanish as well as English, which matters for a city with a large Hispanic population and visitors from Latin America.",
  "Florida is one of the states where <b>ADA website lawsuits</b> are most frequent, and hospitality sites are a common target. Every site we build follows WCAG 2.1 AA and is tested before launch."],
 "search":[
  "Visitors search by attraction and area — near Disney, International Drive, Lake Buena Vista, Kissimmee — and residents search by town: Winter Park, Lake Nona, Sanford, Oviedo.",
  "For tourism, the narrow door is the experience itself, in the visitor's language: Spanish and Portuguese versions often face little competition.",
  "Structured data for events, tours and lodging earns the rich results that win the click."],
 "faq":[
  ("Can you build direct booking for our tours or rentals?","Yes: availability, payments, deposits, cancellations and reminders, connected to your channel manager where you use one."),
  ("Do you build sites in English, Spanish and Portuguese?","Yes. Each language gets its own URLs, correct hreflang tags and content written for that audience."),
  ("Do you work with Orlando companies from Italy?","Yes. Italy is six hours ahead of Orlando, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["tampa"] = {
 "lead":"We are not in Water Street or Westshore. We are a ten-person web and software team in northern Italy, working in English and Spanish for US companies, six hours ahead of Tampa. Here is what we build for Tampa Bay businesses, what it costs, and when a local firm is the better choice.",
 "sectors":[
  ("Financial services and insurance","Quote and application flows, agent and client portals, and internal tools for the many financial operations based around the bay."),
  ("Healthcare","Booking, intake, patient portals and staff scheduling with HIPAA-conscious hosting."),
  ("Defense and government contractors","Capability sites and internal trackers for companies working with the commands at MacDill."),
  ("Port and logistics","Shipment tracking, warehouse and document workflows for companies working through Port Tampa Bay."),
  ("Real estate and construction","Listing and community sites, buyer portals, daily reports and job costing for a fast-growing region."),
  ("Home services and hospitality","Fast sites and booking for businesses in St. Petersburg, Clearwater, Brandon, Wesley Chapel and Sarasota.")],
 "market":[
  "Tampa Bay grew quickly and much of its business runs on tools that did not grow with it. A focused custom system — a portal, a tracker, a booking flow — often pays for itself within months.",
  "Our quotes are fixed, in writing, in stages, at a fraction of a local agency's, and we work in Spanish as well as English.",
  "Florida sees a high number of <b>ADA website lawsuits</b>. Every site we build follows WCAG 2.1 AA and is tested with keyboard and screen reader before launch."],
 "search":[
  "Tampa Bay is several markets: Tampa, St. Petersburg, Clearwater, Brandon, Wesley Chapel, Sarasota. Local searches carry those names, and Google Business Profile plus area pages win the calls.",
  "Seasonality matters for hospitality and home services — winter visitors, hurricane season. Content timed to the season outperforms generic pages.",
  "For B2B, the narrow pages are where buyers search."],
 "faq":[
  ("Can you build an agent portal for our insurance agency?","Yes: quotes, applications, documents and commissions in one place, connected to your carriers' systems where they offer an API."),
  ("Do you build ADA-accessible websites?","Yes, every site follows WCAG 2.1 AA and is tested before launch."),
  ("Do you work with Tampa companies from Italy?","Yes. Italy is six hours ahead of Tampa, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["las-vegas"] = {
 "lead":"We are not on the Strip. We are a ten-person web and software team in northern Italy, working in English and Spanish for US companies, nine hours ahead of Las Vegas. Here is what we build for Las Vegas businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("Hospitality and entertainment","Direct booking, show and event ticketing flows, VIP and loyalty apps for venues, clubs and restaurants."),
  ("Conventions and trade services","Registration, exhibitor portals, lead capture apps and order systems for the companies that serve the convention business."),
  ("Construction and home builders","Daily reports, job costing, subcontractor scheduling and buyer portals for one of the fastest-growing metros in the West."),
  ("Real estate and property management","Listing sites, owner portals and maintenance apps for portfolios across Henderson, Summerlin and North Las Vegas."),
  ("Healthcare and wellness","Booking, intake and memberships — built with Nevada's consumer health data law in mind."),
  ("Home services","Pool, HVAC, solar and landscaping: fast sites and crew scheduling apps for a market where summer demand spikes.")],
 "market":[
  "Las Vegas businesses are fast-moving and seasonal, and much of their software is improvised: spreadsheets, group texts, three booking tools that do not talk. A focused system built around how the business really runs pays back quickly.",
  "Our quotes are fixed, in writing, in stages, at a fraction of a local agency's price, and we build while you sleep.",
  "Nevada has its own online privacy rules, including a <b>consumer health data law</b> that covers more wellness and fitness apps than most teams expect. We design consent and data handling to match; your counsel confirms how it applies."],
 "search":[
  "The valley searches by area: Henderson, Summerlin, North Las Vegas, Spring Valley, Enterprise. Visitors search by the Strip, Downtown and specific venues.",
  "For hospitality, the battle is often for your own name — make sure your official site, not a reseller, takes the booking.",
  "For home services, seasonality decides everything: pages and campaigns timed to the summer peak."],
 "faq":[
  ("Can you build a VIP or loyalty app for our venue?","Yes: memberships, table and bottle reservations, offers and check-ins, connected to your POS where possible."),
  ("Is a nine-hour time difference workable?","For well-scoped work, yes. Calls go in your early morning, about 7 to 9am Pacific, and we build while you are offline."),
  ("Do you build bilingual English and Spanish sites?","Yes, with separate URLs, correct hreflang tags and content written for each audience.")],
}

C["minneapolis"] = {
 "lead":"We are not in the North Loop. We are a ten-person web and software team in northern Italy, working in English for US companies, seven hours ahead of Minneapolis. Here is what we build for Twin Cities businesses, what it costs, and when a local firm is the better choice.",
 "sectors":[
  ("Medical device and medtech","Product sites with real clinical and technical depth, distributor portals and document control for the Medical Alley cluster."),
  ("Corporate headquarters","Internal tools, approval workflows and reporting dashboards that fill the gap between enterprise systems and how teams work."),
  ("Agribusiness and food","B2B ordering, traceability and dealer portals for food and agriculture companies across the Upper Midwest."),
  ("Healthcare and insurance","Member and patient portals, scheduling and intake, with HIPAA-conscious hosting."),
  ("Manufacturing","Configurators, quoting tools and production tracking for manufacturers across the metro and outstate."),
  ("Local businesses","Fast sites and booking for businesses in St. Paul, Edina, Bloomington, Minnetonka and Maple Grove.")],
 "market":[
  "The Twin Cities have an unusual number of large headquarters for a metro this size, and much of what reaches us is the internal software those companies never get to: the tool a department needs this quarter, not next year.",
  "Our quotes are fixed, in writing, in stages, at a fraction of a local agency's price — and the code ends up in your repository.",
  "Minnesota now has its own privacy law, the <b>Minnesota Consumer Data Privacy Act</b>, with some unusual requirements such as documenting data inventories. We build data handling that makes compliance easier; your counsel confirms the details."],
 "search":[
  "Twin Cities search splits between Minneapolis and St. Paul and then by suburb: Edina, Bloomington, Minnetonka, Eden Prairie, Woodbury, Maple Grove.",
  "For medtech and B2B, search is narrow and technical; precise pages win and get quoted by AI search tools.",
  "Narrow first, broad later."],
 "faq":[
  ("Can you build tools for regulated medtech companies?","Yes, with document control, audit trails and access management. Your quality team defines the requirements; we build to them and document it."),
  ("Can you integrate with SAP, Oracle or Microsoft Dynamics?","Usually, through their APIs or integration layers. We check feasibility on the first call before quoting."),
  ("Do you work with Minneapolis companies from Italy?","Yes, in English. Italy is seven hours ahead of Minneapolis, so calls go in your morning, roughly 8 to 11am Central.")],
}

C["detroit"] = {
 "lead":"We are not in Corktown. We are a ten-person web and software team in northern Italy, working in English for US companies, six hours ahead of Detroit. Here is what we build for Detroit businesses — especially manufacturers and auto suppliers — and when a local firm is the better call.",
 "sectors":[
  ("Automotive suppliers","Supplier portals, quality and PPAP document tracking, production and scrap tracking, and quoting tools for Tier 1 and Tier 2 suppliers."),
  ("Manufacturing","Shop-floor data collection on tablets, maintenance scheduling, configurators and dealer portals."),
  ("Mobility and tech startups","MVPs, marketing sites and internal tools at a fixed price for the city's growing tech scene."),
  ("Healthcare","Booking, intake and patient communication with HIPAA-conscious handling."),
  ("Construction and real estate","Daily reports, job costing and tenant portals for a city that keeps rebuilding."),
  ("Local businesses","Fast sites and ordering for businesses in Royal Oak, Troy, Dearborn, Ann Arbor and Birmingham.")],
 "market":[
  "We come from a manufacturing region ourselves: northern Italy is full of suppliers to the auto and machinery industries. We understand shop floors, quality documents and the spreadsheets that hold production together — and we build software that replaces them.",
  "Quotes are fixed, in writing, in stages, each delivering something usable on the floor, at a fraction of what a local firm typically charges.",
  "Every site we build follows WCAG 2.1 AA accessibility and handles consent properly."],
 "search":[
  "Metro Detroit searches by city: Troy, Southfield, Dearborn, Royal Oak, Novi, Ann Arbor. A strong Google Business Profile and area pages win local calls.",
  "For suppliers, buyers search for capabilities: processes, materials, tolerances, certifications. Precise capability pages win.",
  "Those pages also feed the RFQ: a buyer who finds your exact capability is already halfway to a quote."],
 "faq":[
  ("Can you build a tool to track PPAP and quality documents?","Yes: document control by part and customer, approvals, revisions and expiry alerts, with an audit trail."),
  ("Can you collect production data from the shop floor?","Yes, on tablets at each station, or from machines that expose data. The result feeds dashboards management actually reads."),
  ("Do you work with Detroit companies from Italy?","Yes, in English. Italy is six hours ahead of Detroit, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["portland"] = {
 "lead":"We are not in the Pearl District. We are a ten-person web and software team in northern Italy, working in English for US companies, nine hours ahead of Portland. Here is what we build for Portland businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("Outdoor and athletic brands","E-commerce with real product depth, wholesale portals for retailers, and product configurators."),
  ("Food, beverage and craft brands","Online stores, subscriptions, distributor ordering and taproom or tasting-room booking."),
  ("Semiconductor and tech suppliers","Capability sites, supplier portals and document control for companies serving the region's chip industry."),
  ("Design and creative studios","Portfolio sites that load fast, plus project tracking and client portals."),
  ("Healthcare and wellness","Booking, intake and memberships with HIPAA-conscious handling."),
  ("Local businesses","Fast sites and ordering for businesses in Beaverton, Hillsboro, Lake Oswego, Gresham and Vancouver, WA.")],
 "market":[
  "Portland brands care how things are made, and their customers notice the difference. We build sites that are fast, accessible and honest about the product, at a fixed price that leaves budget for the photography.",
  "Our quotes are fixed, in writing, in stages, at a fraction of a local agency's — and we build while you sleep.",
  "Oregon has its own privacy law, the <b>Oregon Consumer Privacy Act</b>, and California-style consent expectations apply to customers across the West Coast. We build consent and data handling to match."],
 "search":[
  "Portland searches by neighborhood and suburb: Alberta, Hawthorne, the Pearl, Beaverton, Hillsboro, Lake Oswego, and across the river in Vancouver.",
  "For brands, the competition is national and the narrow door is the product: specific, long searches with buying intent.",
  "Product pages with real content and structured data beat thin catalogs every time."],
 "faq":[
  ("Can you build a wholesale portal for retailers?","Yes: account pricing, minimum orders, reorders, invoices and shipment tracking, connected to Shopify or your ERP."),
  ("Is a nine-hour time difference workable?","For well-scoped work, yes. Calls go in your early morning, about 7 to 9am Pacific."),
  ("Do you work with Portland companies from Italy?","Yes, in English, with calls in your morning and the build happening overnight.")],
}

C["raleigh"] = {
 "lead":"We are not in the Research Triangle Park. We are a ten-person web and software team in northern Italy, working in English for US companies, six hours ahead of Raleigh. Here is what we build for Triangle businesses, what it costs, and when a local firm is the better choice.",
 "sectors":[
  ("Life sciences and CROs","Sites that explain the science to sponsors and investors, plus sample tracking, scheduling and data intake tools."),
  ("Tech and SaaS","Marketing sites, internal tools and integrations, so engineers stay on the product."),
  ("Universities and research spin-offs","Lab and program sites, MVPs for spin-off companies, and tools that replace shared spreadsheets."),
  ("Healthcare","Booking, intake and patient communication with HIPAA-conscious hosting."),
  ("Construction and real estate","Daily reports, job costing and buyer portals for one of the fastest-growing regions in the Southeast."),
  ("Local businesses","Fast sites and booking for businesses in Durham, Cary, Chapel Hill, Apex and Wake Forest.")],
 "market":[
  "The Triangle has a deep pool of scientific and technical companies, and a thinner pool of affordable development teams. That gap is where we fit: fixed price, written scope, code in your repository.",
  "Our quotes are a fraction of a local agency's for the same scope — because our overhead is low, not because we cut hours.",
  "Every site we build follows WCAG 2.1 AA accessibility, which also matters for anything connected to universities or public funding."],
 "search":[
  "Triangle search splits by city: Raleigh, Durham, Cary, Chapel Hill, Apex, Morrisville. A Google Business Profile and area pages win local calls.",
  "For life sciences and tech, search is national and technical; precise pages win and get cited by AI search tools.",
  "Narrow first, broad later."],
 "faq":[
  ("Can you build an MVP for a university spin-off?","Yes, at a fixed price, cut to the smallest version that tests the idea, on mainstream technology your future team can take over."),
  ("Do you build HIPAA-conscious tools?","Yes, with BAA-backed hosting, encryption, access logs and minimal data collection."),
  ("Do you work with Raleigh companies from Italy?","Yes, in English. Italy is six hours ahead of Raleigh, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["salt-lake-city"] = {
 "lead":"We are not in Lehi. We are a ten-person web and software team in northern Italy, working in English for US companies, eight hours ahead of Salt Lake City. Here is what we build for Utah businesses, what it costs, and when a local agency is the better call.",
 "sectors":[
  ("SaaS companies","Marketing sites, documentation and internal tools for the Silicon Slopes, so engineers stay on the product."),
  ("Direct sales and e-commerce brands","Online stores, rep portals, commissions tracking and subscriptions."),
  ("Outdoor and recreation","E-commerce, rentals and booking for brands and outfitters near the Wasatch."),
  ("Healthcare","Booking, intake and patient communication with HIPAA-conscious handling."),
  ("Construction and home services","Estimating, scheduling and crew apps for a region that keeps growing along I-15."),
  ("Local businesses","Fast sites and booking for businesses in Provo, Ogden, Sandy, West Jordan and Park City.")],
 "market":[
  "Utah's tech salaries have climbed with the Silicon Slopes, and local development rates followed. For a marketing site, an internal tool or a rep portal, that premium rarely buys anything you need.",
  "Fixed price, written scope, in stages, at a fraction of a local agency's quote.",
  "Utah has its own privacy law, the <b>Utah Consumer Privacy Act</b>. We build consent and data handling to match; your counsel confirms how it applies."],
 "search":[
  "The Wasatch Front searches by city: Salt Lake City, Provo, Orem, Lehi, Sandy, Ogden, Park City.",
  "For SaaS, search is national: comparisons, alternatives, integrations, use cases.",
  "For outdoor brands and outfitters, seasonal and activity-specific pages win."],
 "faq":[
  ("Can you build a portal for our sales reps?","Yes: orders, downline or territory views, commissions and training content, connected to your store and payment provider."),
  ("How does the time difference work?","Italy is eight hours ahead of Salt Lake City. Calls go in your early morning, roughly 7 to 10am Mountain."),
  ("Do you work with Utah companies from Italy?","Yes, in English, with calls in your morning and the build happening overnight.")],
}

C["columbus"] = {
 "lead":"We are not in the Short North. We are a ten-person web and software team in northern Italy, working in English for US companies, six hours ahead of Columbus. Here is what we build for Columbus businesses, what it costs, and when a local firm is the better choice.",
 "sectors":[
  ("Insurance and financial services","Quote flows, agent and policyholder portals, and internal tools for one of the country's insurance centers."),
  ("Logistics and distribution","Order tracking, warehouse and driver apps for a region within a day's drive of much of the US population."),
  ("Retail and consumer brands","E-commerce, wholesale portals and internal tools for brands headquartered in the region."),
  ("Healthcare","Booking, intake and patient communication with HIPAA-conscious hosting."),
  ("Manufacturing and tech suppliers","Capability sites, supplier portals and production tracking for the region's growing industrial base."),
  ("Local businesses","Fast sites and booking for businesses in Dublin, Westerville, Grandview, Hilliard and New Albany.")],
 "market":[
  "Columbus is practical and growing, and much of what reaches us is operational: a portal for agents, a tracker for the warehouse, an integration between systems that should already talk.",
  "We quote it fixed, in writing, in stages, at a fraction of a local agency's price.",
  "Every site we build follows WCAG 2.1 AA accessibility and handles consent properly."],
 "search":[
  "Central Ohio searches by suburb: Dublin, Westerville, Hilliard, Grandview, Worthington, New Albany.",
  "For insurance and logistics companies, the narrow pages — the specific product, the specific lane or service — win.",
  "Narrow first, broad later."],
 "faq":[
  ("Can you build a policyholder or agent portal?","Yes: documents, payments, claims status and messaging, connected to your policy system where it offers an API."),
  ("Can you integrate with our WMS?","Usually. If it has an API or reliable export, we can connect it; we check before quoting."),
  ("Do you work with Columbus companies from Italy?","Yes, in English. Italy is six hours ahead of Columbus, so calls go in your morning, between about 9am and noon Eastern.")],
}

C["kansas-city"] = {
 "lead":"We are not in the Crossroads. We are a ten-person web and software team in northern Italy, working in English for US companies, seven hours ahead of Kansas City. Here is what we build for businesses on both sides of the state line, what it costs, and when a local firm is the better call.",
 "sectors":[
  ("Logistics and rail","Kansas City is one of the country's big rail and freight hubs: shipment tracking, dispatch and driver apps, dock scheduling and integrations."),
  ("Engineering and architecture firms","Project portals, document control and resource scheduling for firms managing projects across the country."),
  ("Animal health and agribusiness","Product and distributor portals, traceability and technical sites for companies in the animal health corridor."),
  ("Restaurants and food brands","Online ordering, catering requests, wholesale ordering and shipping for barbecue and food brands that sell nationwide."),
  ("Healthcare","Booking, intake and patient communication with HIPAA-conscious hosting."),
  ("Home services","Fast sites and scheduling tools for businesses in Overland Park, Olathe, Lee's Summit, Independence and Lenexa.")],
 "market":[
  "Kansas City businesses tend to be operational and practical, and so is most of what we build here: tools that cut hours of retyping, portals that stop the phone ringing, and sites that bring real enquiries.",
  "Quotes are fixed, written and in stages, at a fraction of a local agency's price.",
  "Every site we build follows WCAG 2.1 AA accessibility and handles consent properly."],
 "search":[
  "The metro straddles two states, and local searches carry suburb names: Overland Park, Olathe, Lenexa, Lee's Summit, Independence, North Kansas City.",
  "For logistics and engineering firms, search is national and narrow: the specific service, region or project type.",
  "For food brands shipping nationwide, product pages with real content and structured data win."],
 "faq":[
  ("Can you build dispatch and tracking tools for our freight business?","Yes: loads, routes, proof of delivery with photo and signature, and live status for customers, integrated with your TMS and accounting."),
  ("Can you set up nationwide shipping for our food brand?","Yes: shipping zones and rules, perishable handling options, subscriptions and gift orders, with sales tax configured correctly."),
  ("Do you work with Kansas City companies from Italy?","Yes, in English. Italy is seven hours ahead of Kansas City, so calls go in your morning, roughly 8 to 11am Central.")],
}

# ---------------------------------------------------------------------------
def pagina_citta(slug, city, state, tz):
    c = C[slug]
    # Titoli sulle ricerche con volume reale: "web design company <citta>", "website design <citta>"
    title = "%s Web Design Company | Website Design & Apps" % city
    if len(title) > 60: title = "%s Web Design Company | Website Design" % city
    h1 = "Web design company<br>for <span class=\"grad\">%s businesses.</span>" % city
    desc = ("Website design, e-commerce and mobile apps for %s businesses: fixed price agreed upfront, "
            "ADA-accessible, live in weeks, code in your name." % city)
    altri = []
    if slug in SW_CITTA:
        altri.append(("App &amp; software development %s" % city, "/en/software-development-%s/" % slug))
    altri += altri_citta(slug, 5) + ALTRI_BASE
    secs = [servizi_cards(city),
            {"id":"sectors","tipo":"cards","eyebrow":"%s industries" % city,
             "h2":"What we build<br>for <span class=\"grad\">%s</span>" % city,
             "lead":"Every city has its own mix of businesses, and its own software problems. These are the ones we see most from %s." % city,
             "corpo":c["sectors"]},
            {"id":"market","tipo":"testo","eyebrow":"The commercial reality",
             "h2":"Why a team in Italy<br>makes sense <span class=\"grad\">for %s</span>" % city,
             "corpo":c["market"]},
            {"id":"timezone","tipo":"testo","eyebrow":"Honestly",
             "h2":"Time zones, contracts,<br>and when <span class=\"grad\">we are the wrong choice</span>",
             "corpo":[tz_par(tz, city),
                      "The paperwork is simple: contracts in English, a fixed price in writing, invoices without Italian VAT, and intellectual property assigned to your company. Domain, hosting, Google accounts and source code are registered in your name from launch.",
                      "<b>When we are the wrong choice.</b> If you need someone in your office every week, a supplier on chat through your whole afternoon, or a team of fifteen running in parallel on a seven-figure program, a %s firm is the right answer — and we will tell you that on the first call rather than three months in." % city]},
            {"id":"search","tipo":"testo","eyebrow":"Getting found",
             "h2":"%s search:<br>enter through <span class=\"grad\">the narrow door.</span>" % city,
             "corpo":c["search"]},
            metodo()]
    return {
     "lang":"en", "url":"/en/web-design-%s/" % slug,
     "title":title, "desc":desc,
     "ogtitle":"Web design & apps for %s — Danova Tech" % city,
     "ogdesc":"Websites, mobile apps and custom business software for %s companies, built by a ten-person team at a fixed price. You own the domain and the code." % city,
     "crumbs":[("United States","/en/united-states/"),(city,None)],
     "eyebrow":("New York City" if slug == "new-york" else "%s, %s" % (city, state)),
     "h1":h1, "lead":c["lead"],
     "cta1":"Book a free call", "cta2":"What we build",
     "sezioni":secs,
     "faqtitle":"The questions from <span class=\"grad\">%s.</span>" % city,
     "faq":c["faq"] + [faq_comuni(city, tz)[i] for i in (0, 1, 4)],
     "ctabox":ctabox(city),
     "altrititle":"Related pages",
     "altri":altri,
     "svc":{"name":"Web design, app and software development for %s" % city,
            "type":"Website, e-commerce, mobile app and custom software development",
            "desc":"Websites, online stores, mobile apps, client portals and custom business software for companies in %s, %s. Fixed price agreed before work starts, built to WCAG 2.1 AA, domain and source code registered in the client's name." % (city, state),
            "area":area(city, state),"lingue":["English","Spanish","Italian"],
            "catalogo":["Company website","E-commerce store","Mobile app development","Custom business software","CRM and client portals","Integrations and automation","Search engine optimization"]},
    }

for slug, city, state, tz in CITTA:
    PAGINE.append(pagina_citta(slug, city, state, tz))

# ---------------------------------------------------------------------------
# Seconda pagina per NY, LA, Chicago: software e app
SW = {
 "new-york":{
  "lead":"New York companies pay New York rates for software that, more often than not, is an internal tool, a portal or an app built on mainstream technology. We are a ten-person team in northern Italy that builds exactly that, at a fixed price, with the code in your repository.",
  "cards":[
   ("Client and investor portals","Documents, statements, case status and messaging in one secure place, replacing email attachments and shared folders. Common for law firms, wealth managers and real estate operators."),
   ("Internal operations tools","Approvals, scheduling, inventory, reporting: the workflows currently held together by spreadsheets and one person who knows how they work."),
   ("Mobile apps for customers","Ordering, booking, loyalty and memberships for restaurant groups, studios, clinics and retailers with several locations across the boroughs."),
   ("Field and property apps","Work orders, inspections and maintenance requests for property managers and contractors moving between buildings all day."),
   ("Integrations","QuickBooks, Salesforce, HubSpot, Shopify, Yardi, your bank feed — connected so data moves without anyone retyping it."),
   ("Custom CRM and ERP","When off-the-shelf tools force your team to work their way instead of yours: a system built around your process, with data migrated from what you use today.")]},
 "los-angeles":{
  "lead":"Los Angeles runs on brands, production schedules and logistics — and on a lot of software that is really an internal tool or an app with a clear job. We are a ten-person team in northern Italy that builds exactly that, at a fixed price, while you sleep.",
  "cards":[
   ("Customer apps for brands","Loyalty, subscriptions, drops and ordering apps that give DTC and beauty brands a direct line to customers, outside marketplace algorithms."),
   ("Production and project tracking","Schedules, assets, approvals and budgets for studios and agencies that currently run on spreadsheets, shared drives and group texts."),
   ("Wholesale and B2B portals","Buyers place orders, see their prices, reorder and track shipments themselves — for apparel, beauty and food brands selling to retailers."),
   ("Logistics and warehouse tools","Inventory, picking, shipment tracking and customs document workflows around the ports and the Inland Empire."),
   ("Booking and membership apps","Classes, treatments, appointments and memberships for studios, clinics and wellness brands across the city."),
   ("Integrations","Shopify, your 3PL, QuickBooks, Klaviyo, Airtable — connected so orders and stock move on their own.")]},
 "chicago":{
  "lead":"Chicago companies want software that pays for itself: fewer hours retyping, fewer errors, faster quotes. We are a ten-person team in northern Italy that builds custom business software and apps at a fixed price, in stages, with the code in your name.",
  "cards":[
   ("Dispatch and driver apps","Loads, routes, proof of delivery with photo and signature, and live status for customers — for carriers, brokers and distributors."),
   ("Quoting and configurators","Turn a two-day quote into a two-minute one: product rules, pricing and PDF output in a tool your sales team and dealers can use."),
   ("Shop-floor and production tracking","Work orders, machine status, scrap and time per job on tablets on the floor, feeding the reporting management actually reads."),
   ("Dealer and distributor portals","Orders, price lists, documents and warranty claims in a portal your partners use themselves instead of calling."),
   ("Time tracking and field apps","Crew time, job reports and photos — designed to keep biometrics out unless you truly need them, given Illinois' BIPA."),
   ("ERP extensions and integrations","Keep the system you have and add what it is missing: a web interface, a mobile app, a connection to e-commerce or accounting.")]},
 "dallas":{
  "lead":"Dallas–Fort Worth searches for mobile app developers more than almost any metro in the country, and local agency quotes reflect that demand. We are a ten-person team in northern Italy that builds mobile apps and custom software at a fixed price, in stages, with the code in your repository.",
  "cards":[
   ("Customer apps for franchises","Ordering, booking, loyalty and offers across every location, with reporting per store and one codebase for iOS and Android."),
   ("Field and service apps","Jobs, routes, photos, signatures and invoices for HVAC, roofing, pest control and property service crews across the Metroplex."),
   ("Internal tools for HQ teams","Approval flows, dashboards and request portals that sit next to Salesforce, SAP or Microsoft 365 instead of waiting for the IT roadmap."),
   ("Logistics and distribution apps","Order tracking, warehouse scanning and driver apps for the distribution centers around DFW."),
   ("Real estate and construction tools","Investor portals, daily reports, job costing and subcontractor scheduling for builders working north toward Frisco and McKinney."),
   ("Integrations","Salesforce, HubSpot, QuickBooks, Shopify and your ERP connected so data moves without anyone retyping it.")]},
 "houston":{
  "lead":"Houston's software problems are industrial: crews in the field, equipment to maintain, paperwork that has to be right. We are a ten-person team in northern Italy that builds the apps and systems that fix them — offline-ready, at a fixed price, in stages.",
  "cards":[
   ("Field ticket and inspection apps","Tablets that work offline at the well site or plant, with photos, signatures and GPS, synced to the office when signal returns."),
   ("Asset and maintenance tracking","Equipment registers, preventive schedules, work orders and spare parts, with QR codes on every asset."),
   ("Safety and contractor onboarding","Training records, certifications with expiry alerts, permits and incident reports in one place."),
   ("Construction tools","Estimating, daily reports, crew time and job costing for contractors across the Greater Houston area."),
   ("Patient and clinic apps","Booking, intake and reminders for clinics and practices, built with HIPAA-conscious hosting."),
   ("Bilingual customer apps","English and Spanish apps for service businesses whose customers prefer Spanish.")]},
 "miami":{
  "lead":"Miami businesses sell across languages and borders, and their apps have to as well. We are a ten-person team in northern Italy that builds multilingual mobile apps and custom software — English, Spanish, Portuguese, Italian — at a fixed price, in stages.",
  "cards":[
   ("Real estate apps and portals","Pre-construction availability, buyer and investor portals, broker tools and CRM integrations, in several languages."),
   ("Hospitality and nightlife apps","Reservations, VIP tables, loyalty and offers for restaurants, clubs and hotels."),
   ("Trade and logistics portals","B2B ordering, shipment tracking and document workflows for importers, exporters and forwarders working with Latin America."),
   ("Wellness and aesthetics apps","Booking, memberships, packages and before-and-after galleries with careful handling of health data."),
   ("Fintech and wealth tools","Client onboarding, document vaults and reporting dashboards with encryption and audit logs."),
   ("Multilingual by design","Every screen built for English and Spanish from the start, with Portuguese or Italian added without a rewrite.")]},
 "atlanta":{
  "lead":"Atlanta runs on logistics, payments and headquarters operations, and so do most of the apps we build here. We are a ten-person team in northern Italy that builds mobile apps and custom software at a fixed price, in stages, with the code in your name.",
  "cards":[
   ("Logistics and warehouse apps","Scanning, picking, inventory and shipment tracking for distribution operations around the airport and the I-85 corridor."),
   ("Driver and delivery apps","Routes, proof of delivery with photo and signature, and live status for customers."),
   ("Fintech and payments tools","Merchant onboarding, partner portals and internal dashboards around your core platform."),
   ("Production and studio tools","Crew, location and asset scheduling for film and TV production services."),
   ("Internal tools for corporate teams","Requests, approvals and reporting that fill the gap between enterprise systems and real workflows."),
   ("Integrations","WMS, TMS, QuickBooks, Salesforce and Stripe connected so data moves on its own.")]},
 "austin":{
  "lead":"Austin startups need to ship before the runway runs out, and established companies need tools their engineers never get to. We are a ten-person team in northern Italy that builds MVPs, mobile apps and internal software at a fixed price, on mainstream technology.",
  "cards":[
   ("MVPs","A first web or mobile version in six to ten weeks, cut to what tests the idea, with code your future team will be happy to inherit."),
   ("Mobile apps","iOS and Android with React Native or native code, store publishing under your accounts, analytics tied to your hypotheses."),
   ("Internal tools","Admin panels, ops dashboards and support tooling, so engineers stay on the product."),
   ("Booking and event apps","Ticketing, reservations and loyalty for venues and hospitality."),
   ("Construction and real estate tools","Daily reports, buyer portals and job costing for builders around the fast-growing suburbs."),
   ("Integrations","Stripe, HubSpot, Salesforce, Notion and your data warehouse connected without a person in the middle.")]},
 "san-francisco":{
  "lead":"Bay Area engineering time should go to your product. We are a ten-person team in northern Italy that builds the apps and software around it — MVPs, internal tools, integrations, companion apps — at a fixed price, with code in your GitHub from the first commit.",
  "cards":[
   ("MVPs and prototypes","A first version for users and investors in weeks, at a fixed price, on TypeScript, React, Node or Python."),
   ("Companion mobile apps","iOS and Android apps for an existing SaaS product, sharing its API and design system."),
   ("Internal tools","Admin panels, ops dashboards, onboarding and support tooling that no roadmap prioritizes."),
   ("Integrations","Stripe, Salesforce, HubSpot, Segment, your warehouse — built, tested and documented."),
   ("Biotech lab tools","Sample tracking, scheduling and data intake for life sciences teams that outgrew spreadsheets."),
   ("Legacy rescue","Taking over code another vendor started, assessing it honestly and finishing or rebuilding it.")]},
 "denver":{
  "lead":"Denver companies tend to work outdoors, in the field or on job sites, and their software has to work there too. We are a ten-person team in northern Italy that builds mobile apps and custom software at a fixed price, in stages, offline-ready where it matters.",
  "cards":[
   ("Field service and energy apps","Inspections, work orders and maintenance logs that work without signal across the Front Range and beyond."),
   ("Construction tools","Daily reports, job costing and subcontractor scheduling for builders across the metro."),
   ("Rental and booking apps","Gear rentals, guided trips and reservations for outdoor and recreation businesses."),
   ("Healthcare and wellness apps","Booking, memberships and intake with HIPAA-conscious handling and Colorado privacy rules in mind."),
   ("Aerospace supplier tools","RFQ workflows, document control and supplier portals."),
   ("Integrations","QuickBooks, Shopify, your CRM and ERP connected so nobody retypes data.")]},
 "orlando":{
  "lead":"Orlando sells experiences, and every booking that goes through a reseller costs margin. We are a ten-person team in northern Italy that builds booking apps, guest apps and custom software for tourism, hospitality and events — in English, Spanish and Portuguese — at a fixed price.",
  "cards":[
   ("Direct booking apps","Tours, tickets, activities and rentals with availability, deposits, cancellations and reminders."),
   ("Guest and visitor apps","Itineraries, offers, maps and check-in for hotels, vacation rentals and attractions."),
   ("Event and convention apps","Registration, agendas, exhibitor portals and lead capture for organizers and suppliers."),
   ("Vacation rental owner portals","Statements, bookings and maintenance requests for property managers with dozens of homes."),
   ("Simulation and training tools","Internal tools and portals for the region's simulation and training companies."),
   ("Multilingual by design","English, Spanish and Portuguese from the start, for visitors and residents alike.")]},
}

def pagina_sw(slug):
    city = NOME[slug]; state = [s for x,_,s,_ in CITTA if x == slug][0]
    tz = [t for x,_,_,t in CITTA if x == slug][0]
    s = SW[slug]
    return {
     "lang":"en", "url":"/en/software-development-%s/" % slug,
     "title":"App Development Company in %s | Custom Software" % city,
     "desc":"Mobile app development and custom software for %s businesses: fixed price per stage, first version live in 4-8 weeks, code in your repository." % city,
     "ogtitle":"Software & app development for %s — Danova Tech" % city,
     "ogdesc":"Custom business software, mobile apps and integrations for %s companies, built in stages at a fixed price by a ten-person team. You own the code." % city,
     "crumbs":[("United States","/en/united-states/"),(city,"/en/web-design-%s/" % slug),("Software and apps",None)],
     "eyebrow":"%s · Software & apps" % city,
     "h1":"App and software development<br>for <span class=\"grad\">%s businesses.</span>" % city,
     "lead":s["lead"],
     "cta1":"Book a free call", "cta2":"What we build",
     "sezioni":[
      {"id":"build","tipo":"cards","eyebrow":"What we build",
       "h2":"The software %s companies<br><span class=\"grad\">actually ask for</span>" % city,
       "lead":"Very little of it is glamorous. Almost all of it saves hours every week.",
       "corpo":s["cards"]},
      {"id":"stages","tipo":"testo","eyebrow":"How projects are structured",
       "h2":"In stages,<br>so you <span class=\"grad\">can stop.</span>",
       "corpo":[
        "The most common way a custom software project fails is that everything gets specified at once and then built for a year. What arrives matches the specification and no longer matches the business, because twelve months have passed.",
        "We cut it differently. The part that removes the most wasted time goes live first, usually within four to eight weeks. Then we measure what it actually saved, and only then decide the next stage. Each stage has its own fixed price and produces something that works on its own.",
        "That has an awkward consequence for us: you can stop after any stage and keep everything built so far. We think that is the right incentive — it forces the value to arrive early instead of at the end.",
        "Custom business software starts from €1,500; web apps start at €50 a month or €750 one-off. Every quote is fixed and in writing before work starts."]},
      {"id":"stack","tipo":"cards","eyebrow":"Under the hood",
       "h2":"Mainstream technology,<br><span class=\"grad\">your</span> repository",
       "lead":"Nothing exotic, nothing proprietary. Any competent developer you hire later can pick it up.",
       "corpo":[
        ("Web apps","TypeScript, React or Vue, Node or Python, PostgreSQL. Works in any browser on desktop, tablet and phone."),
        ("Mobile apps","Native iOS and Android, or React Native and Flutter when one codebase serves both. Installable web apps when the stores add nothing."),
        ("Offline first","Field apps store data on the device and sync when the signal comes back — basements, warehouses, job sites, rural routes."),
        ("Security by default","Encryption in transit and at rest, roles and permissions, audit logs, backups. HIPAA-conscious hosting when health data is involved."),
        ("Hosting you control","AWS, Google Cloud, Azure or your existing provider, under your account. We can manage it, but you hold the keys."),
        ("Documentation","Code comments, setup guide and an architecture overview in English, written for the next developer rather than for us.")]},
      {"id":"timezone","tipo":"testo","eyebrow":"Honestly",
       "h2":"Working from Italy,<br>and when <span class=\"grad\">it does not fit</span>",
       "corpo":[tz_par(tz, city),
                "Contracts are in English, intellectual property is assigned to your company, and invoices carry no Italian VAT. The code lives in your repository from the first commit.",
                "<b>When we are the wrong choice.</b> If you need developers embedded in your office, or a large team on a multi-year program with daily stand-ups at 2pm your time, a %s firm fits better. We will say so on the first call." % city]},
      metodo()],
     "faqtitle":"Software questions from <span class=\"grad\">%s.</span>" % city,
     "faq":[
      ("How much does custom software cost?","Custom business software starts from €1,500 for a focused first stage. A typical internal tool or portal lands in the low five figures in euros across its stages; a large ERP-style system more. Every stage gets a fixed price in writing after a free analysis."),
      ("Native app or web app?","If your users are your own staff or clients who log in, a web app installed on the home screen usually does the job at a lower cost. If you need app store presence, push notifications on iOS, or deep device features, go native. We tell you which on the first call."),
      ("Can you take over software another developer started?","Yes. We review the code first and tell you honestly whether continuing or rebuilding is cheaper — and why."),
      ("Who owns the code?","You do. It lives in your repository, intellectual property is assigned to your company in the contract, and there is no license tied to us."),
     ] + faq_comuni(city, tz)[1:4],
     "ctabox":{"h2":"Software project in %s?" % city,
               "p":"Thirty minutes on a call: we look at the problem, tell you what the first useful stage would be, what it costs and how long it takes.",
               "btn":"Book a free call"},
     "altrititle":"Related pages",
     "altri":[("Web design %s" % city,"/en/web-design-%s/" % slug)] +
             [("App &amp; software development %s" % NOME[x],"/en/software-development-%s/" % x) for x in SW_CITTA if x != slug][:5] +
             ALTRI_BASE,
     "svc":{"name":"Software and app development for %s" % city,
            "type":"Custom software, mobile app and integration development",
            "desc":"Custom business software, mobile apps, client portals and system integrations for companies in %s, %s. Built in stages with a fixed price per stage, code in the client's repository." % (city, state),
            "area":area(city, state),"lingue":["English","Spanish","Italian"],
            "catalogo":["Custom business software","Mobile app development","Web applications","Client portals","System integrations","ERP and CRM extensions"]},
    }

for slug in SW_CITTA:
    PAGINE.append(pagina_sw(slug))

# ---------------------------------------------------------------------------
# Hub e servizi a livello nazionale
def lista_citta_html():
    return "<br>".join("<b>%s:</b> " % r + " · ".join('<a href="/en/web-design-%s/">%s</a>' % (s, NOME[s]) for s in ss)
                       for r, ss in REGIONI)

def lista_link_html(lst):
    return " · ".join('<a href="%s">%s</a>' % (u, t) for t, u in lst)

AREA_US = [US]
CITTA_ALTRI = [("Web design %s" % n, "/en/web-design-%s/" % s) for s,n,_,_ in CITTA]

PAGINE.append({
 "lang":"en", "url":"/en/united-states/",
 "title":"Web, App & Software Development for US Businesses",
 "desc":"Websites, mobile apps and custom business software for US companies from New York to Los Angeles. Fixed price, ADA-accessible, code in your name.",
 "ogtitle":"Danova Tech for US businesses",
 "ogdesc":"A ten-person web and software team in Italy building websites, apps and business systems for US companies at a fixed price.",
 "crumbs":[("United States",None)],
 "eyebrow":"United States",
 "h1":"Websites, apps and software<br>for <span class=\"grad\">US businesses.</span>",
 "lead":"We are a ten-person web and software team based in northern Italy, working in English for companies across the United States. Fixed prices in writing, accessible sites, code in your name — at a fraction of what a big-city US agency charges, because our overhead is a fraction of theirs.",
 "cta1":"Book a free call", "cta2":"What we do",
 "sezioni":[
  servizi_cards("US"),
  {"id":"cities","tipo":"testo","eyebrow":"Where we work",
   "h2":"From New York<br>to <span class=\"grad\">Los Angeles</span>",
   "corpo":[
    "We work remotely with companies anywhere in the country. For the metros we hear from most, we have written a page about the local market, the industries, the search landscape and the legal details that matter there:",
    lista_citta_html(),
    "Mobile app and custom software development, city by city: " + " · ".join('<a href="/en/software-development-%s/">%s</a>' % (x, NOME[x]) for x in SW_CITTA) + ".",
    "Not on the list? It makes no difference to how we work. Calls are scheduled in your morning, which is our afternoon, and the build happens while you are offline."]},
  {"id":"industries","tipo":"testo","eyebrow":"By industry",
   "h2":"Built for <span class=\"grad\">your industry</span>",
   "corpo":["Most of what we build is specific to a kind of business: the intake flow a law firm needs, the dispatch app a carrier needs, the wholesale portal a brand needs. These pages go into detail:",
            lista_link_html(INDUSTRIE)]},
  {"id":"specific","tipo":"testo","eyebrow":"Specific services",
   "h2":"What people<br><span class=\"grad\">ask us for</span>",
   "corpo":["The services US companies search for most, each with its own page:",
            lista_link_html(EXTRA)]},
  {"id":"guides","tipo":"testo","eyebrow":"Before you buy",
   "h2":"Straight answers<br>on <span class=\"grad\">cost and compliance</span>",
   "corpo":["What things really cost, which US rules apply to your website, and how working with a team in Europe compares with onshore and offshore options:",
            lista_link_html(GUIDE)]},
  {"id":"why","tipo":"testo","eyebrow":"The commercial reality",
   "h2":"US agency prices<br>are a <span class=\"grad\">structure cost.</span>",
   "corpo":[
    "A US agency in a major city carries big-city rent, big-city salaries and an account team between you and the people doing the work. That is a legitimate cost of doing business, and it ends up in your quote.",
    "We are a small team with low fixed costs. For the same work the quote is a fraction of a typical US agency's — a company website from €350, custom business software from €1,500 — and not because we cut hours. You talk directly to the person building your project.",
    "We also build to the US rules that matter: <b>WCAG 2.1 AA accessibility</b> on every site, given how many ADA website claims are filed each year; consent and data handling that respect state privacy laws like California's CCPA/CPRA, Texas' TDPSA and Colorado's CPA; and HIPAA-conscious hosting when health data is involved. Your counsel signs off on policy; we make sure the site actually does what the policy says.",
    "<b>When we are the wrong choice.</b> If you need someone in your office, a supplier on chat all afternoon, or a large team on a multi-year program, a local firm fits better, and we will say so on the first call."]},
  metodo()],
 "faqtitle":"Questions from <span class=\"grad\">US companies.</span>",
 "faq":faq_comuni("your city", "ET")[:1] + [
  ("How do the time zones work?","Italy is six hours ahead of the East Coast, seven of Central time, eight of Mountain and nine of the West Coast. Calls go in your morning, our afternoon; we build while you are offline, so feedback sent in the evening often becomes a new version by morning."),
  ("Do you build ADA-accessible websites?","Yes, every site follows WCAG 2.1 AA and is tested with keyboard navigation and screen readers before launch. No one can guarantee you will never receive a demand letter, but an accessible site gives a claim very little to work with."),
  ("Do you work in Spanish too?","Yes. We work in English, Spanish, Italian, French and German, and build multilingual sites properly — separate URLs, correct hreflang tags, content written for each audience."),
 ] + faq_comuni("your city", "ET")[2:],
 "ctabox":ctabox("the US"),
 "altrititle":"US cities and services",
 "altri":[x for x in ALTRI_BASE if x[1] != "/en/united-states/"] + CITTA_ALTRI,
 "svc":{"name":"Web, app and software development for US businesses",
        "type":"Website, e-commerce, mobile app and custom software development",
        "desc":"Websites, online stores, mobile apps, client portals and custom business software for companies across the United States. Fixed price agreed before work starts, built to WCAG 2.1 AA, domain and source code registered in the client's name.",
        "area":AREA_US,"lingue":["English","Spanish","Italian"],
        "catalogo":["Company website","E-commerce store","Mobile app development","Custom business software","CRM and client portals","Integrations and automation","Search engine optimization"]},
})

def hub(url, title, desc, ogtitle, ogdesc, eyebrow, h1, lead, sezioni, faq, svc_name, svc_type, svc_desc, catalogo, altri_first):
    return {
     "lang":"en","url":url,"title":title,"desc":desc,"ogtitle":ogtitle,"ogdesc":ogdesc,
     "crumbs":[("United States","/en/united-states/"),(eyebrow,None)],
     "eyebrow":eyebrow,"h1":h1,"lead":lead,
     "cta1":"Book a free call","cta2":"What we build",
     "sezioni":sezioni + [
       {"id":"cities","tipo":"testo","eyebrow":"Across the country",
        "h2":"City by <span class=\"grad\">city</span>",
        "corpo":["We work with companies anywhere in the US. For the metros we hear from most, there is a page on the local market, industries and search landscape:",
                 lista_citta_html()]},
       metodo()],
     "faqtitle":"The questions we <span class=\"grad\">always get.</span>",
     "faq":faq + [faq_comuni("your city","ET")[i] for i in (0,2,3,4)],
     "ctabox":ctabox("the US"),
     "altrititle":"Related pages",
     "altri":[x for x in ALTRI_BASE if x[1] != url] + altri_first,
     "svc":{"name":svc_name,"type":svc_type,"desc":svc_desc,"area":AREA_US,
            "lingue":["English","Spanish","Italian"],"catalogo":catalogo},
    }

PAGINE.append(hub(
 "/en/web-design-agency-usa/",
 "Web Design Company USA | Website Design & Development",
 "Website design and development for US businesses: from €350, fixed price agreed upfront, built to WCAG 2.1 AA, live in 2-8 weeks, code in your name.",
 "Web design agency for US businesses — Danova Tech",
 "Company websites and e-commerce for US businesses, built by a ten-person team in Italy at a fixed price.",
 "Web design",
 "Web design company<br>for <span class=\"grad\">US businesses.</span>",
 "A website from €350, or €24.80 a month with hosting and changes included. Fast on a phone, accessible to WCAG 2.1 AA, written around what your customers actually search for — and registered in your company's name.",
 [servizi_cards("US"),
  {"id":"standards","tipo":"cards","eyebrow":"Included in every site",
   "h2":"What every site gets,<br><span class=\"grad\">without asking</span>",
   "corpo":[
    ("Accessibility to WCAG 2.1 AA","Contrast, keyboard navigation, labels, alt text, screen-reader testing — the standard referenced in ADA website cases."),
    ("Speed","Pages that pass Core Web Vitals on a mid-range phone on a cellular connection, because that is where most of your visitors are."),
    ("Search foundations","Clean structure, titles, structured data, sitemap and indexing on Google and Bing, plus Google Business Profile setup for local businesses."),
    ("Privacy and consent","A consent banner that actually blocks trackers until consent, forms that collect only what you need, opt-out links where state laws require them."),
    ("Readable by AI search","Clear answers, structured data and an llms.txt file, so ChatGPT, Perplexity and Google's AI answers can understand and cite you."),
    ("Ownership","Domain, hosting, Google accounts and source code in your company's name. No license tied to us.")]}],
 [("Do you use WordPress?","When it fits — mainly when your team wants to edit lots of content themselves. Otherwise we build lighter, faster sites that are cheaper to host and harder to hack. Either way, you can change text and images yourself.")],
 "Web design and development for US businesses","Website and e-commerce design and development",
 "Company websites and online stores for businesses across the United States: fixed price, WCAG 2.1 AA accessibility, search foundations, domain and code registered in the client's name.",
 ["Company website","E-commerce store","Website redesign and migration","Landing pages","Search engine optimization","Website maintenance"],
 CITTA_ALTRI[:8]))

PAGINE.append(hub(
 "/en/software-development-company-usa/",
 "Custom Software Development Company for US Businesses",
 "Custom software, web apps and integrations for US companies: fixed price per stage, first version live in 4-8 weeks, code in your repository. From €1,500.",
 "Software development for US businesses — Danova Tech",
 "Custom business software, web apps and integrations for US companies, built in stages at a fixed price. You own the code.",
 "Software development",
 "Custom software development<br>for <span class=\"grad\">US companies.</span>",
 "Internal tools, client portals, business systems and integrations, built around how your company actually works. In stages, each with a fixed price and something usable at the end of it. Custom software starts from €1,500.",
 [{"id":"build","tipo":"cards","eyebrow":"What we build",
   "h2":"The software US companies<br><span class=\"grad\">actually ask for</span>",
   "corpo":[
    ("Internal operations tools","Approvals, scheduling, inventory, reporting: the workflows currently held together by spreadsheets and one person who knows how they work."),
    ("Client and partner portals","Orders, documents, status and messaging in one place, so clients and dealers serve themselves instead of emailing you."),
    ("Quoting and configurators","Product rules and pricing in a tool your sales team and partners use, turning two-day quotes into two-minute ones."),
    ("Field service apps","Jobs, photos, signatures and time tracking on the phone, offline when needed, synced with the office."),
    ("Integrations","QuickBooks, Salesforce, HubSpot, Shopify, NetSuite and the rest — connected so nobody retypes data between them."),
    ("MVPs for startups","A first version for users and investors in weeks, at a fixed price, on mainstream technology your future team can take over.")]},
  {"id":"stages","tipo":"testo","eyebrow":"How projects are structured",
   "h2":"In stages,<br>so you <span class=\"grad\">can stop.</span>",
   "corpo":[
    "Most custom software projects fail the same way: everything is specified at once, built for a year, and delivered to a business that has moved on.",
    "We put the part that removes the most wasted time live first, usually within four to eight weeks, measure what it saved, and only then decide the next stage. Each stage has a fixed price and works on its own — you can stop after any of them and keep everything built so far.",
    "Offshore teams are cheaper per hour and slower per decision. We sit in between: a European team with a shared morning window every day, English throughout, and a quote that reflects where we are rather than where you are."]}],
 [("Native app, web app or off-the-shelf SaaS?","If a SaaS product fits 90% of your process, buy it and we can integrate it. If it fits 60%, the missing 40% is where your team loses hours, and custom software usually pays back. We tell you which on the first call.")],
 "Custom software development for US businesses","Custom business software, web application and integration development",
 "Custom business software, web applications, client portals and integrations for companies across the United States, built in stages with a fixed price per stage and code in the client's repository.",
 ["Custom business software","Web applications","Client portals","System integrations","MVP development","Software maintenance"],
 [("App &amp; software development %s" % NOME[x],"/en/software-development-%s/" % x) for x in SW_CITTA]))

PAGINE.append(hub(
 "/en/mobile-app-development-company-usa/",
 "Mobile App Development Company USA | Custom Apps",
 "iOS, Android and web apps for US companies: booking, loyalty, field service and internal apps. Fixed price per stage, code in your name. From €750.",
 "Mobile app development for US businesses — Danova Tech",
 "iOS, Android and installable web apps for US companies, built in stages at a fixed price by a ten-person team in Italy.",
 "Mobile apps",
 "Mobile app development<br>for <span class=\"grad\">US businesses.</span>",
 "Booking, ordering, loyalty, field service and internal apps for iOS and Android — or an installable web app when the App Store adds nothing. Ready-made web apps start from €750; custom apps get a fixed price per stage.",
 [{"id":"build","tipo":"cards","eyebrow":"What we build",
   "h2":"Apps with <span class=\"grad\">a clear job</span>",
   "corpo":[
    ("Booking and appointments","Classes, treatments, consultations, rentals: availability, payments, reminders and cancellations without a marketplace taking a cut."),
    ("Loyalty and memberships","Points, tiers, subscriptions and offers that give you a direct line to your best customers."),
    ("Ordering","Restaurant, retail and B2B ordering apps connected to your POS, inventory and delivery."),
    ("Field service","Jobs, routes, photos, signatures and time tracking for crews — offline when the signal is not there."),
    ("Internal apps","Inventory with barcode scanning, inspections, checklists, approvals: tools for staff who are never at a desk."),
    ("Health and fitness","Coaching, training plans and progress tracking, built with HIPAA and state health-data laws in mind.")]},
  {"id":"choice","tipo":"testo","eyebrow":"Before you build",
   "h2":"Native app<br>or <span class=\"grad\">web app?</span>",
   "corpo":[
    "Not every app needs the App Store. If your users are your own staff, or customers who log in to do one thing, an installable web app works on every phone, updates instantly, needs no store review and costs less to build and maintain.",
    "Go native when you need store presence for discovery, reliable push notifications on iOS, deep device features like Bluetooth or background location, or the polish customers expect from a consumer brand.",
    "We tell you which on the first call, with reasons — and if a ready-made app covers what you need, we say that too."]}],
 [("How long does an app take?","A focused first version typically takes six to ten weeks. We cut it to the smallest version that does the job, fix the price, and ship working builds every week."),
  ("Do you publish to the App Store and Google Play?","Yes, under your company's developer accounts, so the apps and their reviews belong to you.")],
 "Mobile app development for US businesses","iOS, Android and web app development",
 "iOS, Android and installable web apps for companies across the United States: booking, loyalty, ordering, field service and internal apps, built in stages with a fixed price per stage.",
 ["iOS app development","Android app development","Progressive web apps","Booking apps","Loyalty apps","Field service apps"],
 [("App &amp; software development %s" % NOME[x],"/en/software-development-%s/" % x) for x in SW_CITTA]))

PAGINE.append(hub(
 "/en/custom-erp-crm-development-usa/",
 "ERP Development Company | Custom ERP & CRM, USA",
 "Custom ERP and CRM systems for US companies: built around your process, data migrated from spreadsheets, fixed price agreed upfront. From €1,500.",
 "Custom ERP & CRM for US businesses — Danova Tech",
 "Business management systems and CRMs built around how your company works, at a fixed price, by a ten-person team in Italy.",
 "ERP & CRM",
 "Custom ERP and CRM<br>for <span class=\"grad\">US companies.</span>",
 "When off-the-shelf software makes your team work its way instead of yours, the gap gets filled with spreadsheets and retyping. We build business systems around your actual process, migrate your data, train your team — at a fixed price from €1,500.",
 [{"id":"build","tipo":"cards","eyebrow":"What it covers",
   "h2":"One system,<br>built around <span class=\"grad\">your process</span>",
   "corpo":[
    ("Customers and sales","Leads, deals, quotes and follow-ups, with the pipeline your team really uses rather than a vendor's template."),
    ("Orders and inventory","Orders, stock, purchasing and warehouse locations, with barcode scanning on the phone."),
    ("Jobs and projects","Job costing, scheduling, time and materials — the numbers that tell you which work actually makes money."),
    ("Invoicing and accounting sync","Invoices generated from the work, synced to QuickBooks, Xero or NetSuite so accounting stays where it is."),
    ("Portals for clients and partners","Clients and dealers see orders, documents and status themselves."),
    ("Reporting","Dashboards management actually reads, built on data the system already holds instead of a weekly spreadsheet export.")]},
  {"id":"extend","tipo":"testo","eyebrow":"Replace or extend?",
   "h2":"Often the answer is<br><span class=\"grad\">extend.</span>",
   "corpo":[
    "If you already run Salesforce, HubSpot, NetSuite or QuickBooks and it covers most of what you need, replacing it is rarely the cheapest answer. We build the missing module, interface or integration and leave the system of record where it is.",
    "When the existing tool genuinely does not fit — or you are still running on spreadsheets — a custom system built in stages is usually cheaper over three years than a heavily customized enterprise license, and it fits the way you work.",
    "Either way, we map your process before writing code, migrate your data, and train the people who will use it."]}],
 [("Can you migrate our data from spreadsheets or our current system?","Yes. Data migration is part of every ERP project: we clean, map and import it, and check the result with you before switching over.")],
 "Custom ERP and CRM development for US businesses","Custom ERP, CRM and business management software development",
 "Custom ERP and CRM systems and extensions for companies across the United States: process analysis, development in stages, data migration, integrations with accounting and e-commerce, and training.",
 ["Custom ERP development","Custom CRM development","Inventory management software","Job costing software","Data migration","ERP and accounting integrations"],
 [("App &amp; software development %s" % NOME[x],"/en/software-development-%s/" % x) for x in SW_CITTA]))
