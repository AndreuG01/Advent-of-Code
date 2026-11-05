import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0


def look_and_say(s: str) -> str:
    count = 1
    val = s[0]
    new_str = []
    for i in range(1, len(s)):
        if s[i] == val:
            count += 1
        else:
            new_str.append(f"{count}{val}")
            count = 1
        val = s[i]
    new_str.append(f"{count}{val}")
    return "".join(new_str)


seq = file_content
for i in range(50):
    seq = look_and_say(seq)
    if i == 39:
        part_1_res = len(seq)
part_2_res = len(seq)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
