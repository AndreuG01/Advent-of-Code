import sys
file_content = open(sys.argv[1]).read().strip()


def get_slots(dots_list):
    result = []
    i = 0

    while i < len(dots_list):
        if dots_list[i] == ".":
            start = i
            count = 0
            while i < len(dots_list) and dots_list[i] == ".":
                count += 1
                i += 1
            result.append([start, count])
        else:
            i += 1
    return result

def part_1(nums: list, dots: list, final_str):
    nums_start_idx = 0
    nums_end_idx = len(nums) - 1
    part_1_res = 0
    for i in range(len(dots) + len(nums)):
        if nums_start_idx > nums_end_idx: break
        if i in nums:
            curr_char = final_str[nums[nums_start_idx]]
            nums_start_idx += 1
        else:
            curr_char = final_str[nums[nums_end_idx]]
            nums_end_idx -= 1
        part_1_res += i * int(curr_char)
    
    return part_1_res


def part_2(final_str, slots_available: list, nums_available: list):
    new_str = final_str.copy()
    for i in range(len(nums_available) - 1, -1, -1):
        curr_num = nums_available[i]
        for j in range(len(slots_available)):
            curr_slot = slots_available[j]
            if curr_slot == [0, 0]: continue
            if curr_num[0] <= curr_slot[0]: break
            if curr_num[1] <= curr_slot[1]:
                add_num = new_str[curr_num[0]]
                for tmp in range(curr_num[1]):
                    new_str[curr_slot[0] + tmp] = add_num
                    new_str[curr_num[0] + tmp] = "."
                if curr_num[1] == curr_slot[1]:
                    slots_available[j] = [0, 0]
                else:  
                    slots_available[j][0] += curr_num[1]
                    slots_available[j][1] -= curr_num[1]
                    slots_available.append(curr_num)
                break
    
    part_2_res = 0
    for i, elem in enumerate(new_str):
        if elem != ".":
            part_2_res += i * int(elem)
    return part_2_res


file_content = file_content.splitlines()[0]
final_str = []
count = 0
count_1 = 0
count_2 = 0
dots = []
nums = []
for i, num in enumerate(file_content):
    if i % 2 == 0:
        final_str += [str(count) for _ in range(int(num))]
        count += 1
        nums.append([count_1 + j for j in range(int(num))])
    else:
        final_str += ["." for _ in range(int(num))]
        dots.append([count_2 + j for j in range(int(num))])
    count_1 += int(num)
    count_2 += int(num)

dots = [x for xs in dots for x in xs]


slots_available = get_slots(final_str)

nums_available = []
count = 0
start = 0

for i in range(len(final_str)):
    if final_str[i] != "." and (i == 0 or final_str[i] == final_str[i - 1]):
        if count == 0:
            start = i
        count += 1
    elif final_str[i] != ".":
        nums_available.append([start, count])
        start = i
        count = 1
if count:
    nums_available.append([start, count])


nums = [x for xs in nums for x in xs]

part_1_res = part_1(nums, dots, final_str)
print(f"Part 1 res: {part_1_res}")

part_2_res = part_2(final_str, slots_available, nums_available)
print(f"Part 2 res: {part_2_res}")
