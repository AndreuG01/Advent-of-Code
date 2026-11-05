import sys

file_content = open(sys.argv[1]).read().splitlines()


part_1_res = 0
part_2_res = 0
points = {}
points_2 = {}

for line in file_content:
    elems = line.split(" ")
    if len(elems) == 4:
        # Toggle
        action = "toggle"
        nums_f = elems[1].split(",")
        nums_t = elems[3].split(",")
        f_x, f_y = int(nums_f[0]), int(nums_f[1])
        t_x, t_y = int(nums_t[0]), int(nums_t[1])
        
    else:
        action = elems[1]
        nums_f = elems[2].split(",")
        nums_t = elems[4].split(",")
        f_x, f_y = int(nums_f[0]), int(nums_f[1])
        t_x, t_y = int(nums_t[0]), int(nums_t[1])

    for x in range(f_x, t_x + 1):
        for y in range(f_y, t_y + 1):
            if action == "off":
                points[(x, y)] = 0
                if (x, y) in points_2: points_2[(x, y)] = max(0, points_2[(x, y)] - 1)
                else: points_2[(x, y)] = 0
            elif action == "on":
                points[(x, y)] = 1
                if (x, y) in points_2: points_2[(x, y)] += 1
                else: points_2[(x, y)] = 1
            else:
                if (x,y) in points and points[(x, y)] == 1: points[(x, y)] = 0
                else: points[(x, y)] = 1
                
                if (x,y) in points_2: points_2[(x, y)] += 2
                else: points_2[(x, y)] = 2
                

part_1_res = sum(list(points.values()))
part_2_res = sum(list(points_2.values()))

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
