from maze import Maze
import time


class DFS:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

    def find_path(self, maze: Maze, start_pos: tuple, end_pos: tuple):
        start_time = time.time()

        visited = {start_pos}
        stack = [(start_pos, [start_pos])]

        while stack:
            current_node, path = stack.pop()
                  
            if current_node == end_pos:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(visited)

                return visited, path

            if current_node not in visited:
                visited.add(current_node)

            for neighbor in maze.graph[current_node].neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
