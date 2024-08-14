


class Item:
    def __init__(self, name, effect):
        self.__name = name
        self.__effect = effect

    def __str__(self):
        return f"{self.__name}: {self.__effect}"

    def get_name(self):
        return self.__name

    def get_effect(self):
        return self.__effect
    
    #! Hacer una funcion q sea para dropear items, sabiendo q la clase Item tiene( nombre de item y el efecto que otorga al personaje)