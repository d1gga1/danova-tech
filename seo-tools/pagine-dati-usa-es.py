# -*- coding: utf-8 -*-
"""Pagine USA in spagnolo (es-US) per il mercato ispanico. Si usa "ustedes", non "vosotros".
   Si genera con:  python3 seo-tools/pagine-build-usa.py
   COPPIE: ogni pagina spagnola ha la gemella inglese (hreflang reciproco)."""
OGGI = "2026-10-10"
PAGINE = []
US = {"@type":"Country","name":"Estados Unidos"}
COPPIE = {}   # url es -> url en

def area(c, st): return [{"@type":"City","name":c},{"@type":"State","name":st},US]

def servicios(c):
    return {"id":"que","tipo":"cards","eyebrow":"Qué construimos",
     "h2":"Páginas web, apps y software<br>para <span class=\"grad\">negocios de %s</span>" % c,
     "lead":"Seis tipos de proyecto cubren casi todo lo que nos piden empresas en Estados Unidos. Lo primero, en la llamada, es entender cuál necesitan de verdad: muchas veces es más pequeño de lo que pensaban.",
     "corpo":[
      ("Página web de empresa","Pocas páginas bien hechas, rápidas en el celular, accesibles y escritas con las palabras que sus clientes buscan en Google. Desde 350 € en un solo pago, o 24,80 € al mes con hosting y cambios incluidos."),
      ("Sitio bilingüe inglés y español","Dos versiones de verdad, con direcciones separadas y etiquetas hreflang correctas, para que cada idioma aparezca en sus propias búsquedas. Nada de traductores automáticos."),
      ("Tienda en línea","Productos, pagos, envíos y sales tax configurados correctamente, con Shopify o a medida, conectada a su inventario."),
      ("Apps móviles","Reservas, pedidos, fidelización y herramientas para equipos que trabajan en la calle, para iPhone y Android."),
      ("Software de gestión a medida","Inventario, trabajos, citas, cotizaciones y facturación, construido según cómo trabaja su empresa. Desde 1.500 €."),
      ("Integraciones","QuickBooks, Shopify, su CRM y las hojas de cálculo que nadie quiere dejar: conectados para no volver a teclear datos.")]}

def metodo():
    return {"id":"metodo","tipo":"passi","eyebrow":"Cómo trabajamos",
     "h2":"Precio cerrado,<br>sin <span class=\"grad\">sorpresas.</span>",
     "corpo":[
      ("Llamada gratuita de 30 minutos","Qué venden, a quién y qué tiene que hacer la página o el software. Sin presentaciones comerciales."),
      ("Cotización con precio fijo","Una cifra por escrito con todo lo necesario. No cambia a mitad del proyecto: lo nuevo se cotiza aparte y solo si lo piden."),
      ("Construcción por etapas","Ven algo funcionando en las primeras semanas y luego cada semana. Las correcciones se hacen durante el trabajo."),
      ("Publicación y después","Puesta en línea, revisión y capacitación. El dominio, las cuentas y el código quedan a nombre de su empresa.")]}

def faq_comunes(c, horas):
    return [
     ("¿Cuánto cuesta una página web?","Una página web de empresa cuesta 350 € en un solo pago, más 150 € si quieren la optimización inicial para Google y Bing, o 24,80 € al mes con dominio, hosting, mantenimiento y cambios incluidos, con permanencia mínima de 24 meses. Las apps web empiezan en 50 € al mes o 750 € en un pago; el software a medida, desde 1.500 €."),
     ("¿Cómo funciona la diferencia horaria con %s?" % c,"Italia va %d horas por delante. Las llamadas se hacen en su mañana, que es nuestra tarde, y el trabajo avanza mientras ustedes descansan: envían comentarios por la noche y por la mañana ven la nueva versión." % horas),
     ("¿Hablan español de verdad?","Sí. Trabajamos en español, inglés, italiano, francés y alemán. Las llamadas, los textos y el soporte pueden ser en español."),
     ("¿Cómo se paga y en qué moneda?","Los precios están en euros y se facturan en euros, sin IVA italiano para empresas de Estados Unidos. La mayoría de los clientes paga por transferencia internacional o tarjeta, y el banco convierte al cambio del día."),
     ("¿La página y el código serán nuestros?","Sí. En la opción de pago único, el dominio, el hosting, los contenidos y el código quedan a nombre de su empresa desde la publicación. Sin licencias atadas a nosotros."),
    ]

