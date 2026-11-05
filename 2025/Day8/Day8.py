import sys
import re
import numpy as np


def distance(a: tuple[int, int, int], b: tuple[int, int, int]):
    x_a, y_a, z_a = a
    x_b, y_b, z_b = b
    return ((x_b - x_a) ** 2 + (y_b - y_a) ** 2 + (z_b - z_a) ** 2) ** 0.5

def proces_line(elem: str):
    return tuple([int(num) for num in elem.split(",")])



file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

# Create a triangular distance matrix to store the distances between each pair of points
dist_matrix = np.zeros((len(file_content), len(file_content)))    


for i in range(len(file_content)):
    for j in range(i + 1, len(file_content)):
        dist_matrix[i][j] = distance(proces_line(file_content[i]), proces_line(file_content[j]))

# Get the N smallest distances and the indices of the points that produced them
# The example connects the 10 closest pairs, the real input the 1000 closest
N = 10 if len(file_content) <= 20 else 1000

# Mask the diagonal and lower triangle so they are never picked as a minimum
dist_matrix[np.tril_indices(len(file_content))] = np.inf

flat_indices = np.argsort(dist_matrix, axis=None)[:N]
smallest = [
    (dist_matrix.flat[idx], *np.unravel_index(idx, dist_matrix.shape))
    for idx in flat_indices
]

pairs = [(int(i), int(j)) for _, i, j in smallest]
print(pairs)

for dist, i, j in smallest:
    print(f"Distance {dist:.2f} between points {i} and {j}")

# Connect the pairs into groups: a pair joins any group that already contains
# one of its points, and joins two groups together if they each contain one
groups = []
for i, j in pairs:
    group_i = next((group for group in groups if i in group), None)
    group_j = next((group for group in groups if j in group), None)

    if group_i is None and group_j is None:
        groups.append({i, j})
    elif group_i is not None and group_j is None:
        group_i.add(j)
    elif group_j is not None and group_i is None:
        group_j.add(i)
    elif group_i is not group_j:
        group_i |= group_j
        groups.remove(group_j)

print(groups)

# Sort the groups by size
groups.sort(key=len, reverse=True)

TOP_N = 3
groups = groups[:TOP_N]
sizes = [len(group) for group in groups]
part_1_res = np.prod(sizes)
print(f"Part 1 res: {part_1_res}")

# Part 2: keep connecting the closest pairs (this time all of them, not just
# the N closest) until every junction box ends up in a single circuit
points = [proces_line(line) for line in file_content]

parent = list(range(len(points)))
size = [1] * len(points)

def find(x: int) -> int:
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x: int, y: int) -> bool:
    x, y = find(x), find(y)
    if x == y:
        return False
    if size[x] < size[y]:
        x, y = y, x
    parent[y] = x
    size[x] += size[y]
    return True

all_flat_indices = np.argsort(dist_matrix, axis=None)

num_circuits = len(points)
for idx in all_flat_indices:
    i, j = (int(k) for k in np.unravel_index(idx, dist_matrix.shape))
    if union(i, j):
        num_circuits -= 1
        if num_circuits == 1:
            break

part_2_res = points[i][0] * points[j][0]
print(f"Final connection between points {i} and {j}")
print(f"Part 2 res: {part_2_res}")
