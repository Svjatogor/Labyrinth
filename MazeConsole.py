from Labyrinth import Maze
from BuildLabApi import *
import argparse
import sys


def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, default=4, help="width maze")
    parser.add_argument("--h", type=int, default=4, help="height maze")
    parser.add_argument("--seed", type=int, default=2, help="random key")
    args = parser.parse_args()
    w = args.w
    h = args.h
    seed = args.seed
    maze = Maze(w, h, seed)
    print("Maze")
    maze_matrix = maze.generate_maze_data(w, h, seed)
    build_maze_from_matrix(maze_matrix)
    print("Optimize maze")
    ways = maze.way_filter()
    for way in ways:
        print("way {}".format(way['n']))
        build_maze_from_matrix(way['way'])
    print("Evolution maze")
    build_maze_from_matrix(ways[len(ways)-1]['maze'])
if __name__ == "__main__":
    main(sys.argv)

