# from classes.character import Character
# from classes.enemy import Enemy
from classes.item import Item
from constants import *
import os, time

list_items = [
    Item("Hamburguesa", "Restaura 50 puntos de vida", "Salud", 50),
    Item("Papas Fritas", "Restaura 40 puntos de vida", "Salud", 40),
    Item("Chocolate", "Restaura 30 puntos de vida", "Salud", 30),
    Item("Coffler", "Restaura 30 puntos de vida", "Salud", 30),
    Item("Cangrejos", "Disminuye 10 puntos de vida", "Salud", -10),
    Item("Coca-Cola", "Aumenta la Fuerza en 5 puntos", "Fuerza", 5),
    Item("Rockstar", "Disminuye la Fuerza en 5 puntos", "Fuerza", -5),
    Item("Zapatillas Nike", "Aumenta la Fuerza en 5 puntos", "Fuerza", 5),
    Item("Cadena de Oro", "Aumenta la Fuerza en 10 puntos", "Fuerza", 10),
    Item("Disfraz de Batman", "Aumenta la defensa en 15 puntos", "Defensa", 15),
    Item("Chaleco de kevlar", "Aumenta la defensa en 20 puntos", "Defensa", 20),
    Item("Campera Gucci", "Aumenta la defensa en 10 puntos", "Defensa", 10),
    Item("Campera rota", "Disminuye la defensa en 5 puntos", "Defensa", -5),
]

