from random import randint


class Maze:
    def __init__(self):
        self.rows = int(input("How many rows should the maze have?: "))
        self.cols = int(input("How many columns should the maze have?: "))
        self.maze = self.create_maze()
        self.place_walls()
        self.place_start_and_end_position()

    def create_maze(self):
        m = []
        for row in range(self.rows):
            r = []
            for col in range(self.cols):
                if row == 0 or col == 0 or row == self.rows - 1 or col == self.cols - 1:
                    r.append("#")
                else:
                    r.append("-")

            m.append(r)

        return m

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
        start_row_position = randint(1, self.rows - 2)
        start_col_position = randint(1, self.cols - 2)

        end_row_position = randint(1, self.rows - 2)
        end_col_position = randint(1, self.cols - 2)

        self.maze[start_row_position][start_col_position] = "S"
        self.maze[end_row_position][end_col_position] = "E"

    def __str__(self):
        rows = []
        for row in self.maze:
            rows.append("".join(row))

        return "\n".join(rows)


if __name__ == "__main__":
    maze = Maze()
