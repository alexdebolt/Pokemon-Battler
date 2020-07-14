from pokemonClass import Pokemon


# Creating Pokemon subclasses that inherit from Pokemon

class Cyndaquil(Pokemon):
    def __init__(self, level = 2):
        super().__init__("Cyndaquil", "Fire", "Quazar", level)
        self.level_to_evolve = 8

class Totodile(Pokemon):
    def __init__(self, level = 2):
        super().__init__("Totodile", "Water", "Croconaw", level)
        self.level_to_evolve = 8

