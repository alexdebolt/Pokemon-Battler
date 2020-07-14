from trainerClass import Trainer
from pokemon import *


fire_mouse = Cyndaquil(14)
shitsandwich = Cyndaquil(14)
sucxk = Cyndaquil(14)
bad = Cyndaquil(14)
nogood = Cyndaquil(14)


Jesse = Trainer("Jesse", [fire_mouse, shitsandwich, sucxk, bad], 3)

blue_toad = Totodile(7)

Alex = Trainer("Al", [blue_toad], 3)

Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Jesse.switch_current_pokemon(1)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
Alex.attack_opponent_pokemon(Jesse)
print(blue_toad.level)



