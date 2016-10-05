from Labyrinth import Maze
from BuildLabApi import *
import argparse
import sys
import random

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, default=10, help="width maze")
    parser.add_argument("--h", type=int, default=10, help="height maze")
    parser.add_argument("--seed", type=int, default=random.random(), help="random key")
    args = parser.parse_args()
    w = args.w
    h = args.h
    seed = args.seed
    maze = Maze(w, h, seed)
    print("Maze")
    maze_matrix = maze.generate_maze_data(w, h, seed)
    build_maze_from_matrix(maze_matrix)
    print("Optimaze maze")
    ways = maze.way_filter()
    for way in ways:
        print("way {}".format(way['n']))
        build_maze_from_matrix(way['way'])
    print("Evalution maze")
    build_maze_from_matrix(ways[len(ways)-1]['maze'])
if __name__ == "__main__":
    main(sys.argv)

