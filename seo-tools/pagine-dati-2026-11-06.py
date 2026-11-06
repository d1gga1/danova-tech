# -*- coding: utf-8 -*-
"""06/11/2026 - Dati delle pagine nuove (build: seo-tools/pagine-build-2026-11-06.py).
   - IT  /agenti-ai-per-aziende/  ("agenti ai": 1k-10k ricerche/mese nel Keyword Planner, nessuna pagina dedicata)
   - ZH  /zh/   AR /ar/   TR /tr/  pagine base dei servizi, per imprese cinesi, arabe e turche
     che lavorano in Italia o vogliono entrare nel mercato italiano ed europeo.
   Fatti usati (gia' dichiarati sul sito): sede Mansue' (TV), team di 10 persone, P.IVA IT05369890263,
   siti da 350 EUR, sito in 24 ore, gestionali da 1.500 EUR, demo 48-72 ore, preventivo fisso in 24 ore,
   bozza gratuita prima di pagare, codice del cliente, nessun canone obbligatorio, lingue it/en/de/fr/es."""
OGGI = "2026-11-06"

ALT_HOME = {'it': '/', 'en': '/en/', 'de': '/de/', 'fr': '/fr/', 'es': '/es/',
            'zh': '/zh/', 'ar': '/ar/', 'tr': '/tr/'}

EMAIL = 'info@danova-tech.com'
TEL = '+39 388 470 6887'
WA = 'https://wa.me/393884706887'

