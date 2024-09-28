import json
import random

class File:
    def __init__(self, data):
        self.data = data

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(self.data + '\n')

    # def get_random_pokemon(self, filename):
    #     with open(filename, 'r') as file:
    #         data = json.load(file)
    #         random_pokemon = random.choice(data['results'])
    #         return print("The random pokemon you chose: ", Pokemon(random_pokemon['url'], random_pokemon['name']))

    @staticmethod
    def save_pokemon_list(pokemon_list, filename='Pokemons.json'):
        with open(filename, 'w') as file:
            json.dump(pokemon_list, file, indent=4)

    @staticmethod
    def get_random_pokemon(filename='Pokemons.json'):
        with open(filename, 'r') as file:
            pokemon_list = json.load(file)
        return random.choice(pokemon_list)