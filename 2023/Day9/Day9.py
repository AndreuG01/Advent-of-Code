import sys

file_content = open(sys.argv[1]).read().strip().splitlines()


part1_res = 0
part2_res = 0

for line in file_content:
    nums = [int(val) for val in line.split(" ")]
    sequences = []
    sequences.append(nums)
    while not all([num == 0 for num in sequences[-1]]):
        curr = []
        for i in range(1, len(sequences[-1])):
            curr.append(sequences[-1][i] - sequences[-1][i - 1])
        sequences.append(curr)
    
    # Extrapolating forwards
    sequences[-1].append(0)    
    for i in range(len(sequences) - 1):
        sequences[-i -2][-1] = sequences[-i - 1][-1] + sequences[-i -2][-1]
        
    part1_res += sequences[0][-1]
    
    # Extrapolating backwards
    sequences[-1].insert(0, 0)
    for i in range(len(sequences) - 1):
        sequences[-i - 2][0] = sequences[-i -2][0] - sequences[-i -1][0]

    part2_res += sequences[0][0]

print(f"Part 1 res: {part1_res}")
print(f"Part 2 res: {part2_res}")