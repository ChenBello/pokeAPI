import json
import requests
from pokemon import Pokemon
from manifulateFile import File

# Ask the user if they would like to draw a Pokémon
draw_pokemon = input("Would you like to draw a Pokémon? (y/n) ")
if draw_pokemon.lower() == "y":
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")

    if response.status_code == 200:
        pokemon_list = response.json()["results"]
        pokemons = []

        for pokemon in pokemon_list:
            pokemon_url = pokemon["url"]
            pokemon_details_response = requests.get(pokemon_url)

            if pokemon_details_response.status_code == 200:
                pokemon_data = pokemon_details_response.json()
                pokemons.append(Pokemon(pokemon_url, pokemon_data))

        # Save all Pokémon data to JSON file using the File class
        File.save_pokemon_list([pokemon.to_dict() for pokemon in pokemons], 'Pokemons.json')

        # Save Pokémon data to text file
        save_file_txt = File(''.join(f"{pokemon}\n" for pokemon in pokemons))

        save_file_txt.save_to_file('Pokemons.txt')

        print(save_file_txt.data)
        print("Pokemons saved to .txt file.")

        # Get a random Pokémon and display it
        random_pokemon = File.get_random_pokemon('Pokemons.json')
        print(f"Random Pokémon: {random_pokemon['name']} (ID: {random_pokemon['id']})")

    else:
        print("Failed to retrieve Pokémon list.")

# import json
# import requests
# from pokemon import Pokemon
# from manifulateFile import File
#
# # Ask the user if they would like to draw a Pokémon
# draw_pokemon = input("Would you like to draw a Pokémon? (y/n) ")
# if draw_pokemon.lower() == "y":
#     # If the user wants to draw a Pokémon, make a GET request to the PokeAPI
#     response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
#
#     # If the request is successful, print the Pokémon's details
#     if response.status_code == 200:
#         pokemon_list = response.json()["results"]
#         # json_data = json.dumps(pokemon_list, indent=4)
#         #
#         # save_file_json = File(json_data)
#         # save_file_json.save_to_file('Pokemons.json')
#         # save_file_json.get_random_pokemon('Pokemons.json')
#
#         pokemons = []
#         pokemons_json = []
#         for pokemon in pokemon_list:
#             pokemon_name = pokemon["name"]
#             pokemon_url = pokemon["url"]
#
#             # Another GET request to retrieve Pokémon details
#             print(pokemon_url)
#             pokemon_details_response = requests.get(pokemon_url)
#
#             if pokemon_details_response.status_code == 200:
#                 pokemon_data = pokemon_details_response.json()
#                 pokemons_json.append(pokemon_data)
#                 print(f"Name: {pokemon_data['name']}")
#                 print(f"ID: {pokemon_data['id']}")
#                 print(f"Abilities: {[ability['ability']['name'] for ability in pokemon_data['abilities']]}")
#                 print("----------------------------------------------------------------------------------------------------------------------")
#                 pokemons.append(Pokemon(pokemon_url, pokemon_data))
#
#         # Save all Pokémon data to JSON file using the File class
#         File.save_pokemon_list(pokemons, 'Pokemons.json')
#
#         # Save Pokémon data to text file
#         save_file_txt = File(''.join(f"{pokemon}\n" for pokemon in pokemons))
#
#         for pokemon in save_file_txt.data:
#             save_file_txt.save_to_file('Pokemons.txt')
#
#         print(save_file_txt.data)
#         print("Pokemons saved to .txt file.")
#
#         # Save all Pokémon data to JSON file using the File class
#         File.save_pokemon_list(pokemons, 'Pokemons2.json')
#
#         # Get a random Pokémon and display it
#         random_pokemon = File.get_random_pokemon('Pokemons.json')
#         print(f"Random Pokémon: {random_pokemon['name']} (ID: {random_pokemon['id']})")
#
#     else:
#         print("Failed to retrieve Pokémon list.")
