import sys

file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()


def in_bounds(pos, max_x, max_y):
    x, y = pos
    return x >= 0 and x <= max_x and y >= 0 and y <= max_y


def find_all_paths(pos, grid, nrows, ncols, visited=None, current_path=None, all_paths=None):
    if visited is None:
        visited = set()
    if current_path is None:
        current_path = []
    if all_paths is None:
        all_paths = []

    x, y = pos
    current_path.append(pos)
    visited.add(pos)

    if grid[x][y] == 9:
        all_paths.append(current_path.copy())
    else:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if in_bounds((nx, ny), nrows, ncols) and (nx, ny) not in visited:
                if grid[nx][ny] - grid[x][y] == 1:
                    find_all_paths((nx, ny), grid, nrows, ncols, visited, current_path, all_paths)

    current_path.pop()
    visited.remove(pos)

    return all_paths



num_rows = len(file_content) - 1
num_cols = len(file_content[0]) - 1

grid = []
for line in file_content:
    elems = []
    for elem in line:
        elems.append(int(elem))
    grid.append(elems)

part_1_res = 0
part_2_res = 0
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == 0:
            destinations = set()
            res = find_all_paths((i, j), grid, num_rows, num_cols)
            print(res)
            part_2_res += len(res)
            for elem in res:
                destinations.add(elem[-1])
            part_1_res += len(destinations)
        

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")