from colorama import init, Fore, Back, Style



STARTING_POINTS = 400
init()

NAME_OF_GAME = f"""{Fore.CYAN}\n
    ██╗░░░░░░█████╗░░██████╗  ░█████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░░█████╗░░██████╗
    ██║░░░░░██╔══██╗██╔════╝  ██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔════╝
    ██║░░░░░███████║╚█████╗░  ███████║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝███████║╚█████╗░
    ██║░░░░░██╔══██║░╚═══██╗  ██╔══██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══██║░╚═══██╗
    ███████╗██║░░██║██████╔╝  ██║░░██║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║██║░░██║██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n
    ░██████╗░█████╗░██╗░░░░░██╗░░░██╗░█████╗░░░░░░██╗███████╗░██████╗
    ██╔════╝██╔══██╗██║░░░░░██║░░░██║██╔══██╗░░░░░██║██╔════╝██╔════╝
    ╚█████╗░███████║██║░░░░░╚██╗░██╔╝███████║░░░░░██║█████╗░░╚█████╗░
    ░╚═══██╗██╔══██║██║░░░░░░╚████╔╝░██╔══██║██╗░░██║██╔══╝░░░╚═══██╗
    ██████╔╝██║░░██║███████╗░░╚██╔╝░░██║░░██║╚█████╔╝███████╗██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚═════╝░
    """

GAME_OVER = f"""{Fore.CYAN}
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""

GAME_INFORMATION = """
¡Bienvenido al desafío definitivo, una aventura épica en un mundo salvaje y lleno de peligros!

Tu misión es atravesar 3 mazmorras, cada una más letal que la anterior. En el corazón de cada mazmorra, te enfrentarás a 3 criaturas feroces, y al final, te aguarda un imponente jefe 
que pondrá a prueba todas tus habilidades y estrategias.

A medida que derrotes a tus enemigos, obtendrás valiosos ítems que se almacenarán en tu inventario. Úsalos sabiamente cuando más los necesites. La dificultad aumentará a 
cada paso, con enemigos más inteligentes y jefes cada vez más desafiantes. Pero CUIDADO, Hya ítems defectuosos!

Tienes un inventario de máximo 6 ítems.

Dispondrás de un superataque devastador que solo podrás usar una vez por nivel, regenerándose al subir de rango. ¡Será tu as bajo la manga!

¿Tienes el valor y la astucia suficientes para sobrevivir a estas pruebas y convertirte en el campeón definitivo de las bestias? ¡El destino está en tus manos! ¡Buena suerte, bestia!"""


GAME_MENU = f"""{Fore.BLACK + Back.WHITE}╔═════════════════════════════════════════════════╗
║¿Que desea hacer?                                ║
║(1) - Empezar a Jugar 🎮                         ║
║(2) - Ver caracteristicas del personaje          ║
║(3) - Ver informacion del juego 📖               ║
║(4) - Guardar progreso 💾                        ║
║(5) - Salir del juego 🔙                         ║
╚═════════════════════════════════════════════════╝{Back.RESET}"""

PLAY_MENU = f"""{Fore.BLACK + Back.WHITE}╔════════════════════════════════════════════════════╗
║¿Que desea hacer?                                   ║
║(1) - Atacar ⚔️                                      ║
║(2) - Ver caracteristicas del personaje             ║
║(3) - Ver caracteristicas del enemigo 👾            ║
║(4) - Ver inventario 🎒                             ║
║(5) - Guardar progreso 💾                           ║
║(6) - Volver hacia atras 🔙                         ║
╚════════════════════════════════════════════════════╝
{Back.RESET}"""

ANIMAL_MENU = f"""{Fore.BLACK + Back.WHITE}
╔═════════════════════════════════════════════╗
║(1) - 🐗 Jabalí(+20 de fuerza) 🐗            ║
║(2) - 🦏 Rinoceronte(+20 de defensa) 🦏      ║
║(3) - 🐂 Buey(+30 de salud) 🐂               ║
╚═════════════════════════════════════════════╝
{Back.RESET}"""

ITEMS_MENU = f"""{Fore.BLACK + Back.WHITE}
╔═════════════════════════════════════════════╗
║¿Que desea hacer?                            ║
║(1) - Consumir ítem                          ║
║(2) - Volver hacia atras 🔙                  ║
╚═════════════════════════════════════════════╝
{Back.RESET}"""

SAVE_MENU = f"""{Fore.BLACK + Back.WHITE}
╔═════════════════════════════════════════════╗
║¿Que desea hacer?                            ║
║(1) - Cargar partida 💾                      ║
║(2) - Nueva partida 🆕                       ║
║(3) - Salir del juego 🔙                     ║
╚═════════════════════════════════════════════╝{Back.RESET}"""

WELCOME = f"""{Fore.RED}
╔═════════════════════════════════════════════╗
║   ¡Bienvenido a las Aventuras Salvajes!     ║
╚═════════════════════════════════════════════╝"""

ENTRY_NAME = "\nIngrese el nombre para su personaje: "


POINTS = f"""╔══════════════════════════════════════════════════════════════════════════════╗
║Primero que nada, tienes {STARTING_POINTS} puntos para distribuir en vida, fuerza y defensa.║
╚══════════════════════════════════════════════════════════════════════════════╝

              ===> ¡Ojo! Enfocá bien tus puntos para sobrevivir <===          
