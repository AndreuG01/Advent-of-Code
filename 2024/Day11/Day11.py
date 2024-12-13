import sys


file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()[0]

stones = file_content.split(" ")

all_splits = {} # (x, y) = num_stones --> num_stones generated if stone with id x is splitted y times
def recursive_solve(stone: str, num_times: int):
    global all_splits
    length_stone = len(stone)
    if (stone, num_times) in all_splits:
        return all_splits[(stone, num_times)]
    if num_times == 0:
        res = 1
    elif stone == "0":
        res = recursive_solve("1", num_times - 1)
    elif len(stone) % 2 == 0:
        res  = recursive_solve(str(int(stone[:length_stone // 2])), num_times - 1) + recursive_solve(str(int(stone[length_stone // 2:])), num_times - 1)
    else:
        res = recursive_solve(str(int(stone) * 2024), num_times - 1)
    
    all_splits[(stone, num_times)] = res
    return res
    
    
res_1 = []
res_2 = []
for stone in stones:
    res_1.append(recursive_solve(stone, 25))
    res_2.append(recursive_solve(stone, 75))

        
part_1_res = sum(res_1)
part_2_res = sum(res_2)

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")