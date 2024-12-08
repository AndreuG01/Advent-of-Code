import sys

file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()


part_1_res = 0
part_2_res = 0

def is_valid_1(nums: list[int]):
    differences = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    # Valid if all increasing or decreasing, that is, all differences are positive or negative
    if not (all([diff > 0 for diff in differences]) or all([diff < 0 for diff in differences])): return False
    
    return all([abs(diff) >= 1 and abs(diff) <= 3 for diff in differences])


def is_valid_2(nums: list[int]):
    for i in range(len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i != j:
                tmp.append(nums[j])
        if is_valid_1(tmp): return True
    return False


for line in file_content:
    line_nums = [int(num) for num in line.split()]
    if is_valid_1(line_nums): part_1_res += 1
    if is_valid_2(line_nums): part_2_res += 1
    
    
    
print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")