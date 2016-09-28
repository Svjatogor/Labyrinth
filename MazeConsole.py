from Labyrinth import generate_maze_data
from BuildLabApi import build_maze
import argparse
import sys

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, default=8, help="width maze")
    parser.add_argument("--h", type=int, default=4, help="height maze")
    parser.add_argument("--seed", type=int, default=1, help="random key")
    args = parser.parse_args()
    w = args.w
    h = args.h
    seed = args.seed
    cell_border = generate_maze_data(w, h, seed)
    build_maze(cell_border)

if __name__ == "__main__":
    main(sys.argv)