AGENTI = {
 "lang": "it",
 "url": "/agenti-ai-per-aziende/",
 "title": "Agenti AI per aziende: cosa sono, esempi e costi | Danova Tech",
 "desc": "Agenti AI su misura per PMI: leggono email e documenti, aggiornano gestionale e CRM, preparano preventivi e chiedono conferma prima di agire. Esempi e come partire.",
 "ogtitle": "Agenti AI per aziende — Danova Tech",
 "ogdesc": "Agenti AI che fanno lavoro vero nei vostri sistemi, con regole chiare e una persona che approva. Esempi reali, costi e come si parte.",
 "crumbs": [["Software & Automazioni", "/servizi/software-automazioni/"], ["Agenti AI per aziende", None]],
 "eyebrow": "Intelligenza artificiale · Agenti AI su misura",
 "h1": "Agenti AI per aziende: <span class=\"grad\">lavoro fatto, non solo risposte.</span>",
 "lead": "Un chatbot risponde. Un agente AI legge l’email del cliente, controlla il magazzino, prepara l’ordine nel gestionale e vi chiede solo l’ok finale. Li costruiamo su misura per PMI italiane, su un processo alla volta, con regole scritte su cosa l’agente può fare da solo e cosa no.",
 "cta1": "Parliamo del vostro processo",
 "cta2": "Cos’è un agente AI",
 "sezioni": [
  {"id": "in-breve", "tipo": "breve", "eyebrow": "In breve",
   "h2": "Gli agenti AI di Danova Tech, <span class=\"grad\">in cinque righe</span>",
   "testo": "Un <b>agente AI</b> è un programma che usa un modello linguistico (come quelli dietro ChatGPT o Claude) per <b>svolgere un compito in più passaggi</b>: legge una richiesta, consulta i vostri dati, usa i vostri strumenti (gestionale, CRM, email, WhatsApp) e produce un risultato, fermandosi per chiedere conferma quando le regole lo prevedono. Danova Tech, agenzia informatica con sede a Mansuè (Treviso), sviluppa agenti AI su misura per piccole e medie imprese: si parte da un processo preciso, si misura il tempo risparmiato e solo dopo si estende.",
   "fatti": [["Cosa fa", "Compiti in più passaggi nei vostri sistemi"],
             ["Chi decide", "Una persona approva le azioni importanti"],
             ["Dove lavora", "Gestionale, CRM, email, WhatsApp, documenti"],
             ["Come si parte", "Un processo, misurato su dati veri"],
             ["Prezzo", "Fisso per tappa, preventivo in 24 ore"],
             ["Dati", "Su sistemi e fornitori scelti con voi"]]},
  {"id": "cos-e", "tipo": "testo", "eyebrow": "Definizione",
   "h2": "Cos’è un agente AI <span class=\"grad\">(e cosa non è)</span>",
   "corpo": [
    "Un’<b>automazione classica</b> segue un percorso fisso: se arriva un modulo, crea un contatto nel CRM. Funziona benissimo finché i dati arrivano sempre nello stesso formato. Un <b>chatbot</b> risponde a domande: utile, ma non fa nulla nei vostri sistemi. Un <b>agente AI</b> sta a metà: capisce richieste scritte in modo libero (un’email, un PDF, un vocale trascritto), decide quali passaggi servono e li esegue con gli strumenti che gli avete dato.",
    "Esempio concreto: un cliente scrive “mi mandate le solite 40 scatole della settimana scorsa, ma consegna giovedì”. L’agente riconosce il cliente, ritrova l’ordine precedente, verifica la disponibilità, prepara la bozza d’ordine con la nuova data e la mette in coda per l’approvazione. La persona in ufficio controlla in dieci secondi invece di ricopiare tutto in cinque minuti.",
    "Cosa un agente AI <b>non</b> è: non è un dipendente che decide da solo su soldi, contratti o persone, e non è una scatola magica che “fa tutto”. Funziona quando il compito è chiaro, i dati sono raggiungibili e le eccezioni hanno una strada definita. Per questo il lavoro vero non è il modello: è scrivere bene le regole, i permessi e i controlli."]},
  {"id": "esempi", "tipo": "cards", "eyebrow": "Esempi",
   "h2": "Sei agenti AI <span class=\"grad\">che ripagano il lavoro</span>",
   "lead": "Sono i casi in cui il risparmio si misura in ore a settimana. Fuori da questi, spesso basta un’automazione semplice.",
   "corpo": [
    ["Ordini da email e WhatsApp", "Legge il messaggio, riconosce cliente e articoli, controlla disponibilità e prezzi di listino e prepara l’ordine nel gestionale da approvare."],
    ["Preventivi in prima bozza", "Parte dalla richiesta del cliente, applica le vostre regole di prezzo e i vostri modelli e vi consegna un preventivo da rivedere, non da scrivere."],
    ["Documenti dei fornitori", "Legge DDT, fatture e conferme d’ordine, li confronta con l’ordine di acquisto e segnala solo le differenze: quantità, prezzi, date."],
    ["Assistenza di primo livello", "Risponde dai vostri manuali e dallo storico, apre il ticket con i dati già compilati e passa a una persona quando la domanda esce dal seminato."],
    ["Solleciti e scadenze", "Controlla scadenze di pagamenti, contratti e manutenzioni, prepara i messaggi giusti per ogni cliente e li invia solo dopo il vostro ok."],
    ["Report settimanali", "Raccoglie i numeri da gestionale, CRM e campagne, li confronta con la settimana prima e scrive tre righe su cosa è cambiato e perché."]]},
  {"id": "processo", "tipo": "passi", "eyebrow": "Metodo",
   "h2": "Come costruiamo <span class=\"grad\">un agente AI</span>",
   "corpo": [
    ["Scegliamo un processo", "Uno solo, ripetitivo e misurabile: quante richieste al giorno, quanto tempo ciascuna, quanti errori. È il numero da battere."],
    ["Scriviamo le regole", "Cosa l’agente può fare da solo, cosa prepara per l’approvazione, cosa non tocca mai. Permessi separati per ogni sistema."],
    ["Prototipo su dati veri", "Lo proviamo su richieste reali del passato, in parallelo al lavoro di sempre, senza toccare i dati di produzione."],
    ["Misura e correzioni", "Confrontiamo tempi ed errori con il punto di partenza. Se il risultato non c’è, ve lo diciamo e ci fermiamo lì."],
    ["Messa in produzione", "Registro di ogni azione, avvisi sulle eccezioni, costi di esercizio sotto un limite concordato. Poi, se conviene, il processo successivo."]]},
  {"id": "controllo", "tipo": "testo", "eyebrow": "Controllo e AI Act",
   "h2": "Un agente utile <span class=\"grad\">è un agente sorvegliato</span>",
   "corpo": [
    "Ogni azione dell’agente resta in un registro leggibile: cosa ha letto, cosa ha deciso, cosa ha fatto e chi ha approvato. Le azioni che spostano soldi o impegnano l’azienda (ordini, pagamenti, invii a molti clienti) passano sempre da una persona. I permessi sono quelli minimi: se l’agente deve leggere il magazzino, non vede la contabilità.",
    "Sui dati scegliamo con voi dove vengono elaborati: modelli di fornitori con sede o server in Europa e contratti che escludono l’addestramento sui vostri dati, oppure, per documenti molto sensibili, un modello eseguito su un vostro server. Per gli obblighi del regolamento europeo sull’intelligenza artificiale trovate la sintesi pratica nella pagina <a href=\"/ai-act-aziende/\">AI Act per le aziende</a>."]},
  {"id": "costi", "tipo": "testo", "eyebrow": "Costi",
   "h2": "Quanto costa <span class=\"grad\">un agente AI</span>",
   "corpo": [
    "Il costo ha tre parti. <b>Lo sviluppo</b>: analisi, regole, collegamenti ai vostri sistemi e prove, a prezzo fisso per tappa, con preventivo scritto entro 24 ore dalla prima chiamata. <b>L’esercizio</b>: il modello AI si paga a consumo, in base a quante richieste elabora; lo stimiamo sui vostri volumi prima di partire e lo teniamo sotto un tetto concordato. <b>La manutenzione</b>: aggiornamenti quando cambiano i vostri sistemi o i modelli, solo se la volete.",
    "Il modo più economico di partire è un solo processo ben delimitato. Se dopo la prova il tempo risparmiato non giustifica la spesa, è meglio saperlo subito: è il motivo per cui la prima tappa è sempre una misura, non un progetto grande."]},
 ],
 "faqtitle": "Domande frequenti sugli agenti AI",
 "faq": [
  ["Che differenza c’è tra un agente AI e un chatbot?", "Il chatbot risponde a domande. L’agente AI esegue un compito in più passaggi nei vostri sistemi: legge una richiesta, consulta i dati, prepara un ordine o un preventivo e chiede conferma prima delle azioni importanti."],
  ["Un agente AI può sostituire un dipendente?", "No, e non è l’obiettivo. Toglie il lavoro ripetitivo di copiare, controllare e riassumere, così le persone si occupano delle eccezioni, dei clienti e delle decisioni. Le azioni che impegnano l’azienda restano approvate da una persona."],
  ["Con quali programmi funziona?", "Con quelli che hanno un modo per scambiare dati: gestionali e CRM con API o esportazioni, caselle email, WhatsApp Business, cartelle di documenti, fogli di calcolo. Se un sistema è chiuso, lo valutiamo nell’analisi iniziale prima di promettere qualsiasi cosa."],
  ["I nostri dati finiscono ad addestrare l’AI?", "No: usiamo servizi con contratti che escludono l’addestramento sui dati dei clienti, scegliamo con voi dove vengono elaborati e, per documenti molto sensibili, possiamo usare un modello installato su un vostro server."],
  ["Quanto tempo serve per avere il primo agente?", "Dipende dal processo e da quanto sono raggiungibili i dati. Il preventivo con tempi e prezzo fisso per tappa arriva entro 24 ore dalla prima chiamata, dopo aver visto come lavorate oggi."],
  ["Meglio un agente AI o un’automazione con n8n?", "Se i dati arrivano sempre nello stesso formato, un’automazione classica costa meno e sbaglia meno. L’agente AI conviene quando le richieste sono scritte in modo libero o cambiano ogni volta. Spesso la soluzione giusta usa entrambi."],
 ],
 "ctabox": {"h2": "Qual è il processo che vi ruba più ore?",
            "p": "Raccontatecelo in una chiamata di 20 minuti: vi diciamo se un agente AI conviene, se basta un’automazione semplice o se è meglio lasciar perdere.",
            "btn": "Prenota la chiamata"},
 "altrititle": "Approfondisci",
 "altri": [["Chatbot aziendale sui vostri documenti", "/chatbot-aziendale/"],
           ["Automazioni n8n per aziende", "/automazioni-n8n/"],
           ["Automazione dei processi aziendali", "/automazione-processi-aziendali/"],
           ["Consulenza intelligenza artificiale", "/consulenza-intelligenza-artificiale/"],
           ["Intelligenza artificiale per aziende", "/intelligenza-artificiale-per-aziende/"],
           ["WhatsApp aziendale e chatbot WhatsApp", "/whatsapp-aziendale/"],
           ["Integrazione software aziendali", "/integrazione-software-aziendali/"],
           ["AI Act per le aziende", "/ai-act-aziende/"]],
 "svc": {"name": "Agenti AI per aziende", "type": "Sviluppo di agenti di intelligenza artificiale su misura",
         "desc": "Progettazione e sviluppo di agenti AI su misura per PMI: elaborazione di ordini, preventivi, documenti e assistenza clienti nei sistemi aziendali, con approvazione umana delle azioni importanti.",
         "area": [{"@type": "Country", "name": "Italia"}, {"@type": "Place", "name": "Europa"}],
         "lingue": ["it", "en", "de", "fr", "es"],
         "catalogo": ["Agente AI per ordini da email e WhatsApp", "Agente AI per preventivi", "Agente AI per documenti dei fornitori",
                      "Agente AI per assistenza clienti", "Agente AI per solleciti e scadenze", "Agente AI per report aziendali"]},
}


