from visualizer import Visualizer
from maze import Maze
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
import csv


if __name__ == "__main__":
    # Visualizer(50, 50)

    # Automated running below
    sizes = [(50, 50), (100, 100), (150, 150), (200, 200), (250, 250), (300, 300), (350, 350),
             (400, 400), (450, 450), (500, 500)]

    with open('data.csv', 'w') as file:
        fieldnames = ['maze_width', 'maze_height', 'algorithm', 'pathfinding_time', 'visited_nodes', 'path_length']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

    for size in sizes:
        bfs = BFS()
        dfs = DFS()
        dijs = Dijkstra()
        astar = AStar()

        maze = Maze(size[0], size[1])
        print(f"Maze size: {size}")
        bfs.find_path_automated(maze)
        dfs.find_path_automated(maze)
        dijs.find_path_automated(maze)
        astar.find_path_automated(maze)

        with open('data.csv', 'a') as file:
            fieldnames = ['maze_size', 'algorithm', 'pathfinding_time', 'visited_nodes', 'path_length']
            writer = csv.writer(file, delimiter=',')
            writer.writerow([size[0], size[1], 'bfs', bfs.pathfinding_time, bfs.visited_nodes, len(bfs.path)])
            writer.writerow([size[0], size[1], 'dfs', dfs.pathfinding_time, dfs.visited_nodes, len(dfs.path)])
            writer.writerow([size[0], size[1], 'dijkstra', dijs.pathfinding_time, dijs.visited_nodes, len(dijs.path)])
            writer.writerow([size[0], size[1], 'astar', astar.pathfinding_time, astar.visited_nodes, len(astar.path)])
