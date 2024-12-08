import sys
import bisect
from collections import Counter

file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()


part_1_res = 0
part_2_res = 0

left_nums = []
right_nums = []

for line in file_content:
    parsed_line = line.split(" ")
    parsed_line.remove("")
    num_left = int(parsed_line[0])
    num_right = int(parsed_line[-1])
    
    bisect.insort(left_nums, num_left)
    bisect.insort(right_nums, num_right)

right_counter = Counter(right_nums)

part_1_res = sum([abs(right - left) for right, left in zip(left_nums, right_nums)])
part_2_res = sum([num * right_counter[num] if num in right_counter else 0 for num in left_nums])

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")