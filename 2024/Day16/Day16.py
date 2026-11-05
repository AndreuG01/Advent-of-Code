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

# Part 2: the search above only remembers one path per tile, so to find every
# tile on any best path search over (tile, facing) states instead. A state is
# on a best path when the cheapest way from S to it plus the cheapest way from
# it to E adds up to the best score.
def state_costs(sources: list[tuple[tuple[int, int], tuple[int, int]]], backwards: bool):
    costs = {}
    queue = [(0, pos, direction) for pos, direction in sources]
    heapq.heapify(queue)
    while queue:
        score, pos, direction = heapq.heappop(queue)
        if (pos, direction) in costs:
            continue
        costs[(pos, direction)] = score

        # Moving one step in the facing direction (or back against it when
        # searching from E), or turning 90 degrees on the spot
        step = -1 if backwards else 1
        nx, ny = pos[0] + step * direction[0], pos[1] + step * direction[1]
        if file_content[nx][ny] != "#":
            heapq.heappush(queue, (score + 1, (nx, ny), direction))
        dx, dy = direction
        for turned in [(dy, -dx), (-dy, dx)]:
            heapq.heappush(queue, (score + 1000, pos, turned))
    return costs


from_start = state_costs([(start_pos, (0, 1))], backwards=False)
from_end = state_costs([(end_pos, direction) for direction in directions], backwards=True)
best_score = min(from_start.get((end_pos, direction), float("inf")) for direction in directions)

best_tiles = {
    pos for (pos, direction), score in from_start.items()
    if score + from_end.get((pos, direction), float("inf")) == best_score
}

part_2_res = len(best_tiles)
print(f"Part 2 res: {part_2_res}")
