from random import sample
from math import sqrt
from collections import OrderedDict
from math import inf


def start_cromossomes(population : int = 20, cities : list = []) -> list:
    cromossomes = []
    for x in range(population):
        cromossome = sample(range(len(cities)), len(cities))
        cromossome.append(cromossome[0])
        cromossomes.append(cromossome)
    return cromossomes

def fitness_function(cromossomes : list = [], cities : list = []) -> list:
    _fitness_matrix = []
    for cromossome in cromossomes:
        _fitness_matrix.append([_calculate_fitness(cromossome, cities)])
    return _fitness_matrix
        
def _calculate_fitness(cromossome : list = [], cities : list = []) -> int:
    total = 0
    for x in range(len(cromossome) - 2):
        current_city = cities[cromossome[x]]
        next_city = cities[cromossome[x + 1]]

        total += _calculate_distance(current_city, next_city)

    return total

def _calculate_distance(city_one : tuple = (0, 0), city_two : tuple = (0, 0)) -> int:
    
    xi = city_one[0]
    yi = city_one[1]
    
    xj = city_two[0]
    yj = city_two[1]
    
    return sqrt(((xj - xi) ** 2) + ((yj - yi) ** 2))
        
def sort_cromossomes(cromossomes : list = [], fitness_matrix : list = []) -> list:
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(cromossomes) - 1):
            if fitness_matrix[i][0] > fitness_matrix[i + 1][0]:
                fitness_matrix[i][0], fitness_matrix[i + 1][0] = fitness_matrix[i + 1][0], fitness_matrix[i][0]
                cromossomes[i], cromossomes[i + 1] = cromossomes[i + 1], cromossomes[i]
                ordered = False
    return cromossomes
