import sys
from itertools import combinations
from math import prod

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

weights = [int(line) for line in file_content]


def without(weights, group):
    rest = list(weights)
    for weight in group:
        rest.remove(weight)
    return rest


def can_split(weights, num_groups, target) -> bool:
    if num_groups == 1: return sum(weights) == target
    for size in range(1, len(weights) + 1):
        for group in combinations(weights, size):
            if sum(group) == target and can_split(without(weights, group), num_groups - 1, target):
                return True
    return False


def best_entanglement(weights, num_groups) -> int:
    target = sum(weights) // num_groups
    # Sizes go up, so the first size with a valid group has the fewest packages
    for size in range(1, len(weights) + 1):
        groups = [group for group in combinations(weights, size) if sum(group) == target]
        for group in sorted(groups, key=prod):
            # The rest of the packages also have to split into equal groups
            if can_split(without(weights, group), num_groups - 1, target):
                return prod(group)


part_1_res = best_entanglement(weights, 3)
part_2_res = best_entanglement(weights, 4)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
