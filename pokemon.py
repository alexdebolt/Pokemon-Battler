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
        print("{name} gained {health} health points!".format(name=self.name, health=health_boost))
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
        


# class to create trainers
class Trainer:
    # constructor method
    def __init__(self, name, pokemon_list, potions=1):
        self.name = name
        self.pokemons = pokemon_list
        self.potions = potions
        self.current_pokemon = 0
    
    def __repr__(self):
        print("\nThe trainer is named {name} and has the following pokemon: \n".format(name=self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        print("\n--------------------------------------------------------------------")
        return "The current pokemon is {name} \n--------------------------------------------------------------------".format(name = self.pokemons[self.current_pokemon].name)
    
    # method to heal current pokemon
    def use_potion(self, potions):
        if self.potions > 0:
            self.pokemons[self.current_pokemon].gain_health(15)
            self.potions -= 1
            print("You have {potions} potions left.".format(potions=self.potions))
        else:
            print("You are out of potions. Sorry that's tough :(")
    
    # method to attack other trainer's pokemon
    def attack_opponent_pokemon(self, opponent_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        opponent_pokemon = opponent_trainer.pokemons[opponent_trainer.current_pokemon]
        my_pokemon.attack(opponent_pokemon)
    
    # method to switch pokemon
    def switch_current_pokemon(self, new_active_pokemon):
        if new_active_pokemon < len(self.pokemons) and new_active_pokemon >= 0:
            if self.pokemons[new_active_pokemon].is_knocked_out:
                print("{name} is knocked out. Must select another pokemon".format(name=self.pokemons[new_active_pokemon].name))
            elif new_active_pokemon == self.current_pokemon:
                print("That pokemon is already battling")
            else:
                self.current_pokemon = new_active_pokemon
                print("Go {name}! I know you can do it!".format(name=self.pokemons[self.current_pokemon].name))
        else:
            print("That is not an available Pokemon, you need to select a pokemon that your trainer has.")


charizard = Pokemon("Charizard", "Fire", 25)
blastoise = Pokemon("Blastoise", "Water", 35)
venosaur = Pokemon("Venosaur", "Grass", 50)
ninetails = Pokemon("Ninetails", "Fire", 28)
poliwhirl = Pokemon("Poliwhirl", "Water", 32)

Ash = Trainer("Ash", [blastoise, venosaur], 5)
Gary = Trainer("Gary", [ninetails, poliwhirl], 4)


print(Ash)
print(Gary)
Ash.attack_opponent_pokemon(Gary)
Ash.attack_opponent_pokemon(Gary)
Gary.switch_current_pokemon(1)
Gary.switch_current_pokemon(0)


