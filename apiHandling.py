import requests
from pokemon import Pokemon
from manifulateFile import  File

from pokemon import Pokemon
# Ask the user if they would like to draw a Pokémon
draw_pokemon = input("Would you like to draw a Pokémon? (y/n) ")
if draw_pokemon.lower() == "y":
    # If the user wants to draw a Pokémon, make a GET request to the PokeAPI
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")

    # If the request is successful, print the Pokémon's details
    if response.status_code == 200:
        pokemon_list = response.json()["results"]
        pokemons = []

        for pokemon in pokemon_list:
            pokemon_name = pokemon["name"]
            pokemon_url = pokemon["url"]

            # Another GET request to retrieve Pokémon details
            print(pokemon_url)
            pokemon_details_response = requests.get(pokemon_url)

            if pokemon_details_response.status_code == 200:
                pokemon_data = pokemon_details_response.json()
                print(f"Name: {pokemon_data['name']}")
                print(f"ID: {pokemon_data['id']}")
                print(f"Abilities: {[ability['ability']['name'] for ability in pokemon_data['abilities']]}")
                print(Pokemon(pokemon_url, pokemon_data))
                print("----------------------------------------------------------------------------------------------------------------------")
                pokemons.append(Pokemon(pokemon_url, pokemon_data))
        # save_file = File([str(pokemon)+'\n' for pokemon in pokemons])
        save_file = File(''.join(f"{pokemon}\n" for pokemon in pokemons))

        for pokemon in save_file.data:
            save_file.save_to_file('Pokemons.txt')

        print(save_file.data)

        # print(f"Pokemons: {(pokemon.name+',' for pokemon in pokemons)}")
    else:
        print("Failed to retrieve Pokémon list.")

