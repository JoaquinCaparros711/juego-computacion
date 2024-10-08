



class Character:

    def __init__(self, name = "", health = 0, strength = 0, defense = 0, level = 1, super_attack = True):
        self.__name = name
        self.__health = health
        self.__strength = strength
        self.__defense = defense
        self.__level = level
        self.__super_attack = super_attack
    
    def attack(self, other):
        damage = max(self.__strength - other.get_defense() / 2.5, 0)
        new_health = other.get_health() - damage
        if new_health < 0:
            new_health = 0  # Si la salud es negativa, se establece en 0
        other.set_health(round(new_health))
        return damage
    
    def super_attack(self, other):
        damage = max(self.__strength*1.5 - other.get_defense() / 2.5, 0)
        new_health = other.get_health() - damage
        if new_health < 0:
            new_health = 0  # Si la salud es negativa, se establece en 0
        other.set_health(round(new_health))
        return damage

    def level_up(self):
        self.__level += 1
        self.__health += 25
        self.__strength += 15
        self.__defense += 15
        self.__super_attack = True
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

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
        self.__level += level
    
    def get_super_attack(self):
        return self.__super_attack

    def set_super_attack(self, super_attack):
        self.__super_attack = super_attack
    
    def __str__(self):
        return f"{self.__name}:\n❤️ Salud: {self.__health}\n⚔️ Fuerza: {self.__strength}\n🛡️ Defensa: {self.__defense}\nNivel: {self.__level}"

