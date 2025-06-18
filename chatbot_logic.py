# chatbot_logic.py

import nltk
from nltk.corpus import wordnet # Necesario para la lematización si no se descargó antes

from knowledge_base import knowledge_base, default_response
from nlp_processor import preprocess_text

def get_best_match_score(user_lemmas, kb_entry_keywords):
    """
    Calcula una puntuación de coincidencia entre los lemas del usuario
    y las palabras clave de una entrada de la base de conocimiento.
    """
    score = 0
    # Convertir las palabras clave de la base de conocimiento a un conjunto para búsquedas rápidas
    kb_keywords_set = set(kb_entry_keywords)

    for lemma in user_lemmas:
        if lemma in kb_keywords_set:
            score += 1
    return score

def get_chatbot_response(user_question, threshold=0.6):
    """
    Recibe la pregunta del usuario y devuelve la respuesta del chatbot.
    """
    # 1. Preprocesar la pregunta del usuario
    user_lemmas = preprocess_text(user_question)

    best_match_entry = None
    highest_score = 0
    total_user_words = len(user_lemmas)

    if total_user_words == 0: # Si el usuario solo escribió signos de puntuación o nada
        return default_response

    # 2. Iterar sobre la base de conocimiento para encontrar la mejor coincidencia
    for entry in knowledge_base:
        # Preprocesar las palabras clave de la base de conocimiento para esta entrada
        # Aquí, estamos asumiendo que las 'palabras_clave' en knowledge_base.py
        # no están lematizadas y necesitan serlo en tiempo de ejecución.
        # Es una buena práctica para asegurar consistencia.
        kb_lemmas = preprocess_text(" ".join(entry["palabras_clave"]))

        # Calcular la puntuación de coincidencia
        current_score = get_best_match_score(user_lemmas, kb_lemmas)

        # Actualizar la mejor coincidencia si encontramos una puntuación más alta
        if current_score > highest_score:
            highest_score = current_score
            best_match_entry = entry

    # 3. Determinar la respuesta basada en la mejor coincidencia
    # Calcular un porcentaje de coincidencia para el umbral
    # Esto es una aproximación, puedes ajustar la métrica si lo necesitas.
    # Por ejemplo, podrías dividir por el máximo entre len(user_lemmas) y len(kb_lemmas)
    # o por el número de palabras clave de la entrada.
    match_percentage = highest_score / total_user_words if total_user_words > 0 else 0

    if best_match_entry and match_percentage >= threshold:
        return best_match_entry["respuesta"]
    else:
        return default_response

if __name__ == "__main__":
    # Ejemplos de prueba de la lógica del chatbot
    print("--- Probando la lógica del chatbot ---")

    print(f"Chatbot: {get_chatbot_response('Hola')}")
    print(f"Chatbot: {get_chatbot_response('Quiero saber los requisitos para inscripción.')}")
    print(f"Chatbot: {get_chatbot_response('Cuando empiezan las clases?')}")
    print(f"Chatbot: {get_chatbot_response('Dònde puedo ver el plan de estudio de mi carrera?')}")
    print(f"Chatbot: {get_chatbot_response('Necesito ayuda con el campus virtual.')}")
    print(f"Chatbot: {get_chatbot_response('Hay becas?')}")
    print(f"Chatbot: {get_chatbot_response('Qué actividades extracurriculares hay?')}")
    print(f"Chatbot: {get_chatbot_response('Pregunta sin sentido.')}")
    print(f"Chatbot: {get_chatbot_response('Servicios de apoyo')}")
    print(f"Chatbot: {get_chatbot_response('')}") # Pregunta vacía
    print(f"Chatbot: {get_chatbot_response('!!!???')}") # Solo puntuación