def contatti_sez(h2, testo_html):
    return {"id": "contatti", "tipo": "testo", "eyebrow": "Contact", "h2": h2, "corpo": testo_html}


ZH = {
 "lang": "zh", "url": "/zh/", "alt": ALT_HOME,
 "title": "意大利网站建设与定制软件开发公司 | Danova Tech",
 "desc": "Danova Tech 是意大利特雷维索的软件与网络公司：意大利语网站、电子商务、定制管理软件、AI 自动化和意大利市场 SEO。24 小时内固定报价。",
 "ogtitle": "Danova Tech — 意大利网站与定制软件",
 "ogdesc": "为在意大利经营或希望进入意大利和欧洲市场的企业提供网站、管理软件、AI 与网络营销。",
 "crumbs": [["中文", None]],
 "eyebrow": "意大利 · 网站 · 软件 · AI",
 "h1": "在意大利做生意？<span class=\"grad\">网站、软件和网络营销交给一个团队。</span>",
 "lead": "Danova Tech 是一家意大利信息技术公司，总部位于特雷维索省 Mansuè，团队 10 人。我们为在意大利经营的企业以及希望进入意大利和欧洲市场的企业，制作意大利语网站和网店、定制管理软件、AI 自动化，并负责 Google 搜索排名和广告。我们使用英语或意大利语沟通。",
 "cta1": "联系我们", "cta2": "我们的服务",
 "sezioni": [
  {"id": "in-breve", "tipo": "breve", "eyebrow": "概要", "h2": "Danova Tech <span class=\"grad\">一览</span>",
   "testo": "<b>Danova Tech</b> 是一家意大利信息技术公司（增值税号 IT05369890263），总部位于意大利威尼托大区特雷维索省 Mansuè。我们开发网站、电子商务、移动和网页应用、定制管理软件与 CRM、AI 自动化，并提供 SEO、Google Ads 和 Meta Ads 服务。我们特别适合<b>在意大利经营的企业</b>：网站和文字面向意大利客户，软件符合意大利的电子发票等要求。",
   "fatti": [["总部", "意大利 特雷维索省 Mansuè"], ["团队", "10 人"], ["网站", "350 欧元起（含增值税）"],
             ["管理软件", "1,500 欧元起"], ["报价", "24 小时内固定报价"], ["沟通语言", "英语、意大利语"]]},
  {"id": "servizi", "tipo": "cards", "eyebrow": "服务", "h2": "我们能为您做什么",
   "corpo": [
    ["意大利语网站", "面向意大利客户的专业网站：意大利语文字、适配手机、加载快速。基础网站最快 24 小时上线，350 欧元起。"],
    ["网店与电子商务", "在意大利和欧洲销售产品的网店：支付、运费、多语言，以及与仓库和管理软件的连接。"],
    ["定制管理软件", "仓库、订单、生产、门店收银、预约等定制管理软件，可对接意大利电子发票系统。48–72 小时内提供可用演示。"],
    ["AI 与自动化", "AI 助手和自动化流程：读取邮件与文件、整理订单、生成报价和报告，重要操作由人工确认。"],
    ["Google 排名与广告", "意大利市场的 SEO、Google 商家资料、Google Ads 和 Meta Ads 广告，每月提供清晰的报告。"],
    ["广告视频", "用于社交媒体和广告的短视频与 AI 视频，24 小时内交付，价格按项目报价。"]]},
  {"id": "processo", "tipo": "passi", "eyebrow": "流程", "h2": "合作流程",
   "corpo": [
    ["告诉我们需求", "通过邮件、电话或 WhatsApp（英语或意大利语），简单说明您的业务和目标。"],
    ["24 小时内报价", "我们在 24 小时内给出书面固定报价，没有隐藏费用。"],
    ["先看草稿", "网站先看免费草稿，软件先看可用演示，满意后再付款。"],
    ["开发与上线", "按阶段开发，每个阶段价格固定；网站和软件的代码归您所有。"],
    ["持续支持", "上线后提供维护、更新和营销支持，没有强制性的年费。"]]},
  {"id": "perche", "tipo": "testo", "eyebrow": "为什么选择意大利团队", "h2": "了解意大利市场的团队",
   "corpo": [
    "意大利客户用意大利语搜索、比较和购买。一个真正在意大利的团队，知道客户会搜索哪些词、信任哪些信息，以及电子发票、隐私（GDPR）和 Cookie 等当地规定。",
    "我们为意大利各地以及欧洲的客户远程工作，在威尼托、弗留利和伦巴第可以上门会面。所有项目都有书面合同、固定价格和明确的交付时间。"]},
  contatti_sez("联系我们", [
    "电子邮件：<a href=\"mailto:%s\">%s</a>" % (EMAIL, EMAIL),
    "电话 / WhatsApp：<a href=\"%s\">%s</a>" % (WA, TEL),
    "我们使用英语或意大利语沟通，一般在 24 小时内回复。地址：Via Rigole 48, 31040 Mansuè (TV), Italia。"]),
 ],
 "faqtitle": "常见问题",
 "faq": [
  ["你们可以用中文沟通吗？", "我们的团队使用英语和意大利语。所有报价和合同都以书面形式提供，方便您翻译和核对。"],
  ["网站和软件多少钱？", "基础网站 350 欧元起（含增值税），定制管理软件 1,500 欧元起。每个项目都会在 24 小时内收到书面固定报价。"],
  ["什么时候付款？", "网站先看免费草稿，软件先看可用演示，满意后再付款。之后按阶段付款，每个阶段价格固定。"],
  ["代码归谁所有？", "归您所有。域名以您的名义注册，没有强制性年费，您可以随时更换服务商。"],
  ["你们只服务意大利公司吗？", "不是。我们为在意大利经营的企业，以及希望进入意大利和欧洲市场的企业远程工作。"]],
 "ctabox": {"h2": "准备进入意大利市场？", "p": "写邮件或 WhatsApp 告诉我们您的项目，我们在 24 小时内回复。", "btn": "联系我们"},
 "altrititle": "其他语言",
 "altri": [["Italiano", "/"], ["English", "/en/"], ["Deutsch", "/de/"], ["Français", "/fr/"], ["Español", "/es/"],
           ["العربية", "/ar/"], ["Türkçe", "/tr/"]],
 "svc": {"name": "Danova Tech — 网站、定制软件与网络营销", "type": "网站建设与软件开发",
         "desc": "为在意大利经营或希望进入意大利和欧洲市场的企业提供网站、电子商务、定制管理软件、AI 自动化、SEO 和网络广告。",
         "area": [{"@type": "Country", "name": "Italia"}, {"@type": "Place", "name": "Europa"}],
         "lingue": ["it", "en"],
         "catalogo": ["网站建设", "电子商务", "定制管理软件", "AI 自动化", "SEO 与网络广告", "广告视频"]},
}

