from cities import generate_cities
from cromossomes import start_cromossomes, fitness_function, sort_cromossomes


max_iterations = 10_000
current_iteration = 0

cities = generate_cities()
cromossomes = start_cromossomes(population=20, cities=cities)

while current_iteration < max_iterations:
    print(f'Current iteration: {current_iteration}')
    fitness_matrix = fitness_function(cromossomes, cities)
    cromosomes = sort_cromossomes(cromossomes, fitness_matrix)
    
    current_iteration += 1

    
print(cities)

for cromossome in cromossomes:
    print(cromossome)

