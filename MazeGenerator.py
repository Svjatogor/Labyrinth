import random
import time

CELL = 0
WALL = 1


def generate_maze(w, h, seed):
    # matrix include maze
    maze_matrix = []