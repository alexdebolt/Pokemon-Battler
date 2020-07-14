from trainerClass import Trainer
from pokemon import *


fire_mouse = Cyndaquil(5)

Jesse = Trainer("Jesse", [fire_mouse], 3)

blue_toad = Totodile(5)

Alex = Trainer("Al", [blue_toad], 3)


print(Alex)
print(Jesse)

Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)

print(blue_toad.experience)