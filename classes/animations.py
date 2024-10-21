import time


class Animations:


    #! Anima los prints
    def animations(self, string):
        for char in string:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()