def ctabox(c):
    return {"h2":"¿Tienen un proyecto en %s?" % c,
            "p":"Media hora de videollamada gratuita, en español: les decimos qué necesitan de verdad, cuánto cuesta y en cuánto tiempo está en línea.",
            "btn":"Pedir cotización gratuita"}

CIUDADES = [
 # slug es, nombre, estado, horas, url inglesa
 ("miami","Miami","Florida",6,"/en/web-design-miami/"),
 ("houston","Houston","Texas",7,"/en/web-design-houston/"),
 ("los-angeles","Los Ángeles","California",9,"/en/web-design-los-angeles/"),
 ("nueva-york","Nueva York","Nueva York",6,"/en/web-design-new-york/"),
 ("san-antonio","San Antonio","Texas",7,"/en/web-design-san-antonio/"),
]

def otras(slug):
    return ([("Diseño web %s" % n, "/es/diseno-web-%s/" % s) for s,n,_,_,_ in CIUDADES if s != slug] +
            [("Estados Unidos: todas las ciudades","/es/estados-unidos/"),("Precios","/es/precios/")])

X = {}
X["miami"] = {
 "lead":"No estamos en Brickell. Somos un equipo de diez personas de desarrollo web y software en el norte de Italia, y trabajamos en español, inglés e italiano para empresas de Estados Unidos. Aquí explicamos qué construimos para negocios de Miami, cuánto cuesta y cuándo les conviene más una agencia local.",
 "sectores":[
  ("Bienes raíces y desarrolladores","Sitios de proyectos en preventa en español e inglés, portales para compradores e inversionistas y CRM para corredores que venden a clientes de varios países."),
  ("Comercio con América Latina","Portales de pedidos B2B, catálogos multilingües y seguimiento de envíos para importadores, exportadores y agentes de carga en Doral."),
  ("Restaurantes y hospitalidad","Menús rápidos en el celular, pedidos y reservas directas sin comisiones de las plataformas, y apps de fidelización."),
  ("Salud, estética y bienestar","Reservas en línea, formularios de ingreso y membresías, con manejo cuidadoso de los datos de salud."),
  ("Servicios profesionales","Sitios para abogados, contadores y consultores que aparecen en búsquedas concretas, y portales para clientes."),
  ("Marcas italianas en Florida","Comida, moda, diseño y náutica: sitios bilingües y tienda en línea preparada para el mercado de EE. UU.")],
 "mercado":[
  "Miami es el mercado más multilingüe del país, y la mayoría de los sitios lo maneja mal: una versión en español pasada por un traductor automático, o ninguna. Nosotros trabajamos nativamente en español, inglés e italiano y construimos sitios multilingües como Google espera: direcciones separadas, etiquetas hreflang correctas y textos escritos para cada público.",
  "Nuestros costos fijos son bajos, así que, para el mismo trabajo, la cotización es una fracción de la de una agencia de Brickell. Precio fijo, por escrito y por etapas.",
  "Florida es además uno de los estados con más demandas por <b>accesibilidad web (ADA)</b>. Todos nuestros sitios cumplen WCAG 2.1 AA y se prueban con teclado y lector de pantalla antes de publicarse."],
 "busqueda":[
  "En el sur de Florida se busca por zona: Brickell, Doral, Coral Gables, Hialeah, Kendall, Miami Beach, Fort Lauderdale. Un perfil de Google Business bien hecho y páginas para las zonas donde trabajan son el camino más rápido a las llamadas.",
  "La versión en español abre búsquedas en las que sus competidores, que solo tienen inglés, ni siquiera participan."],
 "faq":[("¿Hacen sitios en inglés y español a la vez?","Sí, de forma nativa: cada idioma con sus propias direcciones, etiquetas hreflang correctas y textos escritos para ese público.")],
}
X["houston"] = {
 "lead":"No estamos en el Energy Corridor. Somos un equipo de diez personas de desarrollo web y software en el norte de Italia, y trabajamos en español e inglés para empresas de Estados Unidos. Aquí explicamos qué construimos para negocios de Houston y cuánto cuesta.",
 "sectores":[
  ("Construcción y contratistas","Cotizaciones, reportes diarios con fotos, horarios de cuadrillas y control de horas, y sitios que traen llamadas de Katy, Pasadena o Sugar Land."),
  ("Servicios para el hogar","Aire acondicionado, plomería, techos, jardinería: sitios rápidos en el celular, en inglés y español, con citas en línea."),
  ("Energía y servicios de campo","Apps para técnicos que funcionan sin señal, inspecciones y mantenimiento de equipos."),
  ("Restaurantes y comida","Pedidos en línea sin comisiones, menús rápidos y fidelización para restaurantes y food trucks."),
  ("Clínicas y salud","Citas, formularios de ingreso y comunicación con pacientes, con manejo cuidadoso de los datos."),
  ("Puerto, logística e importación","Seguimiento de envíos, inventario y documentos para empresas que trabajan con el Puerto de Houston.")],
 "mercado":[
  "Una gran parte de los clientes de Houston busca en español, y casi ningún negocio local tiene una versión en español bien hecha. Eso es una oportunidad concreta: búsquedas con menos competencia y clientes que prefieren que les hablen en su idioma.",
  "Trabajamos con precio fijo, por escrito y por etapas, a una fracción del precio de una agencia local, porque nuestros costos fijos son bajos.",
  "Texas tiene su propia ley de privacidad, la <b>Texas Data Privacy and Security Act</b>. Construimos los formularios y el consentimiento de acuerdo con ella; su abogado confirma la parte legal."],
 "busqueda":[
  "Houston es enorme y se busca por zona: Katy, Pasadena, Pearland, Sugar Land, Spring, Cypress, The Woodlands. El perfil de Google Business y páginas por zona deciden quién recibe la llamada.",
  "Para servicios del hogar, la versión en español suele traer clientes que la competencia ni ve."],
 "faq":[("¿Sus apps funcionan sin señal?","Sí. La app guarda todo en el teléfono y se sincroniza sola cuando vuelve la conexión, con fotos, firmas y horas.")],
}
X["los-angeles"] = {
 "lead":"No estamos en Santa Mónica. Somos un equipo de diez personas de desarrollo web y software en el norte de Italia, y trabajamos en español e inglés para empresas de Estados Unidos. Aquí explicamos qué construimos para negocios de Los Ángeles y cuánto cuesta.",
 "sectores":[
  ("Restaurantes y comida","Pedidos y reservas directas, menús rápidos y fidelización, para no dejar el margen en las apps de entrega."),
  ("Moda y ropa","Tiendas en línea, catálogos para compradores mayoristas y control de producción para marcas del Fashion District."),
  ("Belleza y bienestar","Citas en línea, membresías y galerías que cargan rápido."),
  ("Construcción y servicios para el hogar","Cotizaciones, horarios y apps para cuadrillas, y sitios que traen llamadas del Valle, del Este de Los Ángeles o de Long Beach."),
  ("Importación y logística","Seguimiento de envíos, inventario y documentos alrededor de los puertos de Los Ángeles y Long Beach."),
  ("Comercio en línea","Tiendas Shopify o a medida, con sales tax, envíos y suscripciones configurados correctamente.")],
 "mercado":[
  "Los Ángeles es una de las áreas con más hispanohablantes del país, y muchos negocios atienden en español en persona pero no en su página web. Una versión en español bien hecha convierte esa ventaja en búsquedas y llamadas.",
  "Precio fijo, por escrito y por etapas, a una fracción de lo que cobra una agencia del Westside. Y la diferencia horaria juega a su favor: trabajamos mientras ustedes duermen.",
  "En California aplican la ley de privacidad <b>CCPA/CPRA</b> y las demandas por accesibilidad bajo la ADA y la Ley Unruh. Construimos según WCAG 2.1 AA y con un consentimiento de cookies que funciona de verdad."],
 "busqueda":[
  "En Los Ángeles nadie busca \"Los Ángeles\": se busca por ciudad y barrio — Boyle Heights, East LA, Huntington Park, Pasadena, Santa Ana, Long Beach, el Valle.",
  "Un perfil de Google Business bien hecho y páginas por zona, en inglés y en español, compiten en un campo mucho más pequeño que \"web design Los Angeles\"."],
 "faq":[("¿Nueve horas de diferencia es mucho?","Las llamadas se hacen temprano en su mañana, de 7 a 9 hora del Pacífico, y trabajamos mientras ustedes están desconectados. Funciona bien para revisiones semanales; no sirve si necesitan a alguien disponible por la tarde.")],
}
X["nueva-york"] = {
 "lead":"No estamos en Manhattan. Somos un equipo de diez personas de desarrollo web y software en el norte de Italia, y trabajamos en español e inglés para empresas de Estados Unidos. Aquí explicamos qué construimos para negocios de Nueva York y cuánto cuesta.",
 "sectores":[
  ("Restaurantes y bodegas","Menús rápidos, pedidos directos y fidelización para negocios en el Bronx, Queens, Washington Heights o Brooklyn."),
  ("Servicios profesionales","Sitios para abogados de inmigración, contadores y agencias de seguros que aparecen en búsquedas en español."),
  ("Construcción y servicios","Cotizaciones, reportes con fotos y control de horas para contratistas que trabajan en los cinco condados."),
  ("Salud y clínicas","Citas en línea y formularios de ingreso, con manejo cuidadoso de los datos de salud."),
  ("Comercio y distribución","Tiendas en línea y portales de pedidos para distribuidores de alimentos y productos."),
  ("Bienes raíces","Sitios de propiedades, portales para inquilinos y apps de mantenimiento.")],
 "mercado":[
  "Nueva York tiene una de las comunidades hispanas más grandes del país, y muchos negocios que atienden en español no tienen una página en español. Construirla bien abre búsquedas con poca competencia.",
  "Las agencias de Manhattan cobran precios de Manhattan. Nosotros trabajamos con precio fijo, por escrito y por etapas, a una fracción de ese costo.",
  "En Nueva York se presentan muchas <b>demandas por accesibilidad web (ADA)</b>, también contra pequeños negocios. Todos nuestros sitios cumplen WCAG 2.1 AA y se prueban antes de publicarse."],
 "busqueda":[
  "En Nueva York se busca por condado y barrio: el Bronx, Queens, Brooklyn, Washington Heights, Corona, Jackson Heights. El perfil de Google Business y páginas por zona traen las llamadas.",
  "Para abogados y servicios profesionales, las búsquedas en español sobre un problema concreto son pocas pero valen mucho."],
 "faq":[("¿Su sitio cumplirá con la ADA?","Construimos todos los sitios según WCAG 2.1 AA, el estándar al que se refieren los tribunales, y los probamos con teclado y lector de pantalla antes de publicarlos.")],
}
X["san-antonio"] = {
 "lead":"No estamos en el River Walk. Somos un equipo de diez personas de desarrollo web y software en el norte de Italia, y trabajamos en español e inglés para empresas de Estados Unidos. Aquí explicamos qué construimos para negocios de San Antonio y cuánto cuesta.",
 "sectores":[
  ("Servicios para el hogar y construcción","Sitios bilingües que traen llamadas, cotizaciones en línea y apps para cuadrillas."),
  ("Restaurantes y turismo","Menús, pedidos y reservas directas para negocios del centro y del River Walk."),
  ("Clínicas y salud","Citas, formularios de ingreso y comunicación con pacientes."),
  ("Proveedores militares y de defensa","Sitios de capacidades y herramientas internas para empresas que trabajan con las bases de la ciudad."),
  ("Comercio con México","Catálogos bilingües, pedidos B2B y seguimiento de envíos para empresas que trabajan a ambos lados de la frontera."),
  ("Negocios locales","Páginas rápidas y perfil de Google Business para negocios en Stone Oak, Alamo Heights, New Braunfels y Schertz.")],
 "mercado":[
  "San Antonio es una de las grandes ciudades más bilingües del país, y la mayoría de los sitios locales lo ignora. Una versión en español bien construida abre búsquedas que sus competidores no están atendiendo.",
  "Precio fijo, por escrito y por etapas, a una fracción del precio de una agencia local.",
  "Texas tiene su propia ley de privacidad, la <b>Texas Data Privacy and Security Act</b>; construimos los formularios y el consentimiento de acuerdo con ella."],
 "busqueda":[
  "Se busca por zona: Stone Oak, Alamo Heights, el Pearl, Medical Center, New Braunfels, Boerne. El perfil de Google Business y páginas por zona deciden las llamadas.",
  "La versión en español, para muchos negocios de servicios, es la puerta más grande."],
 "faq":[("¿Pueden atendernos en español?","Sí, llamadas, textos y soporte en español, y documentos en inglés cuando hagan falta.")],
}

