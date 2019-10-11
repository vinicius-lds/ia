from random import randint


def generate_cities():
    cities = []
    for x in range(20):
        cities.append((randint(0, 100), randint(0, 100)))
    return cities
