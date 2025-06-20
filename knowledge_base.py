#Base de Conocimiento del chatbot EscoMentor

knowledge_base = [
    {
    "pregunta" : "¿Cómo me doy de baja de una materia?",
    "palabras_clave" : ["baja", "dar de baja", "eliminar", "quitar", "cancelar", "materia", "unidad de aprendizaje", "curso", "asignatura", "tramite", "proceso", "formulario"],
    "respuesta" : "Debes de completar el formulario de Baja de una Materia durante las primeras semanas del semestre. Puedes encontrar el formulario aquí: <a href='https://www.escom.ipn.mx/SSEIS/gestionescolar/servicios/tramite.php' target='_blank'>Formulario de Baja de Materia</a>",
    "categoria": "Trámites"
    },
    {
    "pregunta" : "¿Cómo me inscribo?",
    "palabras_clave" : ["inscripción", "inscribir", "inscribirme", "proceso", "registro", "primer semestre", "nuevo ingreso", "grupo", "asignación", "periodo", "fecha"],
    "respuesta" : "En primer semestre, la inscripción no la realizas tú directamente. Debes estar al pendiente del <a href='https://www.escom.ipn.mx' target='_blank'>sitio oficial de ESCOM</a>. Días previos al inicio del semestre, se habilitará un minisitio donde podrás consultar el grupo y horario en el que fuiste asignado.",
    "categoria": "Trámites"
    },
   {
    "pregunta" : "¿Cómo hago mi reinscripción?",
    "palabras_clave" : ["reinscripción", "reinscribir", "proceso", "siguiente semestre", "semestre", "saes", "fecha", "promedio", "situación escolar", "cita", "inscripción"],
    "respuesta" : "A partir de tu segundo semestre, el proceso de reinscripción se realiza a través del sistema SAES. En el <a href='https://www.escom.ipn.mx' target='_blank'>sitio oficial de ESCOM</a> y sus redes sociales podrás consultar las fechas específicas, que dependen de tu promedio y situación escolar. También podrás ver tu cita de reinscripción directamente en el SAES, en la pestaña de 'Reinscripción'.",
    "categoria": "Trámites"
    },
    {
    "pregunta" : "¿Cómo puedo solicitar una constancia de estudio?",
    "palabras_clave" : ["constancia", "estudio", "solicitar", "pedir", "tramite", "certificado", "documento", "historial", "académico", "papeleo", "gestión"],
    "respuesta" : "Para solicitar una constancia de estudio, debes acceder a la sección de Trámites Escolares desde el sitio web de ESCOM. Puedes encontrar el formulario y los pasos <a href='https://www.escom.ipn.mx/SSEIS/gestionescolar/servicios/tramite.php' target='_blank'>aquí</a>. Deberás registrarte en el sitio y completar el formulario correspondiente.",
    "categoria": "Trámites"
    },
    {
    "pregunta" : "¿Qué materias llevaré en el primer semestre?",
    "palabras_clave" : ["materias", "primer semestre", "plan curricular", "carrera", "asignaturas", "unidades de aprendizaje", "clases", "temario"],
    "respuesta" : "Las materias que llevarás en el primer semestre dependen de tu carrera. Sin embargo, todos los alumnos cursarán las siguientes materias base: <ul><li><strong>Fundamentos de Programación</strong></li><li><strong>Comunicación Oral y Escrita</strong></li><li><strong>Cálculo</strong></li><li><strong>Matemáticas Discretas</strong></li></ul><br>Además de estas, llevarás materias específicas según tu ingeniería: <ul><li><strong>Ingeniería en Sistemas Computacionales (ISC):</strong> Análisis Vectorial</li><li><strong>Ingeniería en Inteligencia Artificial (IIA):</strong> Fundamentos Económicos y Mecánica y Electromagnetismo</li><li><strong>Licenciatura en Ciencia de Datos (LCD):</strong> Introducción a la Ciencia de Datos</li></ul>",
    "categoria": "Planes Académicos"
    },
    {
    "pregunta" : "¿ESCOM tiene clubes?",
    "palabras_clave" : ["club", "clubes", "asociación", "grupo", "sociedad", "organización", "actividad", "extracurricular", "deporte", "cultural", "participar", "unir", "pertenecer", "lista", "directorio"],
    "respuesta" : "¡Sí! ESCOM cuenta con diversos clubes estudiantiles. Puedes consultar la lista completa y sus detalles <a href='https://www.escom.ipn.mx/htmls/escomunidad/clubs.php' target='_blank'>aquí</a>. Además de los clubes, también hay una gran variedad de actividades deportivas y culturales para que te integres a la vida universitaria.",
    "categoria": "Vida Universitaria"
    },
    {
    "pregunta" : "¿Con qué servicios cuenta ESCOM?",
    "palabras_clave" : ["servicio", "servicios", "estudiantil", "salud", "médico", "odontología", "orientación", "apoyo", "disponible", "ayuda", "atención", "departamento"],
    "respuesta" : "ESCOM cuenta con varios servicios para sus estudiantes. Se ofrece servicio médico, de odontología y de orientación académica. Puedes consultar los horarios y los encargados <a href='https://www.escom.ipn.mx/SSEIS/serviciosestudiantiles/servicios/serviciosSalud.php' target='_blank'>aquí</a>.",
    "categoria": "Servicios Estudiantiles"
    },
    {
    "pregunta" : "¿ESCOM ofrece becas?",
    "palabras_clave" : ["beca", "becas", "apoyo", "apoyos", "ayuda", "económica", "financiera", "institucional", "excelencia", "telmex", "convocatoria", "solicitar", "obtener", "beneficio"],
    "respuesta" : "¡Sí! ESCOM ofrece tres tipos de beca institucional,la beca de excelencia de Telmex, la de transporte y becas tanto culturales como deportivas. Las convocatorias se publican al inicio del semestre. Para más información, accede al siguiente enlace: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
    "categoria": "Becas y Apoyos"
    },
    {
	"pregunta" : "=Como se solicita una beca?",
	"palabras_clave" : ["solicitud","beca", "solicitud de beca", "proceso","proceso de solicitud","convocatoria"],
	"respuesta" : "Primero deberás esperar a la publicación de la convocatoria, suele salir durante los primeros dos meses del semestre, así que te recomendamos estar al pendiente de las redes sociales de <a href=https://web.facebook.com/escomipnmx/?locale=es_LA&_rdc=1&_rdr# target='_blank'>ESCOM</a> y la <a href= https://www.facebook.com/IPNDAES target='_blank'>Dirección de Apoyo a Estudiantes del IPN</a>. Después de eso deberás de registraste en el <a href=https://www.sibec.ipn.mx/registro/accesoRegistro.action target='_blank'>SIBec</a> y completar el estudio socioeconómico durante las fechas de la convocatoria. Por último, deberás de entregar la documentación que te solicite la conovcatoria y esperar a los resultados. Si no obtienes la beca tienes derecho a la Reconsideración en los días próximos, deberás de estar al pendiente de la publicación, puesto que también está limitado por fechas. Si quieres revisar el proceso más a detalle puedes consultar el siguiente enlace: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
	"categoría" : "Becas",
	},
    {
    "pregunta" : "¿Dónde se encuentra ESCOM?",
    "palabras_clave" : ["donde", "ubicación", "dirección", "llegar", "localización", "mapa", "metro", "autobus", "trolebús", "direccion", "encuentra", "situado"],
    "respuesta" : "ESCOM se encuentra en la siguiente dirección. Puedes llegar en metro (estación Politécnico de la Línea 5), la Línea 8 del trolebús o una de las rutas de autobús cercanas. Puedes acceder a más información <a href='https://www.escom.ipn.mx/htmls/conocenos/ubicacion.php' target='_blank'>aquí</a>.",
    "categoria": "Ubicación"  
    },
    {
    "pregunta" : "¿En qué consiste la beca institucional?",
    "palabras_clave" : ["beca", "institucional", "ipn", "politencia", "promedio", "requisitos", "monto", "cantidad", "beneficio", "regular", "inscrito"],
    "respuesta" : "Para acceder a la beca institucional, debes ser un alumno inscrito, en situación académica regular y con promedio mayor a 7.0. El monto para nivel superior es de $6,600. Puedes consultar más información en el siguiente enlace: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
    "categoria" : "Becas"
    },
    {
	"pregunta" : "¿En qué consiste la beca TELMEX-TELCEL?",
	"palabras_clave" : ["beca","beca TELMEX", "beca telmex", "telmex", "TELMEX"],
	"respuesta" : "La beca de excelencia TELMEX-TELCEL está dirigida a alumnos con un promedio académico muy alto. En ESCOM, necesitas tener un promedio superior a 9.0 y ser un alumno regular. Como alumno de nuevo ingreso, aún no puedes solicitarla, ya que requieres haber cursado al menos el 30% del total de los créditos de tu carrera. Puedes consultar tu avance de créditos en el SAES, en la pestaña de 'Reinscripción'. Cuando puedas aplicar el monto es el equivalente a un salario mensual mínimo vigente de la Ciudad de México. Para más detalles, visita: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
	"categoría" : "Becas",
    },
    {
    "pregunta" : "¿En qué consiste la beca de transporte?",
    "palabras_clave" : ["beca", "transporte", "pasajes", "traslado", "gasto", "movilidad", "ayuda", "económica", "monto", "requisitos", "comprobante"],
    "respuesta" : "La beca de transporte está diseñada para apoyar a los alumnos que gastan más de $500 pesos mensuales en pasajes. Se requiere un comprobante de tus costos de transporte para poder recibir un monto de $200 pesos mensuales.<br><br>Para más información, visita el: <a href='https://www.escom.ipn.mx/htmls/escomunidad/becas.php' target='_blank'>Portal de Becas de ESCOM</a>",
    "categoria" : "Becas"
    },
	{
    "pregunta" : "¿En qué consiste la beca de excelencia?",
    "palabras_clave" : ["beca", "excelencia", "alto promedio", "promedio", "requisitos", "regular", "creditos", "saes", "apoyo", "talento", "academico", "merito", "monto", "cantidad"],
    "respuesta" : "La beca de excelencia está dirigida a alumnos con un promedio académico muy alto. En ESCOM, necesitas tener un promedio superior a 9.0 y ser un alumno regular. Como alumno de nuevo ingreso, aún no puedes solicitarla, ya que requieres haber cursado al menos el 30% del total de los créditos de tu carrera. Puedes consultar tu avance de créditos en el SAES, en la pestaña de 'Reinscripción'. Cuando puedas aplicar, el monto es de <strong>$19,000</strong>.<br><br>Para más detalles, visita: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
    "categoria" : "Becas"
    },
    {
    "pregunta" : "¿En qué consiste la beca cultural?",
    "palabras_clave" : ["beca", "cultural", "actividad cultural", "requisitos", "promedio", "adeudos", "situación regular", "participar", "difusión cultural", "saes", "monto", "apoyo"],
    "respuesta" : "La beca cultural es para alumnos con un promedio mínimo de 7.0, en situación regular y con un máximo de 2 adeudos. Deberás participar en alguna actividad cultural avalada por la <a href='https://www.ipn.mx/cultura/' target='_blank'>Dirección de Difusión Cultural del IPN</a>. Es importante que esta actividad esté registrada en el SAES, por lo que tendrás que ponerte en contacto con el <a href='https://www.escom.ipn.mx/SSEIS/serviciosestudiantiles/' target='_blank'>Departamento de Servicios Estudiantiles</a>. El monto de esta beca para nivel superior es de $7,000.<br><br>Para más detalles, visita: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
    "categoria" : "Becas"
    },
    {
    "pregunta" : "¿En qué consiste la beca deportiva?",
    "palabras_clave" : ["beca", "deportiva", "deporte", "actividad deportiva", "actividades deportivas", "requisitos", "promedio", "regular", "participar", "saes", "monto", "apoyo", "talento"],
    "respuesta" : "La beca deportiva está disponible para alumnos con un promedio mínimo de 7.0 y en situación académica regular. Debes participar en alguna actividad deportiva avalada por la <a href='http://www.ipn.mx/deportes/' target='_blank'>Dirección de Actividades Deportivas del IPN</a>. Es muy importante que esta actividad esté registrada en el SAES, para lo cual deberás contactar al <a href='https://www.escom.ipn.mx/SSEIS/serviciosestudiantiles/' target='_blank'>Departamento de Servicios Estudiantiles</a>. El monto de esta beca para nivel superior es de $7,000.<br><br>Para más detalles, visita: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
    "categoria" : "Becas"
    },
    {
    "pregunta" : "¿En qué consiste la beca de Bécalos?",
    "palabras_clave" : ["beca", "bécalos", "becalos", "promedio", "requisitos", "apoyo"],
    "respuesta" : "La beca de Bécalos está dirigida a alumnos con un promedio superior a 8.0.<br><br>Para más detalles, visita: <a href='https://www.escom.ipn.mx/SSEIS/apoyoseducativos/servicios/becas.php' target='_blank'>Becas y otros apoyos de ESCOM</a>",
    "categoria" : "Becas"
    },
    {
	"pregunta" : "¿Quién es el responsable de las becas",
	"palabras_clave" : ["becas","encargado","responsable","departamento"],
	"respuesta" : "Si tienes más dudas respecto a becas la persona encargada es la Lic. Martha Angélica Gasca Cervantes. Puedes contactarla al siguiente número telefónico 57296000 Ext. 52056,o al siguiente correo <a href='mailto:becas.escom@ipn.mx'>becas.escom@ipn.mx</a>.",
	"categoría" : "",
	},
    {
	"pregunta" : "¿Cuál es la oferta educativa de ESCOM?",
	"palabras_clave" : ["oferta educativa","oferta","carreras"],
	"respuesta" : "ESCOM ofrece tres carreras en modalidad escolarizada: <ul><li>Ingenieria en Sistemas Computacionales (ISC)</li><li>Ingeniería en Inteligencia Artificial (IIA)</li><li>Licenciatura en Ciencia de Datos (LCD)</li></ul>",
	"categoría" : "Planes Académicos",
	},
    {
	"pregunta" : "¿Cuál es el plan de estudios de Ingeniería en Sistemas Computacionales?",
	"palabras_clave" : ["Ingeniería en Sistemas Computacionales","ISC"],
	"respuesta" : "Puedes consultar el plan de estudios de Ingeniería en Sistemas Computacionales en el siguiente enlace: <a href=https://www.escom.ipn.mx/htmls/oferta/mapaCurrISC2020.php target='_blank'> Plan de Ingenieria en Sistemas Computacionales</a>.<br> También puedes consultar más información de esta carrera en el siguiente enlace: <a href=https://www.escom.ipn.mx/htmls/oferta/isc2020.php target='_blank'>Ingeniería en Sistemas Computacionales (Oferta Educativa)</a>.<br> También puedes consultarlo en formato PDF <a href='/static/docs/mapaCurricularISC2020.pdf' target='_blank'>aquí.",
	"categoría" : "Planes Académicos",
	},
    {
	"pregunta" : "¿Cuál es el plan de estudios de Ingeniería en Inteligencia Artificial?",
	"palabras_clave" : ["Ingeniería en Inteligencia Artificial","IIA"],
	"respuesta" : "Puedes consultar el plan de estudios de Ingeniería en Sistemas Computacionales en el siguiente enlace: <a href=https://www.escom.ipn.mx/htmls/oferta/mapaCurrIIA2020.php target='_blank'> Plan de Ingenieria en Inteligencia Artificial</a>.<br> También puedes consultar más información de esta carrera en el siguiente enlace: <a href=https://www.escom.ipn.mx/htmls/oferta/iia2020.php target='_blank'>Ingeniería en Inteligencia Artificial (Oferta Educativa)</a>.<br> También puedes consultarlo en formato PDF <a href='/static/docs/mapaCurricularIIA2020.pdf' target='_blank'>aquí.",
	"categoría" : "Planes Académicos",
	},
    {
	"pregunta" : "¿Cuál es el plan de estudios de la Licenciatura en Ciencia de Datos?",
	"palabras_clave" : ["Licenciatura en Ciencia de Datos","LCD"],
	"respuesta" : "Puedes consultar el plan de estudios de la Licenciatura en Ciencia de Datos en el siguiente enlace: <a href=https://www.escom.ipn.mx/htmls/oferta/mapaCurrLCD2020.php target='_blank'> Plan de la Licenciatura en Ciencia de Datos</a>.<br> También puedes consultar más información de esta carrera en el siguiente enlace: <a href='https://www.escom.ipn.mx/htmls/oferta/lcd2020.php' target='_blank'>Licenciatura en Ciencia de Datos (Oferta Educativa)</a>.<br> También puedes consultarlo en formato PDF <a href='/static/docs/mapaCurricularLCD2020H.pdf' target='_blank'>aquí.",
	"categoría" : "Planes Académicos",
	},
    {
	"pregunta" : "¿Por dónde puedo acceder a escom?",
	"palabras_clave" : ["acceso","acceder", "puntos de acceso"],
	"respuesta" : "ESCOM cuenta con dos accesos. Uno de ellos es por el Eje Central Lázaro Cardénas y el otro acceso es por la Av.Juan de Dios Bátiz. Ambos accesos cuentan con seguridad en la entrada, por lo que deberás de tener preparada tu credencial de estudiante o comprobante de horario, el cual puedes descargar de tu SAES.",
	"categoría" : "Ubicación",
	},
    {
	"pregunta" : "¿Qué medios de transporte me ayudan a llegar a ESCOM?",
	"palabras_clave" : ["medios de transporte","llegada","llegar","cómo"],
	"respuesta" : "Puedes llegar en Metro (Estación Politécnico--Linea 5), en Metrobús (Estacion Instituto Politecnico Nacional--Linea 6) o Trolebús (Parada ESCOM--Linea 8) ",
	"categoría" : "Ubicación",
	},
    {
	"pregunta" : "¿Cuáles son las redes sociales de ESCOM?",
	"palabras_clave" : ["redes sociales","facebook", "twitter","x","instagram"],
	"respuesta" : "Puedes encontrar a ESCOM en las siguientes redes sociales: <br><ul><li><a href=https://web.facebook.com/escomipnmx/?locale=es_LA&_rdc=1&_rdr# target='_blank'>Facebook</a></li><a href=https://x.com/escomunidad target='_blank'>X(antes Twitter)</a><li><a href=https://www.instagram.com/escom_ipn_mx/?utm_source=ig_embed&ig_rid=9249bb21-a724-420c-be0d-0c9000c46013 target='_blank'>Instagram</a></li></ul>",
	"categoría" : "Ubicación",
	},
    {
	"pregunta" : "¿Cuáles clubes existen en ESCOM?",
	"palabras_clave" : ["club","clubes"],
	"respuesta" : "En la página oficial de ESCOM puedes encontrar 6 clubes:<br><ul><li><a href=https://www.facebook.com/CMR.ESCOM/ target='_blank'>Club de Minirobótica</a></li><a href=https://www.facebook.com/algoritmiaescom/ target='_blank>Club de Algoritmia</a><li><a href=https://www.comunidad.escom.ipn.mx/biorobotica/ target='_blank>Club de Bio-Robótica</a></li><a href=https://web.facebook.com/profile.php?id=100063692365456&locale=es_LA target='blank'>Developer Student Club</a><li></li><a href=https://www.facebook.com/CSI.ESCOM.oficial target='_blank>Club de Seguridad y Hacking Ético</a><li><a href=https://www.instagram.com/weare_tukey/# target='_blank>Club de Ciencia Datos</a></li></ul><br>Sin embargo, existen otros clubes que no se encuentran en la página oficial de ESCOM, esto suele ocurrir ya sea porque son clubes más nuevos o clubes que no cuentan con un profesor encargado de manera oficial. Te recomendamos revisar en los diferentes grupos de Facebook de la escuela y los carteles que puedas ver en la escuela, seguro que hay algún club que te interesa.<br>ESCOM también tiene actividades culturales y deportivas que son aparte de los clubes.",
	"categoría" : "Vida Universitaria",
	},
    {
	"pregunta" : "¿Cómo puedo ingresar a un club?",
	"palabras_clave" : ["ingresar","club","registro"],
	"respuesta" : "Al inicio del semestre se publica un formulario para que te puedas unir a los clubes en las redes sociales de ESCOM. Por norma general, no hay requisitos de entrada, pero ciertos clubes, como el de Algoritmia te harán un examen de ingreso. Te recomendamos acercarte al club al que desees unirte para preguntarles directamente.",
	"categoría" : "Vida Universitaria",
	},
    {
    "pregunta" : "¿Dónde puedo encontrar la biblioteca?",
    "palabras_clave" : ["biblioteca", "ubicación", "donde", "encontrar", "plano", "mapa", "croquis", "edificio", "gobierno"],
    "respuesta" : "La biblioteca se encuentra en la planta baja del Edificio de Gobierno. Aquí tienes el croquis del edificio: <a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edifGobierno.png' target='_blank'>Croquis del Edificio de Gobierno</a>.",
    "categoria" : "Instalaciones"
    },
    {
	"pregunta" : "¿Que debo hacer si pierdo mi credencial de estudiante?",
	"palabras_clave" : ["perdí","pérdida","credencial","reponer"],
	"respuesta" : "Debes acudir a una ventanilla de Gestión Escolar y solicitar una reposición, ten en cuenta que se te hará un cobro por la reposición y tardará de 2 a 5 dias habiles la entrega de tu credencial.",
	"categoría" : "Trámites",
	},
    {
	"pregunta" : "¿Dónde está el servicio médico?",
	"palabras_clave" : ["servicio médico","donde",],
	"respuesta" : "El Servicio Médico de ESCOM se encuentra en la planta baja del Edificio de Gobierno, en la misma habitación que el Servicio de Odontología. Aquí tienes el croquis del edificio: <a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edifGobierno.png' target='_blank'>Croquis del Edificio de Gobierno</a>.",
	"categoría" : "Servicios Estudiantiles",
	},
    {
	"pregunta" : "¿Dónde está el servicio de odontología?",
	"palabras_clave" : ["odontología","dónde","ubicación", "en dónde"],
	"respuesta" : "El Servicio de Odontología de ESCOM se encuentra en la planta baja del Edificio de Gobierno, en la misma habitación que el Servicio Médico. Aquí tienes el croquis del edificio: <a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edifGobierno.png' target='_blank'>Croquis del Edificio de Gobierno</a>.",
	"categoría" : "Servicios Estudiantiles",
	},
    {
	"pregunta" : "¿Cuál es el mapa de ESCOM?",
	"palabras_clave" : ["mapa","croquis","ubicación","edificios","instalaciones","escom"],
	"respuesta" : "ESCOM está dividido en 7 edificios, y tiene otras instlaciones como zonas de estudio (conocidas como palapas), zonas deportivas, cafeterías y papelerías. Aquí está el mapa: <a href='https://pbs.twimg.com/media/FpOHuWdXgAAp8EN?format=jpg&name=4096x4096' target='_blank'>Mapa de ESCOM</a>.<br>Si te pierdes o no encuentras un salón en específico no dudes en preguntar a algún profesor o otro alumno, la comunidad de ESCOM es siempre muy agradable y no dudarán en ayudarte.",
	"categoría" : "Instalaciones",
	},
    {
    "pregunta" : "¿Dónde está mi salón?",
    "palabras_clave" : ["salón", "salones", "donde", "clases", "salón de clase", "salones de clase", "ubicación", "edificio", "aulas", "localizar", "encontrar", "croquis", "mapa"],
    "respuesta" : "Las clases se imparten en los edificios del 1 al 5. Puedes revisar en qué edificio se encuentra tu salón con el siguiente croquis general del campus: <a href='https://pbs.twimg.com/media/FpOHuWdXgAAp8EN?format=jpg&name=4096x4096' target='_blank'>Mapa General de ESCOM</a>.<br><br>Por norma general, los alumnos de ISC toman clases en los edificios 1 y 2. Los alumnos de IIA y LCD tienen clases en los edificios 3, 4 y 5. Aquí están los croquis de cada edificio para que te ubiques mejor:<br><ul><li><a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edificio1.png' target='_blank'>Croquis del Edificio 1</a></li><li><a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edificio2.png' target='_blank'>Croquis del Edificio 2</a></li><li><a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edificio3.png' target='_blank'>Croquis del Edificio 3</a></li><li><a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edificio4.png' target='_blank'>Croquis del Edificio 4</a></li><li><a href='https://www.escom.ipn.mx/docs/conocenos/ubicacion/croquisESCOM2022_edificio5.png' target='_blank'>Croquis del Edificio 5</a></li></ul>",
    "categoria" : "Instalaciones"
    },
    {
	"pregunta" : "¿Cuáles son las actividades culturales?",
	"palabras_clave" : ["actividades culturales","actividades","culturales","cultura","arte","artísticas","artística"],
	"respuesta" : "Las actividades culturales que ofrece ESCOM son: <br><ul><li>Artes Plásticas</li><li>Creación literaria</li><li>Teatro</li><li>Tuna ESCOM (similar a la estudiantina)</li><li>Algoritmo de Baile</li><li>Club de Anime.</li></ul><br>Para más información sobre las actvidades culturales puedes acceder al siguiente enlace: <a href='https://www.escom.ipn.mx/SSEIS/serviciosestudiantiles/servicios/actsCulturales.php' target='_blank'>Actividades Culturales.</a>",
	"categoría" : "Vida Universitaria",
	},
    {
	"pregunta" : "¿Quién es la persona encargada de las actividades culturales?",
	"palabras_clave" : ["actividades culturales","encargado","responsable","persona encargada","persona a cargo","culturales"],
	"respuesta" : "Si tienes más dudas con las actividades culturales la persona encargada es el Lic. Álvaro Olvera Toral. Lo puedes contactar a través del siguiente número telefónico: 57296000 Ext. 52063, o al siguiente correo: <a href='mailto:cultura_y_deportes_escom@ipn.mx'>cultura_y_deportes_escom@ipn.mx</a>",
	"categoría" : "Vida Universitaria",
	},
    {
	"pregunta" : "¿Cuáles son las actividades deportivas?",
	"palabras_clave" : ["actividades deportivas","deporte","actividad","deportes","competencia","ofrece","cuales"],
	"respuesta" : "Las actividades deportivas que ofrece ESCOM son: <ul><li>Fútbol: soccer, siete y rápido</li><li>Voleibol</li><li>Taekwondo</li><li>Ajedrez</li><li>Barras</li><li>Basquetbol</li><li>Ping Pong</li><li>Tochito Bandera</li></ul><br>Las actividades deportivas ofrecidas por ESCOM se dividen en formato varonil y femenil.",
	"categoría" : "Vida Universitaria",
	},
    {
	"pregunta" : "¿Quién es la persona encargada de las actividades deportivas?",
	"palabras_clave" : ["actividades deportivas","encargado","responsable","persona encargada","persona a cargo","deportivas"],
	"respuesta" : "Si tienes más dudas con las actividades deportivas la persona encargada es el Lic. Álvaro Olvera Toral. Lo puedes contactar a través del siguiente número telefónico: 57296000 Ext. 52063, o al siguiente correo: <a href='mailto:cultura_y_deportes_escom@ipn.mx'>cultura_y_deportes_escom@ipn.mx</a>",
	"categoría" : "Vida Universitaria",
	},   
    {
	"pregunta" : "¿Quién es la persina encargada del servicio médico?",
	"palabras_clave" : ["servicio médico","encargado","persona responsable","persona encargada","persona a cargo","médico"],
	"respuesta" : "Si tienes más dudas del servicio médico te puedes poner en contacto con alguno de los doctores responsables en tu turno. Si estás en el turno matutino los doctores encargados son: la Dra. Aideé Lizbeth Galván Zermeño y el Dr. Daniel Mauricio Temozihui Trejo. Si por el contrrio, estás en el turno vespertino los doctores encargados son: el Dr. Óscar Cortés Jiménez y el Dr. Cuauhtémoc Garcóa Hidalgo. Puedes ponerte en contacto con el servicio médico a través del siguiente número telefónico: 57296000 Ext. 52014, ten en cuenta que el horario es a partir de las 8 de la mañana y hasta las 3 de la tarde en el turno matutino y de las 4 de la tarde a las 8 de la noche en el turno vespertino. ",
	"categoría" : "",
	},
]

default_response = "Lo siento, por el momento no puedo responder la pregunta. Puedes consultar en el sitio web oficial de ESCOM o sus redes sociales para encontrar más información."
