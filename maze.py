import random
import time
from random import randint
import sys


class Maze:
    class Node:
        def __init__(self, pos, value):
            self.pos = pos
            self.value = value
            self.weight = randint(1, 50)
            self.walls = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            self.neighbors = []

        def __str__(self):
            return f"Node at {self.pos} with neighbors at {self.neighbors} and walls at {self.walls}"

        def __lt__(self, other):
            return self.f < other.f

        def __le__(self, other):
            return self.f <= other.f

    def __init__(self, width: int, height: int):
        if width == 0 or height == 0:
            self.width = int(input("Enter the width of the maze: "))
            self.height = int(input("Enter the height of the maze: "))

        else:
            self.width = width
            self.height = height

        self.start_position, self.end_position = (0, 0), (0, 0)

        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        self.generation_time = 0

        self.graph = {}
        self.visited_cells = {}
        self.generate_maze()
        self.generate_start_end()

    def generate_maze(self):
        start_time = time.time()

        for x in range(self.width):
            for y in range(self.height):
                self.graph[(x, y)] = Maze.Node((x, y), 1)

        first_node = Maze.Node(self.get_random_unvisited_cell(), 0)

        self.graph[first_node.pos] = first_node
        self.visited_cells = {first_node.pos}

        while len(self.visited_cells) < self.width * self.height:
            path = self.random_walk()

            (x, y) = path["start"]
            (pdx, pdy) = (0, 0)

            while (x, y) not in self.visited_cells:
                # Step 1: Mark Cell as visited
                self.visited_cells.add((x, y))

                # Step 2: Create node at current position
                current_node = Maze.Node((x, y), 0)

                # Step 3: Get directions and remove wall for that direction
                (dx, dy) = path[(x, y)]
                current_node.walls.remove((dx, dy))

                # Step 4: Get previous direction, invert it and remove that wall as well
                if (pdx, pdy) in self.directions:
                    current_node.walls.remove((pdx * -1, pdy * -1))

                # Step 5: Add node to maze
                self.graph[(x, y)] = current_node

                # Step 6: Update values
                (x, y) = (x + dx, y + dy)
                (pdx, pdy) = (dx, dy)

            # Step 7: Get node at final position and remove wall for previous direction
            self.graph[(x, y)].walls.remove((pdx * -1, pdy * -1))

        # Step 8: Get Neighbors
        for pos in self.graph:
            node = self.graph[pos]
            (x, y) = node.pos
            node.neighbors = [(x + dx, y + dy) for (dx, dy) in self.directions if (dx, dy) not in node.walls]

        end_time = time.time()

        self.generation_time = round(end_time - start_time, 5)

    def get_random_unvisited_cell(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)

        while self.graph[(x, y)].value == 0:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

        return x, y

    def random_walk(self):
        (x, y) = self.get_random_unvisited_cell()
        path = {"start": (x, y)}

        while (x, y) not in self.visited_cells:
            dx, dy = random.choice(self.directions)
            nx, ny = x + dx, y + dy

            if 0 <= nx < self.width and 0 <= ny < self.height:
                path[(x, y)] = (dx, dy)
                x, y = nx, ny

        return path

    def generate_start_end(self):
        self.start_position = (0, 0)
        self.end_position = (0, 0)

        while self.start_position == self.end_position:
            self.start_position = (randint(1, self.width - 1), randint(1, self.height - 1))
            self.end_position = (randint(1, self.width - 1), randint(1, self.height - 1))
