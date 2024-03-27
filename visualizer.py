import pygame
from maze import Maze
from algorithms.bfs import BFS

CELL_SIZE = 10
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 255)
START_COLOR = (0, 255, 0)
END_COLOR = (255, 0, 0)
PATHFINDING_COLOR = (0, 0, 255)
VISITED_COLOR = (255, 0, 255)


class Visualizer:
    def __init__(self, maze: Maze):
        pygame.init()
        pygame.display.set_caption("DSA Pathfinding Visualizer")

        width = maze.cols * CELL_SIZE + 200
        height = maze.rows * CELL_SIZE

        self.screen = pygame.display.set_mode((width, height))
        self.maze = maze

        self.regen_button = Button("Regenerate Maze", (self.maze.cols + 1) * CELL_SIZE, 0, width, height, self.screen)
        self.bfs_button = Button("BFS", (self.maze.cols + 1) * CELL_SIZE, 60, width, height, self.screen)

        self.initial_draw()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.regen_button.check_collision(pos):
                        self.maze.create_maze()
                        self.draw_maze()
                    elif self.bfs_button.check_collision(pos):
                        bfs = BFS(self.maze)
                        visited = bfs.visited
                        path = bfs.path

                        if visited and path:
                            self.draw_path(visited, VISITED_COLOR)
                            self.draw_path(path, PATHFINDING_COLOR)

            pygame.display.flip()

        pygame.quit()

    def initial_draw(self):
        # Fill Screen with White
        self.screen.fill(PATH_COLOR)

        # Draw Maze
        self.draw_maze()

        # Draw buttons
        self.regen_button.draw()
        self.bfs_button.draw()

    def draw_maze(self):
        for y, row in enumerate(self.maze.maze):
            for x, cell in enumerate(row):
                if cell == "#":
                    color = WALL_COLOR
                elif cell == "S":
                    color = START_COLOR
                elif cell == "E":
                    color = END_COLOR
                else:
                    color = PATH_COLOR

                pygame.draw.rect(self.screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_path(self, path, color):
        for pos in path:
            if pos != self.maze.start_position and pos != self.maze.end_position:
                pygame.draw.rect(self.screen, color, (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE,
                                                      CELL_SIZE, CELL_SIZE))


class Button:
    def __init__(self, button_text, x, y, width, height, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50
        self.color = (0, 200, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("arial", 18)
        self.button_text = button_text
        self.rect = pygame.Rect((width - self.width) // 2, (height - self.height) // 2, self.width,
                                self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(str(self.button_text), True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text, text_rect)

    def check_collision(self, mouse_pos) -> bool:
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height