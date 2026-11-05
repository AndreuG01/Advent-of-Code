import sys
import re

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

row, col = [int(num) for num in re.findall(r"\d+", file_content)]

# Codes fill the grid by diagonals: (row, col) is on diagonal row + col - 1,
# and all the diagonals before it hold 1 + 2 + ... + (diagonal - 1) codes
diagonal = row + col - 1
position = diagonal * (diagonal - 1) // 2 + col

code = 20151125
for _ in range(position - 1):
    code = code * 252533 % 33554393

part_1_res = code


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
