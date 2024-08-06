# Tasks 1 and 2

import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text



pikachu_data = json.loads(json_data)

print(pikachu_data["name"])
print(pikachu_data["abilities"])

#Task 3

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    json_data = response.text

    pokemon_data = json.loads(json_data)

    return (pokemon_data["name"], pokemon_data["abilities"], pokemon_data["weight"])

print(fetch_pokemon_data("pikachu"))

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def calculate_average_weight(pokemon_list):
    total_weights = 0
    for name in pokemon_list:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        json_data = response.text
        pokemon_data = json.loads(json_data)
        total_weights += pokemon_data["weight"]

    average_weight = total_weights/len(pokemon_list)
    
    print(f"The average weight of the pokemon listed is '{average_weight}'.")


calculate_average_weight(pokemon_names)
