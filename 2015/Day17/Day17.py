import sys
from itertools import combinations

file_content = open(sys.argv[1]).read().strip().replace("\n", " ")

nums = [int(elem) for elem in file_content.split(" ")]


part_1_res = 0
part_2_res = 0

target = 25 if "example" in sys.argv[1] else 150

# combinations works by position, so two containers of the same size stay different
for size in range(1, len(nums) + 1):
    curr_res = 0
    for containers in combinations(nums, size):
        if sum(containers) == target:
            curr_res += 1
    part_1_res += curr_res

    # Part 2: sizes go up, so the first size with a match is the minimum
    if part_2_res == 0:
        part_2_res = curr_res


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
