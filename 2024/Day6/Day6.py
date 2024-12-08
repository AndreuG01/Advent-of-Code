import sys

file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()


directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
dir_idx = 0

x, y = 0, 0
for i, line in enumerate(file_content):
    if "^" in line:
        y = i
        x = line.index("^")


part_1_res = 1
part_2_res = 0


def print_map(content, curr_pos):
    for i, line in enumerate(content):
        for j, char in enumerate(line):
            if (i, j) == curr_pos:
                print("^", end="")
            else:
                if char == "^":
                    print(".", end="")
                else:
                    print(char, end="")
        print()
            

bounds_y = len(file_content) - 1
bounds_x = len(file_content[0]) - 1

visited = [(x, y)]

while True:
    offset = directions[dir_idx % len(directions)]
    x += offset[0]
    y += offset[1]
    if (x < 0 or x > bounds_x) or (y < 0 or y > bounds_y): break
    if file_content[y][x] == "#":
        x -= offset[0]
        y -= offset[1]
        dir_idx += 1
        # part_1_res -= 1
    
    if (x, y) not in visited: part_1_res += 1
    visited.append((x, y))

print(f"Part 1 res: {part_1_res}")