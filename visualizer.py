import pygame
from maze import Maze
from algorithms.bfs import BFS
from colour import Color

CELL_SIZE = 20
WALL_SIZE = 2
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 255)
START_COLOR = (0, 255, 0)
END_COLOR = (255, 0, 0)
PATHFINDING_COLOR = (0, 0, 255)
VISITED_COLOR = (255, 0, 255)


class Visualizer:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("DSA Pathfinding Visualizer")

        self.maze = Maze()
        self.screen_width = self.maze.width * CELL_SIZE + 210  # 210 pixels for buttons
        self.screen_height = self.maze.height * CELL_SIZE + 32 + CELL_SIZE  # 32 pixels for maze generation time text
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font = pygame.font.SysFont("arial", 16, bold=True)

        self.regen_button = Button("Regenerate Maze", (self.maze.width + 1) * CELL_SIZE, 0,
                                   self.screen_width, self.screen_height, self.screen, self.font)
        self.bfs_button = Button("Show BFS Path", (self.maze.width + 1) * CELL_SIZE, 60,
                                 self.screen_width, self.screen_height, self.screen, self.font)

        self.initial_draw()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if self.regen_button.check_collision(pos):
                        self.maze.generate_maze()
                        self.initial_draw()
                    elif self.bfs_button.check_collision(pos):
                        self.initial_draw()
                        bfs = BFS(self.maze)
                        visited, path = bfs.find_path()
                        self.draw_path(path, bfs.start_position, bfs.end_position)

            pygame.display.flip()

        pygame.quit()

    def initial_draw(self):
        # Fill Screen with White
        self.screen.fill(WALL_COLOR)

        # Draw Maze
        self.draw_maze()

        # Draw buttons
        self.regen_button.draw()
        self.bfs_button.draw()

        # Draw Maze generation Time
        text = self.font.render(f"Maze generation time: {self.maze.generation_time} seconds", True, (255, 255, 255))
        self.screen.blit(text, (CELL_SIZE, (self.maze.height + 1) * CELL_SIZE))

        # TODO: Add text for visited nodes, time elapsed to find shortest path, path length, etc.

    def draw_maze(self):
        graph = self.maze.graph
        for pos in graph:
            node = graph[pos]
            x, y = node.pos
            for wall in node.walls:
                x1, x2, y1, y2 = 0, 0, 0, 0
                if wall == (0, -1):
                    x1 = x
                    y1 = y
                    x2 = x + 1
                    y2 = y
                elif wall == (1, 0):
                    x1 = x + 1
                    y1 = y
                    x2 = x + 1
                    y2 = y + 1
                elif wall == (0, 1):
                    x1 = x
                    y1 = y + 1
                    x2 = x + 1
                    y2 = y + 1
                elif wall == (-1, 0):
                    x1 = x
                    y1 = y
                    x2 = x
                    y2 = y + 1

                pygame.draw.line(self.screen, (255, 255, 255), (x1 * CELL_SIZE, y1 * CELL_SIZE),
                                 (x2 * CELL_SIZE, y2 * CELL_SIZE), width=WALL_SIZE)

    def draw_path(self, path, start, end):
        colors = list(Color("green").range_to(Color("red"), len(path)))

        for i, (x, y) in enumerate(path):
            # Scale x and y to fill Cell
            x1 = x * CELL_SIZE
            x1 += WALL_SIZE
            y1 = y * CELL_SIZE
            y1 += WALL_SIZE

            width = CELL_SIZE - WALL_SIZE
            height = CELL_SIZE - WALL_SIZE

            rgb = map(lambda c: c * 255, colors[i].rgb)
            pygame.draw.rect(self.screen, tuple(rgb), (x1, y1, width, height))

            if (x, y) == start:
                s = "S"

            elif (x, y) == end:
                s = "E"
            else:
                current_pos = self.maze.graph[(x, y)].pos
                next_pos = self.maze.graph[path[i + 1]].pos
                c_x, c_y = current_pos
                n_x, n_y = next_pos
                dx = n_x - c_x
                dy = n_y - c_y

                direction = (dx, dy)
                directions = self.maze.directions
                if direction == directions[0]:
                    s = "↑"
                elif direction == directions[1]:
                    s = "→"
                elif direction == directions[2]:
                    s = "↓"
                else:
                    s = "←"

            # Only draw text when cells are big enough
            if CELL_SIZE >= 20:
                text = self.font.render(s, True, (255, 255, 255))
                text_rect = text.get_rect(center=(x1 + width // 2, y1 + height // 2))
                self.screen.blit(text, text_rect)


class Button:
    def __init__(self, button_text, x, y, width, height, screen, font):
        self.screen = screen
        self.font = font
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50
        self.color = (0, 200, 0)
        self.text_color = (255, 255, 255)
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
