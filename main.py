from classes.character import Character
from classes.enemy import Enemy


character1 = Character('The Goat', 120, 40, 35)
enemy1 = Enemy('Escarabajo')

print(character1)
print(enemy1)

enemy1.attack(character1)
character1.attack(enemy1)

print(character1)
print(enemy1)

