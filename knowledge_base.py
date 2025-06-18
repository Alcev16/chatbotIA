#Base de Conocimiento del chatbot EscoMentor

knowledge_base = [
    {
    "pregunta" : "¿Cómo me doy de baja de una materia?",
    "palabras_clave" : ["baja","trámite","materia","dar de baja"],
    "respuesta" : "Debes de completar el formulario de Baja de una Materia durante las primeras semanas del semestre. Puedes encontrar el formulario aquí: <a href='https://www.escom.ipn.mx/SSEIS/gestionescolar/servicios/tramite.php' target='_blank'>Formulario de Baja de Materia</a>",
    "categoria": "Trámites"
    },
    {
        "pregunta" : "¿Cómo me inscribo?",
        "palabras_clave" : ["inscripción","proceso de inscripción","inscribo","inscribirme"], 
        "respuesta" : "En primer semestre la inscripción no la realizan los alumnos, deberás de estar al pendiente del sitio oficial de ESCOM donde en los días previos al semestre se abre un minisitio donde podrás consultar el grupo en el que fuiste inscrito.",
        "categoría": "Trámites"
    },
    {
        "pregunta" : "¿Cómo hago mi reinscripción?",
        "palabras_clave" : ["reinscripción","proceso de reinscripción","reinscribir","siguiente semestre"], 
        "respuesta" : "A partir de tu segundo semestre el proceso de reinscripción se realiza a la plataforma del SAES, en el sitio oficial de ESCOM y sus redes sociales podrás ver las fechas dependiendo de tu promedio y situación escolar. También podrás consultar tu cita desde el SAES en la pestaña del reinscripción.",
        "categoría": "Trámites"
    },
    {
    "pregunta" : "¿Cómo puedo solicitar una constancia de estudio?",
    "palabras_clave" : ["constancia", "estudio", "solicitar", "pedir", "tramite", "certificado", "documento", "historial", "academico", "papel", "boleta"],
    "respuesta" : "Deberás de acceder a la sección de Trámites Escolares desde el sitio web de la ESCOM (<a href='https://www.escom.ipn.mx/SSEIS/gestionescolar/servicios/tramite.php' target='_blank'>aquí</a>) y elegir la opción correspondiente. Después te deberás de registrar en el sitio que se abre y completar el formulario correspondiente.",
    "categoria": "Trámites"
    },
    {
        "pregunta" : "¿Qué materias llevaré en el primer semestre?",
        "palabras_clave" : ["materias","primer semetre", "plan curricular"], 
        "respuesta" : "Depende de la carrera que hayas elegido. Todos los alumnos de primero llevan: Fundamentos de Programación, Comunicación Oral y Escrita, Cálculo y Matemáticas Discretas. Los alumnos de ISC llevan Análisis Vectorial, los de IIA Fundamentos Ecónomicos y Mecánica y Electromagnestimo, y los de LCD Introducción a la Ciencia de Datos.",
        "categoría": "Planes académicos" 
    },
    {
        "pregunta" : "¿Qué materias llevaré en el primer semestre?",
        "palabras_clave" : ["materias","primer semetre", "plan curricular"], 
        "respuesta" : "Depende de la carrera que hayas elegido. Todos los alumnos de primero llevan: Fundamentos de Programación, Comunicación Oral y Escrita, Cálculo y Matemáticas Discretas. Los alumnos de ISC llevan Análisis Vectorial, los de IIA Fundamentos Ecónomicos y Mecánica y Electromagnestimo, y los de LCD Introducción a la Ciencia de Datos.",
        "categoría": "Planes académicos" 
    },
    {
    "pregunta" : "¿ESCOM tiene clubes?",
    "palabras_clave" : ["club", "clubes", "actividad", "extracurricular", "deporte", "cultural", "asociación", "grupo", "sociedad", "organización", "participar", "unir"],
    "respuesta" : "¡Sí! ESCOM tiene diversos clubes. Puedes consultar la lista <a href='https://www.escom.ipn.mx/htmls/escomunidad/clubs.php' target='_blank'>aquí</a>. ESCOM también cuenta con actividades deportivas y culturales.",
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
    "respuesta" : "¡Sí! ESCOM ofrece tres tipos de beca institucional y la beca de excelencia de Telmex, entre otras. Las convocatorias se publican al inicio del semestre. Para más información, accede al siguiente enlace: <a href='https://www.escom.ipn.mx/htmls/escomunidad/becas.php' target='_blank'>Portal de Becas de ESCOM</a>",
    "categoria": "Becas y Apoyos"
    },
    {
    "pregunta" : "¿Dónde se encuentra ESCOM?",
    "palabras_clave" : ["donde", "ubicación", "dirección", "llegar", "localización", "mapa", "metro", "autobus", "trolebús", "direccion", "encuentra", "situado"],
    "respuesta" : "ESCOM se encuentra en la siguiente dirección. Puedes llegar en metro (estación Politécnico de la Línea 5), la Línea 8 del trolebús o una de las rutas de autobús cercanas. Puedes acceder a más información <a href='https://www.escom.ipn.mx/htmls/conocenos/ubicacion.php' target='_blank'>aquí</a>.",
    "categoria": "Ubicación"  
    },
]

default_response = "Lo siento, por el momento no puedo responder la pregunta. Puedes consultar en el sitio web oficial de ESCOM o sus redes sociales para encontrar más información."
