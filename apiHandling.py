import io
import sys
import random
import requests
# from manifulateFile import File
from poke_modules.file_utils import FileUtils
from pokemon import Pokemon

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def draw_pokemon():
    draw_pokemon_input = input("Would you like to draw a Pokémon? (y/n) ")
    return draw_pokemon_input.lower() in ['y', 'yes']

def fetch_new_pokemon():
    pokemon_list = []
    # Fetch new Pokémon data
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
    if response.status_code == 200:
        pokemon_list = response.json()["results"]
    else:
        print("Failed to retrieve Pokémon list.")
    return pokemon_list

def fetch_pokemon_details(url):
    pokemon_data = None
    # Fetch details of a specific Pokémon
    pokemon_details_response = requests.get(url)
    if pokemon_details_response.status_code == 200:
        pokemon_data = pokemon_details_response.json()
    else:
        print("Failed to retrieve Pokémon details.")
    return pokemon_data

def main():
    to_run = True
    while to_run:
        if draw_pokemon():
            existing_pokemons = FileUtils.load_pokemon_list()
            pokemon_list = fetch_new_pokemon()

            if pokemon_list:
                selected_pokemon = random.choice(pokemon_list)
                selected_url = selected_pokemon["url"]

                existing_pokemon = next((p for p in existing_pokemons if p['name'] == selected_pokemon['name']), None)

                if existing_pokemon:
                    print(f"Found existing Pokémon: {existing_pokemon['name']} (ID: {existing_pokemon['id']})")
                    print(f"Abilities: {existing_pokemon['abilities']}")
                else:
                    pokemon_data = fetch_pokemon_details(selected_url)

                    if pokemon_data:
                        new_pokemon = Pokemon(selected_url, pokemon_data)
                        existing_pokemons.append(new_pokemon.to_dict())
                        FileUtils.save_pokemon_list(existing_pokemons)
                        print(f"New Pokémon added: {new_pokemon.name} (ID: {new_pokemon.id})")
                        print(f"Abilities: {new_pokemon.abilities}")
            else:
                print("No Pokémon available to draw.")
        else:
            print("Goodbye!")
            to_run = False

if __name__ == "__main__":
    main()




