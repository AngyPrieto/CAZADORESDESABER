import random
import readchar

# Definir una lista de preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Amazonas", "Nilo", "Misisipi"],
        "respuesta": 2
    },
    {
        "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "opciones": ["1939", "1945", "1914"],
        "respuesta": 3
    },
    {
        "pregunta": "¿Quién pintó La Mona Lisa?",
        "opciones": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh"],
        "respuesta": 2
    },
    # Agrega más preguntas aquí
]


def obtener_pregunta():
    """Obtener una pregunta aleatoria de la lista"""
    return random.choice(preguntas)


def hacer_pregunta(pregunta):
    """Mostrar una pregunta y opciones al jugador"""
    print(pregunta["pregunta"])
    for i, opcion in enumerate(pregunta["opciones"]):
        print(f"{i + 1}. {opcion}")
    respuesta = int(readchar.readchar())
    return respuesta == pregunta["respuesta"]


def jugar_juego():
    """Función principal para ejecutar el juego"""
    print("¡Bienvenido a Cazadores del Saber, el juego de cultura general!")
    puntaje = 0
    for _ in range(5):  # Realizar 5 preguntas
        pregunta = obtener_pregunta()
        if hacer_pregunta(pregunta):
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto.")
        print()
    print(f"Juego terminado. Puntaje final: {puntaje}/5")


# Iniciar el juego
jugar_juego()