AR = {
 "lang": "ar", "url": "/ar/", "alt": ALT_HOME,
 "title": "شركة إيطالية لتصميم المواقع وتطوير البرمجيات | Danova Tech",
 "desc": "Danova Tech شركة تقنية إيطالية في تريفيزو: مواقع باللغة الإيطالية، متاجر إلكترونية، برامج إدارة مخصصة، أتمتة بالذكاء الاصطناعي وتسويق للسوق الإيطالي. عرض سعر ثابت خلال 24 ساعة.",
 "ogtitle": "Danova Tech — مواقع وبرمجيات مخصصة في إيطاليا",
 "ogdesc": "مواقع وبرامج إدارة وذكاء اصطناعي وتسويق رقمي للشركات العاملة في إيطاليا أو الراغبة في دخول السوق الإيطالي والأوروبي.",
 "crumbs": [["العربية", None]],
 "eyebrow": "إيطاليا · مواقع · برمجيات · ذكاء اصطناعي",
 "h1": "تعمل في إيطاليا؟ <span class=\"grad\">الموقع والبرامج والتسويق مع فريق واحد.</span>",
 "lead": "Danova Tech شركة تقنية معلومات إيطالية مقرها في مانسويه بمقاطعة تريفيزو، ويضم فريقها 10 أشخاص. نصمم مواقع ومتاجر إلكترونية باللغة الإيطالية، ونطور برامج إدارة مخصصة وأتمتة بالذكاء الاصطناعي، ونتولى الظهور في بحث Google والإعلانات، للشركات العاملة في إيطاليا أو الراغبة في دخول السوق الإيطالي والأوروبي. نتواصل باللغة الإنجليزية أو الإيطالية.",
 "cta1": "تواصل معنا", "cta2": "خدماتنا",
 "sezioni": [
  {"id": "in-breve", "tipo": "breve", "eyebrow": "باختصار", "h2": "Danova Tech <span class=\"grad\">في سطور</span>",
   "testo": "<b>Danova Tech</b> شركة تقنية معلومات إيطالية (رقم ضريبي IT05369890263) مقرها في مانسويه، مقاطعة تريفيزو، إقليم فينيتو. نطور المواقع والمتاجر الإلكترونية وتطبيقات الهاتف والويب وبرامج الإدارة وإدارة العملاء المخصصة والأتمتة بالذكاء الاصطناعي، ونقدم خدمات تحسين محركات البحث وإعلانات Google وMeta. نحن مناسبون بشكل خاص <b>للشركات التي تعمل في إيطاليا</b>: مواقع ونصوص موجهة للعملاء الإيطاليين، وبرامج متوافقة مع متطلبات مثل الفاتورة الإلكترونية الإيطالية.",
   "fatti": [["المقر", "مانسويه، تريفيزو، إيطاليا"], ["الفريق", "10 أشخاص"], ["المواقع", "ابتداءً من 350 يورو شاملة الضريبة"],
             ["برامج الإدارة", "ابتداءً من 1500 يورو"], ["عرض السعر", "ثابت خلال 24 ساعة"], ["لغة التواصل", "الإنجليزية والإيطالية"]]},
  {"id": "servizi", "tipo": "cards", "eyebrow": "الخدمات", "h2": "ماذا نقدم لك",
   "corpo": [
    ["مواقع باللغة الإيطالية", "مواقع احترافية للعملاء الإيطاليين: نصوص بالإيطالية، سريعة ومناسبة للهاتف. الموقع الأساسي جاهز خلال 24 ساعة، ابتداءً من 350 يورو."],
    ["متاجر إلكترونية", "متاجر للبيع في إيطاليا وأوروبا: الدفع والشحن وتعدد اللغات، مع الربط بالمخزون وبرنامج الإدارة."],
    ["برامج إدارة مخصصة", "برامج للمخزون والطلبات والإنتاج ونقاط البيع والحجوزات، مع إمكانية الربط بنظام الفاتورة الإلكترونية الإيطالي. نسخة تجريبية عاملة خلال 48 إلى 72 ساعة."],
    ["الذكاء الاصطناعي والأتمتة", "مساعدون أذكياء وعمليات مؤتمتة: قراءة البريد والمستندات، وتجهيز الطلبات والعروض والتقارير، مع موافقة بشرية على الإجراءات المهمة."],
    ["الظهور في Google والإعلانات", "تحسين محركات البحث للسوق الإيطالي، وملف النشاط التجاري في Google، وإعلانات Google وMeta، مع تقرير شهري واضح."],
    ["فيديوهات إعلانية", "فيديوهات قصيرة وفيديوهات بالذكاء الاصطناعي لوسائل التواصل والإعلانات، تُسلّم خلال 24 ساعة، والسعر حسب المشروع."]]},
  {"id": "processo", "tipo": "passi", "eyebrow": "طريقة العمل", "h2": "كيف نعمل معك",
   "corpo": [
    ["أخبرنا بما تحتاجه", "عبر البريد أو الهاتف أو واتساب، بالإنجليزية أو الإيطالية: نشاطك وأهدافك في بضعة أسطر."],
    ["عرض سعر خلال 24 ساعة", "عرض مكتوب بسعر ثابت خلال 24 ساعة، دون تكاليف مخفية."],
    ["شاهد قبل أن تدفع", "مسودة مجانية للموقع ونسخة تجريبية عاملة للبرنامج، وتدفع فقط إذا أعجبتك."],
    ["التطوير والإطلاق", "نعمل على مراحل بسعر ثابت لكل مرحلة، وشيفرة الموقع والبرنامج ملك لك."],
    ["دعم مستمر", "صيانة وتحديثات ودعم تسويقي بعد الإطلاق، دون رسوم سنوية إلزامية."]]},
  {"id": "perche", "tipo": "testo", "eyebrow": "لماذا فريق إيطالي", "h2": "فريق يعرف السوق الإيطالي",
   "corpo": [
    "العميل الإيطالي يبحث ويقارن ويشتري باللغة الإيطالية. الفريق الموجود فعلاً في إيطاليا يعرف الكلمات التي يبحث عنها العملاء والمعلومات التي يثقون بها، والقواعد المحلية مثل الفاتورة الإلكترونية والخصوصية (GDPR) وملفات تعريف الارتباط.",
    "نعمل عن بُعد مع عملاء في كل إيطاليا وأوروبا، ويمكننا اللقاء حضورياً في فينيتو وفريولي ولومبارديا. كل مشروع له عقد مكتوب وسعر ثابت وموعد تسليم واضح."]},
  contatti_sez("تواصل معنا", [
    "البريد الإلكتروني: <a href=\"mailto:%s\">%s</a>" % (EMAIL, EMAIL),
    "الهاتف / واتساب: <a href=\"%s\" dir=\"ltr\">%s</a>" % (WA, TEL),
    "نتواصل بالإنجليزية أو الإيطالية ونرد عادةً خلال 24 ساعة. العنوان: Via Rigole 48, 31040 Mansuè (TV), Italia."]),
 ],
 "faqtitle": "أسئلة شائعة",
 "faq": [
  ["هل يمكنكم التواصل باللغة العربية؟", "فريقنا يعمل بالإنجليزية والإيطالية. نرسل كل العروض والعقود مكتوبة لتتمكن من ترجمتها ومراجعتها بسهولة."],
  ["كم تكلفة الموقع أو البرنامج؟", "الموقع الأساسي ابتداءً من 350 يورو شاملة الضريبة، وبرامج الإدارة المخصصة ابتداءً من 1500 يورو. يصلك عرض مكتوب بسعر ثابت خلال 24 ساعة."],
  ["متى أدفع؟", "تشاهد أولاً مسودة مجانية للموقع أو نسخة تجريبية عاملة للبرنامج، وتدفع إذا أعجبتك. بعد ذلك يكون الدفع على مراحل بسعر ثابت لكل مرحلة."],
  ["لمن تعود ملكية الشيفرة؟", "لك. النطاق يُسجَّل باسمك، ولا توجد رسوم سنوية إلزامية، ويمكنك تغيير المزوّد متى شئت."],
  ["هل تعملون مع الشركات الإيطالية فقط؟", "لا. نعمل عن بُعد مع الشركات العاملة في إيطاليا ومع الشركات الراغبة في دخول السوق الإيطالي والأوروبي."]],
 "ctabox": {"h2": "هل أنت مستعد للسوق الإيطالي؟", "p": "اكتب لنا عبر البريد أو واتساب عن مشروعك، وسنرد خلال 24 ساعة.", "btn": "تواصل معنا"},
 "altrititle": "لغات أخرى",
 "altri": [["Italiano", "/"], ["English", "/en/"], ["Deutsch", "/de/"], ["Français", "/fr/"], ["Español", "/es/"],
           ["中文", "/zh/"], ["Türkçe", "/tr/"]],
 "svc": {"name": "Danova Tech — مواقع وبرمجيات مخصصة وتسويق رقمي", "type": "تصميم مواقع وتطوير برمجيات",
         "desc": "مواقع ومتاجر إلكترونية وبرامج إدارة مخصصة وأتمتة بالذكاء الاصطناعي وتحسين محركات البحث وإعلانات رقمية للشركات العاملة في إيطاليا أو الراغبة في دخول السوق الإيطالي والأوروبي.",
         "area": [{"@type": "Country", "name": "Italia"}, {"@type": "Place", "name": "Europa"}],
         "lingue": ["it", "en"],
         "catalogo": ["تصميم المواقع", "المتاجر الإلكترونية", "برامج الإدارة المخصصة", "الأتمتة بالذكاء الاصطناعي", "تحسين محركات البحث والإعلانات", "الفيديوهات الإعلانية"]},
}

