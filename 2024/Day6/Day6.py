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

# Part 2: an extra obstruction only changes the route if the guard would
# walk into it, so the only candidates are the cells of the original route.
start_x, start_y = next(
    (line.index("^"), i) for i, line in enumerate(file_content) if "^" in line
)
obstacles = {
    (j, i) for i, line in enumerate(file_content) for j, char in enumerate(line) if char == "#"
}


def gets_stuck(extra: tuple[int, int]) -> bool:
    x, y, dir_idx = start_x, start_y, 0
    # Remembering the state only when the guard turns is enough to spot a loop
    turns = set()
    while True:
        dx, dy = directions[dir_idx]
        nx, ny = x + dx, y + dy
        if not (0 <= nx <= bounds_x and 0 <= ny <= bounds_y):
            return False
        if (nx, ny) in obstacles or (nx, ny) == extra:
            if (x, y, dir_idx) in turns:
                return True
            turns.add((x, y, dir_idx))
            dir_idx = (dir_idx + 1) % len(directions)
        else:
            x, y = nx, ny


for candidate in set(visited) - {(start_x, start_y)}:
    if gets_stuck(candidate):
        part_2_res += 1

print(f"Part 2 res: {part_2_res}")
