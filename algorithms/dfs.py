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

        while self.start_position == self.end_position:
            self.start_position = (randint(1, self.maze.width - 1), randint(1, self.maze.height - 1))
            self.end_position = (randint(1, self.maze.width - 1), randint(1, self.maze.height - 1))

        visited = {self.start_position}
        stack = [self.start_position]

        while stack:
            current_node = stack.pop()
                  
            if current_node == self.end_position:
                    end_time = time.time()
                    self.pathfinging_time = round(end_time - start_time, 5)

                    self.path = self._reconstruct_route(self.start_position, self.end_position)
                    
                    return visited, self.path

            if current_node not in visited:
                 visited.add(current_node)

                 for neighbor in self.graph[current_node].neighbors:
                      if neighbor not in visited:
                           stack.append(neighbor)

    def _reconstruct_route(self, start, end):
        path = []
        current_node = end

        while current_node != start:
            path.append(current_node)
            current_node = self.path[current_node]

        path.append(start)
        return path[::-1]


        
            
       