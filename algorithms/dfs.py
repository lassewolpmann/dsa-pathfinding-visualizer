import time


class DFS:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

        self.visited = []
        self.path = []

    def find_path(self, maze):
        self.pathfinding_time = 0
        start_time = time.time()

        # A set to store visited nodes
        self.visited.append(maze.start_position)

        # DFS uses stack (FIFO principle)
        # Initialize a stack array, containing tuples with node and path
        stack = [(maze.start_position, [maze.start_position])]

        while stack:
            # Pop the last item in the list!
            current_node, self.path = stack.pop()

            # Check if the current node is the end node.
            # If yes, update the pathfinding time and return the visited nodes and path.
            if current_node == maze.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(self.visited)

                return
            
            # If current node is not the end node continue search

            # If current node is not yet visited add it there
            if current_node not in self.visited:
                self.visited.append(current_node)

            # Check the neighbors of the current node and if the neighbor has not been visited yet, add it to the stack 
            for neighbor in maze.graph[current_node].neighbors:
                if neighbor not in self.visited:
                    stack.append((neighbor, self.path + [neighbor]))
