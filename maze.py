from random import randint


class Maze:
    def __init__(self):
        self.rows = int(input("How many rows should the maze have (min. 4)?: "))
        self.cols = int(input("How many columns should the maze have (min. 4)?: "))
        self.maze = []
        self.graph = {}
        self.start_position = (0, 0)
        self.end_position = (0, 0)

        self.create_maze()

    def create_maze(self):
        self.maze = []

        for row in range(self.rows):
            r = []
            for col in range(self.cols):
                if row == 0 or col == 0 or row == self.rows - 1 or col == self.cols - 1:
                    # Create outer layer of Walls
                    r.append("#")
                else:
                    r.append("-")

            self.maze.append(r)

        self.place_walls()
        self.place_start_and_end_position()
        self.create_graph()

    def place_walls(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                char = self.maze[row][col]
                # Skip if there is already a wall
                if char != "#":
                    # 33% chance of Wall
                    if randint(1, 3) % 3 == 0:
                        self.maze[row][col] = "#"

    def place_start_and_end_position(self):
        start_point = [0, randint(1, self.cols - 2)]
        end_point = [self.rows - 1, randint(1, self.cols - 2)]

        self.start_position = (start_point[0], start_point[1])
        self.end_position = (end_point[0], end_point[1])

        self.maze[start_point[0] + 1][start_point[1]] = "-"
        self.maze[end_point[0] - 1][end_point[1]] = "-"

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

    def __str__(self):
        rows = []
        for row in self.maze:
            rows.append("".join(row))

        return "\n".join(rows)
