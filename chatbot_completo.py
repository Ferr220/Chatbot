import sqlite3
from datetime import datetime
import random

# ============================================================================
# CONEXIÓN Y CREACIÓN DE TABLAS
# ============================================================================

def conectar_bd():
    """Conecta a la base de datos unificada"""
    conexion = sqlite3.connect('chatbot_completo.db')
    cursor = conexion.cursor()
    return conexion, cursor

def crear_tablas():
    """Crea todas las tablas necesarias"""
    conexion, cursor = conectar_bd()
    
    # Tabla de respuestas generales
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS respuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabras_clave TEXT NOT NULL,
            respuesta TEXT NOT NULL,
            categoria TEXT
        )
    ''')
    
    # Tabla de alimentos nutricionales
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            porcion TEXT,
            calorias REAL,
            proteinas REAL,
            carbohidratos REAL,
            grasas REAL,
            fibra REAL,
            categoria TEXT
        )
    ''')
    
    conexion.commit()
    conexion.close()

# ============================================================================
# LLENAR BASE DE DATOS - RESPUESTAS GENERALES
# ============================================================================

def llenar_respuestas_iniciales():
    """Llena la tabla de respuestas generales"""
    conexion, cursor = conectar_bd()
    
    respuestas_iniciales = [
        # Saludos
        ("hola", "¡Hola! Soy Zen, tu asistente nutricional 🥗", "saludos"),
        ("hola", "¡Hola! Puedo ayudarte con nutrición o responder preguntas generales", "saludos"),
        ("hola", "Hola! ¿En qué puedo ayudarte hoy? 😊", "saludos"),
        ("hola", "¡Hola de nuevo! ¿Qué necesitas?", "saludos"),
        ("buenos dias", "Buenos días! Espero tengas un día saludable 💪", "saludos"),
        ("buenas noches", "Buenas noches! Que descanses", "saludos"),
        
        # Nombre
        ("nombre", "Soy Zen, tu chatbot asistente de nutrición e información general!", "info"),
        ("quien eres", "¡Soy Zen! Puedo hablar de nutrición, alimentos y mucho más", "info"),
        
        # Ayuda
        ("ayuda", "Puedo ayudarte con:\n  1) Nutrición de alimentos\n  2) Preguntas generales\n  3) Información sobre calorías, proteínas, etc.", "ayuda"),
        ("que puedes hacer", "Puedo decirte la nutrición de alimentos, la hora, la fecha, y responder preguntas variadas!", "ayuda"),
        
        # Hora y Fecha
        ("hora", "ESPECIAL_HORA", "especial"),
        ("fecha", "ESPECIAL_FECHA", "especial"),
        
        # Despedidas
        ("adios", "¡Adiós! Que disfrutes comiendo saludable 🍎", "despedidas"),
        ("adios", "Hasta luego! Espero haberte ayudado 💪", "despedidas"),
        ("hasta luego", "¡Hasta pronto! Recuerda comer bien 🥗", "despedidas"),
        ("chao", "Chao! Nos vemos pronto!", "despedidas"),
    ]
    
    cursor.execute("SELECT COUNT(*) FROM respuestas")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO respuestas (palabras_clave, respuesta, categoria) VALUES (?, ?, ?)",
            respuestas_iniciales
        )
        conexion.commit()
    
    conexion.close()

# ============================================================================
# LLENAR BASE DE DATOS - ALIMENTOS NUTRICIONALES
# ============================================================================

