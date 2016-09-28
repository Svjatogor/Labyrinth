from Labyrinth import main
import sys
import random

def search_out():
    sys.argv.append('--h')
    sys.argv.append(5)
    sys.argv.append('--w')
    sys.argv.append(5)
    sys.argv.append('--seed')
    sys.argv.append(str(random.randint(0, 1000)))
    maze_for_draw = main(sys.argv)
    # generate matrix for search
    matrix_maze = [] * len(maze_for_draw)
    for i in range(len(maze_for_draw)):
        matrix_maze[i] = [] * len(maze_for_draw[i])

    row = 0
    column = 0
    for i in range(len(maze_for_draw)):
        for j in range(len(maze_for_draw[i])):
            matrix_maze[column][row] = 0
            if maze_for_draw[i][j].find('right') != -1:
                matrix_maze[column][row + 1] = 1
                row += 1
            row += 1


