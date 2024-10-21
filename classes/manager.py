import os, time, random, pygame
from classes.item import Item
from constants import *
from colorama import Fore, init
from classes.saveAndLoad import SaveAndLoad
from classes.animations import Animations



animation = Animations()

# Inicialización de colorama y pygame para sonidos
init()
pygame.init()

# Cargar efectos de sonido
chest = pygame.mixer.Sound("sounds/chest.wav")
sound_win = pygame.mixer.Sound("sounds/win.wav")
sound_game_over = pygame.mixer.Sound("sounds/gameOver.wav")

# Inicialización de la clase SaveAndLoad para manejar guardado y carga de juegos
saveAndLoad = SaveAndLoad()


# Lista de objetos disponibles en el juego
list_items = [
    Item("Hamburguesa🍔", "Restaura 50 puntos de vida", "Salud", 50, "eat"),
    Item("Papas Fritas🍟", "Restaura 40 puntos de vida", "Salud", 40, "eat"),
    Item("Chocolate🍫", "Restaura 30 puntos de vida", "Salud", 30, "eat"),
    Item("Donas🍩", "Restaura 30 puntos de vida", "Salud", 30, "eat"),
    Item("Cangrejos🦀", "Disminuye 15 puntos de vida", "Salud", -15, "eat"),
    Item("Coca-Cola🥤", "Aumenta la fuerza en 5 puntos", "Fuerza", 5, "drink"),
    Item("Rockstar⚗️", "Disminuye la fuerza en 7 puntos", "Fuerza", -7, "drink"),
    Item("Zapatillas Nike👟", "Aumenta la fuerza en 5 puntos", "Fuerza", 5, "clothe"),
    Item("Cadena de Oro🪙", "Aumenta la fuerza en 10 puntos", "Fuerza", 10, "clothe"),
    Item("Disfraz de Batman🦇", "Aumenta la defensa en 15 puntos", "Defensa", 15, "clothe"),
    Item("Chaleco de kevlar🦺", "Aumenta la defensa en 12 puntos", "Defensa", 12, "clothe"),
    Item("Campera Gucci🧥", "Aumenta la defensa en 10 puntos", "Defensa", 10, "clothe"),
    Item("Musculosa🎽", "Disminuye la defensa en 8 puntos", "Defensa", -8, "clothe"),
]

