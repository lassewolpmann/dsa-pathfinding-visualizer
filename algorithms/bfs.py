from maze import Maze


class BFS:
    def __init__(self, maze: Maze):
        self.maze = maze
        try:
            self.visited, self.path = self.find_path()
        except TypeError:
            self.visited = None
            self.path = None

    def find_path(self):
        # Queue for BFS
        queue = [(self.maze.start_position, [self.maze.start_position])]
        # Enqueue the start node and mark it as visited
        visited = {self.maze.start_position}

        while queue:
            # Dequeue a node and its path
            current_node, path = queue.pop(0)
            # If the current node is the end node, return the path
            if current_node == self.maze.end_position:
                return visited, path
            # Explore neighbors of the current node
            for neighbor in self.maze.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, path + [neighbor]))
