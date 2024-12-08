import sys
import re

file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()


part_1_res = 0
part_2_res = 0

do_operation = True

for line in file_content:
    for match in re.findall(r"(do\(\))|(mul\((\d{1,3}),(\d{1,3})\))|(don't\(\))", line):
        if match[0]:
            do_operation = True
        elif match[1]:
            num_1 = int(match[2])
            num_2 = int(match[3])
            part_1_res += num_1 * num_2
            if do_operation: part_2_res += num_1 * num_2
        elif match[4]:
            do_operation = False
    

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")