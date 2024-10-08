import os, time, pickle, random
from classes.item import Item
from constants import *



list_items = [
    Item("Hamburguesa🍔", "Restaura 50 puntos de vida", "Salud", 50),
    Item("Papas Fritas🍟", "Restaura 40 puntos de vida", "Salud", 40),
    Item("Chocolate🍫", "Restaura 30 puntos de vida", "Salud", 30),
    Item("Donas🍩", "Restaura 30 puntos de vida", "Salud", 30),
    Item("Cangrejos🦀", "Disminuye 15 puntos de vida", "Salud", -15),
    Item("Coca-Cola🥤", "Aumenta la fuerza en 5 puntos", "Fuerza", 5),
    Item("Rockstar⚗️", "Disminuye la fuerza en 7 puntos", "Fuerza", -7),
    Item("Zapatillas Nike👟", "Aumenta la fuerza en 5 puntos", "Fuerza", 5),
    Item("Cadena de Oro🪙", "Aumenta la fuerza en 10 puntos", "Fuerza", 10),
    Item("Disfraz de Batman🦇", "Aumenta la defensa en 15 puntos", "Defensa", 15),
    Item("Chaleco de kevlar🦺", "Aumenta la defensa en 12 puntos", "Defensa", 12),
    Item("Campera Gucci🧥", "Aumenta la defensa en 10 puntos", "Defensa", 10),
    Item("Musculosa🎽", "Disminuye la defensa en 8 puntos", "Defensa", -8),
]

