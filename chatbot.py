import random
from datetime import datetime

def responder(mensaje):
    mensaje = mensaje.lower()

    if "hola" in mensaje:
        saludos = ["Hola, ¿cómo estás?", "Saludos, ¿en qué te ayudo?", "Hola, qué bueno verte."]
        return random.choice(saludos)

    elif "nombre" in mensaje:
        return "Mi nombre es ZenBot."

    elif "cual es tu funcion" in mensaje:
        return "Estoy diseñado para ayudarte con tus preguntas y tareas."

    elif "hora" in mensaje:
        hora_actual = datetime.now().strftime("%H:%M:%S")
        return f"La hora actual es {hora_actual}."

    elif "ayuda" in mensaje:
        return "Puedes preguntarme mi nombre, la hora, saludarme o despedirte."

    elif "adios" in mensaje:
        return "Hasta luego."

    else:
        return "No entendí tu mensaje."

print("Bot: Hola, soy ZenBot. Escribe 'salir' para terminar.")

while True:
    mensaje_usuario = input("Tú: ")

    if mensaje_usuario.lower() == "salir":
        print("Bot: Cerrando chatbot...")
        break

    print("Bot:", responder(mensaje_usuario))