from classes.character import *
import random, time, pygame, os
from constants import *
from classes.animations import Animations


# Inicialización de animaciones y pygame
animation = Animations()
pygame.init()

# Se definieron los sonidos del juego
eating = pygame.mixer.Sound("sounds/eating.wav")
drinking = pygame.mixer.Sound("sounds/drinking.wav")
clothe = pygame.mixer.Sound("sounds/clothe.wav")


class Item:
    """
    Atributos:
        __name (str): El nombre del ítem.
        __effect (str): El efecto del ítem cuando es usado.
        __type (str): El tipo del ítem (e.g., Salud, Fuerza, Defensa).
        __value (int): El valor numérico del efecto del ítem.
        __edible (str): Indica si el ítem es comestible, bebible o es indumentaria.
    """
    def __init__(self, name = "", effect = "", type = "", value = 0, edible = ""):
        self.__name = name
        self.__effect = effect
        self.__type = type
        self.__value = value
        self.__edible = edible

    def __str__(self):
        return f"{self.__name}:\n{self.__effect}"
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')  

    # Métodos getters para obtener los atributos del ítem
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
    
    # Dropea un ítem al azar
    def drop_random_item(self, items_list):
        if not items_list:
            return "No hay ítems para dropear."
    
        dropped_item = random.choice(items_list)
        
        return dropped_item
    
    # Permite al usuario usar un item y aplciar sus efectos
    def use_item(self, list_items_saved, character):

        # Mostrar inventario
        if len(list_items_saved) <= 0:
            animation.animations(EMPTY_INVENTORY)
            return

        print(INVENTARY)
        for i in range(len(list_items_saved)):
            print(f"item {i + 1}: {list_items_saved[i].get_name()}")  # Mejor formato de impresión

        while True:
            try:
                animation.animations(SELECT_NUMBER_OF_ITEM)
                item_choice = int(input()) - 1  

                if item_choice + 1 == 9:
                    self.clear_console()
                    break

                if 0 <= item_choice < len(list_items_saved):

                    selected_item = list_items_saved[item_choice]
                    
                    if selected_item.get_edible() == "eat":
                        eating.play()
                    elif selected_item.get_edible() == "drink":
                        drinking.play()
                    else:
                        clothe.play()

                    # Aplica los efectos del item al personaje
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
                    # Elimina el item del inventario tras usarlo
                    list_items_saved.pop(item_choice)
                    break
                else:
                    print("¡Error! El número elegido está fuera del rango del inventario.\n")
            except ValueError:
                print("Por favor ingresa un número válido.\n")
    
    # Maneja la lógica para añadir un ítem al inventario del personaje tras derrotar a un enemigo.
    def handle_item_drop(self, character, item, list_items, list_items_saved): #Lógica para manejar la recolección del item tras derrotar a un enemigo.
        if len(list_items_saved) > 5:
            print(f"{character.get_name()} no se ha podido añadir al inventario el item.\nDebes usar alguno de tu inventario para poder seguir guardando items!\nTienes un máximo de 6 items.")
            time.sleep(1.5)
        else:
            dropped_item = item.drop_random_item(list_items)
            print(f"{character.get_name()} se te ha añadido al inventario: \n{dropped_item.get_name()}")
            time.sleep(1.5)
            list_items_saved.append(dropped_item)


    

   


    