"""

ENTRY_HEALTH = f"{Fore.BLUE}Ingrese la cantidad de vida que desea tener(máximo 300pts): "
ENTRY_STRENGTH = f"{Fore.BLUE}Ingrese la cantidad de fuerza que desea tener(máximo 150pts): "
ENTRY_ANIMAL = f"{Fore.BLUE}\nAntes de comenzar, deberá elegir un tipo de animal: "
ENTRY_SAVE = f"{Fore.BLUE}Ingrese su opción: "

EXCEEDED_POINTS = f"{Fore.RED}Te excediste de puntos o ingresaste un valor no válido. Intenta de nuevo.\n"

CREATED_CHARACTER = f"{Fore.BLUE}\nPersonaje creado con exito!!"

INVALID_OPTION_ANIMAL = f"{Fore.RED}Opción no válida. Por favor, elige un número entre 1 y 3."
INVALID_OPTION_MENU = f"{Fore.RED}Opción no válida. Por favor, elige un número entre 1 y 5."
INVALID_OPTION_MENU2 = f"{Fore.RED}Opción no válida. Por favor, elige un número entre 1 y 6."
INVALID_OPTION_ITEMS_MENU = f"{Fore.RED}Opción no válida. Por favor, elige 1 0 2."
INVALID_OPTION_MENU_SAVE = f"{Fore.RED}Opción no válida. Por favor, elige un número entre 1 y 3."



BEFORE_STATICSTIC = f"{Fore.BLUE}\nTus estadísticas eran: "
AFTER_STATICSTIC = f"{Fore.BLUE}Tus estadísticas actuales son: "

INVALID_NUMBER_ERROR = f"{Fore.BLUE}Error: Debes ingresar un número válido o te exediste."

#! SAVE
FILE_NOT_FOUND = f"{Fore.BLUE}\nNo se encontró ningún archivo de guardado 💾\n"

#! LOAD
SELECT_NUMBER_OF_ITEM = f"{Fore.BLUE}Selecciona el número del ítem que deseas usar (Ingresa 9 si no quieres usar ninguno): "
EMPTY_INVENTORY = f"{Fore.BLUE}📭 Tu inventario está vacío."
INVENTARY = f"{Fore.BLUE}🎒 Inventario:"

#!Game menu
ERROR_LOAD = f"{Fore.BLUE}No se pudo cargar el juego."
GAME_LOADED_SUCCESSFULLY = f"{Fore.BLUE}Juego cargado exitosamente. ¡Sigue jugando! 💾"
COULD_NOT_BE_LOADED = f"{Fore.BLUE}No se pudo cargar el juego 💾"

#! DEF PLAY
CONGRATULATIONS = f"""{Fore.CYAN}
██╗░░██╗░█████╗░░██████╗  ░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██╗
██║░░██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
███████║███████║╚█████╗░  ██║░░██╗░███████║██╔██╗██║███████║██║░░██║██║░░██║██║░░██║██║
██╔══██║██╔══██║░╚═══██╗  ██║░░╚██╗██╔══██║██║╚████║██╔══██║██║░░██║██║░░██║██║░░██║╚═╝
██║░░██║██║░░██║██████╔╝  ╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝╚█████╔╝╚█████╔╝██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝
"""