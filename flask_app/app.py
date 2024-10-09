from flask import Flask, render_template
import json
import random

app = Flask(__name__)

def get_random_pokemon():
    with open('AllPokemons.json', 'r') as file:
        pokemons = json.load(file)
        return random.choice(pokemons)

@app.route('/')
def index():
    random_pokemon = get_random_pokemon()
    return render_template('index.html', pokemon=random_pokemon)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    # app.run(debug=True)
