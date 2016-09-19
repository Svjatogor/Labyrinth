WALL_POINT_SIZE = 3
HORIZONTAL_OPENING = "   "
VERTICAL_OPENING = "\n\n"


def build_horizontal_wall(lenght):
    single_wall = "* "
    print(single_wall * lenght, end='')

def build_vertical_wall(lenght):
    single_wall = "*\n"
    print(single_wall * lenght, end='')

def make_opening(horizontal=False):
    if horizontal:
        print(HORIZONTAL_OPENING, end='')
    else:
        print(VERTICAL_OPENING, end='')

build_horizontal_wall(10)
make_opening(horizontal=True)
build_horizontal_wall(10)
build_vertical_wall(7)
make_opening()
build_vertical_wall(11)
