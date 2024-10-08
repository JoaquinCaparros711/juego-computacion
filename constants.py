




STARTING_POINTS = 400


NAME_OF_GAME = """\n
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

GAME_OVER = """
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""

GAME_INFORMATION = """
¡Bienvenido al desafío definitivo, una aventura épica en un mundo salvaje y lleno de peligros!

Tu misión es atravesar 3 mazmorras, cada una más letal que la anterior. En el corazón de cada mazmorra, te enfrentarás a 3 criaturas feroces, y al final, te aguarda un imponente jefe que pondrá a prueba todas tus habilidades y estrategia.

A medida que derrotes a tus enemigos, obtendrás valiosos ítems que se almacenarán en tu inventario. Úsalos sabiamente cuando más los necesites. La dificultad aumentará a cada paso, con enemigos más inteligentes y jefes cada vez más desafiantes.

Dispondrás de un superataque devastador que solo podrás usar una vez por nivel, regenerándose al subir de rango. ¡Será tu as bajo la manga!

¿Tienes el valor y la astucia suficientes para sobrevivir a estas pruebas y convertirte en el campeón definitivo de las bestias? ¡El destino está en tus manos! ¡Buena suerte, bestia!"""


GAME_MENU = """╔═════════════════════════════════════════════════╗
║¿Que desea hacer?                                ║
║(1) - Empezar a Jugar 🎮                         ║
║(2) - Ver caracteristicas del personaje          ║
║(3) - Ver informacion del juego 📖               ║
║(4) - Guardar progreso 💾                        ║
║(5) - Salir del juego 🔙                         ║
╚═════════════════════════════════════════════════╝
"""

PLAY_MENU = """╔════════════════════════════════════════════════════╗
║¿Que desea hacer?                                   ║
║(1) - Atacar ⚔️                                      ║
║(2) - Ver caracteristicas del personaje             ║
║(3) - Ver caracteristicas del enemigo 👾            ║
║(4) - Ver inventario 🎒                             ║
║(5) - Guardar progreso 💾                           ║
║(6) - Volver hacia atras 🔙                         ║
╚════════════════════════════════════════════════════╝
"""

ANIMAL_MENU = """
╔═════════════════════════════════════════════╗
║(1) - 🐗 Jabalí(+20 de fuerza) 🐗            ║
║(2) - 🦏 Rinoceronte(+20 de defensa) 🦏      ║
║(3) - 🐂 Buey(+30 de salud) 🐂               ║
╚═════════════════════════════════════════════╝
"""

ITEMS_MENU = """
╔═════════════════════════════════════════════╗
║¿Que desea hacer?                            ║
║(1) - Consumir item                          ║
║(2) - Volver hacia atras 🔙                  ║
╚═════════════════════════════════════════════╝
"""

SAVE_MENU = """ 
╔═════════════════════════════════════════════╗
║¿Que desea hacer?                            ║
║(1) - Cargar partida 💾                      ║
║(2) - Nueva partida 🆕                       ║
║(3) - Salir del juego 🔙                     ║
╚═════════════════════════════════════════════╝
"""

WELCOME = """
╔═════════════════════════════════════════════╗
║   ¡Bienvenido a las Aventuras Salvajes!     ║
╚═════════════════════════════════════════════╝"""

ENTRY_NAME = "\nIngrese el nombre para su personaje: "


POINTS = f"""╔══════════════════════════════════════════════════════════════════════════════╗
║Primero que nada, tienes {STARTING_POINTS} puntos para distribuir en vida, fuerza y defensa.║
╚══════════════════════════════════════════════════════════════════════════════╝

              ===> ¡Ojo! Enfocá bien tus puntos para sobrevivir <===          
"""

ENTRY_HEALTH = "Ingrese la cantidad de vida que desea tener(máximo 300pts)❤️: "
ENTRY_STRENGTH = "Ingrese la cantidad de fuerza que desea tener(máximo 150pts)⚔️: "
ENTRY_ANIMAL = "\nAntes de comenzar, deberá elegir un tipo de animal: "
ENTRY_SAVE = "Ingrese su opción: "

EXCEEDED_POINTS = "Te excediste de puntos o ingresaste un valor no válido. Intenta de nuevo.\n"

CREATED_CHARACTER = "\nPersonaje creado con exito!!"

INVALID_OPTION_ANIMAL = "Opción no válida. Por favor, elige un número entre 1 y 3."
INVALID_OPTION_MENU = "Opción no válida. Por favor, elige un número entre 1 y 5."
INVALID_OPTION_MENU2 = "Opción no válida. Por favor, elige un número entre 1 y 6."
INVALID_OPTION_ITEMS_MENU = "Opción no válida. Por favor, elige 1 0 2."
INVALID_OPTION_MENU_SAVE = "Opción no válida. Por favor, elige un número entre 1 y 3."



BEFORE_STATICSTIC = "\nTus estadísticas eran: "
AFTER_STATICSTIC = "Tus estadísticas actuales son: "

INVALID_NUMBER_ERROR = "Error: Debes ingresar un número válido o te exediste."

#! SAVE
LOADED_PROCESS = "\nProgreso cargado exitosamente 💾\n"
FILE_NOT_FOUND = "\nNo se encontró ningún archivo de guardado 💾\n"

#!Game menu
ERROR_LOAD = "No se pudo cargar el juego."
GAME_LOADED_SUCCESSFULLY = "Juego cargado exitosamente. ¡Sigue jugando!"
COULD_NOT_BE_LOADED = "No se pudo cargar el juego 💾"

#! DEF PLAY
CONGRATULATIONS = """"
██╗░░██╗░█████╗░░██████╗  ░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██╗
██║░░██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
███████║███████║╚█████╗░  ██║░░██╗░███████║██╔██╗██║███████║██║░░██║██║░░██║██║░░██║██║
██╔══██║██╔══██║░╚═══██╗  ██║░░╚██╗██╔══██║██║╚████║██╔══██║██║░░██║██║░░██║██║░░██║╚═╝
██║░░██║██║░░██║██████╔╝  ╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝╚█████╔╝╚█████╔╝██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝
"""