import sys
from itertools import permutations

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

# Distances work both ways, so store each pair in both directions
distances = {}
cities = set()
for line in file_content.splitlines():
    route, dist = line.split(" = ")
    a, b = route.split(" to ")
    distances[(a, b)] = int(dist)
    distances[(b, a)] = int(dist)
    cities.update([a, b])

# Few cities (8! = 40320 orders), so trying every order is fast enough
route_lengths = [
    sum(distances[(route[i], route[i + 1])] for i in range(len(route) - 1))
    for route in permutations(cities)
]

part_1_res = min(route_lengths)
part_2_res = max(route_lengths)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
