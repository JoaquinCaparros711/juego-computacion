


class Item:
    def __init__(self, name, effect):
        self.__name = name
        self.__effect = effect

    def __str__(self):
        return f"{self.__name}: {self.__effect}"

    def get_name(self):
        return self.__name

    def get_effect(self):
        return self.__effect
    
def addItem():
    Hamburguesa = Item("Hamburguesa", "Restaura 20 puntos de vida")
    PapasFritas = Item("Papas Fritas", "Restaura 10 puntos de vida")
    Chocolate = Item("Chocolate", "Restaura 5 puntos de vida")
    Cocacola = Item("Coca-Cola", "Aumenta la Fuerza en 5 puntos")
    ZapatillasNike = Item("Zapatillas Nike", "Aumenta la Fuerza en 5 puntos")
    CadenadeOro = Item("Cadena de Oro", "Aumenta la Fuerza en 10 puntos")
    DisfrazdeBatman = Item("Disfraz de Batman", "Aumenta la defensa en 15 puntos")
    Chalecodekevlar = Item("Chaleco de kevlar", "Aumenta la defensa en 20 puntos")
    CamperaGucci = Item("Campera Gucci", "Aumenta la defensa en 10 puntos")




    
