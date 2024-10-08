from classes.character import *
import random


class Item:
    def __init__(self, name = "", effect = "", type = "", value = 0):
        self.__name = name
        self.__effect = effect
        self.__type = type
        self.__value = value

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
    
    # Función para dropear un ítem al azar
    def drop_random_item(self, items_list):
        if not items_list:
            return "No hay ítems para dropear."
    
        dropped_item = random.choice(items_list)
        
        return dropped_item


    

   


    
