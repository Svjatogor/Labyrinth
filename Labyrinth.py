import random
import time

CELL = 0
WALL = 1

class Maze:
    def __init__(self, w, h, seed):
        self.w = w
        self.h = h
        self.seed = seed
        self.maze = None
        self.maze_visited = []
        self.cells_for_way = []
        self.way = []
        self.ways = []

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
                    matrix_maze[row_in_maze + 1][col_in_maze + 1] = 1
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
                            matrix_maze[row_in_maze][col_in_maze + 1] = 0
                            # merge multiplicity
                            maze_multiplicity[i][j + 1] = maze_multiplicity[i][j]
        # add point in prohibited cell
        for i in range(2, h * 2, 2):
            for j in range(2, w * 2, 2):
                matrix_maze[i][j] = 1
        # add entry
        entry_index = random.randint(0, h - 1) * 2 + 1
        matrix_maze[entry_index][0] = 0
        # add out
        exit_index = random.randint(0, h - 1) * 2 + 1
        matrix_maze[exit_index][len(matrix_maze[0]) - 1] = 0
        self.maze = matrix_maze
        return matrix_maze

    def search_out(self, maze=None, start_cell=None, out_cell=None):
        if maze is None:
            maze = self.maze
        maze_visited = []
        for row in maze:
            maze_visited.append(list(row))
        if start_cell is None:
            # search entry
            index_entry = 0
            while maze_visited[index_entry][0] == 1:
                index_entry += 1
            start_cell = [0, index_entry]
        if out_cell is None:
            # search exit
            index_exit = 0
            while maze_visited[index_exit][len(maze_visited[0]) - 1] == 1:
                index_exit += 1
            out_cell = [index_exit, len(maze[0]) - 1]
        # stack for visited cells
        stack_cells = []
        exit_cell = out_cell
        current_cell = start_cell
        # 1. mark the first cell as visits
        maze_visited[current_cell[0]][current_cell[1]] = 8
        # 2. it has not yet  found a way
        while current_cell != exit_cell:
            # search neighbors
            neighbors = self.get_neighbors(maze_visited, current_cell)
            # 1. if the current cell has unvisited neighbors
            if len(neighbors) != 0:
                # 1. add the cell in stack
                stack_cells.append(current_cell)
                # 2. pick a random cells from neighbors
                random.seed(time.time())
                random_neighbors = random.randint(0, len(neighbors) - 1)
                # 3. make this cell current cell and mark it visited
                current_cell = [neighbors[random_neighbors][0], neighbors[random_neighbors][1]]
                maze_visited[neighbors[random_neighbors][0]][neighbors[random_neighbors][1]] = 8
            # 2. if the stack is not empty
            elif len(stack_cells) != 0:
                # 1. pull cell of the stack
                cell_of_stack = stack_cells.pop()
                # 2. make this cell current
                current_cell = [cell_of_stack[0], cell_of_stack[1]]
            # 3. else there is not escape
            else:
                return None, None
        # add last cell
        stack_cells.append(exit_cell)
        return maze_visited, stack_cells

    def get_way(self, maze, cells):
        way = []
        for row in maze:
            way.append(list(row))
        # draw way
        for cell in cells:
            # add cell in way
            way[cell[0]][cell[1]] = 8
        return way

    def way_filter(self, maze):
        ways = []
        # search first way
        _, cells = self.search_out()
        way = self.get_way(self.maze, cells)
        ways.append({'way': way, 'cells': cells, 'maze': maze})
        for cell in range(0, len(ways[0]['cells'])):
            # generate new way (its current cell and +1)
            new_way = ways[0]['cells'][:cell + 1]
            # search new way of current cell
            _, cells = self.search_out(self.maze, new_way[-1:-2])
            if cells is not None:
                way = self.get_way(self.maze, cells)
                ways.append({'way': way, 'cells': cells})


    def get_neighbors(self, maze_visited, current_cell):
        neighbors = []
        # left neighbors
        if current_cell[1] > 0:
            if maze_visited[current_cell[0]][current_cell[1] - 1] == 0:
                neighbors.append([current_cell[0], current_cell[1] - 1])
        # right
        if current_cell[1] < len(maze_visited[0]) - 1:
            if maze_visited[current_cell[0]][current_cell[1] + 1] == 0:
                neighbors.append([current_cell[0], current_cell[1] + 1])
        # up
        if current_cell[0] > 0:
            if maze_visited[current_cell[0] - 1][current_cell[1]] == 0:
                neighbors.append([current_cell[0] - 1, current_cell[1]])
        # down
        if current_cell[0] < len(maze_visited) - 1:
            if maze_visited[current_cell[0] + 1][current_cell[1]] == 0:
                neighbors.append([current_cell[0] + 1, current_cell[1]])
        return neighbors

    def maze_clone(self):
        maze_copy = [];
        for row in self.maze:
            maze_copy.append(list(row))
        return maze_copy