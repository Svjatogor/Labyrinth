import time
from Labyrinth import main
import sys
import random
def calc_running_time():
    for i in range(5, 100, 5):
        seed = random.seed(i)
        argv = sys.argv + '--h ' + i + '--w ' + i + '--seed ' + random.randint()
        main(sys.argv)

if __name__ == '__main__':
    calc_running_time()