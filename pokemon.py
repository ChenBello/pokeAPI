class Pokemon:
    """
    A class representing a Pokemon with its name, ID, abilities, and URL.

    Attributes:
        url (str): The URL of the Pokemon.
        name (str): The name of the Pokemon.
        id (int): The unique identifier for the Pokemon.
        abilities (list): A list of abilities of the Pokemon.
    """

    def __init__(self, url, pokemon_data):
        """
        Initializes the Pokemon object with the given URL and data.

        Args:
            url (str): The URL of the Pokemon.
            pokemon_data (dict): A dictionary containing Pokemon details.
        """
        self.url = url
        self.name = pokemon_data['name']
        self.id = pokemon_data['id']
        self.abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]

    def to_dict(self):
        return {
            'url': self.url,
            'name': self.name,
            'id': self.id,
            'abilities': self.abilities
        }

    def __str__(self):
        """
        Returns a string representation of the Pokemon.

        Returns:
            str: The string representation of the Pokemon.
        """
        abilities_str = ', '.join(self.abilities)
        return f"Pokemon's Name: {self.name}, ID: {self.id}, Abilities: {abilities_str}, URL: {self.url}"
