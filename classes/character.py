



class Character:

    def __init__(self, name, health, strength, defense, level = 1):
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__defense = defense
        self.__level = level
    
    def __str__(self):
        return f"{self.__name} - Salud: {self.__health}, Fuerza: {self.__strength}, Defensa: {self.__defense}, Nivel: {self.__level}"