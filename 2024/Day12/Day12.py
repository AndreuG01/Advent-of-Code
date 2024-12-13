import sys
from collections import defaultdict
file_content = open(sys.argv[1]).read().strip()
# file_content = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""
file_content = file_content.splitlines()

def in_bounds(pos, max_x, max_y):
    x, y = pos
    return x >= 0 and x <= max_x and y >= 0 and y <= max_y



def in_region(grid, pos):
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x, y = pos
    for dx, dy in offsets:
        new_x, new_y = (x+dx, y+dy)
        if in_bounds((new_x, new_y), len(grid) - 1, len(grid[0]) - 1) and (grid[new_x][new_y] == grid[x][y]):
            return True
        
    return False 

def get_perimeter(points):
    neighbors = {}
    for x, y in points:
        count = 0
        if (x - 1, y) in points:
            count += 1
        if (x + 1, y) in points:
            count += 1
        if (x, y - 1) in points:
            count += 1
        if (x, y + 1) in points:
            count += 1
        neighbors[(x, y)] = count

    return sum([4 - val for val in list(neighbors.values())])


def dfs(x, y, plant_type, visited, rows, cols, grid):
        stack = [(x, y)]
        region = []
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            region.append((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == plant_type:
                    stack.append((nx, ny))
        return region
    
def get_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = grid[r][c]
                region = dfs(r, c, plant_type, visited, rows, cols, grid)
                if region:
                    regions[plant_type].append(region)
    
    return dict(regions)
    


plant_types = defaultdict(list)

for i, line in enumerate(file_content):
    for j, char in enumerate(line):
        plant_types[char].append((i, j))

regions = get_regions(file_content)

part_1_res = 0
part_2_res = 0
for type, all_reg in regions.items():
    # print(all_reg)
    for reg in all_reg:
        # print(reg)
        print(f"{type}: {len(reg)} * {get_perimeter(reg)} = {len(reg) * get_perimeter(reg)}")
        part_1_res += len(reg) * get_perimeter(reg)

print(f"Part 1 res: {part_1_res}")