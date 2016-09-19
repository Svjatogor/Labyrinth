import argparse

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, default=2, help="width maze")
    parser.add_argument("--h", type=int, default=2, help="height maze")
    parser.add_argument("--seed", type=int, default=0, help="random key")
    args = parser.parse_args()
    # ADD VALIDATION INPUTS
    if args.h == None or args.w == None:
        print("You must enter the dimensions of the maze")
        return

    w = args.w
    h = args.h
    seed = args.seed
    # generate empry string
    maze_multiplicity = [[0] * w] * h# matrix for multiplicity that describe maze
    cell_border = [[''] * w] * h
    # build labyrinth
    for i in range(h):
        # add unique multiplicity for empty cell
        for j in range(w):
            if maze_multiplicity[i][j] == 0:
                # check the left border
                if j > 0:
                    maze_multiplicity[i][j] = maze_multiplicity[i][j - 1] + 1
                else:
                    maze_multiplicity[i][j] = 1
        # create right border
        for k in range(w):
            # if current cell has same multiplicity as the right cell
            if maze_multiplicity[i][k] == maze_multiplicity[i][k + 1]:
                cell_border[i][k] = 'right'
                continue



if __name__ == "__main__":
    import sys
    main(sys.argv)