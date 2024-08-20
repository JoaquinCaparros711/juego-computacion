import random



class Enemy:

    #!Ver como subirle caracteristicas dependiendo dungeon
    def __init__(self, name):
        self.__name = name
        self.__health = self.__generate_health()
        self.__strength = self.__generate_strength()
        self.__defense = self.__generate_defense()
    
    def attack(self, other):
        damage = max(self.__strength - other.get_defense()/4, 0)
        other.set_health(round(other.get_health() - damage))
        return damage

    def __generate_health(self):
        return random.randint(50, 100)

    def __generate_strength(self):
        return random.randint(10, 20)

    def __generate_defense(self):
        return random.randint(5, 15)

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_strength(self):
        return self.__strength

    def get_defense(self):
        return self.__defense

    def set_health(self, health):
        self.__health = health
    
    def __str__(self):
        return f"{self.__name}\nSalud: {self.__health}\nFuerza: {self.__strength}\nDefensa: {self.__defense}\n"

