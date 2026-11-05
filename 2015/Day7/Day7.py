import sys
from functools import cache

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

MASK = 0xFFFF  # signals are 16-bit

# Instructions are not in order, so first store how each wire is computed,
# then resolve wires recursively (memoized) when asked for.
circuit = {}
for line in file_content:
    expr, dest = line.split(" -> ")
    circuit[dest] = expr.split(" ")


@cache
def signal(operand: str) -> int:
    if operand.isnumeric():
        return int(operand)

    operation = circuit[operand]
    if len(operation) == 1:
        # e.g. "123 -> x" or "lx -> a"
        return signal(operation[0])
    if len(operation) == 2:
        # NOT x
        return ~signal(operation[1]) & MASK

    one, action, two = operation
    if action == "AND":
        return signal(one) & signal(two)
    elif action == "OR":
        return signal(one) | signal(two)
    elif action == "LSHIFT":
        return (signal(one) << int(two)) & MASK
    elif action == "RSHIFT":
        return signal(one) >> int(two)
    raise ValueError(f"Unknown action: {action}")


if "a" in circuit:
    part_1_res = signal("a")

    # Part 2: override wire b with part 1's signal, reset all wires and rerun
    circuit["b"] = [str(part_1_res)]
    signal.cache_clear()
    part_2_res = signal("a")
else:
    # The example has no wire "a": show every wire instead
    for wire in sorted(circuit):
        print(f"{wire}: {signal(wire)}")


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
