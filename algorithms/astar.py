import sys
import time
from maze import Maze


class AStar:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0
        self.distances = {}
        self.prev = {}

    def calc_heuristic(self, a: Maze.Node, b: Maze.Node):
        a_x, a_y = a.pos
        b_x, b_y = b.pos

        return abs(a_x - b_x) + abs(a_y - b_y)

    def find_path(self, visualizer):
        self.pathfinding_time = 0
        start_time = time.time()

        open_list = [visualizer.maze.start_position]
        closed_list = {}

        while open_list:
            current_node = open_list.pop()

            if current_node == visualizer.maze.end_position:
                path = []
                node = visualizer.maze.end_position

                while node != visualizer.maze.start_position:
                    path.append(node)
                    node = closed_list[node]

                path.append(visualizer.maze.start_position)

                self.pathfinding_time = round(time.time() - start_time, 5)
                self.visited_nodes = len(closed_list)

                path.reverse()
                return path

            for neighbor in visualizer.maze.graph[current_node].neighbors:
                if neighbor in closed_list:
                    continue

                neighbor_node = visualizer.maze.graph[neighbor]
                end_node = visualizer.maze.graph[visualizer.maze.end_position]

                tentative_g_score = visualizer.maze.graph[current_node].g + 1
                closed_list[neighbor] = current_node
                neighbor_node.g = tentative_g_score
                neighbor_node.f = neighbor_node.g + self.calc_heuristic(neighbor_node, end_node)

                if neighbor in open_list:
                    continue

                open_list.append(neighbor)
                x, y = neighbor
                visualizer.draw_rect(x, y, (0, 0, 255))

        '''
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
        '''
