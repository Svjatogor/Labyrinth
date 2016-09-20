WALL_POINT_SIZE = 3
HORIZONTAL_OPENING = " " * 4
VERTICAL_OPENING = "\n\n"
SPASE_FOR_CELL = " " * 3
HORIZONTAL_WALL = " * *"


def build_horizontal_wall(lenght):
    single_wall = "* "
    print(single_wall * lenght, end='')

def build_vertical_wall(lenght):
    single_wall = "*\n"
    print(single_wall * lenght, end='')
    build_horizontal_wall(2)

def make_cell(horizontal=False):
    if horizontal:
        print(HORIZONTAL_OPENING, end='')
    else:
        print(VERTICAL_OPENING, end='')

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

def build_maze






build_horizontal_wall(8)
build_row(['rightdown', 'rightdown', 'rightdown'], starting_row=True)
build_row(['rightdown', 'right', 'rightdown'])
