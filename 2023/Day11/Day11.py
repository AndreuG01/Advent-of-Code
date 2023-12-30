import sys

def solve(positions, increase, double_rows, double_cols):
    res = 0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            horizontal_pos = [i for i in range(min(positions[i][0], positions[j][0]), max(positions[i][0], positions[j][0]) + 1)]
            vertical_pos = [i for i in range(min(positions[i][1], positions[j][1]), max(positions[i][1], positions[j][1]) + 1)]
            
            horizontal_intersection = [i for i in horizontal_pos if i in double_rows]
            vertical_intersection = [i for i in vertical_pos if i in double_cols]
            
            length = len(horizontal_intersection) + len(vertical_intersection)
            
            # Compute Manhattan distances between every pair of galaxies

            dist = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1]) + (length * increase)
            res += dist
    
    return res


file_content = open(sys.argv[1]).read().strip().splitlines()
original_file_content = file_content.copy()

# First, expand the input
double_rows = []
double_cols = []

# (rows)
for i, line in enumerate(file_content):
    if "#" not in line:
        double_rows.append(i)

# (columns)
for j in range(len(file_content[0])):
    empty_col = True
    for i in range(len(file_content)):
        if file_content[i][j] == "#":
            empty_col = False
            break
    if empty_col:
        double_cols.append(j)


# Store positions where galaxies are included:
positions = []
for i in range(len(original_file_content)):
    for j in range(len(original_file_content[0])):
        if original_file_content[i][j] == "#":
            positions.append([i, j])


part1_res = solve(positions, 1, double_rows, double_cols)
part2_res = solve(positions, 999999, double_rows, double_cols)


print(f"Part 1 res: {part1_res}")
print(f"Part 2 res: {part2_res}")