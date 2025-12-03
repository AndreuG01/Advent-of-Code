import sys
import math

file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()



dial = 50

part_1_res = 0
part_2_res = 0

for line in file_content:
    direction = line[0]
    rotation = int(line[1:])
    
    old = dial

    if direction == "L":
        dial -= rotation
        if dial == 0:
            part_2_res += 1
        if dial < 0:
            if old != 0:
                part_2_res += 1
            part_2_res += math.floor(abs(rotation - old) / 100)
    else:
        dial += rotation
        part_2_res += math.floor(dial / 100)

    dial %= 100

    if dial == 0:
        part_1_res += 1

    
print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
