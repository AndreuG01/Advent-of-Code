import sys
import hashlib

file_content = open(sys.argv[1]).read().strip()

part_1_done = False
count = 1
while True:
    res = hashlib.md5(f"{file_content}{count}".encode())
    res_str = res.hexdigest()
    # print(res_str)
    if res_str.startswith("00000") and not part_1_done:
        part_1_res = count
        part_1_done = True
    if res_str.startswith("000000"):
        part_2_res = count
        break
    count += 1


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