for slug, c, st, h, en in CIUDADES:
    x = X[slug]
    url = "/es/diseno-web-%s/" % slug
    COPPIE[url] = en
    PAGINE.append({
     "lang":"es","url":url,
     "title":"Diseño Web en %s | Páginas Web, Apps y Software" % c if len("Diseño Web en %s | Páginas Web, Apps y Software" % c) <= 60 else "Diseño Web en %s | Páginas Web y Apps" % c,
     "desc":"Páginas web, apps y software para negocios de %s, en español e inglés: precio fijo, accesibles, en línea en semanas y a nombre de su empresa." % c,
     "ogtitle":"Diseño web en %s — Danova Tech" % c,
     "ogdesc":"Páginas web bilingües, apps y software a medida para negocios de %s, con precio fijo y en español." % c,
     "crumbs":[("Estados Unidos","/es/estados-unidos/"),(c,None)],
     "eyebrow":"%s, %s" % (c, st),
     "h1":"Diseño web<br>para <span class=\"grad\">negocios de %s.</span>" % c,
     "lead":x["lead"],
     "cta1":"Pedir cotización gratuita","cta2":"Qué construimos",
     "sezioni":[servicios(c),
      {"id":"sectores","tipo":"cards","eyebrow":"Sectores","h2":"Lo que construimos<br>para <span class=\"grad\">%s</span>" % c,"corpo":x["sectores"]},
      {"id":"mercado","tipo":"testo","eyebrow":"La realidad","h2":"Por qué un equipo en Italia<br>tiene sentido <span class=\"grad\">para %s</span>" % c,"corpo":x["mercado"]+[
        "<b>Cuándo no somos la opción correcta.</b> Si necesitan a alguien en su oficina cada semana, disponible por chat toda la tarde, o un equipo de quince personas para un programa enorme, les conviene una empresa local, y se lo decimos en la primera llamada."]},
      {"id":"busqueda","tipo":"testo","eyebrow":"Aparecer en Google","h2":"Búsquedas en %s:<br>entrar por <span class=\"grad\">la puerta estrecha.</span>" % c,"corpo":x["busqueda"]},
      metodo()],
     "faqtitle":"Las preguntas de <span class=\"grad\">%s.</span>" % c,
     "faq":x["faq"] + faq_comunes(c, h),
     "ctabox":ctabox(c),
     "altrititle":"Páginas relacionadas",
     "altri":[("Web design %s (English)" % c.replace("Á","A").replace("Nueva York","New York"), en)] + otras(slug),
     "svc":{"name":"Diseño web y software para %s" % c,"type":"Diseño de páginas web, apps y software a medida",
            "desc":"Páginas web bilingües, tiendas en línea, apps y software a medida para negocios de %s, %s, con precio fijo y atención en español." % (c, st),
            "area":area(c, st),"lingue":["Spanish","English","Italian"],
            "catalogo":["Página web de empresa","Sitio bilingüe inglés y español","Tienda en línea","Apps móviles","Software a medida","Posicionamiento en Google"]},
    })

