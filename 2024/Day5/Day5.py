import sys
from collections import deque, defaultdict
file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()

rules_after = defaultdict(set)
rules_before = defaultdict(set)


part_1_res = 0
part_2_res = 0

def part_2(line: list[str], rules_before, rules_after):
    good_sorting = [] # Reversed
    queue = deque([])
    mapping = {}
    for v in line:
        mapping[v] = len(rules_before[v] & set(line))
    
    
    for elem in line:
        if mapping[elem] == 0:
            queue.append(elem)
    while queue:
        curr = queue.popleft()
        good_sorting.append(curr)
        for val in rules_after[curr]:
            if val in mapping:
                mapping[val] -= 1
                if mapping[val] == 0:
                    queue.append(val)
            
    return int(good_sorting[len(good_sorting) // 2])

def part_1(line: list[str], rules_before):
    for i in range(len(line)):
        elem = line[i]
        if elem in rules_before:
            if len(list(set(line[:i]) & set(rules_before[elem]))) > 0:
                return 0
            
    return int(line[len(line) // 2])

adding_rules = True
for line in file_content:
    if line == "":
        adding_rules = False


        continue
    if adding_rules:
        x, y = line.split("|")
        rules_before[x].add(y)
        rules_after[y].add(x)
            
            
    else:
        res = part_1(line.split(","), rules_before)
        part_1_res += res
        if res == 0:
            part_2_res += part_2(line.split(","), rules_before, rules_after)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")

