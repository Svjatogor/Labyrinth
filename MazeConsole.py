from Labyrinth import Maze
from BuildLabApi import *
import argparse
import sys
import random

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, default=12, help="width maze")
    parser.add_argument("--h", type=int, default=12, help="height maze")
    parser.add_argument("--seed", type=int, default=random.random(), help="random key")
    args = parser.parse_args()
    w = args.w
    h = args.h
    seed = args.seed
    maze = Maze(w, h, seed)
    maze_matrix = maze.generate_maze_data(w, h, seed)
    build_maze_from_matrix(maze_matrix)



if __name__ == "__main__":
    main(sys.argv)

