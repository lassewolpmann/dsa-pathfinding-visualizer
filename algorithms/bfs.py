import time


class BFS:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0
        self.path = []

    def find_path(self, visualizer):
        self.pathfinding_time = 0
        start_time = time.time()

        queue = [(visualizer.maze.start_position, [visualizer.maze.start_position])]
        # Enqueue the start node and mark it as visited
        visited = {visualizer.maze.start_position}

        while queue:
            # Dequeue a node and its path
            current_node, self.path = queue.pop(0)

            # If the current node is the end node, return the path
            if current_node == visualizer.maze.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(visited)

                return
            # Explore neighbors of the current node
            for neighbor in visualizer.maze.graph[current_node].neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)

                    # Draw rect for neighbor
                    x, y = neighbor
                    visualizer.draw_rect(x, y, (0, 0, 255))

                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, self.path + [neighbor]))

    def find_path_automated(self, maze):
        self.pathfinding_time = 0
        start_time = time.time()

        queue = [(maze.start_position, [maze.start_position])]
        # Enqueue the start node and mark it as visited
        visited = {maze.start_position}

        while queue:
            # Dequeue a node and its path
            current_node, self.path = queue.pop(0)

            # If the current node is the end node, return the path
            if current_node == maze.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(visited)

                print("BFS")
                print(f"Pathfinding time: {self.pathfinding_time}")
                print(f"Visited nodes: {self.visited_nodes}")
                print(f"Path length: {len(self.path)}\n")

                return
            # Explore neighbors of the current node
            for neighbor in maze.graph[current_node].neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)

                    # Draw rect for neighbor
                    x, y = neighbor

                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, self.path + [neighbor]))
