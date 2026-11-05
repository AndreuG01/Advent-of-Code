import sys
from collections import defaultdict
from itertools import combinations

file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

connections = defaultdict(set)
for line in file_content:
    a, b = line.split("-")
    connections[a].add(b)
    connections[b].add(a)

# For every computer, any two of its neighbours that are also connected to
# each other form a triangle with it. Storing them sorted removes the
# duplicates found from each of the three corners.
triangles = set()
for computer, neighbours in connections.items():
    for a, b in combinations(neighbours, 2):
        if b in connections[a]:
            triangles.add(tuple(sorted((computer, a, b))))

print(f"Sets of three: {len(triangles)}")

part_1_res = sum(any(name.startswith("t") for name in triangle) for triangle in triangles)
print(f"Part 1 res: {part_1_res}")

# Part 2: the LAN party is the largest group where everyone is connected to
# everyone else (the maximum clique). Bron-Kerbosch builds every maximal group
# by extending the current one with candidates connected to all its members.
# Picking a pivot avoids trying candidates that would only lead to groups
# already found through the pivot.
def bron_kerbosch(group: set, candidates: set, excluded: set, cliques: list):
    if not candidates and not excluded:
        cliques.append(group)
        return
    pivot = max(candidates | excluded, key=lambda node: len(connections[node] & candidates))
    for node in list(candidates - connections[pivot]):
        bron_kerbosch(group | {node}, candidates & connections[node], excluded & connections[node], cliques)
        candidates.remove(node)
        excluded.add(node)


cliques = []
bron_kerbosch(set(), set(connections), set(), cliques)
lan_party = max(cliques, key=len)

part_2_res = ",".join(sorted(lan_party))
print(f"Part 2 res: {part_2_res}")
