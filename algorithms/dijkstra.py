import time
import heapq

class Dijkstra:
    def __init__(self):
        self.pathfinding_time = 0
        self.visited_nodes = 0

    def find_path(self, visualizer):
        self.pathfinding_time = 0
        start_time = time.time()

        # A set to store visited nodes
        visited = {visualizer.maze.start_position}
        pq = [(0, visualizer.maze.start_position)]
        self.distances[visualizer.maze.start_position] = 0
        self.prev = {}

        while pq:
            distance, current_node = heapq.heappop(pq)
            if current_node == visualizer.maze.end_position:
                end_time = time.time()
                self.pathfinding_time = round(end_time - start_time, 5)
                self.visited_nodes = len(visited)
                break
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor in visualizer.maze.graph[current_node].neighbors:
                if neighbor not in visited:
                    new_dist = distance + 1 # Assuming all cell weights are 1
                    if neighbor not in self.distances or new_dist < self.distances[neighbor]:
                        self.distances[neighbor] = new_dist
                        self.prev[neighbor] = current_node
                        heapq.heappush(pq, (new_dist, neighbor))

    def shortest_path(self):
        if self.end not in self.prev:
            return None  # No path exists

        path = [self.end]
        while path[-1] != self.start:
            path.append(self.prev[path[-1]])
        path.reverse()
        return path
                        
        
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]
    
    def peek(self):
        return self.elements[0][1]
    
    def __len__(self):
        return len(self.elements)
    
"""
# Example usage:
pq = PriorityQueue()
pq.push('Task 1', 3)
pq.push('Task 2', 1)
pq.push('Task 3', 2)

print("Priority Queue size:", len(pq))
print("Top priority item:", pq.peek())

while not pq.is_empty():
    print("Next item:", pq.pop())
"""