from classes.character import Character
from classes.dungeon import Dungeon
from classes.manager import Manager
from classes.item import Item



list_items_saved = []
enemies = []
manager = Manager()
dungeon = Dungeon()
item = Item()
character = Character()
enemies = dungeon.dungeonGenerator()
manager.save_menu(character, enemies, dungeon, item, list_items_saved)


