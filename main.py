from classes import *
from functions import *
import argparse

# Arguments handling
argparser = argparse.ArgumentParser(description="Travelling Salesman Problem using Genetic Algorithm")
argparser.add_argument('--cities', '-c', nargs='?', default=20, help='number of cities (default 20)')
argparser.add_argument('--popsize', '-p', nargs='?', default=20, help='population size (default 20)')
argparser.add_argument('--selection', '-s', nargs='?', default="roulette", help='selection type ("random", "roulette")')
argparser.add_argument('--generations', '-g', nargs='?', default=2500, help='number of generations (default 2500)')
argparser.add_argument('--print', '-print', action='store_true', help='print every generation')

args = argparser.parse_args()

def TSP():
    generation = 1
    population = []
    solved = False

    all_cities = create_city_list(MAP_SIZE, int(args.cities))

    distance_history = []

    # Create a population
    for _ in range(int(args.popsize)):
        ind = Individual(all_cities)
        population.append(ind)

    print(f"First generation (distances)")
    for pop in population:
        print(f"{int(1/pop.fitness)} ", end="")
    print()
    
    while not solved:

        if(generation >= int(args.generations)):
            break

        # Sort elements by fitness
        population.sort(key=key_fitness, reverse=True)

        distance_history.append(int(1/population[0].fitness))

        if(args.print):
            print(f"Generation: {generation}")
            for pop in population:
                print(f"{int(1/pop.fitness)} ", end="")
            print()

        next_pop = []

        # Elitism
        elite_size = round((int(args.popsize)*20)/100)
        next_pop.extend(population[:elite_size])

        mating_pool_size = int(args.popsize) - elite_size

        if(args.selection == "roulette"):
            for _ in range(mating_pool_size):
                p1 = roulette_wheel_selection(population)
                p2 = roulette_wheel_selection(population)
                
                new_individual = p1.crossover(p2)

                next_pop.append(new_individual)
        else:
            for _ in range(mating_pool_size):
                p1 = population[:50]
                p2 = population[:50]
                
                new_individual = random.choice(p1).crossover(random.choice(p2))

                next_pop.append(new_individual)
        
        # Mutations
        for pop in next_pop:
            pop.mutate()

        population = next_pop

        generation += 1

    print(f"Last generation (distances)")
    for pop in population:
        print(f"{int(1/pop.fitness)} ", end="")
    print()

    # visualize the best one
    population[0].visualize()
    visualize_distance(distance_history)


def print_population(population):
    for ind in population:
        print(f"FITNESS: {ind.fitness}")
        for city in ind.cities:
            print(city, end="")

        print()

    
def key_fitness(elem):
    return elem.fitness

TSP()