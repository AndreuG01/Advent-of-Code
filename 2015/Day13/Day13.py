import sys
from itertools import permutations

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

# happiness[(a, b)] = how much a's happiness changes when sitting next to b
happiness = {}
people = set()
for line in file_content.splitlines():
    # e.g. "Alice would gain 54 happiness units by sitting next to Bob."
    words = line.rstrip(".").split(" ")
    person, action, amount, neighbour = words[0], words[2], int(words[3]), words[-1]
    happiness[(person, neighbour)] = amount if action == "gain" else -amount
    people.update([person, neighbour])


def total_happiness(arrangement) -> int:
    total = 0
    for i in range(len(arrangement)):
        a = arrangement[i]
        b = arrangement[(i + 1) % len(arrangement)]  # the table is round
        total += happiness[(a, b)] + happiness[(b, a)]
    return total


def best_arrangement(people) -> int:
    # The table is round, so rotations are the same seating: fix the first
    # person and only try every order of the rest
    first, *rest = sorted(people)
    return max(total_happiness([first, *order]) for order in permutations(rest))


part_1_res = best_arrangement(people)

# Part 2: add yourself, with 0 happiness towards and from everyone
for person in people:
    happiness[("Me", person)] = 0
    happiness[(person, "Me")] = 0
part_2_res = best_arrangement(people | {"Me"})


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
