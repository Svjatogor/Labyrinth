import argparse
import random

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
    random.seed(seed)
    # 1. generate empty string
    # matrix for multiplicity that describe maze
    maze_multiplicity = [0] * h
    # matrix walls
    cell_border = [0] * h
    for i in range(h):
        maze_multiplicity[i] = [0] * w
        cell_border[i] = [''] * w
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
            rand_right = random.randint(0, 100)
            if rand_right > 50:
                # build wall
                cell_border[i][k] += 'right'
            else:
                # not building wall, merge multiplicity
                maze_multiplicity[i][k + 1] = maze_multiplicity[i][k]
        # 4. build down border
        for k in range(w):
            # search cell in this multiplicity
            down_count = 0
            count_cell = 1
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
                count_cell += 1
                if cell_border[i][q] == 'rightdown' or cell_border[i][q] == 'down':
                    down_count += 1
                q += 1
            # if cell is not one or that build wall or not :)
            if count_cell == 1 or count_cell == down_count + 1:
                continue
            rand_down = random.randint(0, 100)
            if rand_down > 50:
                # build wall
                cell_border[i][k] += 'down'
        # 5. building next or last row
        if i != h - 1:
            # build next row
            # copy current row
            maze_multiplicity[i + 1] = maze_multiplicity[i]
            cell_border[i + 1] = cell_border[i]
            # delete right border
            for j in range(w):
                index_s = cell_border[i + 1][j].find('right')
                if index_s != -1:
                    cell_border[i + 1][j] = cell_border[i + 1][j][index_s + len('right'):]
            # delete cell with down wall
            for j in range(w):
                index_s = cell_border[i + 1][j].find('down')
                if index_s != -1:
                    maze_multiplicity[i + 1][j] = 0
                    cell_border[i + 1][j] = ''
        else:
            # build last row
            # build down wall
            for j in range(w):
                if cell_border[i][j].find('down') == -1:
                    cell_border[i][j] += 'down'
                # delete wall between multiplicity
                if j != w - 1 and maze_multiplicity[i][j] != maze_multiplicity[i][j + 1]:
                    index_s = cell_border[i][j].find('right')
                    if index_s != -1:
                        cell_border[i][j] = cell_border[i][j][index_s + len('right'):]
                    # merge multiplicity
                    maze_multiplicity[i][j + 1] = maze_multiplicity[i][j]

if __name__ == "__main__":
    import sys
    main(sys.argv)