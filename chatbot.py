import random
import json
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Keyword groups and responses
# ---------------------------------------------------------------------------
DATA_PATH = Path(__file__).with_name("chatbot_data.json")

with DATA_PATH.open("r", encoding="utf-8") as f:
    data = json.load(f)

KEYWORDS = data["keywords"]
CHISTES = data["chistes"]


def detectar(msg, grupo):
    return any(kw in msg for kw in KEYWORDS[grupo])


def responder(mensaje):
    msg = mensaje.lower()

    if detectar(msg, "adios"):
        return "¡Hasta luego! Fue un placer charlar contigo."

    if detectar(msg, "saludo"):
        return random.choice(["¡Hola! ¿En qué te puedo ayudar?",
                               "¡Hey! ¿Qué tal? Aquí estoy.",
                               "Hola, qué bueno verte por aquí."])

    if detectar(msg, "estado"):
        return "¡Funcionando al 100%! ¿Y tú cómo estás?"

    if detectar(msg, "bien"):
        return random.choice(["Me alegra escuchar eso.", "¡Genial! Eso es lo que quiero oír."])

    if detectar(msg, "mal"):
        return random.choice(["Lo siento, espero que te animes pronto.", "Ánimo, aquí estoy si necesitas charlar."])

    if detectar(msg, "hora"):
        return f"Son las {datetime.now().strftime('%H:%M:%S')}."

    if detectar(msg, "fecha"):
        return f"Hoy es {datetime.now().strftime('%A %d de %B de %Y')}."

    if detectar(msg, "nombre"):
        return "Mi nombre es ZenBot, tu asistente virtual."

    if detectar(msg, "funcion"):
        return "Estoy diseñado para charlar contigo y responder preguntas simples."

    if detectar(msg, "chiste"):
        return random.choice(CHISTES)

    if detectar(msg, "ayuda"):
        return ("Puedes preguntarme: la hora, la fecha, mi nombre, cómo estoy, "
                "pedirme un chiste, o simplemente saludarme.")

    return random.choice([
        "Hmm, no estoy seguro de entender. ¿Puedes reformularlo?",
        "Interesante... pero no sé cómo responder a eso aún.",
        "No entendí bien. Escribe 'ayuda' para ver qué puedo hacer.",
    ])


# ---------------------------------------------------------------------------
# Welcome screen
# ---------------------------------------------------------------------------
BORDER = "####################################################################################"
W = len(BORDER) - 2


def box_line(text=""):
    padded = (" " + text) if text else ""
    return f"#{padded:<{W}}#"


print(BORDER)
print(box_line())
print(box_line())
print(box_line())
print(box_line("                         ¡BIENVENIDO A ZENBOT!"))
print(box_line())
print(box_line(f"             Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
print(box_line())
print(box_line())
print(box_line("    Escribe 'ayuda' para ver qué puedo hacer."))
print(box_line("    Escribe 'salir' para cerrar."))
print(box_line())
print(BORDER)
print()


# ---------------------------------------------------------------------------
# Chat loop
# ---------------------------------------------------------------------------
while True:
    mensaje_usuario = input("  Tú: ")

    if mensaje_usuario.strip().lower() in ("salir", "exit", "quit"):
        print("\n  ZenBot: ¡Hasta luego! Que tengas un excelente día.")
        break

    respuesta = responder(mensaje_usuario)

    print(f"  ZenBot: {respuesta}")
    print()