TR = {
 "lang": "tr", "url": "/tr/", "alt": ALT_HOME,
 "title": "İtalya'da web sitesi ve özel yazılım geliştirme | Danova Tech",
 "desc": "Danova Tech, Treviso merkezli bir İtalyan yazılım ve web ajansı: İtalyanca web siteleri, e-ticaret, özel yönetim yazılımları, yapay zekâ otomasyonu ve İtalya pazarı için SEO. 24 saatte sabit fiyat teklifi.",
 "ogtitle": "Danova Tech — İtalya'da web sitesi ve özel yazılım",
 "ogdesc": "İtalya'da faaliyet gösteren ya da İtalya ve Avrupa pazarına girmek isteyen şirketler için web sitesi, yazılım, yapay zekâ ve dijital pazarlama.",
 "crumbs": [["Türkçe", None]],
 "eyebrow": "İtalya · Web · Yazılım · Yapay zekâ",
 "h1": "İtalya'da iş mi yapıyorsunuz? <span class=\"grad\">Web sitesi, yazılım ve pazarlama tek ekipte.</span>",
 "lead": "Danova Tech, Treviso iline bağlı Mansuè'de bulunan, 10 kişilik bir İtalyan bilişim şirketidir. İtalya'da faaliyet gösteren veya İtalya ve Avrupa pazarına girmek isteyen şirketler için İtalyanca web siteleri ve e-ticaret mağazaları, özel yönetim yazılımları ve yapay zekâ otomasyonları geliştiriyor, Google aramalarında görünürlük ve reklamları yönetiyoruz. İngilizce veya İtalyanca iletişim kuruyoruz.",
 "cta1": "Bize ulaşın", "cta2": "Hizmetlerimiz",
 "sezioni": [
  {"id": "in-breve", "tipo": "breve", "eyebrow": "Kısaca", "h2": "Danova Tech <span class=\"grad\">bir bakışta</span>",
   "testo": "<b>Danova Tech</b>, merkezi Veneto bölgesinde, Treviso iline bağlı Mansuè'de bulunan bir İtalyan bilişim şirketidir (KDV no. IT05369890263). Web siteleri, e-ticaret, mobil ve web uygulamaları, özel yönetim yazılımları ve CRM, yapay zekâ otomasyonları geliştirir; SEO, Google Ads ve Meta Ads hizmetleri sunar. Özellikle <b>İtalya'da çalışan şirketler</b> için uygundur: İtalyan müşterilere yönelik siteler ve metinler, İtalyan e-fatura gibi gerekliliklere uygun yazılımlar.",
   "fatti": [["Merkez", "Mansuè, Treviso, İtalya"], ["Ekip", "10 kişi"], ["Web siteleri", "350 €'dan başlayan fiyatlarla (KDV dahil)"],
             ["Yönetim yazılımı", "1.500 €'dan başlayan fiyatlarla"], ["Teklif", "24 saatte sabit fiyat"], ["İletişim dili", "İngilizce, İtalyanca"]]},
  {"id": "servizi", "tipo": "cards", "eyebrow": "Hizmetler", "h2": "Sizin için neler yapabiliriz",
   "corpo": [
    ["İtalyanca web sitesi", "İtalyan müşterilere yönelik profesyonel site: İtalyanca metinler, hızlı ve mobil uyumlu. Temel site 24 saatte yayında, 350 €'dan başlayan fiyatlarla."],
    ["E-ticaret mağazası", "İtalya ve Avrupa'da satış için online mağaza: ödeme, kargo, çok dilli yapı; stok ve yönetim yazılımıyla bağlantı."],
    ["Özel yönetim yazılımı", "Stok, sipariş, üretim, mağaza kasası ve rezervasyon için özel yazılım; İtalyan e-fatura sistemine bağlanabilir. 48–72 saatte çalışan demo."],
    ["Yapay zekâ ve otomasyon", "Yapay zekâ asistanları ve otomatik süreçler: e-posta ve belgeleri okuma, sipariş, teklif ve rapor hazırlama; önemli işlemler insan onayıyla."],
    ["Google'da görünürlük ve reklam", "İtalya pazarı için SEO, Google İşletme Profili, Google Ads ve Meta Ads; her ay anlaşılır bir rapor."],
    ["Reklam videoları", "Sosyal medya ve reklamlar için kısa videolar ve yapay zekâ videoları; 24 saatte teslim, fiyat projeye göre."]]},
  {"id": "processo", "tipo": "passi", "eyebrow": "Süreç", "h2": "Nasıl çalışıyoruz",
   "corpo": [
    ["İhtiyacınızı anlatın", "E-posta, telefon veya WhatsApp ile, İngilizce ya da İtalyanca: işinizi ve hedeflerinizi birkaç satırda yazın."],
    ["24 saatte teklif", "24 saat içinde yazılı ve sabit fiyatlı teklif; gizli maliyet yok."],
    ["Ödemeden önce görün", "Web sitesi için ücretsiz taslak, yazılım için çalışan demo; beğenirseniz ödersiniz."],
    ["Geliştirme ve yayın", "Her aşaması sabit fiyatlı adımlarla ilerleriz; site ve yazılımın kodu sizindir."],
    ["Sürekli destek", "Yayından sonra bakım, güncelleme ve pazarlama desteği; zorunlu yıllık ücret yok."]]},
  {"id": "perche", "tipo": "testo", "eyebrow": "Neden İtalyan bir ekip", "h2": "İtalya pazarını bilen bir ekip",
   "corpo": [
    "İtalyan müşteri İtalyanca arar, karşılaştırır ve satın alır. Gerçekten İtalya'da bulunan bir ekip, müşterilerin hangi kelimeleri aradığını, hangi bilgilere güvendiğini ve e-fatura, gizlilik (GDPR) ve çerezler gibi yerel kuralları bilir.",
    "İtalya'nın her yerinden ve Avrupa'dan müşterilerle uzaktan çalışıyoruz; Veneto, Friuli ve Lombardiya'da yüz yüze görüşebiliriz. Her projede yazılı sözleşme, sabit fiyat ve net teslim tarihi vardır."]},
  contatti_sez("Bize ulaşın", [
    "E-posta: <a href=\"mailto:%s\">%s</a>" % (EMAIL, EMAIL),
    "Telefon / WhatsApp: <a href=\"%s\">%s</a>" % (WA, TEL),
    "İngilizce veya İtalyanca iletişim kuruyor, genellikle 24 saat içinde yanıt veriyoruz. Adres: Via Rigole 48, 31040 Mansuè (TV), Italia."]),
 ],
 "faqtitle": "Sık sorulan sorular",
 "faq": [
  ["Türkçe iletişim kurabilir miyiz?", "Ekibimiz İngilizce ve İtalyanca çalışır. Tüm teklif ve sözleşmeleri yazılı gönderiyoruz; kolayca çevirip kontrol edebilirsiniz."],
  ["Web sitesi veya yazılım ne kadar?", "Temel web sitesi KDV dahil 350 €'dan, özel yönetim yazılımı 1.500 €'dan başlar. Her proje için 24 saat içinde yazılı ve sabit fiyatlı teklif alırsınız."],
  ["Ne zaman ödeme yapıyorum?", "Önce web sitesinin ücretsiz taslağını veya yazılımın çalışan demosunu görürsünüz; beğenirseniz ödersiniz. Sonrasında ödeme, her biri sabit fiyatlı aşamalar halinde yapılır."],
  ["Kod kime ait?", "Size. Alan adı sizin adınıza kaydedilir, zorunlu yıllık ücret yoktur ve istediğiniz zaman sağlayıcı değiştirebilirsiniz."],
  ["Sadece İtalyan şirketlerle mi çalışıyorsunuz?", "Hayır. İtalya'da faaliyet gösteren şirketlerle ve İtalya ve Avrupa pazarına girmek isteyen şirketlerle uzaktan çalışıyoruz."]],
 "ctabox": {"h2": "İtalya pazarına hazır mısınız?", "p": "Projenizi e-posta veya WhatsApp ile anlatın, 24 saat içinde yanıt verelim.", "btn": "Bize ulaşın"},
 "altrititle": "Diğer diller",
 "altri": [["Italiano", "/"], ["English", "/en/"], ["Deutsch", "/de/"], ["Français", "/fr/"], ["Español", "/es/"],
           ["中文", "/zh/"], ["العربية", "/ar/"]],
 "svc": {"name": "Danova Tech — web sitesi, özel yazılım ve dijital pazarlama", "type": "Web tasarım ve yazılım geliştirme",
         "desc": "İtalya'da faaliyet gösteren veya İtalya ve Avrupa pazarına girmek isteyen şirketler için web siteleri, e-ticaret, özel yönetim yazılımları, yapay zekâ otomasyonu, SEO ve dijital reklam.",
         "area": [{"@type": "Country", "name": "Italia"}, {"@type": "Place", "name": "Europa"}],
         "lingue": ["it", "en"],
         "catalogo": ["Web sitesi", "E-ticaret", "Özel yönetim yazılımı", "Yapay zekâ otomasyonu", "SEO ve dijital reklam", "Reklam videoları"]},
}

PAGINE = [AGENTI, ZH, AR, TR]
