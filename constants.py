




STARTING_POINTS = 350


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

GAME_INFORMATION = """
Bienvenido al desafío definitivo: ¡una aventura épica en un mundo salvaje!

Tu misión es atravesar 3 mazmorras, cada una más peligrosa que la anterior. En cada mazmorra, deberás enfrentarte a 3 criaturas feroces y finalmente a un poderoso jefe que pondrá a prueba todas tus habilidades.

A lo largo de tu travesía, derrotar a enemigos te otorgará valiosos ítems que podrás usar para fortalecerte en combate. Cada mazmorra aumenta en dificultad, con criaturas más astutas y jefes más temibles a medida que avanzas.

¿Tienes lo necesario para sobrevivir y convertirte en el verdadero campeón de las bestias? ¡MUCHA SUERTE!
"""

GAME_MENU = """
╔═════════════════════════════════════════════════╗
║¿Que desea hacer?                                ║
║(1) - Empezar a Jugar                            ║
║(2) - Ver caracteristicas del personaje          ║
║(3) - Ver informacion del juego                  ║ #!Ver tema de guardado
║(4) - Guardar                                    ║
║(5) - Salir del juego                            ║
╚═════════════════════════════════════════════════╝
"""

PLAY_MENU = """
╔════════════════════════════════════════════════════╗
║¿Que desea hacer?                                   ║
║(1) - Atacar                                        ║
║(2) - Ver caracteristicas del personaje             ║
║(3) - Ver caracteristicas del enemigo               ║
║(4) - Guardar                                       ║
║(5) - Volver hacia atras                            ║
╚════════════════════════════════════════════════════╝
"""

ANIMAL_MENU = """
╔═════════════════════════════════════════════╗
║(1) - Jabalí(+20 de fuerza)                  ║
║(2) - Rinoceronte(+20 de defensa)            ║
║(3) - Buey(+30 de salud)                     ║
╚═════════════════════════════════════════════╝
"""

ITEMS_MENU = """ Has derrotado a un enemigo, tienes la posibilidad de agarrar o dejar un Item:
╔═════════════════════════════════════════════╗
║(1) - Agarrar Item                           ║
║(2) - Dejar Item                             ║
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

ENTRY_HEALTH = "Ingrese la cantidad de vida que desea tener: "
ENTRY_STRENGTH = "Ingrese la cantidad de fuerza que desea tener: "
ENTRY_ANIMAL = "\nAntes de comenzar, deberá elegir un tipo de animal: "

EXCEEDED_POINTS = "Te excediste de puntos o ingresaste un valor no válido. Intenta de nuevo.\n"

CREATED_CHARACTER = "\nPersonaje creado con exito!!"

INVALID_OPTION_ANIMAL = "Opción no válida. Por favor, elige un número entre 1 y 3."
INVALID_OPTION_MENU = "Opción no válida. Por favor, elige un número entre 1 y 5."

BEFORE_STATICSTIC = "\nTus estadísticas eran: "
AFTER_STATICSTIC = "Tus estadísticas actuales son: "
GAME_OVER = "GAME OVER"