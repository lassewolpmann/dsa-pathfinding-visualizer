from maze import Maze
import time


class BFS:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

    def find_path(self, maze: Maze, start_pos: tuple, end_pos: tuple):
        start_time = time.time()

        queue = [(start_pos, [start_pos])]
        # Enqueue the start node and mark it as visited
        visited = {start_pos}

        while queue:
            # Dequeue a node and its path
            current_node, path = queue.pop(0)
            # If the current node is the end node, return the path
            if current_node == end_pos:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(visited)

                return visited, path
            # Explore neighbors of the current node
            for neighbor in maze.graph[current_node].neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, path + [neighbor]))
