import random
import os
import json
from imagenes import *

ARCHIVO_PUNTUACIONES = "puntuaciones.json"

def cargar_puntuaciones():
    """Carga las puntuaciones guardadas en el archivo JSON."""
    try:
        with open(ARCHIVO_PUNTUACIONES, "r") as archivo:
            # Si el archivo está vacío, devolver una lista vacía
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # En caso de que el archivo esté corrupto o mal formado, se devuelve una lista vacía
        return []

def guardar_puntuacion(nombre, puntuacion):
    """Guarda la puntuación de un jugador en el archivo JSON."""
    puntuaciones = cargar_puntuaciones()
    puntuaciones.append({"nombre": nombre, "puntuacion": puntuacion})
    puntuaciones = sorted(puntuaciones, key=lambda x: x["puntuacion"], reverse=True)
    with open(ARCHIVO_PUNTUACIONES, "w") as archivo:
        json.dump(puntuaciones, archivo, indent=4)

def mostrar_puntuaciones():
    """Muestra las puntuaciones en orden de mayor a menor."""
    puntuaciones = cargar_puntuaciones()
    print("\nPuntuaciones:")
    for i, puntaje in enumerate(puntuaciones[:10], 1):  # Muestra las 10 mejores puntuaciones
        print(f"{i}. {puntaje['nombre']} - {puntaje['puntuacion']} puntos")

def seleccionar_categoria():
    """
    Muestra un menú para que el jugador elija una categoría de palabras.
    """
    print("Selecciona una categoría:")
    print("1. Verdulería (Frutas y Verduras)")
    print("2. Países")
    print("3. Salir")

    while True:
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            return "verduleria"
        elif opcion == "2":
            return "paises"
        elif opcion == "3":
            exit()  # Sale del programa
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

def seleccionar_categoria():
    """Muestra un menú para que el jugador elija una categoría de palabras."""
    print("Selecciona una categoría:")
    print("1. Verdulería (Frutas y Verduras)")
    print("2. Países")
    print("3. Animales")
    print("4. Colores")
    print("5. Comida")
    print("6. Películas")
    print("7. Deportes")
    print("8. Instrumentos musicales")
    print("9. Superhéroes")
    print("10. Personajes de videojuegos")
    print("11. Razas de perros")
    print("12. Tecnología")
    print("13. Elementos de la tabla periódica")
    print("14. Celebridades")
    print("15. Lugares turísticos")
    print("16. Salir")

    while True:
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            return "verduleria"
        elif opcion == "2":
            return "paises"
        elif opcion == "3":
            return "animales"
        elif opcion == "4":
            return "colores"
        elif opcion == "5":
            return "comida"
        elif opcion == "6":
            return "peliculas"
        elif opcion == "7":
            return "deportes"
        elif opcion == "8":
            return "instrumentos"
        elif opcion == "9":
            return "superheroes"
        elif opcion == "10":
            return "videojuegos"
        elif opcion == "11":
            return "razas_perros"
        elif opcion == "12":
            return "tecnologia"
        elif opcion == "13":
            return "elementos"
        elif opcion == "14":
            return "celebridades"
        elif opcion == "15":
            exit()  # Sale del programa
        else:
            print("Opción no válida. Elige una categoría válida.")

