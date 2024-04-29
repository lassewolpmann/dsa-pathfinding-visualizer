import time
import heapq
from maze import Maze
from algorithms.path import trace_back_path


def calc_heuristic(a_pos: tuple, b_pos: tuple):
    a_x, a_y = a_pos
    b_x, b_y = b_pos

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

        # For node n, g_score[n] is the cost of the cheapest path from start to n currently known.
        g_score = {node: float('infinity') for node in maze.graph.keys()}
        g_score[maze.start_position] = 0

        # For node n, f_score[n] = g_score[n] + h(n). f_score[n] represents our current best guess as to how cheap
        # a path could be from start to finish if it goes through n.
        f_score = {node: float('infinity') for node in maze.graph.keys()}
        f_score[maze.start_position] = calc_heuristic(maze.start_position, maze.end_position)

        open_list = []
        heapq.heappush(open_list, (f_score[maze.start_position], maze.start_position))

        while open_list:
            # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
            current = heapq.heappop(open_list)
            current_node = current[1]

            # Reconstruct path when reaching end pos
            if current_node == maze.end_position:
                self.path = trace_back_path(maze.start_position, maze.end_position, self.came_from)

                self.pathfinding_time = round(time.time() - start_time, 5)
                self.visited_nodes = len(self.came_from)

                return

            for neighbor in maze.graph[current_node].neighbors:
                # Always adding 1, since we are using an unweighted graph, therefore weight always = 1
                tentative_g_score = g_score[current_node] + 1

                if tentative_g_score < g_score[neighbor]:
                    # This path to neighbor is better than any previous one. Record it!
                    self.came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + calc_heuristic(neighbor, maze.end_position)

                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
