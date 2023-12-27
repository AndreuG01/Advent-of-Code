import sys

def compute_combinations(times, distances):
    comb = []
    for i, time in enumerate(times):
        combinations = 0
        for j in range(time + 1):
            if j * (time - j) > distances[i]:
                combinations += 1
        comb.append(combinations)
    
    return comb



file_content = open(sys.argv[1]).read().strip().splitlines()

# Times for part 1
times = [time for time in file_content[0].split(" ") if time != ""]
times = times[1:]
times_part1 = [int(time) for time in times]


# Times for part 2
time_part2 = [""]
for time in times:
    time_part2[0] += time
time_part2[0] = int(time_part2[0])




# Distances for part 1
distances = [dist for dist in file_content[1].split(" ") if dist != ""]
distances = distances[1:]
distances_part1 = [int(dist) for dist in distances]


# Distances for part 2
distance_part2 = [""]
for dist in distances:
    distance_part2[0] += dist
distance_part2[0] = int(distance_part2[0])



part1_comb = compute_combinations(times_part1, distances_part1)
part2_comb = compute_combinations(time_part2, distance_part2)

part1_res = part1_comb[0]
part2_res = part2_comb[0]

for comb in range(1, len(part1_comb)):
    part1_res *= part1_comb[comb]

for comb in range(1, len(part2_comb)):
    part2_res *= part2_comb[comb]

print(f"Part 1 res: {part1_res}")
print(f"Part 2 res: {part2_res}")
