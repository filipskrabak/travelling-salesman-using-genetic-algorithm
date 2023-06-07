# Travelling Salesman problem using Genetic Algorithm
## Description
University assignment for artificial intelligence course. Since TS is a NP-complete problem, I attempted to get a satisfactory solution in real time. May not always find the optimal solution.
After running the program, two browser tabs will open showing cities visualization and a graph displaying development of distances between cities during each generation.

## Usage
Run this program with ```python main.py```

Use the ```python main.py -h``` command to show command line arguments

```
usage: main.py [-h] [--cities [CITIES]] [--popsize [POPSIZE]] [--selection [SELECTION]] [--generations [GENERATIONS]] [--print]

Travelling Salesman Problem using Genetic Algorithm

options:
  -h, --help            show this help message and exit
  --cities [CITIES], -c [CITIES]
                        number of cities (default 20)
  --popsize [POPSIZE], -p [POPSIZE]
                        population size (default 20)
  --selection [SELECTION], -s [SELECTION]
                        selection type ("random", "roulette")
  --generations [GENERATIONS], -g [GENERATIONS]
                        number of generations (default 2500)
  --print, -print       print every generation
```

## Dependencies
```Python 3.10, plotly, numpy, pandas```

## Visualization

![Cities](https://i.gyazo.com/b1717bd5e015f57d452669479a8e82ba.png)
![Distances](https://i.gyazo.com/f2cae18b3f6f23a69cc7bc05eeefc7ec.png)
