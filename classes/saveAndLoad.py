import os, pickle
from constants import *


class SaveAndLoad:


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
        print(f"{Fore.BLUE}\n{character.get_name()} tu proceso se ha guardado exitosamente en {file_name} 💾")


    # Método para cargar el juego
    def load_game(self, file_name="savegame.pkl"):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as save_file:
                save_data = pickle.load(save_file)
            print(GAME_LOADED_SUCCESSFULLY)
            return save_data['character'], save_data['enemies'], save_data['dungeon'], save_data['list_items_saved']
        else:
            print(FILE_NOT_FOUND)
            return None, None, None