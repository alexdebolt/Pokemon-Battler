from pokemonClass import Pokemon


# Creating Pokemon subclasses that inherit from Pokemon

class Cyndaquil(Pokemon):
    def __init__(self, level = 2):
        super().__init__("Cyndaquil", "Fire", level)


class Totodile(Pokemon):
    def __init__(self, level = 2):
        super().__init__("Totodile", "Water", level)