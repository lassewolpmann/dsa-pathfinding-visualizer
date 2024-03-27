from random import randint
import pygame

WIDTH = 1024
HEIGHT = 1024
CELL_SIZE = 15
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 255)
START_COLOR = (0, 255, 0)
END_COLOR = (255, 0, 0)
PATHFINDING_COLOR = (0, 0, 255)


class Maze:
    def __init__(self):
        self.rows = int(input("How many rows should the maze have?: "))
        self.cols = int(input("How many columns should the maze have?: "))
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

    def __str__(self):
        rows = []
        for row in self.maze:
            rows.append("".join(row))

        return "\n".join(rows)


class Visualizer:
    def __init__(self, maze_object: Maze):
        pygame.init()
        pygame.display.set_caption("DSA Pathfinding Visualizer")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.maze = maze_object

        self.regen_button = Button("Regenerate Maze", (self.maze.rows + 1) * CELL_SIZE, 1 * CELL_SIZE, self.screen)
        self.bfs_button = Button("BFS", (self.maze.rows + 1) * CELL_SIZE, 5 * CELL_SIZE, self.screen)
        self.bfs_path = []

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.regen_button.check_collision(pos):
                        self.bfs_path = []
                        self.maze.create_maze()
                    elif self.bfs_button.check_collision(pos):
                        self.bfs_path = self.bfs()

                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h),
                                                          pygame.RESIZABLE)

            self.screen.fill(PATH_COLOR)
            self.draw_maze()
            self.regen_button.draw()
            self.bfs_button.draw()
            self.draw_path(self.bfs_path)

            pygame.display.flip()

        pygame.quit()

    def draw_maze(self):
        for x, row in enumerate(self.maze.maze):
            for y, cell in enumerate(row):
                if cell == "#":
                    color = WALL_COLOR
                elif cell == "S":
                    color = START_COLOR
                elif cell == "E":
                    color = END_COLOR
                else:
                    color = PATH_COLOR

                pygame.draw.rect(self.screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_path(self, path):
        for pos in path:
            if pos != self.maze.start_position and pos != self.maze.end_position:
                pygame.draw.rect(self.screen, PATHFINDING_COLOR, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE,
                                                                  CELL_SIZE, CELL_SIZE))

    def bfs(self):
        # Queue for BFS
        queue = [(self.maze.start_position, [self.maze.start_position])]
        # Enqueue the start node and mark it as visited
        visited = {self.maze.start_position}

        while queue:
            # Dequeue a node and its path
            current_node, path = queue.pop(0)
            # If the current node is the end node, return the path
            if current_node == self.maze.end_position:
                return path
            # Explore neighbors of the current node
            for neighbor in self.maze.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Enqueue the neighbor and update the path
                    queue.append((neighbor, path + [neighbor]))


class Button:
    def __init__(self, button_text, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50
        self.color = (0, 200, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("arial", 18)
        self.button_text = button_text
        self.rect = pygame.Rect((WIDTH - self.width) // 2, (HEIGHT - self.height) // 2, self.width,
                                self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(str(self.button_text), True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text, text_rect)

    def check_collision(self, mouse_pos) -> bool:
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height


if __name__ == "__main__":
    maze = Maze()
    # shortest_path = maze.bfs()
    visualizer = Visualizer(maze)
