# import os
# import time
from classes.character import Character


# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')


STARTING_POINTS = 250


NAME_OF_GAME = """\n
    ██╗░░░░░░█████╗░░██████╗  ░█████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░░█████╗░░██████╗
    ██║░░░░░██╔══██╗██╔════╝  ██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔════╝
    ██║░░░░░███████║╚█████╗░  ███████║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝███████║╚█████╗░
    ██║░░░░░██╔══██║░╚═══██╗  ██╔══██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══██║░╚═══██╗
    ███████╗██║░░██║██████╔╝  ██║░░██║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║██║░░██║██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n
    ░██████╗░█████╗░██╗░░░░░██╗░░░██╗░█████╗░░░░░░██╗███████╗░██████╗
    ██╔════╝██╔══██╗██║░░░░░██║░░░██║██╔══██╗░░░░░██║██╔════╝██╔════╝
    ╚█████╗░███████║██║░░░░░╚██╗░██╔╝███████║░░░░░██║█████╗░░╚█████╗░
    ░╚═══██╗██╔══██║██║░░░░░░╚████╔╝░██╔══██║██╗░░██║██╔══╝░░░╚═══██╗
    ██████╔╝██║░░██║███████╗░░╚██╔╝░░██║░░██║╚█████╔╝███████╗██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚═════╝░\n
    """

GAME_INFORMATION = """
Bienvenido al desafío definitivo: ¡una aventura épica en un mundo salvaje!

Tu misión es atravesar 3 mazmorras, cada una más peligrosa que la anterior. En cada mazmorra, deberás enfrentarte a 3 criaturas feroces y finalmente a un poderoso jefe que pondrá a prueba todas tus habilidades.

A lo largo de tu travesía, derrotar a enemigos te otorgará valiosos ítems que podrás usar para fortalecerte en combate. Cada mazmorra aumenta en dificultad, con criaturas más astutas y jefes más temibles a medida que avanzas.

¿Tienes lo necesario para sobrevivir y convertirte en el verdadero campeón de las bestias? ¡MUCHA SUERTE!
"""

GAME_MENU = """
╔═════════════════════════════════════════════════╗
║¿Que desea hacer?                                ║
║(1) - Empezar a Jugar                            ║
║(2) - Ver caracteristicas del personaje          ║
║(3) - Ver informacion del juego                  ║ #!Ver tema de guardado
║(4) - Guardar                                    ║
║(5) - Salir del juego                            ║
╚═════════════════════════════════════════════════╝
"""

PLAY_MENU = """
╔════════════════════════════════════════════════════╗
║¿Que desea hacer?                                   ║
║(1) - Atacar                                        ║
║(2) - Ver caracteristicas del personaje             ║
║(3) - Ver caracteristicas del enemigo               ║
║(4) - Guardar                                       ║
║(5) - Volver hacia atras                            ║
╚════════════════════════════════════════════════════╝
"""

ANIMAL_MENU = """
╔═════════════════════════════════════════════╗
║(1) - Jabalí(+10 de fuerza)                  ║
║(2) - Rinoceronte(+10 de defensa)            ║
║(3) - Buey(+10 de salud)                     ║
╚═════════════════════════════════════════════╝
"""

#! Preguntar funciones si van en el main
# def welcome():

#     nameOfCharacter = input("\nIngrese el nombre para su personaje: ")
    
#     print(f"\n¡Hola {nameOfCharacter}!")
#     time.sleep(3)
#     print("╔═════════════════════════════════════════════╗")
#     print("║   ¡Bienvenido a las Aventuras del Jabalí!   ║")
#     print("╚═════════════════════════════════════════════╝\n")
#     time.sleep(3)

#     while True:
#         print("╔══════════════════════════════════════════════════════════════════════════════╗")
#         print(f"║Primero que nada, tienes {STARTING_POINTS} puntos para distribuir en vida, fuerza y defensa.║")
#         print("╚══════════════════════════════════════════════════════════════════════════════╝")
#         time.sleep(3)
#         print("         ===>Pero CUIDADO, depende de vos en que enfocás tus puntos<===\n")
#         time.sleep(3)
#         # Solicitar puntos para la vida
#         health = float(input("Ingrese la cantidad de vida que desea tener: "))
#         if health > STARTING_POINTS or health < 0:
#             print("Te excediste de puntos o ingresaste un valor no válido. Intenta de nuevo.\n")
#             continue

#         remaining_points = STARTING_POINTS - health
#         print(f"\nTe quedan {remaining_points} puntos.")

#         # Bucle para solicitar puntos de fuerza
#         while True:
#             strength = float(input("Ingrese la cantidad de fuerza que desea tener: "))
#             if strength > remaining_points or strength < 0:
#                 print(f"Te excediste de puntos o ingresaste un valor no válido. Te quedan {remaining_points} puntos.\n")
#             else:
#                 break

#         remaining_points -= strength
#         defense = remaining_points

#         # Creación del personaje
#         character1 = Character(nameOfCharacter, health, strength, defense)
#         print("Personaje creado con exito!!")
#         time.sleep(3)
#         clear_console()

#         break

#     print("\nAntes de comenzar, deberá elegir un tipo de animal:")
#     time.sleep(2)
#     print("╔═════════════════════════════════════════════╗")
#     print("║(1) - Jabalí(+10 de fuerza)                  ║")
#     print("║(2) - Rinoceronte(+10 de defensa)            ║")
#     print("║(3) - Buey(+10 de salud)                     ║")
#     print("╚═════════════════════════════════════════════╝\n")

#     while True:
#         characterOption = input(f"{nameOfCharacter}!, ahora elija el animal que desea utilizar (1-3): ")
#         if characterOption in ["1", "2", "3"]:
#             break
#         else:
#             print("Opción no válida. Por favor, elige un número entre 1 y 3.")
#             time.sleep(2)

#     if characterOption == "1":
#         print(f"\n{nameOfCharacter}, has elegido el Jabalí, muy buena opción")
#         character1.set_strength(10)
#     elif characterOption == "2":
#         print(f"\n{nameOfCharacter}, has elegido el Rinoceronte, muy buena opción")
#         character1.set_defense(10)
#     elif characterOption == "3":
#         print(f"\n{nameOfCharacter}, has elegido el Buey, muy buena opción")
#         character1.set_health(10)
    
#     time.sleep(3)
#     clear_console()

#     print("Este es su personaje: ")
#     print(character1)


