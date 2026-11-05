import sys

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

def combinations_sum(num_elems, total=100):
    if num_elems == 1:
        # The last value has to be whatever is left
        yield (total,)
        return
    for first in range(total + 1):
        for rest in combinations_sum(num_elems - 1, total - first):
            yield (first,) + rest

num_elems = len(file_content)

multipliers = [[],[],[],[]]
calories = []

for line in file_content:
    splited_elems = line.split(" ")
    cap, d, f, t, cal = splited_elems[2][:-1], splited_elems[4][:-1], splited_elems[6][:-1], splited_elems[8][:-1], splited_elems[10]
    multipliers[0].append(int(cap))
    multipliers[1].append(int(d))
    multipliers[2].append(int(f))
    multipliers[3].append(int(t))
    calories.append(int(cal))


results = []
results_2 = []
for amounts in combinations_sum(num_elems):
    curr_res = 1
    for prop in multipliers:
        # print(sum([prop[i] * amounts[i] for i in range(len(prop))]))
        if sum([prop[i] * amounts[i] for i in range(len(prop))]) < 0:
            curr_res *= 0
        else: curr_res *= sum([prop[i] * amounts[i] for i in range(len(prop))])
    results.append(curr_res)
    # Part 2: only cookies with exactly 500 calories
    if sum([calories[i] * amounts[i] for i in range(len(calories))]) == 500:
        results_2.append(curr_res)

part_1_res = max(results)
part_2_res = max(results_2)
print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
