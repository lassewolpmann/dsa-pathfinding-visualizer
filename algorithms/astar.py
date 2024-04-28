import time
import heapq
from maze import Maze


def calc_heuristic(a: Maze.Node, b: Maze.Node):
    a_x, a_y = a.pos
    b_x, b_y = b.pos

    return abs(a_x - b_x) + abs(a_y - b_y)


class AStar:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0
        self.distances = {}
        self.prev = {}
        self.path = []

    def trace_path(self, maze, previous_nodes, start_time):
        # Trace back path
        node = maze.end_position

        while node != maze.start_position:
            self.path.append(node)
            node = previous_nodes[node]

        self.path.append(maze.start_position)

        self.pathfinding_time = round(time.time() - start_time, 5)
        self.visited_nodes = len(previous_nodes)

        self.path.reverse()

    def find_path(self, visualizer):
        self.pathfinding_time = 0
        start_time = time.time()

        start_node: Maze.Node = visualizer.maze.graph[visualizer.maze.start_position]
        end_node: Maze.Node = visualizer.maze.graph[visualizer.maze.end_position]

        start_node.g = 0
        start_node.f = calc_heuristic(start_node, end_node)

        open_list = []
        came_from = {}

        heapq.heappush(open_list, (start_node.f, start_node))

        while open_list:
            current = heapq.heappop(open_list)
            current_node = current[1]

            # Reconstruct path when reaching end pos
            if current_node.pos == end_node.pos:
                self.trace_path(visualizer.maze, came_from, start_time)

                return

            for neighbor in current_node.neighbors:
                neighbor_node = visualizer.maze.graph[neighbor]
                tentative_g_score = current_node.g + calc_heuristic(neighbor_node, end_node)

                if tentative_g_score < neighbor_node.g:
                    came_from[neighbor_node.pos] = current_node.pos
                    neighbor_node.g = tentative_g_score
                    neighbor_node.f = neighbor_node.g + calc_heuristic(neighbor_node, end_node)

                    heapq.heappush(open_list, (neighbor_node.f, neighbor_node))

                    x, y = neighbor_node.pos
                    visualizer.draw_rect(x, y, (0, 0, 255))

    def find_path_automated(self, maze):
        self.pathfinding_time = 0
        start_time = time.time()

        start_node: Maze.Node = maze.graph[maze.start_position]
        end_node: Maze.Node = maze.graph[maze.end_position]

        start_node.g = 0
        start_node.f = calc_heuristic(start_node, end_node)

        open_list = []
        came_from = {}

        heapq.heappush(open_list, (start_node.f, start_node))

        while open_list:
            current = heapq.heappop(open_list)
            current_node = current[1]

            # Reconstruct path when reaching end pos
            if current_node.pos == end_node.pos:
                self.trace_path(maze, came_from, start_time)

                print("A*")
                print(f"Pathfinding time: {self.pathfinding_time}")
                print(f"Visited nodes: {self.visited_nodes}")
                print(f"Path length: {len(self.path)}\n")

                return

            for neighbor in current_node.neighbors:
                neighbor_node = maze.graph[neighbor]
                tentative_g_score = current_node.g + calc_heuristic(neighbor_node, end_node)

                if tentative_g_score < neighbor_node.g:
                    came_from[neighbor_node.pos] = current_node.pos
                    neighbor_node.g = tentative_g_score
                    neighbor_node.f = neighbor_node.g + calc_heuristic(neighbor_node, end_node)

                    heapq.heappush(open_list, (neighbor_node.f, neighbor_node))
