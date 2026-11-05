import sys


file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()[0]


def part_1(file_content):
    part_1_string = []
    part_1_res = 0
    for line in file_content.split(","):
        num_1, num_2 = line.split("-")
        num_1 = int(num_1)
        num_2 = int(num_2)
        
        for i in range(num_1, num_2 + 1):
            num = str(i)
            if len(num) % 2 != 0: continue
            middle = len(num) // 2
            if num[:middle] == num[middle:]:
                part_1_res += i
                part_1_string.append(num)
    
    return part_1_res, part_1_string

import re
def part_2(file_content):
    part_2_res = 0
    part_2_string = []
    # (\d+)\1+
    for line in file_content.split(","):
        num_1, num_2 = line.split("-")
        num_1 = int(num_1)
        num_2 = int(num_2)
        
        for i in range(num_1, num_2 + 1):
            num = str(i)
            # Try with regex later
            matches = re.fullmatch(r"(\d+)\1+", num)
            if matches is not None:
                part_2_res += i
                part_2_string.append(num)
            
            # if len(matches) < 1: continue
            
            # first_match = matches[0]
            # print(f"matches: {matches}")
            # num_repetitions = len(num) / len(first_match)
            # print(f"num_repetitions: {num_repetitions}")
            # repeated_match = first_match * num_repetitions
            # # print(repeated_match, num)
            # if repeated_match == num:
            #     part_2_res += i
            #     part_2_string.append(num)
            # print(f"first match: {first_match}")
        # break
    return part_2_res, part_2_string

part_1_res, part_1_string = part_1(file_content)
part_2_res, part_2_string = part_2(file_content)

print(part_2_string)
            
print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
    