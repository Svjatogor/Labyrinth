import random
import time
import copy as cp

CELL = 0
WALL = 1

class Maze:
    def __init__(self, w, h, seed):
        self.w = w
        self.h = h
        self.seed = seed
        self.maze = None

    def generate_maze_data(self, w, h, seed):
        random.seed(seed)
        # 1. generate empty string
        # matrix for multiplicity that describe maze
        maze_multiplicity = [0]
        maze_multiplicity[0] = [0] * w
        # matrix maze
        matrix_maze = [0] * (h * 2 + 1)
        # add up border
        matrix_maze[0] = [1] * (w * 2 + 1)
        # add down border
        matrix_maze[len(matrix_maze) - 1] = [1] * (w * 2 + 1)
        # add left and right borders
        for i in range(1, len(matrix_maze) - 1):
            matrix_maze[i] = [0] * (w * 2 + 1)
            matrix_maze[i][0] = 1
            matrix_maze[i][len(matrix_maze[i]) - 1] = 1
        # build labyrinth
        for i in range(h):
            # index for maze
            row_in_maze = i * 2 + 1
            # generate unique cell
            multiplicity_to_add = []
            for j in range(1, w + 1):
                if j not in maze_multiplicity[i]:
                    multiplicity_to_add.append(j)
            # 2. add unique multiplicity for empty cell
            for j in range(w):
                if maze_multiplicity[i][j] == 0:
                    # check the left border
                    maze_multiplicity[i][j] = multiplicity_to_add[0]
                    multiplicity_to_add = multiplicity_to_add[1:]
            # 3. build right border
            for k in range(w - 1):
                col_in_maze = k * 2 + 1
                # if current cell has same multiplicity as the right cell
                if maze_multiplicity[i][k] == maze_multiplicity[i][k + 1]:
                    matrix_maze[row_in_maze][col_in_maze + 1] = WALL
                    # add wall in mid
                    matrix_maze[row_in_maze + 1][col_in_maze + 1] = 1
                    continue
                # build the wall or not
                rand_right = random.randint(0, 100)
                if rand_right > 50:
                    # build wall
                    matrix_maze[row_in_maze][col_in_maze + 1] = WALL
                    # add wall in mid
                    matrix_maze[row_in_maze + 1][col_in_maze + 1] = 1
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
                    col_in_maze = q * 2 + 1
                    if matrix_maze[row_in_maze + 1][col_in_maze] == 1:
                        down_count += 1
                    q -= 1
                # right search
                q = k + 1
                while q < w and maze_multiplicity[i][k] == maze_multiplicity[i][q]:
                    count_cell += 1
                    col_in_maze = q * 2 + 1
                    if matrix_maze[row_in_maze + 1][col_in_maze] == 1:
                        down_count += 1
                    q += 1
                # if cell is not one or that build wall or not :)
                if count_cell == 1 or count_cell == down_count + 1:
                    continue
                rand_down = random.randint(0, 100)
                if rand_down > 50:
                    # build wall
                    col_in_maze = k * 2 + 1
                    matrix_maze[row_in_maze + 1][col_in_maze] = 1
                    # add wall in mid
                    matrix_maze[row_in_maze + 1][col_in_maze - 1] = 1
            # 5. building next or last row
            if not i == h - 1:
                # build next row
                # copy current row
                maze_multiplicity.append(maze_multiplicity[i].copy())
                # delete wall with down wall
                for j in range(w):
                    col_in_maze = j * 2 + 1
                    if matrix_maze[row_in_maze + 1][col_in_maze] == WALL:
                        maze_multiplicity[i + 1][j] = 0
            else:
                # build last row
                # build down wall
                for j in range(w):
                    # delete wall between multiplicity
                    if j != w - 1 and maze_multiplicity[i][j] != maze_multiplicity[i][j + 1]:
                        col_in_maze = j * 2 + 1
                        if matrix_maze[row_in_maze][col_in_maze + 1] == 1:
                            matrix_maze[row_in_maze][col_in_maze] = 0
                            # merge multiplicity
                            maze_multiplicity[i][j + 1] = maze_multiplicity[i][j]
        # add right border in last cell
        exit_row = random.randint(0, h - 1)
        exit_index = exit_row * 2 + 1
        matrix_maze[exit_index][len(matrix_maze[0]) - 1] = 0
        return matrix_maze

    def convert_maze_data_to_search(self, cell_border):
        # convert from data for border matrix cells and borders
        maze_matrix = [0] * (len(cell_border) * 2 + 1)
        # init empty maze
        for row in range(0, len(maze_matrix)):
            maze_matrix[row] = [0] * (len(cell_border[0]) * 2 + 1)
        # add walls
        for row in range(0, len(cell_border)):
            row_in_matrix = row * 2 + 1
            # add up and down borders
            if row == 0:
                maze_matrix[row_in_matrix - 1] = [1] * (len(cell_border[row]) * 2 + 1)
            elif row == len(cell_border) - 1:
                maze_matrix[row_in_matrix + 1] = [1] * (len(cell_border[row]) * 2 + 1)
            # add wall in row
            for col in range(0, len(cell_border[row])):
                col_in_matrix = col * 2 + 1
                # add left and right borders
                if col == 0:
                    maze_matrix[row_in_matrix][col_in_matrix - 1] = 1
                    maze_matrix[row_in_matrix - 1][col_in_matrix - 1] = 1
                # add wall in mid
                maze_matrix[row_in_matrix + 1][col_in_matrix + 1] = 1
                # add right wall
                if cell_border[row][col].find('right') != -1:
                    maze_matrix[row_in_matrix][col_in_matrix + 1] = 1
                # add down wall
                if cell_border[row][col].find('down') != -1:
                    maze_matrix[row_in_matrix + 1][col_in_matrix] = 1
        random.seed(time.time())
        # make entry
        entry = random.randint(0, len(maze_matrix) - 1)
        while maze_matrix[entry][1] == 1:
            entry = random.randint(0, len(maze_matrix) - 1)
        maze_matrix[entry][0] = 0
        return maze_matrix

    def search_out(self, maze):
        way = []
        maze_matrix = []
        for row in maze:
            way.append(list(row))
            maze_matrix.append(list(row))
        # search entry
        index_entry = 0
        while maze_matrix[index_entry][0] == 1:
            index_entry += 1
        # search exit
        index_exit = 0
        while maze_matrix[index_exit][len(maze_matrix[0]) - 1] == 1:
            index_exit += 1
        # stack for visited cells
        stack_cells = []
        exit_cell = [index_exit, len(maze_matrix[0]) - 1]
        current_cell = [index_entry, 0]
        # 1. mark the first cell as visits
        maze_matrix[current_cell[0]][current_cell[1]] = 8
        # 2. it has not yet  found a way
        while current_cell != exit_cell:
            # search neighbors
            neighbors = []
            # left neighbors
            if current_cell[1] > 0:
                if maze_matrix[current_cell[0]][current_cell[1] - 1] == 0:
                    neighbors.append([current_cell[0], current_cell[1] - 1])
            # right
            if current_cell[1] < len(maze_matrix[0]) - 1:
                if maze_matrix[current_cell[0]][current_cell[1] + 1] == 0:
                    neighbors.append([current_cell[0], current_cell[1] + 1])
            # up
            if current_cell[0] > 0:
                if maze_matrix[current_cell[0] - 1][current_cell[1]] == 0:
                    neighbors.append([current_cell[0] - 1, current_cell[1]])
            # down
            if current_cell[0] < len(maze_matrix) - 1:
                if maze_matrix[current_cell[0] + 1][current_cell[1]] == 0:
                    neighbors.append([current_cell[0] + 1, current_cell[1]])
            # 1. if the current cell has unvisited neighbors
            if len(neighbors) != 0:
                # 1. add the cell in stack
                stack_cells.append(current_cell)
                # 2. pick a random cells from neighbors
                random.seed(time.time())
                random_neighbors = random.randint(0, len(neighbors) - 1)
                # 3. make this cell current cell and mark it visited
                current_cell = [neighbors[random_neighbors][0], neighbors[random_neighbors][1]]
                maze_matrix[neighbors[random_neighbors][0]][neighbors[random_neighbors][1]] = 8
            # 2. if the stack is not empty
            elif len(stack_cells) != 0:
                # 1. pull cell of the stack
                cell_of_stack = stack_cells.pop()
                # 2. make this cell current
                current_cell = [cell_of_stack[0], cell_of_stack[1]]
            # 3. else there is not escape
            else:
                return None
        # draw way
        for cell in stack_cells:
            # add cell in way
            way[cell[0]][cell[1]] = 8
        return way

    def way_filter(self, maze):
        # search first way
        first_way = self.search_out(maze)
        # search unvisited neighbors
        neighbors = []
        for cell in first_way:
            # left neighbors
            if cell[1] > 0:
                if maze[cell[0]][cell[1] - 1] == 0:
                    neighbors.append([cell[0], cell[1] - 1])
            # right
            if cell[1] < len(maze[0]) - 1:
                if maze[cell[0]][cell[1] + 1] == 0:
                    neighbors.append([cell[0], cell[1] + 1])
            # up
            if cell[0] > 0:
                if maze[cell[0] - 1][cell[1]] == 0:
                    neighbors.append([cell[0] - 1, cell[1]])
            # down
            if cell[0] < len(maze) - 1:
                if maze[cell[0] + 1][cell[1]] == 0:
                    neighbors.append([cell[0] + 1, cell[1]])
