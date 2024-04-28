import time
import heapq
from maze import Maze
from algorithms.path import trace_back_path


def calc_heuristic(a: Maze.Node, b: Maze.Node):
    a_x, a_y = a.pos
    b_x, b_y = b.pos

    return abs(a_x - b_x) + abs(a_y - b_y)


class AStar:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

        self.came_from = {}
        self.path = []

    def find_path(self, maze):
        self.pathfinding_time = 0
        start_time = time.time()

        start_node: Maze.Node = maze.graph[maze.start_position]
        end_node: Maze.Node = maze.graph[maze.end_position]

        start_node.g = 0
        start_node.f = calc_heuristic(start_node, end_node)

        open_list = []

        heapq.heappush(open_list, (start_node.f, start_node))

        while open_list:
            current = heapq.heappop(open_list)
            current_node = current[1]

            # Reconstruct path when reaching end pos
            if current_node.pos == end_node.pos:
                self.path = trace_back_path(maze.start_position, maze.end_position, self.came_from)

                self.pathfinding_time = round(time.time() - start_time, 5)
                self.visited_nodes = len(self.came_from)

                return

            for neighbor in current_node.neighbors:
                neighbor_node = maze.graph[neighbor]
                tentative_g_score = current_node.g + calc_heuristic(neighbor_node, end_node)

                if tentative_g_score < neighbor_node.g:
                    self.came_from[neighbor_node.pos] = current_node.pos
                    neighbor_node.g = tentative_g_score
                    neighbor_node.f = neighbor_node.g + calc_heuristic(neighbor_node, end_node)

                    heapq.heappush(open_list, (neighbor_node.f, neighbor_node))
