import random
from classes.enemy import Enemy
from classes.enemyBoss import EnemyBoss


class Dungeon:

    def __init__(self, level = 1):
        self.__level = level
    
    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def dungeonGenerator(self):#! En base a la dungeon, 1,2, o 3 generar los bichos con sus respectivos puntos

        levelDungeon = self.get_level()
        if levelDungeon == 1:
            nameOfEnemies = ["Conejo", "Hiena", "Chancho", "Pollo", "Piche"]
            nameOfEnemyBoss = "Mono Mandrillus sphinx"
        elif levelDungeon == 2:
            nameOfEnemies = ["Puma", "Toro", "Lobo", "Cocodrilo", "Zorro"]
            nameOfEnemyBoss = "Gorila lomo plateado"
        else:
            nameOfEnemies = ["Tigre de bengala", "Hipopotamo", "León", "Elefante", "Gorila"]
            nameOfEnemyBoss = "Oso Grizzly"

        # Selecciona enemigos únicos sin repeticiones
        selected_enemies = random.sample(nameOfEnemies, 3)

        # Crea la lista de enemigos
        enemies = [Enemy(name, levelDungeon) for name in selected_enemies]
        enemies.append(EnemyBoss(nameOfEnemyBoss, levelDungeon))

        return enemies