# import json
# import random
#
# import requests
#
# from manifulateFile import File
# from pokemon import Pokemon
# import sys
# import io
#
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
#
# # Ask the user if they would like to draw a Pokémon
# while True:
#     draw_pokemon = input("Would you like to draw a Pokémon? (y/n) ")
#     if draw_pokemon.lower() in ['y', 'n']:
#         if draw_pokemon.lower() == "y":
#             # Load existing Pokémon from JSON
#             existing_pokemons = File.load_pokemon_list()
#
#             # Fetch new Pokémon data
#             response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
#             if response.status_code == 200:
#                 pokemon_list = response.json()["results"]
#
#                 # Randomly select a Pokémon
#                 selected_pokemon = random.choice(pokemon_list)
#                 selected_url = selected_pokemon["url"]
#
#                 # Check if Pokémon is already in the existing list
#                 existing_pokemon = next((p for p in existing_pokemons if p['name'] == selected_pokemon['name']), None)
#
#                 if existing_pokemon:
#                     # Pokémon is already in the list
#                     print(f"Found existing Pokémon: {existing_pokemon['name']} (ID: {existing_pokemon['id']})")
#                     print(f"Abilities: {existing_pokemon['abilities']}")
#                 else:
#                     # Pokémon is not in the list; fetch details and add to the list
#                     pokemon_details_response = requests.get(selected_url)
#                     if pokemon_details_response.status_code == 200:
#                         pokemon_data = pokemon_details_response.json()
#                         new_pokemon = Pokemon(selected_url, pokemon_data)
#                         existing_pokemons.append(new_pokemon.to_dict())
#                         # Save updated Pokémon list to JSON
#                         File.save_pokemon_list(existing_pokemons)
#                         print(f"New Pokémon added: {new_pokemon.name} (ID: {new_pokemon.id})")
#                         print(f"Abilities: {new_pokemon.abilities}")
#                     else:
#                         print("Failed to retrieve Pokémon details.")
#             else:
#                 print("Failed to retrieve Pokémon list.")
#         else:
#             print("Goodbye!")
#             break
#     else:
#         print("Please enter 'y' or 'n'.")
#
# # import json
# # import requests
# # from pokemon import Pokemon
# # from manifulateFile import File
# # import sys
# # import io
# # # import codecs
# # # import sys
# #
# # sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
# # # sys.stdin = codecs.getreader('utf-8')(sys.stdin.buffer)
# #
# #
# # # Ask the user if they would like to draw a Pokémon
# # while True:
# #     draw_pokemon = input("Would you like to draw a Pokémon? (y/n) ")
# #     if draw_pokemon.lower() in ['y', 'n']:
# #         if draw_pokemon.lower() == "y":
# #             response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
# #
# #             if response.status_code == 200:
# #                 pokemon_list = response.json()["results"]
# #                 pokemons = []
# #
# #                 for pokemon in pokemon_list:
# #                     pokemon_url = pokemon["url"]
# #                     pokemon_details_response = requests.get(pokemon_url)
# #
# #                     if pokemon_details_response.status_code == 200:
# #                         pokemon_data = pokemon_details_response.json()
# #                         pokemons.append(Pokemon(pokemon_url, pokemon_data))
# #
# #                 # Save all Pokémon data to JSON file using the File class
# #                 File.save_pokemon_list([pokemon.to_dict() for pokemon in pokemons], 'AllPokemons.json')
# #
# #                 # Save Pokémon data to text file
# #                 save_file_txt = File(''.join(f"{pokemon}\n" for pokemon in pokemons))
# #
# #                 save_file_txt.save_to_file('Pokemons.txt')
# #
# #                 print(save_file_txt.data)
# #                 print("Pokemons saved to .txt file.")
# #
# #                 # Get a random Pokémon and display it
# #                 random_pokemon = File.get_random_pokemon('AllPokemons.json')
# #                 print(f"Random Pokémon: {random_pokemon['name']} (ID: {random_pokemon['id']})")
# #                 break
# #             else:
# #                 print("Failed to retrieve Pokémon list.")
# #         else:
# #             print("Goodbye!")
# #     else:
# #         print("Please enter 'y' or 'n'.")
# # # import json
# # # import requests
# # # from pokemon import Pokemon
# # # from manifulateFile import File
# # #
# # # # Ask the user if they would like to draw a Pokémon
# # # draw_pokemon = input("Would you like to draw a Pokémon? (y/n) ")
# # # if draw_pokemon.lower() == "y":
# # #     # If the user wants to draw a Pokémon, make a GET request to the PokeAPI
# # #     response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
# # #
# # #     # If the request is successful, print the Pokémon's details
# # #     if response.status_code == 200:
# # #         pokemon_list = response.json()["results"]
# # #         # json_data = json.dumps(pokemon_list, indent=4)
# # #         #
# # #         # save_file_json = File(json_data)
# # #         # save_file_json.save_to_file('AllPokemons.json')
# # #         # save_file_json.get_random_pokemon('AllPokemons.json')
# # #
# # #         pokemons = []
# # #         pokemons_json = []
# # #         for pokemon in pokemon_list:
# # #             pokemon_name = pokemon["name"]
# # #             pokemon_url = pokemon["url"]
# # #
# # #             # Another GET request to retrieve Pokémon details
# # #             print(pokemon_url)
# # #             pokemon_details_response = requests.get(pokemon_url)
# # #
# # #             if pokemon_details_response.status_code == 200:
# # #                 pokemon_data = pokemon_details_response.json()
# # #                 pokemons_json.append(pokemon_data)
# # #                 print(f"Name: {pokemon_data['name']}")
# # #                 print(f"ID: {pokemon_data['id']}")
# # #                 print(f"Abilities: {[ability['ability']['name'] for ability in pokemon_data['abilities']]}")
# # #                 print("----------------------------------------------------------------------------------------------------------------------")
# # #                 pokemons.append(Pokemon(pokemon_url, pokemon_data))
# # #
# # #         # Save all Pokémon data to JSON file using the File class
# # #         File.save_pokemon_list(pokemons, 'AllPokemons.json')
# # #
# # #         # Save Pokémon data to text file
# # #         save_file_txt = File(''.join(f"{pokemon}\n" for pokemon in pokemons))
# # #
# # #         for pokemon in save_file_txt.data:
# # #             save_file_txt.save_to_file('Pokemons.txt')
# # #
# # #         print(save_file_txt.data)
# # #         print("Pokemons saved to .txt file.")
# # #
# # #         # Save all Pokémon data to JSON file using the File class
# # #         File.save_pokemon_list(pokemons, 'Pokemons2.json')
# # #
# # #         # Get a random Pokémon and display it
# # #         random_pokemon = File.get_random_pokemon('AllPokemons.json')
# # #         print(f"Random Pokémon: {random_pokemon['name']} (ID: {random_pokemon['id']})")
# # #
# # #     else:
# # #         print("Failed to retrieve Pokémon list.")
