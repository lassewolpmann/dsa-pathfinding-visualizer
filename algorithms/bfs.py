from maze import Maze
from random import randint


class BFS:
    def __init__(self, maze: Maze):
        self.start_position = (0, 0)
        self.end_position = (0, 0)

        while self.start_position == self.end_position:
            self.start_position = (randint(1, maze.width - 1), randint(1, maze.height - 1))
            self.end_position = (randint(1, maze.width - 1), randint(1, maze.height - 1))

        self.graph = maze.graph
        self.visited, self.path = self.find_path()

    def find_path(self):
        queue = [(self.start_position, [self.start_position])]
        # Enqueue the start node and mark it as visited
        visited = {self.start_position}

        while queue:
            # Dequeue a node and its path
            current_node, path = queue.pop(0)
            # If the current node is the end node, return the path
            if current_node == self.end_position:
                return visited, path
            # Explore neighbors of the current node
            for neighbor in self.graph[current_node].neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, path + [neighbor]))
