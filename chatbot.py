import random
from datetime import datetime

# ---------------------------------------------------------------------------
# Keyword groups and responses
# ---------------------------------------------------------------------------
KEYWORDS = {
    "saludo":    ["hola", "buenas", "hey", "ey", "qué tal", "que tal", "saludos", "buen dia", "buen día"],
    "nombre":    ["nombre", "llamas", "eres", "quien eres", "quién eres"],
    "funcion":   ["funcion", "función", "sirves", "haces", "capaz", "puedes hacer"],
    "hora":      ["hora", "tiempo", "qué hora", "que hora"],
    "fecha":     ["fecha", "dia de hoy", "día de hoy", "hoy es", "qué dia", "que dia", "qué día", "que día"],
    "estado":    ["como estas", "cómo estás", "como te encuentras", "como te va", "todo bien"],
    "bien":      ["bien", "genial", "excelente", "perfecto", "de maravilla"],
    "mal":       ["mal", "triste", "cansado", "aburrido", "deprimido"],
    "chiste":    ["chiste", "broma", "gracioso", "hazme reir", "algo divertido"],
    "ayuda":     ["ayuda", "ayudar", "puedes ayudar", "opciones", "que puedo preguntarte"],
    "adios":     ["adios", "adiós", "chao", "hasta luego", "nos vemos", "bye"],
}

CHISTES = [
    "¿Qué le dijo el cero al ocho? — Bonito cinturón.",
    "¿Por qué los pájaros vuelan al sur? — Porque caminar sería muy largo.",
    "¿Qué hace una abeja en el gimnasio? — ¡Zum-ba!",
    "¿Cómo se llama el campeón de buceo japonés? — Tokofondo.",
]


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
print(box_line("                         WELCOME TO ZENBOT!!!"))
print(box_line())
print(box_line(f"             CURRENT DATE AND TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"))
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