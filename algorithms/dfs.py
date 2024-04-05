from maze import Maze
from random import randint
import time

class DFS:
    def __init__(self, maze: Maze):
        self.start_position = (0, 0)
        self.end_position = (0, 0)
        self.maze = maze

        self.graph = maze.graph
        self.pathfinding_time = 0
        self.visited = {}
        self.path = []

    def find_path(self):
        start_time = time.time()

        self.start_position = (0, 0)
        self.end_position = (0, 0)

        # If start position is the same as end position randomly generate new ones
        while self.start_position == self.end_position:
            self.start_position = (randint(1, self.maze.width - 1), randint(1, self.maze.height - 1))
            self.end_position = (randint(1, self.maze.width - 1), randint(1, self.maze.height - 1))

        # A set to store visited nodes
        visited = {self.start_position}
        # DFS uses stack (FIFO principle)
        # Initialize a stack array, containing tuples with node and path
        stack = [(self.start_position, [self.start_position])]

        while stack:
            current_node, path = stack.pop() # Pop the last item in the list!
                  
            # Check if the current node is the end node. If yes, update the pathfinding time and return the visited nodes and path      
            if current_node == self.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)

                return visited, path
            
            # If current node is not the end node continue search

            # If current node is not yet visited add it there
            if current_node not in visited:
                visited.add(current_node)

            # Check the neighbors of the current node and if the neighbor has not been visited yet, add it to the stack 
            for neighbor in self.graph[current_node].neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
