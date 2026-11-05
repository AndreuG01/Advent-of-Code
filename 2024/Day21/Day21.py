import sys
from functools import cache

file_content = open(sys.argv[1]).read().strip()
codes = file_content.splitlines()

# (row, col) of every button; None marks the gap the arms must never point at
numeric_keypad = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    None: (3, 0), "0": (3, 1), "A": (3, 2),
}
directional_keypad = {
    None: (0, 0), "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2),
}


def candidate_moves(keypad: dict, start: str, end: str) -> list[str]:
    # Changing direction as few times as possible is always best, so only try
    # all horizontal moves then all vertical ones, or the other way round,
    # skipping whichever order would sweep the arm over the gap
    (r1, c1), (r2, c2) = keypad[start], keypad[end]
    horizontal = (">" if c2 > c1 else "<") * abs(c2 - c1)
    vertical = ("v" if r2 > r1 else "^") * abs(r2 - r1)
    gap = keypad[None]

    moves = []
    if (r1, c2) != gap:
        moves.append(horizontal + vertical + "A")
    if (r2, c1) != gap:
        moves.append(vertical + horizontal + "A")
    return moves


@cache
def presses(sequence: str, robots: int, numeric: bool = False) -> int:
    # Fewest presses on my own keypad needed for the robot `robots` levels
    # away to type `sequence`. Every arm starts on A and goes back to A after
    # each press it makes, so each move can be solved independently.
    if robots == 0:
        return len(sequence)
    keypad = numeric_keypad if numeric else directional_keypad
    total = 0
    for start, end in zip("A" + sequence, sequence):
        total += min(presses(moves, robots - 1) for moves in candidate_moves(keypad, start, end))
    return total


def total_complexity(robots: int) -> int:
    total = 0
    for code in codes:
        length = presses(code, robots, numeric=True)
        print(f"{code}: {length} * {int(code[:-1])}")
        total += length * int(code[:-1])
    return total


# The robot at the door plus the two robots on directional keypads
part_1_res = total_complexity(3)
print(f"Part 1 res: {part_1_res}")

# Part 2: the robot at the door plus 25 robots on directional keypads. The
# cache keeps this fast since every move only depends on the two buttons
# involved and the number of robots left.
part_2_res = total_complexity(26)
print(f"Part 2 res: {part_2_res}")
