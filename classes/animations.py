import time


class Animations:


    #! Funcion para animar prints
    def animations(self, string):
        for char in string:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()