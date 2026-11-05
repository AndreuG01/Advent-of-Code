import sys

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

elems = [
    "children",
    "cats",
    "samoyeds",
    "pomeranians",
    "akitas",
    "vizslas",
    "goldfish",
    "trees",
    "cars",
    "perfumes"
]


target = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

for i, line in enumerate(file_content, start=1):
    line = line.replace(":", "")
    line = line.replace(",", "")
    parts = line.split(" ")[2:]
    idx = 0
    matches = True
    matches_2 = True
    while idx < len(parts):
        detect = parts[idx]
        val = int(parts[idx+1])
        expected = target[elems.index(detect)]
        if expected != val:
            matches = False

        # Part 2: cats and trees are lower bounds, pomeranians and goldfish upper bounds
        if detect in ["cats", "trees"]:
            if val <= expected: matches_2 = False
        elif detect in ["pomeranians", "goldfish"]:
            if val >= expected: matches_2 = False
        elif expected != val:
            matches_2 = False
        idx += 2
    if matches:
        part_1_res = i
    if matches_2:
        part_2_res = i



print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
