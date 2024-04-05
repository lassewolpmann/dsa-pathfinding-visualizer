from maze import Maze
from random import randint
import time


class BFS:
    def __init__(self, maze: Maze):
        self.start_position = (0, 0)
        self.end_position = (0, 0)
        self.maze = maze

        self.graph = maze.graph
        self.pathfinding_time = 0
        self.visited = {}

    def find_path(self):
        start_time = time.time()

        self.start_position = (0, 0)
        self.end_position = (0, 0)

        while self.start_position == self.end_position:
            self.start_position = (randint(1, self.maze.width - 1), randint(1, self.maze.height - 1))
            self.end_position = (randint(1, self.maze.width - 1), randint(1, self.maze.height - 1))

        queue = [(self.start_position, [self.start_position])]
        # Enqueue the start node and mark it as visited
        visited = {self.start_position}

        while queue:
            # Dequeue a node and its path
            current_node, path = queue.pop(0)
            # If the current node is the end node, return the path
            if current_node == self.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)

                return visited, path
            # Explore neighbors of the current node
            for neighbor in self.graph[current_node].neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, path + [neighbor]))
