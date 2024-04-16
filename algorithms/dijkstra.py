import sys
import time
import heapq


class Dijkstra:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0
        self.distances = {}
        self.prev = {}

    def find_path(self, visualizer):
        self.pathfinding_time = 0
        start_time = time.time()

        unvisited_nodes = list(visualizer.maze.graph.keys())

        shortest_path = {}
        previous_nodes = {}

        max_value = sys.maxsize

        # Essentially setting the distance to infinity for every node, except the starting node
        for node in unvisited_nodes:
            shortest_path[node] = max_value

        shortest_path[visualizer.maze.start_position] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = visualizer.maze.graph[current_min_node].neighbors
            for neighbor in neighbors:
                x, y = neighbor
                visualizer.draw_rect(x, y, (0, 0, 255))

                tentative_value = shortest_path[current_min_node] + 1
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node

            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)

        path = []
        node = visualizer.maze.end_position

        while node != visualizer.maze.start_position:
            path.append(node)
            node = previous_nodes[node]

        path.append(visualizer.maze.start_position)

        self.pathfinding_time = round(time.time() - start_time, 5)
        self.visited_nodes = len(previous_nodes)

        path.reverse()
        return path
