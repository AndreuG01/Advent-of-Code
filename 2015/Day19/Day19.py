import sys
import random

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

rules, molecule = file_content.split("\n\n")
replacements = [line.split(" => ") for line in rules.splitlines()]

molecules = set()
for source, target in replacements:
    i = molecule.find(source)
    while i != -1:
        molecules.add(molecule[:i] + target + molecule[i + len(source):])
        i = molecule.find(source, i + 1)

part_1_res = len(molecules)


def fewest_steps(molecule) -> int:
    # Work backwards from the molecule to "e". Every way down takes the same number
    # of steps, but a greedy path can get stuck, so restart with a new order if it does
    rules = list(replacements)
    while True:
        random.shuffle(rules)
        curr = molecule
        steps = 0
        changed = True
        while curr != "e" and changed:
            changed = False
            for source, target in rules:
                if target in curr:
                    curr = curr.replace(target, source, 1)
                    steps += 1
                    changed = True
                    break
        if curr == "e": return steps


part_2_res = fewest_steps(molecule)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
