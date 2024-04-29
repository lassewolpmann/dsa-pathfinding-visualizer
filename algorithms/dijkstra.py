import time
import heapq
from algorithms.path import trace_back_path


class Dijkstra:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

        self.previous_nodes = {}
        self.path = []

    def find_path(self, maze):
        self.pathfinding_time = 0
        start_time = time.time()

        # Setting distance to infinity for every node, since we don't have any information yet.
        distances = {node: float('infinity') for node in maze.graph.keys()}

        # Set distance for start position to 0
        distances[maze.start_position] = 0

        # Create priority queue and add start position
        pq = []
        heapq.heappush(pq, (0, maze.start_position))

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            neighbors = maze.graph[current_node].neighbors
            for neighbor in neighbors:

                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    self.previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        self.path = trace_back_path(maze.start_position, maze.end_position, self.previous_nodes)

        self.pathfinding_time = round(time.time() - start_time, 5)
        self.visited_nodes = len(self.previous_nodes)

        return
