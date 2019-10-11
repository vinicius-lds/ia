from math import sqrt
import numpy as np
import random


def generate_cromossomes(limit : int = 20) -> np:
    return np.array([random.sample(range(1, limit + 1), limit) for line in range(limit)])

def generate_cost(limit : int = 20) -> list:
    return [(random.choice([0, 1]), random.choice([0, 1])) for i in range(limit)]

def final_column(cromossomes : np) -> np:
    return np.concatenate((cromossomes, np.array(cromossomes[:,[0]])), axis = 1)

def fitness_function(cromossomes : np, cost : list = []) -> np:
    return np.array([[ _calculate_fitness(cromossome, cost) ] for cromossome in cromossomes])

def _calculate_fitness(cromossome : np, cost : list) -> int:
    return sum([_calculate_distance(cost[cromossome[x] - 1], cost[cromossome[x + 1] - 1]) for x in range(len(cromossome) - 2)])

def _calculate_distance(current_cost_cromossome : tuple = (0, 0), next_cost_cromossome : tuple = (0, 0)) -> int:    
    return sqrt(((next_cost_cromossome[0] - current_cost_cromossome[0]) ** 2) + ((next_cost_cromossome[1] - current_cost_cromossome[1]) ** 2))

def sort_cromossomes(fitness : np) -> np:
    a = np.array(np.sort(fitness, axis=0)) #cost
    b = np.array(np.argsort(fitness, axis=0)) #index
    
    return np.concatenate([a, b], axis=1)
