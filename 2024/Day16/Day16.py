import sys
import heapq

file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()
start_pos = None
end_pos = None

offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for x, line in enumerate(file_content):
    for y, char in enumerate(line):
        if char == "E":
            end_pos = (x, y)
        elif char == "S":
            start_pos = (x, y)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

num_rows = len(file_content)
num_cols = len(file_content[0])

def is_valid(x, y, rows, cols, maze, visited):
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] != "#" and (x, y) not in visited

def calculate_cost(current_direction, next_direction):
    cost = 1
    if current_direction != next_direction:
        cost += 1000
    return cost

def dijkstra(maze, start, end, rows, cols):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, (0, 1), [start]))  # (score, position, direction, path)
    visited = set()

    while priority_queue:
        score, position, current_direction, path = heapq.heappop(priority_queue)

        if position in visited:
            continue
        visited.add(position)

        if position == end:
            return score, path

        x, y = position
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            next_direction = (dx, dy)

            if is_valid(nx, ny, rows, cols, maze, visited):
                next_score = score + calculate_cost(current_direction, next_direction)
                heapq.heappush(priority_queue, (next_score, (nx, ny), next_direction, path + [(nx, ny)]))

    return 100000000, []


part_1_res, part_1_path = dijkstra(file_content, start_pos, end_pos, num_rows, num_cols)
    
def plot_path(maze, path):
    for x, line in enumerate(maze):
        tmp_line = ""
        for y, char in enumerate(line):
            if (x, y) in path:
                tmp_line += "X"
            else:
                tmp_line += char
        print(tmp_line)

plot_path(file_content, part_1_path)

print(f"Part 1 res: {part_1_res}")