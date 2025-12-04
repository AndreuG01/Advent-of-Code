import sys


file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()

num_rows = len(file_content)
num_cols = len(file_content[0])

positions = []

def remove(file_content):
    num_removed = 0
    for i, line in enumerate(file_content):
        for j, char in enumerate(line):
            if char == "@":
                num_paper_rolls = 0
                
                left = file_content[i][j - 1] if j > 0 else "#"
                num_paper_rolls += 1 if left == "@" else 0
                
                right = file_content[i][j + 1] if j < num_cols - 1 else "#"
                num_paper_rolls += 1 if right == "@" else 0
                
                up = file_content[i - 1][j] if i > 0 else "#"
                num_paper_rolls += 1 if up == "@" else 0
                
                down = file_content[i + 1][j] if i < num_rows - 1 else "#"
                num_paper_rolls += 1 if down == "@" else 0
                
                diagonal_ul = file_content[i - 1][j - 1] if i > 0 and j > 0 else "#"
                num_paper_rolls += 1 if diagonal_ul == "@" else 0
                
                diagonal_ur = file_content[i - 1][j + 1] if i > 0 and j < num_cols - 1 else "#"
                num_paper_rolls += 1 if diagonal_ur == "@" else 0
                
                diagonal_dl = file_content[i + 1][j - 1] if i < num_rows - 1 and j > 0 else "#"
                num_paper_rolls += 1 if diagonal_dl == "@" else 0
                
                diagonal_dr = file_content[i + 1][j + 1] if i < num_rows - 1 and j < num_cols - 1 else "#"
                num_paper_rolls += 1 if diagonal_dr == "@" else 0
                
                # print(f"{i} {j}")
                # print(f"Left: {left}")
                # print(f"right: {right}")
                # print(f"Up: {up}")
                # print(f"Down: {down}")
                # print(f"Diagonal UL: {diagonal_ul}")
                # print(f"Diagonal UR: {diagonal_ur}")
                # print(f"Diagonal DL: {diagonal_dl}")
                # print(f"Diagonal DR: {diagonal_dr}")
                # print(f"Number of adjacent paper rolls: {num_paper_rolls}")
                # print("-----")
                
                if num_paper_rolls < 4:
                    num_removed += 1
                    positions.append((i,j))
    return num_removed, positions


part_1_res = len(set(remove(file_content)[1]))


def print_file_content(file_content):
    for line in file_content:
        print(line)
    print("-----")


num_removed, positions = remove(file_content)
part_2_res = num_removed
while num_removed > 0:
    for i, j in positions:
        line_as_list = list(file_content[i])
        line_as_list[j] = "."
        file_content[i] = "".join(line_as_list)
    
    # print(f"Num removed: {num_removed}")
    # print_file_content(file_content)
    num_removed, positions = remove(file_content)
    part_2_res += num_removed

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")