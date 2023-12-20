import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0

for line in file_content.splitlines():
    split_1 = line.split(":")
    
    nums = split_1[1].split("|")
    win_nums = nums[0].split(" ")
    my_nums = nums[1].split(" ")
    
    win_nums = [num for num in win_nums if num != ""]
    my_nums = [num for num in my_nums if num != ""]
    
    points = len([num for num in my_nums if num in win_nums])
    if points > 0:
        part_1_res += 2 ** (points - 1)
    
print(f"Part 1 res: {part_1_res}")