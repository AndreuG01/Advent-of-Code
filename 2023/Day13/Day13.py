import sys


file_content = open(sys.argv[1]).read().strip().splitlines()


def transpose(pattern):
    num_rows = len(pattern)
    num_cols = len(pattern[0])

    transposed_pattern = [[pattern[j][i] for j in range(num_rows)] for i in range(num_cols)]
    return transposed_pattern


def copy_and_change(pattern, target_row, target_col):
    new_pattern = []
    for i in range(len(pattern)):
        curr_row = ""
        for j in range(len(pattern[0])):
            if i == target_row and j == target_col:
                curr_row += "#" if pattern[i][j] == "." else "."
            else:
                curr_row += pattern[i][j]
        new_pattern.append(curr_row)
    
    return new_pattern

def vertical_reflection(pattern, col):
    num_rows = len(pattern)
    num_cols = len(pattern[0])

    for i in range(num_rows):
        for j in range(num_cols):
            sym_col = col * 2 + 1 - j
            
            if 0 <= sym_col < num_cols:
                if pattern[i][j] != pattern[i][sym_col]:
                    return None
    
    return col


def process_pattern(pattern, avoid=[None, None]):
    num_rows = len(pattern)
    num_cols = len(pattern[0])

    vert = None
    for col in range(num_cols - 1):
        if col != avoid[0]:
            vert = vertical_reflection(pattern, col)
            if vert is not None:
                break
    
    hor = None
    transposed_pattern = transpose(pattern)
    for row in range(num_rows - 1):
        if row != avoid[1]:
            hor = vertical_reflection(transposed_pattern, row)
            if hor is not None:
                break
    
    return [vert, hor]

def process_pattern2(pattern):
    num_rows = len(pattern)
    num_cols = len(pattern[0])

    pat = process_pattern(pattern)
    
    for i in range(num_rows):
        for j in range(num_cols):
            copy_pat = copy_and_change(pattern, i, j)

            pat2 = process_pattern(copy_pat, avoid=pat)
            if pat2 != pat and not all(elem is None for elem in pat2):
                score = compute_score(pat2)
                return score



def compute_score(pat):
    if pat[0] is not None:
        return pat[0] + 1
    else:
        return (pat[1] + 1) * 100

pattern = []
part1_res = 0
part2_res = 0
count = 0
for line in file_content:
    if line == "":
        pat = process_pattern(pattern)
        part1_res += compute_score(pat)
        part2_res  += process_pattern2(pattern)
        
        
        pattern = []
        count += 1
    else:
        pattern.append(line)

# Check last pattern
pat = process_pattern(pattern)
part1_res += compute_score(pat)
part2_res += process_pattern2(pattern)

print(f"Part 1 res: {part1_res}")
print(f"Part 2 res: {part2_res}")