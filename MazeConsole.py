from Labyrinth import main
from BuildLabApi import build_maze


if __name__ == "__main__":
    import sys
    cell_border = main(sys.argv)
    build_maze(cell_border)