## Program that allows you to create pokemon and trainers and battle pokemon

# class to construct pokemon and battle related methods
class Pokemon:
    #constructor method
    def __init__(self, name, type, level = 2):
        self.name = name
        self.type = type
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.is_knocked_out = False
        self.experience = 0

    def __repr__(self):
        return self.name + " is level " + str(self.level) + ", " + self.type + " type, and has " + str(self.health) + " health left."

    # method for pokemon to take damage
    def take_damage(self, damage_given):
        self.health -= damage_given
        # if pokemon gets knocked out by attack this will fire
        if self.health <= 0:
            # since the hit will most likely be a negative number, reset health to 0 so it can be revived and call knock out method
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health points left".format(name=self.name,health=self.health))

    # method for knocking out pokemon aka when health == 0
    def knock_out(self):
        self.is_knocked_out = True
        # gurantees pokemon is at zero health when knocked out, a little redundant since take_damage resets to 0
        if self.health != 0:
            self.health = 0
        print("{name} has been knocked out".format(name=self.name))

    
    # method for pokemon to regain health
    def gain_health(self, health_boost):
        if self.is_knocked_out == True:
            self.revival()
        self.health += health_boost
        # caps health so doesn't go over max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} was treated with a potion!".format(name=self.name))
        print("{name} now has {health} health!".format(name=self.name, health=self.health))

    # method for reviving pokemon
    def revival(self):
        self.is_knocked_out = False
        # using a potion on a knocked out pokemon will return it to one health
        if self.health == 0:
            self.health = 1
        print("{name} has been revived, go get em!".format(name=self.name))
        

    # method for attacking another pokemon
    def attack(self, opponent_pokemon):
        # if opponent_pokemon is knocked out
        if self.is_knocked_out:
            print("{name} is knocked out. You need to switch pokemon!".format(name=self.name))
        # damage dealt is super effective
        if (self.type == "Fire" and opponent_pokemon.type == "Grass") or (self.type == "Water" and opponent_pokemon.type == "Fire") or (self.type == "Grass" and opponent_pokemon.type == "Water"):
            print(self.name + " dealt " + str(self.level * 2) + " damage to " + opponent_pokemon.name)
            print("It's super effective!")
            opponent_pokemon.take_damage(self.level * 2)
        # damage dealt is not very effective
        if (self.type == "Grass" and opponent_pokemon.type == "Fire") or (self.type == "Fire" and opponent_pokemon.type == "Water") or (self.type == "Water" and opponent_pokemon.type == "Grass"):
            print(self.name + " dealt " + str(self.level * 0.5) + " damage to " + opponent_pokemon.name)
            print("It's not very effective!")
            opponent_pokemon.take_damage(self.level * 0.5)
        if self.type == opponent_pokemon.type:
            print(self.name + " dealt " + str(self.level) + " damage to " + opponent_pokemon.name)
            opponent_pokemon.take_damage(self.level)
    
    def gain_experience(self, opponent_pokemon):
        self.experience += opponent_pokemon.level
        print("{name} has gained {experience} experience points".format(name=self.name, experience=opponent_pokemon.level))
        if self.experience >= 50:
            self.level += 1
            residual_experience = self.experience - 50
            self.experience = residual_experience
            print("{name} has leveled up to level {level}".format(name=self.name, level=self.level))












