from Labyrinth import Maze
from BuildLabApi import *


maze = Maze(4, 4, 4)
maze.maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 1, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1]]
build_maze_from_matrix(maze.maze)
ways = maze.way_filter()
for way in ways:
    print("way {}".format(way['n']))
    build_maze_from_matrix(way['way'])
print("Evalution maze")
build_maze_from_matrix(ways[len(ways)-1]['maze'])