PAGINE.append({
 "lang":"es","url":"/es/estados-unidos/",
 "title":"Páginas Web y Software para Empresas en Estados Unidos",
 "desc":"Páginas web bilingües, apps y software a medida para negocios en Estados Unidos, en español: precio fijo, accesibles y a nombre de su empresa. Desde 350 €.",
 "ogtitle":"Danova Tech para negocios en Estados Unidos",
 "ogdesc":"Un equipo de diez personas en Italia que construye páginas web, apps y software para negocios en Estados Unidos, en español e inglés.",
 "crumbs":[("Estados Unidos",None)],
 "eyebrow":"Estados Unidos",
 "h1":"Páginas web, apps y software<br>para <span class=\"grad\">negocios en EE. UU.</span>",
 "lead":"Somos un equipo de diez personas de desarrollo web y software en el norte de Italia. Trabajamos en español e inglés para negocios de todo Estados Unidos, con precio fijo por escrito, sitios accesibles y todo a nombre de su empresa.",
 "cta1":"Pedir cotización gratuita","cta2":"Qué construimos",
 "sezioni":[servicios("Estados Unidos"),
  {"id":"ciudades","tipo":"testo","eyebrow":"Dónde trabajamos","h2":"Ciudades con <span class=\"grad\">página propia</span>",
   "corpo":["Trabajamos a distancia con negocios de cualquier parte del país. Para las ciudades con más clientes hispanohablantes hemos escrito una página sobre el mercado local:",
            " · ".join('<a href="/es/diseno-web-%s/">%s</a>' % (s, n) for s,n,_,_,_ in CIUDADES),
            "En inglés tenemos páginas para más de treinta ciudades: <a href=\"/en/united-states/\">ver todas</a>."]},
  {"id":"bilingue","tipo":"testo","eyebrow":"La oportunidad","h2":"El español<br>es <span class=\"grad\">una ventaja.</span>",
   "corpo":["Decenas de millones de personas en Estados Unidos hablan español en casa, y muchas buscan en español. Sin embargo, la mayoría de los negocios que atienden en español no tiene una página en español, o tiene una traducción automática que Google ignora.",
            "Una versión en español bien hecha — direcciones separadas, etiquetas hreflang, textos escritos para ese público — compite en búsquedas con mucha menos competencia que las de inglés.",
            "Y la construimos accesible según WCAG 2.1 AA, porque las demandas por accesibilidad web son frecuentes en Estados Unidos."]},
  metodo()],
 "faqtitle":"Preguntas <span class=\"grad\">frecuentes.</span>",
 "faq":faq_comunes("su ciudad", 6)[:1] + [
   ("¿Cómo funciona la diferencia horaria?","Italia va seis horas por delante de la costa Este, siete de la hora del Centro y nueve de la costa Oeste. Las llamadas se hacen en su mañana y el trabajo avanza mientras ustedes descansan.")
 ] + faq_comunes("su ciudad", 6)[2:],
 "ctabox":ctabox("Estados Unidos"),
 "altrititle":"Páginas relacionadas",
 "altri":[("Diseño web %s" % n, "/es/diseno-web-%s/" % s) for s,n,_,_,_ in CIUDADES] +
         [("US businesses (English)","/en/united-states/"),("Precios","/es/precios/")],
 "svc":{"name":"Páginas web y software para negocios en Estados Unidos","type":"Diseño de páginas web, apps y software a medida",
        "desc":"Páginas web bilingües, tiendas en línea, apps y software a medida para negocios en Estados Unidos, con atención en español y precio fijo.",
        "area":[US],"lingue":["Spanish","English","Italian"],
        "catalogo":["Página web de empresa","Sitio bilingüe","Tienda en línea","Apps móviles","Software a medida"]},
})
COPPIE["/es/estados-unidos/"] = "/en/united-states/"
