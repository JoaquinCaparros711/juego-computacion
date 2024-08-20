



class Character:

    def __init__(self, name, health, strength, defense, level = 1):
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__defense = defense
        self.__level = level
    
    def attack(self, other):
        damage = max(self.__strength - other.get_defense()/4, 0)
        other.set_health(round(other.get_health() - damage))
        return damage

    def level_up(self):
        self.__level += 1
        self.__health += 10
        self.__strength += 5
        self.__defense += 3
    
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health
    
    def get_strength(self):
        return self.__strength
    
    def set_strength(self, strength):
        self.__strength = strength

    def get_defense(self):
        return self.__defense
    
    def set_defense(self, defense):
        self.__defense = defense

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level
    
    def __str__(self):
        return f"{self.__name}\nSalud: {self.__health}\nFuerza: {self.__strength}\nDefensa: {self.__defense}\nNivel: {self.__level}\n"

