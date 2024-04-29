from visualizer import Visualizer
from maze import Maze
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
import csv


if __name__ == "__main__":
    print("How do you want to run the program?: ")
    print("1. Visualizer")
    print("2. Automated running for data collection")
    selection = int(input("Select an option: "))

    if selection == 1:
        Visualizer(0, 0)

    elif selection == 2:
        # Automated running with CSV output
        with open('data.csv', 'w') as file:
            fieldnames = ['maze_size', 'algorithm', 'pathfinding_time', 'visited_nodes', 'path_length']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

        start: int = int(input("Enter starting maze size: "))
        step: int = int(input("Enter step size: "))
        end: int = int(input("Enter ending maze size: "))

        for size in range(start, end + 1, step):
            bfs = BFS()
            dfs = DFS()
            dijs = Dijkstra()
            astar = AStar()

            maze = Maze(size, size)
            print(f"Maze size: {size}x{size}")

            print("BFS...", end="")
            bfs.find_path(maze)
            print("done")

            print("DFS...", end="")
            dfs.find_path(maze)
            print("done")

            print("Dijkstra...", end="")
            dijs.find_path(maze)
            print("done")

            print("A*...", end="")
            astar.find_path(maze)
            print("done")

            with open('data.csv', 'a') as file:
                fieldnames = ['maze_size', 'algorithm', 'pathfinding_time', 'visited_nodes', 'path_length']
                writer = csv.writer(file, delimiter=',')
                writer.writerow([size, 'bfs', bfs.pathfinding_time, bfs.visited_nodes, len(bfs.path)])
                writer.writerow([size, 'dfs', dfs.pathfinding_time, dfs.visited_nodes, len(dfs.path)])
                writer.writerow([size, 'dijkstra', dijs.pathfinding_time, dijs.visited_nodes, len(dijs.path)])
                writer.writerow([size, 'astar', astar.pathfinding_time, astar.visited_nodes, len(astar.path)])
    else:
        print("Please select a valid option")