def ahorcado():
    """Función principal para ejecutar el juego del ahorcado."""
    categorias = {
        "verduleria": ["MANZANA", "BANANA", "ZANAHORIA", "LECHUGA", "PEPINO", "CEREZA", "CEBOLLA", "COLIFLOR", "BROCOLI", "NARANJA"],
        "paises": ["ARGENTINA", "BRASIL", "CANADA", "JAPON", "AUSTRALIA", "CHILE", "KAZAJISTAN", "HOLANDA", "TAILANDIA", "ECUADOR" ],
        "animales": ["PERRO", "GATO", "ELEFANTE", "JIRAFA", "LEON", "COCODRILO", "PEZ", "ORNITORRINCO"],
        "colores": ["ROJO", "AZUL", "VERDE", "AMARILLO", "NEGRO", "ROSA", "DORADO"],
        "comida": ["PIZZA", "PASTA", "TACOS", "BURGER", "SUSHI"],
        "peliculas": ["INCEPTION", "AVATAR", "TITANIC", "JURASSIC PARK", "IRON MAN"],
        "deportes": ["FUTBOL", "BASKETBALL", "TENNIS", "BEISBOL", "NATACION"],
        "instrumentos": ["GUITARRA", "PIANO", "VIOLIN", "TAMBORES", "SAXOFON", "TRIANGULO"],
        "superheroes": ["SPIDERMAN", "BATMAN", "IRONMAN", "WONDERWOMAN", "HULK", "BLACKCANARY", "PHOENIX", "PSYLOCKE", "HAWKEYE", "BLACKWIDOW"],
        "videojuegos": ["MARIO", "LINK", "ZELDA", "SONIC", "RAPIDASH", "RESIDENTEVIL", "CRASH"],
        "razas_perros": ["LABRADOR", "BEAGLE", "BORDER COLLIE", "DACHSHUND", "POODLE"],
        "tecnologia": ["COMPUTADORA", "SMARTPHONE", "INTERNET", "ROBOT", "GADGET", "TABLET"],
        "elementos": ["OXIGENO", "HIDROGENO", "CARBONO", "NITROGENO", "HELMIO"],
        "celebridades": ["MICHAELJACKSON", "LADYGAGA", "LEONARDODICAPRIO", "DUALIPA", "TAYLORSWIFT", "LEOMESSI", "RIHANNA", "CHARLIXCX"],
    }
    # Solicitar el nombre del jugador y configurar la puntuación inicial
    nombre = input("Bienvenido/a, Ingresa tu nombre: ")
    puntuacion = 0

    # Seleccionar la categoría
    categoria = seleccionar_categoria()
    lista_palabras = categorias[categoria]  # Obtiene las palabras de la categoría elegida
    palabra = random.choice(lista_palabras)
    espacios = ["_"] * len(palabra)
    intentos = 6

    letras_seleccionadas = []  # Lista para almacenar las letras ya elegidas

    while True:
        os.system("cls")  # Limpia la pantalla

        # Muestra el estado actual de la palabra, las letras seleccionadas y la puntuación
        print(f"Puntuación: {puntuacion}")
        for character in espacios:
            print(character, end=" ")

        # Muestra las letras ya seleccionadas
        print("\nLetras seleccionadas:", ", ".join(letras_seleccionadas))

        print("\n" + imagenes[intentos])  # Muestra la imagen correspondiente a los intentos

        # Solicita una letra y verifica si es una letra válida
        letra = input("Elige una letra: ").upper()
        if not letra.isalpha() or len(letra) != 1:  # Verifica que sea una sola letra
            print("Opción no válida. Ingresa solo una letra.")
            continue
        if letra in letras_seleccionadas:  # Verifica si la letra ya ha sido seleccionada
            print("Ya elegiste esa letra. Elige otra.")
            continue
        letras_seleccionadas.append(letra)  # Agrega la letra a la lista de letras seleccionadas

        # Verifica si la letra está en la palabra
        verificar_letra = False
        for idx, character in enumerate(palabra):
            if character == letra:
                espacios[idx] = letra
                verificar_letra = True

        # Ajuste de puntuación
        if verificar_letra:
            puntuacion += 10  # Suma 10 puntos por letra correcta
        else:
            puntuacion -= 5   # Resta 5 puntos por letra incorrecta
            intentos -= 1     # Resta un intento

        # Verifica si el jugador ganó
        if "_" not in espacios:
            os.system("cls")
            print(imagen_gana)
            print(f"¡Ganaste, {nombre}! La palabra era: {palabra}. Tu puntuación final es: {puntuacion}")
            guardar_puntuacion(nombre, puntuacion)
            break  # Termina el juego

        # Verifica si el jugador perdió
        if intentos == 0:
            os.system("cls")
            print(f"¡Perdiste, {nombre}! La palabra era: {palabra}. Tu puntuación final es: {puntuacion}")
            print(imagen_pierde)
            guardar_puntuacion(nombre, puntuacion)
            break  # Termina el juego

        # Verifica si el jugador perdió
        if intentos == 0:
            os.system("cls")
            print(f"¡Perdiste, {nombre}! La palabra era: {palabra}. Tu puntuación final es: {puntuacion}")
            print(imagen_pierde)
            guardar_puntuacion(nombre, puntuacion)
            break  # Termina el juego

def jugar():
    """Función para iniciar el juego y preguntar si el jugador desea jugar nuevamente."""
    while True:
        ahorcado()
        mostrar_puntuaciones()  # Muestra las puntuaciones después de cada juego

        # Bucle para asegurar una respuesta válida
        while True:
            respuesta = input("¿Quieres jugar de nuevo? (S/N): ").upper()
            if respuesta == "N":
                print("Gracias por jugar.")
                return  # Sale completamente de la función y del programa
            elif respuesta == "S":
                break  # Sale del bucle interno y reinicia el juego
            else:
                print("Opción no válida. Por favor, elige S para sí o N para no.")

def menu():
    """Muestra el menú principal para el juego."""
    while True:
        print("\nMenú de opciones:")
        print("1. Jugar")
        print("2. Instrucciones")
        print("3. Puntuaciones")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("Instrucciones: El juego consiste en adivinar la palabra antes de que se acaben los intentos.")
        elif opcion == "3":
            mostrar_puntuaciones()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa una opción válida.")
