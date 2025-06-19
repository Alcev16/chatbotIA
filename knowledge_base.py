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
	"respuesta" : "Puedes consultar el plan de estudios de la Licenciatura en Ciencia de Datos en el siguiente enlace: <a href=https://www.escom.ipn.mx/htmls/oferta/mapaCurrLCD2020.php target='_blank'> Plan de la Licenciatura en Ciencia de Datos</a>.<br> También puedes consultar más información de esta carrera en el siguiente enlace: <a href=https://www.escom.ipn.mx/htmls/oferta/iia2020.phphttps://www.escom.ipn.mx/htmls/oferta/lcd2020.php target='_blank'>Licenciatura en Ciencia de Datos (Oferta Educativa)</a>.<br> También puedes consultarlo en formato PDF <a href='/static/docs/mapaCurricularLCD2020H.pdf' target='_blank'>aquí.",
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
]

default_response = "Lo siento, por el momento no puedo responder la pregunta. Puedes consultar en el sitio web oficial de ESCOM o sus redes sociales para encontrar más información."
