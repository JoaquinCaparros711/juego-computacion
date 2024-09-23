from classes.character import Character
#from classes.enemy import Enemy
from classes.dungeon import Dungeon
from classes.manager import Manager
from classes.item import Item
from constants import *
#import os, time




# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')


# def welcome(character):
    
#     print(NAME_OF_GAME)
#     time.sleep(1)
#     nameOfCharacter = input(ENTRY_NAME)
#     print(f"\n¡Hola {nameOfCharacter}!")
#     time.sleep(3)
#     print(WELCOME)
#     time.sleep(2)

#     while True:
#         print(POINTS)
#         time.sleep(3)
#         # Solicitar puntos para la vida
#         health = float(input(ENTRY_HEALTH))
#         if health > STARTING_POINTS or health < 0:
#             print(EXCEEDED_POINTS)
#             continue

#         remaining_points = STARTING_POINTS - health
#         print(f"\nTe quedan {remaining_points} puntos.\n")

#         # Bucle para solicitar puntos de fuerza
#         while True:
#             strength = float(input(ENTRY_STRENGTH))
#             if strength > remaining_points or strength < 0:
#                 print(EXCEEDED_POINTS)
#                 print(f"Te quedan {remaining_points} puntos.\n")
#             else:
#                 break

#         remaining_points -= strength
#         defense = remaining_points

#         # Creación del personaje
#         character.set_name(nameOfCharacter)
#         character.set_health(health)
#         character.set_strength(strength)
#         character.set_defense(defense)

#         print(CREATED_CHARACTER)
#         time.sleep(3)
#         clear_console()

#         break

#     print(ENTRY_ANIMAL)
#     time.sleep(2)
#     print(ANIMAL_MENU)

#     while True:
#         characterOption = input(f"{nameOfCharacter}!, ahora elija el animal que desea utilizar (1-3): ")
#         if characterOption in ["1", "2", "3"]:
#             break
#         else:
#             print(INVALID_OPTION_ANIMAL)
#             time.sleep(2)

#     if characterOption == "1":
#         print(f"\n{nameOfCharacter}, has elegido el Jabalí, muy buena opción!")
#         character.set_strength(character.get_strength() + 10)
#     elif characterOption == "2": #! Preguntar elifs
#         print(f"\n{nameOfCharacter}, has elegido el Rinoceronte, muy buena opción!")
#         character.set_defense(character.get_defense() + 10)
#     elif characterOption == "3":
#         print(f"\n{nameOfCharacter}, has elegido el Buey, muy buena opción!")
#         character.set_health(character.get_health() + 10)
    
#     time.sleep(3)
#     clear_console()

#     print(GAME_INFORMATION)

    
# def gameMenu(character, enemies, dungeon):
#     while True:
#         print("\n" + GAME_MENU)

#         playerOption = input(f"{character.get_name()}!, que desea hacer? (1-5): ")

#         if playerOption in ["1", "2", "3", "4", "5"]:
#             if playerOption == "1":
#                 clear_console()
#                 play(character, enemies, dungeon)
#             elif playerOption == "2":
#                 clear_console()
#                 print(character)
#             elif playerOption == "3":
#                 clear_console()
#                 print(GAME_INFORMATION)
#             elif playerOption == "4":
#                 clear_console()
#                 print("Opción no implementada aún.")
#             elif playerOption == "5":
#                 clear_console()
#                 break
#         else:
#             print(INVALID_OPTION_MENU)
#             time.sleep(1)


# def play(character, enemies, dungeon):
#     while True:
#         print("\n" + PLAY_MENU)

#         if not enemies:
#             print("¡Has derrotado a todos los enemigos de esta mazmorra!")
#             break

#         playOption = input(f"{character.get_name()}!, ¿qué desea hacer? (1-5): ")

#         if playOption in ["1", "2", "3", "4", "5"]:
#             if playOption == "1":  # Atacar
#                 clear_console()
#                 time.sleep(1)
#                 if enemies[0].get_health() <= 0:
#                     print("Enemigo muerto! \n")
#                     del enemies[0]  # Elimina al enemigo derrotado
#                     if not enemies:
#                         print(f"¡Has derrotado a todos los enemigos de la mazmorra {dungeon.get_level()}!")
#                         break
#                 else:
#                     character.attack(enemies[0])
#                     print(f"Vida del enemigo: {enemies[0].get_health()}")
#                     time.sleep(1)
#                     if enemies[0].get_health() <= 0:
#                         print("Enemigo muerto! \n")
#                         del enemies[0]
#                         if not enemies:
#                             print(f"¡Has derrotado a todos los enemigos de la mazmorra {dungeon.get_level()}!")
#                             dungeon.set_level(dungeon.get_level() + 1)
#                             enemies = dungeon.dungeonGenerator()
#                             #break
#                     else:
#                         print(f"Ahora es el turno de {enemies[0].get_name()} de atacar!")
#                         time.sleep(1)
#                         enemies[0].attack(character)
#                         print(f"Tu vida quedó en: {character.get_health()}")
#                         time.sleep(1)
#             elif playOption == "2":  # Ver características del personaje
#                 clear_console()
#                 print(character)
#             elif playOption == "3":  # Ver características del enemigo
#                 clear_console()
#                 print(enemies[0])
#             elif playOption == "4":  # Guardar
#                 clear_console()
#                 print("Opción no implementada aún.")
#             elif playOption == "5":  # Volver
#                 clear_console()
#                 break
#         else:
#             print(INVALID_OPTION_MENU)
#             time.sleep(1)


enemies = []
manager = Manager()
dungeon = Dungeon()
item = Item()
character = Character()
enemies = dungeon.dungeonGenerator()
manager.welcome(character)
# welcome(character1)
manager.gameMenu(character, enemies, dungeon, item)
#gameMenu(character1, enemies, dungeon)



