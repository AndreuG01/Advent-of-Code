import sys
import re
from functools import cache
from itertools import combinations


lights_regex = re.compile(r'\[([.#]+)\]')
button_regex = re.compile(r'\(([\d,]+)\)')
joltage_regex = re.compile(r'\{([\d,]+)\}')


def parse_line(line: str) -> tuple[tuple[int, ...], list[tuple[int, ...]], tuple[int, ...]]:
    lights = tuple(1 if char == "#" else 0 for char in lights_regex.search(line).group(1))
    buttons = [tuple(int(num) for num in match.group(1).split(",")) for match in button_regex.finditer(line)]
    joltage = tuple(int(num) for num in joltage_regex.search(line).group(1).split(","))
    return lights, buttons, joltage


def press_patterns(buttons: list[tuple[int, ...]], num_counters: int) -> dict[tuple[int, ...], dict[tuple[int, ...], int]]:
    # Pressing a button twice is the same as not pressing it for the lights, so
    # every useful combination presses each button at most once. For each subset
    # of buttons store how much it adds to every counter, grouped by the on/off
    # pattern (parity) it leaves the lights in. Only the cheapest subset per
    # increment vector is kept.
    patterns = {}
    for num_pressed in range(len(buttons) + 1):
        for subset in combinations(buttons, num_pressed):
            increments = [0] * num_counters
            for button in subset:
                for counter in button:
                    increments[counter] += 1
            increments = tuple(increments)
            parity = tuple(inc % 2 for inc in increments)
            patterns.setdefault(parity, {}).setdefault(increments, num_pressed)
    return patterns


def min_presses_lights(lights: tuple[int, ...], patterns) -> int:
    return min(patterns[lights].values())


def min_presses_joltage(joltage: tuple[int, ...], patterns) -> int:
    # Any valid solution presses each button some number of times n = 2k + b
    # with b in {0, 1}. The buttons pressed an odd number of times (b = 1) must
    # produce the parity of the target; once they are subtracted, everything
    # left is pressed an even number of times, so we can halve the target and
    # solve the same problem again (each press there counts twice).
    @cache
    def solve(target: tuple[int, ...]) -> float:
        if not any(target):
            return 0
        parity = tuple(t % 2 for t in target)
        best = float("inf")
        for increments, cost in patterns.get(parity, {}).items():
            if any(inc > t for inc, t in zip(increments, target)):
                continue
            half = tuple((t - inc) // 2 for t, inc in zip(target, increments))
            best = min(best, cost + 2 * solve(half))
        return best

    return solve(joltage)


file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

part_1_res = 0
part_2_res = 0
for line in file_content:
    lights, buttons, joltage = parse_line(line)
    patterns = press_patterns(buttons, len(joltage))
    part_1_res += min_presses_lights(lights, patterns)
    part_2_res += min_presses_joltage(joltage, patterns)

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
