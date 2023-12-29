import sys
from math import lcm


def solve(start_nodes):
    path_lengths = []

    for node in start_nodes:
        num_steps = 0
        search_pos = node
        while not search_pos.endswith("Z"):
            dir = instructions[num_steps % len(instructions)]
            
            if dir == "L": idx = 0
            else: idx = 1
            
            search_pos = positions[search_pos][idx]
            num_steps += 1

        path_lengths.append(num_steps)
            

    return lcm(*path_lengths)

file_content = open(sys.argv[1]).read().strip().splitlines()

instructions = file_content[0]
positions = {}

for line in file_content[2:]:

    origin = line.split("=")[0][:3]

    left = line.split("=")[1].split(",")[0][2:]
    right = line.split("=")[1].split(",")[1][1:-1]
    positions[origin] = [left, right]

num_steps = 0

part1_start = ["AAA"]
part2_start = [node for node in positions.keys() if node.endswith("A")]

part1_res = solve(part1_start)
part2_res = solve(part2_start)

print(f"Part 1 res: {part1_res}")
print(f"Part 2 res: {part2_res}")