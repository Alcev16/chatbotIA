#Procesameinto de Texto con NLTK

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet # Necesario para la lematización en español o inglés

# Inicializar el lematizador
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(word):
    """
    Mapea las etiquetas de POS (Part Of Speech) de NLTK a un formato que WordNetLemmatizer puede usar.
    Esto mejora la precisión de la lematización.
    """
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def preprocess_text(text):
    """
    Procesa un texto aplicando tokenización y lematización.
    """
    # 1. Convertir a minúsculas
    text = text.lower()

    # 2. Tokenizar el texto en palabras
    words = nltk.word_tokenize(text, language='spanish') # Especificamos español

    # 3. Lematizar cada palabra
    # Usamos get_wordnet_pos para mejorar la lematización al considerar el tipo de palabra
    lemmas = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in words if word.isalpha()]
    # `if word.isalpha()`: Esto asegura que solo procesamos palabras (excluyendo signos de puntuación, números, etc.)

    return lemmas

if __name__ == "__main__":
    # Ejemplo de uso y prueba de la función
    test_sentences = [
        "¿Cuáles son los requisitos para inscribirme?",
        "Las clases empiezan en agosto",
        "Quiero saber sobre las becas",
        "Dónde puedo ver mi plan de estudios",
        "Estoy interesado en actividades deportivas"
    ]

    print("--- Probando el preprocesador de texto ---")
    for sentence in test_sentences:
        processed_words = preprocess_text(sentence)
        print(f"Texto original: '{sentence}'")
        print(f"Palabras procesadas: {processed_words}\n")