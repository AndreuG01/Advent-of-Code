import sys

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

for elem in file_content:
    elem = elem.split("x")
    l = int(elem[0])
    w = int(elem[1])
    h = int(elem[2])
    
    a_side_1 = l*w
    a_side_2 = w*h
    a_side_3 = h*l
    
    p_side_1 = 2*l + 2*w
    p_side_2 = 2*w + 2*h
    p_side_3 = 2*h + 2*l
    
    
    part_1_res += 2*a_side_1 + 2*a_side_2 + 2*a_side_3 + min(a_side_2, a_side_1, a_side_3)
    part_2_res += min(p_side_1, p_side_2, p_side_3) + l * w * h


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