def llenar_base_nutricional():
    """Llena la tabla de alimentos con información nutricional"""
    conexion, cursor = conectar_bd()
    
    alimentos = [
        # Frutas
        ("manzana", "100g", 52, 0.3, 14, 0.2, 2.4, "frutas"),
        ("plátano", "100g", 89, 1.1, 23, 0.3, 2.6, "frutas"),
        ("naranja", "100g", 47, 0.9, 12, 0.1, 2.4, "frutas"),
        ("fresa", "100g", 32, 0.8, 8, 0.3, 2, "frutas"),
        ("mango", "100g", 60, 0.8, 15, 0.4, 1.6, "frutas"),
        ("piña", "100g", 50, 0.5, 13, 0.1, 1.4, "frutas"),
        ("uva", "100g", 67, 0.6, 17, 0.2, 0.9, "frutas"),
        ("pera", "100g", 57, 0.4, 15, 0.1, 3.1, "frutas"),
        
        # Verduras
        ("brócoli", "100g", 34, 2.8, 7, 0.4, 2.4, "verduras"),
        ("zanahoria", "100g", 41, 0.9, 10, 0.2, 2.8, "verduras"),
        ("lechuga", "100g", 15, 1.2, 3, 0.2, 1.3, "verduras"),
        ("tomate", "100g", 18, 0.9, 4, 0.2, 1.2, "verduras"),
        ("espinaca", "100g", 23, 2.7, 4, 0.4, 2.2, "verduras"),
        ("cebolla", "100g", 40, 1.1, 9, 0.1, 1.7, "verduras"),
        ("pepino", "100g", 16, 0.7, 4, 0.1, 0.5, "verduras"),
        ("calabacín", "100g", 21, 1.5, 4, 0.4, 1, "verduras"),
        
        # Proteínas
        ("pollo (pechuga)", "100g", 165, 31, 0, 3.6, 0, "proteinas"),
        ("huevo", "1 unidad", 155, 13, 1.1, 11, 0, "proteinas"),
        ("salmón", "100g", 208, 20, 0, 13, 0, "proteinas"),
        ("atún", "100g", 144, 30, 0, 1.3, 0, "proteinas"),
        ("carne molida", "100g", 250, 17, 0, 20, 0, "proteinas"),
        ("pechuga de pavo", "100g", 135, 24, 0, 3, 0, "proteinas"),
        ("jamón", "30g", 43, 7, 1, 1.5, 0, "proteinas"),
        
        # Granos
        ("arroz blanco cocido", "100g", 130, 2.7, 28, 0.3, 0.4, "granos"),
        ("pan integral", "30g", 80, 4, 14, 1, 2.7, "granos"),
        ("avena", "100g", 389, 17, 66, 7, 10.6, "granos"),
        ("pasta cocida", "100g", 131, 5, 25, 1.1, 1.8, "granos"),
        ("harina de trigo", "100g", 364, 10, 76, 1, 2.7, "granos"),
        
        # Lácteos
        ("leche desnatada", "100ml", 35, 3.6, 5, 0.1, 0, "lacteos"),
        ("yogur natural", "100g", 61, 3.5, 5, 0.4, 0, "lacteos"),
        ("queso cheddar", "30g", 120, 7, 0.4, 10, 0, "lacteos"),
        ("mozzarella", "30g", 80, 6, 1, 6, 0, "lacteos"),
        
        # Grasas saludables
        ("aguacate", "100g", 160, 2, 9, 15, 7, "grasas"),
        ("almendras", "30g", 164, 6, 6, 14, 3.5, "grasas"),
        ("aceite de oliva", "15ml", 119, 0, 0, 13.5, 0, "grasas"),
        ("nueces", "30g", 196, 4.3, 4, 20, 3.8, "grasas"),
        ("cacahuetes", "30g", 161, 7, 5, 14, 2.5, "grasas"),
    ]
    
    cursor.execute("SELECT COUNT(*) FROM alimentos")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO alimentos (nombre, porcion, calorias, proteinas, carbohidratos, grasas, fibra, categoria)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, alimentos)
        conexion.commit()
    
    conexion.close()

# ============================================================================
# BÚSQUEDA Y PROCESAMIENTO DE INFORMACIÓN
# ============================================================================

def buscar_alimento(nombre_alimento):
    """Busca información nutricional de un alimento"""
    nombre_alimento = nombre_alimento.lower().strip()
    conexion, cursor = conectar_bd()
    
    cursor.execute("""
        SELECT nombre, porcion, calorias, proteinas, carbohidratos, grasas, fibra, categoria
        FROM alimentos
        WHERE nombre LIKE ?
    """, (f"%{nombre_alimento}%",))
    
    resultado = cursor.fetchone()
    conexion.close()
    
    return resultado

