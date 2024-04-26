import sys
import time
import heapq


class Dijkstra:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0
        self.distances = {}
        self.prev = {}
        self.path = []

    def find_path(self, visualizer):
        self.pathfinding_time = 0
        start_time = time.time()

        distances = {node: float('infinity') for node in visualizer.maze.graph.keys()}
        distances[visualizer.maze.start_position] = 0

        pq = [(0, visualizer.maze.start_position)]

        previous_nodes = {}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            neighbors = visualizer.maze.graph[current_node].neighbors
            for neighbor in neighbors:
                x, y = neighbor
                visualizer.draw_rect(x, y, (0, 0, 255))

                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        node = visualizer.maze.end_position

        while node != visualizer.maze.start_position:
            self.path.append(node)
            node = previous_nodes[node]

        self.path.append(visualizer.maze.start_position)

        self.pathfinding_time = round(time.time() - start_time, 5)
        self.visited_nodes = len(previous_nodes)

        self.path.reverse()

        return

    def find_path_automated(self, maze):
        self.pathfinding_time = 0
        start_time = time.time()

        distances = {node: float('infinity') for node in maze.graph.keys()}
        distances[maze.start_position] = 0

        pq = [(0, maze.start_position)]

        previous_nodes = {}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            neighbors = maze.graph[current_node].neighbors
            for neighbor in neighbors:
                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        node = maze.end_position

        while node != maze.start_position:
            self.path.append(node)
            node = previous_nodes[node]

        self.path.append(maze.start_position)

        self.pathfinding_time = round(time.time() - start_time, 5)
        self.visited_nodes = len(previous_nodes)

        self.path.reverse()

        print("Dijkstra")
        print(f"Pathfinding time: {self.pathfinding_time}")
        print(f"Visited nodes: {self.visited_nodes}")
        print(f"Path length: {len(self.path)}\n")

        return
