import time
from Labyrinth import Maze
import random
from collections import OrderedDict
import matplotlib.pyplot as plt
import math

def calc_running_time():
    run_time = {}
    maze = Maze(4, 4, 4)
    interval = [i for i in range(4, 1000)]
    for i in interval:
        random.seed(time.time())
        seed = random.random()
        start_time = time.time()
        # start generate maze
        maze.generate_maze_data(i, i, seed)
        maze.way_filter()
        running_time = time.time() - start_time
        run_time[i] = running_time
        print(i)
    test = OrderedDict(sorted(run_time.items(), key=lambda x: x[0]))
    x = []
    y = []
    for key, value in test.items():
        x.append(key)
        y.append(value)
    plt.plot(x, y, 'ro')
    # sqr_x = [math.sqrt(i) for i in y]
    # plt.plot(sqr_x, y, 'go')
    plt.show()

if __name__ == '__main__':
    calc_running_time()
