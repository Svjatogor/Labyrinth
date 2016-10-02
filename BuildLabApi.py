HORIZONTAL_OPENING = " " * 4
SPASE_FOR_CELL = " " * 3
HORIZONTAL_WALL = " * *"

def build_horizontal_wall(lenght):
    single_wall = "* * "
    print(single_wall * lenght, end='')
    print('*', end='')

def build_row(row, starting_row = False):
    print() # new row
    # first symbolic row
    # print left border
    if starting_row:
        print(' ', end='')
    else:
        print('*', end='')
    for i in row:
        print(SPASE_FOR_CELL, end='') # print cell
        if i.find('right') != -1:
            # draw wall point
            print('*', end='')
        else:
            print(' ', end='')
    # second symbolic row (down wall)
    print('\n*', end='')
    for i in row:
        if i.find('down') != -1:
            print(HORIZONTAL_WALL, end='')
        elif i.find('right') != -1:
            print(SPASE_FOR_CELL + '*', end='')
        else:
            print(HORIZONTAL_OPENING, end='')

def build_maze(maze_plan):
    build_horizontal_wall(len(maze_plan[0]))
    for plan_row in maze_plan:
        if plan_row == maze_plan[0]:
            build_row(plan_row, starting_row=True)
        else:
            build_row(plan_row)
    print()

def build_maze_from_matrix(maze_matrix):
    for row in maze_matrix:
        for element in row:
            if element == 1:
                print('# ', end='')
            elif element == 0:
                print('  ', end='')
            elif element == 8:
                print('*', end='')
        print()