class Manager:

    # Limpiar la consola según el sistema operativo
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')  

     # Lógica para manejar la transición y progreso en la mazmorra
    def handle_dungeon_progression(self, character, dungeon, enemies): #Lógica para manejar la transición y progreso en la mazmorra.
        if not enemies:
            self.clear_console()
            time.sleep(3)
            print(f"\n🎊 ¡Has derrotado a todos los enemigos de la mazmorra {dungeon.get_level()}! 🎊")

            # Verificar si es la mazmorra 3 para terminar el juego
            if dungeon.get_level() == 3:
                print(CONGRATULATIONS)
                sound_win.play()
                return True  # Retornar True si el juego debe terminar

            # Si no es la mazmorra 3, continúa con el siguiente nivel
            print(f"💪 Has matado al jefe de la mazmorra {dungeon.get_level()}, ¡vas muy bien!\nSubes de nivel...\n")
            time.sleep(1)
            character.level_up()
            print(AFTER_STATICSTIC)
            print(character)

            # Sube el nivel de la mazmorra y genera enemigos
            dungeon.set_level(dungeon.get_level() + 1)
            enemies.extend(dungeon.dungeonGenerator())
    
    # Mensaje de bienvenida y asignación de puntos
    def welcome(self, character):
        print(NAME_OF_GAME)
        time.sleep(1) 
        nameOfCharacter = input(ENTRY_NAME)
        print(f"\n¡Hola {nameOfCharacter}!")
        animation.animations(WELCOME)
        
        # Asignación de puntos de vida, fuerza y defensa
        while True:
            animation.animations(POINTS)
            time.sleep(3)
                    
            try:
                health = float(input(ENTRY_HEALTH))
                if health > STARTING_POINTS or health < 0 or health > 300:
                    print(EXCEEDED_POINTS)
                    continue
            except ValueError:
                print(INVALID_NUMBER_ERROR)
                continue

            remaining_points = STARTING_POINTS - health
            print(f"\nTe quedan {remaining_points} puntos.\n")

            while True:
                try:
                    strength = float(input(ENTRY_STRENGTH))
                    if strength > remaining_points or strength < 0 or strength > 150:
                        print(EXCEEDED_POINTS)
                        print(f"Te quedan {remaining_points} puntos.\n")
                    else:
                        break
                except ValueError:
                    print(INVALID_NUMBER_ERROR)
                    
            remaining_points -= strength
            defense = remaining_points
            
            # Asignación de los valores al personaje
            character.set_name(nameOfCharacter)
            character.set_health(health)
            character.set_strength(strength)
            character.set_defense(defense)
            
            # Mostrar estadísticas del personaje
            time.sleep(1)
            print(f"\nEn vida tienes {character.get_health()} puntos❤️\n")
            time.sleep(1)
            print(f"En daño tienes {character.get_strength()} puntos⚔️\n")
            time.sleep(1)
            print(f"Y en defensa tienes {character.get_defense()} puntos🛡️\n")
            time.sleep(1)

            print(CREATED_CHARACTER)
            time.sleep(3)
            self.clear_console()
            break
        

        # Selección del animal
        print(ENTRY_ANIMAL)
        time.sleep(2)
        print(ANIMAL_MENU)

        while True:
            characterOption = input(f"{Fore.BLUE}{nameOfCharacter}!, ahora elija el animal que desea utilizar (1-3): ")
            if characterOption in ["1", "2", "3"]:
                break
            else:
                print(INVALID_OPTION_ANIMAL)
                time.sleep(2)

        if characterOption == "1":
            print(f"\n{nameOfCharacter}, has elegido el Jabalí🐗, ¡una elección poderosa! Este animal es conocido por su tenacidad y fuerza.")
            character.set_strength(character.get_strength() + 20)
        elif characterOption == "2":
            print(f"\n{nameOfCharacter}, has elegido el Rinoceronte🦏, ¡excelente decisión! Con su gran defensa, es casi imparable en el campo de batalla.")
            character.set_defense(character.get_defense() + 20)
        elif characterOption == "3":
            print(f"\n{nameOfCharacter}, has elegido el Buey🐂, ¡una elección formidable! Este noble animal te otorgará una gran cantidad de salud para tus aventuras.")
            character.set_health(character.get_health() + 30)

        time.sleep(6)
        self.clear_console()

        print(GAME_INFORMATION)

        
    def gameMenu(self, character, enemies, dungeon, item, list_items_saved):

        while True:
            print("\n" + GAME_MENU)

            playerOption = input(f"{Fore.BLUE}{character.get_name()}!, ¿qué desea hacer? (1-5): ")

            if playerOption in ["1", "2", "3", "4", "5", "6"]:
                if playerOption == "1":
                    self.clear_console()
                    self.play(character, enemies, dungeon, item, list_items_saved)
                elif playerOption == "2":
                    self.clear_console()
                    print(character)
                elif playerOption == "3":
                    self.clear_console()
                    print(GAME_INFORMATION)
                elif playerOption == "4": 
                    self.clear_console()
                    saveAndLoad.save_game(character, enemies, dungeon, list_items_saved)
                elif playerOption == "5":
                    self.clear_console()
                    break
            else:
                self.clear_console()
                print(INVALID_OPTION_MENU)
                time.sleep(1)
    
    def save_menu(self, character, enemies, dungeon, item, list_items_saved):
        self.clear_console()
        print(NAME_OF_GAME)
        time.sleep(1)
        while True:
            print(SAVE_MENU)
            save_option = input(ENTRY_SAVE)
            if save_option == "1":
                self.clear_console()
                character, enemies, dungeon, list_items_saved = saveAndLoad.load_game() #Carga la partida
                if character is None:
                    print(COULD_NOT_BE_LOADED)
                else:
                    self.gameMenu(character, enemies, dungeon, item, list_items_saved)
            elif save_option == "2":
                self.clear_console()
                self.welcome(character)
                self.gameMenu(character, enemies, dungeon, item, list_items_saved)
            elif save_option == "3":
                self.clear_console()
                break
            else:
                self.clear_console()
                print(INVALID_OPTION_MENU_SAVE)
    

    def play(self, character, enemies, dungeon, item, list_items_saved):
        while True:
            print("\n" + PLAY_MENU)

            playOption = input(f"{Fore.BLUE}{character.get_name()}!, ¿qué desea hacer? (1-6): ")

            if playOption in ["1", "2", "3", "4", "5", "6"]:
                if playOption == "1":  
                    self.clear_console()
                    time.sleep(1)

                    if character.get_health() == 0:
                        print(GAME_OVER)
                        sound_game_over.play()
                        break
                    else:
                        if not enemies and dungeon.get_level() == 3:
                            self.handle_dungeon_progression(character, dungeon, enemies)
                        else:
                            first_turn = random.choice(["character", "enemy"])
                            current_enemy = enemies[0]
                            
                            if character.get_super_attack() == True:
                                status_super_attack = "DISPONIBLE"
                            else:
                                status_super_attack = "NO DISPONIBLE"

                            if (first_turn == "character"):

                                animation.animations(f"🆚 Tu oponente es: *{current_enemy.get_name()}*")
                                time.sleep(1)
                                animation.animations(f"Es tu turno de atacar, super ataque {status_super_attack}, {character.get_name()}!⚔️")
                                time.sleep(1)

                                character.choose_super_atack(character, current_enemy)

                                animation.animations(f"💥 ¡Has golpeado a {current_enemy.get_name()}!")
                                time.sleep(1)
                                animation.animations(f"La vida actual de {current_enemy.get_name()} es: {current_enemy.get_health()} ❤️")
                                time.sleep(1)  
                                                                
                                if current_enemy.get_health() <= 0:
                                    print("🎉 ¡Enemigo derrotado! 🎉\n")
                                    if dungeon.get_level() <= 3 and enemies:
                                        del enemies[0] 
                                        item.handle_item_drop(character, item, list_items, list_items_saved)
                                        self.handle_dungeon_progression(character, dungeon, enemies)
                                        break
                                animation.animations(f"Es turno de, {current_enemy.get_name()} de contraatacar!⚔️")
                                time.sleep(1)
                                current_enemy.attack(character)
                                animation.animations(f"💔 ¡Cuidado! Tu vida ha quedado en: *{character.get_health()}*")
                                time.sleep(1)

                            if (first_turn == "enemy"):
                                animation.animations(f"🆚 Tu oponente es: *{current_enemy.get_name()}*")
                                time.sleep(1)
                                animation.animations(f"Empieza atacando, {current_enemy.get_name()}!⚔️")
                                time.sleep(1)
                                current_enemy.attack(character)
                                animation.animations(f"💔 ¡Cuidado! Tu vida ha quedado en: *{character.get_health()}*")
                                time.sleep(1)

                                if character.get_health() == 0:
                                    print(GAME_OVER)
                                    sound_game_over.play()
                                    break           
                                
                                animation.animations(f"Ahora es tu turno de atacar, super ataque {status_super_attack}, {character.get_name()}!⚔️")
                                time.sleep(1)
                                character.choose_super_atack(character, current_enemy)
                                animation.animations(f"💥 ¡Has golpeado a {current_enemy.get_name()}!")
                                time.sleep(1)
                                animation.animations(f"La vida actual de {current_enemy.get_name()} es: {current_enemy.get_health()} ❤️")
                                time.sleep(1)  
                                                                
                                if current_enemy.get_health() <= 0:
                                    print("🎉 ¡Enemigo derrotado! 🎉\n")
                                    if dungeon.get_level() <= 3 and enemies:
                                        del enemies[0] 
                                        item.handle_item_drop(character, item, list_items, list_items_saved)
                                        self.handle_dungeon_progression(character, dungeon, enemies)

                elif playOption == "2": 
                    self.clear_console()
                    print(character)
                elif playOption == "3": 
                    self.clear_console()
                    print(enemies[0])
                elif playOption == "4": 
                    chest.play()
                    self.clear_console()
                    while True:
                        items_options = input(ITEMS_MENU)
                        if items_options == "1":
                            self.clear_console()
                            item.use_item(list_items_saved, character)
                        elif items_options == "2":
                            self.clear_console()
                            break
                        else:
                            self.clear_console()
                            print(INVALID_OPTION_ITEMS_MENU)
                elif playOption == "5": 
                    self.clear_console()
                    saveAndLoad.save_game(character, enemies, dungeon, list_items_saved)
                elif playOption == "6":  
                    self.clear_console()
                    break
            else:
                self.clear_console()
                print(INVALID_OPTION_MENU)
                time.sleep(1)
