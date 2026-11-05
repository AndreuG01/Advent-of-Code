import sys

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0


data = {}
results = {}

for line in file_content:
    elems = line.split(" ")
    data[elems[0]] = [int(elems[3]), int(elems[6]), int(elems[-2])]
    # [distance, seconds left in current state, is flying]
    results[elems[0]] = [0, int(elems[6]), True, 0]


N = 2503

for i in range(N):
    for elem, vals in data.items():
        if results[elem][2]:
            # Flying
            results[elem][0] += vals[0]
        results[elem][1] -= 1

        if results[elem][1] == 0:
            # Switch between flying and resting
            results[elem][2] = not results[elem][2]
            results[elem][1] = vals[1] if results[elem][2] else vals[-1]
    max_val = max([vals[0] for vals in results.values()]) 
    for elem in results.values():
        if elem[0] == max_val: elem[-1] += 1
    
    
#     print(results)
part_1_res = max_val
part_2_res = max([vals[-1] for vals in results.values()])


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
