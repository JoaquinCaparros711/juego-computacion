import random


class EnemyBoss:
    
        #!Ver como subirle caracteristicas dependiendo dungeon
    def __init__(self, name, dungeon):
        self.__name = name
        self.__dungeon = dungeon
        self.__health = self.__generate_health()
        self.__strength = self.__generate_strength()
        self.__defense = self.__generate_defense()
    
    def attack(self, other):
        damage = max(self.__strength - other.get_defense() / 4, 0)
        new_health = other.get_health() - damage
        if new_health < 0:
            new_health = 0  # Si la salud es negativa, se establece en 0
        other.set_health(round(new_health))
        return damage

    def __generate_health(self):
        if self.__dungeon == 2 or self.__dungeon == 3:
            return round(random.uniform(145 * (self.get_dungeon() - 0.6), 200 * (self.get_dungeon() - 0.6)))
        else:
            return random.randint(145 , 200)

    def __generate_strength(self):
        if self.__dungeon == 2 or self.__dungeon == 3:
            return round(random.uniform(35 * (self.get_dungeon() - 0.6), 45 * (self.get_dungeon() - 0.6)))
        else:
            return random.randint(35 , 45)

    def __generate_defense(self):
        if self.__dungeon == 2 or self.__dungeon == 3:
            return round(random.uniform(25 * (self.get_dungeon() - 0.6), 35 * (self.get_dungeon() - 0.6)))
        else:
            return random.randint(25, 35)

    def get_name(self):
        return self.__name
    
    def get_dungeon(self):
        return self.__dungeon

    def set_dungeon(self, dungeon):
        self.__dungeon = dungeon

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