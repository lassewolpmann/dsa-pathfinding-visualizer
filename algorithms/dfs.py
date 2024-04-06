from maze import Maze
import time


class DFS:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

    def find_path(self, maze: Maze, start_pos: tuple, end_pos: tuple):
        start_time = time.time()

        # A set to store visited nodes
        visited = {start_pos}

        # DFS uses stack (FIFO principle)
        # Initialize a stack array, containing tuples with node and path
        stack = [(start_pos, [start_pos])]

        while stack:
            current_node, path = stack.pop()  # Pop the last item in the list!

            # Check if the current node is the end node.
            # If yes, update the pathfinding time and return the visited nodes and path.
            if current_node == end_pos:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(visited)

                return visited, path
            
            # If current node is not the end node continue search

            # If current node is not yet visited add it there
            if current_node not in visited:
                visited.add(current_node)

            # Check the neighbors of the current node and if the neighbor has not been visited yet, add it to the stack 
            for neighbor in maze.graph[current_node].neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
