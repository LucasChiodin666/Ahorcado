import random
import os

def ahorcado():
    """
    Función principal para ejecutar el juego del ahorcado.
    """

    # Representación gráfica del ahorcado en diferentes estados de intentos
    IMAGENES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    # Lista de palabras para el juego
    lista_palabras = [
        "MANZANA",
        "BANANA",
        "DURAZNO",
        "CEREZA",
        "TOMATE",
        "KIWI",
        "CIRUELA",
        "CEBOLLA",
        
    ]

    # Selección aleatoria de la palabra a adivinar
    palabra = random.choice(lista_palabras)

    # Lista para almacenar los espacios en blanco o letras adivinadas
    espacios = ["_"] * len(palabra)

    # Número de intentos disponibles
    intentos = 6

    # Bucle principal del juego
    while True:
        os.system("cls")  # Limpia la pantalla

        # Imprime el estado actual de la palabra con espacios
        for character in espacios:
            print(character, end=" ")
        
        print("\n" + IMAGENES[intentos])  # Hace un salto de linea y muestra la imagen del estado actual de intentos

        # Solicita una letra al usuario y convierte a mayúscula
        letra = input("Elige una letra: ").upper()

        # Variable para verificar si la letra está en la palabra
        verificar_letra = False

        # Verificación de la letra en la palabra
        for idx, character in enumerate(palabra):
            if character == letra:
                espacios[idx] = letra
                verificar_letra = True  # Se encontró la letra en la palabra

        # Si la letra no está en la palabra, reduce un intento
        if not verificar_letra:
            intentos -= 1

        # Condición de victoria: si no hay guiones bajos, el jugador gana
        if "_" not in espacios:
            os.system("cls")
            print("¡Ganaste!")
            break  # Termina el juego
            input()  # Pausa para que el jugador vea el mensaje de victoria
            
        # Condición de derrota: si no quedan intentos, el jugador pierde
        if intentos == 0:
            os.system("cls")
            print("¡Perdiste!")
            break  # Termina el juego

# Punto de entrada de la aplicación
if __name__ == '__main__':
    ahorcado()
