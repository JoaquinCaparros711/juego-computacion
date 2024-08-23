from classes.character import Character
from classes.enemy import Enemy
from constants import *
import os, time



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome(character):
    
    nameOfCharacter = input("\nIngrese el nombre para su personaje: ")
    print(f"\n¡Hola {nameOfCharacter}!")
    time.sleep(3)
    print("╔═════════════════════════════════════════════╗")
    print("║   ¡Bienvenido a las Aventuras del Jabalí!   ║")
    print("╚═════════════════════════════════════════════╝\n")
    time.sleep(3)

    while True:
        print("╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"║Primero que nada, tienes {STARTING_POINTS} puntos para distribuir en vida, fuerza y defensa.║")
        print("╚══════════════════════════════════════════════════════════════════════════════╝")
        time.sleep(1)
        print("         ===> ¡Ojo! Enfocá bien tus puntos para sobrevivir <===\n")
        time.sleep(2)
        # Solicitar puntos para la vida
        health = float(input("Ingrese la cantidad de vida que desea tener: "))
        if health > STARTING_POINTS or health < 0:
            print("Te excediste de puntos o ingresaste un valor no válido. Intenta de nuevo.\n")
            continue

        remaining_points = STARTING_POINTS - health
        print(f"\nTe quedan {remaining_points} puntos.\n")

        # Bucle para solicitar puntos de fuerza
        while True:
            strength = float(input("Ingrese la cantidad de fuerza que desea tener: "))
            if strength > remaining_points or strength < 0:
                print(f"Te excediste de puntos o ingresaste un valor no válido. Te quedan {remaining_points} puntos.\n")
            else:
                break

        remaining_points -= strength
        defense = remaining_points

        # Creación del personaje
        character.set_name(nameOfCharacter)
        character.set_health(health)
        character.set_strength(strength)
        character.set_defense(defense)

        print("\nPersonaje creado con exito!!")
        time.sleep(3)
        clear_console()

        break

    print("\nAntes de comenzar, deberá elegir un tipo de animal:")
    time.sleep(2)
    print("╔═════════════════════════════════════════════╗")
    print("║(1) - Jabalí(+10 de fuerza)                  ║")
    print("║(2) - Rinoceronte(+10 de defensa)            ║")
    print("║(3) - Buey(+10 de salud)                     ║")
    print("╚═════════════════════════════════════════════╝\n")

    while True:
        characterOption = input(f"{nameOfCharacter}!, ahora elija el animal que desea utilizar (1-3): ")
        if characterOption in ["1", "2", "3"]:
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 1 y 3.")
            time.sleep(2)

    if characterOption == "1":
        print(f"\n{nameOfCharacter}, has elegido el Jabalí, muy buena opción!")
        character.set_strength(character.get_strength() + 10)
    elif characterOption == "2": #! Preguntar elifs
        print(f"\n{nameOfCharacter}, has elegido el Rinoceronte, muy buena opción!")
        character.set_defense(character.get_defense() + 10)
    elif characterOption == "3":
        print(f"\n{nameOfCharacter}, has elegido el Buey, muy buena opción!")
        character.set_health(character.get_health() + 10)
    
    time.sleep(3)
    clear_console()

    print("Este es su personaje: ")
    print(character)

    print(GAME_INFORMATION)

    
def gameMenu(character, enemy):
    while True:
        print("\n" + GAME_MENU)

        playerOption = input(f"{character.get_name()}!, que desea hacer? (1-5): ")

        if playerOption in ["1", "2", "3", "4", "5"]:
            if playerOption == "1":
                clear_console()
                play(character, enemy)
            elif playerOption == "2":
                clear_console()
                print(character)
            elif playerOption == "3":
                clear_console()
                print(GAME_INFORMATION)
            elif playerOption == "4":
                clear_console()
                print("Opción no implementada aún.")
            elif playerOption == "5":
                clear_console()
                break
        else:
            print("Opción no válida. Por favor, elegí un número entre 1 y 5.")
            time.sleep(1)


def dungeonGenerator(dungeon):
    pass #! En base a la dungeon, 1,2, o 3 generar los bichos con sus respectivos puntos


def play(character, enemy):
    while True:
        print("\n" + PLAY_MENU)

        playOption = input(f"{character.get_name()}!, que desea hacer? (1-5): ")

        if playOption in ["1", "2", "3", "4", "5"]:
            if playOption == "1":  # Atacar
                clear_console()
                character.attack(enemy)
            elif playOption == "2":  # Ver características del personaje
                clear_console()
                print(character)
            elif playOption == "3":  # Ver características del enemigo
                clear_console()
                print(enemy)
            elif playOption == "4":  # Guardar
                clear_console()
                print("Opción no implementada aún.")
            elif playOption == "5":  # Volver
                clear_console()
                break
        else:
            print("Opción no válida. Por favor, elegí un número entre 1 y 5.")
            time.sleep(1)

                
dungeon = 1
enemy = Enemy("piche")
character1 = Character()

print(NAME_OF_GAME)
welcome(character1)
gameMenu(character1, enemy)



