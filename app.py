# app.py

from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_chatbot_response # Importamos la función de nuestro chatbot

app = Flask(__name__)

# Ruta principal que renderiza la plantilla HTML del chat
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar las peticiones del chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message') # Obtenemos el mensaje del usuario del JSON
    if not user_message:
        return jsonify({"response": "Por favor, escribe un mensaje."})

    # Obtenemos la respuesta del chatbot
    chatbot_response = get_chatbot_response(user_message)

    # Devolvemos la respuesta como JSON
    return jsonify({"response": chatbot_response})

if __name__ == '__main__':
    # Ejecutamos la aplicación Flask
    # debug=True permite que el servidor se reinicie automáticamente al hacer cambios
    # y muestra errores en el navegador para facilitar la depuración.
    app.run(debug=True)