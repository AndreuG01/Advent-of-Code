import sys
from collections import deque
file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

def print_grid(dims, blocked_positions, path):
    for i in range(dims):
        row = ""
        for j in range(dims):
            if (i, j) in blocked_positions:
                row += "#"
            elif (i, j) in path:
                row += "O"
            else:
                row += "."
        print(row)


def reconstruct_path(came_from, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = came_from[current]
        
    
    return path

def bfs_path(blocked_positions, dims):
    start, end = (0, 0), (dims - 1, dims - 1)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    queue = deque([start])
    visited = set([start])
    came_from = {start: None}

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return reconstruct_path(came_from, end)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < dims and 0 <= ny < dims and (nx, ny) not in blocked_positions and (nx, ny) not in visited:
                visited.add((nx, ny))
                came_from[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return []

num_bytes = 1024
blocked_positions = []
part1_blocked_positions = []
for i, line in enumerate(file_content):
    x, y = line.split(",")
    blocked_positions.append((int(y), int(x)))
    if i > num_bytes: continue
    else: part1_blocked_positions.append((int(y), int(x)))

dims = 71
path_part_1 = bfs_path(part1_blocked_positions, dims)

print_grid(dims, part1_blocked_positions, path_part_1)
part_1_res = len(path_part_1) - 1



# Binary search for part 2, to do a "speeded up brute force approach"
left, right = 0, len(blocked_positions) - 1
first_failure = -1

while left <= right:
    idx = left + (right - left) // 2
    print(f"Left: {left} right: {right}, idx: {idx}")
    part2_path = bfs_path(blocked_positions[:idx], dims)

    if len(part2_path) > 0:
        left = idx + 1
    else:
        first_failure = idx
        right = idx - 1

# Reverse it because we have reversed it when reading the input
first_pos = blocked_positions[first_failure - 1][::-1]
part_2_res = f"{first_pos[0]},{first_pos[1]}"

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
