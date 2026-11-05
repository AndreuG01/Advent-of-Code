import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0
part_2_done = False

for i, char in enumerate(file_content, start=1):
    if char == "(": part_1_res += 1
    else: part_1_res -= 1
    if part_1_res == -1 and not part_2_done:
        part_2_res = i
        part_2_done = True
    

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
