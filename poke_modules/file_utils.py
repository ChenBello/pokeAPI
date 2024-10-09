import json
import random
from typing import List, Optional

class FileUtils:
    @staticmethod
    def save_pokemon_list(pokemon_list: List[dict], filename: str = 'Pokemons.json') -> None:
        """
        Save the given list of Pokémon to a JSON file.

        :param pokemon_list: List of Pokémon data to be saved.
        :param filename: Name of the file to save the data in.
        """
        # encoding='utf-8' ensures that the data will be saved in a readable format for non-English characters
        # ensure_ascii=False ensures that the data will be saved as-is and not converted to ASCII code
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(pokemon_list, file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_pokemon_list(filename: str = 'Pokemons.json') -> List[dict]:
        """
        Load the Pokémon list from a specified JSON file.

        :param filename: Name of the file to load the data from.
        :return: List of Pokémon data loaded from the file, or an empty list if the file does not exist.
        """
        # Attempt to load the Pokémon list from the specified JSON file
        try:
            with open(filename, 'r', encoding='utf-8') as file:  # Ensure proper encoding
                return json.load(file)  # Return the loaded JSON data as a Python object
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist

    @staticmethod
    def save_to_file(data: str, filename: str) -> None:
        """
        Append data to a specified file.

        :param data: The data to be appended to the file.
        :param filename: Name of the file to append the data to.
        """
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(data + '\n')
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    @staticmethod
    def get_random_pokemon(filename: str = 'Pokemons.json') -> Optional[dict]:
        """
        Get a random Pokémon from the specified file.

        :param filename: Name of the file to load Pokémon data from.
        :return: A randomly selected Pokémon or None if the list is empty.
        """
        # Load the Pokémon list from the specified file
        pokemons = FileUtils.load_pokemon_list(filename)

        # Use a single return statement to either return a random Pokémon or None
        return pokemons[random.randint(0, len(pokemons) - 1)] if pokemons else None


