import os
import time
from classes.character import Character


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# def print_menu():
#     clear_console()
#     print(f"{'-'*40}")
#     print(f"{' MENÚ PRINCIPAL ':-^40}")
#     print(f"{'-'*40}")
#     print(f"{'-'*40}")


STARTING_POINTS = 250


def nameOfGame():
    print("\n██╗░░░░░░█████╗░░██████╗  ░█████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░░█████╗░░██████╗")
    print("██║░░░░░██╔══██╗██╔════╝  ██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔════╝")
    print("██║░░░░░███████║╚█████╗░  ███████║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝███████║╚█████╗░")
    print("██║░░░░░██╔══██║░╚═══██╗  ██╔══██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══██║░╚═══██╗")
    print("███████╗██║░░██║██████╔╝  ██║░░██║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║██║░░██║██████╔╝")
    print("╚══════╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n")
    print("██████╗░███████╗██╗░░░░░  ░░░░░██╗░█████╗░██████╗░░█████╗░██╗░░░░░██╗")
    print("██╔══██╗██╔════╝██║░░░░░  ░░░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║")
    print("██║░░██║█████╗░░██║░░░░░  ░░░░░██║███████║██████╦╝███████║██║░░░░░██║")
    print("██║░░██║██╔══╝░░██║░░░░░  ██╗░░██║██╔══██║██╔══██╗██╔══██║██║░░░░░██║")
    print("██████╔╝███████╗███████╗  ╚█████╔╝██║░░██║██████╦╝██║░░██║███████╗██║")
    print("╚═════╝░╚══════╝╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝\n")


#! Preguntar funciones si van en el main
def welcome():

    nameOfCharacter = input("\nIngrese el nombre para su personaje: ")

    print("   ¡Bienvenido a las Aventuras del Jabalí!   ")


    while True:
        print(f"Tienes {STARTING_POINTS} puntos para distribuir en vida, fuerza y defensa.")
        
        # Solicitar puntos para la vida
        health = float(input("Ingrese la cantidad de vida que desea tener: "))
        if health > STARTING_POINTS or health < 0:
            print("Te excediste de puntos o ingresaste un valor no válido. Intenta de nuevo.")
            continue

        remaining_points = STARTING_POINTS - health
        print(f"Te quedan {remaining_points} puntos.")

        # Bucle para solicitar puntos de fuerza
        while True:
            strength = float(input("Ingrese la cantidad de fuerza que desea tener: "))
            if strength > remaining_points or strength < 0:
                print(f"Te excediste de puntos o ingresaste un valor no válido. Te quedan {remaining_points} puntos.")
            else:
                break

        remaining_points -= strength
        print(f"Te quedan {remaining_points} puntos.")
        defense = remaining_points

        # Creación del personaje
        character1 = Character(nameOfCharacter, health, strength, defense)
        print("Personaje creado con exito!!")

        break

    print("\nAntes de comenzar, deberá elegir un tipo de animal:")
    time.sleep(1)
    print("(1) - Jabalí(+10 de fuerza)")
    print("(2) - Rinoceronte(+10 de defensa)")
    print("(3) - Buey(+10 de salud)")

    while True:
        characterOption = input(f"\nBienvenido {nameOfCharacter}!, ahora elija el Jabalí que desea utilizar (1-3): ")
        if characterOption in ["1", "2", "3"]:
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 1 y 3.")
            time.sleep(2)

    if characterOption == "1":
        print(f"\n{nameOfCharacter}, has elegido el Jabalí, muy buena opción")
        character1.set_strength(10)
    elif characterOption == "2":
        print(f"\n{nameOfCharacter}, has elegido el Rinoceronte, muy buena opción")
        character1.set_defense(10)
    elif characterOption == "3":
        print(f"\n{nameOfCharacter}, has elegido el Buey, muy buena opción")
        character1.set_health(10)
    
    time.sleep(3)

    print(character1)


