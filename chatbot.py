import random
from datetime import datetime

def responder(mensaje):
    mensaje = mensaje.lower()
    
    if "hola" in mensaje:
        saludos = ["¡Hola! ¿Cómo estás?", "¡Hola! ¿En qué puedo ayudarte?", "¡Hola! ¿Qué tal tu día?"]
        return random.choice(saludos)
    
    elif "nombre" in mensaje:
        return "Mi nombre es Zen y soy tu chatbot personal :) ¿Cómo puedo ayudarte hoy?"
    
    elif "como estas" in mensaje:
        estados = ["Estoy bien, gracias por preguntar. ¿Y tú?", "¡Me siento genial! ¿Y tú?", "Estoy aquí para ayudarte, ¿cómo estás tú?"]
        return random.choice(estados)
    
    elif "hora" in mensaje:
        ahora = datetime.now().strftime("%H:%M")
        return f"La hora actual es {ahora}."
    
    elif "fecha" in mensaje:
        hoy = datetime.now().strftime("%d/%m/%Y")
        return f"La fecha de hoy es {hoy}."
    
    elif "ayuda" in mensaje:
        return "Puedes preguntarme mi nombre, la hora, la fecha, saludarme o despedirte."
    
    elif "adios" in mensaje or "hasta luego" in mensaje:    
        despedidas = ["¡Adiós! Que tengas un buen día.", "¡Hasta luego! Espero hablar contigo pronto.", "¡Nos vemos! Cuídate mucho."]
        return random.choice(despedidas)
    
    else:
        return "Lo siento, no entiendo lo que quieres decir..."
    
print("¡Hola! Soy Zen, tu chatbot personal. Escribe 'salir' para terminar.")

while True:
    mensaje_usuario = input("Tú: ")
    if mensaje_usuario.lower() == "salir":
        print("¡Adiós! Que tengas un buen día.")
        break
    respuesta = responder(mensaje_usuario)
    print("Zen: " + respuesta)