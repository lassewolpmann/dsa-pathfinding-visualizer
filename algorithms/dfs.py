import time


class DFS:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0
        self.path = []

    def find_path(self, visualizer):
        self.pathfinding_time = 0
        start_time = time.time()

        # A set to store visited nodes
        visited = {visualizer.maze.start_position}

        # DFS uses stack (FIFO principle)
        # Initialize a stack array, containing tuples with node and path
        stack = [(visualizer.maze.start_position, [visualizer.maze.start_position])]

        while stack:
            current_node, self.path = stack.pop()  # Pop the last item in the list!

            # Check if the current node is the end node.
            # If yes, update the pathfinding time and return the visited nodes and path.
            if current_node == visualizer.maze.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(visited)

                return
            
            # If current node is not the end node continue search

            # If current node is not yet visited add it there
            if current_node not in visited:
                visited.add(current_node)

            # Check the neighbors of the current node and if the neighbor has not been visited yet, add it to the stack 
            for neighbor in visualizer.maze.graph[current_node].neighbors:
                x, y = neighbor
                visualizer.draw_rect(x, y, (0, 0, 255))

                if neighbor not in visited:
                    stack.append((neighbor, self.path + [neighbor]))
