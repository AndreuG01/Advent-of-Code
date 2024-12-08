import sys
from collections import Counter

file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()

dims = len(file_content)



part_1_res = 0
part_2_res = 0


def part_1(content):
    target = "XMAS"
    target_reverse = "SAMX"
    num_rows = len(content)
    num_cols = len(content[0])
    offset = len(target)
    res = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if j <= num_cols - offset:
                cont = content[i][j:j+offset]
                if target == cont:
                    res += 1
            if j >= (offset - 1):
                if target_reverse == content[i][j-(offset - 1):j+1]:
                    res += 1
            if i <= num_rows - offset:
                if target == "".join([content[tmp][j] for tmp in range(i, i+offset)]):
                    res += 1
            if i >= (offset - 1):
                if target_reverse == "".join([content[tmp][j] for tmp in range(i-(offset - 1), i+1)]):
                    res += 1
                
            if i >= (offset - 1) and j >= (offset - 1):
                cont = "".join([content[i-tmp][j-tmp] for tmp in range(offset)])
                # Check upper left diagonal
                if target == cont:
                    res += 1
                # Check bottom right diagonal
                if target_reverse == cont:
                    res += 1    
            
            if i <= num_rows - offset and j >= (offset - 1):
                cont = "".join([content[i+tmp][j-tmp] for tmp in range(offset)])
                # Check bottom left diagonal
                if target == cont:
                    res += 1
                # Check upper right left diagonal
                if target_reverse == cont:
                    res += 1
    
    
    return res

def part_2(content):
    target = "SAM"
    target_reverse = "MAS"
    num_rows = len(content)
    num_cols = len(content[0])
    offset = len(target)
    mid_positions = []
    for i in range(num_rows):
        for j in range(num_cols):
            if i >= (offset - 1) and j >= (offset - 1):
                cont = "".join([content[i-tmp][j-tmp] for tmp in range(offset)])
                # Check upper left diagonal
                if target == cont:
                    mid_positions.append([(i-tmp, j-tmp) for tmp in range(offset)][1])
                # Check bottom right diagonal
                if target_reverse == cont:
                    mid_positions.append([(i-tmp, j-tmp) for tmp in range(offset)][1])
            
            if i <= num_rows - offset and j >= (offset - 1):
                cont = "".join([content[i+tmp][j-tmp] for tmp in range(offset)])
                # Check bottom left diagonal
                if target == cont:
                    mid_positions.append([(i+tmp, j-tmp) for tmp in range(offset)][1])
                # Check upper right left diagonal
                if target_reverse == cont:
                    mid_positions.append([(i+tmp, j-tmp) for tmp in range(offset)][1])
    
    count = Counter(mid_positions)
    
    return len([elem for elem in count.values() if elem > 1])




part_1_res = part_1(file_content)
part_2_res = part_2(file_content)

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")