import argparse
import random

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, default=2, help="width maze")
    parser.add_argument("--h", type=int, default=2, help="height maze")
    parser.add_argument("--seed", type=int, default=0, help="random key")
    args = parser.parse_args()
    w = args.w
    h = args.h
    seed = args.seed
    # 1. generate empty string
    maze_multiplicity = [[0] * w] * h # matrix for multiplicity that describe maze
    cell_border = [[''] * w] * h
    # build labyrinth
    for i in range(h):
        # 2. add unique multiplicity for empty cell
        for j in range(w):
            if maze_multiplicity[i][j] == 0:
                # check the left border
                if j > 0:
                    maze_multiplicity[i][j] = maze_multiplicity[i][j - 1] + 1
                else:
                    maze_multiplicity[i][j] = 1
        # 3. build right border
        for k in range(w - 1):
            # if current cell has same multiplicity as the right cell
            if maze_multiplicity[i][k] == maze_multiplicity[i][k + 1]:
                cell_border[i][k] += 'right'
                continue
            # build the wall or not
            random.seed(seed)
            if random.random() > 0.5:
                # build wall
                cell_border[i][k] += 'right'
            else:
                # not building wall, merge multiplicity
                maze_multiplicity[i][k + 1] = maze_multiplicity[i][k]
        # 4. build down border
        for k in range(w):
            # search cell in this multiplicity
            down_count = 0
            count_cell = 0
            # left search
            q = k - 1
            while q >= 0 and maze_multiplicity[i][k] == maze_multiplicity[i][q]:
                count_cell += 1
                if cell_border[i][q] == 'rightdown' or cell_border[i][q] == 'down':
                    down_count += 1
                q -= 1
            # right search
            q = k + 1
            while q < w and maze_multiplicity[i][k] == maze_multiplicity[i][q]:


if __name__ == "__main__":
    import sys
    main(sys.argv)