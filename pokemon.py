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

    def __repr__(self):
        return self.name + " is level " + str(self.level) + " and " + self.type + " type! and has " + str(self.health) + " health left."
        # if self.health < (0.5 * self.max_health):
        #     return self.your_pokemon, self.name + " has " + str(self.health) + " health left! You might want to heal"
        # elif self.health == self.max_health:
        #     return self.your_pokemon, self.name + " is max health!"
        # else:
        #     return self.your_pokemon, self.name + " has " + str(self.health) + ". Fight on!!"

    # method for pokemon to take damage
    def take_damage(self, damage_given):
        self.health -= damage_given
        # if pokemon gets knocked out by attack this will fire
        if self.health <= 0:
            # since the hit will most likely be a negative number, reset health to 0 and call knock out method
            self.health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health points left".format(self.name, self.health))

    # method for knocking out pokemon aka when health == 0
    def knock_out(self):
        self.is_knocked_out = True
        # gurantees pokemon is at zero health when knocked out
        if self.health != 0:
            self.health = 0
        print("Pokemon has been knocked out")
    
    # method for pokemon to regain health
    def gain_health(self, health_boost):
        if self.is_knocked_out == True:
            self.revival()
        self.health += health_boost
        # caps health so doesn't go over max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("Pokemon gained " + str(health_boost) + " health points!")

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
        if opponent_pokemon.knock_out():
            print("That pokemon is knocked out, attack a different one!")
        # damage dealt is super effective
        if (self.type == "Fire" and opponent_pokemon.type == "Grass") or (self.type == "Water" and opponent_pokemon.type == "Fire"):
            opponent_pokemon.take_damage(self.level * 2)
            print(self.name + " dealt " + str(self.level * 2) + " damage to " + opponent_pokemon.name)
        # damage dealt is not very effective
        if (self.type == "Grass" and opponent_pokemon.type == "Fire") or (self.type == "Fire" and opponent_pokemon.type == "Water"):
            opponent_pokemon.take_damage(self.level * 0.5)
            print(self.name + " dealt " + str(self.level * 0.5) + " damage to " + opponent_pokemon.name)
        if self.type == opponent_pokemon.type:
            opponent_pokemon.take_damage(self.level * 0.68)
            print(self.name + " dealt " + str(self.level * 0.68) + " damage to " + opponent_pokemon.name)
        

charizard = Pokemon("Charizard", "Fire", 25)
blastoise = Pokemon("Blastoise", "Water", 35)
venosaur = Pokemon("Venosaur", "Grass", 50)



# class to create trainers
class Trainer:
    # constructor method
    def __init__(self, name, pokemon_list, potions=1):
        self.name = name
        self.pokemons = pokemon_list
        self.potions = potions
        self.current_pokemon = 0
    
    def __repr__(self):
        print("The trainer is named {name} and has the following pokemon:".format(name=self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)
    
    # method to heal current pokemon
    def use_potion(self, potions):
        if self.potions > 0:
            self.pokemons[self.current_pokemon].gain_health(15)
            print("Your pokemon was healed by " + 15 + " health points!")
            self.potions -= 1
        else:
            print("You are out of potions. Sorry that's tough :(")
    
    # method to attack other trainer's pokemon
    def attack_opponent_pokemon(self, opponent_trainer):
        opponent_pokemon = opponent_trainer.pokemons[opponent_trainer.current_pokemon]
        self.pokemons[self.current_pokemon].attack(opponent_pokemon)
    
    # method to switch pokemon
    def switch_current_pokemon(self, new_active_pokemon):
        if self.pokemons[new_active_pokemon].is_knocked_out:
            print("{name} is knocked out. Must select another pokemon".format(name=self.pokemons[new_active_pokemon].name))
            self.current_pokemon = new_active_pokemon
        elif new_active_pokemon == self.current_pokemon:
            print("That pokemon is already battling")
        else:
            self.current_pokemon = new_active_pokemon
            print("Go {name}! I know you can do it!".format(name=self.pokemons[self.current_pokemon].name))

Ash = Trainer("Ash", [charizard, venosaur, blastoise], 5)
print(Ash)









