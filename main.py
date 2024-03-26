from random import randint


class Maze:
    def __init__(self):
        self.rows = int(input("How many rows should the maze have?: "))
        self.cols = int(input("How many columns should the maze have?: "))
        self.maze = []
        self.graph = {}
        self.start_position = (0, 0)
        self.end_position = (0, 0)

        self.create_maze()
        self.place_walls()
        self.place_start_and_end_position()
        self.create_graph()

    def create_maze(self):
        for row in range(self.rows):
            r = []
            for col in range(self.cols):
                if row == 0 or col == 0 or row == self.rows - 1 or col == self.cols - 1:
                    r.append("#")
                else:
                    r.append("-")

            self.maze.append(r)

    def place_walls(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                char = self.maze[row][col]
                # Skip if there is already a wall
                if char != "#":
                    # 25% chance of Wall
                    if randint(1, 4) % 4 == 0:
                        self.maze[row][col] = "#"

    def place_start_and_end_position(self):
        start_point = [0, 0]
        end_point = [0, 0]

        # Make sure that Start- and Endpoint aren't the same
        while start_point == end_point:
            start_point = [randint(1, self.rows - 2), randint(1, self.cols - 2)]
            end_point = [randint(1, self.rows - 2), randint(1, self.cols - 2)]

        self.start_position = (start_point[0], start_point[1])
        self.end_position = (end_point[0], end_point[1])

        self.maze[start_point[0]][start_point[1]] = "S"
        self.maze[end_point[0]][end_point[1]] = "E"

    def create_graph(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] != '#':  # Exclude walls
                    neighbors = []
                    # Check adjacent cells
                    if i > 0 and self.maze[i - 1][j] != '#':
                        neighbors.append((i - 1, j))  # Upper cell
                    if i < self.rows - 1 and self.maze[i + 1][j] != '#':
                        neighbors.append((i + 1, j))  # Lower cell
                    if j > 0 and self.maze[i][j - 1] != '#':
                        neighbors.append((i, j - 1))  # Left cell
                    if j < self.cols - 1 and self.maze[i][j + 1] != '#':
                        neighbors.append((i, j + 1))  # Right cell
                    self.graph[(i, j)] = neighbors

    def bfs(self):
        # Queue for BFS
        queue = [(self.start_position, [self.start_position])]
        # Enqueue the start node and mark it as visited
        visited = {self.start_position}

        while queue:
            # Dequeue a node and its path
            current_node, path = queue.pop(0)
            # If the current node is the end node, return the path
            if current_node == self.end_position:
                return path
            # Explore neighbors of the current node
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, path + [neighbor]))

        # If no path is found
        return None

    def __str__(self):
        rows = []
        for row in self.maze:
            rows.append("".join(row))

        return "\n".join(rows)


if __name__ == "__main__":
    maze = Maze()
    print(maze)
    shortest_path = maze.bfs()
    print(shortest_path)
