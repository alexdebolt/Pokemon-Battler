from pokemon import Pokemon
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
