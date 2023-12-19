import sys
import re

def is_part(char):
    return char != "." and not char.isdigit()



file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()

num_cols = len(file_content[0])
num_rows = len(file_content)

part_1_res = 0
part_2_res = 0

def add_gear_info(char, number, i, j, gear_info):
    if char == "*":
        one_dim_idx = i * num_cols + j
        if one_dim_idx not in gear_info:
            gear_info[one_dim_idx] = [number]
        else:
            gear_info[one_dim_idx].append(number)
    
    
gear_info = {}

for i, line in enumerate(file_content):
    matches = re.finditer("\d+", line)
    for curr_match in matches:
        start = curr_match.start()
        end = curr_match.end() - 1
        num = int(curr_match.group())
        is_part_number = False
        
        # 1. There is a symbol above or below the number (all accross the number)
        for j in range(start, end + 1):
            if i + 1 < num_rows:
                sym = file_content[i + 1][j]
                is_part_number = is_part_number or is_part(sym)
                add_gear_info(sym, num, i + 1, j, gear_info)
            if i - 1 >= 0:
                sym = file_content[i - 1][j]
                is_part_number = is_part_number or is_part(sym)
                add_gear_info(sym, num, i - 1, j, gear_info)
                    
            
        # 2. There is a symbol to the left or right of the number
        if start - 1 >= 0:
            sym = file_content[i][start - 1]
            is_part_number = is_part_number or is_part(sym)
            add_gear_info(sym, num, i, start - 1, gear_info)
            
        if end + 1 < num_cols:
            sym = file_content[i][end + 1]
            is_part_number = is_part_number or is_part(sym)
            add_gear_info(sym, num, i, end + 1, gear_info)
                
            
        # 3. There is a symbol in some of the diagonal positions (both on the top and below)
        if i - 1 >= 0 and start - 1 >= 0:
            sym = file_content[i - 1][start - 1]
            is_part_number = is_part_number or is_part(sym) # Top left
            add_gear_info(sym, num, i - 1, start - 1, gear_info)
                
        if i + 1 < num_rows and end + 1 < num_cols:
            sym = file_content[i + 1][end + 1]
            is_part_number = is_part_number or is_part(sym) # Bottom right
            add_gear_info(sym, num, i + 1, end + 1, gear_info)
                
        if i - i >= 0 and end + 1 < num_cols:
            sym = file_content[i - 1][end + 1]
            is_part_number = is_part_number or is_part(sym) # Top right
            add_gear_info(sym, num, i - 1, end + 1, gear_info)
                
        if i + 1 < num_rows and start - 1 >= 0:
            sym = file_content[i + 1][start - 1]
            is_part_number = is_part_number or is_part(sym) # Bottom left
            add_gear_info(sym, num, i + 1, start - 1, gear_info)
                
        
        if is_part_number:
            part_1_res += num

print(gear_info)

for key, val in gear_info.items():
    if len(val) == 2:
        part_2_res += val[0] * val[1]
    
print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")