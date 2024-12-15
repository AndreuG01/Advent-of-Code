import sys
from collections import Counter, deque
file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()


def print_grid(rows, cols, positions):
    pos_dict = Counter(positions)
    for x in range(rows):
        row = ""
        for y in range(cols):
            if (x, y) in pos_dict:
                row += str(pos_dict[(x, y)])
            else:
                row += "."
        print(row)

positions = []
velocities = []
for line in file_content:
    p, v = line.split(" ")
    y, x = p.split(",")
    x = int(x)
    y = int(y[2:])
    positions.append((x, y))
    
    
    vy, vx = v.split(",")
    vx = int(vx)
    vy = int(vy[2:])
    velocities.append((vx, vy))
    
    # print(f"x: {x}, y: {y}, vx: {vx}, vy: {vy}")
    

def part_1(num_rows, num_cols, final_positions):
    final = Counter(final_positions)
    final_positions = set(final_positions)

    first = 0
    second = 0
    third = 0
    fourth = 0
    for x, y in final_positions:
        if x < num_rows // 2 and y < num_cols // 2:
            first += final[(x, y)]
        if x > num_rows // 2 and y < num_cols // 2:
            second += final[(x, y)]
        if x < num_rows // 2 and y > num_cols // 2:
            third += final[(x, y)]
        
        if x > num_rows // 2 and y > num_cols // 2:
            fourth += final[(x, y)]
    return first * second * third * fourth

def neighbors(row, col):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < num_rows and 0 <= nc < num_cols:
            yield nr, nc

def bfs(start_row, start_col, visited, grid):
        queue = deque([(start_row, start_col)])
        visited.add((start_row, start_col))
        while queue:
            r, c = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))


def get_connected_components(num_rows, num_cols, positions):
    grid = [[0] * num_cols for _ in range(num_rows)]
    for r, c in positions:
        grid[r][c] = 1

    visited = set()
    count = 0

    for r, c in positions:
        if (r, c) not in visited:
            count += 1
            bfs(r, c, visited, grid)

    return count


num_rows = max([elem[0] for elem in positions]) + 1
num_cols = max([elem[1] for elem in positions]) + 1

num_steps = 10000
part_2_res = 0
part_2_positions = []
for i in range(num_steps):
    final_positions = []
    for position, velocity in zip(positions, velocities):
        x, y = position
        vx, vy = velocity
        final_posx, final_posy = x, y
        final_posx = (final_posx + vx) % num_rows
        final_posy = (final_posy + vy) % num_cols
        final_positions.append((final_posx, final_posy))
    if i == 99:
        part_1_res = part_1(num_rows, num_cols, final_positions)
    components = get_connected_components(num_rows, num_cols, final_positions)
    if components <= 300: # 300 found by trial and error
        part_2_res = i + 1
        part_2_positions = final_positions.copy()
        break
        
        
    positions = final_positions.copy()


print(f"Part 1 res: {part_1_res}")
print_grid(num_rows, num_cols, part_2_positions)
print(f"Part 2 res: {part_2_res}")
