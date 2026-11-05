import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

positions = [(0, 0)]

for elem in file_content:
    if elem == "^": curr_pos = (positions[-1][0] + 0, positions[-1][1] +  1)
    elif elem == ">": curr_pos = (positions[-1][0] + 1, positions[-1][1] +  0)
    elif elem == "<": curr_pos = (positions[-1][0] + -1, positions[-1][1] +  0)
    elif elem == "v": curr_pos = (positions[-1][0] + 0, positions[-1][1] +  -1)
    positions.append(curr_pos)


unique_pos = set(positions)
part_1_res = len(unique_pos)

moves = {"^": (0, 1), ">": (1, 0), "<": (-1, 0), "v": (0, -1)}
santas = [(0, 0), (0, 0)]  # Santa and Robo-Santa
visited = {(0, 0)}
for i, elem in enumerate(file_content):
    dx, dy = moves[elem]
    x, y = santas[i % 2]
    santas[i % 2] = (x + dx, y + dy)
    visited.add(santas[i % 2])
part_2_res = len(visited)

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
