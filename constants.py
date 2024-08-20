import os
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# def print_menu():
#     clear_console()
#     print(f"{'-'*40}")
#     print(f"{' MENÚ PRINCIPAL ':-^40}")
#     print(f"{'-'*40}")
#     print(f"{'-'*40}")


def nameOfGame():
    print("\n██╗░░░░░░█████╗░░██████╗  ░█████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░░█████╗░░██████╗")
    print("██║░░░░░██╔══██╗██╔════╝  ██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗██╔════╝")
    print("██║░░░░░███████║╚█████╗░  ███████║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝███████║╚█████╗░")
    print("██║░░░░░██╔══██║░╚═══██╗  ██╔══██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══██║░╚═══██╗")
    print("███████╗██║░░██║██████╔╝  ██║░░██║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║██║░░██║██████╔╝")
    print("╚══════╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░\n")
    print("██████╗░███████╗██╗░░░░░  ░░░░░██╗░█████╗░██████╗░░█████╗░██╗░░░░░██╗")
    print("██╔══██╗██╔════╝██║░░░░░  ░░░░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║")
    print("██║░░██║█████╗░░██║░░░░░  ░░░░░██║███████║██████╦╝███████║██║░░░░░██║")
    print("██║░░██║██╔══╝░░██║░░░░░  ██╗░░██║██╔══██║██╔══██╗██╔══██║██║░░░░░██║")
    print("██████╔╝███████╗███████╗  ╚█████╔╝██║░░██║██████╦╝██║░░██║███████╗██║")
    print("╚═════╝░╚══════╝╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝\n")


def welcome():
    print("   ¡Bienvenido a las Aventuras del Jabalí!   ")
    print("\nAntes de comenzar, deberá elegir un tipo de jabalí:")
    time.sleep(1)
    print("(1) - Jabalí Europeo")
    print("(2) - Pecarí tajacu")
    print("(3) - Jabalí de la Isla de Java")


    nameOfCharacter = input("\nIngrese el nombre para su personaje: ")

    while True:
        characterOption = input(f"\nBienvenido {nameOfCharacter}!, ahora elija el Jabalí que desea utilizar (1-3): ")
        if characterOption in ["1", "2", "3"]:
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 1 y 3.")
            time.sleep(2)

    if characterOption == "1":
        print(f"\n{nameOfCharacter}, has elegido el Jabalí Europeo, muy buena opción")
    elif characterOption == "2":
        print(f"\n{nameOfCharacter}, has elegido el Pecarí tajacu, muy buena opción")
    elif characterOption == "3":
        print(f"\n{nameOfCharacter}, has elegido el Jabalí de la Isla de Java, muy buena opción")
    
    time.sleep(3)


STARTINGPOINTS = 250
