from math import sqrt
import random
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px

MUTATION_CHANCE = 1 # percentage
MAP_SIZE = 200

# City representation
class City:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}], "


# Invidividual
class Individual:

    def __init__(self, cities, permutate = True) -> None:
        # initialize the map
        if(permutate):
            rng = np.random.default_rng()
            self.cities = rng.permutation(cities) # list of routes
        else:
            self.cities = cities

        self.fitness = -1
        self.calculate_fitness()
            
    @staticmethod
    def calculate_distance(City1, City2):
        x_diff = abs(City1.x - City2.x)
        y_diff = abs(City1.y - City2.y)

        return round(sqrt((x_diff**2 + y_diff**2)))

    def calculate_fitness(self):
        temp_fitness = 0
        last_city_index = len(self.cities)-1
        for i in range(last_city_index):
            x1 = self.cities[i].x   
            y1 = self.cities[i].y

            x2 = self.cities[i+1].x
            y2 = self.cities[i+1].y

            temp_fitness += Individual.calculate_distance(self.cities[i], self.cities[i+1])

        # Also add the distance between the last city and the first one
        temp_fitness += Individual.calculate_distance(self.cities[last_city_index], self.cities[0])

        self.fitness = 1/temp_fitness
        return self.fitness

    def crossover(self, other):
        route_len = len(self.cities)

        int_s = random.randint(0, route_len - 1)
        int_e = random.randint(int_s, route_len - 1)

        child_ordered = []
        child_remainder = []
        # Copy the range first
        for i in range(int_s, int_e+1):
            child_ordered.append(self.cities[i])

        for city in other.cities:
            if city not in child_ordered:
                child_remainder.append(city)

        # build the child
        child = child_remainder[:int_s] + child_ordered + child_remainder[int_s:]

        return Individual(child, permutate=False)

    def mutate(self):

        for i in range(len(self.cities)):
            random_num = random.randint(1,100)
            if(random_num <= MUTATION_CHANCE):
                # perform swap cities next to each other
                self.cities[i-1], self.cities[i] = self.cities[i], self.cities[i-1]

        # Recalculate fitness
        self.calculate_fitness()

    def visualize(self):
        x = []
        y = []
        for city in self.cities:
            y.append(city.y)
            x.append(city.x)

        # connect last elem to first
        x.append(self.cities[0].x)
        y.append(self.cities[0].y)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=x, y=y,
                            mode='lines+markers',
                            name='lines+markers'))

        fig.show()

