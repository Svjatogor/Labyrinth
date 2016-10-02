from Labyrinth import *
from BuildLabApi import *
import argparse
import sys

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, default=8, help="width maze")
    parser.add_argument("--h", type=int, default=4, help="height maze")
    parser.add_argument("--seed", type=int, default=random.random(), help="random key")
    args = parser.parse_args()
    w = args.w
    h = args.h
    seed = args.seed
    cell_border = generate_maze_data(w, h, seed)
    maze_matrix = convert_maze_data_to_search(cell_border)
    build_maze_from_matrix(maze_matrix)

if __name__ == "__main__":
    main(sys.argv)

