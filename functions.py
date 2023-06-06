from classes import *

def create_city_list(map_size, cities_num):
    if(cities_num > map_size**2):
        print("Invalid cities number")
        return None

    actual_cities = 0
    cities = []

    # initialize the cities inside the map
    while actual_cities < cities_num: 
        x = random.randint(0, map_size-1)
        y = random.randint(0, map_size-1)

        its_duplicate = False

        for route in cities:
            if(route.x == x and route.y == y):
                its_duplicate = True

        if(not its_duplicate):
            actual_cities += 1
            cities.append(City(x, y))

    return cities

def roulette_wheel_selection(population):
    total_fitness = 0
    # first calculate total fitness
    for individual in population:
        total_fitness += individual.fitness

    # choose a winning number
    winner = random.uniform(0, total_fitness)

    total_fitness = 0

    # get the winner
    for individual in population:
        total_fitness += individual.fitness

        if(total_fitness >= winner):
            return individual

    return None

def visualize_distance(distance_history):
    df = pd.DataFrame(distance_history, columns =['Best Euclidean distance'])
    fig = px.line(df).update_layout(xaxis_title="Generation", yaxis_title="Euclidean distance")
    fig.show()