from classes.character import *
import random, time, pygame
from constants import *


pygame.init()
eating = pygame.mixer.Sound("sounds/eating.wav")
drinking = pygame.mixer.Sound("sounds/drinking.wav")
clothe = pygame.mixer.Sound("sounds/clothe.wav")


class Item:
    def __init__(self, name = "", effect = "", type = "", value = 0, edible = ""):
        self.__name = name
        self.__effect = effect
        self.__type = type
        self.__value = value
        self.__edible = edible

    def __str__(self):
        return f"{self.__name}:\n{self.__effect}"

    def get_name(self):
        return self.__name

    def get_effect(self):
        return self.__effect
    
    def get_type(self):
        return self.__type
    
    def get_value(self):
        return self.__value

    def get_edible(self):
        return self.__edible
    
    # Función para dropear un ítem al azar
    def drop_random_item(self, items_list):
        if not items_list:
            return "No hay ítems para dropear."
    
        dropped_item = random.choice(items_list)
        
        return dropped_item
    
    def animations(self, string):
        for char in string:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()
    
    def use_item(self, list_items_saved, character):
        # Mostrar inventario
        if len(list_items_saved) <= 0:
            self.animations(EMPTY_INVENTORY)
            #print(EMPTY_INVENTORY)
            return

        print(INVENTARY)
        for i in range(len(list_items_saved)):
            print("item", i + 1, list_items_saved[i].get_name())

        while True:
            try:
                self.animations(SELECT_NUMBER_OF_ITEM)
                item_choice = int(input())
                item_choice = item_choice - 1
                

                if item_choice + 1 == 9: #!ACA ALGO Preguntar
                    break

                selected_item = list_items_saved[item_choice]
                
                if selected_item.get_edible() == "eat":
                    eating.play()
                elif selected_item.get_edible() == "drink":
                    drinking.play()
                else:
                    clothe.play()

                # Aplicar los efectos del item al personaje
                if selected_item.get_type() == "Salud":
                    character.set_health(character.get_health() + selected_item.get_value())
                    print(f"El item que has consumido. {selected_item.get_effect()}")
                    print(f"💊 Salud actual: {character.get_health()}")
                elif selected_item.get_type() == "Fuerza":
                    character.set_strength(character.get_strength() + selected_item.get_value())
                    print(f"El item que has consumido. {selected_item.get_effect()}")
                    print(f"💪 Fuerza actual: {character.get_strength()}")
                elif selected_item.get_type() == "Defensa":
                    character.set_defense(character.get_defense() + selected_item.get_value())
                    print(f"El item que has consumido. {selected_item.get_effect()}")
                    print(f"🛡️ Defensa actual: {character.get_defense()}")
                # Eliminar el item del inventario tras usarlo
                list_items_saved.pop(item_choice)
                break
            except ValueError:
                print("Por favor ingresa un número válido.\n")
    
    def handle_item_drop(self, character, item, list_items, list_items_saved): #Lógica para manejar la recolección del item tras derrotar a un enemigo.
        if len(list_items_saved) > 5:
            print(f"{character.get_name()} no se ha podido añadir al inventario el item.\nDebes usar alguno de tu inventario para poder seguir guardando items!\nTienes un máximo de 6 items.")
            time.sleep(1.5)
        else:
            dropped_item = item.drop_random_item(list_items)
            print(f"{character.get_name()} se te ha añadido al inventario: \n{dropped_item.get_name()}")
            time.sleep(1.5)
            list_items_saved.append(dropped_item)


    

   


    
