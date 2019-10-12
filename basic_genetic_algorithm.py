from math import sqrt
from collections import Counter
import numpy as np
import random

# Artificial Intelligence Work 2
# Developed by Carlos Henrique Ponciano da Silva and Vinicius Luis da Silva

# Genetic algorithm developed using numpy library where values ​​are random for mere fictional tests
# To perform the crossover recombination we are using the Cycle method

# generates the population using the random library sample 
# method where you select a random number without repeating it
def generate_cromossomes(population : int) -> np:
    return np.array([random.sample(range(1, population + 1), population) for line in range(population)])

# generates chromosome costs randomly between zero and one 
# using the uniform method of the random library
def generate_cost(population : int) -> list:
    return [(random.uniform(0, 1), random.uniform(0, 1)) for i in range(population)]

# concatenates the first column to the end of the matrix using 
# the concatenate method of numpy library
def final_column(cromossomes : np) -> np:
    return np.concatenate((cromossomes, np.array(cromossomes[:,[0]])), axis = 1)

# chromosome activation function
# defines the costs of chromosomes in two steps
# first calculates the distance between the individual chromosomes
# and then sum all the results previously obtained generating the activation value
# Active function: square_root(((x2 - x1) ^ 2) + ((y2 - y1) ^ 2))
def fitness_function(cromossomes : np, cost : list = []) -> np:
    return np.array([[ _calculate_fitness(cromossome, cost) ] for cromossome in cromossomes])

def _calculate_fitness(cromossome : np, cost : list) -> int:
    return sum([_calculate_distance(cost[cromossome[x] - 1], cost[cromossome[x + 1] - 1]) for x in range(len(cromossome) - 2)])

def _calculate_distance(current_cost_cromossome : tuple = (0, 0), next_cost_cromossome : tuple = (0, 0)) -> int:    
    return sqrt(((next_cost_cromossome[0] - current_cost_cromossome[0]) ** 2) + ((next_cost_cromossome[1] - current_cost_cromossome[1]) ** 2))

# sort costs from lowest to highest using the numpy library's sort method by 
# returning the values ​​in ascending order plus their index before sorting
def sort_cromossomes(fitness : np) -> np:
    a = np.array(np.sort(fitness, axis=0)) #cost
    b = np.array(np.argsort(fitness, axis=0)) #index
    return np.concatenate([a, b], axis=1)

# return only the first ten elements of the matrix
def get_first_10(matrix):
    return matrix[:10]

# return only the lest ten elements of the matrix
def get_lest_10(old_matrix, current_matrix) -> list:
    _half = int(len(old_matrix) / 2)
    
    for i in range(_half, len(old_matrix)):
        _aux = list()
        
        for j in range(len(old_matrix[i])):
            _aux.append(old_matrix[i][j])

        current_matrix.append(_aux)
    
    return current_matrix

# generates the percentage of choice for each chromosome based on its cost
def _generate_percentages(fitness_matrix_sorted : np) -> np:
    _total = sum([fitness_matrix_sorted[x][0] for x in range(len(fitness_matrix_sorted))])
    return np.array([(fitness_matrix_sorted[i][0] / _total) * 100 for i in range(len(fitness_matrix_sorted) - 1, -1, -1)])

# return the five couples to next-generation generation
# first generates roulette based on percentages of choice
# then spells out ten members of the population to train couples
def pick_couples(fitness_matrix_sorted : np) -> list:
    _percentages = _generate_percentages(fitness_matrix_sorted)
    roulette = list()

    for i in range(len(fitness_matrix_sorted)):
        roulette += [fitness_matrix_sorted[i][1]] * int(_percentages[i] * 10_000)

    _out = list()

    while len(_out) != 10:
        _aux = int(roulette[random.randint(0, len(roulette) - 1)])
        if _aux not in _out:
            _out.append(_aux)
    
    return [(_out[i], _out[i + 1]) for i in range(len(_out)) if i % 2 == 0]

# Recursive method for couples recombination using the Cycle method
# first changes a randomly chosen position.
# if the values ​​are equal the operation ends
# if they are different it will be necessary to make changes until they have no more chromosomes with the same load
def crossover_cycle(dad : np, mom : np)  -> tuple:
    return _crossover_cycle(dad, mom, random.randint(0, len(dad) - 1), [])

def _crossover_cycle(son : np, daughter : np, location : int = 0, son_recombination : list = []) -> tuple:
    son[location], daughter[location] = daughter[location], son[location] 
    
    _equals = None

    while _equals != -1:
        for cromossome in son:
            _equals = _duplicate_value_index(son, cromossome, son_recombination)
            if _equals > -1:
                son_recombination.append(_equals)
                son, daughter = _crossover_cycle(son, daughter, _equals, son_recombination)
                break

    return (np.array(son), np.array(daughter))

# check for duplicate values
def _duplicate_value_index(cromossomes : np, cromossome : int = 0, recombination : list = []) -> int:
    _equals = None
    _position = 0

    while _equals != -1:
        _equals = list(filter(lambda x: cromossomes[x] == cromossome, range(len(cromossomes))))

        if _position < len(_equals):
            _equals = _equals.pop(_position) if len(_equals) > 1 else - 1
            if _equals > -1:
                if _equals not in recombination:
                    return _equals
                else:
                    _position += 1

    return -1

# convert an array to a numpy array
def toNumpy(matrix) -> np:
    return np.array(matrix)

if __name__ == "__main__":
    MAX_ITERATIONS = 10_000
    # MAX_ITERATIONS = 10
    POPULATION = 20
    ITERATIONS = list()

    _cromossomes = generate_cromossomes(POPULATION) #20x20
    _cost_cromossomes = generate_cost(POPULATION) #1x20


    for current_iteration in range(MAX_ITERATIONS):
        print(f'Current iteration: {current_iteration}')
        ITERATIONS.append(_cromossomes)

        _aux_cromossomes = final_column(_cromossomes) #20x21
        fitness_results = fitness_function(_aux_cromossomes, _cost_cromossomes)
        sorted_fitness_results = get_first_10(sort_cromossomes(fitness_results))

        _percentage = pick_couples(sorted_fitness_results)
        
        _children = list()
        for p in _percentage:
            _dad = _cromossomes[p[0]]
            _mom = _cromossomes[p[1]]     

            _crossover = crossover_cycle(_dad, _mom)

            _children.append(list(_crossover[0]))
            _children.append(list(_crossover[1]))

        _cromossomes = toNumpy(get_lest_10(_cromossomes, _children))

    
    print(ITERATIONS[95:])