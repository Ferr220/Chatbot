# Chatbot (ZenBot)

Chatbot de consola en Python que responde con reglas basadas en palabras clave.

## Caracteristicas

- Saludos con respuestas aleatorias.
- Responde preguntas sobre su nombre y funcion.
- Informa la hora actual y la fecha actual del sistema.
- Conversacion basica sobre estado de animo (bien/mal).
- Cuenta chistes.
- Muestra ayuda con ejemplos de lo que puede hacer.
- Finaliza la conversacion al escribir `salir`, `exit` o `quit`.

## Requisitos

- Python 3.8 o superior

## Ejecutar el proyecto

Desde la carpeta del proyecto:

```bash
python chatbot.py
```

## Ejemplos de mensajes

Puedes probar con mensajes como:

- `hola`
- `como te llamas`
- `que puedes hacer`
- `que hora es`
- `que dia es hoy`
- `como estas`
- `estoy bien`
- `estoy mal`
- `cuentame un chiste`
- `ayuda`
- `adios`
- `salir`

## Como funciona

1. El bot convierte tu mensaje a minusculas.
2. Busca coincidencias de palabras clave por categoria (saludo, hora, fecha, etc.).
3. Devuelve una respuesta fija o aleatoria segun la intencion detectada.

Si no reconoce el mensaje, responde con una frase de fallback y sugiere usar `ayuda`.

## Estructura del proyecto

```text
Chatbot/
|-- chatbot.py
|-- README
```

## Autor

Proyecto creado por Ferr220.
