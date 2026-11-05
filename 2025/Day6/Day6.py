import sys
import re
import math


num_regex = re.compile(r'(\d+)')
op_regex = re.compile(r'(\*|\+)')

file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()


results = [int(match.group(1)) for match in re.finditer(num_regex, file_content[0])]
operators = [match.group(1) for match in re.finditer(op_regex, file_content[-1])]
print(results)
print(operators)


for line in file_content[1:-1]:
    nums = [int(match.group(1)) for match in re.finditer(num_regex, line)]
    if len(nums) != len(results):
        print("Error: Number of results does not match number of operators.")
        sys.exit(1)
    
    for i, num in enumerate(nums):
        if operators[i] == '+':
            results[i] += num
        elif operators[i] == '*':
            results[i] *= num
            
part_1_res = sum(results)

print(f"Part 1 res: {part_1_res}")

# Part 2: cephalopod math is read in columns. Each column of a problem is one
# number (most significant digit on top), so the original spacing matters and
# the lines can't be stripped.
raw_lines = open(sys.argv[1]).read().split("\n")
raw_lines = [line for line in raw_lines if line.strip()]
width = max(len(line) for line in raw_lines)
raw_lines = [line.ljust(width) for line in raw_lines]
digit_rows, op_row = raw_lines[:-1], raw_lines[-1]


def solve_problem(columns: list[int]) -> int:
    nums = []
    op = None
    for col in columns:
        digits = "".join(row[col] for row in digit_rows).strip()
        if digits:
            nums.append(int(digits))
        if op_row[col] in "+*":
            op = op_row[col]
    return sum(nums) if op == "+" else math.prod(nums)


part_2_res = 0
current = []
for col in range(width):
    if all(line[col] == " " for line in raw_lines):
        if current:
            part_2_res += solve_problem(current)
        current = []
    else:
        current.append(col)
if current:
    part_2_res += solve_problem(current)

print(f"Part 2 res: {part_2_res}")
