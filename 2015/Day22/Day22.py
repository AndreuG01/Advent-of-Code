import sys
import heapq

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

boss_hp, boss_damage = [int(line.split(": ")[1]) for line in file_content]

# The puzzle's examples use a weaker player
player_hp, player_mana = (10, 250) if "example" in sys.argv[1] else (50, 500)


def apply_effects(mana, boss_hp, shield, poison, recharge):
    armor = 7 if shield > 0 else 0
    if poison > 0: boss_hp -= 3
    if recharge > 0: mana += 101
    return mana, boss_hp, max(shield - 1, 0), max(poison - 1, 0), max(recharge - 1, 0), armor


def cast_spells(hp, mana, boss_hp, shield, poison, recharge):
    # Every spell that can be cast now: (cost, hp, boss_hp, shield, poison, recharge)
    options = [
        (53, hp, boss_hp - 4, shield, poison, recharge),      # Magic Missile
        (73, hp + 2, boss_hp - 2, shield, poison, recharge),  # Drain
    ]
    if shield == 0: options.append((113, hp, boss_hp, 6, poison, recharge))
    if poison == 0: options.append((173, hp, boss_hp, shield, 6, recharge))
    if recharge == 0: options.append((229, hp, boss_hp, shield, poison, 5))
    return [option for option in options if option[0] <= mana]


def least_mana(player_hp, player_mana, boss_hp, boss_damage, hard=False) -> int:
    # Dijkstra: always continue from the fight that has spent the least mana so far,
    # so the first won fight taken from the queue is the cheapest one
    queue = [(0, player_hp, player_mana, boss_hp, 0, 0, 0)]
    seen = set()
    while queue:
        state = heapq.heappop(queue)
        spent, hp, mana, boss, shield, poison, recharge = state
        if boss <= 0: return spent
        if state in seen: continue
        seen.add(state)

        # Player turn
        if hard:
            # Part 2: lose 1 HP at the start of each player turn, before effects
            hp -= 1
            if hp <= 0: continue

        mana, boss, shield, poison, recharge, _ = apply_effects(mana, boss, shield, poison, recharge)
        if boss <= 0:
            heapq.heappush(queue, (spent, hp, mana, boss, shield, poison, recharge))
            continue

        for cost, new_hp, new_boss, new_shield, new_poison, new_recharge in cast_spells(hp, mana, boss, shield, poison, recharge):
            # Boss turn
            new_mana, new_boss, new_shield, new_poison, new_recharge, armor = apply_effects(
                mana - cost, new_boss, new_shield, new_poison, new_recharge
            )
            if new_boss > 0:
                new_hp -= max(1, boss_damage - armor)
                if new_hp <= 0: continue
            heapq.heappush(queue, (spent + cost, new_hp, new_mana, new_boss, new_shield, new_poison, new_recharge))


part_1_res = least_mana(player_hp, player_mana, boss_hp, boss_damage)
part_2_res = least_mana(player_hp, player_mana, boss_hp, boss_damage, hard=True)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
