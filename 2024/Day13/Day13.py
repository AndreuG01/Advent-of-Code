import sys
file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()
file_content.append("")

# print(file_content)

def solve(a1, b1, a2, b2, A, B):
    x = (b1 * B - b2 * A) / (b1 * a2 - b2 * a1)
    y = (A - a1 * x) / b1
    if x % 1 == 0.0 and y % 1 == 0.0:
        return int(x), int(y)
    return 0, 0

total_lines = len(file_content)
part_1_res = 0
part_2_res = 0
for i, line in enumerate(file_content):
    start = line[:8]
    
    if line == "" or i == total_lines - 1:
        x, y = solve(a1, b1, a2, b2, A, B)
        part_1_res += x * 3 + y
        new_x, new_y = solve(a1, b1, a2, b2, A_b, B_b)
        part_2_res += new_x * 3 + new_y
        # print(A / (a1 + b1))
        continue
    
    if start == "Button A":
        vals = line.split(" ")
        a1 = int(vals[2][2:-1])
        a2 = int(vals[3][2:])
    elif start == "Button B":
        vals = line.split(" ")
        b1 = int(vals[2][2:-1])
        b2 = int(vals[3][2:])
    elif start == "Prize: X":
        vals = line.split(" ")
        A = int(vals[1][2:-1])
        B = int(vals[2][2:])
        
        A_b = A + 10000000000000
        B_b = B + 10000000000000

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")