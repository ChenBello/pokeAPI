import json
import random

class File:
    def __init__(self):
        pass

    @staticmethod
    def save_pokemon_list(pokemon_list, filename='Pokemons.json'):
        with open(filename, 'w') as file:
            json.dump(pokemon_list, file, indent=4)

    @staticmethod
    def load_pokemon_list(filename='Pokemons.json'):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'a') as file:
            file.write(data + '\n')

    @staticmethod
    def get_random_pokemon(filename='Pokemons.json'):
        pokemons = File.load_pokemon_list(filename)
        if pokemons:
            random_index = random.randint(0, len(pokemons) - 1)
            return pokemons[random_index]
        return None

