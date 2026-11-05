import sys

file_content = open(sys.argv[1]).read().strip()
schematics = [block.splitlines() for block in file_content.split("\n\n")]

locks = []
keys = []
for schematic in schematics:
    # Height of each column, not counting the full row at the top (locks) or
    # at the bottom (keys)
    heights = [sum(row[col] == "#" for row in schematic) - 1 for col in range(len(schematic[0]))]
    if schematic[0][0] == "#":
        locks.append(heights)
    else:
        keys.append(heights)

# The space a pin and a key can share is everything between the top and bottom rows
space = len(schematics[0]) - 2

part_1_res = sum(
    all(pin + cut <= space for pin, cut in zip(lock, key))
    for lock in locks
    for key in keys
)

print(f"Part 1 res: {part_1_res}")