class Manager:

    def __init__(self):
        pass

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def welcome(self, character):
    
        print(NAME_OF_GAME)
        time.sleep(1)
        nameOfCharacter = input(ENTRY_NAME)
        print(f"\n¡Hola {nameOfCharacter}!")
        time.sleep(3)
        print(WELCOME)
        time.sleep(2)

        while True:
            print(POINTS)
            time.sleep(3)
            # Solicitar puntos para la vida
            health = float(input(ENTRY_HEALTH))
            if health > STARTING_POINTS or health < 0:
                print(EXCEEDED_POINTS)
                continue

            remaining_points = STARTING_POINTS - health
            print(f"\nTe quedan {remaining_points} puntos.\n")

            # Bucle para solicitar puntos de fuerza
            while True:
                strength = float(input(ENTRY_STRENGTH))
                if strength > remaining_points or strength < 0:
                    print(EXCEEDED_POINTS)
                    print(f"Te quedan {remaining_points} puntos.\n")
                else:
                    break

            remaining_points -= strength
            defense = remaining_points

            # Creación del personaje
            character.set_name(nameOfCharacter)
            character.set_health(health)
            character.set_strength(strength)
            character.set_defense(defense)

            print(CREATED_CHARACTER)
            time.sleep(3)
            self.clear_console()

            break

        print(ENTRY_ANIMAL)
        time.sleep(2)
        print(ANIMAL_MENU)

        while True:
            characterOption = input(f"{nameOfCharacter}!, ahora elija el animal que desea utilizar (1-3): ")
            if characterOption in ["1", "2", "3"]:
                break
            else:
                print(INVALID_OPTION_ANIMAL)
                time.sleep(2)

        if characterOption == "1":
            print(f"\n{nameOfCharacter}, has elegido el Jabalí, muy buena opción!")
            character.set_strength(character.get_strength() + 20)
        elif characterOption == "2": #! Preguntar elifs
            print(f"\n{nameOfCharacter}, has elegido el Rinoceronte, muy buena opción!")
            character.set_defense(character.get_defense() + 20)
        elif characterOption == "3":
            print(f"\n{nameOfCharacter}, has elegido el Buey, muy buena opción!")
            character.set_health(character.get_health() + 30)
        
        time.sleep(3)
        self.clear_console()

        print(GAME_INFORMATION)

        
    def gameMenu(self, character, enemies, dungeon, item):
        while True:
            print("\n" + GAME_MENU)

            playerOption = input(f"{character.get_name()}!, que desea hacer? (1-5): ")

            if playerOption in ["1", "2", "3", "4", "5"]:
                if playerOption == "1":
                    self.clear_console()
                    self.play(character, enemies, dungeon, item)
                elif playerOption == "2":
                    self.clear_console()
                    print(character)
                elif playerOption == "3":
                    self.clear_console()
                    print(GAME_INFORMATION)
                elif playerOption == "4":
                    self.clear_console()
                    print("Opción no implementada aún.")
                elif playerOption == "5":
                    self.clear_console()
                    break
            else:
                print(INVALID_OPTION_MENU)
                time.sleep(1)


    def play(self, character, enemies, dungeon, item):
        while True:
            print("\n" + PLAY_MENU)

            playOption = input(f"{character.get_name()}!, ¿qué desea hacer? (1-5): ")

            if playOption in ["1", "2", "3", "4", "5"]:
                if playOption == "1":  # Atacar
                    self.clear_console()
                    time.sleep(1)
                    if character.get_health() == 0:
                        print("GAME OVER")#!Constante
                    else:
                        character.attack(enemies[0])
                        print(f"🆚 Tu oponente es: **{enemies[0].get_name()}**")
                        time.sleep(1)
                        print(f"⚔️ Es tu turno de atacar, {character.get_name()}!")
                        time.sleep(1)
                        print(f"💥 ¡Has golpeado a {enemies[0].get_name()}!")
                        print(f"❤️ La vida actual de {enemies[0].get_name()} es: **{enemies[0].get_health()}**")
                        time.sleep(1)
                        if enemies[0].get_health() <= 0:
                            print("Enemigo muerto! \n")                 
                            
                            
                            if dungeon.get_level() <= 3 and enemies:
                                del enemies[0]
                                print(ITEMS_MENU)
                                dropped_item = item.drop_random_item(list_items)
                                itemOption = input(f"{character.get_name()}!, ¿qué desea hacer? (1-2): ")
                                if itemOption == "1": 
                                    print(dropped_item)
                                    time.sleep(3)
                                    self.clear_console()
                                    if dropped_item.get_type() == "Salud":
                                        if character.get_health() <= 0:
                                            break
                                        character.set_health(character.get_health() + dropped_item.get_value())
                                    elif dropped_item.get_type() == "Fuerza":
                                        character.set_strength(character.get_strength() + dropped_item.get_value())
                                    elif dropped_item.get_type() == "Defensa":
                                        character.set_defense(character.get_defense() + dropped_item.get_value())
                                else:
                                    print(f"Has perdido este Item: \n{dropped_item}")

                            if not enemies:
                                print(f"¡Has derrotado a todos los enemigos de la mazmorra {dungeon.get_level()}!")
                                
                                # Verificar si es la mazmorra 3 para terminar el juego
                                if dungeon.get_level() == 3:
                                    print("¡Felicidades! Has completado todas las mazmorras y terminado el juego.")
                                    break  # Termina el juego

                                # Si no es la mazmorra 3, continúa con el siguiente nivel
                                print(f"Has matado al jefe de la mazmorra {dungeon.get_level()}, vas muy bien!\nSubes de nivel...")
                                print(BEFORE_STATICSTIC)
                                print(character)
                                time.sleep(1)
                                character.level_up()
                                print(AFTER_STATICSTIC)
                                print(character)
                                
                                # Subir el nivel de la mazmorra
                                dungeon.set_level(dungeon.get_level() + 1)
                                
                                # Generar nuevos enemigos
                                enemies = dungeon.dungeonGenerator()

                        else:
                            print(f"⚠️ Ahora es el turno de {enemies[0].get_name()} de contraatacar...")
                            enemies[0].attack(character)
                            time.sleep(1)
                            print(f"💔 ¡Cuidado! Tu vida ha quedado en: **{character.get_health()}**")
                            time.sleep(1)
                            if character.get_health() == 0:
                                self.clear_console()
                                print(GAME_OVER)
                                break

                elif playOption == "2":  # Ver características del personaje
                    self.clear_console()
                    print(character)
                elif playOption == "3":  # Ver características del enemigo
                    self.clear_console()
                    print(enemies[0])
                elif playOption == "4":  # Guardar
                    self.clear_console()
                    print("Opción no implementada aún.")
                elif playOption == "5":  # Volver
                    self.clear_console()
                    break
                else:
                    print(INVALID_OPTION_MENU)
                    time.sleep(1)
