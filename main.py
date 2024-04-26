from visualizer import Visualizer
from maze import Maze
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar


if __name__ == "__main__":
    # Visualizer(50, 50)

    # Automated running below
    sizes = [(50, 50), (100, 100), (150, 150), (200, 200), (250, 250), (300, 300), (350, 350),
             (400, 400), (450, 450), (500, 500)]

    for size in sizes:
        maze = Maze(size[0], size[1])
        print(f"Maze size: {size}")
        BFS().find_path_automated(maze)
        DFS().find_path_automated(maze)
        Dijkstra().find_path_automated(maze)
        AStar().find_path_automated(maze)
