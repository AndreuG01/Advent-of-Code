import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

target = int(file_content)

# House n gets 10 presents from each elf that divides n, and house target // 10 + 1
# alone gets at least target presents from elf n, so the answer can't be further away
limit = target // 10 + 1
houses = [0] * (limit + 1)
for elf in range(1, limit + 1):
    for house in range(elf, limit + 1, elf):
        houses[house] += elf * 10

for house in range(1, limit + 1):
    if houses[house] >= target:
        part_1_res = house
        break

# Part 2: each elf only visits 50 houses, but leaves 11 presents per house
limit = target // 11 + 1
houses = [0] * (limit + 1)
for elf in range(1, limit + 1):
    for house in range(elf, min(elf * 50, limit) + 1, elf):
        houses[house] += elf * 11

for house in range(1, limit + 1):
    if houses[house] >= target:
        part_2_res = house
        break


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
