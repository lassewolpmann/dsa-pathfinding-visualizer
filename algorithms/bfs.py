import time


class BFS:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

        self.visited = []
        self.path = []

    def find_path(self, maze):
        self.pathfinding_time = 0
        start_time = time.time()

        queue = [(maze.start_position, [maze.start_position])]
        # Enqueue the start node and mark it as visited
        self.visited.append(maze.start_position)

        while queue:
            # Dequeue a node and its path
            current_node, self.path = queue.pop(0)

            # If the current node is the end node, return the path
            if current_node == maze.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(self.visited)

                return
            # Explore neighbors of the current node
            for neighbor in maze.graph[current_node].neighbors:
                if neighbor not in self.visited:
                    self.visited.append(neighbor)

                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, self.path + [neighbor]))
