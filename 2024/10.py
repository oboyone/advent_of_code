grid = []
target_value = '9'

with open('input.txt') as file:
    for line in file.readlines():
        grid.append([*line.strip()])

class Trailhead:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.score = 0
        self.rating = 0
        self.visited = [[False for _ in range(len(grid[0]))]
                        for _ in range(len(grid))]
        self.visited[x_pos][y_pos] = True
        self.queue = []

    def find_path(self):
        self.visited = [[False for _ in range(len(grid[0]))]
                        for _ in range(len(grid))]
        self.visited[self.x_pos][self.y_pos] = True
        self.queue.append((self.x_pos, self.y_pos))

        while len(self.queue) != 0:
            source = self.queue.pop()
            if grid[source[0]][source[1]] == '9':
                self.score += 1

            # Move Up
            if self.is_valid_next_hop(source[0] - 1, source[1], grid[source[0]][source[1]]):
                self.queue.append((source[0] - 1, source[1]))
                self.visited[source[0] - 1][source[1]] = True

            # Move Down
            if self.is_valid_next_hop(source[0] + 1, source[1], grid[source[0]][source[1]]):
                self.queue.append((source[0] + 1, source[1]))
                self.visited[source[0] + 1][source[1]] = True

            # Move Left
            if self.is_valid_next_hop(source[0], source[1] - 1, grid[source[0]][source[1]]):
                self.queue.append((source[0], source[1] - 1))
                self.visited[source[0]][source[1] - 1] = True

            # Move Right
            if self.is_valid_next_hop(source[0], source[1] + 1, grid[source[0]][source[1]]):
                self.queue.append((source[0], source[1] + 1))
                self.visited[source[0]][source[1] + 1] = True

    def find_raiting(self, x, y, target_value):
        # Found target
        if grid[x][y] == target_value:
            return 1

        # Mark the current cell as visited
        self.visited[x][y] = True

        total_raiting = 0

        # Recursion on all valid directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.is_valid_next_hop(nx, ny, grid[x][y]):
                total_raiting += self.find_raiting(nx, ny, target_value)

        # Set own cell to False again
        self.visited[x][y] = False

        return total_raiting

    def is_valid_next_hop(self, x, y, current_grid_value):
        if ((x >= 0 and y >= 0) and
            (x < len(grid) and y < len(grid[0])) and
            (int(grid[x][y]) == (int(current_grid_value) + 1)) and not self.visited[x][y]):
            return True
        return False




trailhead_objects = []

for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):
        if grid[row][col] == '0':
            trailhead_objects.append(Trailhead(row, col))

total_paths = 0
total_raiting = 0

for trailhead_object in trailhead_objects:
    total_raiting += trailhead_object.find_raiting(
        trailhead_object.x_pos,
        trailhead_object.y_pos,
        target_value='9'
    )
    trailhead_object.find_path()
    total_paths += trailhead_object.score

print("Total paths to target:", total_paths)
print("Total raiting:", total_raiting)

