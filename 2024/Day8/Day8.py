import sys
file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()

def in_bounds(x, y, max_x, max_y):
    return x >= 0 and x <= max_x and y >= 0 and y <= max_y


antennas = {}
max_x = len(file_content) - 1
max_y = len(file_content[0]) - 1

part_1_res = 0
part_2_res = 0

for x, line in enumerate(file_content):
    for y, character in enumerate(line):
        if character != ".":
            if character not in antennas:
                antennas[character] = [(x, y)]
            else:
                antennas[character].append((x, y))
                
num_generate = len(file_content)
antinodes_1 = []
antinodes_2 = []
for char, vals in antennas.items():
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            x1, y1 = vals[i]
            x2, y2 = vals[j]
            offset_x = abs(x2 - x1)
            offset_y = abs(y2 - y1)
            if offset_x == 0:
                slope = 0
            else:
                slope = (y2 - y1) / (x2 - x1)
            
            if slope < 0:
                # Point 1 to the right of point 2
                antinode_1 = (x1 - offset_x, y1 + offset_y)
                antinode_2 = (x2 + offset_x, y2 - offset_y)
                
                for t in range(num_generate):
                    tmp1 = (x1 - offset_x * t, y1 + offset_y * t)
                    tmp2 = (x2 + offset_x * t, y2 - offset_y * t)
                    if in_bounds(tmp1[0], tmp1[1], max_x, max_y):
                        antinodes_2.append(tmp1)
                    if in_bounds(tmp2[0], tmp2[1], max_x, max_y):
                        antinodes_2.append(tmp2)
                
            elif slope > 0:
                # Point 1 to the left of point 2
                antinode_1 = (x1 - offset_x, y1 - offset_y)
                antinode_2 = (x2 + offset_x, y2 + offset_y)
                for t in range(num_generate):
                    tmp1 = (x1 - offset_x * t, y1 - offset_y * t)
                    tmp2 = (x2 + offset_x * t, y2 + offset_y * t)
                    if in_bounds(tmp1[0], tmp1[1], max_x, max_y):
                        antinodes_2.append(tmp1)
                    if in_bounds(tmp2[0], tmp2[1], max_x, max_y):
                        antinodes_2.append(tmp2)
                    
            if in_bounds(antinode_1[0], antinode_1[1], max_x, max_y):
                antinodes_1.append(antinode_1)
            if in_bounds(antinode_2[0], antinode_2[1], max_x, max_y):
                antinodes_1.append(antinode_2)
            

part_1_res = len(set(antinodes_1))
part_2_res = len(set(antinodes_2))

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