def obtener_respuesta_nutricion(mensaje):
    """Procesa preguntas sobre nutrición"""
    mensaje = mensaje.lower().strip()
    
    # Palabras clave de nutrición
    palabras_nutricion = ["calorias", "calorías", "proteina", "proteínas", "carbohidratos", 
                         "grasas", "fibra", "nutricion", "nutrición", "valor nutricional", 
                         "energía", "kilocalorías"]
    
    # Extraer el nombre del alimento
    alimento = None
    for palabra in palabras_nutricion:
        if palabra in mensaje:
            alimento = mensaje.replace(palabra, "").replace(" de ", "").replace(" del ", "").strip()
            break
    
    if alimento and len(alimento) > 2:
        resultado = buscar_alimento(alimento)
        
        if resultado:
            nombre, porcion, calorias, proteinas, carbs, grasas, fibra, categoria = resultado
            respuesta = f"""
🥗 **{nombre.upper()}** ({categoria})
─────────────────────────────────────
📊 Información nutricional por {porcion}:
  • 🔥 Calorías: {calorias} kcal
  • 💪 Proteínas: {proteinas}g
  • 🍞 Carbohidratos: {carbs}g
  • 🧈 Grasas: {grasas}g
  • 🌾 Fibra: {fibra}g
            """.strip()
            return respuesta
        else:
            respuestas_no_encontrado = [
                f"No encontré '{alimento}' en mi base. ¿Intenta con otro alimento? 🤔",
                f"Lo siento, no tengo datos de '{alimento}'. Pregunta por otro 🥗",
                f"Ese alimento no está registrado. ¿Probamos con otro? 😊"
            ]
            return random.choice(respuestas_no_encontrado)
    
    return None

def obtener_respuesta_general(mensaje):
    """Obtiene respuestas generales de la base de datos"""
    mensaje = mensaje.lower()
    conexion, cursor = conectar_bd()
    
    # Buscar respuestas por palabras clave
    cursor.execute("""
        SELECT respuesta FROM respuestas 
        WHERE palabras_clave IN (
            SELECT palabras_clave FROM respuestas 
            WHERE ? LIKE '%' || palabras_clave || '%'
        )
        ORDER BY RANDOM()
        LIMIT 1
    """, (mensaje,))
    
    resultado = cursor.fetchone()
    
    if resultado:
        respuesta = resultado[0]
        conexion.close()
        
        # Procesar respuestas especiales
        if respuesta == "ESPECIAL_HORA":
            ahora = datetime.now().strftime("%H:%M")
            return f"⏰ La hora actual es **{ahora}**"
        elif respuesta == "ESPECIAL_FECHA":
            hoy = datetime.now().strftime("%d/%m/%Y")
            return f"📅 La fecha de hoy es **{hoy}**"
        else:
            return respuesta
    
    # Búsqueda alternativa palabra por palabra
    palabras = mensaje.split()
    for palabra in palabras:
        cursor.execute("""
            SELECT respuesta FROM respuestas 
            WHERE ? LIKE '%' || palabras_clave || '%'
            ORDER BY RANDOM()
            LIMIT 1
        """, (palabra,))
        resultado = cursor.fetchone()
        if resultado:
            conexion.close()
            return resultado[0]
    
    conexion.close()
    return None

def obtener_respuesta(mensaje):
    """Función principal que integra todas las respuestas"""
    # 1. Primero intentar responder sobre nutrición
    respuesta_nutricion = obtener_respuesta_nutricion(mensaje)
    if respuesta_nutricion:
        return respuesta_nutricion
    
    # 2. Luego intentar respuestas generales
    respuesta_general = obtener_respuesta_general(mensaje)
    if respuesta_general:
        return respuesta_general
    
    # 3. Respuesta por defecto
    respuestas_defecto = [
        "¿Preguntas sobre nutrición? Prueba: 'Calorías del pollo' 🍗",
        "No entiendo bien. ¿Pregúntame sobre alimentos o algo general? 🥗",
        "Hmm, ayúdame con más detalles 😊",
        "Estoy aquí para ayudarte! ¿Nutrición o algo más?",
    ]
    return random.choice(respuestas_defecto)

# ============================================================================
# UTILIDADES Y COMANDOS
# ============================================================================

