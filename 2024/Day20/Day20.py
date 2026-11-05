import sys
from collections import Counter

file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

track = set()
for x, line in enumerate(file_content):
    for y, char in enumerate(line):
        if char != "#":
            track.add((x, y))
        if char == "S":
            start_pos = (x, y)
        elif char == "E":
            end_pos = (x, y)

# There is a single path from S to E, so walk it and store how many
# picoseconds it takes to reach every tile of the track
distance = {start_pos: 0}
current = start_pos
while current != end_pos:
    x, y = current
    current = next(
        pos for pos in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if pos in track and pos not in distance
    )
    distance[current] = len(distance)


def cheat_savings(max_cheat: int) -> Counter:
    # A cheat goes in a straight line through walls from one track tile to
    # another one at most max_cheat moves away (Manhattan distance). It saves
    # the part of the track it skips minus the moves the cheat itself takes.
    savings = Counter()
    for (x, y), dist in distance.items():
        for dx in range(-max_cheat, max_cheat + 1):
            for dy in range(-(max_cheat - abs(dx)), max_cheat - abs(dx) + 1):
                target = (x + dx, y + dy)
                if target in distance:
                    saved = distance[target] - dist - abs(dx) - abs(dy)
                    if saved > 0:
                        savings[saved] += 1
    return savings


savings = cheat_savings(2)
# The breakdown is only readable (and comparable with the statement) for the example
if len(file_content) <= 20:
    for saved, count in sorted(savings.items()):
        print(f"There are {count} cheats that save {saved} picoseconds")

part_1_res = sum(count for saved, count in savings.items() if saved >= 100)
print(f"Part 1 res: {part_1_res}")

# Part 2: cheats can now last up to 20 picoseconds
savings = cheat_savings(20)
if len(file_content) <= 20:
    for saved, count in sorted(savings.items()):
        if saved >= 50:
            print(f"There are {count} cheats that save {saved} picoseconds")

part_2_res = sum(count for saved, count in savings.items() if saved >= 100)
print(f"Part 2 res: {part_2_res}")
