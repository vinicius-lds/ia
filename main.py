from cromossomes import generate_cromossomes, generate_cost, final_column, fitness_function, sort_cromossomes


MAX_ITERATIONS = 10_000

if __name__ == "__main__":
    _cromossomes = generate_cromossomes() #20x20
    _cost_cromossomes = generate_cost() #1x20
    _aux_cromossomes = final_column(_cromossomes) #20x21

    for current_iteration in range(MAX_ITERATIONS):
        print(f'Current iteration: {current_iteration}')
        fitness_results = fitness_function(_aux_cromossomes, _cost_cromossomes)
        sorted_fitness_results = sort_cromossomes(fitness_results)
