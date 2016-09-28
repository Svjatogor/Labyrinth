import time
from Labyrinth import main
import sys
import random
import copy
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
import math


def calc_running_time():
    sys_argv = copy.copy(sys.argv)
    run_time = {}
    ran = [math.exp(i) for i in range(1, 100)]
    for i in ran:
        sys.argv = copy.copy(sys_argv)
        random.seed(i)
        sys.argv.append('--h')
        sys.argv.append(str(int(i)))
        sys.argv.append('--w')
        sys.argv.append(str(int(i)))
        sys.argv.append('--seed')
        sys.argv.append(str(random.randint(0, 1000)))
        start_time = time.time()
        main(sys.argv)
        running_time = time.time() - start_time
        print(i)
        run_time[i] = running_time * 1000
    test = OrderedDict(sorted(run_time.items(), key=lambda x: x[0]))
    frame = pd.DataFrame(test, index=[0])
    frame.to_csv('test.csv', index=False, sep=';')
    x = []
    y = []
    for key, value in test.items():
        x.append(key)
        y.append(value)
    plt.plot(x, y, 'ro')
    plt.show()
    print(frame)
    print(test)

if __name__ == '__main__':
    calc_running_time()