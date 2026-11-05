import sys
from itertools import combinations

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

boss_hp, boss_damage, boss_armor = [int(line.split(": ")[1]) for line in file_content]

# [cost, damage, armor]
weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]


def player_wins(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor) -> bool:
    while True:
        boss_hp -= max(1, player_damage - boss_armor)
        if boss_hp <= 0: return True
        player_hp -= max(1, boss_damage - player_armor)
        if player_hp <= 0: return False


def loadouts():
    # Exactly 1 weapon, 0 or 1 armor, 0 to 2 rings
    armor_options = [[]] + [[armor] for armor in armors]
    ring_options = [[]] + [[ring] for ring in rings] + [list(pair) for pair in combinations(rings, 2)]
    for weapon in weapons:
        for armor in armor_options:
            for ring in ring_options:
                yield [weapon] + armor + ring


costs = []
losing_costs = []
for items in loadouts():
    cost = sum([item[0] for item in items])
    damage = sum([item[1] for item in items])
    armor = sum([item[2] for item in items])
    if player_wins(100, damage, armor, boss_hp, boss_damage, boss_armor):
        costs.append(cost)
    else:
        losing_costs.append(cost)

part_1_res = min(costs)
part_2_res = max(losing_costs)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