class Manager:

    def __init__(self):
        pass

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # def show_dungeon_map(self, dungeon, enemies):
    #     """Muestra un mapa detallado de la mazmorra con la ubicación de los enemigos."""
    #     dungeon_size = 5  # Tamaño del mapa de la mazmora (5x5)
    #     map_grid = [['🟩' for _ in range(dungeon_size)] for _ in range(dungeon_size)]

    #     # Colocar al jugador en la posición inicial (0,0)
    #     map_grid[0][0] = '👤'

    #     # Colocar a los enemigos en posiciones aleatorias dentro del mapa
    #     enemy_positions = []
    #        for enemy in enemies:
    #            while True:
    #                enemy_position = (random.randint(1, dungeon_size - 1), random.randint(1, dungeon_size - 1))
    #                if enemy_position not in enemy_positions and map_grid[enemy_position[0]][enemy_position[1]] == '🟩':
    #                    enemy_positions.append(enemy_position)
    #                    map_grid[enemy_position[0]][enemy_position[1]] = '👾'  # Símbolo para representar a un enemigo
    #                    break

    #     # Mostrar el mapa en la consola
    #     print(f"\n📜 Mapa de la Mazmora {dungeon.get_level()}:")
    #     for row in map_grid:
    #         print(" ".join(row))
        
    #     # Mostrar información adicional sobre los enemigos
    #     print("\n🧚‍♂️ Enemigos en la mazmora:")
    #     for idx, enemy in enumerate(enemies):
    #         enemy_position = enemy_positions[idx]
    #         print(f"👾 {enemy.get_name()} está en la posición {enemy_position}.")

    #     print("\nLeyenda: 👤 = Jugador, 👾 = Enemigo, 🟩 = Espacio libre")

    # Método para guardar el juego
    def save_game(self, character, enemies, dungeon, list_items_saved, file_name="savegame.pkl"):
        save_data = {
            'character': character,
            'enemies': enemies,
            'dungeon': dungeon,
            'list_items_saved': list_items_saved
        }
        with open(file_name, 'wb') as save_file:
            pickle.dump(save_data, save_file)
        print(f"\nProgreso guardado exitosamente en {file_name} 💾")


    # Método para cargar el juego
    def load_game(self, file_name="savegame.pkl"):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as save_file:
                save_data = pickle.load(save_file)
            print(LOADED_PROCESS)
            return save_data['character'], save_data['enemies'], save_data['dungeon'], save_data['list_items_saved']
        else:
            print(FILE_NOT_FOUND)
            return None, None, None
    
    def use_item(self, list_items_saved, character):
        # Mostrar inventario
        if len(list_items_saved) <= 0:
            print("📭 Tu inventario está vacío.")
            return

        print("🎒 Inventario:")
        for i in range(len(list_items_saved)):
            print("item", i + 1, list_items_saved[i].get_name())

        while True:
            try:
                item_choice = int(input("Selecciona el número del item que deseas usar (Ingresa 9 si no quieres usar ninguno): "))
                item_choice = item_choice - 1
                
                if item_choice == 9:
                    break

                selected_item = list_items_saved[item_choice]
                # Aplicar los efectos del item al personaje
                if selected_item.get_type() == "Salud":
                    character.set_health(character.get_health() + selected_item.get_value())
                    print(f"\n{selected_item.get_effect()}!!")
                    print(f"💊 Salud actual: {character.get_health()}")
                elif selected_item.get_type() == "Fuerza":
                    character.set_strength(character.get_strength() + selected_item.get_value())
                    print(f"\n{selected_item.get_effect()}!!")
                    print(f"💪 Fuerza actual: {character.get_strength()}")
                elif selected_item.get_type() == "Defensa":
                    character.set_defense(character.get_defense() + selected_item.get_value())
                    print(f"\n{selected_item.get_effect()}!!")
                    print(f"🛡️ Defensa actual: {character.get_defense()}")
                # Eliminar el item del inventario tras usarlo
                list_items_saved.pop(item_choice)
                break
            except ValueError:
                print("Por favor ingresa un número válido.\n")
        
    def handle_item_drop(self, character, item, list_items, list_items_saved): #Lógica para manejar la recolección del item tras derrotar a un enemigo.
        dropped_item = item.drop_random_item(list_items)
        print(f"{character.get_name()} se ha añadido al inventario: \n{dropped_item.get_name()}")
        list_items_saved.append(dropped_item)
        


    def handle_dungeon_progression(self, character, dungeon, enemies): #Lógica para manejar la transición y progreso en la mazmorra.
        if not enemies:
            print(f"\n🎊 ¡Has derrotado a todos los enemigos de la mazmorra {dungeon.get_level()}! 🎊")

            # Verificar si es la mazmorra 3 para terminar el juego
            if dungeon.get_level() == 3:
                print(CONGRATULATIONS)
                return True  # Retornar True si el juego debe terminar

            # Si no es la mazmorra 3, continúa con el siguiente nivel
            print(f"💪 Has matado al jefe de la mazmorra {dungeon.get_level()}, ¡vas muy bien!\nSubes de nivel...\n")
            time.sleep(1)
            character.level_up()
            print(AFTER_STATICSTIC)
            print(character)

            dungeon.set_level(dungeon.get_level() + 1)

            enemies.extend(dungeon.dungeonGenerator())
        
        
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

            # Bucle para solicitar puntos de fuerza
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
            print(f"\n{nameOfCharacter}, has elegido el Jabalí🐗, ¡una elección poderosa! Este animal es conocido por su tenacidad y resistencia.")
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

            playerOption = input(f"{character.get_name()}!, ¿qué desea hacer? (1-5): ")

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
                    self.save_game(character, enemies, dungeon, list_items_saved)
                elif playerOption == "5":
                    self.clear_console()
                    break
            else:
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
                character, enemies, dungeon, list_items_saved = self.load_game()
                if character is None:
                    print(COULD_NOT_BE_LOADED)
                else:
                    print(GAME_LOADED_SUCCESSFULLY)
                    self.gameMenu(character, enemies, dungeon, item, list_items_saved)
            elif save_option == "2":
                self.clear_console()
                self.welcome(character)
                self.gameMenu(character, enemies, dungeon, item, list_items_saved)
            elif save_option == "3":
                self.clear_console()
                break
            else:
                print(INVALID_OPTION_MENU_SAVE)
    
    def choose_super_atack(self, character, current_enemy):
        while True:
            if character.get_super_attack() == False:
                print(f"{character.get_name()} no tiene disponible el super ataque hasta subir de nivel (atacás normal)⚔️")
                character.attack(current_enemy)
                break
            try:
                select_super_attack = input(f"{character.get_name()} quieres usar tu super ataque(SI:1 NO:2)⚔️: ")
                if select_super_attack == "1":
                        character.super_attack(current_enemy)
                        character.set_super_attack(False)
                        break
                elif select_super_attack == "2":
                    character.attack(current_enemy)
                    break
            except ValueError:
                print("Poner error")
                break
    

    def play(self, character, enemies, dungeon, item, list_items_saved):
        while True:
            print("\n" + PLAY_MENU)

            playOption = input(f"{character.get_name()}!, ¿qué desea hacer? (1-6): ")

            if playOption in ["1", "2", "3", "4", "5", "6"]:
                if playOption == "1":  
                    self.clear_console()
                    time.sleep(1)

                    if character.get_health() == 0:
                        print(GAME_OVER)
                        break
                    else:
                        first_turn = random.choice(["character", "enemy"])
                        current_enemy = enemies[0]
                        
                        if character.get_super_attack() == True:
                            status_super_attack = "DISPONIBLE"
                        else:
                            status_super_attack = "NO DISPONIBLE"

                        if (first_turn == "character"):

                            print(f"🆚 Tu oponente es: *{current_enemy.get_name()}*")
                            time.sleep(1)
                            print(f"Es tu turno de atacar ⚔️, super ataque {status_super_attack}, {character.get_name()}!")
                            time.sleep(1)

                            self.choose_super_atack(character, current_enemy)

                            print(f"💥 ¡Has golpeado a {current_enemy.get_name()}!")
                            time.sleep(1)
                            print(f"La vida actual de {current_enemy.get_name()} es: {current_enemy.get_health()}❤️")
                            time.sleep(1)  
                                                            
                            if current_enemy.get_health() <= 0:
                                print("🎉 ¡Enemigo derrotado! 🎉\n")
                                if dungeon.get_level() <= 3 and enemies:
                                    del enemies[0] 
                                    self.handle_item_drop(character, item, list_items, list_items_saved)
                                    self.handle_dungeon_progression(character, dungeon, enemies)
                                    break
                            print(f"Es turno de, {current_enemy.get_name()} de contraatacar!⚔️")
                            time.sleep(1)
                            current_enemy.attack(character)
                            print(f"💔 ¡Cuidado! Tu vida ha quedado en: *{character.get_health()}*")
                            time.sleep(1)

                        if (first_turn == "enemy"):
                            print(f"🆚 Tu oponente es: *{current_enemy.get_name()}*")
                            time.sleep(1)
                            print(f"Empieza atacando, {current_enemy.get_name()}!⚔️")
                            time.sleep(1)
                            current_enemy.attack(character)
                            print(f"💔 ¡Cuidado! Tu vida ha quedado en: *{character.get_health()}*")
                            time.sleep(1)

                            if character.get_health() == 0:
                                print(GAME_OVER)
                                break           

                            print(f"Ahora es tu turno de atacar, super ataque {status_super_attack}, {character.get_name()}!⚔️")
                            time.sleep(1)
                            self.choose_super_atack(character, current_enemy)
                            print(f"💥 ¡Has golpeado a {current_enemy.get_name()}!")
                            time.sleep(1)
                            print(f"La vida actual de {current_enemy.get_name()} es: {current_enemy.get_health()}❤️")
                            time.sleep(1)  
                                                            
                            if current_enemy.get_health() <= 0:
                                print("🎉 ¡Enemigo derrotado! 🎉\n")
                                if dungeon.get_level() <= 3 and enemies:
                                    del enemies[0] 
                                    self.handle_item_drop(character, item, list_items, list_items_saved)
                                    self.handle_dungeon_progression(character, dungeon, enemies)


                elif playOption == "2": 
                    self.clear_console()
                    print(character)
                elif playOption == "3": 
                    self.clear_console()
                    print(enemies[0])
                elif playOption == "4": 
                    self.clear_console()
                    items_options = input(ITEMS_MENU)
                    if items_options == "1":
                        self.clear_console()
                        self.use_item(list_items_saved, character)
                    elif items_options == "2":
                        break
                    else:
                        print(INVALID_OPTION_ITEMS_MENU)
                elif playOption == "5": 
                    self.clear_console()
                    self.save_game(character, enemies, dungeon, list_items_saved)
                elif playOption == "6":  
                    self.clear_console()
                    break
                    # self.show_dungeon_map(dungeon, enemies)
                else:
                    print(INVALID_OPTION_MENU)
                    time.sleep(1)
