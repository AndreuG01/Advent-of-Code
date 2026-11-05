import sys
import random

file_content = open(sys.argv[1]).read().strip()
values_section, gates_section = file_content.split("\n\n")

wires = {}
for line in values_section.splitlines():
    name, value = line.split(": ")
    wires[name] = int(value)

# output wire -> (input a, operation, input b)
gates = {}
for line in gates_section.splitlines():
    a, op, b, _, out = line.split()
    gates[out] = (a, op, b)

operations = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}


def value(wire: str) -> int:
    # There are no loops, so a wire's value can be worked out by first working
    # out the inputs of the gate that drives it
    if wire not in wires:
        a, op, b = gates[wire]
        wires[wire] = operations[op](value(a), value(b))
    return wires[wire]


# z00 is the least significant bit
z_wires = sorted((wire for wire in gates if wire.startswith("z")), reverse=True)
bits = "".join(str(value(wire)) for wire in z_wires)
print(f"Output bits: {bits}")

part_1_res = int(bits, 2)
print(f"Part 1 res: {part_1_res}")

# Part 2: the circuit should be a ripple-carry adder, where every bit i > 0
# is built from the same five gates:
#   x_i XOR y_i -> partial          x_i AND y_i -> direct carry
#   partial XOR carry_in -> z_i     partial AND carry_in -> chained carry
#   direct carry OR chained carry -> carry_out
# A swapped output wire breaks that pattern, so look for gates whose output
# isn't used the way its type requires.
x_wires = sorted(wire for wire in wires if wire.startswith("x"))
last_z = f"z{len(x_wires):02d}"


def is_input(wire: str) -> bool:
    return wire[0] in "xy"


def first_bit(a: str, b: str) -> bool:
    return {a, b} == {"x00", "y00"}


# wire -> operations of the gates that read it
readers = {}
for out, (a, op, b) in gates.items():
    readers.setdefault(a, set()).add(op)
    readers.setdefault(b, set()).add(op)


def find_suspects() -> set[str]:
    suspects = set()
    for out, (a, op, b) in gates.items():
        # Every output bit is an XOR except the last one, which is the final carry
        if out.startswith("z") and out != last_z and op != "XOR":
            suspects.add(out)
        if out == last_z and op != "OR":
            suspects.add(out)
        # An XOR of two internal wires can only be the one producing a z bit
        if op == "XOR" and not is_input(a) and not out.startswith("z"):
            suspects.add(out)
        # The partial sum of x_i and y_i has to go into the XOR of the next level
        if op == "XOR" and is_input(a) and not first_bit(a, b) and "XOR" not in readers.get(out, set()):
            suspects.add(out)
        # Both carry halves are only combined by an OR (except bit 0, whose
        # carry goes straight into bit 1)
        if op == "AND" and not first_bit(a, b) and readers.get(out, set()) != {"OR"}:
            suspects.add(out)
    return suspects


def add(gates: dict, x: int, y: int) -> int | None:
    values = {}
    for i in range(len(x_wires)):
        values[f"x{i:02d}"] = x >> i & 1
        values[f"y{i:02d}"] = y >> i & 1

    def evaluate(wire: str, depth: int = 0) -> int | None:
        # A bad swap can create a loop, which a correct adder never has
        if wire not in values:
            if depth > len(gates):
                return None
            a, op, b = gates[wire]
            value_a, value_b = evaluate(a, depth + 1), evaluate(b, depth + 1)
            if value_a is None or value_b is None:
                return None
            values[wire] = operations[op](value_a, value_b)
        return values[wire]

    total = 0
    for i in range(len(x_wires) + 1):
        bit = evaluate(f"z{i:02d}")
        if bit is None:
            return None
        total |= bit << i
    return total


def pairings(items: list[str]):
    # Every way of splitting the wires into pairs
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for i, other in enumerate(rest):
        for pairs in pairings(rest[:i] + rest[i + 1:]):
            yield [(first, other)] + pairs


def adds_correctly(gates: dict) -> bool:
    rng = random.Random(0)
    limit = (1 << len(x_wires)) - 1
    tests = [(limit, 1), (limit, limit), (0, 0)] + [(rng.randint(0, limit), rng.randint(0, limit)) for _ in range(30)]
    return all(add(gates, x, y) == x + y for x, y in tests)


# An adder has one output bit per input bit plus the final carry; the
# examples don't, so there's nothing to fix in them
z_count = sum(wire.startswith("z") for wire in gates)
if z_count != len(x_wires) + 1:
    print("Part 2: this circuit isn't an adder")
else:
    suspects = sorted(find_suspects())
    print(f"Suspicious wires: {suspects}")

    # Double check the suspects by finding the swaps that make it add correctly
    for pairs in pairings(suspects):
        swapped = dict(gates)
        for a, b in pairs:
            swapped[a], swapped[b] = gates[b], gates[a]
        if adds_correctly(swapped):
            print(f"Swaps: {pairs}")
            part_2_res = ",".join(suspects)
            print(f"Part 2 res: {part_2_res}")
            break
    else:
        print("Part 2: no pairing of the suspicious wires makes the circuit add correctly")
