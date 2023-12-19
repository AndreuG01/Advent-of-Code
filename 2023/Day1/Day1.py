import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in file_content.splitlines():
    nums_1 = []
    nums_2 = []
    for (pos, char) in enumerate(line):
        if char.isdigit():
            nums_1.append(char)
            nums_2.append(char)
        
        for (digit, val) in enumerate(digits):
            if line[pos:].startswith(val):
                nums_2.append(str(digit + 1))
        
        
    part_1_res += int(nums_1[0] + nums_1[-1])
    part_2_res += int(nums_2[0] + nums_2[-1])


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
