class Pokemon:
    """
    A class representing a Pokemon with its name, type, and a list of ingredients.
    """

    def __init__(self, url, pokemon_data):
        self.url = url
        self.name = pokemon_data['name']
        self.id = pokemon_data['id']
        self.abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]

    def add_ability(self, ability):
        self.abilities.append(ability)

    def get_abilities(self):
        return self.abilities

    def __str__(self):
        return f"{self.name} ({self.url})"