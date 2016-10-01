import time
from Labyrinth import generate_maze_data
import random
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys

def calc_running_time():
    run_time = {}
    interval = [i for i in range(4, 1000)]
    for i in interval:
        random.seed(time.time())
        seed = random.random()
        start_time = time.time()
        # start generate maze
        generate_maze_data(i, i, seed)
        running_time = time.time() - start_time
        run_time[i] = running_time * 1000
        print(i)
    test = OrderedDict(sorted(run_time.items(), key=lambda x: x[0]))
    x = []
    y = []
    for key, value in test.items():
        x.append(key)
        y.append(value)
    plt.plot(x, y, 'ro')
    plt.show()

if __name__ == '__main__':
    calc_running_time()