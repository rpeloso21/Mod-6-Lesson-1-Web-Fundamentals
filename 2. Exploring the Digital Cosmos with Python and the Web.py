import requests



# Task 2
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet["name"]
            mass = planet["mass"]["massValue"]
            orbit_period = planet["sideralOrbit"]
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# fetch_planet_data()

# Task 3
def fetch_all_planet_data():
    planet_list = []

    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            planet_list.append(planet)

    return planet_list
# print(fetch_all_planet_data())

def find_heaviest_planet(planets):
    heaviest_planet = None
    heaviest_planet_weight = 0
    for planet in planets:
        if planet["mass"]["massValue"]*(10**planet["mass"]["massExponent"]) > heaviest_planet_weight:
            heaviest_planet = planet
            heaviest_planet_weight = planet["mass"]["massValue"]*(10**planet["mass"]["massExponent"])

    return (heaviest_planet["name"], heaviest_planet["mass"]["massValue"]*(10**heaviest_planet["mass"]["massExponent"]))

planets = fetch_all_planet_data()
find_heaviest_planet(planets)

name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")