def listar_alimentos():
    """Lista todos los alimentos disponibles por categoría"""
    conexion, cursor = conectar_bd()
    cursor.execute("SELECT nombre, categoria FROM alimentos ORDER BY categoria, nombre")
    alimentos = cursor.fetchall()
    conexion.close()
    
    if not alimentos:
        print("No hay alimentos en la base de datos.")
        return
    
    categorias_dict = {}
    for nombre, categoria in alimentos:
        if categoria not in categorias_dict:
            categorias_dict[categoria] = []
        categorias_dict[categoria].append(nombre)
    
    print("\n" + "="*60)
    print("📚 ALIMENTOS DISPONIBLES")
    print("="*60)
    for categoria in sorted(categorias_dict.keys()):
        print(f"\n🏷️  {categoria.upper()}:")
        for alimento in sorted(categorias_dict[categoria]):
            print(f"   • {alimento}")
    print("\n" + "="*60)

def estadisticas_bd():
    """Muestra estadísticas de ambas bases de datos"""
    conexion, cursor = conectar_bd()
    
    # Estadísticas de alimentos
    cursor.execute("SELECT COUNT(*) FROM alimentos")
    total_alimentos = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT categoria) FROM alimentos")
    categorias_alimentos = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM respuestas")
    total_respuestas = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT categoria) FROM respuestas")
    categorias_respuestas = cursor.fetchone()[0]
    
    conexion.close()
    
    print("\n" + "="*60)
    print("📊 ESTADÍSTICAS DE LA BASE DE DATOS")
    print("="*60)
    print(f"\n🍎 ALIMENTOS:")
    print(f"   Total: {total_alimentos} alimentos")
    print(f"   Categorías: {categorias_alimentos}")
    print(f"\n💬 RESPUESTAS:")
    print(f"   Total: {total_respuestas} respuestas")
    print(f"   Categorías: {categorias_respuestas}")
    print("\n" + "="*60)

def ayuda_detallada():
    """Muestra información de ayuda detallada"""
    ayuda = """
╔════════════════════════════════════════════════════════════╗
║          🤖 CHATBOT ZEN - GUÍA COMPLETA                   ║
╚════════════════════════════════════════════════════════════╝

📚 PREGUNTAS SOBRE NUTRICIÓN:
   • "Calorías del pollo"
   • "Proteínas del huevo"
   • "Nutrición de la manzana"
   • "Valor nutricional del salmón"

💬 PREGUNTAS GENERALES:
   • "Hola" / "Buenos días"
   • "¿Cuál es tu nombre?"
   • "¿Qué hora es?"
   • "¿Cuál es la fecha?"
   • "Ayuda" / "¿Qué puedes hacer?"

⌨️  COMANDOS ESPECIALES:
   • listar    - Ver todos los alimentos
   • stats     - Ver estadísticas
   • ayuda     - Esta pantalla
   • salir     - Terminar el programa

🎯 EJEMPLOS:
   Tu: Calorías del brócoli
   🤖 Zen: [Muestra: 34 kcal, proteínas, etc]
   
   Tu: ¿Hora?
   🤖 Zen: ⏰ La hora actual es 14:30

════════════════════════════════════════════════════════════
    """
    print(ayuda)

# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # Inicializar base de datos
    crear_tablas()
    llenar_respuestas_iniciales()
    llenar_base_nutricional()
    
    # Pantalla de bienvenida
    print("\n" + "="*60)
    print("🤖 CHATBOT ZEN - VERSIÓN COMPLETA")
    print("="*60)
    print("\nCombina respuestas generales + información nutricional")
    print("\nEscribe 'ayuda' para instrucciones detalladas")
    print("Escribe 'salir' para terminar")
    print("="*60 + "\n")
    
    while True:
        mensaje_usuario = input("👤 Tu: ").strip()
        
        if not mensaje_usuario:
            continue
        
        # Comandos especiales
        if mensaje_usuario.lower() == "salir":
            print("🤖 ¡Hasta luego! Come saludable 🥗\n")
            break
        
        elif mensaje_usuario.lower() == "listar":
            listar_alimentos()
            continue
        
        elif mensaje_usuario.lower() == "stats":
            estadisticas_bd()
            continue
        
        elif mensaje_usuario.lower() == "ayuda":
            ayuda_detallada()
            continue
        
        # Obtener y mostrar respuesta
        respuesta = obtener_respuesta(mensaje_usuario)
        print(f"🤖 Zen: {respuesta}\n")
